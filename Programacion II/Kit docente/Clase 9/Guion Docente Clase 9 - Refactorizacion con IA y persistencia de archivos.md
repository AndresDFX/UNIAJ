# Guion docente · Clase 9 · Refactorización con IA · Persistencia en archivos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.
- **Entregable de hoy:** La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 9 - Refactorizacion con IA y persistencia de archivos/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Refactorizar es cambiar la forma interna del código sin cambiar ni un milímetro de su comportamiento externo. Si antes de tocar nada la aplicación registraba una mascota y mostraba 'Mascota registrada con ID M004', después de refactorizar tiene que registrar exactamente igual y mostrar exactamente el mismo mensaje; lo único que cambió es que el código quedó más fácil de leer y de modificar. En VetCare el caso clásico es el manejador del botón Registrar: un método de noventa líneas que valida el nombre, convierte la edad, genera el ID consecutivo, arma la línea del CSV, abre el archivo, escribe y muestra el aviso. Refactorizarlo es partirlo en cuatro métodos con nombre propio (validar, generarId, aLineaCsv, escribirArchivo) y mover los dos últimos a una clase RepositorioMascotasCSV. Y aquí va lo que refactorizar NO es: no es agregar funcionalidades nuevas, no es corregir errores de lógica, no es cambiar de librería, no es reescribir el proyecto desde cero. Si al terminar la aplicación hace algo distinto, eso ya no fue una refactorización: fue un cambio de requisitos disfrazado, y hay que probarlo como tal. La prueba de que el refactor salió bien es aburridamente simple: correr el mismo flujo con los mismos datos y obtener las mismas salidas.

Un code smell es un síntoma en el código que casi siempre anuncia un problema mayor; no es un error de compilación ni una excepción, es un olor. Los que van a aparecer sí o sí en los proyectos de VetCare son seis. Primero, el método largo: el ActionListener del botón que hace de todo. Segundo, la duplicación: el mismo bucle de búsqueda por ID copiado y pegado en el botón Buscar, en el botón Editar y en el botón Eliminar, de modo que cuando el criterio de búsqueda cambia hay que acordarse de arreglarlo en tres lugares y siempre se olvida uno. Tercero, los nombres opacos: ArrayList<String[]> a1, variables x, d, v, un método llamado proceso(). Cuarto, los números mágicos: un if (edad > 25) sin explicación, cuando lo correcto es una constante EDAD_MAXIMA = 25 con nombre. Quinto, el catch vacío que se traga la IOException y deja al usuario creyendo que guardó. Sexto, la clase Dios: una única clase Principal que es ventana, es lista y es archivo al mismo tiempo. NetBeans ayuda a atacarlos con acciones seguras del menú Refactor: Rename (Ctrl+R), Extract Method (Ctrl+Alt+M) y Move, que renombran o extraen actualizando todas las referencias, cosa que buscar y reemplazar a mano nunca garantiza.

Persistencia es lograr que los datos sobrevivan al proceso que los creó. Mientras la aplicación está corriendo, el ArrayList<Mascota> vive en la memoria RAM, que es rápida pero volátil: en el instante en que se cierra la ventana, el sistema operativo recupera esa memoria y las mascotas se evaporan. Guardar en disco significa convertir cada objeto Mascota en texto y escribirlo en un archivo que queda en el computador. Un .txt es texto libre, sirve para una bitácora o un log; un .csv es texto también, pero con una estructura tabular acordada: una línea por registro, campos separados por un carácter separador y, opcionalmente, una primera línea de encabezado que documenta el orden de las columnas. Para VetCare la línea acordada es M001;Firulais;Canino;4;1144556677 con encabezado id;nombre;especie;edad;cedula_dueno. Usamos punto y coma y no coma por dos razones muy prácticas: los nombres y las direcciones de los dueños suelen traer comas y le romperían la línea al programa, y el Excel en configuración regional de Colombia abre los archivos separados por punto y coma sin pedir nada. La ventaja enorme del CSV frente a un formato binario es que se puede abrir en el Bloc de notas y ver el dato: cuando algo falla, el estudiante ve con sus ojos si el problema está en lo que escribió o en cómo lo leyó.

Un archivo abierto es un recurso del sistema operativo, y todo recurso hay que cerrarlo. Cuando se escribe con un BufferedWriter, el texto no viaja al disco letra por letra: se acumula en un buffer en memoria y se vuelca cuando el buffer se llena o cuando se cierra el flujo. Por eso el error más desconcertante para un principiante es este: el programa corre sin lanzar ninguna excepción, dice 'guardado', y el archivo mascotas.csv aparece con cero bytes. No se cerró el escritor y lo que estaba en el buffer nunca bajó al disco. La solución moderna es try-with-resources: se declara el recurso entre paréntesis, try (BufferedWriter salida = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { ... }, y Java garantiza que se llama a close() al salir del bloque, ocurra lo que ocurra, incluso si se lanzó una excepción en la mitad. Reemplaza al viejo patrón de finally con verificación de null, que casi nadie escribe bien. Además, IOException es una excepción verificada: el compilador obliga a capturarla o a declararla, y eso no es una molestia, es el lenguaje recordando que el disco puede estar lleno, el archivo puede estar abierto en Excel o la ruta puede no existir. Especificar StandardCharsets.UTF_8 no es adorno: es lo que evita que 'Ñoño' vuelva del archivo convertido en símbolos raros.

La persistencia se conecta al ciclo de vida de la aplicación en dos puntos: se carga al arrancar y se guarda al cerrar (o después de cada cambio, si se quiere ser más seguro). Cargar al arrancar significa que el main construye el repositorio, pide cargar() y solo después muestra la ventana con la tabla ya poblada. Y cargar tiene que ser defensivo, porque el archivo es del mundo real: si mascotas.csv no existe todavía, cargar() devuelve una lista vacía y la aplicación abre normalmente, no revienta con una excepción en la cara del usuario; si una línea quedó con cuatro campos en vez de cinco porque alguien la editó en el Bloc de notas, esa línea se ignora, se avisa por consola con el número de línea y las demás sí se cargan; si la edad viene como 'dos', el Integer.parseInt lanza NumberFormatException, se captura, se descarta ese registro y se sigue. La regla es que un dato malo no puede tumbar la aplicación completa. Del lado de la escritura, el detalle que muerde es la ruta: si se usa la ruta relativa "mascotas.csv", el archivo queda en el directorio de trabajo, que al ejecutar desde NetBeans es la carpeta del proyecto. Por eso conviene imprimir una vez ruta.toAbsolutePath() para que el estudiante sepa dónde buscarlo en vez de jurar que el programa no guardó nada.

Error tipico del docente que no domina el tema: le pega el enunciado a la IA, recibe una solución con ObjectOutputStream y serialización binaria o con la librería OpenCSV, y la copia al proyecto sin entenderla. En clase pasan dos cosas: o no compila porque falta agregar el .jar a las librerías del proyecto, o sí corre pero genera un archivo binario ilegible, con lo cual se pierde justo el valor pedagógico de abrir el .csv y ver la línea escrita, y además se incumple el requisito del PI, que pide .txt o .csv. La otra versión del mismo error es pedirle a la IA 'refactoriza esto', aceptar el bloque completo y no volver a correr la aplicación: la IA cambió el separador, o quitó el encabezado, o invirtió el orden de dos campos, y ahora el archivo viejo se lee corrido con el nombre en la columna de la especie. Eso ya no fue refactorizar, fue romper. La postura correcta, y hay que decirla en voz alta frente al grupo, es que la IA propone y el humano decide: se acepta únicamente lo que uno puede explicar línea por línea, se acepta de a un cambio por vez, y después de cada cambio se vuelve a correr el flujo completo de VetCare. Un docente que no puede explicar por qué su código usa try-with-resources no está en condiciones de exigirle criterio al estudiante.

**Demo que usted debe poder repetir:** El docente registra una mascota, cierra la aplicación, la vuelve a abrir y la mascota sigue ahí; enseguida abre mascotas.csv en el Bloc de notas para mostrar la línea que escribió el programa.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente registra una mascota, cierra la aplicación, la vuelve a abrir y la mascota sigue ahí; enseguida abre mascotas.csv en el Bloc de notas para mostrar la línea que escribió el programa.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 9/Codigo/VetCarePersistencia.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Cree el paquete vetcare.datos y dentro la clase RepositorioMascotasCSV con la constante private static final String SEPARADOR = ";", la constante ENCABEZADO con el texto id;nombre;especie;edad;cedula_dueno y un atributo Path ruta construido con Paths.get("mascotas.csv"); compile el proyecto y verifique que no hay errores rojos antes de seguir.
2. Implemente guardar(List<Mascota>) usando try-with-resources: escriba el encabezado, recorra la lista y escriba una línea por mascota; ejecute, abra mascotas.csv en el Bloc de notas y verifique que tiene exactamente tantas líneas como mascotas más una, y el mismo número de punto y coma en todas.
3. Implemente cargar() de forma defensiva: si el archivo no existe devuelve una lista vacía, descarta la línea de encabezado, ignora las líneas que no tengan cinco campos e ignora las que traigan una edad no numérica, avisando por consola el número de la línea; compruébelo dañando a propósito una línea del archivo y volviendo a ejecutar.
4. Conecte el repositorio al ciclo de vida de la aplicación: cargar() al arrancar antes de mostrar la ventana y guardar() al cerrar; cierre la aplicación, vuelva a abrirla y verifique que el conteo de mascotas en la tabla es el mismo que había antes de cerrar.
5. Haga una revisión asistida por IA de su método guardar(): pídale a la herramienta que señale problemas, aplique como máximo dos mejoras que usted pueda explicar en voz alta, rechace por escrito al menos una sugerencia y registre todo en REFACTOR.md con el formato 'sugerencia / la acepté o no / por qué'; vuelva a correr el flujo completo y confirme que el comportamiento es idéntico.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: La clase RepositorioMascotasCSV con guardar() y cargar() funcionando, el archivo mascotas.csv generado por la propia aplicación y la bitácora REFACTOR.md, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 9/Quiz Clase 9 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare guarda la lista de mascotas en mascotas.csv al cerrar y la vuelve a cargar al abrir.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 9/Solucion Taller Clase 9 - VetCare.docx` — no proyectar completa.
