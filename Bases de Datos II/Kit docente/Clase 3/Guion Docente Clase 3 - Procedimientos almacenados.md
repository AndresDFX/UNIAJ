# Guion docente · Clase 3 · Procedimientos almacenados · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
- **Entregable de hoy:** 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx
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

**[Slide 4] Que es un procedimiento almacenado, y las dos palabras que importan** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un procedimiento almacenado es un bloque de codigo con nombre propio que vive dentro de la base de datos, y las dos palabras que hay que desempacar son guardado e invocado, porque son las que lo separan de un archivo sql en el computador de alguien.
  - Guardado significa que el fuente queda en el catalogo del motor y se puede recuperar sin depender de que su autor siga en el proyecto: en PostgreSQL, SELECT prosrc FROM pg_proc WHERE proname = 'sp_agendar_cita' devuelve el cuerpo
  - Y SELECT pg_get_functiondef('sp_agendar_cita'::regproc) devuelve la definicion completa lista para volver a ejecutar.
  - Consecuencia practica: si el estudiante cierra la pestana, el procedimiento no se perdio, esta en el motor.
  - Invocado significa que hay una sola linea que dispara varias sentencias:.
  - Y hay algo mas importante que el ahorro: la regla queda escrita UNA vez y ninguna pantalla puede saltarsela.
  - La Clase 1 dejo el esquema y la Clase 2 la matriz de roles; esta clase es donde la base de datos deja de ser un almacen pasivo y empieza a contener comportamiento.
  - En PostgreSQL no existe ese estado intermedio: el CREATE PROCEDURE valida la SINTAXIS del cuerpo y, si esta bien escrito, el objeto queda creado y valido, pero las tablas y columnas que el cuerpo menciona NO se verifican hasta la primera ejecucion.
  - La consecuencia practica es concreta y hay que anticiparla: un procedimiento que escribe INSERT INTO citas en lugar de cita se crea sin una sola queja y falla la primera vez que se lo llama.
  - NOTAS:
  - En lugar de enviar cuatro sentencias y esperar cuatro respuestas por la red, la aplicacion envia una y recibe un resultado.
  - Conviene senalar de entrada una diferencia con Oracle que importa hoy, porque cambia como se depura.
  - En Oracle el procedimiento se compila al crearlo y, si algo esta mal, el objeto queda creado pero invalido.
  - Por eso la regla del dia es que crear el procedimiento no es evidencia de nada; la evidencia es el CALL corriendo.
  - CÓDIGO CITADO (referencia):
  - CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00')

**[Slide 5] Por que un procedimiento y no SQL en cada pantalla** — 9 vinetas.

**[Slide 6] El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Se escribe LANGUAGE plpgsql AS $proc$ DECLARE...
  - AS introduce el cuerpo, y aqui esta la trampa de sintaxis mas comun para quien viene de Oracle: alla se escribe IS, aqui IS no existe en este lugar.
  - Los delimitadores $proc$ son lo que se llama dollar-quoting y existen por una razon mecanica: el cuerpo es, para el motor, una cadena de texto
  - Y esa cadena contiene punto y coma y comillas simples; si se delimitara con comillas habria que duplicar cada comilla interna.
  - Con $proc$ el motor sabe que todo lo que hay hasta el siguiente $proc$ es el cuerpo.
  - La etiqueta entre los dolares es arbitraria: $$ funciona igual, y se usa una etiqueta con nombre cuando hay bloques anidados.
  - El punto y coma final despues del ultimo $proc$ si es obligatorio, y en cambio la barra sola en una linea, que en Oracle cierra el bloque, aqui es un error de sintaxis.
  - Los nombres de los tipos son la otra mitad de la lista: INT, NUMERIC, TEXT, VARCHAR(n), TIMESTAMP, BOOLEAN, DATE.
  - VARCHAR2 y NUMBER no existen en PostgreSQL.
  - Y hay un detalle del proyecto que vale mas que la sintaxis: el procedimiento recibe TRES parametros y no cuatro, porque id_cita es SERIAL, es decir el motor genera el valor.
  - Pasarle el identificador desde afuera obliga a la aplicacion a saber cual sigue, que es exactamente el problema que la columna SERIAL resuelve.
  - NOTAS:
  - El molde es fijo y conviene dictarlo entero antes de escribir una sola validacion.
  - END; $proc$; y cada pieza tiene su razon.
  - LANGUAGE plpgsql hace falta porque PostgreSQL admite varios lenguajes procedimentales y no adivina cual se esta usando.
  - Un estudiante que agregue p_id_cita no comete un error de sintaxis, comete un error de diseno.
  - CÓDIGO CITADO (referencia):
  - CREATE OR REPLACE PROCEDURE sp_agendar_cita(p_id_mascota INT, p_id_veterinario INT, p_fecha_hora TIMESTAMP)
  - Fuera de la lamina (habla de la practica): El molde es fijo y conviene dictarlo entero antes de escribir una sola validacion, porque es donde se pierden los puntos sin haber entendido nada mal.
  - Fuera de la lamina (habla de la practica): Un estudiante que agregue p_id_cita no comete un error de sintaxis, comete un error de diseno, y la rubrica lo mira.

**[Slide 7] El molde de un procedimiento en PL/pgSQL** — 18 vinetas.

**[Slide 8] Los modos de parametro, y por que hoy no se usa OUT** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Los parametros tienen modo, y el modo es la direccion en la que viaja el dato.
  - IN es el modo por omision y no se escribe: p_id_mascota INT ya es IN.
  - Si no la mira —y nadie mira lo que no falla— la regla de negocio no se cumplio.
  - Abortar con RAISE EXCEPTION invierte la carga: la aplicacion no puede ignorar el error porque el motor le devolvio un fallo, y ademas nada quedo escrito.
  - El encabezado, en todo caso, es un contrato: nombre, orden y tipos.
  - Vale decirlo con crudeza porque impacta la Clase 12, cuando la aplicacion consuma estos procedimientos: si alguien intercambia el orden de dos parametros del mismo tipo
  - El procedimiento se crea igual, la aplicacion sigue llamandolo sin error y agenda la cita para la mascota equivocada.
  - La proteccion practica, convencion recomendada y no regla dura, es llamar con notacion nombrada,, porque asi el orden deja de importar y la llamada se lee sola seis meses despues.
  - NOTAS:
  - Dentro del cuerpo un parametro IN se comporta como una variable local, asi que se le puede asignar, aunque hacerlo confunde a quien lee y no cambia nada afuera.
  - OUT devuelve un valor a quien llama, e INOUT entra con valor y sale modificado.
  - Hay una particularidad de PostgreSQL que conviene decir porque el estudiante que busque en internet va a tropezar con ella: en un procedimiento, un parametro OUT tambien hay que pasarlo en la llamada, de modo que la sintaxis termina siendo CALL sp_x(1, 2, NULL) con un NULL de relleno; es incomodo, y es una de las razones por las que hoy no se usan.
  - La otra razon es de diseno y es la que hay que defender en clase.
  - Devolver el error en un parametro OUT significa que el procedimiento hizo su trabajo, dejo la fila insertada y ademas puso un texto en una variable que la aplicacion PUEDE mirar.
  - CÓDIGO CITADO (referencia):
  - CALL sp_agendar_cita(p_id_mascota => 1, p_id_veterinario => 2, p_fecha_hora => TIMESTAMP '2026-09-15 10:00:00')
  - Fuera de la lamina (habla de la practica): La otra razon es de diseno y es la que hay que defender en clase, porque es la decision que la solucion docente califica.

**[Slide 9] RAISE EXCEPTION: la validacion que aborta y deshace** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Esta es la parte que convierte una consulta con nombre en logica de negocio.
  - La forma es RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id_mascota; y hay cuatro cosas que decir sobre esa linea.
  - Primera, el signo de porcentaje es el marcador de sustitucion de PL/pgSQL: se reemplaza, en orden, por las expresiones que siguen a la coma, y si hay mas marcadores que expresiones el motor lanza un error de formato.
  - Para imprimir un porcentaje literal se escribe dos veces.
  - Segunda, el mensaje es parte de la interfaz publica del procedimiento: es lo que la aplicacion va a mostrar y lo que la bateria de pruebas va a verificar, asi que se escribe pensando en la recepcionista de la clínica y no en el programador.
  - Tercera, y es lo decisivo: RAISE EXCEPTION aborta.
  - Es imposible que quede una cita a medias, y no porque el codigo lo cuide, sino porque el motor lo garantiza.
  - Cuarta, cada excepcion lleva un codigo SQLSTATE; el de un RAISE EXCEPTION sin mas indicaciones es P0001
  - Y se puede fijar uno propio con USING ERRCODE, lo cual permite que la aplicacion distinga un error de negocio de un fallo de la base sin leer el texto del mensaje.
  - Falta la mecanica de la primera validacion, que es donde el grupo se atora.
  - Se escribe y despues IF NOT FOUND THEN.
  - Ese es el error silencioso mas caro del dia y la razon por la que IF NOT FOUND va primero.
  - Con clave primaria en el WHERE eso no puede ocurrir, y por eso hoy no se usa STRICT.
  - NOTAS:
  - No sale del procedimiento con un aviso, lanza un error que propaga hasta quien llamo, y todo lo que el procedimiento hubiera escrito antes se deshace.
  - Eso ultimo se menciona y no se desarrolla: hoy basta con el texto.
  - Hay que explicar por que funciona, porque no es evidente: en PL/pgSQL, un SELECT INTO deja una variable especial llamada FOUND en verdadero si devolvio al menos una fila y en falso si no devolvio ninguna, y NOT FOUND es simplemente su negacion.
  - Y hay que decir tambien lo que NO pasa, porque es lo contrario de Oracle: si el SELECT INTO no encuentra nada, PL/pgSQL no lanza NO_DATA_FOUND, deja la variable en nulo y sigue adelante.
  - Quien espere la excepcion de Oracle escribe un procedimiento que, ante una mascota inexistente, compara nulo contra 'S', obtiene nulo, entra por el ELSE y termina insertando la cita.
  - Si el SELECT devuelve varias filas, en cambio, PL/pgSQL se queda con la primera sin avisar, salvo que se escriba STRICT, que entonces si lanza excepcion en los dos casos.
  - CÓDIGO CITADO (referencia):
  - SELECT activa INTO v_activa FROM mascota WHERE id_mascota = p_id_mascota
  - Fuera de la lamina (habla de la practica): Esta es la parte que convierte una consulta con nombre en logica de negocio, y es el mecanismo que la pregunta 1 de la clase califica con treinta y cinco puntos.

**[Slide 10] RAISE EXCEPTION en accion: la mascota inactiva** — 14 vinetas.

**[Slide 11] El molde de PL/pgSQL y la validacion que aborta** — 18 vinetas.

**[Slide 12] Donde debe vivir la logica de negocio: la respuesta honesta** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La pregunta de fondo es donde debe vivir la logica de negocio, y merece respuesta honesta y no dogmatica, porque hay equipos serios en las dos orillas.
  - Primero, la regla se cumple aunque alguien entre por fuera de la aplicacion: un guion de migracion, una herramienta de administracion, una segunda aplicacion escrita el proximo semestre.
  - Tercero, y aqui se amarra con la Clase 2, permite un modelo de permisos mas fino: se puede hacer GRANT EXECUTE ON PROCEDURE sp_agendar_cita TO recepcion y a la vez no otorgar INSERT sobre cita
  - Con lo cual la recepcionista agenda citas pero no inserta filas arbitrarias ni corrige estados a mano.
  - Se nombra hoy y se usa en la Clase 12.
  - En contra hay argumentos igual de legitimos: el codigo del procedimiento no se versiona con la naturalidad del codigo de aplicacion
  - Porque si nadie guarda el archivo sql en un repositorio la unica copia esta dentro del motor; probarlo automaticamente es mas incomodo
  - Y por eso la bateria de hoy se escribe a mano; y ata el sistema al motor, ya que llevar estos procedimientos a Oracle o a MySQL implica reescribirlos, no traducirlos.
  - El criterio de oficio, no ley, es este: en la base van los invariantes que no pueden violarse nunca, como que el stock no quede negativo o que una mascota inactiva no agende
  - Y las operaciones de varias sentencias que deben ocurrir juntas; en la aplicacion van la orquestacion, la interfaz y las reglas volatiles.
  - Senal de alerta util: si una regla cambio mas de una vez en el semestre, probablemente no debia estar fija dentro de un procedimiento.
  - NOTAS:
  - A favor de la base de datos hay tres argumentos duros.
  - Segundo, se ahorran viajes de red cuando la operacion implica varias sentencias encadenadas.
  - Eso es minimo privilegio hecho codigo, y conviene senalar el matiz: en PostgreSQL el cuerpo se ejecuta con los privilegios de quien llama, salvo que el procedimiento se declare SECURITY DEFINER, que es lo que lo hace ejecutarse con los del propietario.
  - Sin esa clausula, dar EXECUTE no alcanza.

**[Slide 13] La inyeccion de SQL, explicada y no solo mencionada** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La inyeccion de SQL merece parrafo propio porque es el argumento de seguridad mas concreto de la clase y casi siempre se menciona sin explicarlo.
  - Si escribe Luna todo va bien; si escribe Luna' OR '1'='1 la condicion se vuelve siempre verdadera y la pantalla devuelve el listado completo de mascotas de la clinica; si escribe '
  - Un procedimiento con parametros cierra ese agujero por un motivo tecnico preciso: el valor viaja como parametro
  - Es decir el motor ya analizo y planifico la sentencia antes de conocer el contenido, asi que ese contenido no vuelve a pasar por el analizador sintactico y no puede convertirse en instrucciones.
  - Aqui hace falta el matiz que distingue una clase buena de una recitada: el procedimiento no es inmune por ser procedimiento.
  - En PL/pgSQL la forma correcta de armar una sentencia dinamica es EXECUTE 'SELECT...
  - WHERE nombre = $1' USING p_nombre, o construir el texto con format y los marcadores %L para valores y %I para identificadores, que escapan lo que reciben.
  - Regla dura para el proyecto: ningun dato de usuario se concatena dentro de una sentencia, ni en la aplicacion ni dentro del procedimiento.
  - Ese principio se retoma en la Clase 12.
  - NOTAS:
  - Ocurre cuando la aplicacion arma la consulta pegando texto que escribio el usuario, y ese texto termina interpretado por el motor como codigo y no como dato.
  - En la clínica seria una pantalla de busqueda que construye SELECT * FROM mascota WHERE nombre = seguido de lo que el usuario digito entre comillas.
  - DELETE FROM cita; -- el motor recibe dos sentencias y la segunda borra la agenda.
  - Si dentro del cuerpo alguien escribe EXECUTE 'SELECT...
  - WHERE nombre = ' || p_nombre, el agujero se reabre igual, ahora escondido un nivel mas abajo y por lo tanto mas dificil de auditar.

**[Slide 14] La bateria de pruebas: por que un bloque DO por caso** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El punto de partida es un problema practico: si el estudiante escribe los cuatro CALL uno tras otro y ejecuta todo de un tiro, el primero que falla aborta la ejecucion y los siguientes no corren.
  - La solucion es el bloque anonimo: DO $$ BEGIN...
  - END $$; es un bloque de PL/pgSQL que se ejecuta una vez y no se guarda en ningun catalogo.
  - Los resultados van a una tabla, no a la pantalla, y eso tambien tiene razon: una captura de cuatro mensajes sueltos no se puede comparar contra nada
  - Mientras que un SELECT sobre resultado_prueba(id_prueba, caso, esperado, obtenido, paso) es una sola imagen que muestra los cuatro casos con su veredicto.
  - Los cuatro casos del proyecto son el positivo, con una mascota activa y una franja libre, y los tres negativos: mascota inactiva —Rocky, identificador 3
  - Y Kiara, identificador 8, estan inactivas en los datos sembrados—, mascota inexistente con el identificador 99, y franja ocupada, para la que sirve la cita que el veterinario 1 ya tiene el 2026-09-01 a las 08:00.
  - Y hay que cerrar con la prueba que nadie piensa: un SELECT COUNT(*) FROM cita que demuestre que la tabla paso de diez filas a once y no a catorce.
  - Ese conteo es lo que evidencia que los tres errores no dejaron basura, es decir que RAISE EXCEPTION hizo lo que se dijo que hacia.
  - Hay un detalle de mecanica que conviene conocer porque explica por que esto funciona: un bloque de PL/pgSQL con clausula EXCEPTION abre internamente un punto de retorno, un savepoint, de modo que al capturar el error se deshace solo lo que ese bloque hizo.
  - Una, que la captura tiene un costo y por eso no se envuelve todo el codigo en manejadores por si acaso.
  - Es un buen momento para sembrar la Clase 8: quien confirma la transaccion es quien orquesta la operacion completa, no cada pieza por su cuenta.
  - NOTAS:
  - Un procedimiento sin prueba no esta terminado.
  - Aparecen tres casos sin probar y una captura que no demuestra nada.
  - EXCEPTION WHEN OTHERS THEN...
  - Su clausula EXCEPTION atrapa el error, lo convierte en una fila de resultado y deja que el siguiente bloque corra.
  - Un bloque por caso, cuatro bloques, cuatro filas.
  - Una bateria sin ese conteo prueba que el procedimiento se queja, no que no escribe.
  - Tiene dos consecuencias.
  - Dos, y es la que importa hoy, que el procedimiento de la clase NO lleva COMMIT: si lo llevara, llamarlo desde dentro de un bloque con EXCEPTION fallaria, porque PostgreSQL no permite confirmar la transaccion mientras hay un savepoint activo.
  - Fuera de la lamina (habla de la practica): Un procedimiento sin prueba no esta terminado, y esta parte vale veinticinco de los cien puntos de la clase, asi que hay que dictarla como tema y no como recomendacion.

**[Slide 15] La bateria de pruebas: un bloque DO por caso** — 12 vinetas.

**[Slide 16] El molde de un caso de error y la prueba del conteo** — 3 vinetas.

**[Slide 17] Que significa la columna paso, y la trampa del WHEN OTHERS** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Capturar WHEN OTHERS y escribir paso = TRUE porque hubo excepcion es insuficiente: una excepcion tambien la lanza un nombre de columna mal escrito, un tipo que no convierte o una tabla que no existe.
  - Con ese criterio, un procedimiento roto pasaria las tres pruebas negativas.
  - La forma es paso = SQLERRM ILIKE '%inactiva%', que es una comparacion insensible a mayusculas: se afirma que fallo Y que fallo por lo que se esperaba.
  - La segunda mitad es que la columna paso admite dos lecturas legitimas y hay que elegir una.
  - Si paso significa el resultado coincidio con lo esperado, las cuatro filas quedan en verdadero cuando todo esta bien, porque en un caso negativo lo esperado es la excepcion.
  - Las dos son defendibles; lo que no es defendible es no decir cual.
  - La regla del curso es explicita: se usa la misma lectura para las cuatro filas y se declara en una linea junto a la tabla.
  - Salida esperada de una bateria sana: 4 filas, el caso valido con paso TRUE y los 3 invalidos con paso TRUE y el SQLERRM literal del procedimiento.
  - Un caso invalido con paso FALSE es un hallazgo: el procedimiento dejo pasar algo que debia rechazar.
  - NOTAS:
  - Aqui esta el matiz que separa una bateria que prueba algo de una que se prueba a si misma.
  - Lo que hay que verificar es el TEXTO de la excepcion, y para eso PL/pgSQL expone la variable SQLERRM con el mensaje y SQLSTATE con el codigo.
  - Si paso significa la operacion se completo, los tres casos negativos quedan en falso incluso con el procedimiento perfecto.
  - Conviene decir en voz alta la consecuencia, porque es la que evita reclamos: no se descuenta por elegir una u otra, se descuenta por las cuatro filas en verdadero sin haber verificado el texto.
  - Fuera de la lamina (habla de la practica): Aqui esta el matiz que separa una bateria que prueba algo de una que se prueba a si misma, y conviene dictarlo despacio porque la solucion docente lo califica.
  - Fuera de la lamina (habla de la practica): Las dos son defendibles; lo que no es defendible es no decir cual, porque entonces la columna no significa nada y el docente no puede calificar la captura.

**[Slide 18] La columna paso y la trampa de WHEN OTHERS** — 2 vinetas.

**[Slide 19] El contrato del procedimiento: los 6 bloques que consume la app** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Se escribe para quien va a LLAMAR al procedimiento sin abrirlo, y en este curso esa persona existe con nombre: es el mismo estudiante en la Clase 12, o su companero de Programacion II, construyendo la aplicacion de la clínica.
  - Son seis bloques y cada uno responde una pregunta.
  - La firma exacta, con los tipos y en el orden real, responde como se declara.
  - El ejemplo de llamada, con valores concretos que funcionan, responde como se invoca; y conviene exigirlo porque es lo que convierte el contrato en algo copiable.
  - Las precondiciones responden que tiene que ser verdad antes: la mascota existe y esta activa, la franja del veterinario esta libre.
  - Las postcondiciones responden que queda despues, y aqui la frase importante es la del caso malo: si falla, no queda NADA.
  - La tabla de errores lleva el mensaje LITERAL, no una parafrasis, porque quien llama va a comparar contra ese texto —y porque es el mismo texto que la bateria de pruebas verifica.
  - Y el sexto bloque es la decision de diseno: por que se aborta en vez de devolver un codigo.
  - Ese bloque es el que distingue documentar de pensar, y es el que la solucion docente lee primero.
  - NOTAS:
  - El contrato no es codigo, y hay que explicar para quien se escribe, porque si no el estudiante lo redacta como un resumen del codigo.
  - Un contrato sirve si permite escribir la llamada y manejar los errores sin leer el cuerpo.
  - Sin ella, quien llama no sabe si tiene que limpiar algo.
  - Fuera de la lamina (habla de la practica): La tabla de errores lleva el mensaje LITERAL, no una parafrasis, porque quien llama va a comparar contra ese texto —y porque es el mismo texto que la bateria de pruebas verifica, de modo que los dos entregables tienen que coincidir palabra por palabra.

**[Slide 20] Los 6 bloques del contrato, uno por uno** — 5 vinetas.

**[Slide 21] Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un procedimiento se invoca para que HAGA algo y se llama con CALL sp_x(...); una funcion se invoca para que DEVUELVA un valor y se llama dentro de una expresion, SELECT fn_x(...).
  - No son dos sabores del mismo objeto: en PostgreSQL una funcion no puede hacer COMMIT ni ROLLBACK y un procedimiento si, y esa es la razon tecnica por la que el objeto de hoy es un procedimiento.
  - Otra diferencia que se nota en la practica: llamar a un procedimiento con SELECT sp_agendar_cita(...) devuelve un error explicito de PostgreSQL, que dice que sp_agendar_cita es un procedimiento y sugiere usar CALL.
  - Vale mostrarlo a proposito, porque es un mensaje que el estudiante va a encontrar y conviene que lo reconozca en vez de asustarse.
  - La funcion llega en la Clase 4 con fn_precio_consulta, y ahi la comparacion ya estara hecha.
  - Una FUNCTION devuelve un valor y se usa dentro de una consulta: FROM....
  - Un PROCEDURE no devuelve valor y se invoca como sentencia suelta:.
  - Llamar un procedimiento con SELECT es un error de PostgreSQL, no una variante.
  - NOTAS:
  - Conviene cerrar la teoria con esta distincion, y decirla HOY.
  - CÓDIGO CITADO (referencia):
  - SELECT nombre, fn_precio_consulta(...)
  - CALL sp_agendar_cita(3, 1, TIMESTAMP '2026-09-01 09:00')
  - Fuera de la lamina (habla de la practica): Conviene cerrar la teoria con esta distincion, y decirla HOY, porque el estudiante la va a necesitar en el taller de hoy y no la semana entrante.

**[Slide 22] PROCEDURE o FUNCTION: la diferencia es donde se puede usar** — 13 vinetas.

**[Slide 23] PROCEDURE o FUNCTION: cual se puede usar dentro de un SELECT** — 5 vinetas.

**[Slide 24] Depurar sin depurador: los cuatro movimientos, en PostgreSQL** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Depurar sin depurador es una habilidad concreta y se ensena en cuatro movimientos.
  - Primero, entender que error se esta leyendo, porque hay dos momentos distintos: el error de creacion, que es de sintaxis y lo devuelve el CREATE PROCEDURE senalando linea y posicion
  - Y el error de ejecucion, que es el que aparece con el CALL y es donde salen los nombres de tabla o columna equivocados.
  - A diferencia de Oracle no hay que consultar ninguna vista de errores ni verificar si el objeto quedo invalido: si el CREATE no protesto, el objeto esta creado; lo que no significa que funcione.
  - Segundo, dejar trazas con RAISE NOTICE 'llegue al paso 2, v_activa = %', v_activa; que imprime en la salida de mensajes sin abortar nada, y es el equivalente directo de lo que en Oracle se hace con la salida de servidor.
  - Tercero, aislar: tomar el SELECT activa INTO v_activa FROM mascota WHERE id_mascota = 3 y ejecutarlo suelto con el valor que fallo, para saber si el problema esta en la consulta o en la logica que la rodea.
  - Cuarto, probar con casos deliberados: un caso correcto y tres de error, cada uno en su bloque, escritos en resultado_prueba.
  - Un procedimiento con solo la captura del caso feliz no demuestra manejo de errores, y el Parcial 1 lo pregunta de frente.
  - NOTAS:
  - Conviene mencionar que RAISE tiene niveles —NOTICE, WARNING, EXCEPTION— y que solo el ultimo aborta.

**[Slide 25] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El motor de la clase es PostgreSQL, que corre dentro del navegador, y por lo tanto todo el codigo de hoy es PL/pgSQL.
  - Vale un minuto de clase senalar las cuatro diferencias que mas cuestan —IS en lugar de AS, VARCHAR2 y NUMBER en lugar de TEXT e INT, RAISE_APPLICATION_ERROR en lugar de RAISE EXCEPTION
  - Y la barra final que aqui es un error— y no vale mas, porque cada minuto invertido en sintaxis del otro motor es un minuto que el estudiante no dedica a lo que se le va a evaluar.
  - La regla operativa del curso se mantiene: la fuente de verdad es el archivo sql en la carpeta del proyecto, nunca la pestana del navegador, y el estudiante va bien si reconstruye procedimiento, pruebas y datos pegando su propio guion.
  - NOTAS:
  - Ahi funcionan CREATE PROCEDURE, el dollar-quoting, RAISE EXCEPTION, los bloques DO, SQLERRM y SQLSTATE, y la tabla resultado_prueba: la evidencia de la clase es la salida del motor y no una promesa.
  - Oracle Live SQL sigue en el kit, pero cambia de papel y hay que decirlo sin ambiguedad: sirve como CONTRASTE de sintaxis para quien se vaya a encontrar Oracle en el trabajo.
  - Fuera de la lamina (habla de la practica): Este punto hay que decirlo con precision porque una version anterior de esta guia decia lo contrario y costaria puntos repetirla.
  - Fuera de la lamina (habla de la practica): Oracle Live SQL sigue en el kit, pero cambia de papel y hay que decirlo sin ambiguedad: sirve como CONTRASTE de sintaxis para quien se vaya a encontrar Oracle en el trabajo, no como sitio donde se hace el taller.

**[Slide 26] El segundo procedimiento: sp_registrar_consulta y el EXISTS** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un segundo procedimiento no es relleno: es donde se practica una decision distinta. sp_registrar_consulta escribe en consulta
  - Y la Clase 1 dejo esa tabla con id_cita NOT NULL UNIQUE, porque una consulta pertenece a una cita y una cita tiene a lo sumo una consulta.
  - La pregunta interesante es entonces para que escribir la validacion, si el motor ya defiende el dato.
  - La primera es el mensaje: la restriccion produce un error tecnico que menciona el nombre del indice, y un IF EXISTS () THEN RAISE EXCEPTION 'ERROR: la cita % ya tiene consulta registrada', p_id_cita; produce el mensaje que la recepcionista puede entender.
  - La segunda es que el procedimiento puede validar lo que la restriccion no ve: que la cita exista, y que su estado no sea 'CANCELADA', porque no se documenta la atencion de una cita que se cancelo.
  - La restriccion es la ultima linea de defensa y sigue actuando cuando alguien entra por fuera; el procedimiento mejora el mensaje, no reemplaza la garantia.
  - El orden importa: comprobar con IF EXISTS () antes de insertar permite responder con un mensaje de negocio claro; dejar que choque contra el UNIQUE produce un error del motor que la aplicacion no sabe traducir.
  - NOTAS:
  - Eso significa que registrar dos veces la consulta de la misma cita ya esta impedido por el motor: el segundo INSERT choca contra la restriccion de unicidad y falla.
  - La respuesta tiene dos partes y las dos valen.
  - Conviene decir tambien lo que NO hay que hacer: quitar la restriccion porque ya esta el procedimiento.
  - Esa jerarquia —declarativo primero, procedimiento encima— es exactamente lo que la Clase 4 va a formalizar.
  - CÓDIGO CITADO (referencia):
  - SELECT 1 FROM consulta WHERE id_cita = p_id_cita
  - SELECT 1 FROM consulta WHERE id_cita = p_id_cita

**[Slide 27] Como amarra con las clases vecinas y con la rubrica del PI** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Lo de hoy no es una isla.
  - La Clase 1 dejo el esquema, la baja logica con activa igual a 'S' o 'N' y la restriccion de unicidad sobre la franja del veterinario, que son justamente las tres cosas que las validaciones de hoy usan.
  - La Clase 2 dejo los cuatro roles y hoy aparece el patron mas fino de todos: no dar INSERT sobre cita al rol recepcion, sino EXECUTE sobre sp_agendar_cita, de modo que el usuario solo pueda escribir a traves de la regla de negocio.
  - La Clase 4 cuelga de este procedimiento la funcion y los dos triggers, y ahi se decide, para cada regla, si vive en un CHECK, en un trigger o en la aplicacion.
  - La Clase 8 retoma el punto que hoy se siembra: quien confirma la transaccion.
  - Y la Clase 12 consume estos procedimientos desde la aplicacion.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - «Ejecute el CREATE y no dio error, entonces esta bien»: no necesariamente, y es la pregunta mas importante del dia.
  - PostgreSQL valida la sintaxis del cuerpo pero no resuelve los nombres de tabla y columna hasta la primera ejecucion, asi que el CALL es la unica evidencia.
  - «Por que no resolver la regla con un CHECK y ahorrarse el procedimiento»: porque un CHECK solo puede mirar columnas de la misma fila que se esta insertando
  - Y la regla del proyecto necesita consultar otra tabla, ya que activa vive en mascota y la fila que se inserta esta en cita.
  - «Por que mi procedimiento inserta la cita de una mascota que no existe»: porque en PL/pgSQL un SELECT INTO sin resultado no lanza excepcion, deja la variable en nulo
  - Y comparar nulo con 'S' da nulo, que no es verdadero pero tampoco entra por el IF; falta el IF NOT FOUND.
  - «Un procedimiento es mas rapido»: ahorra viajes de red y analisis repetido, y cada viaje cuesta del orden de uno a cincuenta milisegundos segun la latencia, pero no arregla una consulta mal escrita; eso se ataca en las Clases 6 y 7
  - Y en un motor que corre dentro del navegador la mejora de red no se puede medir, asi que se documenta como argumento y no como cronometraje.
  - «Puedo devolver el mensaje en lugar de abortar»: se puede, y es exactamente lo que el sexto bloque del contrato tiene que justificar; la respuesta corta es que un mensaje que nadie revisa deja la cita creada igual.
  - «Y si el procedimiento queda mal y la aplicacion ya lo llama»: CREATE OR REPLACE reemplaza el cuerpo conservando los privilegios otorgados, asi que no hay que repetir el GRANT EXECUTE mientras la firma no cambie; si cambia la firma hay que ajustar tambien a quien llama, y ahi conviene advertir algo de PostgreSQL: como admite sobrecarga, cambiar los tipos de los parametros no reemplaza el procedimiento anterior, crea uno nuevo al lado, y quedan dos.
  - Se limpia con DROP PROCEDURE nombrando los tipos.
  - Fuera de la lamina (habla de la practica): Lo de hoy no es una isla, y decirlo en voz alta le da sentido al entregable.
  - Fuera de la lamina (habla de la practica): Y la Clase 12 consume estos procedimientos desde la aplicacion, que es cuando el contrato de la pregunta 5 deja de ser un documento y se vuelve la especificacion que alguien lee.


**Demo que usted debe poder repetir:** sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 3 · Procedimientos almacenados · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es un procedimiento almacenado, y las dos palabras que importan
5. Por que un procedimiento y no SQL en cada pantalla
6. El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar
7. El molde de un procedimiento en PL/pgSQL
8. Los modos de parametro, y por que hoy no se usa OUT
9. RAISE EXCEPTION: la validacion que aborta y deshace
10. RAISE EXCEPTION en accion: la mascota inactiva
11. El molde de PL/pgSQL y la validacion que aborta
12. Donde debe vivir la logica de negocio: la respuesta honesta
13. La inyeccion de SQL, explicada y no solo mencionada
14. La bateria de pruebas: por que un bloque DO por caso
15. La bateria de pruebas: un bloque DO por caso
16. El molde de un caso de error y la prueba del conteo
17. Que significa la columna paso, y la trampa del WHEN OTHERS
18. La columna paso y la trampa de WHEN OTHERS
19. El contrato del procedimiento: los 6 bloques que consume la app
20. Los 6 bloques del contrato, uno por uno
21. Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4
22. PROCEDURE o FUNCTION: la diferencia es donde se puede usar
23. PROCEDURE o FUNCTION: cual se puede usar dentro de un SELECT
24. Depurar sin depurador: los cuatro movimientos, en PostgreSQL
25. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar
26. El segundo procedimiento: sp_registrar_consulta y el EXISTS
27. Como amarra con las clases vecinas
28. Demo del dia
29. Cierre · Clase 3

> Privado, no se proyecta: `Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Procedimientos almacenados · VetCare.»
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
- Un procedimiento almacenado es logica de negocio guardada DENTRO de la base, y se llama con CALL. No es una consulta con nombre: recibe parametros tipados y ejecuta varias sentencias como una sola unidad logica, de modo que la regla vive UNA vez y toda la app la respeta.
- El molde de PL/pgSQL es fijo: CREATE PROCEDURE nombre(params) LANGUAGE plpgsql AS $proc$ ... $proc$;. Dentro van DECLARE (variables), BEGIN y END. Los delimitadores $proc$ (dollar-quoting) existen porque el cuerpo lleva punto y coma y el motor necesita saber donde termina. Nada de IS en vez de AS, ni VARCHAR2, ni NUMBER, ni RAISE_APPLICATION_ERROR, ni la barra / final: eso es Oracle y aqui no compila.
- Parametros: IN es el defecto y no se escribe; OUT e INOUT existen pero hoy no se usan para reportar errores. Los tipos son los de PostgreSQL: INT, NUMERIC, TEXT, TIMESTAMP, BOOLEAN.
- La validacion no devuelve un mensaje: aborta con RAISE EXCEPTION 'ERROR: ... %', variable;. El % se sustituye en orden por las variables que siguen a la coma. Al abortar, todo lo que el procedimiento hubiera hecho se deshace, asi que es imposible que quede una cita a medias. Con un mensaje en un parametro OUT el INSERT seguiria corriendo: la regla no se cumpliria.
- Un procedimiento sin prueba no esta terminado: la bateria son bloques DO que capturan el error. Cada caso va en su propio bloque DO $$ BEGIN ... EXCEPTION WHEN OTHERS THEN ... SQLERRM ... END $$;, y el resultado se escribe en una tabla resultado_prueba (caso, esperado, obtenido, paso). Un caso OK y tres casos error, mas el COUNT(*) que demuestra que la tabla cita paso de 10 a 11 filas.
- Procedimiento y funcion se diferencian hoy, no en la Clase 4: CALL sp_x(...) frente a SELECT fn_x(...). El procedimiento se ejecuta como una accion y puede manejar transacciones; la funcion retorna un valor y se invoca dentro de una expresion SQL. En PostgreSQL una funcion no puede hacer COMMIT ni ROLLBACK, y eso es lo que decide cual de los dos se usa.
- El contrato del proc es lo que consume la futura app: firma, precondiciones, postcondiciones y errores. Son 6 bloques: la firma exacta con tipos, un ejemplo de CALL, las precondiciones, las postcondiciones, la tabla de errores con su mensaje literal, y la decision de diseno que explica por que se aborta en vez de devolver un codigo.
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre. El segundo error es dictar el molde de Oracle porque es el que uno recuerda: en ExamLab ese codigo no compila, y el estudiante pierde los 35 puntos de la pregunta 1 por sintaxis, no por no entender el tema.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 28]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 Bateria de pruebas de sp_agendar_cita: P1 OK y P2 rechazado por mascota inactiva [[captura: salida-proc-ok-y-error.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 3 - Procedimientos almacenados/Taller PI - Clase 3 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: >=1 procedimiento de negocio (agendar cita / registrar consulta)
Actividades:
1. Escribir sp_agendar_cita en PL/pgSQL y ejecutarlo en ExamLab (LANGUAGE plpgsql, dollar-quoting, sin sintaxis de Oracle).
2. Incluir las 3 validaciones de negocio del PI, cada una con su RAISE EXCEPTION y su mensaje literal.
3. Correr la bateria de pruebas con bloques DO: 1 caso OK + 3 casos error, escritos en resultado_prueba, mas el COUNT(*) de cita antes y despues.
4. Escribir sp_registrar_consulta, comprobando con EXISTS antes de chocar contra la restriccion UNIQUE.
5. Redactar el contrato del proc en sus 6 bloques (plantilla en este documento) y pegarlo en la pregunta 5.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 3/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 3 - VetCare.docx`. Clave para usted: `Quiz Clase 3 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 29]
**Decir:** «Queda visto: Procedimientos almacenados · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 29] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 03_procs_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 3/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
