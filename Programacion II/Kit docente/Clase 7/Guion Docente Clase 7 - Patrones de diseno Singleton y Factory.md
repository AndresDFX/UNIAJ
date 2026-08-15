# Guion docente · Clase 7 · Patrones de diseno · Singleton y Factory

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con un unico repositorio de datos en memoria compartido por todas las ventanas y una fabrica que crea las consultas del dominio.
- **Entregable de hoy:** Clase RepositorioVetCare convertida en Singleton, FabricaConsultas con tres tipos y evidencia de que dos ventanas ven la misma lista, subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 7 - Patrones de diseno Singleton y Factory/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un patron de diseño no es una libreria que se importa ni un archivo que se descarga: es una solucion probada, con nombre propio, a un problema de diseño que se repite. La analogia que mejor funciona es la de arquitectura: cuando un arquitecto dice 'aqui va un patio interior', nadie le pide los planos del patio, porque el nombre ya comunica el problema (ventilar e iluminar el centro de la casa) y la forma de resolverlo. En programacion pasa igual: cuando un desarrollador dice 'el repositorio de VetCare es un Singleton', su compañero entiende de una que hay una sola instancia y un punto de acceso global, sin necesidad de leer el codigo. El catalogo clasico es el de la Banda de los Cuatro (GoF) y agrupa los patrones en creacionales (como se crean los objetos: Singleton, Factory, Builder), estructurales (como se componen: Adapter, Decorator, Facade) y de comportamiento (como se comunican: Observer, Strategy). Nosotros vamos a usar solo dos hoy, pero bien usados y con criterio, no por coleccionarlos.

El problema que motiva el Singleton ya lo vivimos en la clase pasada, aunque no le pusimos nombre. En VetCare la ventana de registro creaba su propio RepositorioMascotas. Cuando abramos la ventana de citas y esta haga otro new RepositorioMascotas(), la agenda no vera ni una sola de las mascotas registradas, porque son dos ArrayList distintos en dos zonas distintas de memoria. Y no sirve pasar datos por copia: la clinica Huellitas necesita que exista un solo lugar donde vivan los expedientes mientras la aplicacion corre, igual que en la clinica fisica hay un solo archivador y no uno por escritorio. El problema entonces se enuncia asi: necesito garantizar que exista una y solo una instancia de esta clase y que cualquier parte del programa pueda llegar a ella sin andar pasandosela de constructor en constructor. Esa es exactamente la intencion del patron Singleton.

El mecanismo en Java tiene tres piezas y las tres son obligatorias. Primera, un atributo privado y estatico del mismo tipo de la clase (private static RepositorioVetCare instancia): estatico porque debe pertenecer a la clase y no a un objeto, privado para que nadie lo reemplace desde afuera. Segunda, el constructor declarado private: mientras exista un constructor publico, cualquiera puede hacer new y el patron se rompe; al hacerlo privado el compilador se vuelve su aliado y marca en rojo cada intento. Tercera, un metodo publico y estatico getInstancia() que revisa si el atributo es null, lo crea la primera vez y de ahi en adelante devuelve siempre el mismo objeto; a eso se le llama inicializacion perezosa (lazy). Si el programa fuera multihilo, dos hilos podrian entrar al mismo tiempo al if y crear dos instancias; por eso se marca synchronized, o se usa la version temprana (private static final RepositorioVetCare INSTANCIA = new RepositorioVetCare();) que Java garantiza unica. Para verificarlo en pantalla no hay que creer en la fe: se imprime System.identityHashCode(a) y System.identityHashCode(b) desde las dos ventanas y se comprueba que el numero es el mismo.

El segundo patron responde a otro problema distinto: quien decide como se construye un objeto. En VetCare hay tres tipos de consulta con reglas propias: Vacunacion dura 15 minutos y cuesta 35.000, Control dura 30 minutos y cuesta 60.000, Urgencia dura 45 minutos y cuesta 120.000. Si la ventana de agendamiento hace directamente el new de cada subclase, esos numeros y esas decisiones quedan regados por toda la interfaz, y el dia que la clinica suba la tarifa hay que ir a buscarlos en cinco ventanas. Una Factory concentra esa decision en un solo lugar: FabricaConsultas.crear("URGENCIA", "M-001") devuelve un objeto de tipo Consulta y la ventana ni se entera de que subclase le entregaron; ademas la fabrica normaliza el texto que llega del JComboBox y lanza IllegalArgumentException si el tipo no existe, con lo cual un dato basura nunca se convierte en objeto. Fijese en el detalle importante: el metodo retorna el tipo base (Consulta), no la subclase; ahi es donde el polimorfismo que vimos en clases anteriores empieza a pagar, porque el dia que Huellitas agregue 'CIRUGIA' solo se toca la fabrica.

Ahora la parte que casi nadie enseña: cuando NO usarlos. El Singleton es, sin maquillaje, una variable global con corbata. Trae tres costos reales: esconde dependencias (una clase que por dentro llama a getInstancia() no declara en su firma que necesita el repositorio), complica las pruebas (en la clase 8 vamos a querer un repositorio limpio en cada caso de prueba y el Singleton nos va a devolver el sucio de la prueba anterior) y concentra estado compartido que en aplicaciones grandes se vuelve impredecible. La alternativa profesional se llama inyeccion por constructor: pasar el repositorio como parametro, tal como hicimos con ControladorRegistro en la clase 6. En VetCare aceptamos el Singleton para el repositorio porque es una aplicacion de escritorio pequeña, con un solo usuario y una unica fuente de datos, y aun asi vamos a dejarle un metodo limpiar() para poder probarlo. La Factory tiene su propio abuso: si solo hay una clase que crear y ninguna regla que aplicar, una fabrica que hace un new pelado no aporta nada, solo una capa mas de ruido. La regla de oro es: primero el problema, despues el patron; nunca al reves.

Error tipico del docente que no domina el tema: enseñar el Singleton como 'la forma correcta de compartir variables entre ventanas' y terminar poniendo el atributo publico y estatico (public static RepositorioVetCare instancia), con lo cual cualquiera puede reasignarlo desde afuera y ya no hay ninguna garantia; o dejar el constructor publico 'porque NetBeans lo pide', que es exactamente lo unico que no se puede hacer. El segundo error clasico es creer que el Singleton persiste datos: los estudiantes cierran la aplicacion, la vuelven a abrir y preguntan donde quedaron las mascotas, y hay que explicar que el Singleton solo garantiza una instancia mientras el programa corre, que la persistencia en archivos es otro tema que veremos mas adelante. El tercero es la patronitis: llenar el proyecto de fabricas que solo devuelven new de una sola clase y de Singletons para cosas que deberian ser objetos comunes, como Mascota o Cita, que por definicion son muchos. Si al preguntar 'que problema resuelve este patron aqui' la respuesta es 'que lo vimos en clase', el patron esta sobrando.

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
