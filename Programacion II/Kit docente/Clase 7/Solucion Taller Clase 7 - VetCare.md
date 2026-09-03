# Solucion Taller · Clase 7 · Patrones de diseno · Singleton y Factory

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Blinde la creacion. En RepositorioVetCare escriba el atributo 'private static RepositorioVetCare instancia;' y cambie el constructor a 'private RepositorioVetCare() { System.out.println("[Repositorio] Se creo la UNICA instancia de datos."); }'. Apenas guarde, VS Code le marcara en rojo todos los lugares donde alguien hacia new RepositorioVetCare(): eso no es un problema, es el patron trabajando a su favor, porque le muestra exactamente que codigo hay que corregir. El println no es decoracion: es la evidencia visible de cuantas veces se construyo el objeto.
2. Abra la unica puerta. Agregue 'public static synchronized RepositorioVetCare getInstancia() { if (instancia == null) { instancia = new RepositorioVetCare(); } return instancia; }'. Es estatico porque hay que poder llamarlo sin tener aun un objeto (RepositorioVetCare.getInstancia()); el if hace la creacion perezosa, es decir que el objeto solo nace la primera vez que alguien lo pide; y synchronized evita que dos hilos entren simultaneamente al if y terminen creando dos instancias. Compruebe con dos llamadas seguidas y un System.out.println(a == b): imprime true y el mensaje del constructor sale una sola vez.
3. Reemplace en las ventanas. Donde decia 'RepositorioVetCare repo = new RepositorioVetCare();' ahora va 'RepositorioVetCare repo = RepositorioVetCare.getInstancia();'. Para dejar la evidencia, en el metodo refrescar() de cada ventana imprima o pinte System.identityHashCode(RepositorioVetCare.getInstancia()): las dos ventanas deben mostrar el mismo numero. Ese numero es la prueba visible de que ya no hay dos archivadores, sino uno, y es lo que hace que M-002 Michi, registrada en Recepcion, aparezca al refrescar en Consultorio.
4. Centralice la creacion de consultas. FabricaConsultas queda con constructor privado (es una clase de utilidad, nadie debe instanciarla) y un unico metodo estatico crear(String tipo, String idMascota). Adentro: valida que el idMascota no venga vacio, normaliza el texto con tipo.trim().toUpperCase() para que 'vacunacion', 'Vacunacion' y ' VACUNACION ' sean lo mismo, compara esa clave con los tres tipos validos (un switch sobre String o la cadena if/else del demo) devolviendo new ConsultaVacunacion, new ConsultaControl o new ConsultaUrgencia, y en cualquier otro caso lanza IllegalArgumentException con el mensaje 'Tipo de consulta no soportado: ...'. La ventana declara la variable como Consulta, no como ConsultaUrgencia, y llama consulta.duracionMinutos() y consulta.tarifaBase() sin saber cual subclase le tocó: asi el dia que agreguen CIRUGIA solo se toca la fabrica.
5. Justifique por escrito, que es la parte que se evalua. El repositorio es Singleton porque representa un recurso unico y compartido (el archivador de la clinica) y porque su estado debe ser el mismo para todas las ventanas: si hubiera dos, la agenda agendaria citas a mascotas que no existen. Mascota no puede serlo porque el dominio tiene muchas mascotas: un Singleton de Mascota significaria que Huellitas atiende un solo animal. Y anote el costo con nombre propio: en la clase 8, cuando escribamos pruebas, el Singleton va a llegar con los datos de la prueba anterior y las pruebas empezaran a depender del orden; por eso le dejamos el metodo limpiar(), que cada prueba llamara antes de empezar.

## Rubrica corta
- [ ] Singleton correcto: atributo estatico privado, constructor privado y getInstancia (3)
- [ ] Ninguna ventana crea el repositorio con new y ambas comparten datos (2)
- [ ] FabricaConsultas con tres tipos, retorno del tipo base y validacion del tipo desconocido (3)
- [ ] Justificacion escrita del uso del patron y de su costo (2)

## Errores frecuentes
- Dejar el constructor publico o declarar el atributo como public static, con lo cual cualquiera puede crear o reemplazar la 'unica' instancia y el patron queda de adorno.
- Creer que el Singleton guarda los datos entre ejecuciones y reclamar que 'se borraron las mascotas' al cerrar la aplicacion.
- Aplicar Singleton a Mascota, Cita o Dueno, o crear una fabrica que solo hace un new de una sola clase sin ninguna regla ni validacion.

Codigo de apoyo: `Kit docente/Clase 7/Codigo/VetCarePatronesDemo.java`