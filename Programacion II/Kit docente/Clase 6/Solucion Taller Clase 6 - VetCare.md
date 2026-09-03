# Solucion Taller · Clase 6 · Eventos y controladores · ActionListener

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Declare el estado como atributo y no como variable local. En VentanaRegistroMascota, arriba de todo, escriba: private final ControladorRegistro controlador = new ControladorRegistro(new RepositorioMascotas()); Al ser atributo se construye una sola vez, cuando nace la ventana, y sobrevive a todos los clicks porque vive mientras viva el objeto ventana. Este es justamente el error que hace creer que 'el ArrayList no guarda': si esa misma linea queda adentro del listener, en cada click se crea un repositorio nuevo, vacio, y el anterior queda huerfano para el recolector de basura.
2. Registre el escuchador en el constructor de la ventana y delegue de inmediato a un metodo privado. Escriba: btnRegistrar.addActionListener(new ActionListener() { @Override public void actionPerformed(ActionEvent e) { registrar(); } }); Note que addActionListener no ejecuta nada: solo deja anotado que ese objeto quiere enterarse. Como el cuerpo del listener tiene una sola linea, el listener no crece nunca y el metodo registrar() se puede leer completo en pantalla. Si la ventana viene de un generador o de una IA, la regla es la misma: dentro del cuerpo del listener no va mas que la llamada registrar();.
3. Escriba el metodo privado registrar() con la estructura leer-delegar-mostrar y nada mas. Dentro de un try llama a controlador.registrarMascota(txtId.getText(), txtNombre.getText(), txtEspecie.getText(), txtEdad.getText()); si el controlador devuelve la mascota, la vista refresca el area con areaListado.setText(controlador.reporteListado()), limpia los campos y muestra un JOptionPane con el nombre guardado; en el catch (IllegalArgumentException ex) muestra ex.getMessage() con JOptionPane.WARNING_MESSAGE. Fijese en el detalle que hay que decir en voz alta: la vista captura una excepcion y la pinta, pero no valida absolutamente nada.
4. Ponga todas las reglas en el controlador, que es la clase que no importa javax.swing. Ahi va: rechazar id y nombre vacios con trim().isEmpty() lanzando IllegalArgumentException con mensaje en español; convertir la edad con Integer.parseInt(edadTexto.trim()) envuelto en try-catch de NumberFormatException para relanzar IllegalArgumentException con el texto 'La edad debe ser un numero entero'; validar que la edad este entre 0 y 40 anios; y solo cuando todo paso, construir new Mascota(...) y llamar repositorio.registrar(mascota). El repositorio, por su parte, es el unico responsable del ID duplicado: antes de agregar consulta buscarPorId y, si encuentra algo, lanza 'Ya existe una mascota con el ID M-001'. Asi cada regla vive en una sola clase y no se repite.
5. Refresque y verifique con los tres casos del taller. El refresco se hace con areaListado.setText(controlador.reporteListado()), y reporteListado recorre repositorio.listar() armando el texto con un StringBuilder y agregando al final 'Total registradas: N'. Registre M-001 Kira, 4 (debe aparecer en el area y el total decir 1); luego escriba la edad 'tres' (debe salir el JOptionPane de edad invalida, el total sigue en 1 y la consola de VS Code queda limpia, sin traza roja); luego intente M-001 otra vez (mensaje de ID repetido, total sigue en 1). Si los tres casos se comportan asi, el ciclo leer-validar-delegar-refrescar quedo bien armado y es el mismo que reutilizara para las citas.

## Rubrica corta
- [ ] Ventana con formulario, boton y listado funcionando (2)
- [ ] Listener corto que solo lee, delega y muestra (3)
- [ ] ControladorRegistro y RepositorioMascotas sin dependencia de Swing (3)
- [ ] Manejo de errores con try-catch y evidencia de los tres casos (2)

## Errores frecuentes
- Crear el repositorio o el ArrayList dentro del listener, con lo cual cada click arranca con una coleccion vacia y parece que nada se guarda.
- Usar Integer.parseInt sin try-catch: la excepcion sube al EDT, se pinta una traza roja en la consola de VS Code y el usuario no ve ningun mensaje.
- Escribir la validacion dentro de actionPerformed y llenar la vista de ifs, de modo que la misma regla se vuelve a copiar y pegar en la ventana de citas.

Codigo de apoyo: `Kit docente/Clase 6/Codigo/VetCareEventosDemo.java`