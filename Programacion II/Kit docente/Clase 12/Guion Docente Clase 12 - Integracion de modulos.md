# Guion docente · Clase 12 · Integración de módulos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.
- **Entregable de hoy:** El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 12 - Integracion de modulos/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Integrar es lograr que piezas que ya funcionan por separado funcionen juntas dentro de un único ejecutable, y esa palabra 'juntas' esconde casi todo el trabajo. VetCare tiene cuatro piezas y conviene ponerles nombre de paquete para verlas: vetcare.modelo con Mascota (y Dueno, si el equipo lo separó), vetcare.datos con RepositorioMascotasCSV, vetcare.logica con ServicioVetCare que administra el ArrayList y aplica las reglas, y vetcare.ui con la ventana Swing. Entre ellas rige una regla de dependencia que hay que respetar como si fuera ley: la interfaz conoce al servicio, el servicio conoce al repositorio, el repositorio conoce al modelo, y nadie mira hacia arriba; en particular el servicio no puede llamar a un JOptionPane. ¿Por qué importa? Porque así se puede probar la lógica sin abrir la ventana, porque el día que se cambie el .csv por una base de datos solo se toca una clase, y porque cuando algo falle se sabe en qué capa buscar. Integrar bien no es que compile: es que exista un único punto de entrada, un único servicio y un único archivo de datos, y que cada capa haga su oficio y nada más.

El flujo de punta a punta se define antes de integrar, por escrito, y se llama guion de humo porque su único fin es ver si sale humo. Para VetCare son cinco pasos: abrir la aplicación y ver la tabla poblada con lo que había en mascotas.csv; registrar una mascota nueva con dueño y ver que aparece de inmediato en la tabla; buscar por ID y ver el expediente; cerrar la ventana y confirmar que avisó cuántos registros guardó; volver a abrir y encontrar la mascota nueva. Eso es lo que tiene que correr sin que nadie toque código en la mitad. El ciclo de vida que lo soporta es igual de explícito y su orden no es negociable: el main construye el repositorio, construye el servicio pasándole el repositorio, pide cargar los datos y solo entonces manda a construir y mostrar la ventana; al cerrar, el manejador de la ventana pide guardar y solo si el guardado salió bien libera la aplicación. Si se invierte el orden y la ventana se construye antes de cargar, la tabla nace vacía aunque el archivo tenga cien mascotas, y el estudiante va a jurar que la persistencia no funciona cuando lo que está mal es la secuencia de arranque.

Los errores de integración tienen firma propia y conviene reconocerlos por el síntoma. Primero, el más costoso: dos instancias del mismo servicio, una creada en el main y otra creada dentro del constructor de la ventana; se registra en la instancia de la ventana y al cerrar se guarda la del main, así que el archivo queda igual y todo el mundo culpa a la persistencia. Segundo, el orden de arranque invertido que ya mencionamos: tabla vacía con la consola diciendo 'Mascotas cargadas: 12'. Tercero, la ruta del archivo: se ejecuta desde NetBeans y el .csv queda en la carpeta del proyecto, se ejecuta el JAR desde el escritorio y queda en otra parte, entonces 'se perdieron los datos'. Cuarto, el contrato del CSV roto entre quien escribe y quien lee, con el orden de campos distinto: el archivo se ve bien en el Bloc de notas pero la tabla muestra 'Canino' en la columna de edad. Quinto, la unión del código de tres personas que trajeron cada una su propia clase Mascota con constructores distintos. Y sexto, el clásico NullPointerException porque buscarPorId devuelve null cuando el ID no existe y nadie valida antes de usar el resultado.

El debugger de NetBeans es la herramienta de esta clase y hay que perderle el miedo en vivo. Se pone un breakpoint haciendo clic en el número de la línea (o Ctrl+F8), se ejecuta con Depurar proyecto (Ctrl+F5) y la aplicación se congela justo ahí. Desde ese punto, F8 avanza a la línea siguiente sin entrar a los métodos, F7 entra al método que se está llamando, Ctrl+F7 sale del método actual y F5 continúa hasta el siguiente breakpoint. Mientras está detenido, la ventana Variables muestra el valor real de cada campo y de cada objeto, Watches permite vigilar una expresión concreta como servicio.listar().size(), y Call Stack muestra quién llamó a quién, que es justo lo que uno necesita cuando no entiende por qué se ejecutó algo. Hay además una joya para integración: el breakpoint condicional, al que se le pone una condición como id.equals("M009") para que solo se detenga en el caso problemático y no en las doscientas iteraciones buenas. Todo esto es superior a llenar el código de System.out.println por tres razones: no ensucia el proyecto ni deja basura que después hay que borrar, muestra el estado completo y no solo lo que uno se acordó de imprimir, y permite mirar el orden real de las llamadas.

La forma de integrar sin sufrir es por goteo y no de un solo golpe. Integración de un solo golpe es juntar los cuatro módulos la noche anterior a la entrega; el resultado conocido es una aplicación que no arranca y nadie sabe cuál de los cuatro la rompió. Integración por goteo es unir de a un módulo, correr el guion de humo después de cada unión, y no avanzar mientras el ejecutable esté en rojo: primero modelo más servicio con un main de consola, después servicio más repositorio verificando el archivo en disco, después la ventana consumiendo el servicio, y por último el cierre que guarda. Cuando algo se rompe, uno sabe exactamente qué fue lo último que tocó. Tres hábitos más que valen oro: fijar por escrito el contrato entre módulos, es decir la firma de los métodos públicos del servicio y el orden exacto de los campos del CSV, para que quien escribe y quien lee no se contradigan; poner el try-catch en las fronteras, o sea en el manejador del botón y en el acceso al archivo, y no repartido por todo el modelo; y llevar la bitácora de integración con síntoma, causa y corrección de cada defecto, que es lo que se entrega y lo que salva en la sustentación.

Error tipico del docente que no domina el tema: junta todos los módulos la noche anterior, en clase la aplicación no arranca, y termina explicando el flujo en el tablero mientras los estudiantes nunca ven correr el producto; después culpa a NetBeans, al JDK o al computador del salón. El segundo error es no abrir jamás el debugger: llena el código de System.out.println, y como imprime solo lo que se le ocurrió imprimir, no logra distinguir entre 'el dato llegó mal desde el formulario' y 'el dato se guardó mal en el archivo', que son dos defectos completamente distintos con el mismo síntoma. El tercero es no fijar el contrato del CSV: cada estudiante escribe su propio orden de campos, y al integrar el módulo del compañero el archivo se lee corrido, con lo que el docente concluye que 'el CSV es frágil' cuando lo frágil fue el acuerdo. La disciplina que se enseña hoy y que el docente debe haber practicado antes de entrar al salón es: integrar temprano, integrar por partes, tener un guion de humo de dos minutos que se corre después de cada cambio, y llegar a clase con VetCare ya corriendo para poder romperlo a propósito delante del grupo y arreglarlo con el debugger en vivo, que es la única forma de que el estudiante crea que la herramienta sirve.

**Demo que usted debe poder repetir:** El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente corre el guion de humo completo (abrir, registrar, buscar, cerrar, reabrir) y luego pone un breakpoint en el botón Registrar para mostrar con el debugger por qué una edad vacía estaba entrando como cero.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 12/Codigo/VetCareApp.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Organice el proyecto en los paquetes vetcare.modelo, vetcare.datos, vetcare.logica y vetcare.ui, deje un único método main en la clase de arranque, elimine cualquier otro main que haya quedado de los talleres anteriores y verifique que la aplicación abre desde ese único punto.
2. Asegure una sola instancia: cree el repositorio y el servicio en el main y páselos por constructor a la ventana; ponga un breakpoint en el botón Registrar y otro en el cierre, y compruebe en la ventana Variables que el objeto servicio tiene el mismo identificador en ambos puntos.
3. Corra el guion de humo de cinco pasos (abrir con datos, registrar, buscar por ID, cerrar guardando, reabrir y verificar) y anote en qué paso exacto falla y con qué mensaje; si pasa completo a la primera, dañe una línea de mascotas.csv y vuelva a correrlo.
4. Depure el primer defecto con el debugger: breakpoint en el manejador del botón, registre el valor real de cada campo del formulario antes de llegar al servicio, identifique en qué capa se corrompe el dato y aplique la corrección; deje la evidencia en la bitácora.
5. Repita hasta que el guion de humo corra completo dos veces seguidas y entregue la bitácora de integración con tres defectos documentados con síntoma, causa, corrección y cómo lo verificó.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: El proyecto VetCare ejecutable (carpeta del proyecto o JAR) más la bitácora de integración con tres defectos hallados con el debugger, cada uno con síntoma, causa, corrección y evidencia, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare arranca, carga el archivo, registra, busca por ID, lista y guarda al cerrar: el flujo completo del PI corre sin tocar código.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx` — no proyectar completa.
