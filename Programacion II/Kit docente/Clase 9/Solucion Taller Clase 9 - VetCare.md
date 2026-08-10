# Solucion Taller · Clase 9 · Refactorización con IA · Persistencia en archivos

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1. Se crea RepositorioMascotasCSV como única clase que sabe de archivos, con private static final String SEPARADOR = ";" (comillas dobles: es un String, no un char) y private final Path ruta = Paths.get("mascotas.csv"). Se aísla aquí porque así la ventana y el servicio quedan sin una sola línea de entrada/salida: el día que se cambie a base de datos solo se reemplaza esta clase. Se agrega además un método rutaAbsoluta() que devuelve ruta.toAbsolutePath().toString(), que se imprime una vez al arrancar para saber dónde quedó el archivo.
2. Paso 2. guardar() se escribe así: try (BufferedWriter escritor = Files.newBufferedWriter(ruta, StandardCharsets.UTF_8)) { escritor.write(ENCABEZADO); escritor.newLine(); for (Mascota m : mascotas) { escritor.write(aLinea(m)); escritor.newLine(); } } catch (IOException e) { avisar("No se pudo guardar: " + e.getMessage()); }. Se usa newLine() y no el carácter de salto escrito a mano porque newLine() pone el separador de línea del sistema operativo. El try-with-resources cierra el escritor aunque explote a la mitad, y eso es lo que garantiza que el buffer llegue al disco.
3. Paso 3. aLinea(Mascota) concatena los cinco campos con el separador, pero pasando cada texto por limpiar(), que reemplaza cualquier punto y coma que traiga el dato por una coma. Sin ese detalle, un dueño registrado como 'Casa 3; apto 201' partiría la línea en seis campos y al recargar el archivo esa mascota se perdería. Es la lección de que el formato tiene un contrato y hay que defenderlo al escribir, no al leer.
4. Paso 4. cargar() empieza preguntando if (!Files.exists(ruta)) return new ArrayList<>(); esa sola línea es la diferencia entre una aplicación que abre normalmente el primer día y una que arranca con una excepción. Luego, dentro del try-with-resources, se lee la primera línea y se descarta por ser el encabezado, y en el bucle while ((linea = lector.readLine()) != null) se salta lo vacío, se hace split(SEPARADOR, -1), se valida que campos.length == 5 y se convierte la edad dentro de su propio try-catch de NumberFormatException. Las líneas malas se reportan con su número y se ignoran; las buenas se agregan.
5. Paso 5. Se conecta al ciclo de vida: en el main se construye el repositorio, se llama cargar() y solo después se muestra la ventana; en el cierre (windowClosing) se llama guardar(). Para el ejercicio de IA se le pide a la herramienta que revise guardar(); típicamente sugiere extraer el armado de la línea a un método aparte (se acepta: es forma, no comportamiento) y cambiar a serialización de objetos (se rechaza por escrito: el PI exige .csv legible y el archivo binario no se puede inspeccionar en clase). Ambas decisiones quedan en REFACTOR.md y se vuelve a correr el flujo completo para confirmar que el comportamiento no cambió.

## Rubrica corta
- [ ] Metodo guardar() con try-with-resources, encabezado y escape del separador (3)
- [ ] Metodo cargar() tolerante a archivo inexistente y a lineas dañadas (3)
- [ ] Ciclo de vida conectado: carga al abrir y guarda al cerrar, verificado cerrando y reabriendo (2)
- [ ] Bitacora REFACTOR.md con al menos una sugerencia de IA aceptada y una rechazada, ambas justificadas (2)

## Errores frecuentes
- Olvidar el try-with-resources (o abrir el flujo fuera del try) y quedarse con un mascotas.csv de 0 bytes, jurando que el programa no guarda porque 'no dio error'.
- No descartar la línea de encabezado al cargar, con lo cual el programa intenta convertir la palabra 'edad' en número, o peor, aparece una mascota fantasma llamada 'nombre' en la tabla.
- Escribir los campos en un orden al guardar y leerlos en otro al cargar (por ejemplo, especie y edad intercambiadas), de modo que el archivo se ve bien pero la tabla muestra 'Canino' en la columna de edad.

Codigo de apoyo: `Kit docente/Clase 9/Codigo/VetCarePersistencia.java`