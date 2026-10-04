# Guion docente · Clase 2 · Administracion de BD · Roles VetCare

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


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Los cuatro terminos que se confunden todo el tiempo** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Administrar una base de datos es decidir y hacer cumplir quien puede hacer que sobre cada objeto, y dejar rastro de quien lo hizo.
  - Antes de llegar a la sintaxis conviene fijar cuatro terminos que se usan sueltos y se confunden todo el tiempo.
  - Un objeto de base de datos es cualquier cosa que el motor guarda y a la que se le puede poner nombre: una tabla como cita, una vista, un procedimiento, una secuencia.
  - Un esquema es un contenedor con nombre donde viven esos objetos; en PostgreSQL, que es el motor de esta clase, el esquema por omision se llama public y el nombre completo de la tabla es public.cita.
  - Aqui hay que desactivar una confusion que traen quienes vieron Oracle: alli esquema y usuario son practicamente lo mismo y se escribe la clínica.MASCOTA
  - Mientras que en PostgreSQL son cosas separadas, un mismo usuario puede tener objetos en varios esquemas y un esquema puede contener objetos de varios propietarios.
  - Autenticacion es probar quien es usted, con usuario y clave o con un certificado.
  - Autorizacion es decidir que puede hacer una vez que ya esta dentro.
  - Son etapas distintas, se controlan con mecanismos distintos, y un usuario puede autenticarse perfectamente y no tener permiso para leer ni una sola fila.
  - Esta clase se dicta en sesion virtual sincrona, en el bloque normal de 120 minutos: hay explicacion en vivo.
  - NOTAS:
  - Conviene aprovechar precisamente eso, porque los permisos son el tema del curso donde el estudiante mas necesita que alguien le diga en el momento por que su GRANT no surtio efecto.
  - Fuera de la lamina (habla de la practica): Esta clase se dicta en sesion virtual sincrona, en el bloque normal de 120 minutos: hay explicacion en vivo, taller acompanado y espacio para preguntar, asi que este texto es el material con el que el docente dicta y no una lectura que sustituya la clase.

**[Slide 5] Privilegio: la unidad atomica, y la frontera DDL/DML** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un privilegio es un permiso atomico: la unidad mas pequena de autorizacion que el motor sabe otorgar o quitar.
  - En PostgreSQL hay que distinguir dos cosas que los estudiantes mezclan.
  - Los privilegios de objeto habilitan acciones sobre un objeto concreto y son los que se escriben con GRANT: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES y TRIGGER sobre una tabla o una vista
  - Los atributos de rol son otra cosa: LOGIN, CREATEDB, CREATEROLE y SUPERUSER no se otorgan con GRANT sino que se escriben en el CREATE ROLE o se cambian con ALTER ROLE, y son el equivalente de lo que en Oracle se llama privilegio de sistema.
  - DDL, Data Definition Language, son las sentencias que cambian la estructura: CREATE, ALTER, DROP, TRUNCATE.
  - DML, Data Manipulation Language, son las que leen o cambian los datos sin tocar la estructura: SELECT, INSERT, UPDATE, DELETE.
  - Un recepcionista de la clínica necesita DML sobre unas pocas tablas y nunca necesita DDL.
  - Ejemplo en la clínica: GRANT SELECT, INSERT ON cita TO recepcion permite leer y agendar, pero no UPDATE ni DELETE, y tampoco ALTER TABLE, porque modificar la estructura de un objeto no es un privilegio que se conceda con GRANT: lo puede hacer su dueno.
  - NOTAS:
  - EXECUTE sobre una funcion o un procedimiento
  - USAGE sobre un esquema o una secuencia
  - CONNECT y TEMPORARY sobre la base de datos.
  - Vale la pena decirlo porque el estudiante que busque en internet va a encontrar GRANT CREATE SESSION, que es sintaxis de Oracle y en PostgreSQL no existe.
  - La distincion practica que hay que dejar clara es la que separa DDL de DML.
  - Si su cuenta puede ejecutar DROP TABLE cita, un error de copiar y pegar borra la agenda completa, y ningun respaldo de la noche anterior devuelve las citas que se agendaron hoy.

**[Slide 6] Rol: por que existe, con la aritmetica en el tablero** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un rol es un paquete de privilegios con nombre propio, que se otorga a un usuario en un solo paso.
  - El modelo tiene ocho tablas (dueno, mascota, veterinario, cita, consulta, insumo, factura y detalle_factura) y, contando los dos procedimientos que llegaran en la Clase 3, diez objetos que hay que decidir.
  - Si la clinica tiene doce empleados y los permisos se otorgan cuenta por cuenta, el administrador escribe del orden de cientos de sentencias GRANT
  - Pero el problema grave no es el volumen: es que cuando cambie una regla, por ejemplo que recepcion ya no pueda anular facturas, tendra que recordar tocar doce cuentas sin olvidar ninguna.
  - Con roles se define una sola vez el conjunto de privilegios de recepcion y se ejecutan doce sentencias GRANT recepcion TO usuario.
  - Al cambiar la regla se hace un REVOKE sobre el rol y los doce usuarios quedan corregidos en el mismo instante, sin excepciones y sin listas de verificacion.
  - Ejemplo la clínica: cuando entra una recepcionista nueva, el alta es una sola sentencia que le otorga el rol recepcion; cuando se va, la baja es una sola sentencia que se lo revoca.
  - Ningun permiso se toca objeto por objeto: la matriz del rol sigue siendo la misma para las 12 cuentas.
  - NOTAS:
  - Existe por una razon aritmetica que conviene poner en el tablero con los numeros de la clínica.
  - Sobre cada uno hay hasta cinco acciones posibles, asi que la matriz completa tiene cincuenta celdas.
  - Ese es el argumento real que el docente debe transmitir: el rol no ahorra tipeo, ahorra olvidos, y los olvidos en materia de permisos son precisamente los que producen incidentes de seguridad.

**[Slide 7] En PostgreSQL usuario y rol son lo mismo, y por eso hoy se escribe NOLOGIN** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - CREATE USER no es un comando distinto, es un alias de CREATE ROLE...
  - Un rol con el atributo LOGIN es lo que llamamos usuario, porque puede iniciar sesion; un rol sin LOGIN es un paquete de permisos que nadie usa para conectarse.
  - Un segundo detalle, este de convencion y no de motor: el rol del veterinario se llama veterinario_rol y no veterinario.
  - Tecnicamente no hay ninguna obligacion, porque en PostgreSQL los roles son globales al cluster y las tablas viven en un esquema, de modo que un rol llamado veterinario y una tabla llamada veterinario pueden coexistir sin conflicto alguno.
  - La razon es de legibilidad para quien audita: en la linea GRANT SELECT ON cita TO veterinario no se puede saber a simple vista si veterinario es un rol o si alguien se equivoco de sintaxis, mientras que veterinario_rol se lee sin ambiguedad.
  - NOTAS:
  - Hay un detalle del motor que hay que decir temprano porque de lo contrario el tema se vuelve incomprensible: en PostgreSQL usuario y rol son la misma entidad.
  - Por eso los cuatro roles de la clase se crean con CREATE ROLE recepcion NOLOGIN: son bolsas de privilegios, no identidades.
  - La persona viene despues, como CREATE ROLE ana_gomez LOGIN PASSWORD '...', y recibe la bolsa con GRANT recepcion TO ana_gomez.
  - Esa herencia es la que hace que al modificar el rol se corrijan todas las personas a la vez.
  - Conviene decir esto tal cual, porque un estudiante despierto va a preguntar por que el sufijo y merece la respuesta correcta y no una inventada.

**[Slide 8] Crear el rol y otorgar solo lo que el cargo usa** — 11 vinetas.

**[Slide 9] Minimo privilegio aplicado a VetCare: la matriz defendible** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - No necesita leer consulta, porque el historial clinico es informacion sensible del paciente que la recepcion no requiere para hacer su trabajo.
  - El rol veterinario_rol necesita SELECT sobre cita y mascota, y SELECT, INSERT y UPDATE sobre consulta, porque es quien documenta la atencion.
  - El rol admin_bd es el unico con privilegios amplios, y es el que sostiene el DDL.
  - Notese que DELETE no aparece en ninguna fila operativa, y eso no es descuido: en un sistema clinico las cosas no se borran, se marcan.
  - Una cita cancelada lleva estado = 'CANCELADA' y una mascota que ya no se atiende lleva activa = 'N', que es exactamente como quedo el DDL de la Clase 1, con CHAR(1) y CHECK (activa IN ('S','N')).
  - NOTAS:
  - El principio de minimo privilegio dice que cada rol recibe exactamente lo que necesita para cumplir su funcion y ni un privilegio mas.
  - Aplicado a la clínica deja una matriz muy concreta y defendible.
  - El rol recepcion necesita SELECT sobre mascota, dueno y veterinario para poder buscar y agendar, y SELECT, INSERT y UPDATE sobre cita para agendar y reprogramar; nada mas.
  - El rol auditor recibe unicamente SELECT, y jamas una escritura.
  - Eso se llama borrado logico, y hace que el privilegio DELETE sea innecesario para casi todos los usuarios, lo que a su vez elimina de raiz la posibilidad de una perdida accidental de informacion.
  - Conviene escribir esos dos valores en el tablero, porque el estudiante que suponga activa = 0 escribira un UPDATE que el CHECK va a rechazar y perdera diez minutos buscando el error en otra parte.

**[Slide 10] Minimo privilegio, en concreto** — 9 vinetas.

**[Slide 11] Separacion de funciones: el ejemplo de la factura** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Separacion de funciones, o segregation of duties, es la practica de repartir un proceso sensible entre dos o mas personas para que ninguna pueda completarlo sola sin dejar rastro.
  - En terminos de base de datos significa que quien disena y modifica el esquema no debe ser la misma cuenta que opera los datos del dia a dia, y que quien audita solo debe leer.
  - El ejemplo de la clínica es facil de contar: si la misma cuenta que emite una factura puede tambien borrarla, entonces una persona puede cobrar en efectivo y hacer desaparecer el registro, y no queda evidencia de que la factura existio.
  - Separando funciones, emitir una factura es un INSERT permitido a un rol, y anular una factura es un UPDATE de estado permitido a un rol distinto, y ese UPDATE deja fecha, usuario y motivo.
  - Aqui aparece la primera pregunta previsible del estudiante: «no es mas facil darle todo al jefe y ya?».
  - En terminos de privilegios: recepcion puede INSERT en factura pero no UPDATE sobre un total ya emitido, y auditor solo tiene SELECT.
  - NOTAS:
  - La respuesta que el docente debe dar es que el problema no es la confianza en la persona sino el dano posible por un error o por una sesion robada.
  - Si alguien roba la sesion del recepcionista, con minimo privilegio el atacante ve agendas y datos de contacto; con privilegios de administrador, borra la base completa.
  - El permiso no mide cuanto se quiere a un empleado, mide cuanto se puede perder.
  - Ningun rol puede a la vez crear, modificar y aprobar el mismo registro.

**[Slide 12] GRANT y REVOKE: la sintaxis exacta que se va a escribir hoy** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La forma de las sentencias reales, que el estudiante debe poder escribir de memoria al terminar la lectura, es esta: CREATE ROLE recepcion NOLOGIN; luego GRANT SELECT, INSERT, UPDATE ON cita TO recepcion
  - Luego GRANT SELECT ON dueno, mascota, veterinario TO recepcion, aprovechando que PostgreSQL acepta varias tablas en un mismo GRANT; y finalmente GRANT recepcion TO ana_gomez.
  - Primero, un rol recien creado no tiene ningun privilegio sobre las tablas ajenas: no hace falta revocar nada para «empezar limpio», el punto de partida ya es cero.
  - Segundo, para que un rol pueda usar los objetos del esquema necesita USAGE sobre el esquema; en public eso viene concedido por omision, asi que hoy no estorba, pero en un servidor con esquemas propios es la causa numero uno del GRANT que «no surtio efecto».
  - Tercero, existe la forma masiva GRANT SELECT ON ALL TABLES IN SCHEMA public TO auditor, comoda y peligrosa a la vez: aplica a las tablas que existen en ese momento y no a las futuras
  - De modo que la tabla que se cree la semana entrante quedara fuera y nadie se dara cuenta; para eso existe ALTER DEFAULT PRIVILEGES, que vale nombrar sin desarrollar.
  - Error comun: creer que REVOKE de un privilegio que nunca se otorgo es un error: PostgreSQL lo ejecuta sin error y no cambia nada.
  - Tambien es comun olvidar que los privilegios concedidos a PUBLIC los recibe todo rol, incluido el que se acaba de restringir.
  - NOTAS:
  - GRANT otorga y REVOKE retira, y ambos operan igual sobre usuarios y sobre roles.
  - Para retirar un permiso
  - Hay tres detalles operativos que evitan la mitad de los tropiezos de la clase.
  - CÓDIGO CITADO (referencia):
  - REVOKE DELETE ON cita FROM recepcion
  - Fuera de la lamina (habla de la practica): Eso explica por que el REVOKE de DELETE que pide el taller es, tecnicamente, redundante; se escribe de todos modos porque es la evidencia documental de una decision de diseno, y quien revise el script tiene que poder ver que la ausencia de DELETE fue deliberada y no un olvido.

**[Slide 13] WITH GRANT OPTION y PUBLIC: los dos que hacen dano sin avisar** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La clausula WITH GRANT OPTION permite que quien recibio el privilegio lo vuelva a otorgar a otros; suena comodo y es una mala idea
  - Porque el administrador pierde el control de la cadena de permisos y, al hacer REVOKE, se produce una revocacion en cascada con efectos que nadie previo
  - De hecho PostgreSQL rechaza el REVOKE si hay privilegios dependientes y obliga a escribir CASCADE, que es el motor avisando que la operacion va a tocar mas de lo que se le pidio.
  - El segundo es el rol especial PUBLIC, al que pertenecen todos los roles existentes y futuros: un GRANT SELECT ON consulta TO PUBLIC entrega el historial clinico a cualquiera que pueda conectarse, incluido el proximo usuario que se cree manana.
  - Buscar y quitar privilegios otorgados a PUBLIC, con REVOKE ALL ON <tabla> FROM PUBLIC, es una tarea real de endurecimiento en bases de datos heredadas, y vale la pena nombrarla para que el estudiante entienda que estos conceptos no son escolares.
  - NOTAS:
  - Hay dos mecanismos que conviene conocer porque hacen dano en silencio.

**[Slide 14] REVOKE, y los dos que hacen dano en silencio** — 10 vinetas.

**[Slide 15] Cuando el GRANT es demasiado: vista y privilegio por columna** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un GRANT sobre una tabla es todo o nada en filas y columnas: quien tiene SELECT sobre dueno ve las seis columnas y las seis filas.
  - Hay dos mecanismos para recortar esa superficie y hay que saber cuando usar cada uno.
  - Una vista es una consulta guardada con nombre, que se usa como si fuera una tabla; se crea con CREATE VIEW v_agenda_recepcion AS SELECT... y se le otorga SELECT al rol.
  - La vista recorta las dos dimensiones a la vez: filas, con un WHERE estado <> 'CANCELADA', y columnas, con solo dejar el email fuera del SELECT.
  - El segundo mecanismo es el privilegio por columna: ON dueno TO veterinario_rol otorga lectura de dos columnas y de ninguna otra, sin crear ningun objeto nuevo.
  - El criterio para elegir es simple: si el recorte necesita filtrar filas o cruzar tablas, se hace con vista; si es puramente por columna y no se quiere mantener un objeto mas, con privilegio por columna.
  - NOTAS:
  - Aqui esta el concepto que hace la diferencia entre una matriz de aficionado y una defendible.
  - Pero la recepcionista solo necesita el nombre y el telefono para identificar a quien llama, y no tiene por que ver el correo electronico de los clientes.
  - El primero es la vista.
  - Lo que hace que funcione, y es el punto que el estudiante no cree hasta que lo ve, es que la consulta de la vista se ejecuta con los privilegios de su PROPIETARIO y no con los de quien la consulta: por eso se puede dar SELECT sobre la vista a recepcion y al mismo tiempo hacer REVOKE SELECT ON dueno FROM recepcion, y el rol sigue viendo el telefono del dueno a traves de la vista pero no puede consultar la tabla directamente.
  - Tiene una consecuencia que hay que advertir en clase porque genera un error confuso: ese rol ya no puede escribir SELECT * FROM dueno, porque el asterisco pide todas las columnas y dos de ellas le estan negadas; tiene que nombrar las columnas explicitamente.
  - CÓDIGO CITADO (referencia):
  - GRANT SELECT (id_dueno, nombre)
  - Fuera de la lamina (habla de la practica): Aqui esta el concepto que hace la diferencia entre una matriz de aficionado y una defendible, y es la parte que el taller evalua con veinte puntos.

**[Slide 16] Cuando el GRANT sobra: vista y privilegio por columna** — 13 vinetas.

**[Slide 17] Reducir la superficie: vista y privilegio por columna** — 12 vinetas.

**[Slide 18] La matriz como hecho verificable: information_schema** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Una matriz de permisos que solo existe en un documento es una intencion; la matriz se vuelve un hecho cuando se puede consultar en el motor.
  - PostgreSQL expone esa informacion en el esquema estandar information_schema y hay dos vistas que hay que saber usar.
  - La primera es role_table_grants, con ORDER BY grantee, table_name, privilege_type: devuelve una fila por cada combinacion de rol, tabla y privilegio realmente otorgado.
  - La segunda es column_privileges, que agrega la columna column_name y es la unica forma de evidenciar que el privilegio por columna quedo aplicado.
  - NOTAS:
  - Vale explicar por que se usa role_table_grants y no table_privileges, que es la que aparece primero al buscar: table_privileges solo muestra los privilegios en los que el usuario actual es quien otorga o quien recibe, mientras que role_table_grants incluye los de cualquier rol que este habilitado en la sesion, que es justamente lo que necesita el propietario para auditar lo que reparti.
  - CÓDIGO CITADO (referencia):
  - SELECT grantee, table_name, privilege_type FROM information_schema.role_table_grants WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')
  - Fuera de la lamina (habla de la practica): Estas dos consultas son la evidencia que la rubrica exige tres veces, y el docente deberia proyectar su salida en la demo: ver la matriz salir del motor, y no de un documento, es lo que convence al grupo de que los permisos son verificables.

**[Slide 19] La matriz como hecho verificable, no como documento** — 11 vinetas.

**[Slide 20] La politica de altas y bajas: el ciclo de vida de una cuenta** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La politica de altas y bajas documenta el ciclo de vida de una cuenta: quien autoriza que se cree, con que rol nace, que pasa cuando alguien cambia de funcion, y en cuanto tiempo se desactiva cuando se va de la clinica.
  - El plazo que se compromete habitualmente en la industria es el mismo dia del retiro, y por convencion se revisan las cuentas activas cada tres o seis meses; ninguno de esos dos numeros es una regla dura del motor, son practicas de gobierno
  - Y la politica vale precisamente porque fija responsables y plazos concretos en lugar de generalidades.
  - El problema que resuelve es la cuenta huerfana: la del pasante que se fue hace un ano y cuya clave sigue funcionando.
  - Una, nunca cuentas compartidas: si tres recepcionistas entran con la cuenta recepcion1, la tabla de auditoria dira que recepcion1 cancelo la cita y no habra forma de saber quien fue
  - La trazabilidad se pierde de manera irrecuperable y con ella cualquier investigacion posterior.
  - Dos, los permisos no se acumulan: al cambiar de rol se revoca el anterior con REVOKE recepcion FROM ana_gomez, porque quien pasa de recepcion a auditoria y conserva ambos roles termina pudiendo modificar justamente lo que audita.
  - La cuarta seccion, la revision periodica, se apoya en la consulta de information_schema que acaba de verse: la evidencia de la auditoria es su salida, y la politica dice cada cuanto se corre y quien la firma.
  - La quinta seccion es el limite de este entorno, y se desarrolla completa en «El motor de hoy es PostgreSQL» un poco mas abajo.
  - Al dictar la politica conviene bajarla a nombres propios de la clínica en lugar de dejarla en abstracto: quien autoriza el alta es la administradora de la clinica
  - La recepcionista que entra nace con el rol recepcion y con nada mas, y la baja del pasante se hace el mismo dia.
  - Una politica que no dice quien firma ni en cuanto tiempo no es una politica, es una intencion.
  - NOTAS:
  - Dos reglas la cierran.
  - Vale la pena senalar el detalle tecnico de la baja: en PostgreSQL no se puede hacer DROP ROLE de un rol que todavia posee objetos, hay que reasignarlos primero con REASSIGN OWNED BY ana_gomez TO admin_bd, y por eso la politica tiene que decir que pasa con lo que la persona era dueno.
  - Fuera de la lamina (habla de la practica): La diapositiva trae las cinco secciones en el mismo orden en que el taller las va a pedir, asi que se dicta recorriendola de arriba abajo.
  - Fuera de la lamina (habla de la practica): La quinta seccion es el limite de este entorno, y se desarrolla completa en «El motor de hoy es PostgreSQL» un poco mas abajo; lo que se califica ahi no es que la prueba negativa exista, sino que el estudiante sepa nombrarla como brecha de verificacion de su propia entrega.
  - Fuera de la lamina (habla de la practica): Una politica que no dice quien firma ni en cuanto tiempo no es una politica, es una intencion, y asi esta escrita la rubrica.

**[Slide 21] Ciclo de vida de una cuenta: alta, cambio, baja, revision** — 5 vinetas.

**[Slide 22] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El motor de la clase es PostgreSQL, que corre dentro del navegador.
  - Una, esas dos lineas TIENEN que fallar, asi que se ejecutan una por una: un runner que aborta al primer error se llevaria las siguientes.
  - Dos, si el entorno del dia no permite cambiar de rol, no hay que esconderlo — se muestra el mensaje.
  - La diferencia entre las dos cosas es justamente lo que el estudiante tiene que entender: SET ROLE cambia con que permisos se evalua lo que escribo
  - Y conectarse como otro usuario cambia quien esta conectado; para probar que un privilegio falta, basta lo primero.
  - Oracle Live SQL y DB Fiddle siguen en el kit, pero cambian de papel: DB Fiddle sirve para probar SQL suelto y Live SQL solo como contraste de sintaxis, porque alli se escribe CREATE USER...
  - IDENTIFIED BY, se otorga GRANT CREATE SESSION y el esquema es el usuario.
  - Vale un minuto de clase mencionarlo, porque muchos se van a encontrar Oracle en el trabajo; no vale mas, porque el motor de la clase es PostgreSQL y todo minuto invertido en sintaxis del otro motor es un minuto que no se dedica al tema.
  - NOTAS:
  - Ahi CREATE ROLE, GRANT, REVOKE, CREATE VIEW, los privilegios por columna y las consultas a information_schema funcionan todos: son DDL real y son verificables, asi que la evidencia de la clase es la salida del motor y no una promesa.
  - Lo que NO se puede hacer es abrir una segunda conexion: el entorno tiene un solo usuario con login y una sola sesion, asi que nadie va a conectarse como recepcion en otra pestana mientras el docente mira desde la suya.
  - Esa es la limitacion real, y hay que nombrarla con esa precision, porque la version anterior de esta guia decia algo mas fuerte y falso: que por eso la prueba negativa era imposible.
  - Para ver el permiso negado no hace falta otra conexion, hace falta cambiar el rol EFECTIVO dentro de la misma sesion, y eso es lo que hace SET ROLE recepcion; a partir de esa linea los privilegios que el motor revisa son los del rol y no los del propietario, de modo que devuelve permission denied for table cita y tambien, si ya se revoco el SELECT de la tabla.
  - Se cierra con RESET ROLE; y conviene no olvidarlo, porque todo lo que venga despues se seguiria ejecutando con los permisos recortados.
  - Dos advertencias para la demo.
  - CÓDIGO CITADO (referencia):
  - DELETE FROM cita WHERE id_cita = 1
  - SELECT nombre, email FROM dueno
  - Fuera de la lamina (habla de la practica): Este punto hay que decirlo con precision porque una version anterior de esta guia decia lo contrario y costaria puntos repetirla.
  - Fuera de la lamina (habla de la practica): Dos, si el entorno del dia no permite cambiar de rol, no hay que esconderlo — se muestra el mensaje, y entonces si aparece la brecha de verificacion que la pregunta 5 pide nombrar.

**[Slide 23] La matriz es la decision, no el script** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El script es la traduccion mecanica de una decision; la matriz es la decision.
  - Se construye con los objetos en las filas, los roles en las columnas, y en cada celda las acciones permitidas con la notacion abreviada: S para SELECT, I para INSERT, U para UPDATE, D para DELETE, E para EXECUTE y un guion cuando no hay ninguno.
  - Lo exigible para la clínica son los diez objetos por los cuatro roles, sin celdas vacias
  - Y la regla de calidad es que la matriz sea consistente con los GRANT que se ejecutaron en la primera pregunta: si el script no le dio DELETE a nadie, en la matriz no puede aparecer una D.
  - Los dos procedimientos van con E y nunca con S ni con I, y eso no es un detalle de notacion: es el patron que la Clase 3 va a construir y la Clase 12 va a usar, en el que la aplicacion no escribe en las tablas sino que invoca la regla de negocio.
  - Debajo de la matriz van cuatro a seis lineas justificando tres decisiones concretas, y ahi la regla es que una X sin texto no es una celda completa: «auditor sobre cita: solo S, porque auditar es verificar, no corregir» si lo es.
  - NOTAS:
  - Lo central no es el script sino la matriz rol por objeto por privilegio, y conviene explicar por que.

**[Slide 24] Como amarra con las clases vecinas y con la rubrica del PI** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Lo de hoy no es una isla.
  - La Clase 1 dejo el modelo y las claves primarias que hoy se protegen.
  - La Clase 3 introduce procedimientos almacenados y con ellos el patron mas fino de todos: no dar INSERT sobre cita al rol recepcion, sino EXECUTE sobre sp_agendar_cita, de modo que el usuario solo pueda escribir a traves de la regla de negocio.
  - La Clase 4 agrega disparadores de auditoria y el plan de respaldo.
  - Y la Clase 12 reutiliza estos roles para definir la cuenta de servicio con la que la aplicacion se conecta.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - «Ejecute el GRANT y no surtio efecto»: en el noventa por ciento de los casos es una de cuatro cosas.
  - Se otorgo al rol pero no se otorgo el rol a la persona, y falta el
  - O se esta probando en la misma sesion del propietario, que pasa por encima de todos los permisos y por lo tanto nunca ve un error, lo cual hace imposible «comprobar» nada asi.
  - O se escribio el nombre del rol distinto, y conviene recordar que PostgreSQL pasa los identificadores sin comillas a minusculas, de modo que RECEPCION y recepcion son el mismo rol, pero "Recepcion" entre comillas dobles es otro distinto.
  - «Si le doy SELECT solo a la vista, no necesita tambien SELECT sobre dueno?»: no, y es lo mas importante de la clase: la vista se ejecuta con los privilegios de su propietario.
  - «Puedo comprobar que a recepcion le rebota el DELETE?»: si, y no hace falta otra conexion: SET ROLE recepcion; luego el DELETE, que debe devolver permission denied, y RESET ROLE; para volver.
  - Si el navegador no permite el cambio de rol, se documenta el intento: ahi si hay una brecha de verificacion.
  - «Rol y usuario son lo mismo?»: en PostgreSQL si, un usuario es un rol con LOGIN.
  - «Por que auditor no tiene UPDATE ni sobre la tabla de auditoria?»: porque quien puede corregir el registro de lo que hizo puede borrar la evidencia de lo que hizo
  - Y entonces la auditoria no prueba nada; esa tabla llega en la Clase 4 y la respuesta se mantiene igual.
  - O el rol no tiene USAGE sobre el esquema.
  - Lo que no se puede es conectarse como recepcion en una segunda sesion, porque el entorno tiene un solo usuario con login.
  - Fuera de la lamina (habla de la practica): Lo de hoy no es una isla, y decirlo en voz alta le da sentido al entregable.
  - Fuera de la lamina (habla de la practica): La Clase 4 agrega disparadores de auditoria y el plan de respaldo, que son el otro componente de este mismo criterio de rubrica.
  - Fuera de la lamina (habla de la practica): En la rubrica del proyecto, seguridad y respaldo valen 15 de los 100 puntos.


**Demo que usted debe poder repetir:** Los 4 roles de VetCare con CREATE ROLE/GRANT/REVOKE en ExamLab, verificados con information_schema.role_table_grants.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 2 · Administracion de BD · Roles la clínica
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
16. Cuando el GRANT sobra: vista y privilegio por columna
17. Reducir la superficie: vista y privilegio por columna
18. La matriz como hecho verificable: information_schema
19. La matriz como hecho verificable, no como documento
20. La politica de altas y bajas: el ciclo de vida de una cuenta
21. Ciclo de vida de una cuenta: alta, cambio, baja, revision
22. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar
23. La matriz es la decision, no el script
24. Como amarra con las clases vecinas
25. Demo del dia
26. Cierre · Clase 2

> Privado, no se proyecta: `Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Administracion de BD · Roles VetCare.»
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
**Decir:** «Queda visto: Administracion de BD · Roles VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
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
