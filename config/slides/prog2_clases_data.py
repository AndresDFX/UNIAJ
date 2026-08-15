# -*- coding: utf-8 -*-
"""Contenido pedagogico de Programacion II 2026-2 (PI VetCare, Java).

Fuente unica de la que `build_uniajc_prog2_all.py` genera slides, guiones,
talleres, quices, soluciones y codigo. Alineado al plan 2026-2:
las clases 5, 10 y 15 son de parcial (solo evaluacion, sin tema nuevo).

Para cambiar el contenido de una clase se edita AQUI y se regenera; no se
editan los .docx/.pptx a mano.
"""

CLASES = [
    {
        "n": 1,
        "slug": "Introduccion a POO",
        "titulo": "Introduccion a la Programacion Orientada a Objetos",
        "subtitulo": "Clase vs objeto y los cuatro pilares",
        "herramienta": "Apache NetBeans",
        "hito_pi": "Entorno de desarrollo listo y la primera clase del dominio VetCare escrita",
        "entregable": "Proyecto NetBeans con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos",
        "demo": "Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde",
        "teoria": [
            "Antes de la POO un programa era una lista de procedimientos que operaban sobre datos sueltos. Cuando el programa crecia, nadie sabia que funcion tocaba que dato, y un cambio pequeno rompia cosas en lugares inesperados. La POO propone lo contrario: juntar en una sola unidad, el objeto, los datos y las operaciones que los manipulan. El programa deja de ser una receta y pasa a ser un conjunto de piezas que se hablan entre si. En VetCare, en vez de tener por un lado un arreglo de nombres y por otro un arreglo de edades que hay que mantener sincronizados a mano, se tiene una clase Mascota que guarda juntos su nombre, su especie y su edad.",
            "La distincion que mas cuesta el primer dia es clase contra objeto. La clase es el molde; el objeto es la pieza fabricada con ese molde. Mascota es la clase: define que toda mascota tiene nombre, especie y edad. La variable luna es un objeto: una mascota concreta, con nombre Luna, especie Canino, edad 3. De una misma clase se crean tantos objetos como haga falta, cada uno con sus propios valores. La analogia que funciona en clase es el plano de una casa (la clase) frente a las casas construidas con ese plano (los objetos): cada casa puede estar pintada de distinto color, pero todas tienen la misma estructura.",
            "Los cuatro pilares se entienden por el problema que resuelve cada uno. Abstraccion es quedarse solo con lo que importa del problema: para la clinica Huellitas, de una mascota importa su especie y su historial, no su color favorito; modelar es decidir que se ignora. Encapsulamiento es que los datos de un objeto no se tocan directamente desde afuera sino a traves de metodos: el atributo va private y se expone con getters y setters, de modo que el objeto pueda validar (por ejemplo, rechazar una edad negativa) en vez de quedar a merced de quien lo use.",
            "Herencia es que una clase puede extender a otra y reutilizar lo que ya define: Perro extends Mascota hereda nombre y edad, y agrega lo suyo. Advertencia importante: la herencia se sobreusa, y solo aplica cuando de verdad hay una relacion 'es un' (un perro ES una mascota); si la relacion es 'tiene un', no es herencia sino composicion. Polimorfismo es que el mismo mensaje produce comportamientos distintos segun el objeto que lo recibe: si Perro y Gato heredan de Mascota y ambos redefinen hacerSonido(), recorrer una lista de mascotas y llamar ese metodo produce Guau o Miau segun el objeto real, sin que el codigo que recorre la lista necesite saber de que tipo es cada una.",
            "El constructor es el metodo que se ejecuta al crear el objeto y deja sus atributos en un estado valido. La instruccion new Mascota(\"Luna\", \"Canino\", 3) reserva memoria y llama al constructor. Si no se escribe ninguno, Java agrega uno vacio por defecto, y ahi es donde aparecen objetos a medio inicializar que despues fallan con NullPointerException en el peor momento. Por eso desde la primera clase se escribe el constructor completo.",
            "Error tipico del docente que no domina el tema: presentar los cuatro pilares como cuatro definiciones que hay que memorizar. El estudiante los aprende cuando ve el problema que cada uno resuelve, no cuando los recita; por eso hoy solo se introducen con un ejemplo concreto de VetCare y se profundizan en las clases siguientes. El segundo tropiezo es olvidar sobreescribir toString(): al imprimir un objeto sale algo como vetcare.Mascota@6d06d69c y medio grupo cree que el programa fallo."
        ],
        "taller": [
            "Instale y verifique el entorno (JDK + Apache NetBeans) y cree un proyecto Java Application llamado VetCare con paquete vetcare. Este paso es el objetivo real del bloque: nadie puede quedarse sin entorno funcionando.",
            "Escriba la clase Mascota con al menos tres atributos privados (id, nombre, especie) y un constructor que los reciba todos.",
            "Agregue al menos un getter y sobreescriba toString() para que la mascota se imprima de forma legible.",
            "En el main, cree DOS objetos Mascota con datos distintos e imprimalos: debe verse que salen del mismo molde pero con valores diferentes.",
            "Si termina antes: agregue un setter que valide (por ejemplo, que rechace una edad negativa) y pruebelo desde el main."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ la clase Mascota que escriba hoy es la semilla de todo VetCare; las clases siguientes se apoyan en ella.",
            "Sin entorno funcionando no se puede avanzar en ninguna sesion posterior: por eso hoy se resuelve.",
            "El diagnostico de hoy no tiene nota: sirve para calibrar el ritmo de las proximas clases."
        ],
        "escenario": [
            "Dominio: clinica veterinaria Huellitas, que hoy lleva toda su gestion en papel.",
            "Herramienta: Apache NetBeans con JDK instalado.",
            "Se parte de cero: no hay codigo previo del proyecto."
        ],
        "criterios": [
            "El proyecto compila y ejecuta sin errores en NetBeans.",
            "La clase Mascota tiene atributos private y un constructor que los inicializa todos.",
            "El main crea dos objetos distintos de la misma clase.",
            "Al imprimir una mascota se ve texto legible, no vetcare.Mascota@6d06d69c."
        ],
        "pistas": [
            "¿Los atributos quedaron private o los deje accesibles desde fuera?",
            "¿El constructor inicializa TODOS los atributos?",
            "¿Sobreescribi toString() o estoy imprimiendo la direccion de memoria?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. En NetBeans: File > New Project > Java with Ant > Java Application, nombre VetCare, marcando Create Main Class con paquete vetcare. Si NetBeans reclama que no encuentra el JDK, se apunta en Tools > Java Platforms. Este es el paso que mas tiempo consume el primer dia: conviene circular por los puestos en vez de avanzar.",
            "Paso 2 resuelto. La clase queda: public class Mascota { private String id; private String nombre; private String especie; public Mascota(String id, String nombre, String especie) { this.id = id; this.nombre = nombre; this.especie = especie; } }. El this. distingue el atributo del parametro que tiene el mismo nombre; sin el, el atributo queda en null.",
            "Paso 3 resuelto. El getter es public String getNombre() { return nombre; } y el toString queda: @Override public String toString() { return id + \" - \" + nombre + \" (\" + especie + \")\"; }. La anotacion @Override no es obligatoria, pero avisa en compilacion si uno escribe mal el nombre del metodo (por ejemplo toSting).",
            "Paso 4 resuelto. En el main: Mascota luna = new Mascota(\"M-001\", \"Luna\", \"Canino\"); Mascota michi = new Mascota(\"M-002\", \"Michi\", \"Felino\"); System.out.println(luna); System.out.println(michi); Deben salir dos lineas distintas: ahi se ve, sin explicarlo, la diferencia entre clase (el molde) y objeto (cada mascota concreta)."
        ],
        "solucion_rubrica": [
            "Entorno funcionando (3)",
            "Clase Mascota con atributos private (3)",
            "Constructor completo con this. (2)",
            "Dos objetos distintos impresos legiblemente (2)"
        ],
        "solucion_errores": [
            "Dejar los atributos public 'para que sea mas facil': rompe el encapsulamiento desde el primer dia y despues cuesta corregirlo.",
            "Olvidar el this. en el constructor: el atributo queda en null y el programa falla con NullPointerException al imprimir.",
            "No sobreescribir toString(): imprime la direccion de memoria y el estudiante cree que el programa fallo."
        ],
        "codigo_slide_titulo": "La primera clase de VetCare",
        "codigo_slide_lineas": [
            "public class Mascota {",
            "    private String id;          // private = nadie lo toca desde afuera",
            "    private String nombre;",
            "    private String especie;",
            "",
            "    public Mascota(String id, String nombre, String especie) {",
            "        this.id = id;           // this. distingue atributo de parametro",
            "        this.nombre = nombre;",
            "        this.especie = especie;",
            "    }",
            "",
            "    @Override",
            "    public String toString() {  // sin esto se imprime vetcare.Mascota@6d06d69c",
            "        return id + \" - \" + nombre + \" (\" + especie + \")\";",
            "    }",
            "}"
        ],
        "codigo_slide_caption": "La clase es el molde; cada new Mascota(...) fabrica un objeto distinto con ese molde.",
        "codigo_archivo": "Mascota.java",
        "codigo_fuente": "package vetcare;\n\n/**\n * VetCare - Clinica Veterinaria Huellitas\n * Clase 1: primera clase del dominio. Es el molde a partir del cual se crean\n * los objetos Mascota; todo el proyecto se apoya en ella.\n */\npublic class Mascota {\n\n    private String id;\n    private String nombre;\n    private String especie;\n    private int edad;\n\n    public Mascota(String id, String nombre, String especie, int edad) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n        this.edad = edad;\n    }\n\n    public String getId() { return id; }\n    public String getNombre() { return nombre; }\n    public String getEspecie() { return especie; }\n    public int getEdad() { return edad; }\n\n    /** El objeto se defiende: una edad negativa no tiene sentido en el dominio. */\n    public void setEdad(int edad) {\n        if (edad < 0) {\n            System.out.println(\"Edad invalida, se conserva la anterior: \" + this.edad);\n            return;\n        }\n        this.edad = edad;\n    }\n\n    @Override\n    public String toString() {\n        return id + \" - \" + nombre + \" (\" + especie + \", \" + edad + \" anios)\";\n    }\n\n    public static void main(String[] args) {\n        Mascota luna = new Mascota(\"M-001\", \"Luna\", \"Canino\", 3);\n        Mascota michi = new Mascota(\"M-002\", \"Michi\", \"Felino\", 5);\n        System.out.println(\"Pacientes registrados hoy en Huellitas:\");\n        System.out.println(luna);\n        System.out.println(michi);\n        luna.setEdad(-2);\n    }\n}\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "¿Cual es la diferencia entre una clase y un objeto?",
                "opciones": [
                    "A) Son sinonimos en Java",
                    "B) La clase es el molde; el objeto es una pieza concreta creada con ese molde",
                    "C) El objeto es el molde y la clase la instancia",
                    "D) La clase solo existe en tiempo de ejecucion"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "En VetCare, declarar los atributos de Mascota como private corresponde al pilar de:",
                "opciones": [
                    "A) Herencia",
                    "B) Polimorfismo",
                    "C) Encapsulamiento",
                    "D) Abstraccion"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Si no se escribe un constructor, Java agrega uno vacio por defecto.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Usar herencia siempre es mejor diseno que usar composicion.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Al imprimir un objeto sale 'vetcare.Mascota@6d06d69c'. Esto significa que:",
                "opciones": [
                    "A) El programa fallo y hay que reiniciar NetBeans",
                    "B) Falta sobreescribir el metodo toString()",
                    "C) El objeto quedo en null",
                    "D) El constructor no se ejecuto"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Abstraer es decidir que caracteristicas del problema real se ignoran en el modelo.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Escriba la firma del constructor de su clase Mascota.",
                "clave": "Ej: public Mascota(String id, String nombre, String especie, int edad). Debe recibir e inicializar todos los atributos usando this."
            },
            {
                "tipo": "abierta",
                "q": "Si Perro y Gato heredan de Mascota y ambos redefinen hacerSonido(), ¿que pilar se usa y que ventaja da?",
                "clave": "Polimorfismo. Permite recorrer una lista de Mascota y llamar hacerSonido() sin que el codigo necesite saber de que tipo concreto es cada objeto."
            }
        ],
        "fundamento": "En Programacion I el estudiante trabajo con programacion estructurada: los datos por un lado y las funciones por otro. Vale la pena hacer visible el limite de ese enfoque con el mismo dominio del proyecto antes de nombrar la palabra objeto. Para registrar mascotas en la clinica se declaraban arreglos paralelos: String[] nombres, String[] especies, int[] edades, y la mascota numero cinco era la casilla cinco de los tres arreglos al mismo tiempo. Eso funciona en un ejercicio de veinte lineas y se cae en cuanto el programa crece, por tres razones concretas. Ordenar la lista por nombre obliga a mover los tres arreglos en perfecta sincronia, y basta olvidar uno para que Luna quede con la edad de otro animal. Agregar un dato nuevo, por ejemplo si la mascota esta activa, obliga a abrir todas las funciones que reciben esos arreglos y agregarles un parametro. Y nada en el lenguaje impide que nombres tenga diez elementos y edades solo nueve: la consistencia depende de que todos los programadores se acuerden de mantenerla. La programacion orientada a objetos propone una unidad distinta: un tipo llamado Mascota que reune en un mismo lugar el estado, que son los datos de la mascota, y el comportamiento, que son las operaciones que se le pueden hacer. La ganancia no es estetica: agregar un dato pasa a ser una linea en un solo archivo, y la responsabilidad de mantener la consistencia queda dentro del tipo y no repartida en la cabeza del equipo.\n\nAhora el punto que decide el semestre, y por eso va temprano: que es un objeto en la memoria. En Java una variable local vive en la pila, una zona pequena y ordenada asociada al metodo que se esta ejecutando, mientras que el objeto creado con new vive en el monton, una zona grande donde el programa reserva espacio a medida que lo necesita. La consecuencia es que la variable no guarda el objeto: guarda una referencia, que es un valor que indica donde esta el objeto. La imagen que funciona en clase es que la variable es el control remoto y el objeto es el televisor: se pueden tener dos controles del mismo televisor, y apretar el boton en cualquiera de los dos cambia el mismo aparato. Escrito en el tablero: Mascota a = new Mascota(\"Luna\", \"Canino\", 3); despues Mascota b = a; despues b.setEdad(4); y finalmente System.out.println(a.getEdad()) imprime 4, aunque nadie toco la variable a. No hay dos mascotas, hay una con dos nombres. El contraste hay que hacerlo en el mismo tablero con tipos primitivos: int x = 3; int y = x; y = 5; y x sigue valiendo 3, porque ahi si se copio el valor. Java tiene exactamente ocho tipos primitivos (byte, short, int, long, float, double, char y boolean) y esa es regla dura del lenguaje: todo lo demas, incluido String, se maneja por referencia. De aqui se deriva un tercer hecho que conviene decir hoy aunque se practique despues: cuando se pasa un objeto a un metodo, el metodo puede modificar el objeto y quien llamo vera el cambio, pero si el metodo reasigna su parametro con un new, la variable de afuera no se enteran de nada.\n\nDe lo anterior sale la pregunta que aparece sin falta en las primeras semanas: por que mascota1 == mascota2 dice que son distintas si tienen los mismos datos. La respuesta es exacta y hay que darla asi: el operador == compara referencias, es decir pregunta si las dos variables apuntan al mismo objeto, no si los objetos se parecen. Dos objetos Mascota creados con new a partir de la misma linea de un archivo CSV son dos televisores identicos en fabrica y en habitaciones distintas: == devuelve false y esta bien, porque no son el mismo. Para comparar contenido existe el metodo equals, con una trampa que hay que enunciar: el equals que toda clase hereda de Object hace exactamente lo mismo que ==, asi que mientras usted no lo sobrescriba, equals tampoco compara contenido. Sobrescribirlo significa escribirlo en Mascota para que dos mascotas sean iguales cuando su identificador sea igual. Y viene una regla del lenguaje que no es opcional: si sobrescribe equals debe sobrescribir tambien hashCode, porque las estructuras que se veran en la Clase 4, HashMap y HashSet, ubican los objetos usando hashCode antes de compararlos, y dos objetos iguales que devuelven codigos distintos terminan guardados como si fueran diferentes. Un ultimo detalle que produce mucha confusion: con cadenas de texto escritas literalmente en el codigo, == a veces devuelve true porque Java reutiliza los literales identicos en una zona comun, pero new String(\"Luna\") == \"Luna\" devuelve false. Por eso la regla practica del curso es sin excepciones: con objetos nunca se usa ==, se usa equals; == se reserva para primitivos y para preguntar si algo es null.\n\nRecien ahora tiene sentido la analogia clasica. La clase es el molde y el objeto es la pieza fabricada con ese molde; el acto de fabricar se llama instanciar y se hace con new, y por eso objeto e instancia son sinonimos. Mascota es la clase: declara que toda mascota tiene nombre, especie y edad. La mascota con nombre Luna, especie Canino y edad 3 es una instancia. La analogia es util pero tiene tres limites que hay que decir en voz alta, porque el estudiante que se queda solo con la analogia la estira mal. Primero, un molde fisico no sabe cuantas piezas produjo, y una clase tampoco lleva por si sola la lista de sus objetos: si VetCare necesita saber cuantas mascotas se han creado, alguien tiene que programar ese conteo. Segundo, la clase no define solo la forma, define tambien el comportamiento: un plano de casa no cocina, mientras que Mascota si sabe calcular si esta al dia con sus vacunas. Tercero, existen miembros que pertenecen a la clase y no a cada objeto, y se marcan con la palabra static: un static int totalMascotas existe una sola vez aunque haya mil mascotas, y se lee como Mascota.totalMascotas y no como luna.totalMascotas. En VetCare el uso legitimo de hoy es generar el siguiente identificador con un contador compartido. Y conviene una advertencia que ahorra dolores: static es la puerta de regreso a la programacion estructurada, porque una clase llena de metodos static es un archivo de funciones con otro nombre; en la Clase 7 static reaparece con criterio al estudiar Singleton.\n\nEl encapsulamiento se ensena mal cuando se presenta como la orden de poner private y generar getters. Se ensena bien cuando se muestra el problema que resuelve, y en VetCare el problema tiene nombre. La clinica tiene una regla del proyecto: una mascota inactiva no puede agendar cita, y toda inactivacion debe quedar con motivo y fecha. Suponga que el atributo se declaro como public boolean activa. Entonces cualquier linea de cualquier archivo del sistema puede escribir luna.activa = false, y la afirmacion toda mascota inactiva tiene motivo y fecha de inactivacion, que es lo que llamamos una invariante porque debe ser verdadera durante toda la vida del objeto, se rompe sin dejar rastro. Peor todavia: para encontrar quien la rompio hay que revisar el proyecto completo, porque el compilador permite esa asignacion en cualquier parte. Si en cambio el atributo es private y la unica forma de apagarlo es el metodo inactivar(String motivo), que exige el motivo, guarda la fecha y deja registro, entonces existe un unico lugar en el mundo donde una mascota puede volverse inactiva. Lo mismo pasa con la edad: luna.edad = -3 es aceptado por el compilador sin una queja, mientras que un setEdad que lanza IllegalArgumentException cuando el valor es negativo detiene el error en el instante en que se comete y no tres pantallas despues. Y aqui va la parte honesta que casi nunca se dice: usar el atajo del entorno de desarrollo para generar getters y setters de los quince campos no es encapsular. Si existe un setActiva(boolean) publico, el campo sigue siendo publico con dos pasos extra. Encapsular es exponer operaciones del dominio, inactivar, agendar, aplicarVacuna, y no casillas. La pregunta del estudiante llega sola: si igual funciona con public, para que me complico. La respuesta concreta es que funciona hoy, con un archivo y con usted como unico autor; en la Clase 12, integrando modulos de tres companeros, quien escriba la pantalla de facturacion pondra activa en false por comodidad y usted perdera una tarde buscando por que las citas desaparecieron.\n\nEl constructor es la pieza que garantiza que el objeto nazca valido. Es un metodo especial que se llama igual que la clase, no declara tipo de retorno y se ejecuta una sola vez, en el momento de la creacion. La instruccion new hace dos cosas: reserva la memoria en el monton y llama al constructor. Si la clase no declara ninguno, Java agrega uno sin parametros; en el instante en que usted escribe un constructor con parametros, el vacio desaparece, y ese es literalmente el primer error de compilacion del curso cuando alguien sigue escribiendo new Mascota() en otro archivo. La responsabilidad del constructor es la validacion: si el nombre llega null o vacio, lanza; si la edad llega negativa, lanza; y como consecuencia, en todo el programa no puede existir una Mascota sin nombre. Eso elimina una familia entera de errores aguas abajo, porque nadie tendra que preguntarse mas adelante si el nombre podria estar vacio. El anti patron a evitar es el constructor vacio seguido de cinco setters: permite que exista un objeto a medio llenar que viajara hasta la interfaz grafica de la Clase 4 y fallara alli, a doscientas lineas del lugar donde en realidad se creo mal, que es el peor escenario de depuracion posible. Como convencion, no como regla, si un constructor pide mas de cuatro o cinco parametros es senal de que la clase esta juntando cosas que no pertenecen al mismo concepto.\n\nQueda el error mas frecuente de Java, y hay que nombrarlo hoy porque su causa es todo lo anterior. null significa que la referencia no apunta a ningun objeto: es un control remoto sin televisor. No es cero, no es cadena vacia y no es un objeto con los campos en blanco; es la ausencia de destino. NullPointerException es lo que ocurre cuando el programa intenta usar esa referencia, por ejemplo llamando un metodo o leyendo un campo. Los tres casos que produciran esa excepcion en VetCare son predecibles: un metodo buscarMascota(id) que devuelve null cuando no encuentra nada y un llamador que hace m.getNombre() sin preguntar; una Cita cuya Mascota nunca se asigno; y una lista declarada pero no inicializada. Dato citable: Tony Hoare introdujo la referencia nula en 1965 y en una conferencia de 2009 la llamo publicamente su error de mil millones de dolares. Las encuestas y los reportes de errores en produccion la ubican de forma consistente como la excepcion mas frecuente en aplicaciones Java, y conviene presentarlo asi, como observacion de la industria y no como ley. Las defensas, en orden de utilidad real: validar en el constructor para que no nazcan objetos incompletos; nunca devolver null en un metodo que devuelve una coleccion, sino una lista vacia; usar Optional cuando la ausencia es un resultado legitimo de una busqueda; y leer el mensaje de la excepcion, porque desde Java 14 el mensaje indica cual variable exacta era null. Pregunta previsible: entonces le pongo cadena vacia y listo. No: eso no resuelve el problema, lo esconde, y cambia una excepcion clara por un dato falso guardado en el archivo de la Clase 9.\n\nEl entorno cierra la clase y tiene dos reglas duras que producen el noventa por ciento de los tropiezos del primer dia. El JDK debe estar instalado en una version de soporte extendido, 17 o 21, y se verifica con java -version en la consola, no confiando en la pantalla del instalador; y un archivo .java contiene una clase publica cuyo nombre coincide caracter por caracter con el nombre del archivo, mayusculas incluidas, de modo que la clase Mascota vive en Mascota.java y en ningun otro lugar. El comando javac compila a un archivo .class con bytecode y java lo ejecuta; el entorno de desarrollo hace ambas cosas por dentro, y verlo una vez en consola evita que el estudiante crea que Java es el boton verde del IDE. El amarre con la Clase 2 conviene decirlo explicito al cerrar: hoy quedaron mascota1, mascota2 y mascota3 como variables sueltas, y eso no escala a una clinica con cuatrocientos pacientes, asi que la proxima clase entra ArrayList de Mascota. Todo lo de hoy se vuelve indispensable ahi: la lista guarda referencias y no copias, de modo que modificar el objeto cambia lo que la lista muestra; los metodos contains e indexOf usan equals, asi que sin sobrescribirlo la busqueda por identificador fallara sin dar error; y en la Clase 9, al guardar en CSV, hara falta un constructor que reciba una linea de texto y valide, es decir el mismo constructor de hoy. La Clase 13 formalizara con try-catch lo que hoy se hizo a mano lanzando IllegalArgumentException.\n\nError tipico del docente que no domina el tema: el primero es explicar el objeto como una variable que agrupa datos y dibujarlo en el tablero dentro de la variable, sin la flecha de la referencia. Es comodo y parece suficiente el primer dia, pero deja al grupo sin modelo mental: cuando en la Clase 2 dos posiciones de la lista apunten al mismo objeto, o cuando un metodo modifique la mascota que recibio, el estudiante no podra explicar por que cambio algo que el no toco, y atribuira al azar o a un supuesto error de Java lo que en la Clase 12 se convertira en errores de estado compartido durante la integracion. El segundo es presentar el encapsulamiento como el procedimiento de poner private y pedirle al entorno que genere getters y setters. El estudiante entrega entonces clases con quince setters publicos, cero validaciones y ninguna operacion del dominio, con lo cual la regla de que una mascota inactiva no agenda cita queda escrita a mano en cada pantalla; en la revision cruzada de la Clase 11 apareceran tres versiones distintas de la misma regla y ninguna sera la oficial."
    },
    {
        "n": 2,
        "slug": "Colecciones dinamicas ArrayList",
        "titulo": "Colecciones dinamicas · ArrayList",
        "subtitulo": "De arreglos fijos a listas que crecen",
        "herramienta": "Apache NetBeans",
        "hito_pi": "El registro de mascotas de VetCare deja de vivir en un arreglo de tamano fijo y pasa a un ArrayList<Mascota> que crece con la clinica.",
        "entregable": "Proyecto NetBeans con las clases Mascota y RegistroMascotas y un menu de consola que agrega, lista, busca por ID y elimina mascotas, comprimido y subido a ExamLab.",
        "demo": "El docente muestra un Mascota[3] que revienta al intentar guardar la cuarta ficha y luego el mismo caso resuelto con ArrayList, imprimiendo size() despues de cada operacion.",
        "teoria": [
            "Empecemos por el problema real de Huellitas. Hoy la clinica guarda las fichas de las mascotas en una carpeta de carton con 50 separadores; cuando llega la mascota 51 toca comprar otra carpeta y volver a organizar todo. En Java eso mismo es un arreglo: cuando usted escribe Mascota[] fichero = new Mascota[50] esta pidiendole a la maquina un bloque de memoria contiguo con exactamente 50 casillas, y ese numero queda grabado en piedra para toda la vida del objeto. El arreglo no tiene metodo para crecer, solo tiene el atributo length, que es de solo lectura; si quiere 80 casillas debe crear otro arreglo mas grande, copiar una por una las 50 fichas viejas y reasignar la variable. Un arreglo es rapidisimo y perfectamente valido cuando usted sabe de antemano cuantos elementos va a tener (los 7 dias de la semana, los 12 meses), pero es una pesima idea para algo que crece todos los dias, como el numero de pacientes de una veterinaria que apenas esta digitalizando su operacion.",
            "Un ArrayList es exactamente esa carpeta que se agranda sola, y aqui viene lo importante: por dentro tambien es un arreglo. La clase ArrayList guarda un arreglo interno oculto (llamado elementData) y lleva dos numeros distintos: la capacidad, que es cuantas casillas tiene el arreglo interno, y el tamano, que es cuantos elementos usted realmente guardo. Cuando usted hace add y el arreglo interno se llena, ArrayList crea silenciosamente uno nuevo aproximadamente 1.5 veces mas grande, copia todo con Arrays.copyOf y sigue como si nada; usted nunca se entera. Esa arquitectura explica el rendimiento: get(i) es instantaneo porque salta directo a la posicion i del arreglo interno, agregar al final es barato casi siempre, pero add(0, mascota) o remove(0) obligan a correr un puesto a todos los demas elementos. En VetCare eso significa que agregar la mascota nueva al final del registro no cuesta nada, mientras que borrar siempre la primera ficha de una lista de 5.000 pacientes es la operacion mas cara que usted puede pedir.",
            "La interfaz de trabajo es corta y hay que dominarla de memoria. Se declara asi: List<Mascota> mascotas = new ArrayList<>(); el List<Mascota> del lado izquierdo es la interfaz (el contrato) y el ArrayList<> del lado derecho es la implementacion concreta. Los metodos que usaremos toda la clase son add(objeto) para agregar al final, get(indice) para leer la posicion indicada, size() para saber cuantos hay, remove(indice) o remove(objeto) para sacar, set(indice, objeto) para reemplazar, isEmpty(), contains(objeto) e indexOf(objeto). El <Mascota> entre los picos se llama generico y no es decoracion: le dice al compilador que ahi solo entran Mascotas, de modo que si un estudiante intenta guardar un String el error aparece al compilar y no como un ClassCastException en plena sustentacion. Ojo con un detalle fino que confunde a todo el mundo: contains e indexOf comparan usando equals, asi que si usted no sobreescribe equals en Mascota, dos objetos con el mismo ID pero creados por separado seran considerados diferentes; por eso en VetCare buscamos por ID recorriendo la lista y comparando m.getId().equalsIgnoreCase(id).",
            "Recorrer la lista tiene dos formas y cada una tiene su momento. El for clasico con indice (for (int i = 0; i < mascotas.size(); i++)) se usa cuando usted necesita el numero de la posicion, por ejemplo para imprimir el listado numerado de la sala de espera. El for-each (for (Mascota m : mascotas)) se usa cuando solo va a leer, es mas limpio y es el que debe volverse su reflejo. Ahora la trampa que se lleva por delante a media clase: si usted borra un elemento dentro de un for-each, Java lanza ConcurrentModificationException, porque el recorrido se da cuenta de que la lista cambio debajo de sus pies. La solucion correcta es usar un Iterator explicito y llamar a it.remove(), o usar mascotas.removeIf(m -> m.getEdad() >= 9). En VetCare esto aparece apenas queremos pasar a control geriatrico a todas las mascotas de nueve anios o mas: se recorre con Iterator, se saca con it.remove() y no truena nada.",
            "La ultima idea es de diseno, y es la que hace que este codigo sirva para el resto del proyecto integrador. La lista no debe ser un atributo publico que cualquiera manipula desde main; debe vivir privada dentro de la clase RegistroMascotas, y el mundo exterior solo puede hablarle a traves de metodos con reglas de negocio: agregar valida que el ID no este repetido, eliminarPorId avisa si la mascota no existe, buscarPorId devuelve null cuando no la encuentra. Eso es encapsulamiento aplicado a colecciones, y es lo que hara posible que en las proximas clases la misma clase RegistroMascotas alimente una tabla de Swing y despues se guarde en un archivo CSV sin cambiar una sola linea de la logica. Programe siempre contra la interfaz (List) y no contra la implementacion (ArrayList), porque si manana necesita cambiar a LinkedList solo toca una linea. Y sobreescriba toString() en Mascota desde ya: sin el, imprimir la lista muestra basura como vetcare.Mascota@6d06d69c y los estudiantes creen que el programa fallo.",
            "Error tipico del docente que no domina el tema: creer que new ArrayList<>(50) ya trae 50 mascotas adentro y hacer get(0) de una, lo que revienta con IndexOutOfBoundsException porque ese 50 es capacidad, no tamano; la lista recien creada tiene size() igual a cero. El segundo tropiezo es la confusion de nombres: los arreglos usan .length (sin parentesis), los String usan .length() (con parentesis) y las colecciones usan .size(); el docente escribe mascotas.length, no compila, y se queda mudo frente al grupo. El tercero es recorrer con i <= mascotas.size(), que siempre falla en la ultima vuelta porque los indices van de 0 a size()-1. Y el cuarto, el mas comun, es escribir ArrayList mascotas = new ArrayList(); sin generico, que compila con una advertencia amarilla, obliga a castear cada elemento al leerlo y termina en ClassCastException en tiempo de ejecucion. Antes de la clase, ejecute usted mismo estos cuatro errores en NetBeans para reconocer el mensaje rojo en dos segundos y convertirlo en ensenanza en vez de en silencio incomodo."
        ],
        "taller": [
            "Cree en NetBeans el proyecto Java Application llamado VetCare con paquete vetcare, y dentro de el la clase Mascota con los atributos privados id, nombre, especie, edad y dueno, su constructor completo, sus getters y el metodo toString(); verifique imprimiendo una mascota de prueba y confirmando que en consola sale el texto legible y no vetcare.Mascota@1a2b3c.",
            "Cree la clase RegistroMascotas con el atributo private final List<Mascota> mascotas = new ArrayList<>(); y el metodo agregar(Mascota m) que rechace un ID ya existente; verifique agregando dos veces la mascota M-001 y comprobando que la consola muestra el aviso de ID repetido y que cantidad() sigue devolviendo 1.",
            "Implemente listar(), que recorra con for indexado e imprima cada ficha numerada, y buscarPorId(String id), que recorra con for-each y devuelva la Mascota o null; verifique que buscarPorId(\"M-003\") imprime la ficha de Rocky y que buscarPorId(\"M-099\") imprime que no existe, sin lanzar NullPointerException.",
            "Implemente eliminarPorId(String id) usando remove(objeto) y el metodo pasarAGeriatria(int edadMinima) usando Iterator con it.remove(); verifique que despues de eliminar M-002 y de pasar a geriatria a las mascotas de 9 anios o mas, size() bajo exactamente en la cantidad de fichas retiradas y el programa no lanza ConcurrentModificationException.",
            "Arme un menu de consola con Scanner y opciones 1-Agregar, 2-Listar, 3-Buscar por ID, 4-Eliminar, 5-Salir dentro de un ciclo while; ejecute el programa cargando las seis fichas del escenario, tome captura de la consola con el listado final y suba el proyecto comprimido mas la captura a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ VetCare no puede tener un tope de pacientes escrito a mano en el codigo, y toda la persistencia en CSV de las clases finales va a leer y escribir exactamente esta lista de mascotas.",
            "El requisito tecnico del PI pide colecciones de Java, y ArrayList es la coleccion base sobre la que despues montaremos la cola de la sala de espera, el HashMap de expedientes y la tabla de Swing.",
            "Encapsular la lista dentro de RegistroMascotas es lo que permitira cambiar la interfaz de consola por una ventana grafica sin reescribir la logica del negocio."
        ],
        "escenario": [
            "La recepcionista de Huellitas transcribio seis fichas de papel: M-001 Firulais canino 4 anios de Ana Gomez, M-002 Michi felino 2 anios de Luis Perez, M-003 Rocky canino 9 anios de Ana Gomez, M-004 Nieve felino 1 ano de Sara Diaz, M-005 Toby canino 11 anios de Sara Diaz y una ficha repetida de M-001.",
            "El codigo de partida es un Mascota[3] que ya no admite mas fichas y lanza ArrayIndexOutOfBoundsException al guardar la cuarta.",
            "No hay archivos ni base de datos todavia: todo vive en memoria durante la ejecucion, y al cerrar el programa los datos se pierden (eso se resuelve en las clases de persistencia)."
        ],
        "criterios": [
            "El registro acepta mas de tres mascotas sin declarar ningun tamano fijo y size() refleja el numero real de fichas activas.",
            "Al intentar agregar un ID ya existente el programa lo rechaza con mensaje claro y no aumenta el tamano de la lista.",
            "buscarPorId devuelve la mascota correcta cuando existe y maneja el caso de no encontrada sin lanzar NullPointerException.",
            "La eliminacion masiva por edad se hace con Iterator o removeIf y el programa termina sin ConcurrentModificationException."
        ],
        "pistas": [
            "Si su lista imprime algo como vetcare.Mascota@6d06d69c, que metodo heredado de Object le esta faltando a la clase Mascota?",
            "Cuando el recorrido llega a la ultima ficha y truena con IndexOutOfBoundsException, revise la condicion del for: el ultimo indice valido es igual a size() o es size() menos uno?",
            "Si borra una mascota justo dentro de un for-each y aparece ConcurrentModificationException, quien deberia estar autorizado para sacar el elemento: la lista o el objeto que la esta recorriendo?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: en Mascota se declaran los cinco atributos como private final String id, nombre, especie, dueno y private final int edad, y se genera el constructor con Alt+Insert en NetBeans. Los getters se generan igual (Alt+Insert > Getter). El toString queda asi: return id + \" | \" + nombre + \" (\" + especie + \", \" + edad + \" anios) - dueno: \" + dueno; con eso cualquier System.out.println(mascota) o cualquier impresion de la lista completa muestra texto legible, porque println llama automaticamente a toString sobre el objeto.",
            "Paso 2 resuelto: en RegistroMascotas se escribe private final List<Mascota> mascotas = new ArrayList<>(); El final protege la referencia (nadie puede reemplazar la lista entera) pero el contenido si cambia. El metodo agregar queda: if (m == null) { avisa y devuelve false; } if (buscarPorId(m.getId()) != null) { System.out.println(\"ID repetido, se rechaza: \" + m.getId()); return false; } mascotas.add(m); return true; Como la validacion vive dentro de la clase y no en el main, cualquier interfaz futura (consola, ventana Swing, carga de CSV) hereda la misma regla sin repetir codigo.",
            "Paso 3 resuelto: listar recorre con for (int i = 0; i < mascotas.size(); i++) e imprime (i + 1) + \". \" + mascotas.get(i), usando el indice solo porque necesita el numero de renglon; antes valida if (mascotas.isEmpty()) para no imprimir un listado vacio. buscarPorId recorre con for (Mascota m : mascotas) y compara con m.getId().equalsIgnoreCase(id), no con ==, porque == compara referencias de memoria y no el contenido del texto; equalsIgnoreCase ademas tolera que la recepcionista escriba m-003. Si el ciclo termina sin encontrar nada devuelve null, y quien llama debe validarlo: System.out.println(encontrada != null ? encontrada : \"No existe esa mascota\").",
            "Paso 4 resuelto: eliminarPorId(String id) primero hace Mascota m = buscarPorId(id); si m es null imprime que no existe y devuelve false; si no, llama a mascotas.remove(m), que es remove(Object) y no remove(int), diferencia clave porque remove(2) borraria por posicion. pasarAGeriatria(int edadMinima) obtiene Iterator<Mascota> it = mascotas.iterator(); y dentro de un while (it.hasNext()) toma Mascota m = it.next(); si m.getEdad() >= edadMinima llama a it.remove(). El Iterator es el unico que puede borrar mientras recorre porque el mismo actualiza su contador interno; hacer mascotas.remove(m) dentro del ciclo produce ConcurrentModificationException. La version corta equivalente es mascotas.removeIf(m -> m.getEdad() >= edadMinima).",
            "Paso 5 resuelto: el menu se arma con Scanner sc = new Scanner(System.in); dentro de un while (opcion != 5). La opcion se lee con Integer.parseInt(sc.nextLine().trim()) envuelto en try-catch de NumberFormatException, para que escribir una letra no tumbe el programa sino que imprima \"Escriba un numero del 1 al 5\" y vuelva a preguntar. Cada case llama al metodo correspondiente del registro: case 1 pide los cinco datos y hace registro.agregar(new Mascota(...)); case 2 llama registro.listar(); case 3 pide el ID y valida el null antes de imprimir; case 4 llama registro.eliminarPorId(id). El main nunca toca la lista directamente: solo conversa con RegistroMascotas, que es justo lo que permitira cambiar la consola por una ventana en la Clase 4."
        ],
        "solucion_rubrica": [
            "Clase Mascota con atributos privados, constructor, getters y toString (2)",
            "RegistroMascotas con List<Mascota> encapsulada y agregar que rechaza IDs repetidos (3)",
            "buscarPorId y eliminarPorId funcionando, incluido el caso no encontrado (3)",
            "Menu de consola ejecutable, sin excepciones, con evidencia subida a ExamLab (2)"
        ],
        "solucion_errores": [
            "Escribir mascotas.length en vez de mascotas.size(): length es de arreglos, length() es de String y size() es de colecciones; el proyecto ni siquiera compila.",
            "Recorrer con for (int i = 0; i <= mascotas.size(); i++), lo que siempre lanza IndexOutOfBoundsException en la ultima vuelta porque el indice valido llega hasta size()-1.",
            "Borrar con mascotas.remove(m) dentro de un for-each y recibir ConcurrentModificationException, en vez de usar Iterator.remove() o removeIf."
        ],
        "codigo_slide_titulo": "El arreglo se llena; la lista crece sola",
        "codigo_slide_lineas": [
            "Mascota nieve = new Mascota(\"M-004\", \"Nieve\", \"Felino\", 1, \"Sara Diaz\");",
            "",
            "Mascota[] fichero = new Mascota[3];          // tamano decidido HOY, para siempre",
            "fichero[3] = nieve;                          // ArrayIndexOutOfBoundsException",
            "",
            "List<Mascota> mascotas = new ArrayList<>();  // interfaz List, implementacion ArrayList",
            "mascotas.add(nieve);                         // add SIEMPRE agrega al final",
            "System.out.println(mascotas.size());         // size() = cuantas hay, no capacidad",
            "Mascota m = mascotas.get(0);                 // get(indice): de 0 a size()-1",
            "",
            "for (Mascota x : mascotas) {                 // for-each: solo para LEER",
            "    System.out.println(x);                   // usa toString() de Mascota",
            "}",
            "",
            "Iterator<Mascota> it = mascotas.iterator();  // para BORRAR mientras se recorre",
            "while (it.hasNext()) {",
            "    if (it.next().getEdad() >= 9) it.remove();   // geriatria, sin excepcion",
            "}"
        ],
        "codigo_slide_caption": "El arreglo obliga a adivinar el futuro; el ArrayList lo administra por usted, siempre que respete size() y borre con Iterator.",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare se declara List<Mascota> mascotas = new ArrayList<>(); Que devuelve mascotas.size() inmediatamente despues de esa linea?",
                "opciones": [
                    "A) 10, que es la capacidad inicial por defecto del arreglo interno",
                    "B) 0, porque todavia no se ha agregado ninguna mascota",
                    "C) null, porque la lista aun no tiene elementos",
                    "D) Un error de compilacion, porque size() solo se puede llamar despues del primer add"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "El registro tiene 5 mascotas. Cual instruccion lanza IndexOutOfBoundsException?",
                "opciones": [
                    "A) mascotas.get(0)",
                    "B) mascotas.get(4)",
                    "C) mascotas.get(mascotas.size())",
                    "D) mascotas.get(mascotas.size() - 1)"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Se quiere retirar de la lista activa a todas las mascotas de 9 anios o mas mientras se recorre la coleccion. Cual es la forma correcta?",
                "opciones": [
                    "A) Un for-each llamando a mascotas.remove(m) adentro",
                    "B) Un Iterator llamando a it.remove(), o mascotas.removeIf(m -> m.getEdad() >= 9)",
                    "C) Recorrer con for indexado ascendente y usar remove(i) sin ajustar el indice",
                    "D) Copiar la lista a un arreglo del mismo tamano, borrar alli y devolverla"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Por que en VetCare se declara List<Mascota> a la izquierda y new ArrayList<>() a la derecha?",
                "opciones": [
                    "A) Porque List<Mascota> ocupa menos memoria que ArrayList<Mascota>",
                    "B) Porque asi la lista queda inmutable y nadie puede agregar mascotas",
                    "C) Porque se programa contra la interfaz y cambiar de implementacion cuesta una sola linea",
                    "D) Porque los metodos add y get solo existen en List, no en ArrayList"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "El numero que se pasa en new ArrayList<>(50) significa que la lista ya contiene 50 mascotas listas para leer con get().",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "En un arreglo se consulta el tamano con .length, en un String con .length() y en un ArrayList con .size().",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Explique con sus palabras que hace un ArrayList por dentro cuando su arreglo interno se llena y usted llama a add().",
                "clave": "Crea un arreglo interno nuevo mas grande (aproximadamente 1.5 veces), copia todos los elementos existentes al nuevo arreglo con Arrays.copyOf, descarta el viejo y agrega el elemento al final; el programador no se entera porque el proceso es automatico."
            },
            {
                "tipo": "abierta",
                "q": "En RegistroMascotas, por que buscarPorId devuelve null cuando no encuentra la mascota y que obligacion le impone eso a quien llama al metodo?",
                "clave": "Devuelve null porque no hay ningun objeto que entregar cuando el ID no existe; quien llama esta obligado a validar el resultado (por ejemplo con if (m != null)) antes de usarlo, de lo contrario se produce NullPointerException al invocar cualquier metodo sobre esa referencia."
            }
        ],
        "codigo_fuente": "package vetcare;\n\nimport java.util.ArrayList;\nimport java.util.Iterator;\nimport java.util.List;\nimport java.util.Scanner;\n\n/**\n * VetCare - Clase 2: de arreglos fijos a ArrayList.\n * Clinica Veterinaria Huellitas.\n * Archivo unico: clic derecho sobre el archivo > Run File (Shift+F6) en NetBeans.\n * Los bloques 1 a 4 corren solos; el bloque 5 abre el menu y pide datos por consola.\n */\npublic class VetCareRegistroMascotas {\n\n    public static void main(String[] args) {\n\n        System.out.println(\"=== 1. El arreglo fijo se queda corto ===\");\n        Mascota[] fichero = new Mascota[3]; // el tamano se decide hoy y ya no cambia\n        fichero[0] = new Mascota(\"M-001\", \"Firulais\", \"Canino\", 4, \"Ana Gomez\");\n        fichero[1] = new Mascota(\"M-002\", \"Michi\", \"Felino\", 2, \"Luis Perez\");\n        fichero[2] = new Mascota(\"M-003\", \"Rocky\", \"Canino\", 9, \"Ana Gomez\");\n        try {\n            fichero[3] = new Mascota(\"M-004\", \"Nieve\", \"Felino\", 1, \"Sara Diaz\");\n        } catch (ArrayIndexOutOfBoundsException e) {\n            System.out.println(\"No cabe la cuarta mascota: fichero.length = \" + fichero.length);\n        }\n\n        System.out.println();\n        System.out.println(\"=== 2. El mismo caso con ArrayList ===\");\n        RegistroMascotas registro = new RegistroMascotas();\n        for (Mascota m : fichero) {\n            registro.agregar(m);\n        }\n        registro.agregar(new Mascota(\"M-004\", \"Nieve\", \"Felino\", 1, \"Sara Diaz\"));\n        registro.agregar(new Mascota(\"M-005\", \"Toby\", \"Canino\", 11, \"Sara Diaz\"));\n        registro.agregar(new Mascota(\"M-001\", \"Firulais repetida\", \"Canino\", 4, \"Ana Gomez\"));\n        System.out.println(\"size() = \" + registro.cantidad() + \" (la lista crecio sola)\");\n\n        System.out.println();\n        System.out.println(\"=== 3. Recorrido y busqueda por ID ===\");\n        registro.listar();\n        System.out.println(\"buscarPorId(M-003) -> \" + registro.buscarPorId(\"M-003\"));\n        System.out.println(\"buscarPorId(M-099) -> \" + registro.buscarPorId(\"M-099\"));\n\n        System.out.println();\n        System.out.println(\"=== 4. Eliminar sin romper el recorrido ===\");\n        registro.eliminarPorId(\"M-002\");\n        registro.pasarAGeriatria(9); // con Iterator: borrar en un for-each lanza excepcion\n        registro.listar();\n        System.out.println(\"Total activo: \" + registro.cantidad());\n\n        System.out.println();\n        System.out.println(\"=== 5. Menu de consola (el main nunca toca la lista) ===\");\n        menu(registro);\n    }\n\n    /** El menu solo conversa con RegistroMascotas: no conoce la lista por dentro. */\n    private static void menu(RegistroMascotas registro) {\n        Scanner sc = new Scanner(System.in);\n        int opcion = 0;\n        while (opcion != 5) {\n            System.out.println();\n            System.out.println(\"1-Agregar  2-Listar  3-Buscar por ID  4-Eliminar  5-Salir\");\n            System.out.print(\"Opcion: \");\n            if (!sc.hasNextLine()) {\n                break; // la consola no tiene mas entrada disponible\n            }\n            try {\n                opcion = Integer.parseInt(sc.nextLine().trim());\n            } catch (NumberFormatException e) {\n                System.out.println(\"Escriba un numero del 1 al 5\");\n                continue;\n            }\n            switch (opcion) {\n                case 1:\n                    System.out.print(\"ID: \");\n                    String id = sc.nextLine().trim();\n                    System.out.print(\"Nombre: \");\n                    String nombre = sc.nextLine().trim();\n                    System.out.print(\"Especie: \");\n                    String especie = sc.nextLine().trim();\n                    System.out.print(\"Edad: \");\n                    int edad = leerEntero(sc);\n                    System.out.print(\"Dueno: \");\n                    String dueno = sc.nextLine().trim();\n                    registro.agregar(new Mascota(id, nombre, especie, edad, dueno));\n                    break;\n                case 2:\n                    registro.listar();\n                    break;\n                case 3:\n                    System.out.print(\"ID a buscar: \");\n                    Mascota encontrada = registro.buscarPorId(sc.nextLine().trim());\n                    System.out.println(encontrada != null ? encontrada : \"No existe esa mascota\");\n                    break;\n                case 4:\n                    System.out.print(\"ID a eliminar: \");\n                    registro.eliminarPorId(sc.nextLine().trim());\n                    break;\n                case 5:\n                    System.out.println(\"Hasta luego\");\n                    break;\n                default:\n                    System.out.println(\"Opcion no valida\");\n            }\n        }\n    }\n\n    private static int leerEntero(Scanner sc) {\n        try {\n            return Integer.parseInt(sc.nextLine().trim());\n        } catch (NumberFormatException e) {\n            System.out.println(\"Edad invalida: se registra 0\");\n            return 0;\n        }\n    }\n}\n\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private final String especie;\n    private final int edad;\n    private final String dueno;\n\n    public Mascota(String id, String nombre, String especie, int edad, String dueno) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n        this.edad = edad;\n        this.dueno = dueno;\n    }\n\n    public String getId() { return id; }\n    public String getNombre() { return nombre; }\n    public String getEspecie() { return especie; }\n    public int getEdad() { return edad; }\n    public String getDueno() { return dueno; }\n\n    @Override\n    public String toString() {\n        return id + \" | \" + nombre + \" (\" + especie + \", \" + edad + \" anios) - dueno: \" + dueno;\n    }\n}\n\nclass RegistroMascotas {\n\n    // La lista vive privada: nadie le mete mano sin pasar por las reglas del negocio\n    private final List<Mascota> mascotas = new ArrayList<>();\n\n    public boolean agregar(Mascota m) {\n        if (m == null) {\n            System.out.println(\"Ficha nula, no se registra\");\n            return false;\n        }\n        if (buscarPorId(m.getId()) != null) {\n            System.out.println(\"ID repetido, se rechaza: \" + m.getId());\n            return false;\n        }\n        mascotas.add(m); // add siempre agrega al final\n        System.out.println(\"Registrada: \" + m.getNombre());\n        return true;\n    }\n\n    public Mascota buscarPorId(String id) {\n        if (id == null) {\n            return null;\n        }\n        for (Mascota m : mascotas) { // for-each: solo para leer\n            if (m.getId().equalsIgnoreCase(id.trim())) {\n                return m;\n            }\n        }\n        return null; // null = no esta; quien llama debe validarlo\n    }\n\n    public boolean eliminarPorId(String id) {\n        Mascota m = buscarPorId(id);\n        if (m == null) {\n            System.out.println(\"No existe la mascota \" + id);\n            return false;\n        }\n        mascotas.remove(m); // remove(Object), no remove(indice)\n        System.out.println(\"Retirada de la lista activa: \" + m.getNombre());\n        return true;\n    }\n\n    public void pasarAGeriatria(int edadMinima) {\n        Iterator<Mascota> it = mascotas.iterator();\n        while (it.hasNext()) {\n            Mascota m = it.next();\n            if (m.getEdad() >= edadMinima) {\n                it.remove(); // unica forma segura de borrar mientras se recorre\n                System.out.println(\"Pasa a control geriatrico: \" + m.getNombre());\n            }\n        }\n    }\n\n    public void listar() {\n        if (mascotas.isEmpty()) {\n            System.out.println(\"(no hay mascotas registradas)\");\n            return;\n        }\n        for (int i = 0; i < mascotas.size(); i++) { // ojo: < size(), nunca <=\n            System.out.println((i + 1) + \". \" + mascotas.get(i));\n        }\n    }\n\n    public int cantidad() {\n        return mascotas.size();\n    }\n}\n",
        "codigo_archivo": "VetCareRegistroMascotas.java"
    },
    {
        "n": 3,
        "slug": "Pilas y colas",
        "titulo": "Pilas y colas · Stack y Queue",
        "subtitulo": "Cuando restringir el acceso hace el software mas seguro",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare queda con la sala de espera modelada como cola FIFO y el historial de atenciones recientes como pila LIFO, ambas conectadas al registro de mascotas de la clase anterior.",
        "entregable": "Clases SalaDeEspera (Queue) e HistorialReciente (Deque como pila) integradas al proyecto VetCare, con una demo que atiende en orden de llegada las cuatro mascotas del escenario y deshace la ultima atencion registrada; comprimido y subido a ExamLab.",
        "demo": "El docente encola cuatro mascotas, muestra en pantalla la diferencia entre peek() y poll() atendiendo en orden de llegada, y luego usa push/pop para deshacer la ultima atencion registrada.",
        "teoria": [
            "La clase pasada nos dio un ArrayList, que es una herramienta poderosa justamente porque permite todo: agregar al final, insertar en la mitad, sacar de cualquier posicion, reordenar. Ese poder es un problema cuando lo que usted esta modelando tiene reglas. La sala de espera de Huellitas tiene una regla sagrada: el que llega primero pasa primero. Si la sala de espera es un ArrayList, cualquier programador del equipo (o usted mismo a las once de la noche) puede escribir salaEspera.add(0, mascotaDelAmigo) y colar a alguien sin que nada falle: compila, corre y la clinica pierde la confianza de sus clientes. Una estructura restrictiva como Queue no ofrece ese metodo; simplemente no existe en su contrato, entonces el error se vuelve imposible de escribir. Esa es la idea grande de hoy: elegir la estructura mas limitada que resuelva el problema no es una limitacion tecnica, es una forma de blindar la regla del negocio dentro del tipo de dato.",
            "La cola, o Queue, funciona con disciplina FIFO: First In, First Out, el primero que entra es el primero que sale, igual que la fila del banco. En Java, Queue es una interfaz, no una clase, asi que se declara Queue<Turno> salaEspera = new LinkedList<>(); o new ArrayDeque<>(); intentar new Queue<>() no compila y ese es el primer error que veremos en pantalla. La cola tiene tres operaciones utiles y cada una viene en dos sabores: offer(x) agrega al final y devuelve false si no cabe (la version add lanza IllegalStateException en ese caso), poll() saca y devuelve el primero o null si esta vacia (la version remove lanza NoSuchElementException), y peek() mira el primero sin sacarlo o devuelve null (la version element tambien lanza excepcion). En VetCare usamos siempre offer/poll/peek porque avisan con false o con null en vez de reventar, y en una recepcion que puede quedar vacia a media manana eso es exactamente lo que queremos. peek es lo que alimenta la pantalla de turnos que ve el publico; poll es lo que hace el medico cuando abre la puerta del consultorio.",
            "La pila, o Stack, funciona al reves: LIFO, Last In, First Out, como la pila de historias clinicas sobre el escritorio, donde uno siempre coge la de encima. Sus operaciones son push(x) para poner encima, pop() para sacar el de encima y peek() para mirarlo sin sacarlo. Java trae una clase llamada Stack, pero es codigo de 1995: hereda de Vector, esta sincronizada (lo que la hace mas lenta sin necesidad) y permite acceder por indice, con lo cual rompe la propia restriccion que dice defender. La practica actual es usar Deque<String> historial = new ArrayDeque<>(); y llamarle push/pop/peek, que es exactamente la misma API pero sobre una implementacion moderna. En VetCare la pila guarda el historial de atenciones recientes: cada consulta terminada se apila, la pantalla del medico muestra siempre la de encima con peek, y si registro una atencion por equivocacion, pop la deshace. Eso es literalmente como funciona el Ctrl+Z de cualquier programa.",
            "Vale la pena entender por que estas estructuras son rapidas, porque ahi esta el argumento tecnico y no solo el pedagogico. ArrayDeque es un arreglo circular con dos punteros, uno al frente y otro al final: cuando usted saca del frente no mueve ni un elemento, solo corre el puntero, y cuando el puntero llega al final del arreglo da la vuelta al inicio. Por eso agregar y sacar por cualquiera de los dos extremos cuesta tiempo constante. LinkedList, en cambio, es una cadena de nodos donde cada nodo apunta al siguiente y al anterior, asi que sacar el primero es simplemente mover la cabeza de la cadena. Compare eso con usar un ArrayList como cola: mascotas.remove(0) obliga a desplazar todos los elementos restantes un puesto hacia la izquierda, lo que en una jornada de 300 turnos significa decenas de miles de movimientos innecesarios. La estructura correcta no solo previene errores de negocio, tambien evita que el programa se arrastre.",
            "Un punto que confunde mucho: una cola no se recorre para buscar. Si usted se descubre iterando la sala de espera para encontrar a Firulais y sacarlo del medio, la senal es que ese caso de uso no es una cola pura, y que necesita otra estructura al lado (por ejemplo un Deque que permita addFirst para urgencias, o un HashMap que veremos la proxima clase). En VetCare resolvemos la urgencia sin traicionar el modelo: usamos Deque<Turno> y decimos addLast para el que llega normal y addFirst para el caso critico, dejando explicito en el codigo que colarse es una operacion excepcional y con nombre propio, no un accidente. Ademas, recorrer una cola con for-each la muestra pero no la consume; muchos estudiantes imprimen la cola con un for-each, ven todos los turnos y creen que ya los atendieron, cuando en realidad size() sigue igual. Consumir es poll; mirar es peek o for-each.",
            "Error tipico del docente que no domina el tema: escribir Queue<Turno> sala = new Queue<>() y quedarse en blanco cuando NetBeans subraya la linea, sin poder explicar que Queue es una interfaz y que necesita una implementacion concreta como LinkedList o ArrayDeque. El segundo clasico es usar la clase Stack solamente porque es la primera que aparece en Google, y no poder responder cuando un estudiante pregunta por que la documentacion recomienda ArrayDeque. El tercero, muy frecuente, es confundir peek con poll durante la demo: el docente llama a peek dentro de un while creyendo que va a vaciar la cola y arma un ciclo infinito en plena clase. El cuarto es llamar pop() sobre una pila vacia sin validar isEmpty(), que con ArrayDeque lanza NoSuchElementException y con Stack lanza EmptyStackException; hay que mostrar esa excepcion a proposito y envolverla en try-catch, porque el PI exige manejo de errores. Ensaye los cuatro casos antes de entrar al salon para que cada mensaje rojo sea una leccion planeada y no una sorpresa."
        ],
        "taller": [
            "Cree la clase Turno con id, nombre de la mascota, nombre del dueno y motivo de consulta, mas sus getters y su toString(); verifique imprimiendo un turno suelto en consola antes de meterlo en cualquier estructura.",
            "Cree la clase SalaDeEspera con el atributo private final Queue<Turno> cola = new LinkedList<>(); y los metodos registrarLlegada(Turno t) usando offer, siguienteEnPantalla() usando peek y atender() usando poll; verifique que despues de registrar cuatro llegadas y llamar dos veces a siguienteEnPantalla(), cantidad() sigue siendo 4.",
            "Haga que atender() valide la cola vacia con isEmpty() y devuelva un mensaje controlado en vez de un null suelto; verifique llamando a atender() cinco veces cuando solo hay cuatro turnos y confirmando que la quinta llamada imprime que la sala esta vacia y el programa no se cae.",
            "Cree la clase HistorialReciente con private final Deque<String> pila = new ArrayDeque<>(); y los metodos registrar(String), ultimaAtencion() con peek y deshacer() con pop protegido por isEmpty(); verifique que despues de atender a Firulais, Michi y Rocky, ultimaAtencion() muestra a Rocky y deshacer() lo retira dejando a Michi arriba.",
            "Conecte las dos estructuras en un main: cada vez que atender() saca un turno de la cola, registre automaticamente esa consulta en la pila; ejecute el flujo completo con las cuatro mascotas del escenario mas la urgencia de Canela agregada con addFirst sobre un Deque, capture la consola y suba el proyecto a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ VetCare debe agendar y atender en orden real de llegada, y esa regla queda garantizada por el tipo de dato y no por la buena memoria del programador.",
            "El historial de atenciones recientes en pila es la base del deshacer que despues protegera al usuario cuando la interfaz grafica permita registrar consultas por error.",
            "Cola y pila son las estructuras que se guardaran y recargaran desde archivo en las clases de persistencia, asi que hoy definimos el orden en que se escribiran las lineas del CSV."
        ],
        "escenario": [
            "Es lunes 8:00 a.m. en Huellitas y llegan en este orden: Firulais (M-001, vacuna, dueno Ana Gomez), Michi (M-002, control, dueno Luis Perez), Rocky (M-003, revision de patas, dueno Ana Gomez) y Nieve (M-004, desparasitacion, duena Sara Diaz).",
            "La sala de espera arranca vacia y el historial de atenciones recientes tambien; el registro de mascotas de la Clase 2 ya esta cargado y se reutiliza.",
            "A las 8:20 entra Canela (M-009, duena Ana Gomez) con una urgencia real y debe pasar de primera sin destruir el orden de los demas."
        ],
        "criterios": [
            "Las mascotas se atienden exactamente en el orden en que llegaron, verificable en la salida de consola.",
            "peek/siguienteEnPantalla no altera el tamano de la cola, mientras que poll/atender lo reduce en uno por llamada.",
            "Atender con la sala vacia o deshacer con la pila vacia produce un mensaje controlado y nunca una excepcion sin capturar.",
            "Cada consulta atendida queda registrada automaticamente en la pila y deshacer retira siempre la mas reciente."
        ],
        "pistas": [
            "Si su ciclo while nunca termina y la consola se llena con el mismo nombre, cual de los dos metodos esta usando dentro del ciclo: el que mira o el que saca?",
            "Si necesita sacar a una mascota que esta en la mitad de la fila, la estructura que eligio sigue siendo la adecuada, o el requisito le esta pidiendo otra cosa?",
            "Antes de llamar a pop(), que pregunta deberia hacerle a la pila para que el programa no lance NoSuchElementException?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: Turno se construye igual que Mascota, con atributos private final String id, nombre, dueno y motivo, constructor completo, getters y toString del estilo return nombre + \" (\" + id + \") - \" + motivo + \" | dueno: \" + dueno; Tener toString desde el principio es lo que hace legible toda la demo de colas, porque cada poll imprime una linea entendible en vez de vetcare.Turno@3f2a1b.",
            "Paso 2 resuelto: dentro de SalaDeEspera se declara private final Queue<Turno> cola = new LinkedList<>(); a la izquierda va la interfaz Queue porque es la que define el contrato FIFO, y a la derecha LinkedList porque Queue es interfaz y no se puede instanciar. registrarLlegada hace cola.offer(t) y devuelve cola.size() para informarle al dueno que numero de turno le toco. siguienteEnPantalla hace return cola.peek(), que devuelve la referencia al primero sin retirarlo; por eso el tamano no cambia, y ese es el metodo que alimentaria un JLabel de la pantalla de turnos en la Clase 4.",
            "Paso 3 resuelto: atender queda asi: if (cola.isEmpty()) { System.out.println(\"Sala de espera vacia: no hay a quien atender\"); return null; } Turno t = cola.poll(); System.out.println(\"Pasa a consultorio: \" + t); return t; Validar con isEmpty antes de sacar es la version defensiva y explicita; la alternativa es llamar directamente a poll y comparar el resultado con null, porque poll no lanza excepcion, a diferencia de remove(). Lo que nunca se debe hacer es llamar remove() a ciegas: con la sala vacia lanza NoSuchElementException y tumba el programa delante del cliente.",
            "Paso 4 resuelto: la pila se declara private final Deque<String> pila = new ArrayDeque<>(); y no con la clase Stack, que hereda de Vector y esta sincronizada sin necesidad. registrar(String consulta) hace pila.push(consulta), que inserta arriba; ultimaAtencion hace return pila.isEmpty() ? \"(sin movimientos)\" : pila.peek(); y deshacer hace if (pila.isEmpty()) return \"Nada que deshacer\"; else return \"Se deshizo: \" + pila.pop(); Como push mete arriba y pop saca de arriba, el ultimo registrado es siempre el primero en salir: eso es LIFO, y es exactamente el comportamiento de un Ctrl+Z.",
            "Paso 5 resuelto: en el main se conectan las dos estructuras con while (!sala.estaVacia()) { Turno t = sala.atender(); historial.registrar(\"Consulta de \" + t.getNombre() + \" (\" + t.getId() + \")\"); } Como la condicion del while ya garantizo que la cola no esta vacia, t nunca es null dentro del ciclo. Para la urgencia se usa Deque<Turno> filaConUrgencias = new ArrayDeque<>(); con addLast(nieve) y addLast(toby) para las llegadas normales y addFirst(canela) para la urgencia; se vacia con pollFirst(). Nombrar la operacion addFirst deja escrito en el codigo que ese salto de fila es una excepcion autorizada del negocio y no un descuido del programador."
        ],
        "solucion_rubrica": [
            "Clase Turno completa con toString y clase SalaDeEspera con Queue correctamente declarada (2)",
            "Uso correcto de offer, peek y poll con la diferencia entre mirar y sacar demostrada en consola (3)",
            "HistorialReciente con Deque usado como pila y deshacer funcionando (3)",
            "Manejo de cola y pila vacias con mensaje controlado, mas evidencia subida a ExamLab (2)"
        ],
        "solucion_errores": [
            "Escribir Queue<Turno> cola = new Queue<>(), que no compila porque Queue es una interfaz y necesita una implementacion como LinkedList o ArrayDeque.",
            "Usar peek() dentro del while que debe vaciar la cola, generando un ciclo infinito porque el elemento nunca se retira.",
            "Llamar a pop() o remove() sobre una estructura vacia sin validar isEmpty(), lo que lanza NoSuchElementException o EmptyStackException y tumba el programa."
        ],
        "codigo_slide_titulo": "FIFO para la sala, LIFO para el historial",
        "codigo_slide_lineas": [
            "// Turno firulais, michi, nieve y canela ya fueron creados con new Turno(...)",
            "Queue<Turno> sala = new LinkedList<>();      // Queue es INTERFAZ, no se instancia sola",
            "sala.offer(firulais);                        // offer = encolar al final (FIFO)",
            "sala.offer(michi);",
            "Turno enPantalla = sala.peek();              // MIRA el primero, size() NO cambia",
            "Turno atendido   = sala.poll();              // SACA el primero, size() baja en 1",
            "System.out.println(sala.poll());             // cola vacia -> null, no explota",
            "",
            "Deque<String> historial = new ArrayDeque<>(); // pila moderna, mejor que Stack",
            "historial.push(\"Consulta de Firulais\");      // push = poner encima (LIFO)",
            "historial.push(\"Consulta de Michi\");",
            "System.out.println(historial.peek());        // Michi: el ultimo que entro",
            "if (!historial.isEmpty()) historial.pop();   // deshacer, siempre validando primero",
            "",
            "Deque<Turno> fila = new ArrayDeque<>();      // urgencia sin colarse a escondidas",
            "fila.addLast(nieve);                         // llegada normal: al final",
            "fila.addFirst(canela);                       // URGENCIA: al frente, con nombre propio"
        ],
        "codigo_slide_caption": "La estructura restrictiva no le quita poder: le quita la posibilidad de romper la regla del negocio sin darse cuenta.",
        "quiz": [
            {
                "tipo": "om",
                "q": "En la sala de espera de VetCare se llama a peek() tres veces seguidas sobre una cola con 4 turnos. Cuantos turnos quedan?",
                "opciones": [
                    "A) 1, porque peek va sacando uno por uno",
                    "B) 4, porque peek solo mira el primero sin retirarlo",
                    "C) 0, porque peek vacia la cola",
                    "D) Lanza NoSuchElementException a la segunda llamada"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual declaracion compila correctamente para la sala de espera de VetCare?",
                "opciones": [
                    "A) Queue<Turno> sala = new Queue<>();",
                    "B) Queue<Turno> sala = new LinkedList<>();",
                    "C) Queue<Turno> sala = new ArrayList<>();",
                    "D) Queue<Turno> sala = new Stack<>();"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Por que hoy se prefiere Deque con ArrayDeque en vez de la clase Stack para el historial de atenciones?",
                "opciones": [
                    "A) Porque Stack no tiene los metodos push, pop ni peek",
                    "B) Porque Stack hereda de Vector, esta sincronizada sin necesidad y permite acceso por indice, rompiendo la restriccion LIFO",
                    "C) Porque Stack no permite recorrer sus elementos con for-each",
                    "D) Porque Stack obliga a declarar el tamano maximo de la pila al crearla"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Que ocurre al llamar poll() sobre una cola vacia y remove() sobre esa misma cola vacia?",
                "opciones": [
                    "A) Ambos lanzan NoSuchElementException",
                    "B) Ambos devuelven null",
                    "C) poll() devuelve null y remove() lanza NoSuchElementException",
                    "D) poll() lanza excepcion y remove() devuelve null"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Usar un ArrayList y llamar remove(0) para atender turnos es equivalente en costo a usar una cola, porque en ambos casos se saca el primero.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "Recorrer la sala de espera con un for-each imprime los turnos pero no los retira: para consumirlos hay que usar poll().",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Explique por que en VetCare es mas seguro modelar la sala de espera con Queue que con ArrayList, en terminos de la regla del negocio.",
                "clave": "Porque Queue solo expone agregar al final y sacar del frente, de modo que la regla de que el primero en llegar es el primero en pasar queda garantizada por el tipo de dato; con ArrayList cualquiera puede usar add(0, x) o remove(indice) y colar a alguien sin que el compilador ni el programa se quejen."
            },
            {
                "tipo": "abierta",
                "q": "Describa como se implementa el deshacer del historial de atenciones y que validacion es obligatoria antes de ejecutarlo.",
                "clave": "Cada atencion terminada se apila con push, de modo que la mas reciente queda arriba; deshacer llama a pop, que retira justamente esa ultima. Antes de llamar a pop es obligatorio validar isEmpty() (o capturar la excepcion), porque hacer pop sobre una pila vacia lanza NoSuchElementException con ArrayDeque o EmptyStackException con Stack."
            }
        ],
        "codigo_fuente": "package vetcare;\n\nimport java.util.ArrayDeque;\nimport java.util.Deque;\nimport java.util.LinkedList;\nimport java.util.Queue;\n\n/**\n * VetCare - Clase 3: sala de espera (cola FIFO) e historial reciente (pila LIFO).\n * Clinica Veterinaria Huellitas.\n * Archivo unico: clic derecho sobre el archivo > Run File (Shift+F6) en NetBeans.\n */\npublic class VetCareSalaDeEspera {\n\n    public static void main(String[] args) {\n\n        SalaDeEspera sala = new SalaDeEspera();\n        HistorialReciente historial = new HistorialReciente();\n\n        System.out.println(\"=== 1. Llegadas a recepcion (offer = al final) ===\");\n        sala.registrarLlegada(new Turno(\"M-001\", \"Firulais\", \"Ana Gomez\", \"Vacuna\"));\n        sala.registrarLlegada(new Turno(\"M-002\", \"Michi\", \"Luis Perez\", \"Control\"));\n        sala.registrarLlegada(new Turno(\"M-003\", \"Rocky\", \"Ana Gomez\", \"Revision de patas\"));\n        sala.registrarLlegada(new Turno(\"M-004\", \"Nieve\", \"Sara Diaz\", \"Desparasitacion\"));\n        System.out.println(\"En espera: \" + sala.cantidad());\n        System.out.println(\"Pantalla de turnos (peek): \" + sala.siguienteEnPantalla());\n        System.out.println(\"Despues del peek siguen en espera: \" + sala.cantidad());\n\n        System.out.println();\n        System.out.println(\"=== 2. El consultorio atiende (poll = saca el primero) ===\");\n        while (!sala.estaVacia()) {\n            Turno t = sala.atender(); // dentro del while nunca es null\n            historial.registrar(\"Consulta de \" + t.getNombre() + \" (\" + t.getId() + \")\");\n        }\n        sala.atender(); // sala vacia: mensaje controlado, sin excepcion\n\n        System.out.println();\n        System.out.println(\"=== 3. Historial reciente (LIFO) ===\");\n        System.out.println(\"Ultimo movimiento (peek): \" + historial.ultimaAtencion());\n        System.out.println(historial.deshacer());\n        System.out.println(\"Ahora el ultimo es: \" + historial.ultimaAtencion());\n        System.out.println(\"Movimientos guardados: \" + historial.cantidad());\n\n        System.out.println();\n        System.out.println(\"=== 4. Pila vacia: se valida, no se revienta ===\");\n        while (historial.cantidad() > 0) {\n            System.out.println(historial.deshacer());\n        }\n        System.out.println(\"Intento extra -> \" + historial.deshacer());\n\n        System.out.println();\n        System.out.println(\"=== 5. Urgencia: pasa de primera, con nombre propio ===\");\n        Deque<Turno> filaConUrgencias = new ArrayDeque<>();\n        filaConUrgencias.addLast(new Turno(\"M-004\", \"Nieve\", \"Sara Diaz\", \"Desparasitacion\"));\n        filaConUrgencias.addLast(new Turno(\"M-005\", \"Toby\", \"Sara Diaz\", \"Control\"));\n        filaConUrgencias.addFirst(new Turno(\"M-009\", \"Canela\", \"Ana Gomez\", \"URGENCIA\"));\n        while (!filaConUrgencias.isEmpty()) {\n            System.out.println(\"Pasa: \" + filaConUrgencias.pollFirst());\n        }\n    }\n}\n\nclass Turno {\n\n    private final String id;\n    private final String nombre;\n    private final String dueno;\n    private final String motivo;\n\n    public Turno(String id, String nombre, String dueno, String motivo) {\n        this.id = id;\n        this.nombre = nombre;\n        this.dueno = dueno;\n        this.motivo = motivo;\n    }\n\n    public String getId() { return id; }\n    public String getNombre() { return nombre; }\n    public String getDueno() { return dueno; }\n    public String getMotivo() { return motivo; }\n\n    @Override\n    public String toString() {\n        return nombre + \" (\" + id + \") - \" + motivo + \" | dueno: \" + dueno;\n    }\n}\n\n/** Sala de espera: FIFO puro. No expone la cola, solo las operaciones del negocio. */\nclass SalaDeEspera {\n\n    private final Queue<Turno> cola = new LinkedList<>(); // Queue es interfaz\n\n    public int registrarLlegada(Turno t) {\n        cola.offer(t); // offer = agregar al final\n        System.out.println(\"Llega \" + t.getNombre() + \" -> turno numero \" + cola.size());\n        return cola.size();\n    }\n\n    public Turno siguienteEnPantalla() {\n        return cola.peek(); // MIRA el primero: el tamano no cambia\n    }\n\n    public Turno atender() {\n        if (cola.isEmpty()) {\n            System.out.println(\"Sala de espera vacia: no hay a quien atender\");\n            return null;\n        }\n        Turno t = cola.poll(); // SACA el primero\n        System.out.println(\"Pasa a consultorio: \" + t);\n        return t;\n    }\n\n    public boolean estaVacia() {\n        return cola.isEmpty();\n    }\n\n    public int cantidad() {\n        return cola.size();\n    }\n}\n\n/** Historial reciente: LIFO. Deque usado como pila (moderna, mejor que Stack). */\nclass HistorialReciente {\n\n    private final Deque<String> pila = new ArrayDeque<>();\n\n    public void registrar(String consulta) {\n        pila.push(consulta); // push = poner encima\n        System.out.println(\"Historial <- \" + consulta);\n    }\n\n    public String ultimaAtencion() {\n        return pila.isEmpty() ? \"(sin movimientos)\" : pila.peek();\n    }\n\n    public String deshacer() {\n        if (pila.isEmpty()) {\n            return \"Nada que deshacer\"; // nunca se llama pop() sin preguntar por isEmpty()\n        }\n        return \"Se deshizo: \" + pila.pop();\n    }\n\n    public int cantidad() {\n        return pila.size();\n    }\n}\n",
        "codigo_archivo": "VetCareSalaDeEspera.java"
    },
    {
        "n": 4,
        "slug": "Mapas conjuntos e interfaces graficas GUI",
        "titulo": "Mapas, conjuntos e interfaces graficas · HashMap, HashSet y Swing",
        "subtitulo": "Buscar por clave en un instante y darle cara al sistema",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare encuentra cualquier expediente por ID en tiempo constante con HashMap y estrena su primera ventana Swing para consultarlo.",
        "entregable": "Clase RegistroExpedientes con HashMap y HashSet mas la ventana VentanaBuscarExpediente construida a mano (sin arrastrar componentes) que busca por ID y muestra el resultado o un mensaje de error controlado; comprimido y subido a ExamLab.",
        "demo": "El docente busca la ficha H-5000 dentro de un archivo historico de 5.000 expedientes, primero recorriendo un ArrayList y luego con get() sobre un HashMap comparando los nanosegundos, y despues ejecuta la misma busqueda desde una ventana Swing escrita linea por linea.",
        "teoria": [
            "Antes de entrar en materia, el reparto del tiempo, porque hoy son dos temas en un solo bloque de 120 minutos y hay que ser estricto: minutos 0 a 10 encuadre y repaso rapido de cola y pila; minutos 10 a 55 mapas y conjuntos con demo en consola; minutos 55 a 65 pausa; minutos 65 a 95 introduccion a Swing con la ventana construida en vivo; minutos 95 a 115 taller integrado donde la ventana consulta el HashMap; minutos 115 a 120 cierre y entrega en ExamLab. Si el primer bloque se alarga, la ventana queda sin terminar y la clase se pierde, asi que ponga un cronometro visible. El hilo que une los dos temas es uno solo: hoy le damos a VetCare la capacidad de responder en un instante la pregunta que mas hace la recepcionista de Huellitas, que es dame el expediente de la mascota M-004, y ademas le damos una pantalla para hacerla sin abrir NetBeans.",
            "El problema tecnico es este: con un ArrayList, buscar por ID obliga a recorrer la lista comparando uno por uno, lo que se llama busqueda lineal y en el peor caso revisa los 5.000 elementos del archivo historico. Un HashMap resuelve eso con una idea distinta: en vez de guardar solo el objeto, guarda parejas clave-valor, y usa la clave para calcular directamente en que casilla del arreglo interno esta el valor. Ese calculo lo hace el metodo hashCode() del objeto clave: convierte el texto M-004 en un numero, ese numero se transforma en una posicion del arreglo interno, y ahi mismo queda el expediente. Cuando dos claves distintas caen en la misma casilla (una colision), el mapa guarda ambas en esa casilla y usa equals() para distinguirlas al leer. El resultado practico es que get(\"M-004\") no depende de cuantas mascotas haya: con 10 o con 100.000 tarda basicamente lo mismo, y eso es lo que vamos a medir en vivo con System.nanoTime(). En VetCare declaramos Map<String, Expediente> expedientes = new HashMap<>(); y la clave es el ID, que es unico por definicion.",
            "La API de Map es corta pero tiene trampas que hay que nombrar en voz alta. put(clave, valor) agrega, pero si la clave ya existia reemplaza el valor anterior en silencio y devuelve el que estaba: eso significa que un HashMap nunca tiene claves repetidas, y que guardar dos veces M-001 no da error, simplemente pisa el expediente anterior, lo cual puede ser exactamente lo que usted quiere o un bug grave si no lo controla. get(clave) devuelve el valor o null si la clave no existe, por eso siempre hay que validar antes de usar el resultado; getOrDefault(clave, valorPorDefecto) es la version comoda. containsKey pregunta por la clave y containsValue por el valor, siendo esta ultima lenta porque esa si recorre todo el mapa. Para recorrer se usa for (Map.Entry<String, Expediente> e : expedientes.entrySet()) y dentro se leen e.getKey() y e.getValue(); tambien existen keySet() para las claves y values() para los valores. Y algo crucial: si algun dia usted usa un objeto propio como clave, esta obligado a sobreescribir equals() y hashCode() juntos, porque si no, el mapa guardara duplicados que a los ojos del negocio son el mismo.",
            "El HashSet es el hermano del HashMap: por dentro es literalmente un HashMap donde solo importan las claves. Su promesa es una sola y es potente: no admite duplicados y responde en tiempo constante a la pregunta esto ya esta. Su metodo add devuelve un boolean que casi nadie mira y que vale oro: devuelve false si el elemento ya estaba. En VetCare lo usamos para dos cosas concretas: un Set<String> de IDs ya usados, para rechazar un registro duplicado sin recorrer nada, y un Set<String> de razas atendidas, que se llena solo y nos dice cuantas razas distintas ha visto la clinica sin que nadie las cuente a mano; como Firulais y Toby son los dos labradores, al guardar el segundo el conjunto responde false y sigue reportando una sola vez esa raza. Lo que un HashSet no le garantiza es el orden: si usted agrega Labrador, Criollo y Persa y luego imprime el conjunto, pueden salir en cualquier orden, porque la posicion la decide el hash. Si necesita conservar el orden de insercion use LinkedHashSet o LinkedHashMap, y si necesita orden alfabetico use TreeSet o TreeMap, que ordenan pero cuestan un poco mas.",
            "Ahora la parte grafica, y aqui empieza el segundo bloque de la clase. Swing es la biblioteca de escritorio de Java y funciona por anidamiento: la ventana es un JFrame, dentro del frame hay un contenedor donde se ponen paneles JPanel, y dentro de los paneles van los componentes visibles como JLabel (texto fijo), JTextField (caja donde el usuario escribe) y JButton (boton). Como se acomodan esos componentes lo decide un layout manager: el JFrame usa BorderLayout por defecto, que reparte la ventana en NORTH, SOUTH, EAST, WEST y CENTER; el JPanel usa FlowLayout, que va poniendo los componentes en fila; y GridLayout arma una cuadricula de filas y columnas. Todo JFrame necesita tres lineas obligatorias o el estudiante creera que su programa no sirve: setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) para que cerrar la ventana termine el programa, setSize o pack para darle tamano, y setVisible(true) para que aparezca. Ademas, la ventana debe crearse dentro de SwingUtilities.invokeLater porque toda la interfaz de Swing vive en un hilo especial llamado EDT; hacerlo bien desde hoy evita cuelgues raros mas adelante.",
            "Error tipico del docente que no domina el tema: abrir el disenador visual de NetBeans, arrastrar tres componentes, hacer doble clic en el boton y escribir toda la logica del negocio dentro de jButton1ActionPerformed. Eso produce una demo bonita en cinco minutos y un curso que no entiende nada, porque el codigo generado esta bloqueado, no se puede editar, y el estudiante nunca ve donde se crea el JFrame ni como se conecta el evento. Escriba la ventana a mano al menos esta primera vez, y deje claro que la ventana solo lee el texto del JTextField y llama a un metodo del registro: la logica y el HashMap viven en la clase de negocio, no en la interfaz. Los otros tropiezos son mecanicos y hay que provocarlos a proposito: olvidar setVisible(true) y quedarse esperando una ventana que nunca aparece; usar setLayout(null) y posicionar todo con coordenadas fijas que se descuadran al cambiar el tamano; y en la parte de mapas, imprimir un HashMap esperando el orden de insercion y no poder explicar por que salio revuelto. Ensaye la clase completa una vez de corrido antes del miercoles, con cronometro, porque el riesgo real de hoy no es tecnico sino de tiempo."
        ],
        "taller": [
            "Bloque de mapas (minutos 10 a 30): cree la clase Expediente con id, nombre, raza, dueno y nota clinica, y la clase RegistroExpedientes con private final Map<String, Expediente> expedientes = new HashMap<>(); verifique guardando los cinco expedientes del escenario e imprimiendo expedientes.size().",
            "Bloque de mapas (minutos 30 a 45): implemente buscar(String id) con get y validacion de null, y guardar(Expediente e) que use containsKey para avisar cuando un ID ya existe antes de que put lo reemplace en silencio; verifique guardando dos veces M-001 y confirmando que el mapa sigue en cinco expedientes y aparece el aviso.",
            "Bloque de conjuntos (minutos 45 a 55): agregue private final Set<String> razas = new HashSet<>(); que se llene automaticamente en cada guardar y aproveche el boolean que devuelve add para avisar cuando la raza ya estaba; verifique que al cargar a Firulais y a Toby, ambos labradores, el conjunto reporta la raza repetida y razas.size() cuenta una sola vez Labrador.",
            "Bloque Swing (minutos 65 a 95): escriba a mano la clase VentanaBuscarExpediente que extiende JFrame, con un JPanel superior que contenga un JLabel, un JTextField y un JButton, y un JLabel central para el resultado; verifique que la ventana abre centrada, con titulo VetCare y que al cerrarla el programa termina.",
            "Integracion (minutos 95 a 115): conecte el boton con addActionListener usando lambda para que lea el ID del JTextField, lo normalice con trim() y toUpperCase(), consulte el HashMap y muestre el expediente en el JLabel central o un JOptionPane de advertencia si no existe, todo dentro de try-catch; capture la ventana con una busqueda exitosa y una fallida y suba el proyecto a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el enunciado del proyecto exige buscar expedientes por ID y tener interfaz grafica, y hoy quedan resueltos los dos requisitos con la misma pieza de codigo.",
            "El HashMap sera el indice en memoria que se reconstruye al cargar el archivo CSV en las clases de persistencia, y el HashSet garantizara que no entren IDs repetidos.",
            "Esta primera ventana es el esqueleto sobre el que se montaran despues el formulario de registro de mascotas y la agenda de citas, por eso se escribe a mano y con la logica separada."
        ],
        "escenario": [
            "El registro arranca precargado con cinco expedientes: M-001 Firulais labrador de Ana Gomez, M-002 Michi criollo de Luis Perez, M-003 Rocky pastor aleman de Ana Gomez, M-004 Nieve persa de Sara Diaz y M-005 Toby labrador de Sara Diaz.",
            "Ademas hay un archivo historico de 5.000 fichas viejas (H-0001 a H-5000) que se usa solo para comparar la busqueda lineal del ArrayList contra el get() del HashMap.",
            "La recepcionista busca por ID escrito en minusculas o con espacios sobrantes, asi que el texto que entra debe limpiarse con trim() y toUpperCase() antes de consultar el mapa.",
            "Ningun estudiante debe usar el disenador visual de NetBeans en esta clase: la ventana se escribe linea por linea para entender la jerarquia frame, panel y componente."
        ],
        "criterios": [
            "La busqueda por ID usa get() del HashMap y no un recorrido de lista, y responde correctamente tanto para un ID existente como para uno inexistente.",
            "Intentar registrar un ID ya existente produce un aviso explicito y el tamano del mapa no cambia por accidente.",
            "La ventana abre centrada, con titulo, con el boton funcionando y termina el programa al cerrarse (setDefaultCloseOperation configurado).",
            "El evento del boton solo lee la entrada y llama al registro: ninguna estructura de datos ni regla de negocio esta escrita dentro del ActionListener."
        ],
        "pistas": [
            "Si al guardar dos veces el mismo ID el mapa sigue teniendo el mismo tamano y nadie aviso nada, que hace put cuando la clave ya existe y con que metodo pudo haberlo detectado antes?",
            "Si compila sin errores pero no aparece ninguna ventana en pantalla, cual es la ultima linea que suele faltar despues de construir el JFrame?",
            "Si el resultado sale correcto en la consola pero el JLabel no cambia, esta llamando al metodo que actualiza el texto del componente o solo esta imprimiendo?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: se declara private final Map<String, Expediente> expedientes = new HashMap<>(); con String como clave porque el ID es texto unico e inmutable, que es la condicion ideal para una clave (si la clave cambia despues de guardarla, el mapa ya no la encuentra). El metodo guardar hace primero if (expedientes.containsKey(e.getId())) { System.out.println(\"Atencion: el ID \" + e.getId() + \" ya existia y sera reemplazado\"); } y luego ejecuta expedientes.put(e.getId(), e). Sin ese containsKey, put pisa el expediente anterior sin decir nada y el tamano del mapa no cambia, que es justo lo que hace invisible el error.",
            "Paso 2 resuelto: buscar queda asi: String clave = id.trim().toUpperCase(); Expediente e = expedientes.get(clave); if (e == null) { avisar que no existe; } else { mostrar e; } La normalizacion es obligatoria porque el HashMap compara las claves de forma exacta: m-001, \" M-001 \" y M-001 producen hashCode distintos y por tanto son tres claves diferentes, aunque para la recepcionista sean la misma mascota. Para demostrar la ganancia en velocidad se construye un archivo historico con 5.000 Expediente y se cronometra con System.nanoTime() la busqueda lineal (for sobre el ArrayList comparando getId) contra indice.get(\"H-5000\"): la primera recorre las 5.000 fichas, la segunda salta directo a la casilla.",
            "Paso 3 resuelto: el conjunto se declara private final Set<String> razas = new HashSet<>(); y dentro de guardar se escribe boolean razaNueva = razas.add(e.getRaza()); if (!razaNueva) { System.out.println(\"Raza ya registrada: \" + e.getRaza()); } Ese boolean es la joya del HashSet: dice si el elemento entro o si ya estaba, sin recorrer nada y sin necesidad de un if previo con contains. Con los datos del escenario, al guardar a Toby (labrador, igual que Firulais) aparece el aviso y razas.size() responde 4, que es el numero de razas distintas que atiende la clinica.",
            "Paso 4 resuelto: la ventana extiende JFrame y en el constructor llama a super(\"VetCare - Buscar expediente\"). Se crea un JPanel superior (que trae FlowLayout por defecto) y se le agregan el JLabel del rotulo, el JTextField de 12 columnas y el JButton. Sobre el frame se llama setLayout(new BorderLayout(10, 10)) y se agregan add(panelSuperior, BorderLayout.NORTH), add(lblResultado, BorderLayout.CENTER) y add(pie, BorderLayout.SOUTH). Se cierra la configuracion con setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE) para que cerrar la ventana termine el proceso, setSize(600, 230) para darle tamano y setLocationRelativeTo(null) para centrarla en pantalla; el setVisible(true) se llama desde el main.",
            "Paso 5 resuelto: el evento se conecta con btnBuscar.addActionListener(e -> buscar()); y ademas con txtId.addActionListener(e -> buscar()); para que la tecla Enter tambien busque. El metodo buscar hace todo dentro de try-catch: toma el texto con txtId.getText().trim().toUpperCase(), lanza IllegalArgumentException si quedo vacio, consulta expedientes.get(id), y si el resultado es null actualiza el JLabel y muestra JOptionPane.showMessageDialog(this, mensaje, \"Sin resultados\", JOptionPane.WARNING_MESSAGE); si existe, pinta los datos con lblResultado.setText(\"<html>...</html>\"), que permite varias lineas dentro de un JLabel. El main arranca con SwingUtilities.invokeLater(() -> new VetCareBuscarExpediente().setVisible(true)) para construir la interfaz en el hilo de eventos (EDT), que es el unico autorizado a tocar componentes Swing."
        ],
        "solucion_rubrica": [
            "RegistroExpedientes con HashMap, busqueda por clave y control de ID duplicado (3)",
            "HashSet de razas aprovechando el boolean de add y reportando razas distintas (2)",
            "Ventana Swing escrita a mano con JFrame, JPanel, JLabel, JTextField, JButton y layout correcto (3)",
            "Evento del boton conectado, try-catch con JOptionPane y evidencia subida a ExamLab (2)"
        ],
        "solucion_errores": [
            "Usar put sin verificar containsKey y quedarse sin entender por que el expediente anterior desaparecio: put reemplaza en silencio cuando la clave ya existe.",
            "Construir el JFrame completo y olvidar setVisible(true) o setDefaultCloseOperation, con lo cual la ventana no aparece o el programa sigue corriendo despues de cerrarla.",
            "Escribir la busqueda, la coleccion de expedientes y las validaciones dentro del ActionListener del boton, dejando la clase de negocio vacia y haciendo imposible reutilizar la logica en la persistencia."
        ],
        "codigo_slide_titulo": "El mapa busca; la ventana solo pregunta",
        "codigo_slide_lineas": [
            "Map<String, Expediente> fichas = new HashMap<>();   // clave = ID unico",
            "fichas.put(\"M-001\", firulais);                      // put REEMPLAZA si la clave existe",
            "Expediente e = fichas.get(\"M-004\");                 // O(1) promedio: no recorre nada",
            "if (e == null) { /* la clave no existe: validar SIEMPRE */ }",
            "",
            "Set<String> razas = new HashSet<>();",
            "boolean nueva = razas.add(\"Labrador\");              // false si ya estaba: sin duplicados",
            "",
            "JFrame v = new JFrame(\"VetCare\");                   // 1) la ventana",
            "JPanel p = new JPanel();                            // 2) el panel contenedor",
            "JTextField txtId = new JTextField(12);              // 3) los componentes",
            "JButton btn = new JButton(\"Buscar\");",
            "p.add(new JLabel(\"ID:\")); p.add(txtId); p.add(btn);",
            "v.add(p, BorderLayout.NORTH);",
            "btn.addActionListener(ev -> buscar());              // la GUI llama, NO calcula",
            "v.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);",
            "v.setVisible(true);                                 // sin esta linea no aparece nada"
        ],
        "codigo_slide_caption": "El HashMap guarda la inteligencia y la ventana solo pregunta: si la logica se le mete al boton, el sistema deja de ser reutilizable.",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare se ejecuta expedientes.put(\"M-001\", nuevoExpediente) cuando la clave M-001 ya existia. Que ocurre?",
                "opciones": [
                    "A) Lanza una excepcion de clave duplicada",
                    "B) Se ignora la operacion y el mapa queda igual",
                    "C) Reemplaza el valor anterior en silencio y devuelve el que estaba",
                    "D) Guarda los dos expedientes bajo la misma clave y size() aumenta en 1"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual es la principal ventaja de buscar el expediente H-5000 con HashMap frente a recorrer un ArrayList de 5.000 fichas?",
                "opciones": [
                    "A) Que el HashMap ordena alfabeticamente los expedientes por su clave",
                    "B) Que el tiempo de busqueda no depende de la cantidad de elementos, porque la clave calcula la posicion",
                    "C) Que el HashMap siempre ocupa menos memoria que el ArrayList",
                    "D) Que el ArrayList no permite guardar objetos Expediente"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Al guardar a Toby (labrador) cuando Firulais (labrador) ya estaba, que devuelve razas.add(\"Labrador\")?",
                "opciones": [
                    "A) true, porque add siempre inserta el elemento",
                    "B) false, y el conjunto queda igual con una sola vez la raza Labrador",
                    "C) true, y reemplaza el elemento anterior por el nuevo",
                    "D) Lanza IllegalStateException por elemento duplicado"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual linea es indispensable para que la ventana de VetCare aparezca en pantalla?",
                "opciones": [
                    "A) frame.setSize(600, 230)",
                    "B) frame.setLocationRelativeTo(null)",
                    "C) frame.setVisible(true)",
                    "D) frame.setTitle(\"VetCare\")"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Un HashMap conserva el orden en que se insertaron las claves, por eso al imprimirlo salen en el mismo orden en que se hizo put.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "En Swing la jerarquia habitual es JFrame que contiene JPanel y el JPanel contiene los componentes como JLabel, JTextField y JButton.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Explique por que en la ventana de VetCare el ActionListener del boton no debe contener la logica de busqueda ni la estructura de datos.",
                "clave": "Porque la interfaz solo debe leer la entrada del usuario y mostrar resultados; si el HashMap y las reglas viven dentro del boton, esa logica no se puede reutilizar desde la persistencia en archivo, ni probar, ni cambiar de interfaz. Separar capas permite que la misma clase RegistroExpedientes sirva para consola, ventana y archivo CSV."
            },
            {
                "tipo": "abierta",
                "q": "Que precaucion hay que tomar con el texto que escribe la recepcionista antes de consultar el HashMap y por que?",
                "clave": "Hay que limpiarlo con trim() y normalizarlo con toUpperCase(), porque el HashMap compara las claves de forma exacta y distingue mayusculas de minusculas y espacios: m-001, ' M-001 ' y M-001 serian claves diferentes y get devolveria null aunque el expediente exista."
            }
        ],
        "codigo_fuente": "package vetcare;\n\nimport java.awt.BorderLayout;\nimport java.awt.Font;\nimport java.util.ArrayList;\nimport java.util.HashMap;\nimport java.util.HashSet;\nimport java.util.List;\nimport java.util.Map;\nimport java.util.Set;\nimport javax.swing.JButton;\nimport javax.swing.JFrame;\nimport javax.swing.JLabel;\nimport javax.swing.JOptionPane;\nimport javax.swing.JPanel;\nimport javax.swing.JTextField;\nimport javax.swing.SwingConstants;\nimport javax.swing.SwingUtilities;\n\n/**\n * VetCare - Clase 4: HashMap + HashSet + primera ventana Swing.\n * Clinica Veterinaria Huellitas.\n * Ventana escrita A MANO (sin el disenador visual) para entender la jerarquia.\n * Archivo unico: clic derecho sobre el archivo > Run File (Shift+F6) en NetBeans.\n */\npublic class VetCareBuscarExpediente extends JFrame {\n\n    // ---- Datos: la inteligencia del sistema vive aqui, no en el boton ----\n    private final Map<String, Expediente> expedientes = new HashMap<>();\n    private final Set<String> razas = new HashSet<>();\n\n    // ---- Componentes de la interfaz ----\n    private final JTextField txtId = new JTextField(12);\n    private final JButton btnBuscar = new JButton(\"Buscar expediente\");\n    private final JLabel lblResultado = new JLabel(\"Escriba un ID (ej: M-002) y presione Buscar\", SwingConstants.CENTER);\n\n    public VetCareBuscarExpediente() {\n        super(\"VetCare - Buscar expediente\");\n        cargarDatosDePrueba();\n        compararBusquedas();\n        construirInterfaz();\n    }\n\n    private void cargarDatosDePrueba() {\n        guardar(new Expediente(\"M-001\", \"Firulais\", \"Labrador\", \"Ana Gomez\", \"Vacunacion al dia\"));\n        guardar(new Expediente(\"M-002\", \"Michi\", \"Criollo\", \"Luis Perez\", \"Control de peso\"));\n        guardar(new Expediente(\"M-003\", \"Rocky\", \"Pastor Aleman\", \"Ana Gomez\", \"Revision de patas\"));\n        guardar(new Expediente(\"M-004\", \"Nieve\", \"Persa\", \"Sara Diaz\", \"Desparasitacion\"));\n        guardar(new Expediente(\"M-005\", \"Toby\", \"Labrador\", \"Sara Diaz\", \"Control geriatrico\"));\n        System.out.println(\"Expedientes: \" + expedientes.size() + \" | Razas distintas: \" + razas.size());\n    }\n\n    /** Regla de negocio: avisar antes de que put reemplace en silencio. */\n    private void guardar(Expediente e) {\n        if (expedientes.containsKey(e.getId())) {\n            System.out.println(\"Atencion: el ID \" + e.getId() + \" ya existia y sera reemplazado\");\n        }\n        expedientes.put(e.getId(), e);              // clave -> valor\n        boolean razaNueva = razas.add(e.getRaza()); // add devuelve false si ya estaba\n        if (!razaNueva) {\n            System.out.println(\"Raza ya registrada: \" + e.getRaza());\n        }\n    }\n\n    /** Demo del dia: recorrer 5.000 fichas contra preguntarle la clave al mapa. */\n    private void compararBusquedas() {\n        List<Expediente> archivoHistorico = new ArrayList<>();\n        Map<String, Expediente> indice = new HashMap<>();\n        for (int i = 1; i <= 5000; i++) {\n            Expediente e = new Expediente(\"H-\" + i, \"Paciente \" + i, \"Criollo\",\n                    \"Dueno \" + i, \"Archivo historico\");\n            archivoHistorico.add(e);\n            indice.put(e.getId(), e);\n        }\n        String buscado = \"H-5000\"; // peor caso: la ultima ficha del archivo\n\n        long t1 = System.nanoTime();\n        Expediente porRecorrido = null;\n        for (Expediente e : archivoHistorico) {   // busqueda lineal: compara una por una\n            if (e.getId().equals(buscado)) {\n                porRecorrido = e;\n                break;\n            }\n        }\n        long nsLineal = System.nanoTime() - t1;\n\n        long t2 = System.nanoTime();\n        Expediente porClave = indice.get(buscado); // busqueda por clave: no recorre nada\n        long nsMapa = System.nanoTime() - t2;\n\n        System.out.println(\"ArrayList recorriendo 5.000: encontrado=\" + (porRecorrido != null)\n                + \" en \" + nsLineal + \" ns\");\n        System.out.println(\"HashMap con get(clave):      encontrado=\" + (porClave != null)\n                + \" en \" + nsMapa + \" ns\");\n    }\n\n    private void construirInterfaz() {\n        JPanel panelSuperior = new JPanel();           // FlowLayout por defecto\n        panelSuperior.add(new JLabel(\"ID de la mascota:\"));\n        panelSuperior.add(txtId);\n        panelSuperior.add(btnBuscar);\n\n        lblResultado.setFont(new Font(\"SansSerif\", Font.PLAIN, 14));\n\n        JLabel pie = new JLabel(\"Expedientes cargados: \" + expedientes.size()\n                + \"  |  Razas distintas: \" + razas.size(), SwingConstants.CENTER);\n\n        setLayout(new BorderLayout(10, 10));           // el JFrame usa BorderLayout\n        add(panelSuperior, BorderLayout.NORTH);\n        add(lblResultado, BorderLayout.CENTER);\n        add(pie, BorderLayout.SOUTH);\n\n        btnBuscar.addActionListener(e -> buscar());    // el evento solo delega\n        txtId.addActionListener(e -> buscar());        // Enter tambien busca\n\n        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n        setSize(600, 230);\n        setLocationRelativeTo(null);                   // centrada en pantalla\n    }\n\n    /** Lee la entrada, consulta el mapa y pinta el resultado. Nada mas. */\n    private void buscar() {\n        try {\n            String id = txtId.getText().trim().toUpperCase();\n            if (id.isEmpty()) {\n                throw new IllegalArgumentException(\"Debe escribir un ID, por ejemplo M-002\");\n            }\n            Expediente e = expedientes.get(id);        // busqueda por clave, sin recorrer\n            if (e == null) {                           // get devuelve null si no existe\n                lblResultado.setText(\"No existe expediente con ID \" + id);\n                JOptionPane.showMessageDialog(this,\n                        \"No existe expediente con ID \" + id,\n                        \"Sin resultados\", JOptionPane.WARNING_MESSAGE);\n                return;\n            }\n            lblResultado.setText(\"<html><b>\" + e.getNombre() + \"</b> (\" + e.getRaza() + \")<br>\"\n                    + \"Dueno: \" + e.getDueno() + \"<br>Nota clinica: \" + e.getNota() + \"</html>\");\n        } catch (IllegalArgumentException ex) {\n            JOptionPane.showMessageDialog(this, ex.getMessage(),\n                    \"Dato invalido\", JOptionPane.ERROR_MESSAGE);\n        }\n    }\n\n    public static void main(String[] args) {\n        // La interfaz se construye en el hilo de eventos de Swing (EDT)\n        SwingUtilities.invokeLater(() -> new VetCareBuscarExpediente().setVisible(true));\n    }\n}\n\nclass Expediente {\n\n    private final String id;\n    private final String nombre;\n    private final String raza;\n    private final String dueno;\n    private final String nota;\n\n    public Expediente(String id, String nombre, String raza, String dueno, String nota) {\n        this.id = id;\n        this.nombre = nombre;\n        this.raza = raza;\n        this.dueno = dueno;\n        this.nota = nota;\n    }\n\n    public String getId() { return id; }\n    public String getNombre() { return nombre; }\n    public String getRaza() { return raza; }\n    public String getDueno() { return dueno; }\n    public String getNota() { return nota; }\n\n    @Override\n    public String toString() {\n        return id + \" | \" + nombre + \" (\" + raza + \") - dueno: \" + dueno + \" - \" + nota;\n    }\n}\n",
        "codigo_archivo": "VetCareBuscarExpediente.java"
    },
    {
        "n": 5,
        "slug": "Parcial 1",
        "titulo": "Parcial 1",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    },
    {
        "n": 6,
        "slug": "Eventos y controladores ActionListener",
        "titulo": "Eventos y controladores · ActionListener",
        "subtitulo": "El boton que de verdad guarda",
        "herramienta": "Apache NetBeans",
        "hito_pi": "El formulario de VetCare queda conectado: al oprimir 'Registrar mascota' el objeto entra al ArrayList y el listado en pantalla se actualiza.",
        "entregable": "Proyecto VetCare con la ventana de registro operativa y la clase ControladorRegistro separada de la vista, comprimido y subido a ExamLab.",
        "demo": "El docente oprime el boton en NetBeans y muestra en vivo como la mascota pasa del formulario al ArrayList, incluyendo que pasa cuando la edad se escribe como texto.",
        "teoria": [
            "Hasta ahora los programas de VetCare corrian en linea recta: el main llamaba un metodo, ese metodo llamaba a otro y el programa terminaba. Una aplicacion con ventanas no funciona asi. Cuando usted hace setVisible(true), Swing arranca un hilo especial llamado EDT (Event Dispatch Thread) que se queda vivo esperando que el usuario haga algo: mover el mouse, escribir en un campo, oprimir un boton. Cada una de esas acciones se convierte en un objeto de evento que entra a una cola, y Swing va sacando esos eventos uno por uno y le avisa al objeto que previamente dijo 'a mi me interesa ese boton'. Eso es programacion dirigida por eventos: usted ya no decide cuando corre su codigo; usted lo deja escrito y registrado, y quien decide cuando se ejecuta es la recepcionista de Huellitas el dia que oprima 'Registrar mascota'. Por eso el metodo que guarda la mascota nunca aparece llamado desde el main: aparece registrado, no llamado, y esa diferencia es la que hay que entender hoy.",
            "ActionListener es una interfaz de java.awt.event que tiene un solo metodo: void actionPerformed(ActionEvent e). Implementarla es firmar un contrato que dice 'yo se reaccionar a una accion'. El registro se hace con btnRegistrar.addActionListener(objetoQueEscucha): desde esa linea el boton guarda una referencia a su objeto y, cuando lo oprimen, Swing invoca actionPerformed pasandole un ActionEvent con informacion del disparo (quien lo genero, en que instante, con que comando). Hay tres formas validas de escribirlo en NetBeans y conviene mostrarlas todas: una clase aparte que implements ActionListener, una clase anonima escrita ahi mismo con new ActionListener() { ... }, o una expresion lambda e -> registrar() si el proyecto esta en Java 8 o superior. Un detalle practico que confunde a medio salon: si usted arma la ventana con el diseñador visual y hace doble clic sobre el boton, NetBeans le genera automaticamente el metodo btnRegistrarActionPerformed y deja el addActionListener dentro del bloque gris protegido. Ese bloque no se edita a mano, pero el metodo generado si es suyo y ahi adentro va su llamada.",
            "Separar la logica de la interfaz significa que la ventana no conoce reglas de negocio y que las reglas no saben que existe una ventana. En VetCare vamos a tener tres capas claras: el modelo (Mascota, Dueno, Cita), que solo guarda datos y comportamiento propio; el servicio o controlador (ControladorRegistro, RepositorioMascotas), donde viven las validaciones, la busqueda por ID y el ArrayList; y la vista (VentanaRegistroMascota), que unicamente pinta campos, lee texto y muestra mensajes. La prueba acida es esta pregunta: si mañana Huellitas pide la misma funcionalidad en consola, o migramos a JavaFX, cuanto codigo hay que reescribir? Si la respuesta es 'solamente la ventana', el diseño esta bien. Si toca reescribir todo porque la conversion de la edad estaba adentro del boton, el diseño esta mal. Y hay una razon adicional que se vuelve evidente en la clase 8: a un ControladorRegistro se le pueden hacer pruebas automaticas; a un boton no se le puede.",
            "Vale la pena desarmar en camara lenta lo que ocurre en un click de 'Registrar mascota'. Primero la vista lee texto crudo: txtId.getText(), txtNombre.getText(), txtEdad.getText(); todo lo que sale de un JTextField es String, incluida la edad. Segundo, ese texto viaja al controlador, que hace el trabajo sucio: recorta espacios con trim(), rechaza campos vacios, convierte la edad con Integer.parseInt dentro de un try-catch porque si la auxiliar escribio 'tres' salta NumberFormatException, y le pregunta al repositorio si ese ID ya existe. Tercero, si algo esta mal el controlador lanza una excepcion con un mensaje entendible para un humano ('La edad debe ser un numero entero'); si todo esta bien, construye el objeto Mascota y lo agrega al ArrayList. Cuarto, la vista atrapa esa excepcion y la convierte en un JOptionPane, o, si no hubo error, limpia los campos y refresca el area de listado. Ese ciclo leer-validar-delegar-refrescar es exactamente el mismo que vamos a repetir despues para agendar citas, para buscar expedientes y para guardar en archivo.",
            "Dos detalles mas que le van a servir. El ActionEvent trae e.getSource(), que devuelve el componente que disparo el evento; eso permite que un mismo listener atienda varios botones y decida con un if (e.getSource() == btnBuscar). Es comodo, pero uselo con cabeza: si el metodo se llena de ifs, es mas limpio un listener por boton. Ademas de ActionListener existen otros escuchadores que ya vamos a necesitar en VetCare: ItemListener para el JComboBox de especie, ListSelectionListener para cuando el usuario selecciona una fila del listado de mascotas, y WindowListener para preguntar 'desea guardar antes de salir' cuando lleguemos a persistencia. Y una advertencia de rendimiento: todo lo que usted escriba dentro de actionPerformed corre en el EDT, el mismo hilo que dibuja la ventana; si ahi mete una tarea larga, la interfaz se congela y el usuario cree que el programa se colgo. Para eso existe SwingWorker. Por ahora la regla es simple: listeners cortos que solo leen, delegan y muestran.",
            "Error tipico del docente que no domina el tema: escribir toda la aplicacion adentro de actionPerformed y, peor aun, crear el repositorio dentro del listener. Se ve asi de inocente: 'RepositorioMascotas repo = new RepositorioMascotas();' como primera linea del boton. Compila, no marca error, el estudiante registra dos mascotas y la lista siempre muestra una sola, y el docente termina diciendo en voz alta que 'ArrayList no esta guardando'. Lo que realmente pasa es que en cada click se construye un repositorio vacio nuevo y el anterior se lo lleva el recolector de basura: la coleccion tiene que ser un atributo de la ventana o del controlador, creado una sola vez. El segundo error de la misma familia es pelearse con el bloque gris que NetBeans protege tratando de escribir ahi el addActionListener, cuando lo que hay que editar es el metodo generado. Y el tercero es capturar Exception con un catch vacio: la aplicacion no se cae, pero tampoco avisa nada, y el error se vuelve invisible para el estudiante y para usted."
        ],
        "taller": [
            "Cree el paquete vetcare.vista y dentro la clase VentanaRegistroMascota que extiende JFrame, con los campos ID, nombre, especie y edad, el boton 'Registrar mascota' y un JTextArea de solo lectura para el listado; ejecutela y verifique que abre centrada y que cierra con EXIT_ON_CLOSE.",
            "Deje Mascota en vetcare.modelo y cree en vetcare.servicio la clase RepositorioMascotas con un ArrayList<Mascota> privado y los metodos registrar, buscarPorId, listar y total; compruebe con Ctrl+F que ninguna de esas dos clases tiene un import de javax.swing.",
            "Cree ControladorRegistro con el metodo registrarMascota(String id, String nombre, String especie, String edadTexto) que valide obligatorios, convierta la edad con Integer.parseInt dentro de try-catch y lance IllegalArgumentException con mensajes en español; el repositorio debe recibirse por el constructor, no crearse adentro del metodo.",
            "Conecte el boton con addActionListener de manera que el cuerpo del listener tenga maximo cinco lineas: leer los getText(), llamar al controlador, refrescar el area, limpiar campos y mostrar el JOptionPane; declare el controlador como atributo de la ventana, nunca dentro del listener.",
            "Pruebe y capture evidencia de tres casos: (a) registro valido de M-001 Kira, (b) edad escrita como 'tres', (c) ID repetido M-001; guarde las tres capturas, exporte el proyecto comprimido y subalo a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el PI exige interfaz grafica y manejo de errores con try-catch; hoy es la clase donde la ventana deja de ser un dibujo bonito y empieza a mover datos reales de la coleccion de mascotas.",
            "La separacion vista-controlador que hacemos hoy es la que permitira, en la clase 8, escribir pruebas automaticas sin abrir una sola ventana.",
            "Todo lo que falta del PI (agendar cita, buscar expediente por ID, guardar en archivo) repite exactamente el mismo ciclo: leer, validar, delegar, refrescar."
        ],
        "escenario": [
            "El proyecto VetCare ya tiene la clase Mascota (id, nombre, especie, edad) y un ArrayList que hasta hoy se llenaba con datos quemados dentro del main.",
            "La ventana de registro ya existe pero el boton 'Registrar mascota' no hace nada: se oprime y la pantalla queda igualita.",
            "Datos de partida para las pruebas de hoy: la clinica Huellitas necesita registrar a M-001 Kira (perro, 4), M-002 Michi (gato, 2) y M-003 Rocky (perro, 7)."
        ],
        "criterios": [
            "Al oprimir 'Registrar mascota' la mascota aparece en el listado y el total aumenta en uno por cada registro exitoso.",
            "Ninguna clase de los paquetes modelo o servicio importa javax.swing, y el cuerpo del listener no contiene ninguna validacion ni conversion de datos.",
            "Escribir 'tres' en el campo edad muestra un mensaje entendible en un JOptionPane y la aplicacion sigue funcionando, sin traza roja en la consola de NetBeans.",
            "Intentar registrar un ID que ya existe es rechazado con mensaje y la lista no queda con dos mascotas con el mismo ID."
        ],
        "pistas": [
            "Si oprime el boton dos veces y el listado siempre muestra un solo registro: en que linea exacta se esta creando el ArrayList y cuantas veces se ejecuta esa linea?",
            "Si borra el import de javax.swing de su controlador, el proyecto sigue compilando? Que le dice esa respuesta sobre donde quedo la logica?",
            "Cuando la edad llega como 'tres', quien deberia darse cuenta primero del problema (el JTextField, el controlador o el usuario) y en que orden viajan la excepcion y el mensaje?"
        ],
        "solucion_pasos": [
            "Declare el estado como atributo y no como variable local. En VentanaRegistroMascota, arriba de todo, escriba: private final ControladorRegistro controlador = new ControladorRegistro(new RepositorioMascotas()); Al ser atributo se construye una sola vez, cuando nace la ventana, y sobrevive a todos los clicks porque vive mientras viva el objeto ventana. Este es justamente el error que hace creer que 'el ArrayList no guarda': si esa misma linea queda adentro del listener, en cada click se crea un repositorio nuevo, vacio, y el anterior queda huerfano para el recolector de basura.",
            "Registre el escuchador en el constructor de la ventana y delegue de inmediato a un metodo privado. Escriba: btnRegistrar.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { registrar(); } }); Note que addActionListener no ejecuta nada: solo deja anotado que ese objeto quiere enterarse. Como el cuerpo del listener tiene una sola linea, el listener no crece nunca y el metodo registrar() se puede leer completo en pantalla. Si usted arma la ventana con el diseñador de NetBeans, es exactamente igual: la unica linea que escribe dentro del metodo generado btnRegistrarActionPerformed es registrar();.",
            "Escriba el metodo privado registrar() con la estructura leer-delegar-mostrar y nada mas. Dentro de un try llama a controlador.registrarMascota(txtId.getText(), txtNombre.getText(), txtEspecie.getText(), txtEdad.getText()); si el controlador devuelve la mascota, la vista refresca el area con areaListado.setText(controlador.reporteListado()), limpia los campos y muestra un JOptionPane con el nombre guardado; en el catch (IllegalArgumentException ex) muestra ex.getMessage() con JOptionPane.WARNING_MESSAGE. Fijese en el detalle que hay que decir en voz alta: la vista captura una excepcion y la pinta, pero no valida absolutamente nada.",
            "Ponga todas las reglas en el controlador, que es la clase que no importa javax.swing. Ahi va: rechazar id y nombre vacios con trim().isEmpty() lanzando IllegalArgumentException con mensaje en español; convertir la edad con Integer.parseInt(edadTexto.trim()) envuelto en try-catch de NumberFormatException para relanzar IllegalArgumentException con el texto 'La edad debe ser un numero entero'; validar que la edad este entre 0 y 40 anios; y solo cuando todo paso, construir new Mascota(...) y llamar repositorio.registrar(mascota). El repositorio, por su parte, es el unico responsable del ID duplicado: antes de agregar consulta buscarPorId y, si encuentra algo, lanza 'Ya existe una mascota con el ID M-001'. Asi cada regla vive en una sola clase y no se repite.",
            "Refresque y verifique con los tres casos del taller. El refresco se hace con areaListado.setText(controlador.reporteListado()), y reporteListado recorre repositorio.listar() armando el texto con un StringBuilder y agregando al final 'Total registradas: N'. Registre M-001 Kira, 4 (debe aparecer en el area y el total decir 1); luego escriba la edad 'tres' (debe salir el JOptionPane de edad invalida, el total sigue en 1 y la consola de NetBeans queda limpia, sin traza roja); luego intente M-001 otra vez (mensaje de ID repetido, total sigue en 1). Si los tres casos se comportan asi, el ciclo leer-validar-delegar-refrescar quedo bien armado y es el mismo que reutilizara para las citas."
        ],
        "solucion_rubrica": [
            "Ventana con formulario, boton y listado funcionando (2)",
            "Listener corto que solo lee, delega y muestra (3)",
            "ControladorRegistro y RepositorioMascotas sin dependencia de Swing (3)",
            "Manejo de errores con try-catch y evidencia de los tres casos (2)"
        ],
        "solucion_errores": [
            "Crear el repositorio o el ArrayList dentro del listener, con lo cual cada click arranca con una coleccion vacia y parece que nada se guarda.",
            "Usar Integer.parseInt sin try-catch: la excepcion sube al EDT, se pinta una traza roja en la consola de NetBeans y el usuario no ve ningun mensaje.",
            "Escribir la validacion dentro de actionPerformed y llenar la vista de ifs, de modo que la misma regla se vuelve a copiar y pegar en la ventana de citas."
        ],
        "codigo_slide_titulo": "El listener que solo lee, delega y muestra",
        "codigo_slide_lineas": [
            "private final ControladorRegistro controlador =",
            "        new ControladorRegistro(new RepositorioMascotas());  // ATRIBUTO: una sola vez",
            "",
            "btnRegistrar.addActionListener(new ActionListener() {        // se registra, no se llama",
            "    @Override",
            "    public void actionPerformed(ActionEvent e) {             // lo invoca Swing, en el EDT",
            "        try {",
            "            Mascota m = controlador.registrarMascota(        // la regla vive afuera",
            "                    txtId.getText(), txtNombre.getText(),",
            "                    txtEspecie.getText(), txtEdad.getText());",
            "            areaListado.setText(controlador.reporteListado());",
            "            JOptionPane.showMessageDialog(null, \"Guardada: \" + m.getNombre());",
            "        } catch (IllegalArgumentException ex) {              // el error no tumba la app",
            "            JOptionPane.showMessageDialog(null, ex.getMessage());",
            "        }",
            "    }",
            "});"
        ],
        "codigo_slide_caption": "El boton no sabe reglas: lee texto, delega en el controlador y muestra el resultado o el error.",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cuando el usuario oprime un JButton que tiene un ActionListener registrado, que metodo se ejecuta?",
                "opciones": [
                    "A) main",
                    "B) actionPerformed",
                    "C) addActionListener",
                    "D) setVisible"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual linea conecta el boton 'Registrar mascota' con el objeto que va a reaccionar?",
                "opciones": [
                    "A) btnRegistrar.setText(\"Registrar mascota\")",
                    "B) btnRegistrar.addActionListener(escucha)",
                    "C) btnRegistrar.actionPerformed(escucha)",
                    "D) escucha.addActionListener(btnRegistrar)"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "El programador es quien llama directamente al metodo actionPerformed cada vez que quiere procesar un click.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Que excepcion lanza Integer.parseInt cuando el campo edad de VetCare trae el texto 'tres'?",
                "opciones": [
                    "A) IOException",
                    "B) NullPointerException",
                    "C) NumberFormatException",
                    "D) ArithmeticException"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Si dentro del listener se escribe 'RepositorioMascotas repo = new RepositorioMascotas();', por que el listado siempre muestra una sola mascota?",
                "opciones": [
                    "A) Porque un ArrayList solo admite un elemento a la vez",
                    "B) Porque en cada click se crea un repositorio vacio nuevo y se pierde el anterior",
                    "C) Porque falta llamar a pack() despues de registrar",
                    "D) Porque setText reemplaza el texto en vez de agregarlo al final"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Poner toda la validacion y la regla de negocio dentro de actionPerformed impide reutilizar y probar esa logica sin abrir la ventana.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Explique con sus palabras que hace addActionListener y quien termina ejecutando el codigo que usted escribio adentro.",
                "clave": "addActionListener registra (suscribe) un objeto escuchador en el boton; el codigo no lo llama el programador sino Swing, desde el hilo de eventos (EDT), cuando el usuario dispara la accion."
            },
            {
                "tipo": "abierta",
                "q": "Escriba las tres responsabilidades que SI le corresponden al metodo del boton en VetCare y una que NO.",
                "clave": "SI: leer el texto de los campos, delegar en el controlador y mostrar el resultado o el mensaje de error (refrescar y limpiar). NO: validar datos, convertir tipos, decidir si el ID esta repetido ni manipular directamente el ArrayList."
            }
        ],
        "codigo_fuente": "package vetcare.eventos;\n\nimport java.awt.BorderLayout;\nimport java.awt.GridLayout;\nimport java.awt.event.ActionEvent;\nimport java.awt.event.ActionListener;\nimport java.util.ArrayList;\nimport java.util.List;\nimport javax.swing.JButton;\nimport javax.swing.JFrame;\nimport javax.swing.JLabel;\nimport javax.swing.JOptionPane;\nimport javax.swing.JPanel;\nimport javax.swing.JScrollPane;\nimport javax.swing.JTextArea;\nimport javax.swing.JTextField;\nimport javax.swing.SwingUtilities;\n\n/** Clase 6 de VetCare: el boton Registrar mascota que de verdad guarda. */\npublic class VetCareEventosDemo {\n\n    public static void main(String[] args) {\n        SwingUtilities.invokeLater(new Runnable() {\n            @Override\n            public void run() {\n                new VentanaRegistroMascota().setVisible(true);\n            }\n        });\n    }\n}\n\n/** Modelo: una mascota del expediente de la clinica Huellitas. */\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private final String especie;\n    private final int edad;\n\n    public Mascota(String id, String nombre, String especie, int edad) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n        this.edad = edad;\n    }\n\n    public String getId() { return id; }\n\n    public String getNombre() { return nombre; }\n\n    public String getEspecie() { return especie; }\n\n    public int getEdad() { return edad; }\n\n    @Override\n    public String toString() {\n        return id + \" | \" + nombre + \" (\" + especie + \", \" + edad + \" anios)\";\n    }\n}\n\n/** Servicio: guarda las mascotas en memoria. No sabe que existen ventanas. */\nclass RepositorioMascotas {\n\n    private final List<Mascota> mascotas = new ArrayList<Mascota>();\n\n    public void registrar(Mascota mascota) {\n        if (mascota == null) {\n            throw new IllegalArgumentException(\"No se puede registrar una mascota nula.\");\n        }\n        if (buscarPorId(mascota.getId()) != null) {\n            throw new IllegalArgumentException(\"Ya existe una mascota con el ID \" + mascota.getId());\n        }\n        mascotas.add(mascota);\n    }\n\n    public Mascota buscarPorId(String id) {\n        for (Mascota m : mascotas) {\n            if (m.getId().equalsIgnoreCase(id)) {\n                return m;\n            }\n        }\n        return null;\n    }\n\n    public List<Mascota> listar() { return new ArrayList<Mascota>(mascotas); }\n\n    public int total() { return mascotas.size(); }\n}\n\n/** Controlador: traduce el texto de la pantalla a objetos del dominio y valida. */\nclass ControladorRegistro {\n\n    private final RepositorioMascotas repositorio;\n\n    public ControladorRegistro(RepositorioMascotas repositorio) {\n        if (repositorio == null) {\n            throw new IllegalArgumentException(\"El controlador necesita un repositorio.\");\n        }\n        this.repositorio = repositorio;\n    }\n\n    public Mascota registrarMascota(String id, String nombre, String especie, String edadTexto) {\n        if (id == null || id.trim().isEmpty()) {\n            throw new IllegalArgumentException(\"El ID de la mascota es obligatorio.\");\n        }\n        if (nombre == null || nombre.trim().isEmpty()) {\n            throw new IllegalArgumentException(\"El nombre de la mascota es obligatorio.\");\n        }\n        int edad;\n        try {\n            edad = Integer.parseInt(edadTexto == null ? \"\" : edadTexto.trim());\n        } catch (NumberFormatException e) {\n            throw new IllegalArgumentException(\"La edad debe ser un numero entero. Se recibio: \" + edadTexto);\n        }\n        if (edad < 0 || edad > 40) {\n            throw new IllegalArgumentException(\"La edad debe estar entre 0 y 40 anios.\");\n        }\n        String especieLimpia = (especie == null || especie.trim().isEmpty())\n                ? \"Sin especificar\" : especie.trim();\n        Mascota mascota = new Mascota(id.trim(), nombre.trim(), especieLimpia, edad);\n        repositorio.registrar(mascota);\n        return mascota;\n    }\n\n    public String reporteListado() {\n        StringBuilder sb = new StringBuilder();\n        for (Mascota m : repositorio.listar()) {\n            sb.append(m.toString()).append(System.lineSeparator());\n        }\n        sb.append(\"Total registradas: \").append(repositorio.total());\n        return sb.toString();\n    }\n}\n\n/** Vista: captura datos, delega y muestra resultados. Nada mas. */\nclass VentanaRegistroMascota extends JFrame {\n\n    private final JTextField txtId = new JTextField();\n    private final JTextField txtNombre = new JTextField();\n    private final JTextField txtEspecie = new JTextField();\n    private final JTextField txtEdad = new JTextField();\n    private final JTextArea areaListado = new JTextArea(10, 32);\n    private final JButton btnRegistrar = new JButton(\"Registrar mascota\");\n\n    private final ControladorRegistro controlador =\n            new ControladorRegistro(new RepositorioMascotas());\n\n    public VentanaRegistroMascota() {\n        super(\"VetCare - Registro de mascotas\");\n        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n        setLayout(new BorderLayout());\n\n        JPanel formulario = new JPanel(new GridLayout(5, 2, 6, 6));\n        formulario.add(new JLabel(\"ID (ej. M-001):\"));\n        formulario.add(txtId);\n        formulario.add(new JLabel(\"Nombre:\"));\n        formulario.add(txtNombre);\n        formulario.add(new JLabel(\"Especie:\"));\n        formulario.add(txtEspecie);\n        formulario.add(new JLabel(\"Edad (anios):\"));\n        formulario.add(txtEdad);\n        formulario.add(new JLabel(\"\"));\n        formulario.add(btnRegistrar);\n\n        areaListado.setEditable(false);\n        add(formulario, BorderLayout.NORTH);\n        add(new JScrollPane(areaListado), BorderLayout.CENTER);\n\n        btnRegistrar.addActionListener(new ActionListener() {\n            @Override\n            public void actionPerformed(ActionEvent e) {\n                registrar();\n            }\n        });\n\n        pack();\n        setLocationRelativeTo(null);\n    }\n\n    private void registrar() {\n        try {\n            Mascota mascota = controlador.registrarMascota(\n                    txtId.getText(), txtNombre.getText(), txtEspecie.getText(), txtEdad.getText());\n            areaListado.setText(controlador.reporteListado());\n            limpiar();\n            JOptionPane.showMessageDialog(this, \"Mascota registrada: \" + mascota.getNombre());\n        } catch (IllegalArgumentException ex) {\n            JOptionPane.showMessageDialog(this, ex.getMessage(),\n                    \"Datos invalidos\", JOptionPane.WARNING_MESSAGE);\n        }\n    }\n\n    private void limpiar() {\n        txtId.setText(\"\");\n        txtNombre.setText(\"\");\n        txtEspecie.setText(\"\");\n        txtEdad.setText(\"\");\n        txtId.requestFocus();\n    }\n}\n",
        "codigo_archivo": "VetCareEventosDemo.java"
    },
    {
        "n": 7,
        "slug": "Patrones de diseno Singleton y Factory",
        "titulo": "Patrones de diseno · Singleton y Factory",
        "subtitulo": "Soluciones con nombre a problemas que ya nos pasaron",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.",
        "entregable": "Clase RepositorioVetCare convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.",
        "demo": "El docente abre dos ventanas de VetCare, registra una mascota en la primera y la muestra apareciendo en la segunda porque ambas comparten la unica instancia del repositorio.",
        "teoria": [
            "Un patron de diseño no es una libreria que se importa ni un archivo que se descarga: es una solucion probada, con nombre propio, a un problema de diseño que se repite. La analogia que mejor funciona es la de arquitectura: cuando un arquitecto dice 'aqui va un patio interior', nadie le pide los planos del patio, porque el nombre ya comunica el problema (ventilar e iluminar el centro de la casa) y la forma de resolverlo. En programacion pasa igual: cuando un desarrollador dice 'el repositorio de VetCare es un Singleton', su compañero entiende de una que hay una sola instancia y un punto de acceso global, sin necesidad de leer el codigo. El catalogo clasico es el de la Banda de los Cuatro (GoF) y agrupa los patrones en creacionales (como se crean los objetos: Singleton, Factory, Builder), estructurales (como se componen: Adapter, Decorator, Facade) y de comportamiento (como se comunican: Observer, Strategy). Nosotros vamos a usar solo dos hoy, pero bien usados y con criterio, no por coleccionarlos.",
            "El problema que motiva el Singleton ya lo vivimos en la clase pasada, aunque no le pusimos nombre. En VetCare la ventana de registro creaba su propio RepositorioMascotas. Cuando abramos la ventana de citas y esta haga otro new RepositorioMascotas(), la agenda no vera ni una sola de las mascotas registradas, porque son dos ArrayList distintos en dos zonas distintas de memoria. Y no sirve pasar datos por copia: la clinica Huellitas necesita que exista un solo lugar donde vivan los expedientes mientras la aplicacion corre, igual que en la clinica fisica hay un solo archivador y no uno por escritorio. El problema entonces se enuncia asi: necesito garantizar que exista una y solo una instancia de esta clase y que cualquier parte del programa pueda llegar a ella sin andar pasandosela de constructor en constructor. Esa es exactamente la intencion del patron Singleton.",
            "El mecanismo en Java tiene tres piezas y las tres son obligatorias. Primera, un atributo privado y estatico del mismo tipo de la clase (private static RepositorioVetCare instancia): estatico porque debe pertenecer a la clase y no a un objeto, privado para que nadie lo reemplace desde afuera. Segunda, el constructor declarado private: mientras exista un constructor publico, cualquiera puede hacer new y el patron se rompe; al hacerlo privado el compilador se vuelve su aliado y marca en rojo cada intento. Tercera, un metodo publico y estatico getInstancia() que revisa si el atributo es null, lo crea la primera vez y de ahi en adelante devuelve siempre el mismo objeto; a eso se le llama inicializacion perezosa (lazy). Si el programa fuera multihilo, dos hilos podrian entrar al mismo tiempo al if y crear dos instancias; por eso se marca synchronized, o se usa la version temprana (private static final RepositorioVetCare INSTANCIA = new RepositorioVetCare();) que Java garantiza unica. Para verificarlo en pantalla no hay que creer en la fe: se imprime System.identityHashCode(a) y System.identityHashCode(b) desde las dos ventanas y se comprueba que el numero es el mismo.",
            "El segundo patron responde a otro problema distinto: quien decide como se construye un objeto. En VetCare hay tres tipos de consulta con reglas propias: Vacunacion dura 15 minutos y cuesta 35.000, Control dura 30 minutos y cuesta 60.000, Urgencia dura 45 minutos y cuesta 120.000. Si la ventana de agendamiento hace directamente el new de cada subclase, esos numeros y esas decisiones quedan regados por toda la interfaz, y el dia que la clinica suba la tarifa hay que ir a buscarlos en cinco ventanas. Una Factory concentra esa decision en un solo lugar: FabricaConsultas.crear(\"URGENCIA\", \"M-001\") devuelve un objeto de tipo Consulta y la ventana ni se entera de que subclase le entregaron; ademas la fabrica normaliza el texto que llega del JComboBox y lanza IllegalArgumentException si el tipo no existe, con lo cual un dato basura nunca se convierte en objeto. Fijese en el detalle importante: el metodo retorna el tipo base (Consulta), no la subclase; ahi es donde el polimorfismo que vimos en clases anteriores empieza a pagar, porque el dia que Huellitas agregue 'CIRUGIA' solo se toca la fabrica.",
            "Ahora la parte que casi nadie enseña: cuando NO usarlos. El Singleton es, sin maquillaje, una variable global con corbata. Trae tres costos reales: esconde dependencias (una clase que por dentro llama a getInstancia() no declara en su firma que necesita el repositorio), complica las pruebas (en la clase 8 vamos a querer un repositorio limpio en cada caso de prueba y el Singleton nos va a devolver el sucio de la prueba anterior) y concentra estado compartido que en aplicaciones grandes se vuelve impredecible. La alternativa profesional se llama inyeccion por constructor: pasar el repositorio como parametro, tal como hicimos con ControladorRegistro en la clase 6. En VetCare aceptamos el Singleton para el repositorio porque es una aplicacion de escritorio pequeña, con un solo usuario y una unica fuente de datos, y aun asi vamos a dejarle un metodo limpiar() para poder probarlo. La Factory tiene su propio abuso: si solo hay una clase que crear y ninguna regla que aplicar, una fabrica que hace un new pelado no aporta nada, solo una capa mas de ruido. La regla de oro es: primero el problema, despues el patron; nunca al reves.",
            "Error tipico del docente que no domina el tema: enseñar el Singleton como 'la forma correcta de compartir variables entre ventanas' y terminar poniendo el atributo publico y estatico (public static RepositorioVetCare instancia), con lo cual cualquiera puede reasignarlo desde afuera y ya no hay ninguna garantia; o dejar el constructor publico 'porque NetBeans lo pide', que es exactamente lo unico que no se puede hacer. El segundo error clasico es creer que el Singleton persiste datos: los estudiantes cierran la aplicacion, la vuelven a abrir y preguntan donde quedaron las mascotas, y hay que explicar que el Singleton solo garantiza una instancia mientras el programa corre, que la persistencia en archivos es otro tema que veremos mas adelante. El tercero es la patronitis: llenar el proyecto de fabricas que solo devuelven new de una sola clase y de Singletons para cosas que deberian ser objetos comunes, como Mascota o Cita, que por definicion son muchos. Si al preguntar 'que problema resuelve este patron aqui' la respuesta es 'que lo vimos en clase', el patron esta sobrando."
        ],
        "taller": [
            "Convierta RepositorioVetCare en Singleton: atributo private static instancia, constructor private con un System.out.println que avise cuando se crea, y metodo public static synchronized getInstancia(); ejecute el programa y verifique que el mensaje de creacion aparece una sola vez aunque llame getInstancia() tres veces.",
            "Elimine todos los 'new RepositorioVetCare()' que queden en las ventanas y reemplacelos por RepositorioVetCare.getInstancia(); use Ctrl+F en el proyecto para confirmar que no queda ni uno solo fuera del propio metodo getInstancia.",
            "Cree la jerarquia Consulta (abstracta) con ConsultaVacunacion, ConsultaControl y ConsultaUrgencia, cada una con su duracionMinutos() y tarifaBase(), y la clase FabricaConsultas con el metodo estatico crear(String tipo, String idMascota) que normalice el texto y lance IllegalArgumentException si el tipo no existe.",
            "Ejecute el demo y compruebe dos cosas: en la consola, que el mensaje del constructor sale una sola vez y que los dos identityHashCode coinciden; en pantalla, que al registrar M-002 Michi en la ventana Recepcion y oprimir Refrescar en la ventana Consultorio, Michi aparece junto a M-001 Kira, que fue registrada desde el main.",
            "Escriba al final del archivo un comentario de tres lineas justificando por que el repositorio SI es Singleton, por que Mascota NO debe serlo y que problema tendria el Singleton cuando lleguemos a las pruebas; suba el proyecto y el comentario a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el PI pide una sola aplicacion con varias ventanas trabajando sobre los mismos datos; sin un unico repositorio compartido, la agenda de citas nunca vera las mascotas registradas.",
            "La fabrica de consultas es la que va a permitir agregar nuevos servicios de la clinica (guarderia, cirugia) sin tocar el codigo de las ventanas.",
            "El punto unico de acceso a los datos es tambien el punto unico por donde despues pasara la lectura y escritura de los archivos .txt/.csv del PI."
        ],
        "escenario": [
            "VetCare ya tiene la ventana de registro funcionando y esta a punto de nacer la ventana de agendamiento de citas.",
            "Cada ventana esta creando hoy su propio repositorio, asi que lo registrado en una es invisible para la otra.",
            "La clinica Huellitas maneja por ahora tres tipos de consulta: vacunacion (15 min, 35.000), control (30 min, 60.000) y urgencia (45 min, 120.000)."
        ],
        "criterios": [
            "El mensaje del constructor del repositorio se imprime una sola vez en toda la ejecucion, sin importar cuantas veces se pida la instancia.",
            "El constructor del repositorio es privado y no existe ningun new RepositorioVetCare() fuera de getInstancia().",
            "Registrar una mascota en la ventana Recepcion y refrescar la ventana Consultorio muestra esa mascota en ambas, y el identityHashCode del repositorio impreso en las dos ventanas es identico.",
            "FabricaConsultas devuelve el tipo base Consulta para los tres tipos validos y rechaza con excepcion un tipo desconocido como 'peluqueria espacial'."
        ],
        "pistas": [
            "Si el mensaje del constructor aparece dos veces, quien mas esta creando el objeto y en que linea quedo un new olvidado?",
            "Si alguien hace 'RepositorioVetCare.instancia = null;' desde otra clase y el programa se lo permite, que modificador de acceso quedo mal puesto?",
            "Pregunta de criterio: cuantas mascotas hay en la clinica y cuantos archivadores hay? Cual de esos dos conceptos merece ser Singleton?"
        ],
        "solucion_pasos": [
            "Blinde la creacion. En RepositorioVetCare escriba el atributo 'private static RepositorioVetCare instancia;' y cambie el constructor a 'private RepositorioVetCare() { System.out.println(\"[Repositorio] Se creo la UNICA instancia de datos.\"); }'. Apenas guarde, NetBeans le marcara en rojo todos los lugares donde alguien hacia new RepositorioVetCare(): eso no es un problema, es el patron trabajando a su favor, porque le muestra exactamente que codigo hay que corregir. El println no es decoracion: es la evidencia visible de cuantas veces se construyo el objeto.",
            "Abra la unica puerta. Agregue 'public static synchronized RepositorioVetCare getInstancia() { if (instancia == null) { instancia = new RepositorioVetCare(); } return instancia; }'. Es estatico porque hay que poder llamarlo sin tener aun un objeto (RepositorioVetCare.getInstancia()); el if hace la creacion perezosa, es decir que el objeto solo nace la primera vez que alguien lo pide; y synchronized evita que dos hilos entren simultaneamente al if y terminen creando dos instancias. Compruebe con dos llamadas seguidas y un System.out.println(a == b): imprime true y el mensaje del constructor sale una sola vez.",
            "Reemplace en las ventanas. Donde decia 'RepositorioVetCare repo = new RepositorioVetCare();' ahora va 'RepositorioVetCare repo = RepositorioVetCare.getInstancia();'. Para dejar la evidencia, en el metodo refrescar() de cada ventana imprima o pinte System.identityHashCode(RepositorioVetCare.getInstancia()): las dos ventanas deben mostrar el mismo numero. Ese numero es la prueba visible de que ya no hay dos archivadores, sino uno, y es lo que hace que M-002 Michi, registrada en Recepcion, aparezca al refrescar en Consultorio.",
            "Centralice la creacion de consultas. FabricaConsultas queda con constructor privado (es una clase de utilidad, nadie debe instanciarla) y un unico metodo estatico crear(String tipo, String idMascota). Adentro: valida que el idMascota no venga vacio, normaliza el texto con tipo.trim().toUpperCase() para que 'vacunacion', 'Vacunacion' y ' VACUNACION ' sean lo mismo, compara esa clave con los tres tipos validos (un switch sobre String o la cadena if/else del demo) devolviendo new ConsultaVacunacion, new ConsultaControl o new ConsultaUrgencia, y en cualquier otro caso lanza IllegalArgumentException con el mensaje 'Tipo de consulta no soportado: ...'. La ventana declara la variable como Consulta, no como ConsultaUrgencia, y llama consulta.duracionMinutos() y consulta.tarifaBase() sin saber cual subclase le tocó: asi el dia que agreguen CIRUGIA solo se toca la fabrica.",
            "Justifique por escrito, que es la parte que se evalua. El repositorio es Singleton porque representa un recurso unico y compartido (el archivador de la clinica) y porque su estado debe ser el mismo para todas las ventanas: si hubiera dos, la agenda agendaria citas a mascotas que no existen. Mascota no puede serlo porque el dominio tiene muchas mascotas: un Singleton de Mascota significaria que Huellitas atiende un solo animal. Y anote el costo con nombre propio: en la clase 8, cuando escribamos pruebas, el Singleton va a llegar con los datos de la prueba anterior y las pruebas empezaran a depender del orden; por eso le dejamos el metodo limpiar(), que cada prueba llamara antes de empezar."
        ],
        "solucion_rubrica": [
            "Singleton correcto: atributo estatico privado, constructor privado y getInstancia (3)",
            "Ninguna ventana crea el repositorio con new y ambas comparten datos (2)",
            "FabricaConsultas con tres tipos, retorno del tipo base y validacion del tipo desconocido (3)",
            "Justificacion escrita del uso del patron y de su costo (2)"
        ],
        "solucion_errores": [
            "Dejar el constructor publico o declarar el atributo como public static, con lo cual cualquiera puede crear o reemplazar la 'unica' instancia y el patron queda de adorno.",
            "Creer que el Singleton guarda los datos entre ejecuciones y reclamar que 'se borraron las mascotas' al cerrar la aplicacion.",
            "Aplicar Singleton a Mascota, Cita o Dueno, o crear una fabrica que solo hace un new de una sola clase sin ninguna regla ni validacion."
        ],
        "codigo_slide_titulo": "Singleton: un solo archivador para toda la clinica",
        "codigo_slide_lineas": [
            "public class RepositorioVetCare {                  // el archivador de Huellitas",
            "    private static RepositorioVetCare instancia;   // 1. unica referencia, privada y estatica",
            "    private final List<Mascota> mascotas = new ArrayList<Mascota>();",
            "",
            "    private RepositorioVetCare() { }               // 2. privado: nadie puede hacer new",
            "",
            "    public static synchronized RepositorioVetCare getInstancia() {",
            "        if (instancia == null) {                   // 3. se crea la primera vez que la piden",
            "            instancia = new RepositorioVetCare();",
            "        }",
            "        return instancia;                          // 4. de ahi en adelante, siempre la misma",
            "    }",
            "}",
            "// En cada ventana: RepositorioVetCare repo = RepositorioVetCare.getInstancia();  // nunca new"
        ],
        "codigo_slide_caption": "El constructor privado no es un adorno: es lo unico que le garantiza al compilador que existira una sola instancia.",
        "quiz": [
            {
                "tipo": "om",
                "q": "Que es un patron de diseno?",
                "opciones": [
                    "A) Una libreria de Java que se importa con un import",
                    "B) Una solucion probada y con nombre a un problema de diseno que se repite",
                    "C) Un diagrama UML obligatorio antes de programar",
                    "D) Un framework para construir interfaces graficas"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual elemento es indispensable para que RepositorioVetCare sea realmente un Singleton?",
                "opciones": [
                    "A) Que el atributo instancia sea public static para poder alcanzarlo desde cualquier ventana",
                    "B) Que el constructor sea privado",
                    "C) Que getInstancia sea un metodo de instancia y no estatico",
                    "D) Que la clase implemente una interfaz"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Si el repositorio de VetCare es Singleton, los datos quedan guardados aunque se cierre la aplicacion.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Cual es el riesgo principal de abusar del Singleton?",
                "opciones": [
                    "A) Que el objeto ocupa memoria durante toda la ejecucion del programa",
                    "B) Que se convierte en estado global oculto: esconde dependencias y ensucia las pruebas",
                    "C) Que obliga a escribir un metodo getInstancia en todas las clases del proyecto",
                    "D) Que impide usar herencia en el resto del proyecto"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Que problema resuelve FabricaConsultas en VetCare?",
                "opciones": [
                    "A) Garantizar que exista una sola instancia de la clase Consulta",
                    "B) Centralizar en un solo lugar la decision de que subclase de Consulta crear y con que duracion y tarifa",
                    "C) Ordenar la lista de citas por fecha antes de mostrarla",
                    "D) Convertir a numero el texto que escribe la recepcionista en los JTextField"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Una fabrica que siempre devuelve el mismo tipo de objeto y no aplica ninguna regla ni validacion agrega valor real al diseno.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Explique por que el repositorio de VetCare SI puede ser Singleton pero la clase Mascota NO debe serlo.",
                "clave": "El repositorio representa un recurso unico y compartido (el archivador de la clinica) cuyo estado debe ser el mismo para todas las ventanas; Mascota representa una entidad de la que existen muchas instancias distintas, hacerla Singleton significaria que la clinica atiende un solo animal."
            },
            {
                "tipo": "abierta",
                "q": "Como demuestra en pantalla, sin creer en la fe, que dos ventanas estan usando el mismo repositorio?",
                "clave": "Imprimiendo System.identityHashCode de la referencia en cada ventana (o comparando con ==) y verificando que el numero es identico, y registrando en una ventana un dato que aparece al refrescar la otra; ademas el mensaje del constructor privado se imprime una sola vez en toda la ejecucion."
            }
        ],
        "codigo_fuente": "package vetcare.patrones;\n\nimport java.awt.BorderLayout;\nimport java.awt.GridLayout;\nimport java.awt.event.ActionEvent;\nimport java.awt.event.ActionListener;\nimport java.util.ArrayList;\nimport java.util.List;\nimport javax.swing.JButton;\nimport javax.swing.JFrame;\nimport javax.swing.JLabel;\nimport javax.swing.JOptionPane;\nimport javax.swing.JPanel;\nimport javax.swing.JScrollPane;\nimport javax.swing.JTextArea;\nimport javax.swing.JTextField;\nimport javax.swing.SwingUtilities;\n\n/** Clase 7 de VetCare: un solo repositorio (Singleton) y una fabrica de consultas (Factory). */\npublic class VetCarePatronesDemo {\n\n    public static void main(String[] args) {\n        RepositorioVetCare a = RepositorioVetCare.getInstancia();\n        RepositorioVetCare b = RepositorioVetCare.getInstancia();\n        System.out.println(\"Son el mismo objeto? \" + (a == b));\n        System.out.println(\"id a = \" + System.identityHashCode(a)\n                + \"   id b = \" + System.identityHashCode(b));\n\n        a.registrar(new Mascota(\"M-001\", \"Kira\", \"perro\"));\n        System.out.println(\"Mascotas vistas desde b: \" + b.listar());\n\n        Consulta vacuna = FabricaConsultas.crear(\"vacunacion\", \"M-001\");\n        Consulta urgencia = FabricaConsultas.crear(\"URGENCIA\", \"M-001\");\n        System.out.println(vacuna.describir());\n        System.out.println(urgencia.describir());\n        try {\n            FabricaConsultas.crear(\"peluqueria espacial\", \"M-001\");\n        } catch (IllegalArgumentException e) {\n            System.out.println(\"La fabrica protege el dominio: \" + e.getMessage());\n        }\n\n        SwingUtilities.invokeLater(new Runnable() {\n            @Override\n            public void run() {\n                new VentanaSucursal(\"Recepcion\").setVisible(true);\n                new VentanaSucursal(\"Consultorio\").setVisible(true);\n            }\n        });\n    }\n}\n\n/** Expediente basico de una mascota de la clinica Huellitas. */\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private final String especie;\n\n    public Mascota(String id, String nombre, String especie) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n    }\n\n    public String getId() { return id; }\n\n    public String getNombre() { return nombre; }\n\n    public String getEspecie() { return especie; }\n\n    @Override\n    public String toString() {\n        return id + \" - \" + nombre + \" (\" + especie + \")\";\n    }\n}\n\n/** Singleton: unico punto de acceso a los datos en memoria de VetCare. */\nclass RepositorioVetCare {\n\n    private static RepositorioVetCare instancia;\n\n    private final List<Mascota> mascotas = new ArrayList<Mascota>();\n\n    private RepositorioVetCare() {\n        System.out.println(\"[Repositorio] Se creo la UNICA instancia de datos.\");\n    }\n\n    public static synchronized RepositorioVetCare getInstancia() {\n        if (instancia == null) {\n            instancia = new RepositorioVetCare();\n        }\n        return instancia;\n    }\n\n    public void registrar(Mascota mascota) {\n        if (mascota == null || mascota.getId() == null || mascota.getId().trim().isEmpty()) {\n            throw new IllegalArgumentException(\"El ID de la mascota es obligatorio.\");\n        }\n        if (buscarPorId(mascota.getId()) != null) {\n            throw new IllegalArgumentException(\"El ID \" + mascota.getId() + \" ya esta registrado.\");\n        }\n        mascotas.add(mascota);\n    }\n\n    public Mascota buscarPorId(String id) {\n        for (Mascota m : mascotas) {\n            if (m.getId().equalsIgnoreCase(id)) {\n                return m;\n            }\n        }\n        return null;\n    }\n\n    public List<Mascota> listar() { return new ArrayList<Mascota>(mascotas); }\n\n    public int total() { return mascotas.size(); }\n\n    /** Necesario para poder probar en la clase 8: deja el archivador vacio. */\n    public void limpiar() { mascotas.clear(); }\n}\n\n/** Tipo base de los servicios que presta la clinica. */\nabstract class Consulta {\n\n    protected final String idMascota;\n\n    protected Consulta(String idMascota) {\n        this.idMascota = idMascota;\n    }\n\n    public abstract int duracionMinutos();\n\n    public abstract double tarifaBase();\n\n    public String describir() {\n        return getClass().getSimpleName() + \" para \" + idMascota\n                + \" | \" + duracionMinutos() + \" min | $\" + tarifaBase();\n    }\n}\n\nclass ConsultaVacunacion extends Consulta {\n\n    public ConsultaVacunacion(String idMascota) { super(idMascota); }\n\n    @Override\n    public int duracionMinutos() { return 15; }\n\n    @Override\n    public double tarifaBase() { return 35000; }\n}\n\nclass ConsultaControl extends Consulta {\n\n    public ConsultaControl(String idMascota) { super(idMascota); }\n\n    @Override\n    public int duracionMinutos() { return 30; }\n\n    @Override\n    public double tarifaBase() { return 60000; }\n}\n\nclass ConsultaUrgencia extends Consulta {\n\n    public ConsultaUrgencia(String idMascota) { super(idMascota); }\n\n    @Override\n    public int duracionMinutos() { return 45; }\n\n    @Override\n    public double tarifaBase() { return 120000; }\n}\n\n/** Factory: la ventana pide un tipo y no se entera de que subclase se construyo. */\nclass FabricaConsultas {\n\n    private FabricaConsultas() { }\n\n    public static Consulta crear(String tipo, String idMascota) {\n        if (idMascota == null || idMascota.trim().isEmpty()) {\n            throw new IllegalArgumentException(\"La consulta necesita el ID de la mascota.\");\n        }\n        String clave = (tipo == null) ? \"\" : tipo.trim().toUpperCase();\n        if (clave.equals(\"VACUNACION\")) {\n            return new ConsultaVacunacion(idMascota.trim());\n        } else if (clave.equals(\"CONTROL\")) {\n            return new ConsultaControl(idMascota.trim());\n        } else if (clave.equals(\"URGENCIA\")) {\n            return new ConsultaUrgencia(idMascota.trim());\n        } else {\n            throw new IllegalArgumentException(\"Tipo de consulta no soportado: \" + tipo);\n        }\n    }\n}\n\n/** Dos instancias de esta ventana comparten el mismo repositorio. */\nclass VentanaSucursal extends JFrame {\n\n    private final JTextField txtId = new JTextField();\n    private final JTextField txtNombre = new JTextField();\n    private final JTextField txtEspecie = new JTextField();\n    private final JTextArea area = new JTextArea(8, 30);\n    private final JButton btnRegistrar = new JButton(\"Registrar\");\n    private final JButton btnRefrescar = new JButton(\"Refrescar\");\n\n    public VentanaSucursal(String punto) {\n        super(\"VetCare - \" + punto);\n        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);\n        setLayout(new BorderLayout());\n\n        JPanel form = new JPanel(new GridLayout(4, 2, 6, 6));\n        form.add(new JLabel(\"ID (ej. M-002):\"));\n        form.add(txtId);\n        form.add(new JLabel(\"Nombre:\"));\n        form.add(txtNombre);\n        form.add(new JLabel(\"Especie:\"));\n        form.add(txtEspecie);\n        form.add(btnRegistrar);\n        form.add(btnRefrescar);\n\n        area.setEditable(false);\n        add(form, BorderLayout.NORTH);\n        add(new JScrollPane(area), BorderLayout.CENTER);\n\n        btnRegistrar.addActionListener(new ActionListener() {\n            @Override\n            public void actionPerformed(ActionEvent e) {\n                registrar();\n            }\n        });\n\n        btnRefrescar.addActionListener(new ActionListener() {\n            @Override\n            public void actionPerformed(ActionEvent e) {\n                refrescar();\n            }\n        });\n\n        pack();\n        setLocationByPlatform(true);\n        refrescar();\n    }\n\n    private void registrar() {\n        try {\n            RepositorioVetCare.getInstancia().registrar(new Mascota(\n                    txtId.getText().trim(), txtNombre.getText().trim(), txtEspecie.getText().trim()));\n            txtId.setText(\"\");\n            txtNombre.setText(\"\");\n            txtEspecie.setText(\"\");\n            refrescar();\n        } catch (IllegalArgumentException ex) {\n            JOptionPane.showMessageDialog(this, ex.getMessage());\n        }\n    }\n\n    private void refrescar() {\n        StringBuilder sb = new StringBuilder();\n        sb.append(\"Repositorio #\")\n                .append(System.identityHashCode(RepositorioVetCare.getInstancia()))\n                .append(System.lineSeparator());\n        for (Mascota m : RepositorioVetCare.getInstancia().listar()) {\n            sb.append(m.toString()).append(System.lineSeparator());\n        }\n        sb.append(\"Total: \").append(RepositorioVetCare.getInstancia().total());\n        area.setText(sb.toString());\n    }\n}\n",
        "codigo_archivo": "VetCarePatronesDemo.java"
    },
    {
        "n": 8,
        "slug": "Documentacion y QA Javadoc y pruebas",
        "titulo": "Documentacion y QA · Javadoc y pruebas",
        "subtitulo": "Codigo que se explica solo y que se puede comprobar",
        "herramienta": "Apache NetBeans",
        "hito_pi": "Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.",
        "entregable": "Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.",
        "demo": "El docente escribe un bloque Javadoc, genera la documentacion HTML desde NetBeans y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.",
        "teoria": [
            "Documentar no es llenar el codigo de comentarios. Un comentario como '// suma uno al contador' encima de la linea contador++ no le sirve a nadie: repite lo que ya dice el codigo y ademas envejece mal, porque cuando alguien cambia la linea nadie se acuerda de cambiar el comentario, y entonces el comentario miente. Javadoc resuelve otro problema, que es el del contrato: le dice a quien va a usar su clase que hace el metodo, que espera recibir, que devuelve y en que casos revienta, sin que esa persona tenga que abrir el codigo fuente. En VetCare esa diferencia es concreta: el estudiante que escriba la ventana de citas necesita saber que agendar() lanza excepcion si la mascota esta inactiva, y no tiene por que leer las veinte lineas del metodo para descubrirlo. La documentacion tecnica no describe la implementacion, describe la promesa.",
            "Un bloque Javadoc se escribe con /** y se cierra con */, y va inmediatamente encima de la clase, del constructor, del atributo o del metodo que documenta (si lo pone debajo, no sirve). La primera frase debe ser un resumen corto que termine en punto, porque esa frase es la que aparece en las tablas resumen del HTML generado. Despues vienen las etiquetas: @param una por cada parametro con su nombre exacto, @return si el metodo devuelve algo, @throws por cada excepcion documentada, y a nivel de clase @author y @version. Se pueden usar marcas como {@code M-001} para que un texto se vea con tipografia de codigo y @see para remitir a otra clase. Lo que se genera es un sitio web: en NetBeans es clic derecho sobre el proyecto, Generate Javadoc, y el IDE ejecuta la herramienta javadoc del JDK, crea la carpeta dist/javadoc y abre el navegador con la misma cara que tiene la documentacion oficial de Java. Un beneficio inmediato que se ve sin generar nada: apenas usted escribe el Javadoc, NetBeans se lo muestra en el globo de ayuda cuando alguien invoca el metodo con Ctrl+Espacio.",
            "Ahora bien, la mejor documentacion es la que no hay que escribir, y eso se logra con nombres que se explican solos. Compare 'public boolean verificar(String x)' con 'public boolean estaActiva(String idMascota)': la segunda no necesita comentario. En Java hay convenciones que el mundo entero respeta y que sus estudiantes deben respetar desde ya: clases en PascalCase (AgendaService), metodos y variables en camelCase (agendarCita, idMascota), constantes en MAYUSCULAS con guion bajo (TARIFA_BASE), metodos que devuelven boolean nombrados como una pregunta (estaActiva, tieneCitasPendientes), y metodos que hacen algo nombrados con verbo (agendar, registrar, buscarPorId). Nada de proc1, dato2, aux ni flag. En VetCare hicimos precisamente ese refactor: lo que empezo llamandose 'validar' pasa a llamarse 'agendar', y la variable 'b' pasa a llamarse 'mascotaActiva'; el codigo quedo igual de largo pero dejo de necesitar traductor.",
            "La segunda mitad de la clase es control de calidad. Un caso de prueba tiene cuatro partes y conviene escribirlas en el tablero antes de tocar el teclado: un nombre que se lea como una frase, unos datos o estado de partida, una accion concreta y un resultado esperado. En ingles a esa estructura se le dice AAA: Arrange (preparar), Act (ejecutar), Assert (comprobar). Y no basta con probar que todo salga bien: por cada funcionalidad se necesitan pruebas positivas (mascota activa agenda y la cita queda registrada), negativas (mascota inactiva no agenda y lanza excepcion) y de borde (fecha vacia, ID inexistente, horario ya ocupado). Para la regla de hoy la tabla queda asi: caso 1, mascota M-001 Kira activa, agendar el 30 de septiembre a las 10:00, se espera una cita creada y total de citas igual a 1; caso 2, mascota M-009 Rocky inactiva, misma accion, se espera IllegalStateException y total de citas igual a 0. Fijese que el resultado esperado se define ANTES de correr el programa; si usted primero ejecuta y despues decide que esperaba, eso no es una prueba, es una conformidad.",
            "JUnit es la herramienta que convierte esos casos en codigo que se ejecuta solo. En NetBeans se agrega con clic derecho sobre el proyecto, en Test Libraries, y las clases de prueba viven en Test Packages, separadas del codigo de produccion; la convencion es AgendaServiceTest para probar AgendaService. Cada caso es un metodo publico anotado con @Test cuyo nombre describe el escenario (agendar_mascotaInactiva_lanzaIllegalStateException), con un metodo anotado @Before o @BeforeEach que arma el estado limpio antes de cada caso, para que ninguna prueba dependa de la anterior. Las comprobaciones se hacen con assertEquals(esperado, obtenido), assertTrue(condicion) y assertThrows(IllegalStateException.class, () -> agenda.agendar(...)), que es la forma moderna de verificar que algo debe fallar. La diferencia con la prueba manual es importante y hay que decirla completa: la prueba unitaria es automatica, repetible, rapida y prueba logica aislada, y por eso se corre cada vez que se toca el codigo; la prueba manual la hace un humano usando la interfaz, sirve para lo que no se puede automatizar facil (que el JOptionPane se lea bien, que la ventana no se congele, que el flujo tenga sentido para la recepcionista) y no reemplaza a la otra. Y aqui se cobra la clase 6: como la regla de agendar vive en AgendaService y no dentro de un boton, se puede probar sin abrir ni una sola ventana.",
            "Error tipico del docente que no domina el tema: confundir Javadoc con comentarios normales y escribir // encima de los metodos creyendo que eso genera documentacion, o abrir el bloque con /* en vez de /** y despues no entender por que el HTML sale vacio. Muy de la mano va el vicio de documentar lo obvio (un @return 'retorna el nombre' sobre getNombre()) y dejar sin una sola linea el metodo agendar, que es justo donde vive la regla de negocio que nadie adivina. En pruebas los errores son igual de tipicos: llamar 'prueba' a un main con System.out.println donde el docente mira la consola y dice 'si, funciono' (eso no es automatico ni repetible, y nadie se entera cuando se rompe tres semanas despues); escribir pruebas que dependen del orden porque comparten un Singleton sucio de la prueba anterior; e intentar probar la ventana en vez del servicio, que es el sintoma clasico de haber metido la logica dentro del boton. Y el peor de todos, el que hay que desarmar en voz alta: creer que 'si compila, funciona'. Compilar solo significa que la sintaxis esta bien; que la mascota inactiva no pueda agendar cita es algo que solo se sabe si alguien lo comprueba."
        ],
        "taller": [
            "Documente con Javadoc las clases Mascota y Cita y el servicio AgendaService: bloque de clase con resumen y @author, y en cada metodo publico @param por parametro, @return si aplica y @throws por cada excepcion; el metodo agendar debe dejar escrita la regla 'una mascota inactiva no puede agendar'.",
            "Renombre al menos tres identificadores pobres del proyecto (por ejemplo validar por agendar, b por mascotaActiva, dato1 por idMascota) usando Refactor > Rename de NetBeans para que el cambio se propague sin romper nada.",
            "Genere la documentacion con clic derecho sobre el proyecto y Generate Javadoc, abra el HTML y verifique que en la ficha de AgendaService se lee la regla de negocio y las tres excepciones documentadas; guarde una captura.",
            "Cree en Test Packages la clase AgendaServiceTest con un metodo de preparacion que registre M-001 Kira activa, M-002 Michi activa y M-009 Rocky inactiva, y escriba cuatro casos: mascota activa agenda, mascota inactiva lanza IllegalStateException, ID inexistente lanza NoSuchElementException y horario ocupado no duplica la cita.",
            "Rompa a proposito la regla (comente la validacion de mascota inactiva), corra las pruebas y capture la barra roja; restaure la validacion, corra otra vez y capture la barra verde; escriba ademas dos pruebas manuales que NO se pueden automatizar y suba todo a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el PI se entrega y se sustenta, y un evaluador no puede confiar en lo que no esta documentado ni comprobado; hoy VetCare pasa de 'a mi me funciono' a 'aqui esta la evidencia'.",
            "Las reglas del dominio (mascota inactiva, ID inexistente, horario ocupado) son las que van a fallar en la sustentacion si nadie las prueba antes.",
            "La documentacion generada hoy es la que permite que otro compañero use AgendaService en la ventana de citas sin leer el codigo por dentro."
        ],
        "escenario": [
            "VetCare ya tiene el dominio (Mascota, Cita), el servicio de agendamiento y la interfaz conectada por eventos, con el repositorio unico de la clase anterior.",
            "Las clases estan sin documentar y hay tres metodos con nombres heredados de los primeros borradores: validar, proceso y dato1.",
            "Expedientes de partida: M-001 Kira activa, M-002 Michi activa y M-009 Rocky inactiva (dada de baja del servicio)."
        ],
        "criterios": [
            "El Javadoc de agendar incluye @param de los dos parametros, @return y al menos dos @throws, y la regla de la mascota inactiva queda escrita en palabras.",
            "La documentacion HTML se genera sin errores y en la ficha de AgendaService se lee el resumen de cada metodo publico.",
            "Existen cuatro casos de prueba con nombres que describen escenario y resultado esperado, y cada uno funciona sin depender de los otros.",
            "Al comentar la validacion de mascota inactiva la prueba correspondiente falla, y al restaurarla vuelve a pasar (evidencia de rojo y de verde)."
        ],
        "pistas": [
            "Si el HTML generado sale vacio o le falta un metodo: con que tres caracteres exactos abre su bloque de comentario y donde esta ubicado respecto al metodo?",
            "Si una prueba pasa cuando se corre sola pero falla cuando se corren todas, que estado esta sobreviviendo de un caso al siguiente y quien deberia limpiarlo?",
            "Si para comprobar la regla usted necesita abrir la ventana y oprimir un boton, donde quedo escrita esa regla y donde deberia estar?"
        ],
        "solucion_pasos": [
            "Documente el contrato, no la implementacion. Sobre el metodo agendar, y pegado a su firma, escriba el bloque: /** Agenda una cita para una mascota registrada y activa. Una mascota inactiva no puede agendar: en ese caso no se crea ninguna cita. @param idMascota identificador del expediente, por ejemplo {@code M-001} @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm @return la cita creada @throws IllegalArgumentException si la fecha y hora vienen vacias @throws NoSuchElementException si no existe expediente con ese ID @throws IllegalStateException si la mascota esta inactiva o el horario ya esta ocupado */. Note que en ninguna linea se dice como esta programado por dentro (ni el Map, ni el for): se dice que promete y cuando incumple, que es justo lo que necesita quien va a escribir la ventana de citas.",
            "Genere y verifique. Clic derecho sobre el proyecto, Generate Javadoc; NetBeans ejecuta la herramienta javadoc del JDK, crea la carpeta dist/javadoc y abre index.html en el navegador. Entre a la ficha de AgendaService y confirme que aparece el resumen de cada metodo publico y que en agendar se leen las tres excepciones. Si un metodo no aparece, casi siempre es por una de dos razones: el bloque se abrio con /* en vez de /**, o quedo debajo de la firma en vez de encima. Aproveche para mostrar que ahora, al escribir agenda.agendar( en otra clase, el globo de ayuda de NetBeans muestra su propio texto: la documentacion empezo a trabajar de inmediato, sin esperar al HTML.",
            "Arme el estado limpio antes de cada caso. En AgendaServiceTest declare 'private AgendaService agenda;' como atributo y en el metodo anotado con @Before (JUnit 4) o @BeforeEach (JUnit 5) escriba 'agenda = new AgendaService();' y registre las tres mascotas del escenario: new Mascota(\"M-001\", \"Kira\", true), new Mascota(\"M-002\", \"Michi\", true) y new Mascota(\"M-009\", \"Rocky\", false). Ese metodo se ejecuta antes de CADA @Test, no una sola vez, y es lo que garantiza que las pruebas no se contaminen entre si; si el repositorio fuera el Singleton de la clase 7, aqui iria ademas RepositorioVetCare.getInstancia().limpiar().",
            "Escriba el caso estrella con assertThrows. El metodo se llama agendar_mascotaInactiva_lanzaIllegalStateException y su cuerpo tiene dos lineas: assertThrows(IllegalStateException.class, () -> agenda.agendar(\"M-009\", \"2026-09-30 10:00\")); y luego assertEquals(0, agenda.totalCitas());. La primera comprueba que revento como debia y con la excepcion correcta (si el servicio lanzara NoSuchElementException, la prueba fallaria, que es lo que uno quiere). La segunda comprueba algo que casi todos olvidan: que ademas de reventar no dejo basura, es decir que la cita no quedo a medio agendar en la lista. Complete la bateria con el caso positivo (assertNotNull sobre la cita de M-001 y total igual a 1), el de ID inexistente M-777 con NoSuchElementException y el de horario ocupado, donde la segunda cita a la misma hora debe rebotar y el total quedar en 1.",
            "Muestre el rojo y despues el verde, que es la leccion completa. Comente la linea 'if (!mascota.estaActiva()) { throw new IllegalStateException(...); }' y corra las pruebas con Alt+F6: la barra se pone roja y JUnit dice exactamente cual caso fallo y por que (se esperaba una excepcion que nunca llego). Restaure la linea, vuelva a correr y muestre la barra verde con los cuatro casos. Diga en voz alta la conclusion: la prueba no sirve para confirmar que usted tiene razon, sirve para avisarle el dia que deje de tenerla, por ejemplo cuando un compañero toque el servicio en tres semanas. Cierre documentando en el informe las dos pruebas manuales que hoy no se automatizan: que el mensaje del JOptionPane se lea claro para la recepcionista y que la ventana no se congele al listar muchas citas."
        ],
        "solucion_rubrica": [
            "Javadoc completo en Mascota, Cita y AgendaService con @param, @return y @throws (3)",
            "Documentacion HTML generada y navegable con la regla de negocio visible (2)",
            "Cuatro casos de prueba independientes y con nombres que se leen solos (3)",
            "Evidencia de la prueba en rojo y en verde mas dos pruebas manuales documentadas (2)"
        ],
        "solucion_errores": [
            "Abrir el bloque con /* en lugar de /**, o ponerlo debajo de la firma del metodo: el codigo compila igual pero el HTML sale sin esa documentacion.",
            "Documentar getters obvios y dejar sin una sola linea el metodo agendar, que es donde vive la regla que nadie puede adivinar.",
            "Llamar prueba a un main con System.out.println revisado a ojo, o escribir pruebas que dependen del orden porque comparten estado sucio del caso anterior."
        ],
        "codigo_slide_titulo": "El contrato documentado y su prueba",
        "codigo_slide_lineas": [
            "/**",
            " * Agenda una cita para una mascota registrada y activa.",
            " * @param idMascota identificador del expediente, por ejemplo {@code M-001}",
            " * @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm",
            " * @return la cita creada",
            " * @throws IllegalStateException si la mascota esta inactiva",
            " */",
            "public Cita agendar(String idMascota, String fechaHora) { /* reglas en AgendaService */ }",
            "",
            "@Test   // un caso = un metodo cuyo nombre se lee como una frase",
            "public void agendar_mascotaInactiva_lanzaIllegalStateException() {",
            "    agenda.registrarMascota(new Mascota(\"M-009\", \"Rocky\", false));   // Arrange",
            "    assertThrows(IllegalStateException.class,                         // Act + Assert",
            "            () -> agenda.agendar(\"M-009\", \"2026-09-30 10:00\"));",
            "    assertEquals(0, agenda.totalCitas());   // y ademas no dejo la cita a medias",
            "}"
        ],
        "codigo_slide_caption": "Lo que el Javadoc promete es exactamente lo que la prueba obliga a cumplir.",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cual de estos bloques genera documentacion HTML cuando se ejecuta la herramienta javadoc?",
                "opciones": [
                    "A) // Agenda una cita para una mascota activa",
                    "B) /* Agenda una cita para una mascota activa */",
                    "C) /** Agenda una cita para una mascota activa. */",
                    "D) /*** Agenda una cita para una mascota activa ***/"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual etiqueta se usa para documentar la excepcion que puede lanzar el metodo agendar?",
                "opciones": [
                    "A) @param",
                    "B) @return",
                    "C) @see",
                    "D) @throws"
                ],
                "clave": "D"
            },
            {
                "tipo": "vf",
                "q": "Javadoc genera un sitio HTML de documentacion a partir de los comentarios escritos en el codigo fuente.",
                "clave": "V"
            },
            {
                "tipo": "om",
                "q": "Que significa la estructura AAA de un caso de prueba?",
                "opciones": [
                    "A) Analizar, Aprobar, Archivar",
                    "B) Arrange (preparar), Act (ejecutar), Assert (comprobar)",
                    "C) Agregar, Actualizar, Anular",
                    "D) Abrir, Asignar, Almacenar"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Un main con System.out.println que el docente revisa a ojo equivale a una prueba unitaria automatizada.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Que comprobacion usaria para verificar que agendar con la mascota inactiva M-009 lanza excepcion?",
                "opciones": [
                    "A) assertEquals",
                    "B) assertTrue",
                    "C) assertThrows",
                    "D) assertNotNull"
                ],
                "clave": "C"
            },
            {
                "tipo": "abierta",
                "q": "Explique la diferencia entre prueba unitaria y prueba manual, y mencione un caso de VetCare donde la manual sea la unica opcion razonable.",
                "clave": "La unitaria es codigo automatico, aislado, rapido y repetible que prueba logica (por ejemplo la regla de agendamiento en AgendaService); la manual la hace una persona usando la interfaz y no es repetible ni automatica. Es la unica opcion para cosas como verificar que el mensaje del JOptionPane se entienda, que la ventana no se congele o que el flujo tenga sentido para la recepcionista."
            },
            {
                "tipo": "abierta",
                "q": "Escriba completo el caso de prueba de la regla 'mascota inactiva no agenda': nombre, datos de partida, accion y resultado esperado.",
                "clave": "Nombre: agendar_mascotaInactiva_lanzaIllegalStateException. Datos: expediente M-009 Rocky registrado como inactivo y agenda vacia. Accion: llamar agenda.agendar(\"M-009\", \"2026-09-30 10:00\"). Resultado esperado: se lanza IllegalStateException con mensaje sobre mascota inactiva y el total de citas queda en 0 (no se crea la cita)."
            }
        ],
        "codigo_fuente": "package vetcare.qa;\n\nimport java.util.ArrayList;\nimport java.util.LinkedHashMap;\nimport java.util.List;\nimport java.util.Map;\nimport java.util.NoSuchElementException;\n\n/**\n * Clase 8 de VetCare: dominio documentado con Javadoc y su bateria de casos de prueba.\n * Este archivo se ejecuta sin librerias externas: el metodo main corre los mismos casos\n * que despues se escriben con JUnit (ver el bloque comentado al final del archivo).\n *\n * @author Equipo VetCare\n * @version 1.0\n */\npublic class VetCareQADemo {\n\n    private static int aprobadas = 0;\n    private static int fallidas = 0;\n\n    public static void main(String[] args) {\n        AgendaService agenda = nuevaAgenda();\n        Cita cita = agenda.agendar(\"M-001\", \"2026-09-30 10:00\");\n        verificar(\"agendar_mascotaActiva_creaLaCita\", cita != null && agenda.totalCitas() == 1);\n\n        agenda = nuevaAgenda();\n        try {\n            agenda.agendar(\"M-009\", \"2026-09-30 10:00\");\n            verificar(\"agendar_mascotaInactiva_lanzaIllegalStateException\", false);\n        } catch (IllegalStateException e) {\n            verificar(\"agendar_mascotaInactiva_lanzaIllegalStateException\", agenda.totalCitas() == 0);\n        }\n\n        agenda = nuevaAgenda();\n        try {\n            agenda.agendar(\"M-777\", \"2026-09-30 10:00\");\n            verificar(\"agendar_idInexistente_lanzaNoSuchElementException\", false);\n        } catch (NoSuchElementException e) {\n            verificar(\"agendar_idInexistente_lanzaNoSuchElementException\", agenda.totalCitas() == 0);\n        }\n\n        agenda = nuevaAgenda();\n        agenda.agendar(\"M-001\", \"2026-09-30 10:00\");\n        try {\n            agenda.agendar(\"M-002\", \"2026-09-30 10:00\");\n            verificar(\"agendar_horarioOcupado_noDuplicaLaCita\", false);\n        } catch (IllegalStateException e) {\n            verificar(\"agendar_horarioOcupado_noDuplicaLaCita\", agenda.totalCitas() == 1);\n        }\n\n        agenda = nuevaAgenda();\n        try {\n            agenda.agendar(\"M-001\", \"   \");\n            verificar(\"agendar_fechaVacia_lanzaIllegalArgumentException\", false);\n        } catch (IllegalArgumentException e) {\n            verificar(\"agendar_fechaVacia_lanzaIllegalArgumentException\", agenda.totalCitas() == 0);\n        }\n\n        System.out.println(\"---------------------------------------------\");\n        System.out.println(\"Aprobadas: \" + aprobadas + \"   Fallidas: \" + fallidas);\n    }\n\n    /**\n     * Prepara el mismo estado inicial para cada caso: equivale al metodo anotado\n     * con {@code @Before} en JUnit.\n     *\n     * @return una agenda con Kira y Michi activas y Rocky inactivo\n     */\n    private static AgendaService nuevaAgenda() {\n        AgendaService agenda = new AgendaService();\n        agenda.registrarMascota(new Mascota(\"M-001\", \"Kira\", true));\n        agenda.registrarMascota(new Mascota(\"M-002\", \"Michi\", true));\n        agenda.registrarMascota(new Mascota(\"M-009\", \"Rocky\", false));\n        return agenda;\n    }\n\n    private static void verificar(String nombreDelCaso, boolean paso) {\n        if (paso) {\n            aprobadas++;\n            System.out.println(\"[OK]    \" + nombreDelCaso);\n        } else {\n            fallidas++;\n            System.out.println(\"[FALLA] \" + nombreDelCaso);\n        }\n    }\n}\n\n/**\n * Expediente de una mascota de la clinica Huellitas.\n * Una mascota inactiva es la que fue dada de baja del servicio y no puede agendar citas.\n *\n * @author Equipo VetCare\n */\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private boolean activa;\n\n    /**\n     * Crea el expediente de una mascota.\n     *\n     * @param id identificador unico del expediente, por ejemplo M-001\n     * @param nombre nombre con el que el dueno reconoce a la mascota\n     * @param activa true si la mascota esta habilitada para agendar citas\n     */\n    public Mascota(String id, String nombre, boolean activa) {\n        this.id = id;\n        this.nombre = nombre;\n        this.activa = activa;\n    }\n\n    public String getId() { return id; }\n\n    public String getNombre() { return nombre; }\n\n    /**\n     * Indica si la mascota puede recibir servicios de la clinica.\n     *\n     * @return true si el expediente esta activo\n     */\n    public boolean estaActiva() { return activa; }\n\n    /** Da de baja el expediente: la mascota deja de poder agendar citas. */\n    public void inactivar() { this.activa = false; }\n}\n\n/**\n * Cita agendada para una mascota en una fecha y hora determinada.\n */\nclass Cita {\n\n    private final String idMascota;\n    private final String fechaHora;\n\n    /**\n     * Crea una cita ya validada por el servicio de agenda.\n     *\n     * @param idMascota expediente al que pertenece la cita\n     * @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm\n     */\n    public Cita(String idMascota, String fechaHora) {\n        this.idMascota = idMascota;\n        this.fechaHora = fechaHora;\n    }\n\n    public String getIdMascota() { return idMascota; }\n\n    public String getFechaHora() { return fechaHora; }\n\n    @Override\n    public String toString() {\n        return \"Cita[\" + idMascota + \" -> \" + fechaHora + \"]\";\n    }\n}\n\n/**\n * Reglas de agendamiento de VetCare.\n * No conoce ventanas ni botones, y por eso se puede probar de forma automatica.\n *\n * @author Equipo VetCare\n */\nclass AgendaService {\n\n    private final Map<String, Mascota> expedientes = new LinkedHashMap<String, Mascota>();\n    private final List<Cita> citas = new ArrayList<Cita>();\n\n    /**\n     * Registra o actualiza el expediente de una mascota.\n     *\n     * @param mascota expediente a guardar; no puede ser null\n     * @throws IllegalArgumentException si el expediente viene en null\n     */\n    public void registrarMascota(Mascota mascota) {\n        if (mascota == null) {\n            throw new IllegalArgumentException(\"El expediente no puede ser null.\");\n        }\n        expedientes.put(mascota.getId(), mascota);\n    }\n\n    /**\n     * Agenda una cita para una mascota registrada y activa.\n     * Una mascota inactiva no puede agendar: en ese caso no se crea ninguna cita.\n     *\n     * @param idMascota identificador del expediente, por ejemplo M-001\n     * @param fechaHora fecha y hora en formato yyyy-MM-dd HH:mm\n     * @return la cita creada\n     * @throws IllegalArgumentException si la fecha y hora vienen vacias\n     * @throws NoSuchElementException si no existe expediente con ese identificador\n     * @throws IllegalStateException si la mascota esta inactiva o el horario ya esta ocupado\n     */\n    public Cita agendar(String idMascota, String fechaHora) {\n        if (fechaHora == null || fechaHora.trim().isEmpty()) {\n            throw new IllegalArgumentException(\"La fecha y hora de la cita son obligatorias.\");\n        }\n        Mascota mascota = expedientes.get(idMascota);\n        if (mascota == null) {\n            throw new NoSuchElementException(\"No existe expediente con ID \" + idMascota);\n        }\n        if (!mascota.estaActiva()) {\n            throw new IllegalStateException(\"La mascota \" + mascota.getNombre()\n                    + \" esta inactiva y no puede agendar citas.\");\n        }\n        String horario = fechaHora.trim();\n        for (Cita registrada : citas) {\n            if (registrada.getFechaHora().equals(horario)) {\n                throw new IllegalStateException(\"Ya hay una cita agendada para \" + horario);\n            }\n        }\n        Cita cita = new Cita(idMascota, horario);\n        citas.add(cita);\n        return cita;\n    }\n\n    /**\n     * Cantidad de citas agendadas.\n     *\n     * @return numero de citas vigentes en memoria\n     */\n    public int totalCitas() { return citas.size(); }\n\n    /**\n     * Copia de la agenda actual.\n     *\n     * @return lista con las citas agendadas\n     */\n    public List<Cita> listarCitas() { return new ArrayList<Cita>(citas); }\n}\n\n/*\n * ---------------------------------------------------------------------------\n * Version JUnit de los mismos casos. Va en Test Packages, archivo AgendaServiceTest.java\n * (agregar la libreria de pruebas desde el nodo Test Libraries del proyecto).\n *\n * import org.junit.jupiter.api.BeforeEach;\n * import org.junit.jupiter.api.Test;\n * import static org.junit.jupiter.api.Assertions.assertEquals;\n * import static org.junit.jupiter.api.Assertions.assertNotNull;\n * import static org.junit.jupiter.api.Assertions.assertThrows;\n *\n * public class AgendaServiceTest {\n *\n *     private AgendaService agenda;\n *\n *     @BeforeEach\n *     public void prepararAgendaLimpia() {\n *         agenda = new AgendaService();\n *         agenda.registrarMascota(new Mascota(\"M-001\", \"Kira\", true));\n *         agenda.registrarMascota(new Mascota(\"M-002\", \"Michi\", true));\n *         agenda.registrarMascota(new Mascota(\"M-009\", \"Rocky\", false));\n *     }\n *\n *     @Test\n *     public void agendar_mascotaActiva_creaLaCita() {\n *         Cita cita = agenda.agendar(\"M-001\", \"2026-09-30 10:00\");\n *         assertNotNull(cita);\n *         assertEquals(1, agenda.totalCitas());\n *     }\n *\n *     @Test\n *     public void agendar_mascotaInactiva_lanzaIllegalStateException() {\n *         assertThrows(IllegalStateException.class,\n *                 () -> agenda.agendar(\"M-009\", \"2026-09-30 10:00\"));\n *         assertEquals(0, agenda.totalCitas());\n *     }\n * }\n * ---------------------------------------------------------------------------\n */\n",
        "codigo_archivo": "VetCareQADemo.java"
    },
    {
        "n": 9,
        "slug": "Refactorizacion con IA y persistencia de archivos",
        "titulo": "Refactorización con IA · Persistencia en archivos",
        "subtitulo": "Que los datos de VetCare no se pierdan al cerrar la ventana",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.",
        "entregable": "La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.",
        "demo": "El docente registra una mascota, cierra la aplicación, la vuelve a abrir y la mascota sigue ahí; enseguida abre mascotas.csv en el Bloc de notas para mostrar la línea que escribió el programa.",
        "teoria": [
            "Refactorizar es cambiar la forma interna del código sin cambiar ni un milímetro de su comportamiento externo. Si antes de tocar nada la aplicación registraba una mascota y mostraba 'Mascota registrada con ID M004', después de refactorizar tiene que registrar exactamente igual y mostrar exactamente el mismo mensaje; lo único que cambió es que el código quedó más fácil de leer y de modificar. En VetCare el caso clásico es el manejador del botón Registrar: un método de noventa líneas que valida el nombre, convierte la edad, genera el ID consecutivo, arma la línea del CSV, abre el archivo, escribe y muestra el aviso. Refactorizarlo es partirlo en cuatro métodos con nombre propio (validar, generarId, aLineaCsv, escribirArchivo) y mover los dos últimos a una clase RepositorioMascotasCSV. Y aquí va lo que refactorizar NO es: no es agregar funcionalidades nuevas, no es corregir errores de lógica, no es cambiar de librería, no es reescribir el proyecto desde cero. Si al terminar la aplicación hace algo distinto, eso ya no fue una refactorización: fue un cambio de requisitos disfrazado, y hay que probarlo como tal. La prueba de que el refactor salió bien es aburridamente simple: correr el mismo flujo con los mismos datos y obtener las mismas salidas.",
            "Un code smell es un síntoma en el código que casi siempre anuncia un problema mayor; no es un error de compilación ni una excepción, es un olor. Los que van a aparecer sí o sí en los proyectos de VetCare son seis. Primero, el método largo: el ActionListener del botón que hace de todo. Segundo, la duplicación: el mismo bucle de búsqueda por ID copiado y pegado en el botón Buscar, en el botón Editar y en el botón Eliminar, de modo que cuando el criterio de búsqueda cambia hay que acordarse de arreglarlo en tres lugares y siempre se olvida uno. Tercero, los nombres opacos: ArrayList<String[]> a1, variables x, d, v, un método llamado proceso(). Cuarto, los números mágicos: un if (edad > 25) sin explicación, cuando lo correcto es una constante EDAD_MAXIMA = 25 con nombre. Quinto, el catch vacío que se traga la IOException y deja al usuario creyendo que guardó. Sexto, la clase Dios: una única clase Principal que es ventana, es lista y es archivo al mismo tiempo. NetBeans ayuda a atacarlos con acciones seguras del menú Refactor: Rename (Ctrl+R), Extract Method (Ctrl+Alt+M) y Move, que renombran o extraen actualizando todas las referencias, cosa que buscar y reemplazar a mano nunca garantiza.",
            "Persistencia es lograr que los datos sobrevivan al proceso que los creó. Mientras la aplicación está corriendo, el ArrayList<Mascota> vive en la memoria RAM, que es rápida pero volátil: en el instante en que se cierra la ventana, el sistema operativo recupera esa memoria y las mascotas se evaporan. Guardar en disco significa convertir cada objeto Mascota en texto y escribirlo en un archivo que queda en el computador. Un .txt es texto libre, sirve para una bitácora o un log; un .csv es texto también, pero con una estructura tabular acordada: una línea por registro, campos separados por un carácter separador y, opcionalmente, una primera línea de encabezado que documenta el orden de las columnas. Para VetCare la línea acordada es M001;Firulais;Canino;4;1144556677 con encabezado id;nombre;especie;edad;cedula_dueno. Usamos punto y coma y no coma por dos razones muy prácticas: los nombres y las direcciones de los dueños suelen traer comas y le romperían la línea al programa, y el Excel en configuración regional de Colombia abre los archivos separados por punto y coma sin pedir nada. La ventaja enorme del CSV frente a un formato binario es que se puede abrir en el Bloc de notas y ver el dato: cuando algo falla, el estudiante ve con sus ojos si el problema está en lo que escribió o en cómo lo leyó.",
            "Un archivo abierto es un recurso del sistema operativo, y todo recurso hay que cerrarlo. Cuando se escribe con un BufferedWriter, el texto no viaja al disco letra por letra: se acumula en un buffer en memoria y se vuelca cuando el buffer se llena o cuando se cierra el flujo. Por eso el error más desconcertante para un principiante es este: el programa corre sin lanzar ninguna excepción, dice 'guardado', y el archivo mascotas.csv aparece con cero bytes. No se cerró el escritor y lo que estaba en el buffer nunca bajó al disco. La solución moderna es try-with-resources: se declara el recurso entre paréntesis, try (BufferedWriter salida = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { ... }, y Java garantiza que se llama a close() al salir del bloque, ocurra lo que ocurra, incluso si se lanzó una excepción en la mitad. Reemplaza al viejo patrón de finally con verificación de null, que casi nadie escribe bien. Además, IOException es una excepción verificada: el compilador obliga a capturarla o a declararla, y eso no es una molestia, es el lenguaje recordando que el disco puede estar lleno, el archivo puede estar abierto en Excel o la ruta puede no existir. Especificar StandardCharsets.UTF_8 no es adorno: es lo que evita que 'Ñoño' vuelva del archivo convertido en símbolos raros.",
            "La persistencia se conecta al ciclo de vida de la aplicación en dos puntos: se carga al arrancar y se guarda al cerrar (o después de cada cambio, si se quiere ser más seguro). Cargar al arrancar significa que el main construye el repositorio, pide cargar() y solo después muestra la ventana con la tabla ya poblada. Y cargar tiene que ser defensivo, porque el archivo es del mundo real: si mascotas.csv no existe todavía, cargar() devuelve una lista vacía y la aplicación abre normalmente, no revienta con una excepción en la cara del usuario; si una línea quedó con cuatro campos en vez de cinco porque alguien la editó en el Bloc de notas, esa línea se ignora, se avisa por consola con el número de línea y las demás sí se cargan; si la edad viene como 'dos', el Integer.parseInt lanza NumberFormatException, se captura, se descarta ese registro y se sigue. La regla es que un dato malo no puede tumbar la aplicación completa. Del lado de la escritura, el detalle que muerde es la ruta: si se usa la ruta relativa \"mascotas.csv\", el archivo queda en el directorio de trabajo, que al ejecutar desde NetBeans es la carpeta del proyecto. Por eso conviene imprimir una vez ruta.toAbsolutePath() para que el estudiante sepa dónde buscarlo en vez de jurar que el programa no guardó nada.",
            "Error tipico del docente que no domina el tema: le pega el enunciado a la IA, recibe una solución con ObjectOutputStream y serialización binaria o con la librería OpenCSV, y la copia al proyecto sin entenderla. En clase pasan dos cosas: o no compila porque falta agregar el .jar a las librerías del proyecto, o sí corre pero genera un archivo binario ilegible, con lo cual se pierde justo el valor pedagógico de abrir el .csv y ver la línea escrita, y además se incumple el requisito del PI, que pide .txt o .csv. La otra versión del mismo error es pedirle a la IA 'refactoriza esto', aceptar el bloque completo y no volver a correr la aplicación: la IA cambió el separador, o quitó el encabezado, o invirtió el orden de dos campos, y ahora el archivo viejo se lee corrido con el nombre en la columna de la especie. Eso ya no fue refactorizar, fue romper. La postura correcta, y hay que decirla en voz alta frente al grupo, es que la IA propone y el humano decide: se acepta únicamente lo que uno puede explicar línea por línea, se acepta de a un cambio por vez, y después de cada cambio se vuelve a correr el flujo completo de VetCare. Un docente que no puede explicar por qué su código usa try-with-resources no está en condiciones de exigirle criterio al estudiante."
        ],
        "taller": [
            "Cree el paquete vetcare.datos y dentro la clase RepositorioMascotasCSV con la constante private static final String SEPARADOR = \";\", la constante ENCABEZADO con el texto id;nombre;especie;edad;cedula_dueno y un atributo Path ruta construido con Paths.get(\"mascotas.csv\"); compile el proyecto y verifique que no hay errores rojos antes de seguir.",
            "Implemente guardar(List<Mascota>) usando try-with-resources: escriba el encabezado, recorra la lista y escriba una línea por mascota; ejecute, abra mascotas.csv en el Bloc de notas y verifique que tiene exactamente tantas líneas como mascotas más una, y el mismo número de punto y coma en todas.",
            "Implemente cargar() de forma defensiva: si el archivo no existe devuelve una lista vacía, descarta la línea de encabezado, ignora las líneas que no tengan cinco campos e ignora las que traigan una edad no numérica, avisando por consola el número de la línea; compruébelo dañando a propósito una línea del archivo y volviendo a ejecutar.",
            "Conecte el repositorio al ciclo de vida de la aplicación: cargar() al arrancar antes de mostrar la ventana y guardar() al cerrar; cierre la aplicación, vuelva a abrirla y verifique que el conteo de mascotas en la tabla es el mismo que había antes de cerrar.",
            "Haga una revisión asistida por IA de su método guardar(): pídale a la herramienta que señale problemas, aplique como máximo dos mejoras que usted pueda explicar en voz alta, rechace por escrito al menos una sugerencia y registre todo en REFACTOR.md con el formato 'sugerencia / la acepté o no / por qué'; vuelva a correr el flujo completo y confirme que el comportamiento es idéntico."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el PI exige explícitamente persistencia en archivos .txt o .csv, y sin ella VetCare sigue siendo una libreta que se borra sola: la clínica Huellitas no puede recuperar el expediente de Firulais al día siguiente.",
            "Esta es la primera clase donde el producto deja de existir solo mientras la ventana está abierta; a partir de hoy el proyecto tiene datos reales acumulados que las clases siguientes van a leer, integrar y revisar.",
            "La bitácora REFACTOR.md es también la evidencia del uso responsable de IA que se le va a exigir en la sustentación final: quien no pueda explicar su propio código no puede defenderlo."
        ],
        "escenario": [
            "VetCare ya tiene la clase Mascota con atributos privados y getters, un ArrayList<Mascota> administrado por el servicio y una ventana Swing que registra y lista (trabajo de las clases 1 a 6).",
            "En la carpeta del proyecto todavía no existe ningún archivo de datos: cada vez que se cierra la aplicación, la lista arranca vacía otra vez.",
            "Se trabaja con tres mascotas de prueba: M001 Firulais, canino, 4 años, dueño CC 1144556677; M002 Michi, felino, 2 años, dueño CC 1098765432; M003 Pelusa, felino, 1 año, dueño CC 1052233445."
        ],
        "criterios": [
            "Al cerrar la aplicación y volver a abrirla, la tabla muestra las mismas mascotas que había antes: el conteo coincide y los datos no cambiaron de columna.",
            "El archivo mascotas.csv tiene una línea de encabezado y una línea por mascota, todas con el mismo número de separadores y sin líneas en blanco intermedias.",
            "Toda lectura y escritura de archivo usa try-with-resources y captura IOException informando al usuario: no queda ningún catch vacío en el proyecto.",
            "Si mascotas.csv no existe o si una línea está dañada, la aplicación arranca igual, reporta el problema indicando el número de línea y carga los registros válidos restantes."
        ],
        "pistas": [
            "Si el archivo aparece con 0 bytes aunque el programa dijo que guardó, ¿quién debía vaciar el buffer y cuándo se supone que eso ocurre?",
            "Si al reabrir la aplicación aparecen cero mascotas pero el .csv tiene contenido, ¿está descartando el encabezado o lo está intentando convertir en una mascota?",
            "De las sugerencias que le dio la IA, ¿cuál cambia únicamente la forma del código y cuál cambia lo que el programa hace? ¿Puede explicar la diferencia sin volver a preguntarle a la IA?"
        ],
        "solucion_pasos": [
            "Paso 1. Se crea RepositorioMascotasCSV como única clase que sabe de archivos, con private static final String SEPARADOR = \";\" (comillas dobles: es un String, no un char) y private final Path ruta = Paths.get(\"mascotas.csv\"). Se aísla aquí porque así la ventana y el servicio quedan sin una sola línea de entrada/salida: el día que se cambie a base de datos solo se reemplaza esta clase. Se agrega además un método rutaAbsoluta() que devuelve ruta.toAbsolutePath().toString(), que se imprime una vez al arrancar para saber dónde quedó el archivo.",
            "Paso 2. guardar() se escribe así: try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { escritor.write(ENCABEZADO); escritor.newLine(); for (Mascota m : mascotas) { escritor.write(aLinea(m)); escritor.newLine(); } } catch (IOException e) { avisar(\"No se pudo guardar: \" + e.getMessage()); }. Se usa newLine() y no el carácter de salto escrito a mano porque newLine() pone el separador de línea del sistema operativo. El try-with-resources cierra el escritor aunque explote a la mitad, y eso es lo que garantiza que el buffer llegue al disco.",
            "Paso 3. aLinea(Mascota) concatena los cinco campos con el separador, pero pasando cada texto por limpiar(), que reemplaza cualquier punto y coma que traiga el dato por una coma. Sin ese detalle, un dueño registrado como 'Casa 3; apto 201' partiría la línea en seis campos y al recargar el archivo esa mascota se perdería. Es la lección de que el formato tiene un contrato y hay que defenderlo al escribir, no al leer.",
            "Paso 4. cargar() empieza preguntando if (!Files.exists(ruta)) return new ArrayList<>(); esa sola línea es la diferencia entre una aplicación que abre normalmente el primer día y una que arranca con una excepción. Luego, dentro del try-with-resources, se lee la primera línea y se descarta por ser el encabezado, y en el bucle while ((linea = lector.readLine()) != null) se salta lo vacío, se hace split(SEPARADOR, -1), se valida que campos.length == 5 y se convierte la edad dentro de su propio try-catch de NumberFormatException. Las líneas malas se reportan con su número y se ignoran; las buenas se agregan.",
            "Paso 5. Se conecta al ciclo de vida: en el main se construye el repositorio, se llama cargar() y solo después se muestra la ventana; en el cierre (windowClosing) se llama guardar(). Para el ejercicio de IA se le pide a la herramienta que revise guardar(); típicamente sugiere extraer el armado de la línea a un método aparte (se acepta: es forma, no comportamiento) y cambiar a serialización de objetos (se rechaza por escrito: el PI exige .csv legible y el archivo binario no se puede inspeccionar en clase). Ambas decisiones quedan en REFACTOR.md y se vuelve a correr el flujo completo para confirmar que el comportamiento no cambió."
        ],
        "solucion_rubrica": [
            "Metodo guardar() con try-with-resources, encabezado y escape del separador (3)",
            "Metodo cargar() tolerante a archivo inexistente y a lineas dañadas (3)",
            "Ciclo de vida conectado: carga al abrir y guarda al cerrar, verificado cerrando y reabriendo (2)",
            "Bitacora REFACTOR.md con al menos una sugerencia de IA aceptada y una rechazada, ambas justificadas (2)"
        ],
        "solucion_errores": [
            "Olvidar el try-with-resources (o abrir el flujo fuera del try) y quedarse con un mascotas.csv de 0 bytes, jurando que el programa no guarda porque 'no dio error'.",
            "No descartar la línea de encabezado al cargar, con lo cual el programa intenta convertir la palabra 'edad' en número, o peor, aparece una mascota fantasma llamada 'nombre' en la tabla.",
            "Escribir los campos en un orden al guardar y leerlos en otro al cargar (por ejemplo, especie y edad intercambiadas), de modo que el archivo se ve bien pero la tabla muestra 'Canino' en la columna de edad."
        ],
        "codigo_slide_titulo": "guardar(): el archivo como memoria larga de VetCare",
        "codigo_slide_lineas": [
            "// Sin esto, al cerrar la ventana la clinica Huellitas vuelve al papel.",
            "try (BufferedWriter salida = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {",
            "    salida.write(\"id;nombre;especie;edad;cedula_dueno\"); // encabezado = contrato del CSV",
            "    salida.newLine();",
            "    for (Mascota m : mascotas) {",
            "        salida.write(m.getId() + \";\" + m.getNombre() + \";\" + m.getEspecie()",
            "                   + \";\" + m.getEdad() + \";\" + m.getCedulaDueno());",
            "        salida.newLine();                 // una mascota = una linea, siempre 4 separadores",
            "    }",
            "}                                          // aqui se cierra solo y el buffer baja al disco",
            "catch (IOException e) {                    // IOException es checked: el compilador la exige",
            "    JOptionPane.showMessageDialog(null, \"No se pudo guardar: \" + e.getMessage());",
            "}                                          // un catch vacio aqui = mascota perdida en silencio"
        ],
        "codigo_slide_caption": "El try-with-resources cierra el archivo pase lo que pase; si no cierra, el .csv queda en cero bytes aunque el programa diga que guardó.",
        "quiz": [
            {
                "tipo": "om",
                "q": "¿Qué garantiza una refactorización bien hecha en VetCare?",
                "opciones": [
                    "A) Que el programa quede más rápido",
                    "B) Que se agreguen funcionalidades nuevas al proyecto",
                    "C) Que el comportamiento observable de la aplicación siga siendo exactamente el mismo",
                    "D) Que desaparezcan los bloques try-catch del código"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "¿Qué hace exactamente el try-with-resources al escribir mascotas.csv?",
                "opciones": [
                    "A) Cierra automáticamente el BufferedWriter al salir del bloque, incluso si ocurrió una excepción",
                    "B) Reintenta la operación de escritura si falla",
                    "C) Convierte las excepciones verificadas en no verificadas",
                    "D) Garantiza que el archivo se escriba aunque el disco esté lleno"
                ],
                "clave": "A"
            },
            {
                "tipo": "vf",
                "q": "Si no se cierra el BufferedWriter, mascotas.csv puede quedar vacío o incompleto aunque el programa no haya lanzado ninguna excepción.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Refactorizar incluye corregir de paso los errores de lógica que uno vaya encontrando.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Con el contrato id;nombre;especie;edad;cedula_dueno, ¿cuál es la línea correcta para Firulais, canino de 4 años del dueño con cédula 1144556677?",
                "opciones": [
                    "A) M001, Firulais, Canino, 4, 1144556677",
                    "B) Firulais;M001;4;Canino;1144556677",
                    "C) M001;Firulais;Canino;cuatro;1144556677",
                    "D) M001;Firulais;Canino;4;1144556677"
                ],
                "clave": "D"
            },
            {
                "tipo": "om",
                "q": "¿Cuál de estas situaciones es un code smell en el proyecto VetCare?",
                "opciones": [
                    "A) Que la clase Mascota tenga sus atributos privados con getters",
                    "B) Que exista una constante EDAD_MAXIMA con nombre en vez de un número suelto",
                    "C) Que el mismo bucle de búsqueda por ID esté copiado en los botones Buscar, Editar y Eliminar",
                    "D) Que la escritura del archivo esté aislada en la clase RepositorioMascotasCSV"
                ],
                "clave": "C"
            },
            {
                "tipo": "abierta",
                "q": "¿Por qué cargar() debe devolver una lista vacía en lugar de lanzar una excepción cuando mascotas.csv todavía no existe?",
                "clave": "Porque la primera vez que se instala VetCare en la clínica el archivo no existe y eso no es un error: es el estado inicial normal. Si cargar() revienta, la aplicación no abre nunca y el usuario queda bloqueado sin poder registrar la primera mascota. Devolviendo una lista vacía la aplicación arranca, permite registrar y al cerrar crea el archivo por primera vez."
            },
            {
                "tipo": "abierta",
                "q": "Un compañero acepta un refactor sugerido por la IA que no entiende y, tras el cambio, la aplicación deja de guardar la edad. ¿Qué dos reglas de uso responsable incumplió y cómo debió proceder?",
                "clave": "Incumplió dos reglas: aceptar solo código que uno pueda explicar línea por línea, y volver a ejecutar el flujo completo después de cada cambio para verificar que el comportamiento no cambió. Debió aplicar un cambio a la vez, leerlo y explicarlo, correr el ciclo registrar-guardar-cerrar-abrir comparando el archivo antes y después, y dejar en REFACTOR.md qué aceptó, qué rechazó y por qué."
            }
        ],
        "codigo_fuente": "import java.io.BufferedReader;\nimport java.io.BufferedWriter;\nimport java.io.IOException;\nimport java.nio.charset.StandardCharsets;\nimport java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.nio.file.Paths;\nimport java.util.ArrayList;\nimport java.util.List;\n\n/**\n * VetCare - Clase 9\n * Persistencia de mascotas en archivo CSV, con lectura defensiva y try-with-resources.\n * Clinica Veterinaria Huellitas.\n *\n * Ejecutar desde consola:  java VetCarePersistencia.java\n * (o crear el proyecto en NetBeans y ejecutar la clase principal)\n *\n * Corra el programa DOS veces seguidas: la segunda vez debe recuperar lo que\n * escribio la primera. Esa es toda la leccion.\n */\npublic class VetCarePersistencia {\n\n    public static void main(String[] args) {\n        RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV(\"mascotas.csv\");\n\n        System.out.println(\"=== VetCare: arranque ===\");\n        System.out.println(\"Archivo de datos: \" + repositorio.rutaAbsoluta());\n\n        List<Mascota> mascotas = repositorio.cargar();\n        System.out.println(\"Mascotas recuperadas del archivo: \" + mascotas.size());\n\n        if (mascotas.isEmpty()) {\n            System.out.println(\"No habia datos previos. Sembrando el arranque de la clinica...\");\n            mascotas.add(new Mascota(\"M001\", \"Firulais\", \"Canino\", 4, \"1144556677\"));\n            mascotas.add(new Mascota(\"M002\", \"Michi\", \"Felino\", 2, \"1098765432\"));\n        }\n\n        Mascota nueva = new Mascota(siguienteId(mascotas), \"Pelusa\", \"Felino\", 1, \"1052233445\");\n        mascotas.add(nueva);\n        System.out.println(\"Registrada en memoria: \" + nueva);\n\n        repositorio.guardar(mascotas);\n        System.out.println(\"Datos escritos en disco.\");\n\n        System.out.println(\"=== VetCare: simulacion de reapertura ===\");\n        List<Mascota> verificacion = repositorio.cargar();\n        for (Mascota m : verificacion) {\n            System.out.println(\"  \" + m);\n        }\n        System.out.println(\"Total tras reabrir: \" + verificacion.size());\n    }\n\n    /** Genera el consecutivo M001, M002, ... sin repetir ids existentes. */\n    private static String siguienteId(List<Mascota> mascotas) {\n        int mayor = 0;\n        for (Mascota m : mascotas) {\n            String id = m.getId();\n            if (id == null || id.length() < 2) {\n                continue;\n            }\n            try {\n                int numero = Integer.parseInt(id.substring(1));\n                if (numero > mayor) {\n                    mayor = numero;\n                }\n            } catch (NumberFormatException e) {\n                System.out.println(\"Aviso: id con formato inesperado, se ignora: \" + id);\n            }\n        }\n        return String.format(\"M%03d\", mayor + 1);\n    }\n}\n\n/** Modelo del dominio: una mascota de la clinica. */\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private final String especie;\n    private final int edad;\n    private final String cedulaDueno;\n\n    public Mascota(String id, String nombre, String especie, int edad, String cedulaDueno) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n        this.edad = edad;\n        this.cedulaDueno = cedulaDueno;\n    }\n\n    public String getId() {\n        return id;\n    }\n\n    public String getNombre() {\n        return nombre;\n    }\n\n    public String getEspecie() {\n        return especie;\n    }\n\n    public int getEdad() {\n        return edad;\n    }\n\n    public String getCedulaDueno() {\n        return cedulaDueno;\n    }\n\n    @Override\n    public String toString() {\n        return id + \" - \" + nombre + \" (\" + especie + \", \" + edad + \" anios) dueno CC \" + cedulaDueno;\n    }\n}\n\n/**\n * Unica clase del proyecto que sabe de archivos.\n * Si manana VetCare pasa a base de datos, solo se reemplaza esta clase.\n */\nclass RepositorioMascotasCSV {\n\n    private static final String SEPARADOR = \";\";\n    private static final String ENCABEZADO = \"id;nombre;especie;edad;cedula_dueno\";\n    private static final int CAMPOS_ESPERADOS = 5;\n\n    private final Path ruta;\n\n    public RepositorioMascotasCSV(String nombreArchivo) {\n        this.ruta = Paths.get(nombreArchivo);\n    }\n\n    public String rutaAbsoluta() {\n        return ruta.toAbsolutePath().toString();\n    }\n\n    /** Escribe TODA la lista. try-with-resources cierra y vacia el buffer pase lo que pase. */\n    public void guardar(List<Mascota> mascotas) {\n        try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {\n            escritor.write(ENCABEZADO);\n            escritor.newLine();\n            for (Mascota m : mascotas) {\n                escritor.write(aLinea(m));\n                escritor.newLine();\n            }\n        } catch (IOException e) {\n            System.out.println(\"No se pudo guardar el archivo: \" + e.getMessage());\n        }\n    }\n\n    /** Lectura defensiva: si no hay archivo devuelve lista vacia; una linea mala no tumba la app. */\n    public List<Mascota> cargar() {\n        List<Mascota> mascotas = new ArrayList<>();\n        if (!Files.exists(ruta)) {\n            return mascotas;\n        }\n        try (BufferedReader lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {\n            lector.readLine(); // primera linea = encabezado: se descarta a proposito\n            String linea;\n            int numeroDeLinea = 1;\n            while ((linea = lector.readLine()) != null) {\n                numeroDeLinea++;\n                if (linea.trim().isEmpty()) {\n                    continue;\n                }\n                Mascota m = desdeLinea(linea, numeroDeLinea);\n                if (m != null) {\n                    mascotas.add(m);\n                }\n            }\n        } catch (IOException e) {\n            System.out.println(\"No se pudo leer el archivo: \" + e.getMessage());\n        }\n        return mascotas;\n    }\n\n    private String aLinea(Mascota m) {\n        return limpiar(m.getId()) + SEPARADOR\n                + limpiar(m.getNombre()) + SEPARADOR\n                + limpiar(m.getEspecie()) + SEPARADOR\n                + m.getEdad() + SEPARADOR\n                + limpiar(m.getCedulaDueno());\n    }\n\n    private Mascota desdeLinea(String linea, int numeroDeLinea) {\n        String[] campos = linea.split(SEPARADOR, -1);\n        if (campos.length != CAMPOS_ESPERADOS) {\n            System.out.println(\"Linea \" + numeroDeLinea + \" ignorada: se esperaban \"\n                    + CAMPOS_ESPERADOS + \" campos y llegaron \" + campos.length);\n            return null;\n        }\n        try {\n            int edad = Integer.parseInt(campos[3].trim());\n            return new Mascota(campos[0].trim(), campos[1].trim(), campos[2].trim(),\n                    edad, campos[4].trim());\n        } catch (NumberFormatException e) {\n            System.out.println(\"Linea \" + numeroDeLinea + \" ignorada: la edad '\"\n                    + campos[3] + \"' no es un numero entero.\");\n            return null;\n        }\n    }\n\n    /** Protege el contrato del CSV: un dato con ';' partiria la linea y perderia el registro. */\n    private String limpiar(String texto) {\n        if (texto == null) {\n            return \"\";\n        }\n        return texto.replace(SEPARADOR, \",\").trim();\n    }\n}\n",
        "codigo_archivo": "VetCarePersistencia.java"
    },
    {
        "n": 10,
        "slug": "Parcial 2",
        "titulo": "Parcial 2",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    },
    {
        "n": 11,
        "slug": "Revision de codigo cruzada",
        "titulo": "Revisión de código cruzada",
        "subtitulo": "Leer el código de otro estudiante y devolver una crítica que sirva",
        "herramienta": "Apache NetBeans",
        "hito_pi": "Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.",
        "entregable": "Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.",
        "demo": "El docente proyecta VetCareParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.",
        "teoria": [
            "Una revisión de código es la lectura sistemática del código de otra persona con el fin de encontrar problemas antes de que lleguen al usuario, y de paso repartir conocimiento en el equipo. En la industria esto no es opcional: nadie mezcla su trabajo al proyecto sin que alguien más lo apruebe, y esa aprobación deja rastro escrito. Conviene decirlo claro porque el estudiante llega con dos ideas equivocadas: que la revisión es un examen donde lo van a rajar, o que es un trámite para poner 'todo bien' y salir rápido. No es ninguna de las dos. Es un control de calidad barato: encontrar hoy que buscarPorId devuelve null y nadie lo valida cuesta diez minutos; encontrarlo el día de la sustentación, con la ventana de VetCare congelada y la clínica Huellitas sin poder mostrar el expediente de Firulais, cuesta la nota y la credibilidad. Además la revisión enseña: quien lee el proyecto ajeno descubre una forma distinta de organizar el repositorio o de validar la edad, y se la lleva para el suyo. Hoy no hay tema técnico nuevo; hoy se entrena criterio, que es la habilidad que separa a alguien que escribe código de alguien que responde por él.",
            "Revisar no es leer de arriba a abajo a ver qué salta: se revisa por capas y en orden de importancia, porque el tiempo es finito y el detalle cosmético es el que más tienta. Primera capa: ¿el proyecto abre y hace lo que dice hacer? Se ejecuta antes de opinar. Segunda capa: corrección y casos borde, que en VetCare son siempre los mismos y hay que buscarlos a propósito: edad negativa o con letras, campos vacíos, ID repetido, buscar un ID que no existe, cerrar sin haber registrado nada, archivo mascotas.csv inexistente o con una línea dañada. Tercera capa: diseño y responsabilidades, es decir si hay clases de verdad o solo arreglos de String, si los atributos son privados, y si la ventana está haciendo de repositorio escribiendo archivos por su cuenta. Cuarta capa: manejo de errores, con el catch vacío como sospechoso número uno. Quinta capa: legibilidad, o sea nombres, métodos largos y duplicación. Y solo al final, la sexta: formato e indentación, que es la que menos vale y la que todo el mundo comenta primero. Si un informe de revisión de VetCare tiene ocho comentarios de espacios y ninguno sobre el NullPointerException al buscar un ID inexistente, esa revisión no sirvió.",
            "La retroalimentación útil tiene una estructura, y esa estructura se enseña con plantilla porque a punta de buena intención no sale. Primero, se habla del código y nunca de la persona: 'el método guarda sin validar' y jamás 'usted no valida nada'. Segundo, se aporta evidencia localizable: archivo y línea, o el paso exacto para reproducirlo. Tercero, se explica el impacto, es decir qué se rompe y cuándo, porque un hallazgo sin consecuencia no convence a nadie. Cuarto, se propone una salida concreta. Compare las dos versiones. Mala: 'el manejo de errores está horrible'. Buena: 'En VentanaPrincipal.java línea 84 el catch (Exception e) está vacío; si el disco está lleno la mascota registrada se pierde y el usuario ve el mensaje de éxito igual. Sugerencia: mostrar un JOptionPane con e.getMessage() y no limpiar el formulario hasta confirmar el guardado'. La segunda se puede atender esta tarde; la primera solo produce rabia. Dos reglas más: cuando hay duda se pregunta en vez de afirmar ('¿qué pasa si el usuario deja la edad vacía?'), y cada hallazgo se etiqueta como bloqueante, mayor o menor, porque un informe con cuarenta comentarios del mismo peso no lo atiende nadie.",
            "El checklist es lo que impide que la revisión se vuelva una conversación de gustos. Se construye directamente con los requisitos del PI de VetCare, y sus ítems son binarios y verificables: ¿existe al menos una clase del dominio con atributos privados y getters, o los datos andan sueltos en arreglos de String? ¿se usa una colección de Java para administrar las mascotas? ¿la interfaz gráfica muestra la lista y permite registrar y buscar? ¿hay try-catch en las fronteras, es decir donde entra texto del usuario y donde se toca el archivo? ¿el proyecto guarda y recupera datos de un .txt o .csv? ¿hay algún catch vacío? ¿algún método pasa de cincuenta líneas? ¿hay bloques duplicados? Cada ítem se marca cumple, no cumple o no aplica, y el 'no cumple' obliga a escribir la evidencia archivo:línea. Esto tiene tres efectos: hace comparables las revisiones entre unos y otros, evita que el revisor se quede solo con lo que le llamó la atención, y le da al autor del proyecto una lista de trabajo en vez de una sensación. El checklist no reemplaza el criterio; lo ordena, que es distinto.",
            "Recibir la crítica también se practica, y es la mitad difícil. La reacción natural del autor es defenderse en caliente y explicar por qué lo hizo así; el protocolo de clase es otro: escuchar completo, pedir aclaración si el hallazgo no se entiende, y luego decidir con una de tres respuestas escritas: acepto y corrijo (con responsable y fecha), justifico por qué se queda como está, o difiero para después de la entrega. Todo eso queda en el plan de corrección y es lo que el docente revisa. Del lado del revisor también hay deberes: verificar antes de acusar, porque un hallazgo falso como 'esto no compila' cuando en realidad faltaba abrir el proyecto correcto quema la credibilidad de todo el informe. Hay tres antipatrones que van a aparecer y conviene nombrarlos de una vez: la revisión de sello, que aprueba en dos minutos sin haber ejecutado nada; la revisión de gusto personal, que solo señala estilo e indentación; y la revisión que rediseña el proyecto ajeno, donde el revisor propone rehacer VetCare con su propia arquitectura en vez de señalar problemas concretos del que tiene enfrente.",
            "Error tipico del docente que no domina el tema: cree que revisar código es leer y decir si le gusta, entonces la sesión se convierte en un intercambio de opiniones sobre llaves e indentación mientras el NullPointerException sigue vivo; o peor, convierte la revisión en calificación entre estudiantes y se le arma la pelea en clase, porque nadie recibe bien que un compañero le ponga la nota. Otro error muy frecuente es no exigir que el revisor ejecute el proyecto antes de escribir: así aparecen hallazgos inventados y el autor se defiende con razón, con lo cual la actividad pierde toda autoridad. Y un tercero: no dar plantilla ni checklist, esperando que el criterio salga solo. El manejo correcto es explícito desde el minuto uno: la nota la pone el docente y el informe de quien revisa es un insumo, no una sentencia; todo hallazgo va con evidencia reproducible; se revisa el código y nunca a la persona; y el docente modela en vivo, con VetCareParaRevisar.java proyectado, cómo se reescribe un comentario agresivo en uno accionable. Un docente que nunca ha recibido una revisión de su propio código tiende a defender el suyo igual que el estudiante, y por eso conviene que empiece dejando revisar el archivo de la demo."
        ],
        "taller": [
            "Intercambien proyectos: cada estudiante entrega su carpeta comprimida más un archivo de tres líneas con las instrucciones de ejecución, y recibe el proyecto de otro compañero (si el docente autorizó equipos, el de otro equipo; la revisión funciona igual); lo primero es abrirlo en NetBeans y ejecutarlo, anotando si arrancó y, si no, el mensaje de error exacto copiado tal cual.",
            "Recorran el proyecto recibido con el checklist de doce ítems (clase de dominio, encapsulamiento, colección, interfaz gráfica, try-catch en fronteras, persistencia, catch vacío, métodos largos, duplicación, nombres, números mágicos, validación de casos borde) marcando cumple / no cumple / no aplica y escribiendo la evidencia archivo:línea en cada 'no cumple'.",
            "Provoquen a propósito los cuatro casos borde de VetCare (edad con letras, campos vacíos, buscar un ID inexistente, borrar o dañar una línea de mascotas.csv) y registren qué hizo la aplicación en cada uno, con el texto del mensaje o de la excepción.",
            "Redacten cinco hallazgos priorizados como bloqueante, mayor o menor, cada uno con el formato Evidencia + Impacto + Sugerencia, todos referidos al código y ninguno a la persona; incluyan al menos un bloqueante si existe.",
            "Hagan la devolución cruzada de ocho minutos por proyecto revisado y cierren con el plan de corrección escrito por su autor: qué acepta y corrige, qué justifica y deja igual, y qué difiere, con responsable en cada línea."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ la semana entrante se integran los módulos, y un defecto que entra a la integración cuesta el triple de encontrar; esta revisión es el filtro que deja entrar solo código que otro humano ya leyó.",
            "El informe que reciba cada uno es la lista de tareas real con la que va a llegar a la entrega final: deja de adivinar qué le falta a VetCare porque alguien externo se lo escribió con evidencia.",
            "Saber dar y recibir retroalimentación técnica es exactamente lo que se le va a exigir en el primer empleo, donde nadie mezcla código sin la aprobación de otro."
        ],
        "escenario": [
            "Cada estudiante llega con su versión de VetCare hasta la clase 9: dominio, colección, ventana Swing y persistencia en .csv, en distinto grado de avance.",
            "El docente proyecta el archivo VetCareParaRevisar.java, que compila y arranca pero termina con una excepción en tiempo de ejecución y contiene al menos siete hallazgos sembrados a propósito.",
            "Los estudiantes se cruzan en cadena (el 1 revisa al 2, el 2 al 3 y así hasta cerrar el círculo) y nadie revisa a quien lo está revisando (si el docente autorizó equipos, la cadena se arma entre equipos)."
        ],
        "criterios": [
            "El informe demuestra que el proyecto fue ejecutado: incluye el resultado de los cuatro casos borde con el mensaje o la excepción textual observada.",
            "El checklist está completo y todo ítem marcado 'no cumple' trae evidencia localizable en formato archivo:línea o pasos para reproducir.",
            "Los cinco hallazgos están priorizados y redactados con Evidencia + Impacto + Sugerencia; ninguno se refiere a la persona ni al esfuerzo que puso el otro estudiante.",
            "El autor del proyecto entrega su plan de corrección con las tres decisiones posibles (acepto, justifico, difiero) y un responsable por línea."
        ],
        "pistas": [
            "¿Su informe le sirve al otro estudiante para trabajar esta misma tarde, o solo le dice que algo está mal sin decirle dónde ni qué hacer?",
            "Si tuviera que borrar todos sus comentarios menos uno, ¿cuál dejaría, y por qué ese es más importante que los otros cuatro?",
            "¿Cuántos de sus hallazgos los comprobó ejecutando y cuántos los está suponiendo por haber leído el código?"
        ],
        "solucion_pasos": [
            "Paso 1. Ejecutar antes de opinar. Al correr VetCareParaRevisar.java la salida imprime cuatro líneas 'ok' (una por cada llamada a proceso), dice 'Registros en memoria: 4', imprime la ficha de M002, luego 'Busqueda 1 no encontro nada' y termina con un NullPointerException. Ese solo hecho ya produce dos hallazgos bloqueantes sin haber leído una línea: la búsqueda no encuentra un registro que sí existe, y el programa se cae al buscar un ID inexistente. Un revisor que no ejecuta se pierde justamente los dos más graves.",
            "Paso 2. Localizar la causa de la búsqueda que falla. En buscarPorId() la comparación es datos.get(i)[0] == id, que compara referencias y no contenido; como los IDs se arman en tiempo de ejecución con \"M00\" + consecutivo, no son los mismos objetos que el literal \"M002\" y la comparación siempre da falso. El hallazgo se escribe así: Evidencia, VetCareParaRevisar.java línea de buscarPorId; Impacto, ningún expediente se encuentra desde ese botón aunque la mascota esté registrada; Sugerencia, usar equals o equalsIgnoreCase, como ya lo hacen correctamente buscarDeNuevo() e imprimirFicha() en el mismo archivo. Note que el propio proyecto tiene la versión correcta a pocas líneas: eso es duplicación inconsistente y es otro hallazgo.",
            "Paso 3. El NullPointerException final. buscarDeNuevo(\"M009\") devuelve null porque ese ID no existe, y el llamador usa fantasma[1] sin validar. Hallazgo bloqueante: Evidencia, última línea de main; Impacto, la aplicación se cierra con excepción cuando la recepcionista escribe mal un ID, que es el escenario más común del mostrador; Sugerencia, validar null y mostrar 'No existe expediente con ID ...' en un JOptionPane. Aquí se aprovecha para mostrar cómo se prioriza: esto va antes que cualquier comentario de nombres.",
            "Paso 4. Barrer los hallazgos de calidad con el checklist. El catch (Exception ex) vacío convierte la edad \"dos\" en 0 y guarda el registro como si nada, lo que corrompe el dato en silencio; el if (x > 25) es un número mágico sin nombre y además no rechaza la edad -3, que entra derecho; los datos se guardan en String[] en vez de una clase Mascota, así que no hay encapsulamiento ni tipos; el atributo public static ArrayList<String[]> datos permite que cualquier clase lo modifique; el método proceso(a, b, c, d, e) no dice qué hace ni qué recibe; y los avisos salen por System.out.println, o sea que el usuario de la ventana nunca se entera. Cada uno se marca como mayor o menor según su impacto en el usuario.",
            "Paso 5. Reescribir el tono y priorizar. Se toma un comentario real y agresivo, por ejemplo 'este código es un desastre, no se entiende nada', y se convierte en un hallazgo concreto: 'Evidencia: el método proceso() de VetCareParaRevisar.java recibe cinco parámetros llamados a, b, c, d, e. Impacto: quien lo llame no sabe cuál es la especie y cuál la cédula, y basta invertir dos argumentos para registrar a Firulais como especie 1144556677. Sugerencia: recibir un objeto Mascota o renombrar los parámetros a nombre, especie, edad y cedulaDueno'. Finalmente se ordena el informe: primero los dos bloqueantes, después los mayores (catch vacío y validación de edad) y de últimos los menores; se entrega en una página y el autor del proyecto responde con su plan de corrección."
        ],
        "solucion_rubrica": [
            "Ejecucion del proyecto ajeno y reporte de los cuatro casos borde con evidencia textual (3)",
            "Checklist completo con evidencia archivo:linea en cada 'no cumple' (2)",
            "Cinco hallazgos priorizados y redactados con Evidencia + Impacto + Sugerencia (3)",
            "Plan de corrección del autor del proyecto con decisión y responsable por hallazgo (2)"
        ],
        "solucion_errores": [
            "Revisar sin ejecutar: el informe se llena de comentarios de estilo y se le escapan el NullPointerException y la búsqueda que nunca encuentra, que son los dos hallazgos que de verdad importan.",
            "Redactar sobre la persona ('no sabe programar', 'le quedó muy mal hecho') en vez de sobre el código, con lo cual el autor se pone a la defensiva y no corrige nada.",
            "Entregar treinta comentarios sin priorizar y todos del mismo peso, mezclando un catch vacío que pierde datos con una línea en blanco de más; el autor no sabe por dónde empezar y termina no atendiendo ninguno."
        ],
        "codigo_slide_titulo": "Un método real de VetCare y sus seis hallazgos",
        "codigo_slide_lineas": [
            "public static void proceso(String a, String b, String c, String d, String e) { // 1. nombre y parametros sin significado",
            "    int x = 0;",
            "    try {",
            "        x = Integer.parseInt(d);",
            "    } catch (Exception ex) {            // 2. catch vacio: la edad \"dos\" se vuelve 0 en silencio",
            "    }",
            "    if (x > 25) {                       // 3. numero magico: por que 25? y la edad -3 pasa derecho",
            "        System.out.println(\"edad rara\"); // 4. el aviso muere en consola: la ventana no se entera",
            "    }",
            "    String[] v = new String[5];         // 5. arreglo de String en vez de la clase Mascota",
            "    v[0] = a; v[1] = b; v[2] = c; v[3] = String.valueOf(x); v[4] = e;",
            "    datos.add(v);                       // 6. 'datos' es public static: cualquiera lo modifica",
            "}"
        ],
        "codigo_slide_caption": "El código compila y corre; la revisión no busca errores del compilador, busca lo que va a doler en el mostrador de la clínica.",
        "quiz": [
            {
                "tipo": "om",
                "q": "Al recibir el proyecto VetCare de otro estudiante, ¿qué se verifica primero?",
                "opciones": [
                    "A) Que el proyecto ejecute y haga lo que dice hacer",
                    "B) La indentación y las llaves",
                    "C) Los nombres de las variables",
                    "D) Que los comentarios estén actualizados"
                ],
                "clave": "A"
            },
            {
                "tipo": "om",
                "q": "¿Cuál de estos comentarios es retroalimentación útil?",
                "opciones": [
                    "A) El manejo de errores está horrible",
                    "B) Ustedes no validan nada, así no se programa",
                    "C) En VentanaPrincipal.java línea 84 el catch está vacío: si el disco está lleno la mascota se pierde y el usuario ve mensaje de éxito. Sugerencia: mostrar el error en un JOptionPane",
                    "D) Le faltó orden al proyecto en general"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Todo hallazgo debe indicar dónde está el problema (archivo y línea, o los pasos para reproducirlo).",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Si VetCare funciona en el caso normal, no hay nada que reportar en la revisión.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "¿Cuál de estos hallazgos en VetCare se clasifica como bloqueante?",
                "opciones": [
                    "A) Una variable llamada x dentro de un bucle",
                    "B) Falta una línea en blanco entre dos métodos",
                    "C) Un comentario que quedó desactualizado",
                    "D) Un catch vacío que hace perder la mascota registrada sin avisarle al usuario"
                ],
                "clave": "D"
            },
            {
                "tipo": "om",
                "q": "¿Para qué sirve el checklist de revisión?",
                "opciones": [
                    "A) Para reemplazar la nota del docente",
                    "B) Para que la revisión no dependa del gusto del revisor y sea comparable entre un proyecto y otro",
                    "C) Para que el revisor no tenga que ejecutar el proyecto",
                    "D) Para reescribir el proyecto ajeno con la arquitectura del revisor"
                ],
                "clave": "B"
            },
            {
                "tipo": "abierta",
                "q": "Reescriba el comentario 'tu código es un desastre, no se entiende nada' como un hallazgo útil sobre VetCareParaRevisar.java, usando la estructura Evidencia + Impacto + Sugerencia.",
                "clave": "Ejemplo válido: 'Evidencia: en VetCareParaRevisar.java el método proceso() recibe cinco parámetros llamados a, b, c, d, e. Impacto: quien lo llame no distingue la especie de la cédula y basta invertir dos argumentos para registrar a Firulais con la especie en el campo del documento. Sugerencia: recibir un objeto Mascota o renombrar los parámetros a nombre, especie, edad y cedulaDueno'. Se evalúa que hable del código y no de la persona, que localice el problema, que explique la consecuencia y que proponga una acción concreta."
            },
            {
                "tipo": "abierta",
                "q": "¿Por qué el revisor debe ejecutar el proyecto antes de escribir el informe?",
                "clave": "Porque hay defectos que solo se ven corriendo: la búsqueda que nunca encuentra por comparar con ==, el NullPointerException al buscar un ID inexistente, el mascotas.csv que queda en cero bytes. Además, un hallazgo inventado o mal comprobado quema la credibilidad de todo el informe y le da al autor una excusa para no atender el resto. Ejecutar permite reportar la evidencia textual del mensaje o de la excepción observada."
            }
        ],
        "codigo_fuente": "import java.util.ArrayList;\n\n/**\n * VetCare - Clase 11: material para la revision cruzada.\n * Clinica Veterinaria Huellitas.\n *\n * Este archivo COMPILA y ARRANCA, pero tiene al menos siete hallazgos de\n * revision (correccion, diseno, legibilidad y manejo de errores) y termina\n * con una excepcion en tiempo de ejecucion. Eso es a proposito.\n *\n * Ejecutar:  java VetCareParaRevisar.java\n *\n * Instruccion para el estudiante: NO corrija nada todavia. Primero ejecutelo,\n * anote la salida real, aplique el checklist y escriba los hallazgos con el\n * formato Evidencia + Impacto + Sugerencia.\n */\npublic class VetCareParaRevisar {\n\n    public static ArrayList<String[]> datos = new ArrayList<String[]>();\n\n    public static void main(String[] args) {\n        System.out.println(\"=== VetCare Huellitas (version para revisar) ===\");\n\n        int consecutivo = 1;\n        proceso(\"M00\" + consecutivo, \"Firulais\", \"Canino\", \"4\", \"1144556677\");\n        consecutivo++;\n        proceso(\"M00\" + consecutivo, \"Michi\", \"Felino\", \"2\", \"1098765432\");\n        consecutivo++;\n        proceso(\"M00\" + consecutivo, \"Pelusa\", \"Felino\", \"-3\", \"1052233445\");\n        consecutivo++;\n        proceso(\"M00\" + consecutivo, \"Nube\", \"Felino\", \"dos\", \"1052233446\");\n\n        System.out.println(\"Registros en memoria: \" + datos.size());\n\n        String[] encontrada = buscarPorId(\"M002\");\n        if (encontrada != null) {\n            System.out.println(\"Busqueda 1 encontro a: \" + encontrada[1]);\n        } else {\n            System.out.println(\"Busqueda 1 no encontro nada.\");\n        }\n\n        imprimirFicha(\"M002\");\n\n        String[] fantasma = buscarDeNuevo(\"M009\");\n        System.out.println(\"Busqueda 3 devolvio: \" + fantasma[1]);\n    }\n\n    public static void proceso(String a, String b, String c, String d, String e) {\n        int x = 0;\n        try {\n            x = Integer.parseInt(d);\n        } catch (Exception ex) {\n        }\n        if (x > 25) {\n            System.out.println(\"edad rara\");\n        }\n        String[] v = new String[5];\n        v[0] = a;\n        v[1] = b;\n        v[2] = c;\n        v[3] = String.valueOf(x);\n        v[4] = e;\n        datos.add(v);\n        System.out.println(\"ok \" + a + \" \" + b);\n    }\n\n    public static String[] buscarPorId(String id) {\n        for (int i = 0; i < datos.size(); i++) {\n            if (datos.get(i)[0] == id) {\n                return datos.get(i);\n            }\n        }\n        return null;\n    }\n\n    public static void imprimirFicha(String id) {\n        for (int i = 0; i < datos.size(); i++) {\n            if (datos.get(i)[0].equals(id)) {\n                System.out.println(\"Ficha -> id=\" + datos.get(i)[0]\n                        + \" nombre=\" + datos.get(i)[1]\n                        + \" especie=\" + datos.get(i)[2]\n                        + \" edad=\" + datos.get(i)[3]\n                        + \" cc=\" + datos.get(i)[4]);\n            }\n        }\n    }\n\n    public static String[] buscarDeNuevo(String id) {\n        for (int i = 0; i < datos.size(); i++) {\n            if (datos.get(i)[0].equals(id)) {\n                return datos.get(i);\n            }\n        }\n        return null;\n    }\n}\n",
        "codigo_archivo": "VetCareParaRevisar.java"
    },
    {
        "n": 12,
        "slug": "Integracion de modulos",
        "titulo": "Integración de módulos",
        "subtitulo": "De piezas sueltas a una aplicación que corre de punta a punta",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.",
        "entregable": "El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.",
        "demo": "El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.",
        "teoria": [
            "Integrar es lograr que piezas que ya funcionan por separado funcionen juntas dentro de un único ejecutable, y esa palabra 'juntas' esconde casi todo el trabajo. VetCare tiene cuatro piezas y conviene ponerles nombre de paquete para verlas: vetcare.modelo con Mascota (y Dueno, si el equipo lo separó), vetcare.datos con RepositorioMascotasCSV, vetcare.logica con ServicioVetCare que administra el ArrayList y aplica las reglas, y vetcare.ui con la ventana Swing. Entre ellas rige una regla de dependencia que hay que respetar como si fuera ley: la interfaz conoce al servicio, el servicio conoce al repositorio, el repositorio conoce al modelo, y nadie mira hacia arriba; en particular el servicio no puede llamar a un JOptionPane. ¿Por qué importa? Porque así se puede probar la lógica sin abrir la ventana, porque el día que se cambie el .csv por una base de datos solo se toca una clase, y porque cuando algo falle se sabe en qué capa buscar. Integrar bien no es que compile: es que exista un único punto de entrada, un único servicio y un único archivo de datos, y que cada capa haga su oficio y nada más.",
            "El flujo de punta a punta se define antes de integrar, por escrito, y se llama guion de humo porque su único fin es ver si sale humo. Para VetCare son cinco pasos: abrir la aplicación y ver la tabla poblada con lo que había en mascotas.csv; registrar una mascota nueva con dueño y ver que aparece de inmediato en la tabla; buscar por ID y ver el expediente; cerrar la ventana y confirmar que avisó cuántos registros guardó; volver a abrir y encontrar la mascota nueva. Eso es lo que tiene que correr sin que nadie toque código en la mitad. El ciclo de vida que lo soporta es igual de explícito y su orden no es negociable: el main construye el repositorio, construye el servicio pasándole el repositorio, pide cargar los datos y solo entonces manda a construir y mostrar la ventana; al cerrar, el manejador de la ventana pide guardar y solo si el guardado salió bien libera la aplicación. Si se invierte el orden y la ventana se construye antes de cargar, la tabla nace vacía aunque el archivo tenga cien mascotas, y el estudiante va a jurar que la persistencia no funciona cuando lo que está mal es la secuencia de arranque.",
            "Los errores de integración tienen firma propia y conviene reconocerlos por el síntoma. Primero, el más costoso: dos instancias del mismo servicio, una creada en el main y otra creada dentro del constructor de la ventana; se registra en la instancia de la ventana y al cerrar se guarda la del main, así que el archivo queda igual y todo el mundo culpa a la persistencia. Segundo, el orden de arranque invertido que ya mencionamos: tabla vacía con la consola diciendo 'Mascotas cargadas: 12'. Tercero, la ruta del archivo: se ejecuta desde NetBeans y el .csv queda en la carpeta del proyecto, se ejecuta el JAR desde el escritorio y queda en otra parte, entonces 'se perdieron los datos'. Cuarto, el contrato del CSV roto entre quien escribe y quien lee, con el orden de campos distinto: el archivo se ve bien en el Bloc de notas pero la tabla muestra 'Canino' en la columna de edad. Quinto, la unión del código de tres personas que trajeron cada una su propia clase Mascota con constructores distintos. Y sexto, el clásico NullPointerException porque buscarPorId devuelve null cuando el ID no existe y nadie valida antes de usar el resultado.",
            "El debugger de NetBeans es la herramienta de esta clase y hay que perderle el miedo en vivo. Se pone un breakpoint haciendo clic en el número de la línea (o Ctrl+F8), se ejecuta con Depurar proyecto (Ctrl+F5) y la aplicación se congela justo ahí. Desde ese punto, F8 avanza a la línea siguiente sin entrar a los métodos, F7 entra al método que se está llamando, Ctrl+F7 sale del método actual y F5 continúa hasta el siguiente breakpoint. Mientras está detenido, la ventana Variables muestra el valor real de cada campo y de cada objeto, Watches permite vigilar una expresión concreta como servicio.listar().size(), y Call Stack muestra quién llamó a quién, que es justo lo que uno necesita cuando no entiende por qué se ejecutó algo. Hay además una joya para integración: el breakpoint condicional, al que se le pone una condición como id.equals(\"M009\") para que solo se detenga en el caso problemático y no en las doscientas iteraciones buenas. Todo esto es superior a llenar el código de System.out.println por tres razones: no ensucia el proyecto ni deja basura que después hay que borrar, muestra el estado completo y no solo lo que uno se acordó de imprimir, y permite mirar el orden real de las llamadas.",
            "La forma de integrar sin sufrir es por goteo y no de un solo golpe. Integración de un solo golpe es juntar los cuatro módulos la noche anterior a la entrega; el resultado conocido es una aplicación que no arranca y nadie sabe cuál de los cuatro la rompió. Integración por goteo es unir de a un módulo, correr el guion de humo después de cada unión, y no avanzar mientras el ejecutable esté en rojo: primero modelo más servicio con un main de consola, después servicio más repositorio verificando el archivo en disco, después la ventana consumiendo el servicio, y por último el cierre que guarda. Cuando algo se rompe, uno sabe exactamente qué fue lo último que tocó. Tres hábitos más que valen oro: fijar por escrito el contrato entre módulos, es decir la firma de los métodos públicos del servicio y el orden exacto de los campos del CSV, para que quien escribe y quien lee no se contradigan; poner el try-catch en las fronteras, o sea en el manejador del botón y en el acceso al archivo, y no repartido por todo el modelo; y llevar la bitácora de integración con síntoma, causa y corrección de cada defecto, que es lo que se entrega y lo que salva en la sustentación.",
            "Error tipico del docente que no domina el tema: junta todos los módulos la noche anterior, en clase la aplicación no arranca, y termina explicando el flujo en el tablero mientras los estudiantes nunca ven correr el producto; después culpa a NetBeans, al JDK o al computador del salón. El segundo error es no abrir jamás el debugger: llena el código de System.out.println, y como imprime solo lo que se le ocurrió imprimir, no logra distinguir entre 'el dato llegó mal desde el formulario' y 'el dato se guardó mal en el archivo', que son dos defectos completamente distintos con el mismo síntoma. El tercero es no fijar el contrato del CSV: cada estudiante escribe su propio orden de campos, y al integrar el módulo del compañero el archivo se lee corrido, con lo que el docente concluye que 'el CSV es frágil' cuando lo frágil fue el acuerdo. La disciplina que se enseña hoy y que el docente debe haber practicado antes de entrar al salón es: integrar temprano, integrar por partes, tener un guion de humo de dos minutos que se corre después de cada cambio, y llegar a clase con VetCare ya corriendo para poder romperlo a propósito delante del grupo y arreglarlo con el debugger en vivo, que es la única forma de que el estudiante crea que la herramienta sirve."
        ],
        "taller": [
            "Organice el proyecto en los paquetes vetcare.modelo, vetcare.datos, vetcare.logica y vetcare.ui, deje un único método main en la clase de arranque, elimine cualquier otro main que haya quedado de los talleres anteriores y verifique que la aplicación abre desde ese único punto.",
            "Asegure una sola instancia: cree el repositorio y el servicio en el main y páselos por constructor a la ventana; ponga un breakpoint en el botón Registrar y otro en el cierre, y compruebe en la ventana Variables que el objeto servicio tiene el mismo identificador en ambos puntos.",
            "Corra el guion de humo de cinco pasos (abrir con datos, registrar, buscar por ID, cerrar guardando, reabrir y verificar) y anote en qué paso exacto falla y con qué mensaje; si pasa completo a la primera, dañe una línea de mascotas.csv y vuelva a correrlo.",
            "Depure el primer defecto con el debugger: breakpoint en el manejador del botón, registre el valor real de cada campo del formulario antes de llegar al servicio, identifique en qué capa se corrompe el dato y aplique la corrección; deje la evidencia en la bitácora.",
            "Repita hasta que el guion de humo corra completo dos veces seguidas y entregue la bitácora de integración con tres defectos documentados con síntoma, causa, corrección y cómo lo verificó."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ hasta hoy VetCare eran cuatro talleres que funcionaban por separado; a partir de esta clase es un producto que la clínica Huellitas podría instalar, y eso es exactamente lo que se sustenta al final.",
            "Todo lo que se construyó desde la clase 1 (POO, colecciones, GUI, try-catch y persistencia) tiene que aparecer funcionando en el mismo ejecutable: la integración es donde el PI se comprueba como un todo.",
            "La bitácora de integración con el debugger es la evidencia de que el equipo sabe diagnosticar y no solo adivinar, que es lo que se evalúa en la defensa del proyecto."
        ],
        "escenario": [
            "Cada estudiante llega con los cuatro módulos funcionando por separado y ya revisados por otro compañero en la clase anterior, con su plan de corrección en la mano.",
            "Existe un archivo mascotas.csv con datos reales de pruebas anteriores, y al menos una línea de ese archivo está dañada a propósito para probar el arranque.",
            "El contrato acordado del archivo es id;nombre;especie;edad;cedula_dueno y todos deben respetarlo tal cual para poder intercambiar archivos de datos."
        ],
        "criterios": [
            "La aplicación arranca desde un único main, muestra la tabla con los datos del archivo y no requiere tocar código para completar el guion de humo.",
            "Existe una sola instancia del servicio y del repositorio en toda la aplicación, verificable con el debugger: lo que se ve en la tabla es lo que se guarda al cerrar.",
            "Los cinco pasos del guion de humo se ejecutan de corrido dos veces seguidas, y al reabrir aparecen las mascotas registradas en la corrida anterior.",
            "La bitácora documenta tres defectos con síntoma observable, causa encontrada con el debugger, corrección aplicada y forma de verificarla; ningún defecto quedó 'arreglado' sin explicación."
        ],
        "pistas": [
            "Si la consola dice 'Mascotas cargadas: 12' pero la tabla aparece vacía, ¿el problema está en el archivo, en la carga o en el momento en que se llena la tabla?",
            "¿Cuántas veces aparece la expresión new ServicioVetCare en todo su proyecto, y qué pasaría si aparece más de una?",
            "Cuando el dato llega mal, ¿ya comprobó con el debugger si sale mal del formulario o si se daña más adelante, en el servicio o al escribir la línea del archivo?"
        ],
        "solucion_pasos": [
            "Paso 1. Se deja un solo punto de entrada y se cablea la aplicación en el orden correcto dentro del main: RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV(\"mascotas.csv\"); ServicioVetCare servicio = new ServicioVetCare(repositorio); servicio.cargarDesdeArchivo(); y solo después SwingUtilities.invokeLater(() -> new VetCareApp(servicio).setVisible(true)). El servicio se inyecta por constructor y la ventana no crea el suyo: esa sola decisión elimina de raíz el defecto de las dos instancias. Se corre y la consola debe imprimir cuántas mascotas trajo el CSV antes de que exista un solo botón en pantalla.",
            "Paso 2. Se conecta la tabla al servicio con un único método refrescarTabla() que hace modelo.setRowCount(0) y vuelve a llenar recorriendo servicio.listar(). Ese método se llama en el constructor de la ventana, después de registrar y después de cualquier cambio. Si la tabla sale vacía con datos cargados, se pone un breakpoint dentro de refrescarTabla() y en Variables se mira el tamaño de la lista: si llega en cero, el problema es que la ventana está mirando otro servicio; si llega en doce y la tabla sigue vacía, el problema es que refrescarTabla() se llamó antes de cargar o que el DefaultTableModel que se llena no es el que está montado en el JTable.",
            "Paso 3. Se ponen los try-catch en las fronteras y no en el modelo. El servicio valida y lanza DatosInvalidosException con un mensaje entendible (\"La edad debe ser un numero entero. Llego: ''\"), y quien captura y muestra el JOptionPane es el manejador del botón, que es la capa que sabe de ventanas. Con esto el caso de la edad vacía deja de guardarse como cero: antes, un catch mal ubicado la convertía en 0 en silencio; ahora el usuario ve exactamente qué escribió mal y el registro no entra.",
            "Paso 4. Se depura un defecto real con el debugger. Síntoma: al registrar 'Pelusa' con edad vacía, la mascota aparecía con edad 0. Breakpoint en registrarMascota(), Ctrl+F5 para depurar, se llena el formulario y al detenerse se mira en Variables que txtEdad.getText() trae la cadena vacía; con F7 se entra a servicio.registrar() y se ve que el Integer.parseInt lanza NumberFormatException que estaba siendo capturada asignando cero. Causa localizada en la capa de lógica, no en la interfaz. Corrección: convertir esa captura en el lanzamiento de DatosInvalidosException. Verificación: se repite el caso y ahora sale el aviso 'La edad debe ser un numero entero' y no se agrega ninguna fila a la tabla.",
            "Paso 5. Se cierra la ventana con guardado controlado: setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE) más un WindowAdapter cuyo windowClosing llama a servicio.guardarEnArchivo(), avisa cuántas mascotas quedaron en el archivo y solo entonces hace dispose(); si el guardado lanza IOException, se le pregunta al usuario si desea cerrar de todas formas en lugar de perder los datos en silencio. Después se corre el guion de humo completo dos veces seguidas: la segunda corrida debe mostrar en la tabla la mascota registrada en la primera, y ese es el criterio de que la integración quedó."
        ],
        "solucion_rubrica": [
            "Un solo main, capas separadas y una sola instancia de servicio y repositorio inyectada por constructor (3)",
            "Guion de humo de cinco pasos corriendo completo dos veces seguidas, con persistencia verificada al reabrir (3)",
            "Manejo de errores en las fronteras: validación en el servicio y mensaje al usuario en la interfaz, sin catch vacíos (2)",
            "Bitacora de integración con tres defectos documentados con síntoma, causa hallada con el debugger, corrección y verificación (2)"
        ],
        "solucion_errores": [
            "Que la ventana cree su propio ServicioVetCare además del que creó el main: se registra en una lista y se guarda la otra, entonces el archivo nunca cambia y el equipo culpa a la persistencia.",
            "Construir y mostrar la ventana antes de llamar a cargarDesdeArchivo(), con lo cual la tabla nace vacía aunque la consola confirme que se cargaron doce mascotas.",
            "Usar el resultado de buscarPorId() sin validar null, de modo que la aplicación se cae con NullPointerException justo cuando el usuario escribe un ID que no existe, que es el caso más común del mostrador."
        ],
        "codigo_slide_titulo": "El main que amarra las cuatro capas de VetCare",
        "codigo_slide_lineas": [
            "public static void main(String[] args) {",
            "    RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV(\"mascotas.csv\"); // capa de datos",
            "    ServicioVetCare servicio = new ServicioVetCare(repositorio);   // logica: dueno del ArrayList",
            "    servicio.cargarDesdeArchivo();      // PRIMERO los datos...",
            "    SwingUtilities.invokeLater(() -> new VetCareApp(servicio).setVisible(true)); // ...DESPUES la ventana",
            "}",
            "// Una sola instancia de servicio para toda la app: la ventana NO crea la suya.",
            "// Breakpoint en la linea del cargarDesdeArchivo (Ctrl+F8) y F7 para entrar:",
            "// en la ventana Variables se ve cuantas mascotas trajo el CSV antes de que",
            "// exista un solo boton en pantalla.",
            "// Si la tabla sale vacia pero la consola dice \"Mascotas cargadas: 12\", el",
            "// defecto NO esta en el archivo: esta en refrescarTabla() o en que la ventana",
            "// esta mirando otro objeto servicio."
        ],
        "codigo_slide_caption": "El orden de arranque y la instancia única no son detalles de estilo: son la causa de los dos defectos de integración más frecuentes.",
        "quiz": [
            {
                "tipo": "om",
                "q": "¿Cuál es el orden correcto de arranque en el main de VetCare?",
                "opciones": [
                    "A) Mostrar la ventana y luego cargar los datos del archivo",
                    "B) Crear la ventana y dejar que ella cree su propio servicio y cargue lo que necesite",
                    "C) Cargar los datos dentro del botón Buscar la primera vez que se use",
                    "D) Crear el repositorio, crear el servicio, cargar los datos y por último mostrar la ventana"
                ],
                "clave": "D"
            },
            {
                "tipo": "vf",
                "q": "Si la ventana crea su propio ServicioVetCare y el main crea otro, lo que se registra puede no ser lo que se guarda al cerrar.",
                "clave": "V"
            },
            {
                "tipo": "om",
                "q": "En el debugger de NetBeans, ¿qué hace F7 (Step Into)?",
                "opciones": [
                    "A) Entra al método que se está llamando en esa línea",
                    "B) Avanza a la siguiente línea sin entrar a los métodos",
                    "C) Sale del método actual y vuelve a quien lo llamó",
                    "D) Continúa la ejecución hasta el siguiente breakpoint"
                ],
                "clave": "A"
            },
            {
                "tipo": "om",
                "q": "El archivo mascotas.csv se ve bien en el Bloc de notas, pero la tabla muestra 'Canino' en la columna de edad. ¿Cuál es la causa más probable?",
                "opciones": [
                    "A) El archivo está guardado en UTF-8",
                    "B) El orden de los campos al escribir no es el mismo que al leer",
                    "C) La tabla tiene menos columnas de las necesarias",
                    "D) Falta usar try-with-resources al leer"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Llenar el código de System.out.println hace lo mismo que el debugger y no tiene desventajas.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "¿Para qué sirve un breakpoint condicional como id.equals(\"M009\")?",
                "opciones": [
                    "A) Para que la aplicación solo funcione con ese ID",
                    "B) Para borrar ese registro del archivo mascotas.csv",
                    "C) Para que la ejecución se detenga únicamente en el caso problemático y no en cada iteración",
                    "D) Para saltarse el try-catch durante la depuración"
                ],
                "clave": "C"
            },
            {
                "tipo": "abierta",
                "q": "Describa el guion de humo de VetCare en sus cinco pasos y explique para qué sirve.",
                "clave": "Paso 1: abrir la aplicación y ver la tabla poblada con lo que había en mascotas.csv. Paso 2: registrar una mascota nueva y verla aparecer de inmediato en la tabla. Paso 3: buscar por ID y ver el expediente. Paso 4: cerrar la ventana y confirmar el aviso de cuántos registros se guardaron. Paso 5: volver a abrir y encontrar la mascota registrada. Sirve como prueba rápida de dos minutos que se corre después de cada unión de módulos, para detectar de inmediato cuál fue el último cambio que rompió la aplicación."
            },
            {
                "tipo": "abierta",
                "q": "La consola dice 'Mascotas cargadas: 12' pero la tabla aparece vacía. ¿Dónde pondría el breakpoint y qué revisaría?",
                "clave": "Breakpoint dentro de refrescarTabla(), en la línea del recorrido de servicio.listar(). Con la ejecución detenida se revisa en Variables el tamaño de la lista devuelta: si llega en cero, la ventana está usando una instancia de servicio distinta a la del main y hay que inyectar la misma por constructor; si llega en doce y la tabla sigue vacía, entonces refrescarTabla() se está llamando antes de cargarDesdeArchivo() o el DefaultTableModel que se está llenando no es el que está montado en el JTable."
            }
        ],
        "codigo_fuente": "import java.awt.BorderLayout;\nimport java.awt.GridLayout;\nimport java.awt.event.WindowAdapter;\nimport java.awt.event.WindowEvent;\nimport java.io.BufferedReader;\nimport java.io.BufferedWriter;\nimport java.io.IOException;\nimport java.nio.charset.StandardCharsets;\nimport java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.nio.file.Paths;\nimport java.util.ArrayList;\nimport java.util.List;\nimport javax.swing.BorderFactory;\nimport javax.swing.JButton;\nimport javax.swing.JFrame;\nimport javax.swing.JLabel;\nimport javax.swing.JOptionPane;\nimport javax.swing.JPanel;\nimport javax.swing.JScrollPane;\nimport javax.swing.JTable;\nimport javax.swing.JTextField;\nimport javax.swing.SwingUtilities;\nimport javax.swing.WindowConstants;\nimport javax.swing.table.DefaultTableModel;\n\n/**\n * VetCare - Clase 12: aplicacion integrada de punta a punta.\n * Clinica Veterinaria Huellitas.\n *\n * Capas:  Mascota (modelo) -> RepositorioMascotasCSV (datos)\n *         -> ServicioVetCare (logica) -> VetCareApp (interfaz)\n *\n * Un solo main. Una sola instancia de servicio. Un solo archivo de datos.\n *\n * Ejecutar:  java VetCareApp.java\n *\n * Guion de humo: abrir con datos -> registrar -> buscar por ID -> cerrar\n * guardando -> reabrir y verificar que la mascota nueva sigue ahi.\n */\npublic class VetCareApp extends JFrame {\n\n    private final ServicioVetCare servicio;\n\n    private final DefaultTableModel modelo = new DefaultTableModel(\n            new Object[]{\"ID\", \"Nombre\", \"Especie\", \"Edad\", \"CC Dueno\"}, 0) {\n        @Override\n        public boolean isCellEditable(int fila, int columna) {\n            return false;\n        }\n    };\n\n    private final JTextField txtNombre = new JTextField();\n    private final JTextField txtEspecie = new JTextField();\n    private final JTextField txtEdad = new JTextField();\n    private final JTextField txtCedula = new JTextField();\n    private final JTextField txtBuscar = new JTextField();\n\n    public VetCareApp(ServicioVetCare servicio) {\n        super(\"VetCare - Clinica Veterinaria Huellitas\");\n        this.servicio = servicio;\n        construirInterfaz();\n        refrescarTabla();\n        setSize(760, 420);\n        setLocationRelativeTo(null);\n        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);\n        addWindowListener(new WindowAdapter() {\n            @Override\n            public void windowClosing(WindowEvent e) {\n                cerrarGuardando();\n            }\n        });\n    }\n\n    private void construirInterfaz() {\n        JPanel formulario = new JPanel(new GridLayout(5, 2, 6, 6));\n        formulario.setBorder(BorderFactory.createTitledBorder(\"Registrar mascota\"));\n        formulario.add(new JLabel(\"Nombre:\"));\n        formulario.add(txtNombre);\n        formulario.add(new JLabel(\"Especie:\"));\n        formulario.add(txtEspecie);\n        formulario.add(new JLabel(\"Edad (anios):\"));\n        formulario.add(txtEdad);\n        formulario.add(new JLabel(\"Cedula del dueno:\"));\n        formulario.add(txtCedula);\n        JButton btnRegistrar = new JButton(\"Registrar\");\n        btnRegistrar.addActionListener(e -> registrarMascota());\n        formulario.add(new JLabel(\"\"));\n        formulario.add(btnRegistrar);\n\n        JPanel busqueda = new JPanel(new BorderLayout(6, 6));\n        busqueda.setBorder(BorderFactory.createTitledBorder(\"Buscar expediente por ID\"));\n        JButton btnBuscar = new JButton(\"Buscar\");\n        btnBuscar.addActionListener(e -> buscarPorId());\n        busqueda.add(txtBuscar, BorderLayout.CENTER);\n        busqueda.add(btnBuscar, BorderLayout.EAST);\n\n        JPanel izquierda = new JPanel(new BorderLayout(6, 6));\n        izquierda.add(formulario, BorderLayout.NORTH);\n        izquierda.add(busqueda, BorderLayout.SOUTH);\n\n        add(izquierda, BorderLayout.WEST);\n        add(new JScrollPane(new JTable(modelo)), BorderLayout.CENTER);\n    }\n\n    /** Frontera: aqui se capturan los errores de datos y se le hablan al usuario. */\n    private void registrarMascota() {\n        try {\n            Mascota registrada = servicio.registrar(txtNombre.getText(), txtEspecie.getText(),\n                    txtEdad.getText(), txtCedula.getText());\n            refrescarTabla();\n            limpiarFormulario();\n            JOptionPane.showMessageDialog(this, \"Mascota registrada con ID \" + registrada.getId());\n        } catch (DatosInvalidosException ex) {\n            JOptionPane.showMessageDialog(this, ex.getMessage(), \"Datos invalidos\",\n                    JOptionPane.WARNING_MESSAGE);\n        }\n    }\n\n    private void buscarPorId() {\n        Mascota encontrada = servicio.buscarPorId(txtBuscar.getText());\n        if (encontrada == null) {\n            JOptionPane.showMessageDialog(this, \"No existe expediente con ID \" + txtBuscar.getText(),\n                    \"Sin resultados\", JOptionPane.INFORMATION_MESSAGE);\n        } else {\n            JOptionPane.showMessageDialog(this, encontrada.ficha(), \"Expediente\",\n                    JOptionPane.INFORMATION_MESSAGE);\n        }\n    }\n\n    private void refrescarTabla() {\n        modelo.setRowCount(0);\n        for (Mascota m : servicio.listar()) {\n            modelo.addRow(new Object[]{m.getId(), m.getNombre(), m.getEspecie(),\n                m.getEdad(), m.getCedulaDueno()});\n        }\n    }\n\n    private void limpiarFormulario() {\n        txtNombre.setText(\"\");\n        txtEspecie.setText(\"\");\n        txtEdad.setText(\"\");\n        txtCedula.setText(\"\");\n    }\n\n    private void cerrarGuardando() {\n        try {\n            servicio.guardarEnArchivo();\n            JOptionPane.showMessageDialog(this, \"Se guardaron \" + servicio.listar().size()\n                    + \" mascotas en el archivo.\");\n            dispose();\n        } catch (IOException ex) {\n            int opcion = JOptionPane.showConfirmDialog(this,\n                    \"No se pudo guardar (\" + ex.getMessage() + \"). Cerrar de todas formas?\",\n                    \"Error al guardar\", JOptionPane.YES_NO_OPTION);\n            if (opcion == JOptionPane.YES_OPTION) {\n                dispose();\n            }\n        }\n    }\n\n    public static void main(String[] args) {\n        RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV(\"mascotas.csv\");\n        ServicioVetCare servicio = new ServicioVetCare(repositorio);\n        servicio.cargarDesdeArchivo();\n        SwingUtilities.invokeLater(() -> new VetCareApp(servicio).setVisible(true));\n    }\n}\n\n/** Error de datos del usuario: no es una falla del programa, es informacion para la interfaz. */\nclass DatosInvalidosException extends Exception {\n\n    public DatosInvalidosException(String mensaje) {\n        super(mensaje);\n    }\n}\n\nclass Mascota {\n\n    private final String id;\n    private final String nombre;\n    private final String especie;\n    private final int edad;\n    private final String cedulaDueno;\n\n    public Mascota(String id, String nombre, String especie, int edad, String cedulaDueno) {\n        this.id = id;\n        this.nombre = nombre;\n        this.especie = especie;\n        this.edad = edad;\n        this.cedulaDueno = cedulaDueno;\n    }\n\n    public String getId() {\n        return id;\n    }\n\n    public String getNombre() {\n        return nombre;\n    }\n\n    public String getEspecie() {\n        return especie;\n    }\n\n    public int getEdad() {\n        return edad;\n    }\n\n    public String getCedulaDueno() {\n        return cedulaDueno;\n    }\n\n    public String ficha() {\n        return \"Expediente \" + id + \"\\nNombre: \" + nombre + \"\\nEspecie: \" + especie\n                + \"\\nEdad: \" + edad + \" anios\\nDueno CC: \" + cedulaDueno;\n    }\n}\n\n/** Logica del negocio: dueno del ArrayList y de las reglas. No sabe que existe Swing. */\nclass ServicioVetCare {\n\n    private static final int EDAD_MAXIMA = 25;\n\n    private final RepositorioMascotasCSV repositorio;\n    private final List<Mascota> mascotas = new ArrayList<>();\n\n    public ServicioVetCare(RepositorioMascotasCSV repositorio) {\n        this.repositorio = repositorio;\n    }\n\n    public void cargarDesdeArchivo() {\n        mascotas.clear();\n        mascotas.addAll(repositorio.cargar());\n        System.out.println(\"Mascotas cargadas: \" + mascotas.size());\n    }\n\n    public void guardarEnArchivo() throws IOException {\n        repositorio.guardar(mascotas);\n    }\n\n    public List<Mascota> listar() {\n        return new ArrayList<>(mascotas);\n    }\n\n    public Mascota buscarPorId(String id) {\n        if (id == null || id.trim().isEmpty()) {\n            return null;\n        }\n        for (Mascota m : mascotas) {\n            if (m.getId().equalsIgnoreCase(id.trim())) {\n                return m;\n            }\n        }\n        return null;\n    }\n\n    public Mascota registrar(String nombre, String especie, String edadTexto, String cedula)\n            throws DatosInvalidosException {\n        if (nombre == null || nombre.trim().isEmpty()) {\n            throw new DatosInvalidosException(\"El nombre de la mascota es obligatorio.\");\n        }\n        if (especie == null || especie.trim().isEmpty()) {\n            throw new DatosInvalidosException(\"La especie es obligatoria.\");\n        }\n        if (cedula == null || cedula.trim().isEmpty()) {\n            throw new DatosInvalidosException(\"La cedula del dueno es obligatoria.\");\n        }\n        String texto = (edadTexto == null) ? \"\" : edadTexto.trim();\n        int edad;\n        try {\n            edad = Integer.parseInt(texto);\n        } catch (NumberFormatException e) {\n            throw new DatosInvalidosException(\"La edad debe ser un numero entero. Llego: '\" + texto + \"'\");\n        }\n        if (edad < 0 || edad > EDAD_MAXIMA) {\n            throw new DatosInvalidosException(\"La edad debe estar entre 0 y \" + EDAD_MAXIMA + \" anios.\");\n        }\n        Mascota nueva = new Mascota(siguienteId(), nombre.trim(), especie.trim(), edad, cedula.trim());\n        mascotas.add(nueva);\n        return nueva;\n    }\n\n    private String siguienteId() {\n        int mayor = 0;\n        for (Mascota m : mascotas) {\n            String id = m.getId();\n            if (id == null || id.length() < 2) {\n                continue;\n            }\n            try {\n                int numero = Integer.parseInt(id.substring(1));\n                if (numero > mayor) {\n                    mayor = numero;\n                }\n            } catch (NumberFormatException e) {\n                System.out.println(\"Aviso: id con formato inesperado, se ignora: \" + id);\n            }\n        }\n        return String.format(\"M%03d\", mayor + 1);\n    }\n}\n\n/** Unica clase que sabe de archivos. Contrato: id;nombre;especie;edad;cedula_dueno */\nclass RepositorioMascotasCSV {\n\n    private static final String SEPARADOR = \";\";\n    private static final String ENCABEZADO = \"id;nombre;especie;edad;cedula_dueno\";\n    private static final int CAMPOS_ESPERADOS = 5;\n\n    private final Path ruta;\n\n    public RepositorioMascotasCSV(String nombreArchivo) {\n        this.ruta = Paths.get(nombreArchivo);\n    }\n\n    public String rutaAbsoluta() {\n        return ruta.toAbsolutePath().toString();\n    }\n\n    public void guardar(List<Mascota> mascotas) throws IOException {\n        try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) {\n            escritor.write(ENCABEZADO);\n            escritor.newLine();\n            for (Mascota m : mascotas) {\n                escritor.write(limpiar(m.getId()) + SEPARADOR\n                        + limpiar(m.getNombre()) + SEPARADOR\n                        + limpiar(m.getEspecie()) + SEPARADOR\n                        + m.getEdad() + SEPARADOR\n                        + limpiar(m.getCedulaDueno()));\n                escritor.newLine();\n            }\n        }\n    }\n\n    public List<Mascota> cargar() {\n        List<Mascota> mascotas = new ArrayList<>();\n        if (!Files.exists(ruta)) {\n            System.out.println(\"No existe \" + rutaAbsoluta() + \": se arranca con la lista vacia.\");\n            return mascotas;\n        }\n        try (BufferedReader lector = Files.newBufferedReader(ruta, StandardCharsets.UTF_8)) {\n            lector.readLine(); // primera linea = encabezado: se descarta\n            String linea;\n            int numeroDeLinea = 1;\n            while ((linea = lector.readLine()) != null) {\n                numeroDeLinea++;\n                if (linea.trim().isEmpty()) {\n                    continue;\n                }\n                String[] campos = linea.split(SEPARADOR, -1);\n                if (campos.length != CAMPOS_ESPERADOS) {\n                    System.out.println(\"Linea \" + numeroDeLinea + \" ignorada: llegaron \"\n                            + campos.length + \" campos y se esperaban \" + CAMPOS_ESPERADOS);\n                    continue;\n                }\n                try {\n                    mascotas.add(new Mascota(campos[0].trim(), campos[1].trim(), campos[2].trim(),\n                            Integer.parseInt(campos[3].trim()), campos[4].trim()));\n                } catch (NumberFormatException e) {\n                    System.out.println(\"Linea \" + numeroDeLinea + \" ignorada: edad no numerica ('\"\n                            + campos[3] + \"')\");\n                }\n            }\n        } catch (IOException e) {\n            System.out.println(\"No se pudo leer el archivo: \" + e.getMessage());\n        }\n        return mascotas;\n    }\n\n    private String limpiar(String texto) {\n        if (texto == null) {\n            return \"\";\n        }\n        return texto.replace(SEPARADOR, \",\").trim();\n    }\n}\n",
        "codigo_archivo": "VetCareApp.java"
    },
    {
        "n": 13,
        "slug": "Control de excepciones",
        "titulo": "Control de excepciones · try-catch-finally",
        "subtitulo": "Que VetCare no se caiga porque escribieron 'tres' en la edad",
        "herramienta": "Apache NetBeans",
        "hito_pi": "El registro de mascotas de VetCare valida edad, peso e ID y avisa con un mensaje claro en lugar de cerrarse.",
        "entregable": "Clase DatoInvalidoException mas los setters validados de Mascota y la carga del CSV con try-with-resources, con evidencia de cinco pruebas de entrada (cuatro malas y una valida), subido a ExamLab.",
        "demo": "El docente escribe 'tres' en el campo edad, muestra la aplicacion reventando con el stack trace rojo, y en vivo la envuelve en try-catch hasta que responde con un aviso amable.",
        "teoria": [
            "Una excepcion es un objeto que Java crea en el momento exacto en que una instruccion no puede cumplir lo que promete, y que interrumpe el flujo normal del programa para buscar a alguien que se haga cargo. No es un mensaje de texto: es un objeto con tipo, mensaje y rastro de llamadas (stack trace). Toda la familia cuelga de Throwable, que se divide en Error (fallas de la maquina virtual, como quedarse sin memoria, que no debemos atrapar) y Exception (fallas del programa o del entorno, que si podemos atender). En VetCare esto se ve todos los dias: cuando la secretaria de la clinica Huellitas escribe 'tres' en el campo edad y el codigo hace Integer.parseInt(txtEdad.getText()), Java no puede convertir esa palabra en numero, entonces fabrica un objeto NumberFormatException, lo lanza hacia arriba y, como nadie lo recibe, el hilo muere: la ventana queda congelada y en la consola aparece el chorro rojo que asusta al usuario. La excepcion no es el enemigo, es el mensajero; el problema es que nadie la esta esperando.",
            "Java parte las excepciones en dos grupos y esa division decide cuanto codigo debe escribir usted. Las checked (Exception y sus hijas, menos RuntimeException) representan fallas previsibles del mundo exterior: el archivo mascotas.csv que alguien borro, el disco lleno, la carpeta sin permisos; el compilador las vigila y obliga a capturarlas con try-catch o a declararlas con throws, y si no lo hace su proyecto ni siquiera compila. Las unchecked (RuntimeException y sus hijas: NumberFormatException, NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException) representan errores de programacion o datos que nadie valido, y el compilador las deja pasar en silencio hasta que explotan en ejecucion. La regla practica que le sirve al estudiante es esta: si la falla viene de afuera (archivo, red, base de datos) casi siempre es checked; si la falla viene de adentro (usted no valido, usted no inicializo el objeto, usted se salio del arreglo) casi siempre es unchecked. En VetCare la lectura de datos/mascotas.csv lanza IOException, que es checked, y la conversion de la edad lanza NumberFormatException, que es unchecked; por eso se manejan en lugares distintos del programa y por eso una obliga a escribir throws y la otra no.",
            "La estructura try-catch-finally tiene una anatomia que conviene explicar despacio. En el try va el codigo que puede fallar y nada mas: entre menos lineas tenga el try, mas facil es saber quien fallo. En los catch va la reaccion, y se escriben del tipo mas especifico al mas general, porque Java entrega la excepcion al primer catch que la acepte; si usted pone catch (Exception e) antes de catch (NumberFormatException e), NetBeans marca error de compilacion con el mensaje 'exception has already been caught'. Por la misma razon, al leer el CSV de VetCare, catch (FileNotFoundException e) va antes que catch (IOException e), porque la primera es hija de la segunda. Desde Java 7 se pueden unir tipos hermanos con multi-catch: catch (NumberFormatException | NullPointerException e). El bloque finally se ejecuta siempre, haya o no haya excepcion, e incluso si dentro del try hay un return (lo unico que se lo salta es apagar la maquina virtual con System.exit), y por eso fue durante anios el sitio para cerrar archivos y liberar recursos. Hoy preferimos el try-with-resources, que abre el recurso entre los parentesis del try y lo cierra solo, y funciona con cualquier objeto que implemente la interfaz AutoCloseable, como BufferedReader o PrintWriter: try (BufferedReader lector = new BufferedReader(new FileReader('datos/mascotas.csv'))) { ... }. En VetCare esto significa que si el CSV esta corrupto a la mitad, el archivo igual se cierra y la aplicacion sigue viva con las mascotas que alcanzo a leer.",
            "throw y throws se parecen en el nombre y hacen cosas opuestas, y esa confusion es la que mas cuesta en el parcial. throw (sin s) es una instruccion que se ejecuta y lanza un objeto en ese instante: throw new DatoInvalidoException('La edad debe estar entre 0 y 30 anios.'). throws (con s) es una advertencia escrita en la firma del metodo: public void setEdad(String texto) throws DatoInvalidoException, y significa 'yo no resuelvo esto, quien me llame vera que hace'. De ahi sale la regla de capas que usaremos en VetCare: las clases del dominio (Mascota, Dueno, Cita) validan y LANZAN, porque no saben si hay una ventana, una consola o un servidor al otro lado; la capa de interfaz (el JFrame o el menu de consola) CAPTURA y traduce ese error a un JOptionPane que el usuario entiende. Crear una excepcion propia vale la pena por dos motivos: como DatoInvalidoException extiende Exception queda checked, es decir que el compilador no deja que nadie llame a setEdad sin hacerse cargo del error, y ademas el mensaje ya viene escrito en lenguaje de la clinica y no en lenguaje de la maquina: el usuario lee 'La edad debe ser un numero entero' y no 'For input string: tres'.",
            "El catch vacio, ese catch (Exception e) { } que aparece cuando NetBeans ofrece 'Surround with try-catch' y el estudiante borra el contenido para que no moleste, es el error mas caro del curso. Silencia la falla pero no la arregla: el objeto queda a medio construir, la mascota nunca se agrego a la lista, el usuario cree que guardo y el error reaparece tres pantallas mas adelante como un NullPointerException que no tiene nada que ver con la causa real. Manejar una excepcion significa hacer al menos una de cuatro cosas: informarle al usuario en su idioma, registrar el problema para poder repararlo despues, asumir un valor por defecto que este documentado, o relanzar la excepcion envuelta en otra con mas contexto. Ojo: e.printStackTrace() tampoco es manejar, es apenas dejar una nota en una consola que el usuario final nunca ve. Y la mejor excepcion es la que no ocurre: validar antes de convertir (revisar null, aplicar trim, verificar isEmpty y comprobar el rango) evita el 80 por ciento de los try-catch de VetCare y hace que el codigo se lea como las reglas del negocio.",
            "Error tipico del docente que no domina el tema: envolver todo el main en un unico try { ... } catch (Exception e) { } gigante y anunciarle al grupo que 'el programa ya quedo blindado'. Lo que quedo fue ciego: cualquier falla, venga del archivo o de la edad, cae en el mismo saco, se pierde la causa y el usuario no recibe ningun mensaje util. Otras variantes del mismo error son usar excepciones para controlar el flujo normal (lanzar una excepcion para decir que la busqueda no encontro la mascota, en vez de devolver null o un Optional), atrapar Throwable o Error creyendo que 'asi cubro todo', y explicar que las excepciones 'son cuando el programa se dana', lo cual deja al estudiante sin la idea clave: la excepcion es un canal de comunicacion entre la capa que detecta el problema y la capa que sabe como responderle al humano. Antes de la clase practique tres cosas en NetBeans: provocar el error de compilacion por catch mal ordenado, mostrar que finally se ejecuta incluso cuando el try hace return, y borrar datos/mascotas.csv para que el grupo vea la diferencia entre FileNotFoundException y IOException; son las tres preguntas que el grupo siempre hace."
        ],
        "taller": [
            "Paso 1. Abra el proyecto VetCare en NetBeans, cree el paquete vetcare.excepciones y dentro la clase DatoInvalidoException que extienda Exception con un constructor que reciba el mensaje; compile y verifique que no hay errores.",
            "Paso 2. En la clase Mascota reemplace setEdad(int) por setEdad(String texto) throws DatoInvalidoException: rechace vacio, convierta con Integer.parseInt dentro de un try, atrape NumberFormatException y relance DatoInvalidoException con un mensaje de la clinica, y valide el rango 0 a 30; repita la idea en setPeso con Double.parseDouble y rango 0.1 a 120.",
            "Paso 3. En el formulario de registro (JFrame o menu de consola) envuelva las llamadas a los setters en un try-catch que muestre JOptionPane.showMessageDialog con e.getMessage(), devuelva el foco al campo culpable con requestFocus() y NO agregue la mascota a la lista cuando hubo error.",
            "Paso 4. Cambie la carga de datos/mascotas.csv a try-with-resources con dos catch separados: FileNotFoundException, que arranca con lista vacia e informa que es la primera ejecucion, e IOException, que muestra el problema real; las lineas del CSV con datos malos se omiten con un aviso, sin tumbar la carga completa.",
            "Paso 5. Pruebe el formulario con estas cinco entradas de edad: vacio, 'tres', '-2', '150' y '4'; capture la pantalla de cada caso, arme una tabla de evidencia con entrada, mensaje mostrado y estado de la aplicacion, y suba el codigo mas la tabla a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el requisito tecnico del Proyecto Integrador exige manejo de errores con try-catch, y el jurado lo comprueba de la forma mas simple: escribe basura en un campo y mira si la aplicacion aguanta.",
            "VetCare ya tiene clases, colecciones, ventanas y archivos; lo unico que falta para que sea usable por la secretaria de Huellitas es que un dato mal escrito no borre el trabajo de toda la manana.",
            "Todo lo que blindemos hoy es lo que permitira, en la clase 14, hacer una demo en vivo tranquila: hasta se puede provocar el error a proposito para mostrar la validacion como una fortaleza."
        ],
        "escenario": [
            "El proyecto VetCare ya trae las clases Dueno, Mascota y Cita, un ArrayList<Mascota> cargado en memoria y el archivo datos/mascotas.csv con seis registros separados por punto y coma.",
            "El formulario de registro toma el texto del campo edad y hace Integer.parseInt directo, sin validar nada; hoy la aplicacion se cae con cualquier letra o campo vacio.",
            "En la carpeta datos hay tambien un archivo mascotas_danado.csv con una linea incompleta y una edad escrita como 'dos', para probar la carga tolerante a errores."
        ],
        "criterios": [
            "Existe la clase DatoInvalidoException que extiende Exception y todos sus mensajes estan escritos en lenguaje de la clinica, no en lenguaje tecnico.",
            "Con las cinco entradas de prueba (vacio, texto, negativo, fuera de rango y valida) la aplicacion nunca se cierra ni muestra stack trace al usuario, y solo la ultima agrega la mascota.",
            "La lectura del CSV usa try-with-resources, distingue FileNotFoundException de IOException y omite unicamente las lineas malas, conservando las buenas.",
            "No queda ningun catch vacio en el proyecto: cada catch informa, registra o asume un valor por defecto documentado con un comentario."
        ],
        "pistas": [
            "Si borro el archivo datos/mascotas.csv y ejecuto la aplicacion, ¿arranca con lista vacia y un aviso, o se cierra?",
            "¿En que capa esta el mensaje que ve el usuario: dentro de la clase Mascota o dentro del formulario? ¿Que pasaria si manana cambio Swing por consola?",
            "¿Cuantos catch de mi proyecto no tienen ni una linea adentro, y que haria el sistema si esa falla ocurriera de verdad?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. En vetcare/excepciones/DatoInvalidoException.java escriba: public class DatoInvalidoException extends Exception { public DatoInvalidoException(String mensaje) { super(mensaje); } }. El constructor no hace nada raro: recibe el texto y se lo pasa a super(mensaje), que es lo que despues devuelve e.getMessage(). Al extender Exception y no RuntimeException la excepcion queda checked, y eso es exactamente lo que buscamos: el compilador obligara a que cualquiera que llame a setEdad la declare con throws o la capture, de modo que nadie la ignore por descuido.",
            "Paso 2 resuelto. En Mascota: public void setEdad(String texto) throws DatoInvalidoException { if (texto == null || texto.trim().isEmpty()) { throw new DatoInvalidoException(\"La edad no puede quedar vacia.\"); } int valor; try { valor = Integer.parseInt(texto.trim()); } catch (NumberFormatException e) { throw new DatoInvalidoException(\"La edad debe ser un numero entero. Escribieron: \" + texto); } if (valor < 0 || valor > 30) { throw new DatoInvalidoException(\"La edad debe estar entre 0 y 30 anios. Recibi: \" + valor); } this.edad = valor; }. Fijese en tres detalles: el orden de las validaciones va de vacio a formato y de formato a regla del negocio, de modo que cada mensaje senala una causa distinta; la asignacion this.edad = valor es la ultima linea, asi que el objeto nunca queda con un dato a medias; y setPeso es identico cambiando Integer.parseInt por Double.parseDouble(texto.trim().replace(',', '.')) y el rango por 0.1 a 120 kg, porque en Colombia la secretaria escribe 12,5 con coma.",
            "Paso 3 resuelto. En el boton Guardar del formulario: try { Mascota m = new Mascota(txtId.getText(), txtNombre.getText()); m.setEdad(txtEdad.getText()); m.setPeso(txtPeso.getText()); listaMascotas.add(m); JOptionPane.showMessageDialog(this, \"Mascota registrada.\"); } catch (DatoInvalidoException ex) { JOptionPane.showMessageDialog(this, ex.getMessage(), \"Dato invalido\", JOptionPane.WARNING_MESSAGE); txtEdad.requestFocus(); }. El add queda DENTRO del try y despues de los setters: si algo falla, la instruccion add nunca se ejecuta y la mascota incompleta jamas entra a la coleccion. Note ademas que aqui, y solo aqui, aparece la palabra JOptionPane: la clase Mascota no muestra ventanas, porque el dia que VetCare se vuelva web esa clase debe seguir sirviendo sin tocar una linea.",
            "Paso 4 resuelto. La carga queda con dos niveles de try. El externo protege el archivo y el interno protege cada linea: try (BufferedReader lector = new BufferedReader(new FileReader(\"datos/mascotas.csv\"))) { String linea; while ((linea = lector.readLine()) != null) { String[] c = linea.split(\";\"); if (c.length < 4) { System.out.println(\"Linea incompleta omitida: \" + linea); continue; } try { Mascota m = new Mascota(c[0], c[1]); m.setEdad(c[2]); m.setPeso(c[3]); lista.add(m); } catch (DatoInvalidoException e) { System.out.println(\"Linea omitida: \" + e.getMessage()); } } } catch (FileNotFoundException e) { System.out.println(\"No existe el archivo; VetCare arranca con la lista vacia. Es la primera ejecucion.\"); } catch (IOException e) { System.out.println(\"Fallo la lectura del archivo: \" + e.getMessage()); }. Tres cosas para explicar en el tablero: el catch de FileNotFoundException va antes que el de IOException porque es su hija y al reves el proyecto no compila; el try interno es el que permite que la linea con edad 'dos' se omita sin tumbar las otras cinco; y no hace falta ningun finally para cerrar el lector, porque BufferedReader implementa AutoCloseable y el try-with-resources lo cierra solo, incluso si hubo excepcion.",
            "Paso 5 resuelto. La tabla de evidencia queda con cinco filas y tres columnas (entrada, mensaje mostrado, estado de la aplicacion): campo vacio muestra 'La edad no puede quedar vacia', la ventana sigue abierta y la lista queda en su tamano anterior; 'tres' muestra 'La edad debe ser un numero entero. Escribieron: tres', igual estado; '-2' y '150' muestran 'La edad debe estar entre 0 y 30 anios' con el valor recibido, y tampoco agregan nada; '4' no muestra advertencia, muestra 'Mascota registrada' y la lista crece exactamente en uno, lo cual se comprueba mirando la tabla del formulario o imprimiendo listaMascotas.size() antes y despues. La regla de aceptacion es dura: si en alguna fila aparece un stack trace rojo en la consola o la ventana se congela, el taller no esta terminado."
        ],
        "solucion_rubrica": [
            "Clase DatoInvalidoException checked, con mensajes en lenguaje de la clinica (2)",
            "Setters setEdad y setPeso que validan vacio, formato y rango, y lanzan con throws (3)",
            "Carga de CSV con try-with-resources y catch diferenciados (FileNotFoundException / IOException) sin perder las lineas buenas (3)",
            "Tabla de evidencia con las cinco pruebas, sin cierres de la aplicacion ni catch vacios (2)"
        ],
        "solucion_errores": [
            "Poner catch (Exception e) antes de catch (NumberFormatException e), o catch (IOException e) antes de catch (FileNotFoundException e): NetBeans marca 'exception has already been caught' y el proyecto no compila; los catch van del mas especifico al mas general.",
            "Dejar el add a la lista fuera del try o antes de los setters: la mascota entra a la coleccion sin edad ni peso y el error aparece despues, al guardar el CSV, con una linea que dice ';;0;0.0'.",
            "Mostrar e.getMessage() de la NumberFormatException original al usuario: el cliente de la clinica lee 'For input string: tres', que no le dice que hacer; hay que traducir la excepcion tecnica a un mensaje del negocio."
        ],
        "codigo_slide_titulo": "Validar la edad sin que VetCare se caiga",
        "codigo_slide_lineas": [
            "public void setEdad(String texto) throws DatoInvalidoException {   // el dominio LANZA, no muestra ventanas",
            "    if (texto == null || texto.trim().isEmpty()) {",
            "        throw new DatoInvalidoException(\"La edad no puede quedar vacia.\");   // validar ANTES de convertir",
            "    }",
            "    int valor;",
            "    try {",
            "        valor = Integer.parseInt(texto.trim());        // aqui nace NumberFormatException (unchecked)",
            "    } catch (NumberFormatException e) {",
            "        throw new DatoInvalidoException(\"La edad debe ser un numero entero. Escribieron: \" + texto);",
            "    }",
            "    if (valor < 0 || valor > 30) {                     // regla del negocio, no del lenguaje",
            "        throw new DatoInvalidoException(\"Edad fuera de rango (0-30 anios). Recibi: \" + valor);",
            "    }",
            "    this.edad = valor;   // solo se asigna cuando el dato paso las tres validaciones",
            "}"
        ],
        "codigo_slide_caption": "El objeto valida y lanza; la ventana captura y traduce: asi el mismo codigo sirve en Swing, en consola o en un servidor.",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare, el usuario escribe 'tres' en el campo edad y el codigo ejecuta Integer.parseInt(txtEdad.getText()). ¿Que excepcion se lanza?",
                "opciones": [
                    "A) IOException",
                    "B) NumberFormatException",
                    "C) NullPointerException",
                    "D) ArithmeticException"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Las excepciones checked obligan al programador a capturarlas con try-catch o a declararlas con throws, y si no lo hace el proyecto no compila.",
                "clave": "V"
            },
            {
                "tipo": "om",
                "q": "¿Cuando se ejecuta el bloque finally?",
                "opciones": [
                    "A) Solo si no hubo excepcion",
                    "B) Solo si hubo excepcion",
                    "C) Siempre, haya o no excepcion, incluso si dentro del try hay un return",
                    "D) Solo cuando se usa try-with-resources"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Al leer datos/mascotas.csv se escribe catch (IOException e) antes de catch (FileNotFoundException e). ¿Que ocurre?",
                "opciones": [
                    "A) Compila y funciona igual",
                    "B) Error de compilacion: 'exception has already been caught', porque FileNotFoundException es hija de IOException",
                    "C) Solo aparece una advertencia amarilla en NetBeans",
                    "D) Compila, pero el archivo se cierra dos veces"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "throw y throws son sinonimos y se pueden usar indistintamente.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "El try-with-resources que usa VetCare para leer el CSV cierra automaticamente los objetos que implementan la interfaz:",
                "opciones": [
                    "A) Serializable",
                    "B) AutoCloseable",
                    "C) Comparable",
                    "D) Runnable"
                ],
                "clave": "B"
            },
            {
                "tipo": "abierta",
                "q": "Explique por que un catch vacio es peligroso en VetCare y mencione dos alternativas correctas.",
                "clave": "Porque silencia la falla sin resolverla: la mascota nunca se agrega a la lista, el usuario cree que guardo y el error reaparece despues como un NullPointerException lejos de la causa real. Alternativas correctas: mostrar un mensaje claro al usuario (JOptionPane con e.getMessage()), registrar el error en un log o archivo, asumir un valor por defecto documentado con un comentario, o relanzar la excepcion envuelta con mas contexto."
            },
            {
                "tipo": "abierta",
                "q": "Escriba la firma y las tres validaciones que debe tener setEdad(String) en la clase Mascota antes de asignar el valor.",
                "clave": "public void setEdad(String texto) throws DatoInvalidoException. Validaciones: 1) que el texto no sea null ni vacio despues de trim; 2) convertir con Integer.parseInt dentro de un try y atrapar NumberFormatException para relanzar DatoInvalidoException con mensaje del negocio; 3) verificar el rango valido 0 a 30 anios. Solo si pasa las tres se ejecuta this.edad = valor, que va como ultima linea del metodo."
            }
        ],
        "codigo_fuente": "import java.io.BufferedReader;\nimport java.io.File;\nimport java.io.FileNotFoundException;\nimport java.io.FileReader;\nimport java.io.IOException;\nimport java.io.PrintWriter;\nimport java.util.ArrayList;\nimport java.util.List;\nimport java.util.Scanner;\n\n/**\n * VetCare - Clinica Veterinaria Huellitas\n * Clase 13: control de excepciones (checked vs unchecked, try-catch-finally, throw / throws).\n * Ejecutar en Apache NetBeans: clic derecho sobre el archivo y luego Run File.\n */\npublic class DemoExcepcionesVetCare {\n\n    private static final String ARCHIVO = \"datos/mascotas.csv\";\n\n    /** Excepcion CHECKED propia: al extender Exception el compilador obliga a capturarla o a declararla. */\n    public static class DatoInvalidoException extends Exception {\n\n        public DatoInvalidoException(String mensaje) {\n            super(mensaje);\n        }\n    }\n\n    /** Entidad del dominio: valida y LANZA. Nunca muestra ventanas ni le habla al usuario. */\n    public static class Mascota {\n\n        private String id;\n        private String nombre;\n        private int edad;\n        private double peso;\n\n        public Mascota(String id, String nombre) throws DatoInvalidoException {\n            if (id == null || id.trim().isEmpty()) {\n                throw new DatoInvalidoException(\"El ID de la mascota es obligatorio.\");\n            }\n            if (nombre == null || nombre.trim().isEmpty()) {\n                throw new DatoInvalidoException(\"El nombre de la mascota es obligatorio.\");\n            }\n            this.id = id.trim();\n            this.nombre = nombre.trim();\n        }\n\n        public String getId() {\n            return id;\n        }\n\n        public String getNombre() {\n            return nombre;\n        }\n\n        public void setEdad(String texto) throws DatoInvalidoException {\n            if (texto == null || texto.trim().isEmpty()) {\n                throw new DatoInvalidoException(\"La edad no puede quedar vacia.\");\n            }\n            int valor;\n            try {\n                valor = Integer.parseInt(texto.trim());\n            } catch (NumberFormatException e) {\n                // Traducimos una excepcion tecnica (unchecked) a un mensaje del negocio.\n                throw new DatoInvalidoException(\"La edad debe ser un numero entero. Escribieron: \" + texto);\n            }\n            if (valor < 0 || valor > 30) {\n                throw new DatoInvalidoException(\"La edad debe estar entre 0 y 30 anios. Recibi: \" + valor);\n            }\n            this.edad = valor;\n        }\n\n        public void setPeso(String texto) throws DatoInvalidoException {\n            if (texto == null || texto.trim().isEmpty()) {\n                throw new DatoInvalidoException(\"El peso no puede quedar vacio.\");\n            }\n            double valor;\n            try {\n                valor = Double.parseDouble(texto.trim().replace(',', '.'));\n            } catch (NumberFormatException e) {\n                throw new DatoInvalidoException(\"El peso debe ser un numero, por ejemplo 12.5. Escribieron: \" + texto);\n            }\n            if (valor <= 0 || valor > 120) {\n                throw new DatoInvalidoException(\"El peso debe estar entre 0.1 y 120 kg. Recibi: \" + valor);\n            }\n            this.peso = valor;\n        }\n\n        public String toLineaCsv() {\n            return id + \";\" + nombre + \";\" + edad + \";\" + peso;\n        }\n\n        @Override\n        public String toString() {\n            return id + \" - \" + nombre + \" (\" + edad + \" anios, \" + peso + \" kg)\";\n        }\n    }\n\n    /** Capa de aplicacion: aqui SI se captura, porque aqui se le habla al usuario. */\n    private static void registrar(List<Mascota> agenda, String id, String nombre, String edad, String peso) {\n        try {\n            Mascota m = new Mascota(id, nombre);\n            m.setEdad(edad);\n            m.setPeso(peso);\n            agenda.add(m);   // el add va DESPUES de validar: nada incompleto entra a la coleccion\n            System.out.println(\"  [OK] Registrada: \" + m);\n        } catch (DatoInvalidoException e) {\n            // En Swing seria: JOptionPane.showMessageDialog(this, e.getMessage(), \"Dato invalido\", JOptionPane.WARNING_MESSAGE);\n            System.out.println(\"  [AVISO AL USUARIO] \" + e.getMessage());\n        } finally {\n            System.out.println(\"  (finally) Intento terminado. Mascotas en memoria: \" + agenda.size());\n        }\n    }\n\n    /** Prueba de que finally se ejecuta incluso cuando el try ya hizo return. */\n    private static String buscarNombrePorId(List<Mascota> agenda, String id) {\n        try {\n            for (Mascota m : agenda) {\n                if (m.getId().equalsIgnoreCase(id)) {\n                    return m.getNombre();   // el return NO se salta el finally\n                }\n            }\n            return \"(no esta en la agenda)\";\n        } finally {\n            System.out.println(\"  (finally) Busqueda de \" + id + \" terminada, con return y todo.\");\n        }\n    }\n\n    /** Lectura tolerante: el try externo protege el archivo, el interno protege cada linea. */\n    private static List<Mascota> cargar(String ruta) {\n        List<Mascota> lista = new ArrayList<>();\n        try (BufferedReader lector = new BufferedReader(new FileReader(ruta))) {   // BufferedReader es AutoCloseable\n            String linea;\n            while ((linea = lector.readLine()) != null) {\n                String[] campos = linea.split(\";\");\n                if (campos.length < 4) {\n                    System.out.println(\"  [OMITIDA] Linea incompleta: \" + linea);\n                    continue;\n                }\n                try {\n                    Mascota m = new Mascota(campos[0], campos[1]);\n                    m.setEdad(campos[2]);\n                    m.setPeso(campos[3]);\n                    lista.add(m);\n                } catch (DatoInvalidoException e) {\n                    System.out.println(\"  [OMITIDA] \" + e.getMessage());\n                }\n            }\n        } catch (FileNotFoundException e) {   // hija de IOException: por eso va primero\n            System.out.println(\"  [INFO] No existe \" + ruta + \". VetCare arranca con la lista vacia.\");\n        } catch (IOException e) {\n            System.out.println(\"  [ERROR] Fallo leyendo \" + ruta + \": \" + e.getMessage());\n        }\n        return lista;\n    }\n\n    private static void guardar(String ruta, List<Mascota> lista) {\n        File carpeta = new File(ruta).getParentFile();   // ruta relativa: sirve en cualquier maquina\n        if (carpeta != null && !carpeta.exists()) {\n            carpeta.mkdirs();\n        }\n        try (PrintWriter salida = new PrintWriter(ruta)) {\n            for (Mascota m : lista) {\n                salida.println(m.toLineaCsv());\n            }\n            System.out.println(\"  [OK] Guardadas \" + lista.size() + \" mascotas en \" + ruta);\n        } catch (FileNotFoundException e) {\n            System.out.println(\"  [ERROR] No pude guardar en \" + ruta + \": \" + e.getMessage());\n        }\n    }\n\n    /** ASI NO: ejemplo intencional de catch vacio, para verlo fallar en clase. */\n    private static void malaPractica(List<Mascota> agenda) {\n        int antes = agenda.size();\n        try {\n            Mascota m = new Mascota(\"M-999\", \"Fantasma\");\n            m.setEdad(\"tres\");\n            agenda.add(m);\n        } catch (DatoInvalidoException e) {\n            // MALA PRACTICA A PROPOSITO: catch vacio, nadie se entera de nada.\n        }\n        System.out.println(\"  Antes: \" + antes + \" | Ahora: \" + agenda.size() + \" -> la mascota nunca entro y nadie aviso.\");\n    }\n\n    public static void main(String[] args) {\n        System.out.println(\"=== VetCare | Clase 13: control de excepciones ===\");\n\n        List<Mascota> agenda = cargar(ARCHIVO);\n        System.out.println(\"Mascotas cargadas del archivo: \" + agenda.size());\n\n        System.out.println(\"\");\n        System.out.println(\"1) Entradas simuladas desde el formulario de registro:\");\n        registrar(agenda, \"M-001\", \"Firulais\", \"4\", \"28.5\");\n        registrar(agenda, \"M-002\", \"Michi\", \"tres\", \"3.2\");\n        registrar(agenda, \"M-003\", \"Rocky\", \"\", \"20\");\n        registrar(agenda, \"M-004\", \"Luna\", \"150\", \"8\");\n        registrar(agenda, \"M-005\", \"Pelusa\", \"2\", \"cuatro kilos\");\n\n        System.out.println(\"\");\n        System.out.println(\"2) finally se ejecuta aunque el try haga return:\");\n        System.out.println(\"  Mascota M-001 -> \" + buscarNombrePorId(agenda, \"M-001\"));\n\n        System.out.println(\"\");\n        System.out.println(\"3) Que pasa cuando el catch queda vacio:\");\n        malaPractica(agenda);\n\n        System.out.println(\"\");\n        System.out.println(\"4) Turno del usuario. Escriba edades (o 'fin' para salir):\");\n        Scanner teclado = new Scanner(System.in);\n        boolean seguir = true;\n        while (seguir) {\n            System.out.print(\"Edad de la mascota: \");\n            String entrada = teclado.nextLine();\n            if (\"fin\".equalsIgnoreCase(entrada.trim())) {\n                seguir = false;\n            } else {\n                try {\n                    Mascota prueba = new Mascota(\"M-TMP\", \"Prueba\");\n                    prueba.setEdad(entrada);\n                    System.out.println(\"  Edad aceptada. La aplicacion sigue viva.\");\n                } catch (DatoInvalidoException e) {\n                    System.out.println(\"  \" + e.getMessage() + \" Intente de nuevo.\");\n                }\n            }\n        }\n        teclado.close();\n\n        guardar(ARCHIVO, agenda);\n        System.out.println(\"=== Fin de la demo: VetCare nunca se cerro por un dato mal escrito. ===\");\n    }\n}\n",
        "codigo_archivo": "DemoExcepcionesVetCare.java"
    },
    {
        "n": 14,
        "slug": "Preparacion de la presentacion final",
        "titulo": "Preparacion de la presentacion final · Sustentacion de VetCare",
        "subtitulo": "Que mostrar, en que orden y como lograr que la demo no falle",
        "herramienta": "Apache NetBeans",
        "hito_pi": "VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.",
        "entregable": "Guion de sustentacion con bloques, minutos y evidencia que se muestra (mas el responsable nominal solo si el docente autorizo equipo), mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.",
        "demo": "El docente sustenta VetCare en 6 minutos delante del grupo, provoca a proposito un error de edad para mostrar la validacion, y luego repite la misma demo con la lista vacia para que se vea el desastre de no sembrar datos.",
        "teoria": [
            "Sustentar un proyecto de software no es exponer diapositivas: es demostrar, delante de un jurado que duda con razon, que un problema real quedo resuelto por un programa que corre. El jurado no compra promesas ni diagramas bonitos, compra evidencia; por eso la regla practica es que al menos la mitad del tiempo debe ser aplicacion corriendo en pantalla. El orden que funciona es siempre el mismo y va de lo humano a lo tecnico y de vuelta a lo humano: primero el problema de la clinica Huellitas en una frase concreta (todo en papel, se pierden expedientes, no se sabe quien tiene cita manana), luego la solucion en una frase (una aplicacion de escritorio en Java que registra duenos y mascotas, agenda citas y conserva los datos), despues la arquitectura en treinta segundos (las clases Dueno, Mascota y Cita y como se relacionan), enseguida la demo en vivo que es el corazon, y al cerrar los aprendizajes y las limitaciones. Empezar por el diagrama de clases o por la lista de tecnologias es el error mas comun: nadie sabe todavia para que sirve eso.",
            "La sustentacion es una coreografia y hay que repartirla como se reparte una obra de teatro, aunque suba una sola persona. La sustentacion es individual por defecto: el estudiante trocea su exposicion en bloques completos con inicio, final y evidencia en pantalla —no frases sueltas—, define en que momento suelta la diapositiva y toma el mouse, y deja listo un computador de respaldo con el proyecto ya abierto. Las transiciones entre bloques se dicen en voz alta, con una formula corta del tipo 'para mostrar como quedan guardados esos datos, abro de nuevo la aplicacion', porque los silencios incomodos al cambiar de tema son lo que mas se nota. Si el docente autorizo equipo de 2 o 3, cada integrante toma bloques completos, ninguno se queda callado aunque otro domine mas el codigo, y las transiciones se nombran ('sigue Julian'), porque el jurado pregunta quien hizo que y tiene derecho a preguntarle a cualquiera sobre cualquier parte. Un guion escrito, con minutos y evidencia por bloque (y el nombre del responsable si hay equipo), convierte una exposicion nerviosa en algo que se puede ensayar y medir; en VetCare ese guion tiene cinco bloques y suma siete minutos, con cuatro dedicados a la demo.",
            "La demo en vivo no falla por mala suerte, falla por falta de preparacion, y se blinda con un chequeo previo que llamaremos pre-vuelo. Lo primero es sembrar datos de demostracion: tres duenos, cuatro mascotas y tres citas ya cargadas en los CSV, porque una aplicacion con la lista vacia parece una aplicacion que no funciona, y ademas los datos deben ser creibles del dominio (Marta Lopez con Firulais, labrador de 4 anios) y nunca 'aaa' ni 'prueba1'. Lo segundo es tener ensayado el camino feliz exacto, es decir la secuencia de clics que se va a hacer, sin improvisar busquedas ni teclear rutas largas frente al publico. Lo tercero es la higiene de pantalla: aumentar el tamano de fuente del IDE, cerrar notificaciones y pestanas ajenas, dejar el proyecto ya compilado y, si es posible, ejecutar el .jar en lugar de compilar delante del jurado. Lo cuarto es el plan B: un video de dos o tres minutos de la ruta feliz y seis capturas de pantalla listas, para que si el computador falla la presentacion continue sin panico. Y hay un quinto detalle que suma puntos: provocar a proposito un error de edad para mostrar la validacion de la clase 13 como una fortaleza, no como un accidente.",
            "Las preguntas del jurado son casi siempre las mismas y se pueden preparar una por una. Donde esta la herencia y por que la usaron; por que ArrayList y no un arreglo fijo; que pasa si borro el archivo mascotas.csv; como controlan que alguien escriba texto donde va la edad; quien programo cada parte; que harian distinto si empezaran de nuevo. La forma de responder tiene tres reglas: responda con la aplicacion o el codigo en pantalla, porque mostrar vale mas que explicar; no se demore mas de treinta o cuarenta segundos por respuesta; y si no sabe, digalo con dignidad y proponga como lo averiguaria, que eso el jurado lo respeta mucho mas que un invento. Tambien conviene tener a la mano el archivo de cada respuesta ya abierto en una pestana del IDE (Dueno.java para la herencia, Mascota.java para las validaciones, la clase de persistencia para el CSV), de modo que la respuesta sea abrir una pestana y no buscar en vivo.",
            "El manejo del tiempo y del nervio se entrena, no se improvisa. Un ensayo cronometrado revela cosas que el papel no muestra: que la introduccion se come tres minutos, que la demo se atasca en un formulario, que el cierre queda cortado. Por eso hoy ensayamos con reloj y anotamos el tiempo real de cada bloque frente al planeado, y se repite hasta que el total caiga entre cinco y ocho minutos con margen. Hay cosas que restan puntos siempre: leer las diapositivas de espaldas al jurado, pedir disculpas por el proyecto antes de mostrarlo, culpar al computador, hablar de lo que 'iban a hacer' en vez de mostrar lo que hicieron, y pasarse del tiempo, porque eso obliga al jurado a cortar justo en la parte que mas les costo. Al reves, suman: hablar mirando al jurado, usar el vocabulario del dominio (dueno, mascota, cita, historia clinica) y reconocer con naturalidad las limitaciones conocidas.",
            "Error tipico del docente que no domina el tema: dejar la sustentacion para el ultimo dia, decir 'preparen una exposicion' y confiar en que el guion se arma solo. Eso produce demos improvisadas con la aplicacion vacia y proyectos que se ponen a compilar en vivo mientras el jurado espera. Otras variantes: no cronometrar nunca, permitir que el estudiante muestre codigo linea por linea en lugar de la aplicacion corriendo, y no exigir plan B, para despues perder media hora del examen porque el computador de alguien no encendio. Cuando el docente autoriza equipos aparece un problema extra: si nadie exige reparto escrito, tres personas se quedan mudas y la nota la sostiene un solo orador. La clase de hoy no tiene tema tecnico nuevo, pero tiene un producto verificable, y ese es el punto: si al final del bloque cada estudiante no tiene guion escrito, datos sembrados y dos ensayos cronometrados, la clase no se cumplio."
        ],
        "taller": [
            "Paso 1. Escriban el guion de la sustentacion en una tabla de cinco bloques con tres columnas: bloque, minutos planeados y evidencia exacta que se muestra en pantalla (si el docente autorizo equipo, agreguen una cuarta columna con el responsable); el total debe sumar entre 5 y 7 minutos, dejando margen, y la demo en vivo debe ocupar por lo menos la mitad.",
            "Paso 2. Ejecuten el sembrador de datos de demostracion para dejar datos_demo con duenos.csv, mascotas.csv y citas.csv, y corran el chequeo pre-vuelo hasta que las tres lineas salgan en [OK] con filas mayores que cero.",
            "Paso 3. Hagan el ensayo numero uno con el cronometro del programa: hablen cada bloque completo de pie y sin saltarse ninguno (si trabajan en equipo, cada integrante el suyo), y al final anoten tiempo real contra tiempo planeado de cada bloque en la planilla.",
            "Paso 4. Graben el plan B: un video de dos a tres minutos con la ruta feliz completa (registrar dueno, registrar mascota, agendar cita, buscar por ID, cerrar y volver a abrir mostrando que los datos siguen ahi) y exporten seis capturas de pantalla de esos mismos momentos.",
            "Paso 5. Intercambien con otro compañero (o con otro equipo, si el docente lo autorizo) una ronda de cinco preguntas de jurado, ajusten el guion con lo que fallo, hagan el ensayo numero dos y suban a ExamLab el guion, la planilla de tiempos de los dos ensayos y el video de respaldo."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ la nota del Proyecto Integrador no se define solo por el codigo sino por lo que el jurado alcance a ver en 5 a 8 minutos, y una demo que falla borra tres meses de trabajo bien hecho.",
            "VetCare ya cumple los requisitos tecnicos (POO, colecciones, interfaz grafica, manejo de errores y persistencia); hoy lo que se construye es la evidencia de que todo eso funciona junto y en vivo.",
            "El guion, los datos sembrados y el video de respaldo son artefactos reales del oficio: en la industria a esto se le llama preparar el demo day, y se hace exactamente igual."
        ],
        "escenario": [
            "Cada estudiante llega con su VetCare compilando y corriendo, con las funciones de registrar dueno y mascota, agendar cita, buscar por ID y guardar en archivo ya terminadas.",
            "La carpeta datos del proyecto puede estar vacia o con basura de las pruebas de la clase pasada; el chequeo pre-vuelo debe detectarlo antes del primer ensayo.",
            "El salon tiene videobeam y un solo cable: cada proyecto dispone de 8 minutos de reloj y una unica oportunidad de conectar, igual que el dia de la sustentacion."
        ],
        "criterios": [
            "El guion escrito cubre los cinco bloques con minutos y evidencia, sin bloques huerfanos; si el docente autorizo equipo, todos los integrantes tienen bloque y ninguno queda sin intervencion.",
            "El chequeo pre-vuelo devuelve [OK] en los tres archivos de datos_demo y la aplicacion arranca mostrando informacion, nunca una lista vacia.",
            "Los dos ensayos quedan cronometrados y el segundo cae entre 5 y 8 minutos, con la demo en vivo ocupando al menos la mitad del tiempo.",
            "Existe plan B verificado: video de la ruta feliz reproducible sin internet y seis capturas exportadas en la carpeta del proyecto."
        ],
        "pistas": [
            "Si el computador no enciende cinco minutos antes de sustentar, ¿que muestra en su lugar y donde lo tiene a la mano?",
            "¿Cual es la primera pantalla que ve el jurado y que informacion tiene: hay datos, o una tabla vacia que parece un programa que no sirve?",
            "Si el jurado pregunta 'donde esta la herencia en su proyecto', ¿en cuantos segundos puede tener ese archivo en pantalla?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. El guion que funciona queda asi, y es el mismo si sustenta una sola persona o un equipo autorizado: bloque 1, problema y solucion, 1 minuto, evidencia la diapositiva unica del dolor de Huellitas; bloque 2, arquitectura (clases Dueno, Mascota y Cita, herencia y colecciones), 1 minuto, evidencia Persona.java al lado de Dueno.java; bloque 3, demo de registro de dueno y mascota con la validacion de edad de la clase 13, 2 minutos, evidencia la aplicacion corriendo; bloque 4, demo de agendar cita, buscar por ID y persistencia en CSV, 2 minutos, evidencia cerrar y reabrir la aplicacion; bloque 5, limitaciones, aprendizajes y cierre, 1 minuto. Los puntos del guion se ganan por tener los cinco bloques con minutos y evidencia, no por cuantas personas hablan; si el docente autorizo equipo, se agrega la columna de responsable y ningun integrante queda sin bloque. Total planeado 7 minutos dentro de una ventana de 8: la demo se lleva 4, es decir mas de la mitad, que es exactamente lo que buscamos, y quedan 60 segundos de colchon para las preguntas o los tropiezos.",
            "Paso 2 resuelto. Ejecuten la opcion 1 del programa (sembrar datos) y despues la opcion 2 (pre-vuelo); la salida correcta muestra [OK] datos_demo/duenos.csv -> 3 filas, [OK] datos_demo/mascotas.csv -> 4 filas y [OK] datos_demo/citas.csv -> 3 filas. Si alguna linea sale [FALLA] con 0 filas, no se ensaya todavia: casi siempre es que el programa se esta ejecutando desde otra carpeta, porque la ruta datos_demo es relativa a la carpeta desde donde arranca el proyecto, o que la carpeta no se pudo crear por permisos. Los datos deben ser creibles y del dominio (Marta Lopez con Firulais, un labrador de 4 anios, y una cita de vacunacion a las 08:00) porque nombres como 'aaa' o 'prueba1' le dicen al jurado que el sistema nunca se uso de verdad.",
            "Paso 3 resuelto. En el ensayo uno lo normal es que el bloque 1 se pase a 2 minutos y que la demo se atrase buscando ventanas. La correccion no es hablar mas rapido: es recortar la teoria y dejar la demo intacta. Una frase que resuelve el bloque 1 completo, y que se aprende de memoria, es esta: 'La clinica Huellitas lleva todo en papel, pierde expedientes y no sabe quien tiene cita manana; VetCare es una aplicacion de escritorio en Java que registra duenos y mascotas, agenda citas y conserva los datos aunque se cierre el programa.' Con eso ya se puede pasar a la arquitectura. La planilla queda con cuatro columnas: bloque, planeado, real y ajuste que se hara para el segundo ensayo.",
            "Paso 4 resuelto. El plan B se graba con el grabador de pantalla del sistema (Xbox Game Bar con la tecla Windows mas G, o cualquier grabador instalado), en la resolucion de la pantalla del salon y sin audio de fondo. El video debe mostrar la ruta feliz completa: registrar un dueno, registrar su mascota, provocar el error de edad y ver el aviso, agendar una cita, buscar por ID y, al final, cerrar y volver a abrir la aplicacion para que se vea que los datos siguen ahi, porque ese es el momento que demuestra la persistencia. Se guarda dentro de la carpeta del proyecto y ademas en una memoria USB: si el video vive solo en una nube y el salon no tiene internet, no es plan B.",
            "Paso 5 resuelto. Las respuestas modelo a las tres preguntas mas frecuentes, cada una de menos de 40 segundos: sobre la herencia, se abre Persona.java al lado de Dueno.java, se senala la palabra extends y el metodo sobrescrito con @Override, y se explica que nombre, documento y telefono se escribieron una sola vez; sobre por que ArrayList y no un arreglo, se responde que el numero de mascotas de la clinica cambia todos los dias y un arreglo obliga a fijar el tamano de antemano, mientras que la lista crece con add y se recorre igual; sobre que pasa si borran el CSV, se borra el archivo en vivo, se reinicia la aplicacion y se muestra que arranca con la lista vacia y el aviso de primera ejecucion, sin caerse, gracias al catch de FileNotFoundException de la clase 13. Esa ultima respuesta se ensaya antes, porque hacerla en vivo sin haberla probado es una apuesta."
        ],
        "solucion_rubrica": [
            "Guion escrito con cinco bloques, responsable y minutos, con la demo ocupando la mitad o mas (3)",
            "Datos de demostracion sembrados y chequeo pre-vuelo en [OK] antes del ensayo (2)",
            "Dos ensayos cronometrados con planilla de tiempo real contra planeado, el segundo entre 5 y 8 minutos (3)",
            "Plan B completo y verificado: video de la ruta feliz mas seis capturas, disponibles sin internet (2)"
        ],
        "solucion_errores": [
            "Sustentar con la aplicacion vacia: el jurado ve tablas en blanco y concluye que el sistema no guarda nada, aunque el codigo de persistencia este perfecto.",
            "Compilar o buscar el proyecto en vivo delante del jurado: se pierden dos de los ocho minutos y cualquier error de compilacion se lleva por delante toda la presentacion.",
            "Repartir la exposicion en frases sueltas en vez de bloques completos con evidencia: el jurado pregunta por cualquier parte del proyecto. Y si el docente autorizo equipo, dejar que hable solo el que mas sabe: los integrantes mudos arrastran la nota de todos."
        ],
        "codigo_slide_titulo": "Chequeo pre-vuelo: la demo que no falla",
        "codigo_slide_lineas": [
            "private static boolean chequeoPreVuelo() {          // se ejecuta 10 minutos antes de sustentar",
            "    String[] requeridos = {\"datos_demo/duenos.csv\", \"datos_demo/mascotas.csv\", \"datos_demo/citas.csv\"};",
            "    boolean listo = true;",
            "    for (String ruta : requeridos) {",
            "        int filas = contarFilas(ruta);              // 0 filas = pantalla vacia frente al jurado",
            "        System.out.println((filas > 0 ? \"[OK]    \" : \"[FALLA] \") + ruta + \" -> \" + filas + \" filas\");",
            "        if (filas == 0) {",
            "            listo = false;",
            "        }",
            "    }",
            "    return listo;   // si devuelve false, todavia no se sustenta ni se ensaya",
            "}"
        ],
        "codigo_slide_caption": "Una demo se prepara con codigo, no con fe: si el pre-vuelo no da verde, la sustentacion no arranca.",
        "quiz": [
            {
                "tipo": "om",
                "q": "En una sustentacion de 5 a 8 minutos, ¿cuanto tiempo deberia ocupar la aplicacion corriendo en pantalla?",
                "opciones": [
                    "A) Menos del 10 por ciento",
                    "B) Alrededor del 20 por ciento",
                    "C) Al menos la mitad del tiempo",
                    "D) Todo el tiempo, sin explicar el problema ni la arquitectura"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "¿Con que bloque debe abrir la sustentacion de VetCare?",
                "opciones": [
                    "A) Con el diagrama de clases",
                    "B) Con el problema de la clinica Huellitas y a quien le duele",
                    "C) Con la lista de tecnologias usadas",
                    "D) Con el codigo fuente de la clase principal"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Compilar el proyecto delante del jurado demuestra dominio tecnico y por eso se recomienda.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Durante la demo, la tabla de mascotas aparece vacia. ¿Que debio hacerse antes para evitarlo?",
                "opciones": [
                    "A) Cerrar y volver a abrir la aplicacion",
                    "B) Pedir disculpas y continuar con diapositivas",
                    "C) Sembrar el juego de datos de demostracion y correr el chequeo pre-vuelo",
                    "D) Registrar cinco mascotas en vivo mientras el jurado espera"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Si el docente autoriza trabajo en equipo, todos los integrantes deben intervenir en la sustentacion, aunque uno domine mas el codigo que los demas.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Un video grabado de la ruta feliz, guardado en el equipo y en una memoria USB, sirve como plan B cuando el computador o el videobeam fallan.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "El jurado pregunta: '¿donde esta la herencia en su proyecto?'. Describa como responderia en menos de 40 segundos.",
                "clave": "Abriendo en pantalla la clase padre (Persona) y la hija (Dueno) para mostrar la palabra extends, senalando que atributos comunes como nombre, documento y telefono se escribieron una sola vez y se reutilizan, y mostrando un metodo sobrescrito con @Override. Responder con el codigo ya abierto en una pestana, corto y sin rodeos, y luego devolver el control a la demo."
            },
            {
                "tipo": "abierta",
                "q": "Mencione tres elementos del chequeo pre-vuelo que se hacen antes de conectar el videobeam.",
                "clave": "Verificar que los archivos de datos de demostracion existan y tengan filas (duenos, mascotas y citas); tener el proyecto ya compilado o el .jar listo para ejecutar sin compilar; aumentar el tamano de fuente del IDE y cerrar notificaciones y pestanas ajenas; y tener el plan B (video y capturas) accesible sin internet."
            }
        ],
        "codigo_fuente": "import java.io.BufferedReader;\nimport java.io.File;\nimport java.io.FileNotFoundException;\nimport java.io.FileReader;\nimport java.io.IOException;\nimport java.io.PrintWriter;\nimport java.util.Scanner;\n\n/**\n * VetCare - Clinica Veterinaria Huellitas\n * Clase 14: preparacion de la sustentacion final.\n * 1) Siembra el juego de datos de demostracion.\n * 2) Chequeo pre-vuelo antes de conectar el videobeam.\n * 3) Ensayo cronometrado de 5 a 8 minutos.\n * Trabajo individual por defecto: si el docente autoriza equipo, agregue los nombres\n * en PRESENTADORES y el reparto de bloques se hace automatico.\n * Ejecutar en Apache NetBeans: clic derecho sobre el archivo y luego Run File.\n */\npublic class EnsayoSustentacionVetCare {\n\n    private static final String CARPETA = \"datos_demo\";\n\n    // Modalidad de trabajo: INDIVIDUAL por defecto. Si el docente autoriza equipo de 2 o 3,\n    // escriba los nombres aqui y el reparto de bloques se calcula solo.\n    // Individual: {\"Usted\"}   |   Equipo: {\"Marta\", \"Julian\", \"Sara\"}\n    private static final String[] PRESENTADORES = {\"Usted\"};\n\n    // Guion: bloque, evidencia que se muestra en pantalla y minutos planeados.\n    // Total 7 minutos, con la demo ocupando 4. El guion no cambia por el numero de expositores.\n    private static final String[][] GUION = {\n        {\"Problema de la clinica Huellitas y solucion propuesta\", \"Diapositiva con los 3 dolores\", \"1\"},\n        {\"Arquitectura: clases, herencia y colecciones\", \"Persona.java al lado de Dueno.java\", \"1\"},\n        {\"DEMO: registrar dueno y mascota (con validacion de edad)\", \"La aplicacion corriendo\", \"2\"},\n        {\"DEMO: agendar cita, buscar por ID y guardar en CSV\", \"Cerrar y reabrir con los datos ahi\", \"2\"},\n        {\"Limitaciones, aprendizajes y cierre\", \"Lista de 3 limitaciones\", \"1\"}\n    };\n\n    /** Quien habla el bloque i. Con un solo presentador, todos los bloques son suyos. */\n    private static String responsableDe(int i) {\n        if (PRESENTADORES.length == 0) {\n            return \"Usted\";\n        }\n        return PRESENTADORES[i % PRESENTADORES.length];\n    }\n\n    public static void main(String[] args) {\n        Scanner teclado = new Scanner(System.in);\n        boolean seguir = true;\n        while (seguir) {\n            System.out.println(\"\");\n            System.out.println(\"=== VetCare | Preparacion de la sustentacion ===\");\n            System.out.println(\"1. Sembrar datos de demostracion\");\n            System.out.println(\"2. Chequeo pre-vuelo\");\n            System.out.println(\"3. Ensayo cronometrado\");\n            System.out.println(\"4. Salir\");\n            System.out.print(\"Opcion: \");\n            String opcion = teclado.nextLine().trim();\n            switch (opcion) {\n                case \"1\":\n                    sembrarDatosDemo();\n                    break;\n                case \"2\":\n                    chequeoPreVuelo();\n                    break;\n                case \"3\":\n                    if (chequeoPreVuelo()) {\n                        ensayo(teclado);\n                    } else {\n                        System.out.println(\"Primero siembre los datos: nadie ensaya con la aplicacion vacia.\");\n                    }\n                    break;\n                case \"4\":\n                    seguir = false;\n                    break;\n                default:\n                    System.out.println(\"Opcion no valida.\");\n            }\n        }\n        teclado.close();\n        System.out.println(\"Recuerde: dos ensayos cronometrados antes de sustentar.\");\n    }\n\n    /** Datos creibles del dominio veterinario: nombres reales, no 'prueba1' ni 'aaa'. */\n    private static void sembrarDatosDemo() {\n        File carpeta = new File(CARPETA);\n        if (!carpeta.exists()) {\n            carpeta.mkdirs();\n        }\n        escribir(CARPETA + \"/duenos.csv\", new String[]{\n            \"D-001;Marta Lopez;3155551212;Calle 5 #23-41\",\n            \"D-002;Julian Perez;3009998877;Carrera 8 #12-30\",\n            \"D-003;Sara Quintero;3126665544;Avenida 4N #10-15\"\n        });\n        escribir(CARPETA + \"/mascotas.csv\", new String[]{\n            \"M-001;Firulais;Canino;Labrador;4;28.5;D-001\",\n            \"M-002;Michi;Felino;Criollo;2;3.8;D-001\",\n            \"M-003;Rocky;Canino;Pastor;6;32.0;D-002\",\n            \"M-004;Luna;Felino;Siames;1;2.9;D-003\"\n        });\n        escribir(CARPETA + \"/citas.csv\", new String[]{\n            \"C-001;M-001;08:00;Vacunacion anual;Programada\",\n            \"C-002;M-003;09:30;Control de peso;Programada\",\n            \"C-003;M-004;11:00;Desparasitacion;Atendida\"\n        });\n        System.out.println(\"Datos de demostracion listos en la carpeta \" + CARPETA);\n    }\n\n    private static void escribir(String ruta, String[] lineas) {\n        try (PrintWriter salida = new PrintWriter(ruta)) {\n            for (String linea : lineas) {\n                salida.println(linea);\n            }\n            System.out.println(\"  [OK] \" + ruta + \" (\" + lineas.length + \" registros)\");\n        } catch (FileNotFoundException e) {\n            System.out.println(\"  [ERROR] No pude crear \" + ruta + \": \" + e.getMessage());\n        }\n    }\n\n    /** Si esto no da verde, no se conecta el videobeam. */\n    private static boolean chequeoPreVuelo() {\n        String[] requeridos = {CARPETA + \"/duenos.csv\", CARPETA + \"/mascotas.csv\", CARPETA + \"/citas.csv\"};\n        boolean listo = true;\n        System.out.println(\"--- Chequeo pre-vuelo ---\");\n        for (String ruta : requeridos) {\n            int filas = contarFilas(ruta);\n            System.out.println((filas > 0 ? \"  [OK]    \" : \"  [FALLA] \") + ruta + \" -> \" + filas + \" filas\");\n            if (filas == 0) {\n                listo = false;\n            }\n        }\n        System.out.println(listo ? \"  Listos para la demo en vivo.\" : \"  Siembre los datos con la opcion 1 antes de continuar.\");\n        return listo;\n    }\n\n    private static int contarFilas(String ruta) {\n        int filas = 0;\n        try (BufferedReader lector = new BufferedReader(new FileReader(ruta))) {\n            while (lector.readLine() != null) {\n                filas++;\n            }\n        } catch (IOException e) {\n            // El archivo no existe o no se puede leer: para la demo es lo mismo que estar vacio.\n            return 0;\n        }\n        return filas;\n    }\n\n    /** Cronometro real: se avanza con Enter al terminar cada bloque. */\n    private static void ensayo(Scanner teclado) {\n        System.out.println(\"--- Ensayo cronometrado. Presione Enter al terminar cada bloque ---\");\n        long inicio = System.currentTimeMillis();\n        long anterior = inicio;\n        for (int i = 0; i < GUION.length; i++) {\n            String[] bloque = GUION[i];\n            System.out.println(\"\");\n            System.out.println(\"-> \" + bloque[0]);\n            System.out.println(\"   Evidencia: \" + bloque[1]);\n            System.out.println(\"   Habla: \" + responsableDe(i) + \" | Planeado: \" + bloque[2] + \" min\");\n            teclado.nextLine();\n            long ahora = System.currentTimeMillis();\n            double real = (ahora - anterior) / 60000.0;\n            double plan = Double.parseDouble(bloque[2]);\n            String veredicto = real > plan ? \"SE PASO\" : \"en tiempo\";\n            System.out.println(String.format(\"   Real: %.2f min | Planeado: %.0f min | %s\", real, plan, veredicto));\n            anterior = ahora;\n        }\n        double total = (System.currentTimeMillis() - inicio) / 60000.0;\n        System.out.println(String.format(\"TOTAL: %.2f min\", total));\n        if (total < 5) {\n            System.out.println(\"Muy corto: falto profundidad en la demo. Meta: entre 5 y 8 minutos.\");\n        } else if (total > 8) {\n            System.out.println(\"Se paso: recorte la parte teorica, nunca la demo.\");\n        } else {\n            System.out.println(\"Tiempo dentro de la ventana. Repita el ensayo una vez mas.\");\n        }\n    }\n}\n",
        "codigo_archivo": "EnsayoSustentacionVetCare.java"
    },
    {
        "n": 15,
        "slug": "Parcial 3",
        "titulo": "Parcial 3",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    }
]
