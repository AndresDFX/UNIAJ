# Guion docente · Clase 12 · Integracion app <-> BD · Prep. presentacion

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Contrato integracion + preparacion de entrega/sustentacion
- **Entregable de hoy:** Contrato app<->BD + outline de slides de sustentacion (5-8 min)
- **Herramienta:** ExamLab (PostgreSQL/PGlite) + Excalidraw / Mermaid
- **Slides:** Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): Hasta hoy la base se usó desde un editor de SQL. Hoy la usa una aplicación, y la pregunta es por dónde entra: si arma texto SQL contra las tablas o si llama operaciones con un contrato.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema y pregunta: «si la recepcionista escribe un nombre raro en el buscador de mascotas, ¿podría borrar o cambiar algo?». Deja la pregunta abierta: se responde en la lámina de la inyección.
- Después: Cierra: «al final van a poder explicar por qué un parámetro hace imposible la inyección y qué lleva el contrato de una operación».

CUIDADO: Esta sesión es doble con la Clase 11: si la revisión se alargó, recorta el pool de conexiones, no la inyección ni el contrato.

PASA A LA SIGUIENTE: Empezamos por la decisión de la que sale todo lo demás: la puerta.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido del bloque: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] Integrar no es conectarse: cual es la unica puerta de entrada

QUÉ ES (dilo así): Integrar la aplicación con la base no es abrir una conexión: es decidir cuál es la única puerta por la que la aplicación toca los datos y dejarla escrita en un contrato. Hay dos formas de construirla, y la elección decide la seguridad, dónde vive cada regla y qué tan fácil es cambiar el esquema.

CÓMO DARLA (≈4 min):
- Al entrar: Primera forma: la aplicación escribe SELECT, INSERT y UPDATE contra dueno, mascota, cita e insumo. Consecuencias: inyección SQL posible, la regla de negocio repetida en cada pantalla y las tablas atadas al código.
- Clic 1: Segunda forma: la aplicación solo llama procedimientos y funciones (los de las Clases 3 y 4), descritos en un contrato. Cada regla vive en un lugar, las tablas pueden reorganizarse por dentro y al rol de la aplicación se le deja solo EXECUTE, el mínimo privilegio de la Clase 2.
- Clic 2: La frase: conectarse son dos líneas; integrar es elegir la puerta. Todo lo demás de hoy sale de esta decisión.

EJEMPLO: Con la segunda forma, el rol de la aplicación recibe GRANT EXECUTE ON PROCEDURE sp_agendar_cita(INT, INT, TIMESTAMP) y ningún INSERT sobre cita: aunque alguien tome el control de la aplicación, no puede escribir en la tabla sino a través de la regla.

SI PREGUNTAN:
- «¿Y las consultas de solo lectura, también por función?» → Pueden ir por función (como api_agenda_del_dia, más adelante) o con SELECT sobre las tablas o vistas que la pantalla necesita. Lo que no se da es escritura directa.

CUIDADO: En PostgreSQL una función o un procedimiento nuevo queda con EXECUTE para PUBLIC: si no se revoca, cualquier rol puede llamarlo. El mínimo privilegio exige REVOKE EXECUTE … FROM PUBLIC y luego el GRANT al rol de la aplicación.

PASA A LA SIGUIENTE: La primera consecuencia de la puerta equivocada tiene nombre: inyección SQL.

### [Slide 5] Inyeccion SQL: cuando el dato se interpreta como codigo

QUÉ ES (dilo así): La inyección SQL pasa cuando la aplicación pega dentro del texto de la consulta lo que escribió el usuario. El motor recibe una cadena, la analiza completa y ejecuta lo que diga: no puede saber qué parte puso el programador y qué parte el usuario.

CÓMO DARLA (≈5 min):
- Al entrar: La aplicación arma sql = "… WHERE nombre = '" + entrada + "'". Con «Luna» el motor recibe WHERE nombre = 'Luna' y devuelve una fila: todo parece correcto. El usuario malicioso escribe ' OR 1=1 --.
- Clic 1: Lo que recibe el motor: WHERE nombre = '' OR 1=1 --'. La comilla del usuario cierra el texto, OR 1=1 es verdadero para toda fila y el doble guion convierte en comentario la comilla que sobraba.
- Clic 2: Resultado: las 8 mascotas de la tabla, no una. El mismo truco en un formulario de acceso (WHERE usuario = 'U' AND clave = 'C') deja entrar sin conocer ninguna clave.

EJEMPLO: SELECT id_mascota, nombre FROM mascota WHERE nombre = '' OR 1=1 --' devuelve 8 filas: Firulais, Luna, Rocky, Mishi, Bobby, Nube, Toby y Kiara.

SI PREGUNTAN:
- «¿Basta con quitar las comillas de la entrada?» → No: filtrar caracteres es una carrera que se pierde (números sin comillas, ORDER BY armado con texto, otras codificaciones). La defensa es que el dato nunca forme parte del texto: parámetros.
- «¿Esto sigue pasando hoy?» → Sí: la inyección ha estado en todas las ediciones del Top 10 de OWASP y fue la número uno en 2010, 2013 y 2017.

CUIDADO: No reduzcas la clase a «usen parámetros» sin mostrar la cadena rompiéndose: quien no vio el mecanismo vuelve a concatenar justo donde el parámetro le estorba, como en un ORDER BY o una lista IN.

PASA A LA SIGUIENTE: Las dos versiones en código, una al lado de la otra.

### [Slide 6] La inyeccion de SQL, explicada con las dos versiones

QUÉ ES (dilo así): La misma búsqueda de dueños armada de las dos maneras. La mala pega la entrada al texto; la buena prepara la sentencia con un marcador $1 y manda el valor aparte.

CÓMO DARLA (≈3 min):
- Líneas 1-4: Versión mala: si alguien escribe x'; UPDATE cita SET estado = 'CANCELADA'; -- el motor recibe dos sentencias, la búsqueda y un UPDATE sin WHERE, y ejecuta las dos: toda la agenda queda cancelada. En PostgreSQL, apilar sentencias con punto y coma funciona cuando el texto se envía sin parámetros.
- Líneas 6-8: Versión buena: PREPARE buscar_dueno (VARCHAR) deja la sentencia analizada, con $1 como casilla para un valor de texto.
- Líneas 10-12: EXECUTE buscar_dueno('Ana Gomez') devuelve 1 fila (1 | Ana Gomez | 3001112233). Con la entrada maliciosa devuelve 0 filas: busca un dueño que se llame literalmente así y el UPDATE nunca se ejecuta. Las comillas dobladas ('') son solo la forma de escribir una comilla dentro de un texto SQL.

EJEMPLO: SELECT COUNT(*) FROM cita WHERE estado = 'CANCELADA'; da 1 antes y después del EXECUTE malicioso: nada cambió. Con la versión concatenada, el UPDATE responde UPDATE 10 y el conteo pasa a 10.

SI PREGUNTAN:
- «¿Y un DROP TABLE cita?» → Apilado también se intentaría, pero en esta base lo detiene la clave foránea de consulta («cannot drop table cita because other objects depend on it»). Un UPDATE sin WHERE no tiene ese freno.
- «¿Cómo se ve en el código de la aplicación?» → En Python con psycopg2: cur.execute("SELECT … WHERE nombre = %s", (entrada,)). El valor va en la tupla, nunca dentro de la cadena.

CUIDADO: PREPARE y EXECUTE son la versión en SQL del mecanismo; en la aplicación lo hace el driver con parámetros. La idea es la misma: el valor viaja separado del texto.

PASA A LA SIGUIENTE: ¿Por qué el parámetro lo evita siempre, y no casi siempre?

### [Slide 7] Por que el parametro lo evita por construccion

QUÉ ES (dilo así): El parámetro no limpia la entrada: cambia el orden en que el motor trabaja. Primero analiza la sentencia con un marcador y fija su estructura; después recibe el valor como dato. Como el valor nunca pasa por el analizador, no puede cambiar la estructura de la sentencia.

CÓMO DARLA (≈4 min):
- Al entrar: Llega la sentencia sola: SELECT id_mascota, nombre FROM mascota WHERE nombre = $1. El analizador fija su estructura: una comparación de nombre con una casilla.
- Clic 1: Después llega el valor, ' OR 1=1 --, y entra en la casilla como texto literal. No vuelve al analizador: no hay forma de que se convierta en un OR.
- Clic 2: Resultado: 0 filas, ninguna mascota se llama así. No se filtró nada: la estructura ya estaba cerrada cuando llegó el dato.

EJEMPLO: Marcadores según la tecnología: $1 en una sentencia preparada de PostgreSQL, ? en JDBC, %s en psycopg2 de Python. Oracle escribe :p_nombre, solo como contraste.

SI PREGUNTAN:
- «Si uso un ORM como JPA, ¿ya estoy protegido?» → Sí mientras uses sus métodos o consultas con parámetros nombrados; no en el momento en que armes una consulta nativa concatenando texto. La vulnerabilidad la produce la concatenación, no la tecnología.
- «¿psycopg2 también manda el valor aparte?» → psycopg2 escapa el valor de forma segura en el cliente antes de enviarlo; psycopg 3 lo envía separado al servidor. En los dos casos, usando %s con la tupla, la entrada no puede cambiar la sentencia.

CUIDADO: No lo expliques como «limpiar la entrada»: con un parámetro del servidor ($1) el valor nunca se analiza como código, y por eso la protección no se puede saltar.

PASA A LA SIGUIENTE: Si la aplicación solo llama operaciones, cada operación necesita su contrato.

### [Slide 8] El contrato y sus seis partes

QUÉ ES (dilo así): El contrato es el documento de la puerta: lo que una operación recibe, lo que exige, lo que cambia, cómo falla, si se puede repetir y cómo evoluciona. Con él, un desarrollador que nunca vio la base puede usarla sin adivinar.

CÓMO DARLA (≈5 min):
- Al entrar: Solo el nombre, sp_agendar_cita(…), no es contrato. Las tres primeras partes: la firma (parámetros con tipo y dirección IN, OUT o INOUT, y lo que devuelve), las precondiciones (la mascota existe y está activa, la franja está libre) y el efecto (inserta una fila en cita en estado PROGRAMADA). En una función de la capa de API, la firma incluye el contrato de retorno: RETURNS TABLE (ok, mensaje, id_generado).
- Clic 1: Las otras tres: los errores, cada uno con su mensaje o código (mascota inexistente, mascota inactiva, franja ocupada); la idempotencia (¿dos llamadas iguales dejan lo mismo que una?); y la versión (cómo cambia sin romper a quien ya la llama).
- Clic 2: Lo respetan las dos partes. Y el ejemplo de idempotencia: agendar no lo es; si la recepcionista da doble clic, o la red corta la respuesta y la aplicación reintenta, quedan dos citas, salvo que el UNIQUE (id_veterinario, fecha_hora) haga fallar el segundo intento en la base.

EJEMPLO: El contrato de agendar en PostgreSQL: sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP), invocado con CALL; si una regla falla, aborta con un mensaje literal y no deja nada escrito.

SI PREGUNTAN:
- «¿Qué es idempotente, con un ejemplo de la clínica?» → Una operación que repetida deja lo mismo que una vez. Marcar la cita 7 como ATENDIDA lo es; agendar una cita, no.
- «¿Cómo se hace idempotente agendar?» → Con una restricción única que absorba el duplicado, o con una clave de idempotencia que la aplicación genera y la base guarda como única.

CUIDADO: Un contrato que es solo una tabla con nombres de procedimientos y una descripción vaga no sirve: sin tipos, errores e idempotencia, quien integra no sabe qué hacer cuando la llamada falla.

PASA A LA SIGUIENTE: Así se ve una operación de la capa de API en código.

### [Slide 9] El contrato de la capa de API: siempre parametros ligados

QUÉ ES (dilo así): Una operación de lectura de la capa de API: la agenda de un día. La aplicación no conoce las tablas cita, mascota ni dueno; llama api_agenda_del_dia con una fecha y recibe filas con columnas fijas.

CÓMO DARLA (≈3 min):
- Líneas 2-5: La firma: un parámetro DATE, RETURNS TABLE con las cuatro columnas que la pantalla recibe, LANGUAGE sql porque es una sola consulta y STABLE porque lee tablas sin modificarlas.
- Líneas 7-10: El cuerpo une cita con mascota y dueno por sus claves foráneas.
- Líneas 11-12: Filtra por rango, desde el día (p_dia) hasta el siguiente (p_dia + 1), sin función sobre la columna, para que un índice sobre fecha_hora sirva. Ordena por hora.

EJEMPLO: SELECT * FROM api_agenda_del_dia(DATE '2026-09-01'); devuelve 3 filas: la cita 1 de Firulais a las 08:00 y la 2 de Luna a las 09:00 (dueña Ana Gomez), y la 3 de Mishi a las 10:00 (dueña Marcela Diaz).

SI PREGUNTAN:
- «¿Por qué STABLE y no IMMUTABLE?» → Porque lee tablas: si alguien agenda, el resultado cambia. IMMUTABLE prometería que nunca cambia (Clase 4).
- «Las columnas se declaran VARCHAR y en la tabla son TEXT: ¿falla?» → No: PostgreSQL convierte el resultado al tipo declarado. Aun así, lo limpio es declarar el mismo tipo de la tabla.

CUIDADO: La aplicación la llama con parámetro: SELECT * FROM api_agenda_del_dia(%s), con la fecha en la tupla, nunca pegada en el texto.

PASA A LA SIGUIENTE: Y una operación de escritura: el contrato que la aplicación consume.

### [Slide 10] El contrato que la app consume (no SQL suelto)

QUÉ ES (dilo así): Lo único que la aplicación conoce de la base para agendar: el nombre del procedimiento, sus parámetros y los mensajes con que puede fallar.

CÓMO DARLA (≈3 min):
- Líneas 1-5: La llamada con parámetros nombrados (p_id_mascota => 3): no depende del orden y se lee sola. Los valores viajan tipados, no como texto pegado.
- Líneas 7-8: La mascota 3 (Rocky) está inactiva: el CALL aborta. El mensaje completo del procedimiento de la clase es «ERROR: la mascota 3 esta inactiva; no se agenda cita»: el primer ERROR lo pone el cliente y el segundo es parte del texto del RAISE.
- Leyenda: El contrato fija la firma, un ejemplo de llamada, los mensajes literales y qué queda en la base si la llamada falla: nada.

EJEMPLO: SELECT COUNT(*) FROM cita; da lo mismo antes y después del CALL fallido.

SI PREGUNTAN:
- «¿Por qué el mensaje dice ERROR dos veces?» → El cliente antepone «ERROR:» a todo error, y el procedimiento escribió «ERROR:» dentro de su mensaje. Con USING ERRCODE la aplicación reconoce el caso por el código, sin leer el texto.

CUIDADO: Mostrar este mensaje al usuario está bien porque es de negocio; lo que nunca se muestra es un error técnico del motor, como «relation "cita" does not exist».

PASA A LA SIGUIENTE: ¿Qué hace cada capa cuando algo falla? Tres reglas.

### [Slide 11] El manejo de errores entre capas: las tres reglas

QUÉ ES (dilo así): Cuando algo falla, cada capa tiene una tarea: la base informa de una forma que no se pueda pasar por alto, la aplicación lo traduce para el usuario y registra el detalle técnico, y nadie confirma a medias. La base tiene dos formas correctas de informar, y se elige por la clase de fallo.

CÓMO DARLA (≈4 min):
- Al entrar: Regla 1: un p_resultado := -1 en un parámetro de salida se ignora fácil. Un rechazo de negocio esperado (mascota inactiva, franja ocupada, sin stock) se devuelve en la fila del contrato: RETURN QUERY SELECT FALSE, 'Franja ocupada', NULL, y la aplicación está obligada a leer ok. Un error que debe abortar (una regla rota a mitad de una operación de varios pasos, una llamada desde otro procedimiento o un trigger, un dato imposible) se lanza: RAISE EXCEPTION … USING ERRCODE = 'MA001'. Sin USING ERRCODE todos los errores propios salen con el código genérico P0001.
- Clic 1: Regla 2: la aplicación muestra «La mascota está inactiva» (lo traduce del mensaje o del código MA001) y guarda en el log del servidor el error técnico con un identificador de correlación. Nunca muestra el texto crudo del motor: un «relation "cita" does not exist» le regala al atacante el nombre de las tablas.
- Clic 2: Regla 3: la operación de negocio completa vive en un procedimiento o una función. Si lanza el error, la excepción sale del CALL y deshace todo sin que nadie escriba ROLLBACK; si devuelve ok = false, la aplicación hace rollback de lo suyo. Nadie confirma a la mitad.

EJEMPLO: DO $$ BEGIN RAISE EXCEPTION 'la mascota % esta inactiva', 3 USING ERRCODE = 'MA001'; END $$; responde ERROR: la mascota 3 esta inactiva, con SQLSTATE MA001; sin el USING, el mismo mensaje sale con P0001.

SI PREGUNTAN:
- «¿Cuándo devuelvo y cuándo lanzo?» → Se devuelve lo que la aplicación debe manejar como respuesta normal de la operación (el usuario puede elegir otra franja). Se lanza lo que debe deshacer todo y no dejar seguir a nadie por descuido.
- «¿Y un WHEN OTHERS dentro de una función de la capa de API?» → Vale si devuelve ok = false con SQLERRM: el bloque EXCEPTION deshace lo que alcanzó a escribir y la aplicación recibe una fila que debe revisar. Lo que nunca vale es WHEN OTHERS THEN NULL, que captura y no informa.

CUIDADO: El error que arruina proyectos es capturar toda excepción, no informar nada y continuar: las citas se pierden en silencio y el informe deja de coincidir con la base.

PASA A LA SIGUIENTE: Así se ve una operación que devuelve su resultado en la fila del contrato.

### [Slide 12] El contrato como fila: ok, mensaje e id_generado

QUÉ ES (dilo así): Una función de la capa de API con contrato de retorno: siempre devuelve una fila con ok, mensaje e id_generado. Los rechazos de negocio salen como ok = false con su mensaje; lo inesperado se captura, se deshace y también sale como ok = false. La aplicación nunca recibe una excepción cruda, pero está obligada a revisar ok.

CÓMO DARLA (≈3 min):
- Líneas 1-3: La firma: un parámetro y RETURNS TABLE (ok BOOLEAN, mensaje TEXT, id_generado INT). Ese es el contrato de retorno, igual para todas las operaciones de la capa.
- Líneas 5-10: El UPDATE solo toca la cita si está PROGRAMADA. Si no tocó nada (IF NOT FOUND) es un rechazo de negocio esperado: devuelve FALSE, 'No se puede cancelar' y NULL en id_generado, y termina con RETURN.
- Línea 11: Camino feliz: TRUE, 'Cita cancelada' y el id de la cita afectada.
- Líneas 12-13: Lo inesperado: EXCEPTION WHEN OTHERS deshace lo que el bloque alcanzó a escribir y devuelve FALSE con SQLERRM. Informa; no se traga el error.
- Líneas 16-17: La primera llamada cancela la cita 3 (t | Cita cancelada | 3); la segunda ya no la encuentra programada (f | No se puede cancelar | NULL).

EJEMPLO: Si un trigger fallara después del UPDATE, la función devolvería f con el mensaje del trigger y la cita seguiría PROGRAMADA: el bloque EXCEPTION deshizo el UPDATE.

SI PREGUNTAN:
- «¿Por qué se llama id_generado si aquí no se genera nada?» → Es el nombre fijo del contrato para toda la capa: en una operación que crea trae el id nuevo; en cancelar, el de la cita afectada; si ok es falso, NULL.
- «¿Quién hace COMMIT?» → La aplicación, según ok: si es verdadero confirma; si es falso hace rollback de lo que llevaba en su transacción.

CUIDADO: Este diseño solo funciona si la aplicación revisa ok en cada llamada: una aplicación que ignora la fila repite el problema del -1.

PASA A LA SIGUIENTE: La misma operación, dibujada como diagrama de secuencia.

### [Slide 13] El flujo de la operacion en sequenceDiagram, con alt y else

QUÉ ES (dilo así): El diagrama de secuencia documenta quién llama a quién y qué responde, en orden de arriba abajo. La rama de error se dibuja con alt … else … end, y una nota fija la regla de acceso.

CÓMO DARLA (≈3 min):
- Líneas 1-5: sequenceDiagram y los participantes: actor para la persona (Recepcionista) y participant para cada sistema (Aplicacion, Capa de API, Tabla cita). Lo que va después de as es el nombre que se dibuja.
- Líneas 6-8: Las llamadas: ->> es una flecha sólida de quien llama a quien responde, con el mensaje después de los dos puntos. La aplicación pasa el id como parámetro y la capa hace el UPDATE.
- Líneas 9-15: alt abre la rama ok = false: la respuesta (-->> es la línea punteada, la de vuelta) y la aplicación muestra el mensaje y no sigue. else abre la rama ok = true. end cierra el bloque.
- Línea 16: Note over A,B pone una nota que abarca de la aplicación a la capa: la aplicación no hace UPDATE directo.

EJEMPLO: Pegado en mermaid.live dibuja cuatro columnas, las flechas en orden y un recuadro alt con sus dos compartimentos.

SI PREGUNTAN:
- «¿Puedo usar punto y coma dentro de un mensaje?» → No: en Mermaid el punto y coma corta la línea y el diagrama da error de sintaxis. Los dos puntos dentro del mensaje sí se aceptan.
- «¿Y si quiero un paso opcional, sin rama de error?» → Se usa opt … end, que dibuja una sola rama.

CUIDADO: Un diagrama que solo tiene el camino feliz no dice qué hace la aplicación cuando la base rechaza: la rama alt es la mitad importante.

PASA A LA SIGUIENTE: Un tema de la aplicación que afecta a la base: cómo se abren las conexiones.

### [Slide 14] El pool de conexiones: que es y por que se agota

QUÉ ES (dilo así): Un pool de conexiones es un conjunto de conexiones abiertas y autenticadas que la aplicación reutiliza. Existe por una asimetría: abrir una conexión es caro y ejecutar una consulta es barato.

CÓMO DARLA (≈4 min):
- Al entrar: Abrir y cerrar en cada consulta: saludo TCP, autenticación, creación de la sesión (en PostgreSQL, un proceso nuevo en el servidor por cada conexión) y memoria. Decenas de milisegundos de trámite contra 2 o 3 de trabajo: casi todo el tiempo de respuesta es protocolo. Los valores exactos se miden; la dirección de la desigualdad es la regla.
- Clic 1: El pool: diez conexiones ya abiertas que se prestan y se devuelven; tomar una prestada cuesta una fracción de milisegundo. No se maximiza: cada sesión consume memoria del servidor y más conexiones activas que núcleos de CPU solo alargan la cola. Unas diez para una aplicación de este tamaño es una convención, no una ley.
- Clic 2: La fuga: si una ruta del código no devuelve la conexión (faltó el finally o el try con recursos), se van perdiendo hasta que no queda ninguna y las peticiones esperan. El síntoma: funciona media hora y después no responde.

EJEMPLO: En Java: try (Connection c = ds.getConnection()) { … } devuelve la conexión al pool al salir del bloque, aunque haya una excepción; un getConnection() sin su close() en un finally es una fuga.

SI PREGUNTAN:
- «¿No es más lento llamar un procedimiento que consultar directo?» → Normalmente es más rápido: una llamada resuelve en el servidor lo que la aplicación haría en tres o cuatro viajes de red. En todo caso, se mide (Clase 8).
- «¿Cuántas conexiones aguanta PostgreSQL?» → Por omisión, max_connections es 100. Por eso cada aplicación usa un pool pequeño en vez de una conexión por usuario.

CUIDADO: No digas «el pool más grande es el más rápido»: pasado el número de núcleos, más conexiones solo agregan espera y memoria.

PASA A LA SIGUIENTE: ¿Cuánta lógica conviene poner en la base? Con honestidad.

### [Slide 15] Logica en la base o en la aplicacion: honestidad y no propaganda

QUÉ ES (dilo así): Poner lógica en la base tiene ventajas reales y costos reales, y el estudiante va a encontrar equipos que defienden lo contrario de lo que oye hoy. El criterio no es de gusto: depende de dónde cae el costo del error.

CÓMO DARLA (≈4 min):
- Al entrar: A favor de la base: la regla escrita una vez la cumplen todos los clientes, incluida la consola del administrador y el script de las once de la noche; queda en la misma transacción que los datos, sin ventana entre validar y escribir; y ahorra viajes de red. La balanza se inclina.
- Clic 1: En contra: PL/pgSQL es más difícil de probar de forma automática y de versionar, hay menos gente que lo domine, ata el proyecto al motor, y la CPU de la base es el recurso más caro de escalar (agregar servidores de aplicación es fácil; de base, no). La balanza se equilibra.
- Clic 2: El criterio: las reglas que protegen la integridad van en la base, porque no pueden depender de que todos los clientes se porten bien; en la clínica, que una mascota inactiva no agende, que el stock nunca quede negativo y que los cambios sensibles queden auditados. La orquestación, la presentación, los formatos y los correos van en la aplicación.

EJEMPLO: Enviar el recordatorio de la cita por correo va en la aplicación (un servicio externo no debe correr dentro de la transacción); impedir que se agende a Rocky, que está inactiva, va en la base.

SI PREGUNTAN:
- «Entonces, ¿cuál es mejor?» → Depende de dónde caiga el costo del error. Para datos que no se pueden reconstruir, ese costo cae del lado de la base.

CUIDADO: No hagas propaganda de un solo lado: si solo se dicen las ventajas, el estudiante no sabe defender la decisión cuando se la discutan.

PASA A LA SIGUIENTE: Último tema: cambiar el esquema sin romper la aplicación que ya corre.

### [Slide 16] Cambiar el esquema sin romper la aplicacion que ya corre

QUÉ ES (dilo así): Cambiar el esquema de una base que ya usa una aplicación no se hace de un golpe. Se agrega lo nuevo al lado de lo viejo, se migra por pasos y se borra lo viejo al final; en cada paso funcionan a la vez la versión vieja y la nueva de la aplicación.

CÓMO DARLA (≈6 min):
- Al entrar: El caso: registrar la fecha en que una mascota se inactivó. Fase 1, expandir: ALTER TABLE mascota ADD COLUMN fecha_inactivacion DATE; admite nulos, ningún procedimiento cambia y la aplicación vieja la ignora (visto). La nueva todavía no existe.
- Clic 1: Fase 2, escribir en ambos lados: sp_inactivar_mascota se actualiza para poner activa = 'N' y además llenar la fecha. Las dos versiones funcionan.
- Clic 2: Fase 3, rellenar el histórico: las mascotas que ya estaban inactivas reciben su fecha con UPDATE por lotes, nunca uno gigante que bloquee la tabla por minutos (los bloqueos de la Clase 10).
- Clic 3: Fase 4, mover las lecturas: reportes y pantallas pasan a leer la columna nueva.
- Clic 4: Fase 5, contraer: si la fecha reemplaza al indicador activa, activa se borra solo cuando ninguna versión desplegada la lee. La vieja queda retirada.
- Clic 5: La regla, y lo mismo con procedimientos: un parámetro nuevo al final con valor DEFAULT no rompe las llamadas existentes; cambiar el orden, el tipo o el significado de un error sí, y entonces se publica sp_agendar_cita_v2 y la anterior se conserva hasta que la aplicación migre.

EJEMPLO: Tras la fase 1, SELECT nombre, activa, fecha_inactivacion FROM mascota WHERE activa = 'N'; devuelve Rocky y Kiara con la fecha en NULL: eso es lo que la fase 3 rellena.

SI PREGUNTAN:
- «¿Por qué no un solo ALTER TABLE que cambie todo?» → Porque la aplicación que está corriendo espera el esquema viejo: en el instante del cambio, todo lo que la usa se rompe. Expandir primero deja funcionando las dos versiones.
- «¿Dónde se guardan estos cambios?» → En scripts de migración numerados en el repositorio, que no se editan después de aplicados: si algo quedó mal, se escribe el siguiente número.

CUIDADO: Agregar la columna como NOT NULL de entrada falla en una tabla con filas («column "fecha_inactivacion" of relation "mascota" contains null values»): por eso la fase 1 la agrega admitiendo nulos.

PASA A LA SIGUIENTE: Veamos en la demo la puerta, la inyección y el contrato.

### [Slide 17] Demo del dia

QUÉ ES (dilo así): La demo pone en pantalla las dos maneras de entrar a la base: la puerta equivocada, que deja que el dato se vuelva código, y la correcta, que solo acepta valores y responde con su contrato.

CÓMO DARLA (≈15 min):
- 1 · Concatenado: Ejecuta SELECT id_mascota, nombre FROM mascota WHERE nombre = '' OR 1=1 --' como si lo hubiera armado la aplicación: 8 filas. Muestra cómo quedó la cadena.
- 2 · Parámetro: PREPARE buscar_mascota (VARCHAR) AS SELECT id_mascota, nombre FROM mascota WHERE nombre = $1; y EXECUTE buscar_mascota(''' OR 1=1 --'): 0 filas. Repite con 'Luna': 1 fila (2 | Luna).
- 3 · Contrato: CALL sp_agendar_cita(3, 1, TIMESTAMP '2026-09-01 09:00:00'): aborta con «ERROR: la mascota 3 esta inactiva; no se agenda cita». SELECT COUNT(*) FROM cita antes y después: igual.
- 4 · Cierre: Pregunta: «¿qué privilegios necesita el rol de la aplicación para todo esto?». Respuesta: EXECUTE sobre las operaciones y SELECT de lectura; nada de INSERT directo.

EJEMPLO: Tiempos sugeridos: concatenado 4 min, parámetro 4 min, contrato 4 min, cierre 3 min.

SI PREGUNTAN:
- «¿Por qué se escribe la cadena a mano?» → Porque la base no tiene aplicación: escribir el texto que la aplicación habría armado muestra exactamente lo que recibiría el motor.

CUIDADO: Una comilla dentro de un texto SQL se escribe doblada (''). Si te equivocas en vivo, el error de sintaxis distrae del punto: lleva las sentencias preparadas.

PASA A LA SIGUIENTE: Para el diagrama del flujo: del boceto al código Mermaid.

### [Slide 18] Del boceto al código Mermaid

QUÉ ES (dilo así): El diagrama de secuencia se entrega como texto Mermaid, no como imagen: la imagen sale del código. Se piensa dibujando, se traduce a texto, se comprueba que dibuje y se guardan las dos cosas.

CÓMO DARLA (≈3 min):
- Paso 1: Diseña visual: en Excalidraw o draw.io se dibuja quién llama a quién, en orden de arriba abajo.
- Paso 2: Traduce con IA: pide el código sequenceDiagram a partir del boceto. Revisa el resultado: la IA acierta la sintaxis, no el flujo; los nombres de las operaciones tienen que ser los del contrato.
- Paso 3: Renderiza y corrige en un visor Mermaid (mermaid.live): si no dibuja, no comunica.
- Paso 4: Guarda el texto Mermaid, que es la fuente, y exporta el PNG.

EJEMPLO: El diagrama de la operación de cancelar, proyectado antes en la lámina del flujo en sequenceDiagram, es el modelo: participantes, ->> para la llamada, -->> para la respuesta y alt … else … end para la rama de error.

SI PREGUNTAN:
- «¿Por qué no basta una imagen del diagrama?» → Porque el texto se puede revisar, comparar con el contrato y versionar; una imagen no se corrige sin volver a dibujarla.

CUIDADO: El diagrama debe mostrar la rama de error: un flujo que solo tiene el camino feliz no dice qué hace la aplicación cuando la base rechaza.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Plantilla contrato sp_agendar_cita + storyboard 6 slides.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 12 · Integracion app <-> BD · Prep. presentacion
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Integrar no es conectarse: cual es la unica puerta de entrada
5. Inyeccion SQL: cuando el dato se interpreta como codigo
6. La inyeccion de SQL, explicada con las dos versiones
7. Por que el parametro lo evita por construccion
8. El contrato y sus seis partes
9. El contrato de la capa de API: siempre parametros ligados
10. El contrato que la app consume (no SQL suelto)
11. El manejo de errores entre capas: las tres reglas
12. El contrato como fila: ok, mensaje e id_generado
13. El flujo de la operacion en sequenceDiagram, con alt y else
14. El pool de conexiones: que es y por que se agota
15. Logica en la base o en la aplicacion: honestidad y no propaganda
16. Cambiar el esquema sin romper la aplicacion que ya corre
17. Demo del dia
18. Del boceto al código Mermaid
19. Cierre · Clase 12

> Privado, no se proyecta: `Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Integracion app <-> BD · Prep. presentacion.»
Proyectar [Slide 2] «Encuadre de hoy · Tema y objetivo» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde 
**Decir:** «Esto es lo que hay que saber del tema de hoy.»
Proyecte estas diapositivas, en este orden, ~25 min cada una. Son la teoria
completa del dia: **ninguna se salta**, porque el taller cobra puntos por lo que se
proyecta en todas ellas.


El desarrollo completo de cada una esta arriba, en «Fundamento teorico», dividido por
diapositiva: esa seccion esta escrita para dictarla sin consultar otra fuente.
Ideas que tienen que quedar dichas:
- Integrar app<->BD significa que la aplicacion NUNCA arma SQL dinamico contra las tablas directamente; llama procedimientos y funciones ya construidos (Clases 3-4). Esto evita SQL injection (nadie concatena texto de usuario dentro de una consulta), centraliza la regla de negocio en un solo lugar, y permite cambiar el esquema interno sin romper la app mientras el contrato del proc se mantenga igual.
- Un contrato de integracion documenta, por cada operacion: nombre del proc, parametros de entrada con su tipo, que retorna (valor OUT o codigo de resultado), y que errores puede lanzar y con que significado (ej. 'ERROR: mascota inactiva' vs una excepcion no controlada del motor). Sin este contrato, cualquier desarrollador que use la BD debe adivinar el comportamiento leyendo el codigo SQL directamente.
- Manejo de errores en la frontera app-BD: la app no deberia mostrar al usuario final un error crudo de base de datos (ej. 'ORA-00001: unique constraint violated'); el proc devuelve un mensaje o codigo de negocio legible, y la app lo traduce a un mensaje humano ('Ya existe una cita en ese horario').
- Autenticacion/autorizacion en este punto es conceptual, no de implementacion: la app se conecta con una cuenta de servicio que respeta los roles definidos en Clase 2 (principio de minimo privilegio) — la app de recepcion no deberia poder ejecutar procs reservados a auditoria o administracion.
- Preparar la sustentacion no es 'hacer diapositivas bonitas': es organizar la evidencia tecnica en una narrativa logica -> problema real que resuelve VetCare, modelo de datos (ER + normalizacion), seguridad (roles), automatizacion (procs/triggers), rendimiento (indices/optimizacion), y una demo en vivo que conecte todo eso con una operacion real (agendar una cita, facturar).
- Error de docente que no domina el tema: dejar que la 'integracion' quede como una idea abstracta sin contrato escrito — el entregable de hoy exige documentar minimo 3 operaciones con su firma completa, no solo mencionarlas de palabra.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 17][Slide 18]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Plantilla contrato sp_agendar_cita + storyboard 6 slides.
Herramienta: ExamLab (PostgreSQL/PGlite) + Excalidraw / Mermaid

**Cierre la demo dentro de ExamLab** [Slide 18] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 12 [[captura: cap01_demo.png | receta: 1) Abra ExamLab (PostgreSQL/PGlite) + Excalidraw / Mermaid y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 12/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 12 - Integracion y preparacion final/Taller PI - Clase 12 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Contrato integracion + preparacion de entrega/sustentacion
Actividades:
1. Redactar contrato de >=3 operaciones.
2. Diagrama flujo app->BD (Excalidraw) opcional.
3. Outline presentacion 5-8 min + quien habla que.
4. Empaquetar borrador entrega final.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Contrato app<->BD + outline de slides de sustentacion (5-8 min)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 12/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 12 - VetCare.docx`. Clave para usted: `Quiz Clase 12 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 19]
**Decir:** «Queda visto: Integracion app <-> BD · Prep. presentacion. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 19] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 12_contrato_ops.sql.

## Capturas
Carpeta `Kit docente/Clase 12/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
