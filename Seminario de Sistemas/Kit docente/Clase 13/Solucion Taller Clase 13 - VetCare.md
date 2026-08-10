# Solucion Taller · Clase 13 · Diseño de interfaces

> DOCUMENTO DOCENTE — PRIVADO. No publicar en Clases/.

## Solucion paso a paso
1. Paso 1 resuelto. El wireframe de Registrar mascota queda en tres bloques verticales. Bloque uno, Dueño, con un campo de busqueda por documento o telefono y un enlace secundario Registrar dueño nuevo. Bloque dos, Datos de la mascota, con Nombre, Especie como lista cerrada de Canino, Felino y Otro, Raza como lista con opcion Mestizo, Fecha de nacimiento con selector de calendario, Sexo con dos opciones visibles y Peso con la unidad kg escrita al lado del campo. Bloque tres, zona de accion abajo a la derecha con boton primario Guardar y enlace discreto Cancelar. Total nueve campos y cero scroll.
2. Paso 2 resuelto. La tabla de anotaciones queda asi. Uno, Nombre, viene de Mascota.nombre, texto de sesenta, obligatorio, exigido por RF-03. Dos, Especie, viene de Mascota.especie, lista cerrada, obligatorio, RF-03. Tres, Fecha de nacimiento, viene de Mascota.fecha_nacimiento, tipo fecha, opcional porque muchos dueños no la saben, RF-03. Cuatro, buscador de dueño, viene de Dueño.documento, texto de quince, obligatorio antes de guardar, exigido por RF-02 y por la regla toda mascota debe tener un dueño registrado. Cinco, mensaje Ficha guardada, codigo M-0421, cumple visibilidad del estado y el RNF-02 de respuesta en menos de tres segundos. Seis, boton Guardar deshabilitado mientras falten obligatorios, cumple prevencion de errores.
3. Paso 3 resuelto. Buscar expediente ofrece tres criterios en una sola barra con selector: documento del dueño, nombre de la mascota y codigo de ficha. La lista de resultados muestra cinco columnas, codigo, nombre de la mascota, especie, edad calculada y nombre del dueño, que es justo lo que permite desambiguar doce Firulais. Cuando no hay resultados el mensaje es No encontramos ninguna ficha con ese dato, con dos acciones sugeridas debajo, Buscar por otro criterio y Registrar mascota nueva, en vez de dejar la pantalla en blanco.
4. Paso 4 resuelto. En Penpot se crean tres frames y se conectan. Guardar de Registrar mascota lleva al frame Confirmacion con el codigo visible, que cumple visibilidad del estado. Ver ficha de la confirmacion lleva a Buscar expediente con el codigo ya cargado, que cumple reconocer antes que recordar. Un clic sobre una fila de resultados lleva a la Ficha del paciente. Ademas se modela el camino alterno: el enlace Registrar dueño nuevo abre un frame de dueño y regresa al formulario de mascota conservando lo ya escrito.
5. Paso 5 resuelto. La prueba de pasillo con un compañero de otro equipo arroja tipicamente que la persona duda en el buscador de dueño porque no sabe si buscar o registrar primero, y que no encuentra el boton Guardar por estar muy abajo. Los dos cambios concretos que se documentan son: poner un texto de ayuda bajo el buscador que diga Escriba el documento del dueño; si no aparece, registrelo aqui, y anclar la barra de accion al pie de la pantalla para que Guardar sea siempre visible. Se anota el tiempo antes y despues, por ejemplo dos minutos cuarenta y luego un minuto cincuenta.

## Rubrica corta
- [ ] Wireframes en gris de las dos pantallas, con jerarquia clara y sin scroll (2)
- [ ] Tabla de anotaciones con trazabilidad campo a RF y a diccionario de datos (3)
- [ ] Prototipo navegable con tres transiciones y dos caminos alternos resueltos (3)
- [ ] Evidencia escrita de los cuatro principios de usabilidad y bitacora de la prueba de pasillo (2)

## Errores frecuentes
- Entregar directamente el mockup bonito sin wireframe previo, lo que hace que el equipo discuta colores durante media hora y llegue a la clase 14 sin haber resuelto el flujo ni los mensajes de error.
- Dibujar campos que no existen en el diccionario de datos, como correo de la mascota o numero de chip, y al mismo tiempo olvidar el campo obligatorio de dueño, con lo cual la pantalla contradice el modelo de clases entregado en clases anteriores.
- Diseñar solo el camino feliz: no hay pantalla de resultados multiples, no hay mensaje de busqueda sin resultados y no hay confirmacion tras guardar, de modo que el prototipo se cae en la sustentacion apenas el jurado hace clic en algo distinto de lo ensayado.

Plantilla de apoyo: `Kit docente/Clase 13/Plantillas/Wireframes-Anotados-VetCare.md`