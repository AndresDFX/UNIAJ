# Guion docente · Clase 2 · Administracion de BD · Roles y privilegios

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Plan de roles/privilegios de VetCare
- **Entregable de hoy:** Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx
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

QUÉ ES (dilo así): Ayer la base guardaba datos; hoy decidimos quién puede hacer qué con ellos. Vamos a crear roles, darles solo los privilegios que su trabajo necesita, recortar lo que ven con vistas y privilegios por columna, y comprobar en el propio motor que un permiso que quitamos de verdad no está.

CÓMO DARLA (≈4 min):
- Al entrar: Pregunta de arranque: «si la recepcionista y el veterinario entran con la misma cuenta, ¿quién canceló la cita de ayer?». Deja que respondan 1-2 personas: nadie lo puede saber.
- Cierre del encuadre: «Hoy vamos a diseñar las cuentas de la clínica para que esa pregunta siempre tenga respuesta».

CUIDADO: Todo se hace en PostgreSQL. Si alguien trae sintaxis de Oracle (CREATE USER ... IDENTIFIED BY, GRANT CREATE SESSION), avisa desde ya que aquí no existe.

PASA A LA SIGUIENTE: El recorrido de las dos horas.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): Las dos horas en cinco tramos: encuadre, teoría con una lámina por concepto, demo en vivo, práctica opcional y cierre.

CÓMO DARLA (≈1 min):
- Al entrar: Señala los tramos sin detenerte. La práctica tiene su guía en la carpeta de la clase y es opcional.

PASA A LA SIGUIENTE: Antes de la sintaxis, cuatro palabras que se confunden todo el tiempo.

### [Slide 4] Los cuatro terminos que se confunden todo el tiempo

QUÉ ES (dilo así): Administrar una base de datos es decidir quién puede hacer qué sobre cada objeto, y dejar rastro de quién lo hizo. Para hablar de eso sin enredarse hacen falta cuatro palabras: objeto, esquema, privilegio y rol.

CÓMO DARLA (≈4 min):
- Al entrar: Los objetos: cita (tabla), v_agenda (vista), sp_agendar (procedimiento), seq_cita (secuencia). «Objeto es todo lo que el motor guarda con nombre».
- Clic 1: Aparece el esquema public que los contiene: el nombre completo de la tabla es public.cita.
- Clic 2: El privilegio: SELECT sobre cita. «Es la unidad más pequeña de permiso, siempre sobre un objeto concreto».
- Clic 3: El rol recepcion, que agrupa privilegios. Lee la frase final: quién puede hacer qué sobre cada objeto, y dejar rastro.

EJEMPLO: SELECT * FROM public.cita y SELECT * FROM cita son la misma consulta: el motor busca primero en public.

SI PREGUNTAN:
- «¿Autenticación y autorización no son lo mismo?» → No. Autenticación es probar quién eres (usuario y clave). Autorización es decidir qué puedes hacer ya dentro. Alguien puede entrar perfectamente y no tener permiso para leer una sola fila.
- «En Oracle el esquema era el usuario, ¿aquí también?» → No. En PostgreSQL esquema y usuario son cosas separadas: un esquema puede tener objetos de varios dueños.

CUIDADO: No digas «creo un privilegio» ni «le doy el rol a la tabla»: los privilegios ya vienen definidos por el motor; lo único que se crea son roles, y los privilegios se otorgan o se retiran.

PASA A LA SIGUIENTE: Miremos de cerca el privilegio y la frontera que más importa: DDL contra DML.

### [Slide 5] Privilegio: la unidad atomica, y la frontera DDL/DML

QUÉ ES (dilo así): Un privilegio es el permiso más pequeño que el motor otorga o quita. En PostgreSQL hay que separar dos cosas: los privilegios sobre objetos, que se dan con GRANT, y los atributos del rol, como LOGIN, que se escriben al crearlo. Y una frontera práctica: DDL cambia la estructura, DML lee o cambia datos.

CÓMO DARLA (≈3 min):
- Al entrar: Dos columnas. Izquierda, privilegios de objeto: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, que se otorgan con GRANT. Derecha, atributos de rol: LOGIN, CREATEDB, CREATEROLE, SUPERUSER, que van en CREATE ROLE o ALTER ROLE.
- Clic 1: La frontera: DDL (CREATE, ALTER, DROP, TRUNCATE) cambia la estructura; DML (SELECT, INSERT, UPDATE, DELETE) toca los datos. «Quien opera datos no necesita DDL».

EJEMPLO: Si la cuenta de recepción pudiera ejecutar DROP TABLE cita, un error de copiar y pegar borra la agenda completa, y ningún respaldo de anoche devuelve las citas agendadas hoy.

SI PREGUNTAN:
- «¿Cómo le doy permiso de ALTER TABLE a alguien?» → No existe como privilegio de GRANT: cambiar la estructura de una tabla lo puede hacer su dueño. Por eso el DDL queda en admin_bd.
- «Encontré GRANT CREATE SESSION en internet.» → Es de Oracle. En PostgreSQL poder conectarse es el atributo LOGIN del rol.

CUIDADO: TRUNCATE aparece en las dos listas: es un privilegio de tabla que se da con GRANT, y a la vez vacía la tabla entera; no se le da a ningún rol operativo.

PASA A LA SIGUIENTE: Dar privilegios uno por uno a cada persona no escala. Para eso existe el rol.

### [Slide 6] Rol: por que existe, con la aritmetica en el tablero

QUÉ ES (dilo así): Un rol existe por una razón aritmética. La clínica tiene diez objetos que proteger y doce empleados; dar permisos cuenta por cuenta son cientos de sentencias, y cuando cambia una regla hay que acordarse de tocar las doce. Con un rol se define el paquete una vez y se corrige en un solo lugar: el rol no ahorra tipeo, ahorra olvidos.

CÓMO DARLA (≈2 min):
- Al entrar: Cuenta por cuenta: doce personas, cada una con líneas hacia los diez objetos. «Un cambio de regla obliga a tocar doce cuentas sin olvidar ninguna».
- Clic 1: Con un rol: los mismos diez objetos, un solo rol recepcion, y doce GRANT recepcion TO usuario.
- Clic 2: El REVOKE sobre el rol corrige a los doce en el mismo instante.

EJEMPLO: Ocho tablas más dos procedimientos son diez objetos; con hasta cinco acciones por objeto, la matriz tiene 50 celdas por decidir. Cuando entra una recepcionista nueva, su alta es GRANT recepcion TO nueva_persona; cuando se va, REVOKE recepcion FROM nueva_persona.

SI PREGUNTAN:
- «¿Un usuario puede tener dos roles?» → Sí, y hereda la suma de los dos. Por eso al cambiar de función hay que revocar el rol anterior.

CUIDADO: Los olvidos en permisos son los que producen incidentes: ese es el argumento, no la comodidad.

PASA A LA SIGUIENTE: En PostgreSQL hay un detalle que lo cambia todo: usuario y rol son lo mismo.

### [Slide 7] En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN

QUÉ ES (dilo así): En PostgreSQL no hay usuarios por un lado y roles por otro: todo es un rol. Un rol con LOGIN puede conectarse y lo llamamos usuario; un rol sin LOGIN es una bolsa de permisos. Por eso los roles de cargo se crean NOLOGIN y la persona, con LOGIN, recibe la bolsa.

CÓMO DARLA (≈3 min):
- Al entrar: CREATE USER ana_gomez es lo mismo que CREATE ROLE ana_gomez LOGIN: un alias, el mismo objeto.
- Clic 1: Dos roles: recepcion NOLOGIN (nadie se conecta con él) y ana_gomez LOGIN (la persona). La flecha es GRANT recepcion TO ana_gomez: ella hereda todo lo del rol.
- Clic 2: La convención: veterinario_rol y no veterinario, porque en GRANT SELECT ON cita TO veterinario no se sabe a simple vista si es un rol o un error.

EJEMPLO: Si mañana recepción pierde un permiso, se hace un REVOKE sobre recepcion y ana_gomez, junto con las demás recepcionistas, lo pierde en el mismo instante.

SI PREGUNTAN:
- «¿Puede haber un rol y una tabla con el mismo nombre?» → Sí: los roles son globales al servidor y las tablas viven en un esquema, así que no chocan. El sufijo _rol es solo para leer mejor.

CUIDADO: Si el GRANT «no surte efecto», la causa más común es haberlo dado al rol y no haber dado el rol a la persona (falta GRANT recepcion TO ana_gomez).

PASA A LA SIGUIENTE: Así queda escrito, completo, para la recepción.

### [Slide 8] Crear el rol y otorgar solo lo que el cargo usa

QUÉ ES (dilo así): El código de hoy en su forma más corta: el rol de cargo sin login, la persona con login que lo recibe, y los privilegios exactos que necesita la recepción para agendar.

CÓMO DARLA (≈3 min):
- Líneas 1-2: CREATE ROLE recepcion NOLOGIN: el paquete. Nace con cero privilegios.
- Líneas 3-5: La persona: CREATE ROLE ana_gomez LOGIN PASSWORD y GRANT recepcion TO ana_gomez. La clave del ejemplo se cambia en producción.
- Líneas 7-9: SELECT, INSERT y UPDATE sobre cita para agendar, reprogramar y cancelar; solo SELECT sobre dueño, mascota y veterinario, en un único GRANT con tres tablas.
- Líneas 10-11: USAGE sobre la secuencia cita_id_cita_seq: el SERIAL de id_cita la usa en cada INSERT.

EJEMPLO: Sin la línea 10, el INSERT de una cita hecho como recepcion falla con «permission denied for sequence cita_id_cita_seq», aunque tenga INSERT sobre la tabla.

SI PREGUNTAN:
- «¿Por qué recepción no tiene DELETE?» → Porque cancelar no es borrar: es un UPDATE del estado a 'CANCELADA', y así la historia se conserva.
- «¿Y consulta?» → Nada: es el historial clínico, información sensible que la recepción no necesita para agendar.

CUIDADO: El error de la secuencia confunde porque el mensaje no menciona la tabla cita: léelo en voz alta si aparece.

PASA A LA SIGUIENTE: Ese «lo que el cargo usa» tiene nombre: mínimo privilegio.

### [Slide 9] Minimo privilegio aplicado a la clínica: la matriz defendible

QUÉ ES (dilo así): El principio de mínimo privilegio dice que cada rol recibe exactamente lo que necesita para su función y ni un privilegio más. Aplicado a la clínica deja una matriz concreta y defendible, y una consecuencia llamativa: nadie que opere datos tiene DELETE.

CÓMO DARLA (≈4 min):
- Al entrar: Fila de recepcion: S I U sobre cita, S sobre mascota y nada sobre consulta. «No lee el historial clínico porque su trabajo no lo requiere».
- Clic 1: Fila de veterinario_rol: S sobre cita y mascota, S I U sobre consulta, porque es quien documenta la atención.
- Clic 2: Fila de admin_bd: todo y además el DDL. Es el único con privilegios amplios.
- Clic 3: La conclusión: ningún rol operativo tiene DELETE. En la clínica las cosas se marcan: estado = 'CANCELADA', activa = 'N'.

EJEMPLO: El cuarto rol, auditor, recibe solo SELECT (sobre dueño, mascota, cita, consulta y factura) y jamás una escritura.

SI PREGUNTAN:
- «¿No es más fácil darle todo al jefe?» → El permiso no mide la confianza en la persona: mide cuánto se pierde si su sesión es robada o comete un error. Con mínimo privilegio, un atacante con la sesión de recepción ve agendas; con todo, borra la base.

CUIDADO: Escribe 'S' y 'N' en el tablero: quien asume activa = 0 escribe un UPDATE que el CHECK rechaza.

PASA A LA SIGUIENTE: El contraste en una sola lámina: lo que suele pasar y lo que pide el principio.

### [Slide 10] Minimo privilegio, en concreto

QUÉ ES (dilo así): Antes y después: la forma habitual de dar permisos en una empresa pequeña, y la que pide el mínimo privilegio.

CÓMO DARLA (≈1 min):
- Al entrar: Lee la columna izquierda como un diagnóstico: un admin compartido, GRANT ALL «para que no falle», nadie sabe quién borró qué, cuentas vivas de gente que ya se fue. Luego la derecha, punto por punto, como su remedio: cuatro roles, matriz por objeto, cancelar con UPDATE, baja el mismo día.

CUIDADO: GRANT ALL a todos «para que la práctica no se trabe» deja una matriz sin ninguna decisión que defender.

PASA A LA SIGUIENTE: Un paso más allá del mínimo privilegio: que nadie complete solo un proceso sensible.

### [Slide 11] Separacion de funciones: el ejemplo de la factura

QUÉ ES (dilo así): Separación de funciones es repartir un proceso sensible entre dos o más personas para que ninguna lo complete sola sin dejar rastro. En la base significa que quien diseña el esquema no es quien opera los datos, y que quien audita solo lee.

CÓMO DARLA (≈3 min):
- Al entrar: Una sola cuenta: INSERT de la factura (cobra) y DELETE de la factura (la borra). Queda sin evidencia de que existió.
- Clic 1: Funciones separadas: un rol emite con INSERT y otro anula con UPDATE del estado a 'ANULADA'. La factura sigue ahí, con fecha, usuario y motivo.
- Clic 2: La regla: nadie completa solo un proceso sensible.

EJEMPLO: Si alguien roba la sesión de recepción, con funciones separadas puede emitir una factura, pero no borrarla ni corregir su total.

SI PREGUNTAN:
- «¿Por qué el auditor no tiene UPDATE ni sobre la tabla de auditoría?» → Porque quien puede corregir el registro de lo que hizo puede borrar la evidencia, y entonces la auditoría no prueba nada.

CUIDADO: La tabla factura de los datos de práctica no tiene columna estado: la animación muestra el patrón. Si se quiere aplicar, primero se agrega la columna.

PASA A LA SIGUIENTE: Ya sabemos qué dar a quién. Ahora la sintaxis exacta.

### [Slide 12] GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy

QUÉ ES (dilo así): GRANT otorga y REVOKE retira, igual sobre roles que sobre personas. Son cuatro sentencias que hay que poder escribir de memoria: crear el rol, darle privilegios, dárselo a la persona y, si hace falta, retirar.

CÓMO DARLA (≈2 min):
- Al entrar: CREATE ROLE recepcion NOLOGIN: nace con cero privilegios.
- Clic 1: Dos GRANT: SELECT, INSERT, UPDATE sobre cita (varios privilegios en uno) y SELECT sobre dueno, mascota, veterinario (varias tablas en uno).
- Clic 2: GRANT recepcion TO ana_gomez: la persona recibe el paquete.
- Clic 3: REVOKE DELETE ON cita FROM recepcion: nunca se otorgó, así que no cambia nada ni falla; se escribe porque deja constancia de que la ausencia de DELETE fue una decisión y no un olvido.

EJEMPLO: GRANT SELECT ON ALL TABLES IN SCHEMA public TO auditor da SELECT sobre las tablas que existen hoy, no sobre las que se creen mañana; para esas existe ALTER DEFAULT PRIVILEGES.

SI PREGUNTAN:
- «¿Hace falta USAGE sobre el esquema?» → Sí, para usar sus objetos; en public viene concedido por omisión, por eso hoy no estorba. En un esquema propio es la causa número uno del GRANT que «no funciona».

CUIDADO: Probar los permisos con la cuenta dueña de las tablas no demuestra nada: el dueño pasa por encima de todo y nunca ve un error.

PASA A LA SIGUIENTE: Hay dos formas de dar permisos que hacen daño sin avisar.

### [Slide 13] WITH GRANT OPTION y PUBLIC: los dos que hacen dano sin avisar

QUÉ ES (dilo así): Dos mecanismos que hacen daño en silencio. WITH GRANT OPTION permite que quien recibió un privilegio lo vuelva a dar, y el administrador pierde el control de quién tiene qué. PUBLIC es un rol especial al que pertenecen todos, incluso los que se creen mañana.

CÓMO DARLA (≈3 min):
- Al entrar: La cadena: admin da con GRANT OPTION a rol_a, rol_a se lo da a rol_b, rol_b a rol_c. «El admin ya no sabe quién tiene el privilegio».
- Clic 1: REVOKE ... FROM rol_a CASCADE: sin CASCADE el motor lo rechaza porque hay privilegios que dependen de ese; con CASCADE se van todos los de la cadena.
- Clic 2: PUBLIC: GRANT SELECT ON consulta TO PUBLIC le entrega el historial clínico a cualquiera que se conecte, incluido el usuario que se cree mañana.
- Clic 3: La limpieza: REVOKE ALL ON consulta FROM PUBLIC. Es una tarea real de endurecimiento en bases heredadas.

EJEMPLO: El mensaje real al revocar sin CASCADE es «dependent privileges exist», con la pista «Use CASCADE to revoke them too».

SI PREGUNTAN:
- «Si revoco un permiso a recepcion, ¿por qué ese rol todavía puede leer?» → Revisa si el privilegio está concedido a PUBLIC: lo que recibe PUBLIC lo recibe todo rol, también el que se acaba de restringir.

PASA A LA SIGUIENTE: Las dos cosas en código, con la REVOKE de la matriz.

### [Slide 14] REVOKE, y los dos que hacen dano en silencio

QUÉ ES (dilo así): Tres REVOKE con propósitos distintos: dejar escrita una decisión, limpiar PUBLIC y deshacer una cadena de reotorgamientos.

CÓMO DARLA (≈2 min):
- Línea 1: REVOKE DELETE ON cita FROM recepcion: redundante a propósito; es la evidencia de que recepción no borra.
- Líneas 3-4: REVOKE ALL ON consulta FROM PUBLIC: nadie lee el historial por ser «todo el mundo».
- Líneas 6-10: GRANT ... WITH GRANT OPTION al auditor, y cómo se le quita solo la opción de reotorgar: REVOKE GRANT OPTION FOR SELECT ... CASCADE. El auditor conserva su SELECT; lo que él concedió desaparece.

EJEMPLO: Si el auditor alcanzó a dar SELECT sobre cita a veterinario_rol, el REVOKE sin CASCADE responde «dependent privileges exist»; con CASCADE, veterinario_rol pierde ese SELECT y el auditor queda con el suyo, sin opción de reotorgar.

SI PREGUNTAN:
- «¿Qué diferencia hay entre REVOKE SELECT y REVOKE GRANT OPTION FOR SELECT?» → El primero le quita el privilegio; el segundo solo le quita la capacidad de darlo a otros.

CUIDADO: REVOKE SELECT ON cita FROM auditor CASCADE también le quita su propio SELECT, y el auditor necesita leer citas.

PASA A LA SIGUIENTE: A veces el GRANT sobre la tabla entera es demasiado.

### [Slide 15] Cuando el GRANT es demasiado: vista y privilegio por columna

QUÉ ES (dilo así): Un GRANT sobre una tabla entrega todas sus filas y columnas. La recepcionista solo necesita el nombre y el teléfono de quien llama, no su correo. Hay dos formas de recortar: una vista, que recorta filas y columnas, y el privilegio por columna, que recorta solo columnas.

CÓMO DARLA (≈4 min):
- Al entrar: La tabla entera: todas las filas, incluida la CANCELADA, y todas las columnas, incluido el email.
- Clic 1: La vista: deja fuera las filas canceladas (WHERE estado <> 'CANCELADA') y la columna email (no está en su SELECT).
- Clic 2: El privilegio por columna: GRANT SELECT (id_dueno, nombre) da solo esas dos columnas. La regla de abajo: ¿filtra filas o cruza tablas? vista; ¿solo columnas? privilegio por columna.

EJEMPLO: La tabla dueno tiene cinco columnas (id_dueno, nombre, telefono, email, ciudad) y seis filas: con SELECT sobre la tabla se ven las 30 celdas.

SI PREGUNTAN:
- «Si le doy SELECT solo a la vista, ¿no necesita también SELECT sobre dueno?» → No, y es lo más importante de la clase: la vista se ejecuta con los privilegios de su propietario. Por eso se puede revocar la tabla y dejar la vista.

CUIDADO: Con privilegio por columna, SELECT * falla: el asterisco pide también las columnas negadas. Hay que nombrar las columnas.

PASA A LA SIGUIENTE: Las dos formas, escritas.

### [Slide 16] Reducir la superficie: vista y privilegio por columna

QUÉ ES (dilo así): Los dos mecanismos en código: la vista de agenda para recepción, con la tabla revocada, y el privilegio por columna para el veterinario.

CÓMO DARLA (≈3 min):
- Líneas 1-6: CREATE VIEW v_agenda_recepcion: id_cita, fecha_hora, el nombre del dueño y su teléfono, uniendo cita, mascota y dueño, sin las canceladas. El email no está.
- Líneas 7-8: GRANT SELECT sobre la vista y REVOKE SELECT ON dueno: recepción llega al dueño solo a través de la vista.
- Línea 11: GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol: dos columnas de la tabla y ninguna otra.

EJEMPLO: Con los datos de práctica la vista devuelve 9 filas: las 10 citas menos la que está CANCELADA.

SI PREGUNTAN:
- «¿Por qué no hacer otra vista también para el veterinario?» → Se podría. Si el recorte es solo de columnas y no se quiere mantener un objeto más, el privilegio por columna es más simple.

CUIDADO: Si la vista se crea con una cuenta que no puede leer dueno, falla al consultarla: corre con los privilegios de quien la creó.

PASA A LA SIGUIENTE: ¿Cómo sabemos que todo esto quedó así? Se le pregunta al motor.

### [Slide 17] La matriz como hecho verificable: information_schema

QUÉ ES (dilo así): Lo que dice un documento es lo que creemos haber dado; lo que dice el motor es lo que de verdad quedó. PostgreSQL lo expone en information_schema con dos vistas: role_table_grants y column_privileges.

CÓMO DARLA (≈2 min):
- Al entrar: Documento contra motor: «una matriz escrita es una intención; consultada, es un hecho».
- Clic 1: La consulta a role_table_grants y su salida: una fila por rol, tabla y privilegio (recepcion · cita · INSERT, SELECT, UPDATE…).
- Clic 2: column_privileges agrega la columna: es la única que muestra el privilegio por columna.

EJEMPLO: Si la matriz dice que nadie tiene DELETE, en role_table_grants no debe aparecer ninguna fila con privilege_type = 'DELETE' para los roles operativos.

SI PREGUNTAN:
- «¿Por qué role_table_grants y no table_privileges?» → Para el propietario que audita devuelven lo mismo; la única diferencia es que role_table_grants omite lo que se ve solo por un GRANT a PUBLIC. Se usa por convención del curso.

PASA A LA SIGUIENTE: Las dos consultas completas.

### [Slide 18] La matriz como hecho verificable, no como documento

QUÉ ES (dilo así): Las dos consultas de auditoría: la matriz de privilegios por tabla para los cuatro roles y, aparte, los privilegios por columna.

CÓMO DARLA (≈2 min):
- Líneas 2-5: role_table_grants filtrada por los cuatro roles y ordenada por rol, tabla y privilegio: así se lee como la matriz.
- Líneas 7-11: column_privileges para veterinario_rol sobre dueno: debe devolver exactamente dos filas, id_dueno y nombre.

EJEMPLO: Después de la lámina anterior, recepcion aparece con INSERT, SELECT y UPDATE sobre cita, SELECT sobre mascota y veterinario, y SELECT sobre v_agenda_recepcion; ya no aparece SELECT sobre dueno.

SI PREGUNTAN:
- «Me salieron cinco filas en column_privileges, con email y teléfono.» → Entonces se otorgó la tabla completa: column_privileges muestra también los privilegios de tabla repartidos por columna.

CUIDADO: role_table_grants no muestra los privilegios por columna: si solo se corre la primera consulta, el recorte del veterinario parece no existir.

PASA A LA SIGUIENTE: La matriz cambia cuando cambian las personas: la política de altas y bajas.

### [Slide 19] La politica de altas y bajas: el ciclo de vida de una cuenta

QUÉ ES (dilo así): La política de altas y bajas documenta el ciclo de vida de una cuenta: quién autoriza que se cree, con qué rol nace, qué pasa cuando alguien cambia de función y en cuánto tiempo se desactiva cuando se va. Vale porque fija responsables y plazos, no generalidades.

CÓMO DARLA (≈2 min):
- Al entrar: La línea de tiempo: alta (quién autoriza y con qué rol), cambio de función (se revoca un rol y se otorga otro), baja (el mismo día), y debajo la revisión de cuentas activas cada 3 a 6 meses.
- Clic 1: Los dos riesgos que cierra: la cuenta huérfana del pasante que se fue hace un año, y la cuenta compartida que deja a la auditoría sin saber quién fue.
- Clic 2: La frase final: una política sin responsables ni plazos es solo una intención.

EJEMPLO: En la clínica: el alta la autoriza la administradora; la recepcionista nueva nace con el rol recepcion y nada más; la baja del pasante se hace el día de su salida.

CUIDADO: El mismo día y cada 3 a 6 meses son prácticas de gobierno, no reglas del motor: dilo así.

PASA A LA SIGUIENTE: Cada fase del ciclo es una sentencia concreta.

### [Slide 20] Ciclo de vida de una cuenta: alta, cambio, baja, revision

QUÉ ES (dilo así): Cada fase del ciclo de vida se ejecuta con una sentencia: un GRANT o un REVOKE. La política le pone responsable y plazo a cada una, y termina con una prueba: comprobar en el motor que el permiso retirado de verdad no está.

CÓMO DARLA (≈3 min):
- Al entrar: Recorre las cinco tarjetas con su código. Alta: CREATE ROLE ... LOGIN y GRANT recepcion. Cambio: GRANT del rol nuevo y REVOKE del anterior. Baja: REVOKE y ALTER ROLE ... NOLOGIN. Revisión: la consulta a role_table_grants, cada 3 a 6 meses, firmada por alguien. Prueba: SET ROLE recepcion y un DELETE que debe fallar. Cierra con el recuadro: antes de DROP ROLE, REASSIGN OWNED.

EJEMPLO: Si ana_gomez creó una tabla, DROP ROLE ana_gomez falla con «role "ana_gomez" cannot be dropped because some objects depend on it»; primero REASSIGN OWNED BY ana_gomez TO admin_bd.

SI PREGUNTAN:
- «¿Por qué no basta con borrar la cuenta?» → Porque PostgreSQL no deja borrar un rol que todavía es dueño de objetos, y porque la traza de auditoría debe seguir diciendo quién hizo qué.

CUIDADO: Quien pasa de recepción a auditoría y conserva los dos roles termina auditando lo que él mismo modifica: el REVOKE del rol anterior es la mitad importante del cambio.

PASA A LA SIGUIENTE: Esa prueba final depende de lo que este motor permite hacer.

### [Slide 21] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar

QUÉ ES (dilo así): El motor de la clase es PostgreSQL corriendo en el navegador. Ahí funciona todo lo de hoy, con una sola limitación real: hay una sesión y un usuario con login, así que no se puede abrir otra conexión como recepcion. Para probar un permiso no hace falta: SET ROLE cambia el rol con el que el motor evalúa lo que escribimos.

CÓMO DARLA (≈3 min):
- Al entrar: SET ROLE recepcion: desde esa línea los permisos son los de recepcion. SELECT * FROM cita funciona, porque tiene SELECT.
- Clic 1: SELECT * FROM consulta falla con permission denied, y el DELETE sobre cita también: lo que el rol no tiene, el motor lo niega.
- Clic 2: RESET ROLE devuelve al rol propio. La regla del recuadro: cada línea que debe fallar se ejecuta sola, porque un ejecutor que aborta al primer error se lleva las siguientes.

EJEMPLO: SET ROLE recepcion; DELETE FROM cita WHERE id_cita = 1; responde «permission denied for table cita».

SI PREGUNTAN:
- «¿SET ROLE es lo mismo que conectarse como recepcion?» → No. SET ROLE cambia con qué permisos se evalúa lo que escribo; conectarse cambia quién está conectado. Para probar que un privilegio falta, basta lo primero; lo que no se prueba aquí es el login ni dos personas a la vez.

CUIDADO: Si olvidas RESET ROLE, todo lo que sigue corre con los permisos recortados y parece que «se dañó la base».

PASA A LA SIGUIENTE: La prueba completa, sobre la vista y el privilegio por columna.

### [Slide 22] SET ROLE: demostrar en el motor que el permiso falta

QUÉ ES (dilo así): La prueba de que el recorte funciona: como recepcion se ve la agenda por la vista y se niegan el DELETE y la tabla dueño; como veterinario_rol se leen solo las dos columnas concedidas.

CÓMO DARLA (≈2 min):
- Líneas 1-3: SET ROLE recepcion y la vista: 9 filas, sin la cita cancelada.
- Líneas 4-7: DELETE sobre cita y SELECT sobre dueño: las dos responden permission denied, con el nombre de la tabla.
- Línea 8: RESET ROLE: de vuelta al rol propio.
- Líneas 10-14: Como veterinario_rol: SELECT id_dueno, nombre devuelve las 6 filas; SELECT * falla porque el asterisco pide columnas que no tiene.

EJEMPLO: Recepción ve el teléfono del dueño en la vista aunque no pueda leer la tabla dueno: la vista corre con los privilegios de su propietario.

SI PREGUNTAN:
- «¿Por qué ejecutar las líneas una por una?» → Porque las que fallan a propósito abortan un script de una sola corrida, y las siguientes no se ejecutarían.

CUIDADO: Este bloque supone que ya se corrió el de «Reducir la superficie»: sin la vista, la línea 3 falla por otra razón (la vista no existe).

PASA A LA SIGUIENTE: Con todo verificado, la decisión se escribe en una matriz.

### [Slide 23] La matriz es la decision, no el script

QUÉ ES (dilo así): Lo central no es el script sino la matriz rol por objeto. El script es la traducción mecánica de una decisión; la matriz es la decisión, y debajo de ella van las razones.

CÓMO DARLA (≈2 min):
- Al entrar: La matriz: objetos en filas, roles en columnas y en cada celda las letras. Lee la leyenda: S SELECT, I INSERT, U UPDATE, D DELETE, E EXECUTE, guion ninguno.
- Clic 1: Se resalta la fila del procedimiento: va con E, nunca con S ni con I. «La aplicación invoca la regla de negocio; no escribe en la tabla».
- Clic 2: Las dos reglas de calidad: sin celdas vacías, y coherente con los GRANT ejecutados.

EJEMPLO: Una celda bien justificada: «auditor sobre cita: solo S, porque auditar es verificar, no corregir». Una X sin texto no es una decisión.

SI PREGUNTAN:
- «¿Por qué E para un procedimiento que todavía no existe?» → Porque la matriz decide el diseño: en la Clase 3 recepción agendará a través de sp_agendar_cita en lugar de insertar en cita.

PASA A LA SIGUIENTE: Cómo se conecta lo de hoy con las clases vecinas.

### [Slide 24] Como amarra con las clases vecinas

QUÉ ES (dilo así): Lo de hoy no es una isla: protege lo que dejó la Clase 1 y es la base de tres clases que vienen.

CÓMO DARLA (≈1 min):
- Al entrar: Recorre la imagen: la Clase 1 llega con tablas y claves; hoy se les ponen roles; la 3 cambia el INSERT de recepción por EXECUTE sobre un procedimiento; la 4 usa current_user en la auditoría y respalda los roles; la 12 crea la cuenta con la que se conecta la aplicación.

CUIDADO: Si todos comparten una cuenta, la auditoría de la Clase 4 registrará siempre el mismo nombre y no servirá para nada.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 25] Demo del dia

QUÉ ES (dilo así): La demo junta lo de hoy: los cuatro roles con su matriz, la vista y el privilegio por columna, la prueba negativa con SET ROLE y la verificación en information_schema.

CÓMO DARLA (≈15 min):
- Al entrar: 1) CREATE ROLE de admin_bd, recepcion, veterinario_rol y auditor, todos NOLOGIN, y los GRANT de la matriz con el REVOKE de DELETE (5 min). 2) La vista v_agenda_recepcion, el REVOKE de dueño y el GRANT por columna al veterinario (4 min). 3) SET ROLE recepcion; el DELETE, una línea sola, y lee el mensaje; RESET ROLE (3 min). 4) Las dos consultas de information_schema y compáralas con la matriz en voz alta (3 min).

CUIDADO: Ejecuta las líneas que deben fallar una por una, y no olvides RESET ROLE antes de las consultas de verificación.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Los 4 roles de VetCare con CREATE ROLE/GRANT/REVOKE en ExamLab, verificados con information_schema.role_table_grants.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 2 · Administracion de BD · Roles y privilegios
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Los cuatro terminos que se confunden todo el tiempo
5. Privilegio: la unidad atomica, y la frontera DDL/DML
6. Rol: por que existe, con la aritmetica en el tablero
7. En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN
8. Crear el rol y otorgar solo lo que el cargo usa
9. Minimo privilegio aplicado a la clínica: la matriz defendible
10. Minimo privilegio, en concreto
11. Separacion de funciones: el ejemplo de la factura
12. GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy
13. WITH GRANT OPTION y PUBLIC: los dos que hacen dano sin avisar
14. REVOKE, y los dos que hacen dano en silencio
15. Cuando el GRANT es demasiado: vista y privilegio por columna
16. Reducir la superficie: vista y privilegio por columna
17. La matriz como hecho verificable: information_schema
18. La matriz como hecho verificable, no como documento
19. La politica de altas y bajas: el ciclo de vida de una cuenta
20. Ciclo de vida de una cuenta: alta, cambio, baja, revision
21. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar
22. SET ROLE: demostrar en el motor que el permiso falta
23. La matriz es la decision, no el script
24. Como amarra con las clases vecinas
25. Demo del dia
26. Cierre · Clase 2

> Privado, no se proyecta: `Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Administracion de BD · Roles y privilegios.»
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
- Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. recepcion), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto). En PostgreSQL usuario y rol son la misma cosa: un usuario es un rol con LOGIN.
- Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.
- Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.
- GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol recepcion) y modificar en un solo lugar en vez de uno por uno.
- Un GRANT no es todo-o-nada: se puede recortar la superficie con una vista (CREATE VIEW deja fuera filas y columnas) o con privilegios por columna (GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol). Asi el rol llega al dato que necesita sin ver el resto de la tabla.
- Un permiso no vale nada sin evidencia: information_schema.role_table_grants y information_schema.column_privileges son las dos consultas que prueban que la matriz quedo como se decidio. Sin ellas la matriz es una intencion, no un hecho verificable.
- Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar ALL PRIVILEGES a todo el mundo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 25]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Los 4 roles de VetCare con CREATE ROLE/GRANT/REVOKE en ExamLab, verificados con information_schema.role_table_grants.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 Salida esperada de la demo de la Clase 2 [[captura: cap01_demo.png | receta: 1) Abra ExamLab (PostgreSQL) + Google Docs y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 2/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 2 - Administracion de bases de datos/Taller PI - Clase 2 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Plan de roles/privilegios de VetCare
Actividades:
1. Crear los 4 roles (admin_bd, recepcion, veterinario_rol, auditor) con GRANT/REVOKE que corran.
2. Recortar la superficie: vista v_agenda_recepcion + privilegio por columna sobre dueno.
3. Matriz rol x objeto x privilegio de los 10 objetos, justificando privilegio minimo.
4. Redactar 1 pagina: politica de altas/bajas de usuarios, con la prueba negativa (SET ROLE) corrida y su mensaje de error.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 2/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 2 - VetCare.docx`. Clave para usted: `Quiz Clase 2 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 26]
**Decir:** «Queda visto: Administracion de BD · Roles y privilegios. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 26] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 02_roles_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 2/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
