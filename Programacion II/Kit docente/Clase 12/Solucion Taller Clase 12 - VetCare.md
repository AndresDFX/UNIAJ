# Solucion Taller · Clase 12 · Integración de módulos

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1. Se deja un solo punto de entrada y se cablea la aplicación en el orden correcto dentro del main: RepositorioMascotasCSV repositorio = new RepositorioMascotasCSV("mascotas.csv"); ServicioVetCare servicio = new ServicioVetCare(repositorio); servicio.cargarDesdeArchivo(); y solo después SwingUtilities.invokeLater(() -> new VetCareApp(servicio).setVisible(true)). El servicio se inyecta por constructor y la ventana no crea el suyo: esa sola decisión elimina de raíz el defecto de las dos instancias. Se corre y la consola debe imprimir cuántas mascotas trajo el CSV antes de que exista un solo botón en pantalla.
2. Paso 2. Se conecta la tabla al servicio con un único método refrescarTabla() que hace modelo.setRowCount(0) y vuelve a llenar recorriendo servicio.listar(). Ese método se llama en el constructor de la ventana, después de registrar y después de cualquier cambio. Si la tabla sale vacía con datos cargados, se pone un breakpoint dentro de refrescarTabla() y en Variables se mira el tamaño de la lista: si llega en cero, el problema es que la ventana está mirando otro servicio; si llega en doce y la tabla sigue vacía, el problema es que refrescarTabla() se llamó antes de cargar o que el DefaultTableModel que se llena no es el que está montado en el JTable.
3. Paso 3. Se ponen los try-catch en las fronteras y no en el modelo. El servicio valida y lanza DatosInvalidosException con un mensaje entendible ("La edad debe ser un numero entero. Llego: ''"), y quien captura y muestra el JOptionPane es el manejador del botón, que es la capa que sabe de ventanas. Con esto el caso de la edad vacía deja de guardarse como cero: antes, un catch mal ubicado la convertía en 0 en silencio; ahora el usuario ve exactamente qué escribió mal y el registro no entra.
4. Paso 4. Se depura un defecto real con el debugger. Síntoma: al registrar 'Pelusa' con edad vacía, la mascota aparecía con edad 0. Breakpoint en registrarMascota(), Ctrl+F5 para depurar, se llena el formulario y al detenerse se mira en Variables que txtEdad.getText() trae la cadena vacía; con F7 se entra a servicio.registrar() y se ve que el Integer.parseInt lanza NumberFormatException que estaba siendo capturada asignando cero. Causa localizada en la capa de lógica, no en la interfaz. Corrección: convertir esa captura en el lanzamiento de DatosInvalidosException. Verificación: se repite el caso y ahora sale el aviso 'La edad debe ser un numero entero' y no se agrega ninguna fila a la tabla.
5. Paso 5. Se cierra la ventana con guardado controlado: setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE) más un WindowAdapter cuyo windowClosing llama a servicio.guardarEnArchivo(), avisa cuántas mascotas quedaron en el archivo y solo entonces hace dispose(); si el guardado lanza IOException, se le pregunta al usuario si desea cerrar de todas formas en lugar de perder los datos en silencio. Después se corre el guion de humo completo dos veces seguidas: la segunda corrida debe mostrar en la tabla la mascota registrada en la primera, y ese es el criterio de que la integración quedó.

## Rubrica corta
- [ ] Un solo main, capas separadas y una sola instancia de servicio y repositorio inyectada por constructor (3)
- [ ] Guion de humo de cinco pasos corriendo completo dos veces seguidas, con persistencia verificada al reabrir (3)
- [ ] Manejo de errores en las fronteras: validación en el servicio y mensaje al usuario en la interfaz, sin catch vacíos (2)
- [ ] Bitacora de integración con tres defectos documentados con síntoma, causa hallada con el debugger, corrección y verificación (2)

## Errores frecuentes
- Que la ventana cree su propio ServicioVetCare además del que creó el main: se registra en una lista y se guarda la otra, entonces el archivo nunca cambia y el equipo culpa a la persistencia.
- Construir y mostrar la ventana antes de llamar a cargarDesdeArchivo(), con lo cual la tabla nace vacía aunque la consola confirme que se cargaron doce mascotas.
- Usar el resultado de buscarPorId() sin validar null, de modo que la aplicación se cae con NullPointerException justo cuando el usuario escribe un ID que no existe, que es el caso más común del mostrador.

Codigo de apoyo: `Kit docente/Clase 12/Codigo/VetCareApp.java`