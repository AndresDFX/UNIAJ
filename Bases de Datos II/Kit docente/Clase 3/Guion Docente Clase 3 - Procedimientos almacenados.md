# Guion docente · Clase 3 · Procedimientos almacenados · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
- **Entregable de hoy:** Script proc + casos de prueba (captura o enlace Live SQL)
- **Herramienta:** Oracle Live SQL
- **Slides:** Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Un procedimiento almacenado (stored procedure) es un bloque de codigo SQL/PLSQL con nombre propio, guardado y compilado DENTRO de la base de datos, que se invoca con CALL o EXECUTE en vez de reescribir la logica cada vez.
- Parametros: IN (entra un valor, ej. p_id_mascota), OUT (el proc devuelve un valor al que lo llamo, ej. p_msg con el resultado), IN OUT (ambos). A diferencia de una consulta suelta, un proc puede recibir varios parametros y ejecutar varias sentencias como una sola unidad logica.
- Ventaja central para el PI: sin proc, cada pantalla de la futura app (o cada persona que toque el codigo) reescribiria la regla 'mascota inactiva no agenda' con su propio SQL, y tarde o temprano alguien la escribe distinto o la olvida. Con el proc, la regla vive UNA vez dentro de la BD; toda la app la respeta sin excepcion.
- Manejo de errores controlado: en vez de dejar que la insercion falle con un error crudo de motor, el proc valida primero (SELECT activa FROM mascota) y responde con un mensaje de negocio claro ('ERROR: mascota inactiva; no se agenda'), y usa EXCEPTION/TRY-CATCH segun el motor para capturar fallos inesperados sin tumbar la transaccion completa.
- Diferencia con una funcion (se vera en Clase 4): el procedimiento se ejecuta como una accion (CALL sp_algo), la funcion se invoca dentro de una expresion SQL y retorna un valor (SELECT fn_algo(x) FROM ...).
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre, no resuelve el problema que motiva usar procedimientos.

### Desarrollo del tema (para dictar sin consultar otra fuente)

### Que es un procedimiento almacenado, y las dos palabras que importan - diapositiva 4
Un procedimiento almacenado es un bloque de codigo con nombre propio que vive dentro de la base de datos, y las dos palabras que hay que desempacar son guardado y compilado, porque son las que lo separan de un archivo sql en el computador de alguien. Guardado significa que el fuente queda en el diccionario de datos y se puede recuperar con SELECT text FROM user_source WHERE name = 'SP_AGENDAR_CITA' ORDER BY line, de modo que el codigo no depende de que su autor siga en el proyecto. Compilado significa que el motor lo valida al crearlo: si la tabla cita no existe o la columna se llama distinto, el error aparece en el CREATE y no seis semanas despues en produccion. Esa validacion temprana es la primera ventaja concreta y suele omitirse en clase. La invocacion es explicita, con CALL sp_agendar_cita(...) o EXECUTE segun el cliente, y ahi aparece la segunda ventaja medible: en lugar de enviar cuatro sentencias y esperar cuatro respuestas por la red, la aplicacion envia una linea de unos sesenta bytes y recibe un resultado. La Clase 1 dejo el esquema y la Clase 2 la matriz de roles; esta clase es donde la base de datos deja de ser un almacen pasivo y empieza a contener comportamiento, y por eso es la primera en la que el proyecto adquiere reglas que ninguna pantalla puede saltarse.
### Los modos de parametro: IN, OUT e INOUT - diapositiva 4
Los parametros tienen modo, y el modo es la direccion en la que viaja el dato. Un parametro IN entra con un valor y dentro del cuerpo es de solo lectura: en Oracle, asignarle un valor produce error de compilacion, no un aviso, y ese detalle explica la mitad de los errores que el grupo vera hoy. Un parametro OUT llega siempre nulo, exista o no un valor previo en la variable de quien llama, y el cuerpo esta obligado a asignarle algo antes de terminar. Un IN OUT entra con valor y sale modificado, y se usa poco porque dificulta razonar sobre el flujo. El procedimiento del proyecto queda asi: CREATE OR REPLACE PROCEDURE sp_agendar_cita (p_id_cita IN NUMBER, p_id_mascota IN NUMBER, p_fecha IN TIMESTAMP, p_msg OUT VARCHAR2). Ese encabezado es un contrato: nombre, orden, tipos y modos. Vale decirlo con crudeza porque impacta la Clase 12, cuando la aplicacion consuma estos procedimientos: si alguien intercambia el orden de dos parametros del mismo tipo, el procedimiento compila, la aplicacion sigue llamandolo sin error y agenda la cita para la mascota equivocada. La proteccion practica, convencion recomendada mas que regla dura, es llamar con notacion nombrada, sp_agendar_cita(p_id_mascota => 10, p_id_cita => 100, p_fecha => SYSTIMESTAMP, p_msg => v_msg), porque asi el orden deja de importar y la llamada se lee sola seis meses despues.
### Donde debe vivir la logica de negocio: la respuesta honesta - diapositiva 5
La pregunta de fondo es donde debe vivir la logica de negocio, y merece respuesta honesta y no dogmatica, porque hay equipos serios en las dos orillas. A favor de la base de datos hay tres argumentos duros. Primero, la regla se cumple aunque alguien entre por fuera de la aplicacion: un guion de migracion, una herramienta de administracion, una segunda aplicacion escrita el proximo semestre. Segundo, se ahorran viajes de red cuando la operacion implica varias sentencias encadenadas. Tercero, y aqui se amarra con la Clase 2, permite un modelo de permisos mas fino: se puede hacer GRANT EXECUTE ON sp_agendar_cita TO recepcion y a la vez no otorgar INSERT sobre cita, con lo cual la recepcionista agenda citas pero no inserta filas arbitrarias ni corrige estados a mano. Eso es minimo privilegio hecho codigo. En contra hay argumentos igual de legitimos: el PL/SQL no se versiona con la naturalidad del codigo de aplicacion, porque si nadie guarda el archivo sql en un repositorio la unica copia esta dentro del motor; probarlo automaticamente es mas incomodo; y ata el sistema al motor, ya que llevar estos procedimientos a PostgreSQL implica reescribirlos. El criterio de oficio, no ley, es este: en la base van los invariantes que no pueden violarse nunca, como que el stock no quede negativo o que una mascota inactiva no agende, y las operaciones de varias sentencias que deben ocurrir juntas; en la aplicacion van la orquestacion, la interfaz y las reglas volatiles. Senal de alerta util: si una regla cambio mas de una vez en el semestre, probablemente no debia estar fija dentro de un procedimiento.
### La inyeccion de SQL, explicada y no solo mencionada - diapositiva 5
La inyeccion de SQL merece parrafo propio porque es el argumento de seguridad mas concreto de la clase y casi siempre se menciona sin explicarlo. Ocurre cuando la aplicacion arma la consulta pegando texto que escribio el usuario, y ese texto termina interpretado por el motor como codigo y no como dato. En VetCare seria una pantalla de busqueda que construye SELECT * FROM mascota WHERE nombre = seguido de lo que el usuario digito entre comillas. Si escribe Luna todo va bien; si escribe Luna' OR '1'='1 la condicion se vuelve siempre verdadera y la pantalla devuelve el listado completo de mascotas de la clinica; si escribe '; DELETE FROM cita; -- el motor recibe dos sentencias y la segunda borra la agenda. Un procedimiento con parametros cierra ese agujero por un motivo tecnico preciso: el valor viaja como variable ligada, es decir el motor ya analizo y planifico la sentencia antes de conocer el contenido, asi que ese contenido no vuelve a pasar por el analizador sintactico y no puede convertirse en instrucciones. Aqui hace falta el matiz que distingue una clase buena de una recitada: el procedimiento no es inmune por ser procedimiento. Si dentro del cuerpo alguien escribe EXECUTE IMMEDIATE 'SELECT ... WHERE nombre = ' || p_nombre, el agujero se reabre igual, ahora escondido un nivel mas abajo y por lo tanto mas dificil de auditar. Regla dura para el proyecto: ningun dato de usuario se concatena dentro de una sentencia, ni en la aplicacion ni dentro del procedimiento; siempre va por parametro o variable ligada. Ese principio se retoma en la Clase 12.
### Manejo de errores: la regla de negocio y el fallo del motor - diapositiva 6
El manejo de errores es lo que convierte una consulta con nombre en logica de negocio, y exige separar dos cosas que suelen mezclarse. Un error de negocio esperado no es una excepcion: que la mascota este inactiva es un resultado previsto, y lo correcto es detectarlo, asignar p_msg := 'ERROR: mascota inactiva; no se agenda' y salir con RETURN, porque la aplicacion quiere mostrar un mensaje entendible a la recepcionista, no una traza tecnica. Una excepcion es lo inesperado: la mascota no existe, hay dos filas donde deberia haber una, la clave primaria ya estaba usada. Para eso esta el bloque EXCEPTION, con excepciones nombradas que cubren casi todos los casos del proyecto: NO_DATA_FOUND cuando un SELECT INTO no encontro fila, TOO_MANY_ROWS cuando encontro varias, DUP_VAL_ON_INDEX cuando se violo una unicidad, y WHEN OTHERS como ultima red, siempre acompanada de SQLERRM y SQLCODE. El antipatron mas frecuente del mundo, y hay que nombrarlo hoy, es WHEN OTHERS THEN NULL: el fallo se silencia, la aplicacion cree que la cita quedo agendada y el error reaparece semanas despues como un dato que falta sin explicacion. Queda un punto que conviene sembrar sin resolver: el procedimiento del guion hace COMMIT al final y ROLLBACK en el manejador. Sirve para la demostracion, pero un procedimiento que confirma la transaccion por su cuenta no puede participar en una operacion mayor, como facturar y descontar stock en una sola unidad. Ese es el tema de la Clase 8, y decirlo aqui evita ensenar hoy un habito que habra que corregir despues.
### Depurar sin depurador: los cuatro movimientos - diapositiva 7
Depurar sin depurador es una habilidad concreta y se ensena en cuatro movimientos. Primero, leer el error de compilacion, porque hay una trampa que desorienta al grupo entero: si el procedimiento tiene errores, el motor lo crea de todos modos en estado invalido, y Live SQL responde que fue creado con errores de compilacion; quien no lo sabe cree que quedo bien. El diagnostico es SELECT line, position, text FROM user_errors WHERE name = 'SP_AGENDAR_CITA', y el estado se verifica con SELECT object_name, status FROM user_objects WHERE object_type = 'PROCEDURE'. Segundo, dejar trazas: DBMS_OUTPUT.PUT_LINE con SET SERVEROUTPUT ON muestra el flujo paso a paso y Live SQL lo soporta; cuando el cliente no muestra esa salida, la tecnica portable es crear log_debug(id, momento, paso, valor) e insertar una fila en cada punto de interes, con la advertencia de que un ROLLBACK tambien borra esas filas salvo que se use una transaccion autonoma. Tercero, aislar: tomar el SELECT activa INTO v_activa FROM mascota WHERE id_mascota = 10 y ejecutarlo suelto con el valor que fallo, para saber si el problema esta en la consulta o en la logica que la rodea. Cuarto, probar con casos deliberados, y aqui hay un numero exigible: el entregable pide como minimo dos ejecuciones, el caso correcto y el de regla de negocio, pero la convencion del curso son tres, agregando el dato inexistente que dispara NO_DATA_FOUND. Un procedimiento con solo la captura del caso feliz no demuestra manejo de errores, y el Parcial 1 lo pregunta de frente.
### Preguntas frecuentes del grupo - diapositiva 4
Tres preguntas aparecen todos los semestres. Primera: por que no resolver la regla con un CHECK o una clave foranea y ahorrarse el procedimiento. La respuesta es precisa: un CHECK solo puede mirar columnas de la misma fila que se esta insertando, y la regla del proyecto necesita consultar otra tabla, porque el estado activa vive en mascota y la fila que se inserta esta en cita. Un CHECK no puede hacer eso, asi que quedan dos caminos, el procedimiento de hoy o el disparador de la Clase 4. Segunda: un procedimiento es mas rapido. Si, pero hay que ser honesto en donde esta la ganancia: ahorra analisis sintactico repetido y viajes de red, y cada viaje cuesta del orden de uno a cincuenta milisegundos segun la latencia, de modo que ahorrar cuatro viajes es una mejora real en produccion. Lo que no hace es arreglar una consulta mal escrita: si el SELECT interno recorre la tabla completa, el procedimiento sera igual de lento, y eso se ataca en las Clases 6 y 7. Conviene agregar que en un playground todo corre en el mismo servidor, asi que la mejora de red no se puede medir ahi y se documenta como argumento, no como cronometraje. Tercera: y si el procedimiento queda mal y la aplicacion ya lo llama. CREATE OR REPLACE reemplaza el cuerpo conservando los privilegios ya otorgados, asi que no hay que repetir el GRANT EXECUTE de la Clase 2 mientras la firma no cambie; si cambia la firma, hay que ajustar tambien a quien llama.
### El playground de hoy decide si el taller se puede hacer - diapositiva 8
Sobre las herramientas gratuitas hay que ser muy claro hoy, porque es la clase donde el playground equivocado hace perder el taller. Oracle Live SQL es la unica opcion del kit que soporta PL/SQL real: acepta CREATE OR REPLACE PROCEDURE, el bloque EXCEPTION, DBMS_OUTPUT y las excepciones nombradas, conserva el esquema y los guiones en la cuenta gratuita y produce un enlace compartible que sirve de evidencia en ExamLab. Sus limites son igual de reales: un solo esquema, no permite crear usuarios ni roles, no ofrece depurador paso a paso y corta las ejecuciones muy largas, asi que el guion del estudiante conviene partirlo en bloques de pocas sentencias. DB Fiddle corre PostgreSQL o MySQL y tambien admite procedimientos, pero con otra sintaxis: en PostgreSQL el cuerpo va dentro de un bloque delimitado por dobles signos de dolar y el lenguaje se declara plpgsql, los parametros de salida se manejan distinto y no existen DBMS_OUTPUT ni las excepciones con nombre de Oracle. El estudiante que copie el procedimiento de Oracle en DB Fiddle recibira un error de sintaxis que no tiene nada que ver con su logica, y ahi se van veinte minutos de clase. La recomendacion operativa es explicita: todo lo que sea PL/SQL se hace en Live SQL, y DB Fiddle se reserva para el lenguaje de definicion de datos y las consultas. Lo unico que hoy no se puede demostrar y hay que documentar en papel es la parte de permisos, porque otorgar EXECUTE a otro usuario requiere crear ese usuario; el estudiante lo deja en la matriz de la Clase 2 con una linea por procedimiento.
### Errores tipicos del docente que no domina el tema
Error tipico del docente que no domina el tema: mostrar la sintaxis de CREATE PROCEDURE y ejecutar unicamente el caso que funciona. La consecuencia aguas abajo es doble y visible: el estudiante entrega la captura del caso feliz, nunca aprende a consultar user_errors ni a interpretar el estado invalido de un objeto, y llega a la Clase 4 sin saber donde mirar cuando su disparador no compila, con lo cual pierde la sesion de automatizacion depurando a ciegas justo cuando el Parcial 1 evalua el manejo de errores. El segundo tropiezo es pegar el procedimiento de Oracle en DB Fiddle durante la demostracion, ver el error de sintaxis y concluir en voz alta que la herramienta gratuita no sirve, o peor, cambiar de playground a mitad de bloque. La consecuencia es que se consumen veinte de los cincuenta minutos del taller configurando entornos, el estudiante sale sin evidencia del hito, y arrastra la deuda a la Clase 4, que asume el procedimiento ya funcionando para colgarle encima la funcion y el disparador de auditoria.


**Demo que usted debe poder repetir:** CREATE PROCEDURE sp_agendar_cita(...) con validacion de mascota activa.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 3 · Procedimientos almacenados · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Por que un procedimiento y no SQL en cada pantalla
6. La validacion que justifica usar un procedimiento
7. Demo del dia
8. Herramientas de hoy
9. Taller PI VetCare — contexto / por que importa
10. Taller PI VetCare — objetivo y criterios
11. Taller PI VetCare — escenario / datos de partida
12. Taller PI VetCare — pasos guiados
13. Taller PI VetCare — pistas (checklist vacio)
14. Criterios de exito / entregable
15. Para el PI esta semana
16. Cierre · Clase 3

> Privado, no se proyecta: `Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=1 procedimiento de negocio (agendar cita / registrar consulta).
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · [Slide 4]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyectar [Slide 4] «Teoria Core (breve)». El desarrollo completo de cada punto esta
arriba, en «Fundamento teorico», dividido por diapositiva.
Cubrir:
- Un procedimiento almacenado (stored procedure) es un bloque de codigo SQL/PLSQL con nombre propio, guardado y compilado DENTRO de la base de datos, que se invoca con CALL o EXECUTE en vez de reescribir la logica cada vez.
- Parametros: IN (entra un valor, ej. p_id_mascota), OUT (el proc devuelve un valor al que lo llamo, ej. p_msg con el resultado), IN OUT (ambos). A diferencia de una consulta suelta, un proc puede recibir varios parametros y ejecutar varias sentencias como una sola unidad logica.
- Ventaja central para el PI: sin proc, cada pantalla de la futura app (o cada persona que toque el codigo) reescribiria la regla 'mascota inactiva no agenda' con su propio SQL, y tarde o temprano alguien la escribe distinto o la olvida. Con el proc, la regla vive UNA vez dentro de la BD; toda la app la respeta sin excepcion.
- Manejo de errores controlado: en vez de dejar que la insercion falle con un error crudo de motor, el proc valida primero (SELECT activa FROM mascota) y responde con un mensaje de negocio claro ('ERROR: mascota inactiva; no se agenda'), y usa EXCEPTION/TRY-CATCH segun el motor para capturar fallos inesperados sin tumbar la transaccion completa.
- Diferencia con una funcion (se vera en Clase 4): el procedimiento se ejecuta como una accion (CALL sp_algo), la funcion se invoca dentro de una expresion SQL y retorna un valor (SELECT fn_algo(x) FROM ...).
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre, no resuelve el problema que motiva usar procedimientos.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 7]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CREATE PROCEDURE sp_agendar_cita(...) con validacion de mascota activa.
Herramienta: Oracle Live SQL
📸 sp_agendar_cita: caso OK vs caso rechazado por mascota inactiva [[captura: salida-proc-ok-y-error.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 12]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Implementar sp_agendar_cita o sp_registrar_consulta en Live SQL.
2. Incluir validacion de negocio del PI (>=1).
3. Ejecutar 2 pruebas: caso OK + caso error.
4. Documentar firma del proc (contrato para la futura app).
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script proc + casos de prueba (captura o enlace Live SQL)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 3/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 14]
Repasar checklist del dia con [Slide 14] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 3 - VetCare.docx`. Clave para usted: `Quiz Clase 3 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 16]
**Decir:** «Queda avanzado: >=1 procedimiento de negocio (agendar cita / registrar consulta). Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 16] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 03_procs_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 3/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
