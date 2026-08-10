# Guion docente · Clase 8 · Tuning · Transacciones · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Transaccion de negocio (factura + stock) + notas de tuning
- **Entregable de hoy:** Script transaccional + checklist tuning del PI (1 pag.)
- **Herramienta:** Oracle Live SQL / DB Fiddle
- **Slides:** Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde el ultimo COMMIT si algo salio mal (ej. el insumo no tenia stock suficiente). Sin ROLLBACK explicito ante el error, quedaria una factura registrada sin el descuento real de stock: inconsistencia de datos.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Una transaccion es una unidad logica de trabajo compuesta por una o mas sentencias que el motor trata como indivisible frente a dos amenazas distintas: las fallas, porque no puede quedar aplicada a medias, y las demas sesiones, porque nadie debe ver el estado intermedio. Lo primero que hay que aclarar, porque el estudiante lo asume mal, es donde empieza y donde termina. En Oracle la transaccion empieza sola con la primera sentencia DML que se ejecuta, sin que nadie escriba BEGIN, y termina con COMMIT o con ROLLBACK. En PostgreSQL y en MySQL, si no se abre explicitamente con BEGIN o con START TRANSACTION, cada sentencia es su propia transaccion y se confirma sola. El ejemplo del PI es la facturacion: BEGIN; INSERT INTO factura (id_factura, id_dueno, fecha, total) VALUES (5001, 1, CURRENT_DATE, 62000); INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, subtotal) VALUES (5001, 50, 2, 24000); UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 50 AND stock >= 2; COMMIT; Son tres sentencias que describen UN hecho de negocio, cobrar una consulta con dos vacunas, y no tres hechos independientes que casualmente ocurren juntos. Vale detenerse en el detalle del WHERE: la condicion stock >= 2 no es decoracion, es la que impide que el descuento se aplique cuando no hay existencias y hace que el motor informe cero filas afectadas en lugar de dejar un numero negativo. Cero filas afectadas se consulta con SQL%ROWCOUNT en Oracle o con ROW_COUNT() en MySQL, y es la senal que la aplicacion debe convertir en un ROLLBACK.

Atomicidad significa que la transaccion se aplica completa o no se aplica en absoluto, sin estados intermedios visibles ni persistentes. El fallo concreto que ocurre en VetCare cuando falta esta propiedad: se ejecuta el INSERT en factura, se ejecuta el INSERT en detalle_factura y justo antes del UPDATE de stock se cae la red del consultorio. Sin atomicidad quedan la factura 5001 y su detalle cobrando dos vacunas antirrabicas mientras insumo sigue diciendo stock 3 en lugar de 1. Nadie recibe un error, la clinica cobro bien, y el dano aparece semanas despues, cuando el inventario fisico no cuadra y ya no hay forma de saber que factura lo desajusto. La consulta que detecta ese tipo de descuadre conviene tenerla escrita porque es tambien un buen ejercicio: SELECT d.id_insumo, SUM(d.cantidad) AS vendido FROM detalle_factura d GROUP BY d.id_insumo, contrastada contra los movimientos registrados en insumo. Con atomicidad, en cambio, el corte de red deja la transaccion sin COMMIT y el motor la deshace por su cuenta al detectar que la sesion murio: no queda factura, no queda detalle, no se descuenta nada, y la recepcionista simplemente repite la operacion. Esa es la razon por la que el entregable pide un script con COMMIT y ROLLBACK explicitos y no tres sentencias sueltas ejecutadas una tras otra.

Consistencia significa que la transaccion lleva la base de datos de un estado valido a otro estado valido, y la palabra valido no es filosofica: valido es lo que cumplen las restricciones declaradas, es decir claves primarias, claves foraneas, UNIQUE, NOT NULL, CHECK y los disparadores de la Clase 4. Aqui esta el malentendido mas costoso del tema y hay que enunciarlo de frente: la atomicidad NO produce consistencia. Si nadie declaro la restriccion, la transaccion puede ser perfectamente atomica y dejar la base en un estado absurdo. El fallo concreto: la regla de negocio de VetCare dice que el stock de un insumo nunca queda negativo, pero si la tabla insumo no tiene la restriccion y la aplicacion factura 5 unidades de las 3 disponibles, el UPDATE insumo SET stock = stock - 5 WHERE id_insumo = 50 deja stock en menos 2, confirma sin quejarse y el sistema queda vendiendo lo que no existe. La regla se declara una sola vez y vale para siempre, sin importar quien escriba el SQL despues: ALTER TABLE insumo ADD CONSTRAINT ck_insumo_stock_no_negativo CHECK (stock >= 0); Con eso, el mismo UPDATE falla con un error del motor y la transaccion se puede deshacer entera. Y hay una diferencia entre motores que conviene conocer antes de la demo, porque desconcierta en vivo: cuando una restriccion falla, PostgreSQL aborta la transaccion completa y toda sentencia posterior responde que la transaccion actual esta abortada hasta que se haga ROLLBACK, mientras Oracle aborta solo la sentencia que fallo y deja la transaccion abierta, de modo que el programa puede decidir si continua o si deshace.

Aislamiento significa que dos transacciones concurrentes producen un resultado equivalente al que darian si se hubieran ejecutado una despues de la otra. El fallo concreto, y el mas facil de contar: quedan 2 vacunas y dos recepcionistas facturan cada una 2 al mismo tiempo. Ambas leen stock igual a 2, ambas calculan 2 menos 2 y ambas escriben 0; el resultado es stock 0 con cuatro vacunas vendidas y dos entregadas de aire. Eso se llama actualizacion perdida o lost update, y la primera defensa es de diseno: no leer y luego escribir con el valor leido, sino dejar que el motor haga la resta dentro de la misma sentencia, UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 50 AND stock >= 2, porque esa sentencia es atomica y toma un bloqueo sobre la fila mientras se ejecuta. La segunda defensa es el nivel de aislamiento, la perilla con la que se decide cuanto ve una transaccion de lo que otra esta haciendo. Numeros para citar: el estandar SQL define cuatro niveles, READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE; Oracle implementa solo dos de ellos, READ COMMITTED, que es el predeterminado, y SERIALIZABLE; PostgreSQL acepta los cuatro nombres pero READ UNCOMMITTED se comporta como READ COMMITTED, y su valor por omision tambien es READ COMMITTED; MySQL con InnoDB usa REPEATABLE READ por omision, que es un valor distinto y explica diferencias reales cuando se porta un script de un motor a otro. Aqui queda el gancho explicito, y hay que decirlo tal cual en clase: hoy se garantiza que UNA transaccion sea correcta consigo misma, y la Clase 10 estudia que pasa cuando dos se cruzan, con los fenomenos de lectura sucia, lectura no repetible y lectura fantasma, con los bloqueos y con el interbloqueo o deadlock.

Durabilidad significa que despues del COMMIT el dato sobrevive, incluso si el servidor se apaga un segundo mas tarde. Lo que lo hace posible es el registro de transacciones, llamado WAL o write-ahead log en PostgreSQL y redo log en Oracle, y conviene explicarlo porque desmitifica todo el tema: es un archivo secuencial donde el motor escribe lo que va a cambiar ANTES de tocar las paginas de datos. La consecuencia practica es contraintuitiva y muy citable: el COMMIT no necesita escribir en disco las paginas de datos modificadas, solo necesita que su registro del log quede fisicamente grabado; por eso un COMMIT cuesta una escritura secuencial de unos cientos de bytes en lugar de varias escrituras dispersas, y por eso mismo hacer un COMMIT por cada fila en una carga de 100.000 filas puede resultar entre cinco y veinte veces mas lento que agrupar, cifra que es orden de magnitud y hay que medir en cada motor. El ROLLBACK tampoco es magia: el motor conserva la version anterior de cada fila modificada, en el area de undo en Oracle o como versiones antiguas de fila bajo MVCC en PostgreSQL, y deshacer consiste en descartar lo nuevo o restaurar lo viejo. La recuperacion tras una caida usa el mismo mecanismo en dos fases: al arrancar, el motor relee el log, vuelve a aplicar todo lo que estaba confirmado y deshace todo lo que quedo sin confirmar. Vale decir esto en voz alta el mismo dia que se explica ROLLBACK, porque conecta con el respaldo de la Clase 4: un respaldo restaura el estado hasta un punto, y el log es lo que permite avanzar desde ese punto hasta el instante anterior a la falla.

El enemigo silencioso de esta clase en los playgrounds es el autocommit, un modo en el que cada sentencia se confirma automaticamente al terminar, como si cada una llevara su propio COMMIT invisible. Importa porque produce la escena mas frustrante posible: el estudiante escribe su INSERT, escribe ROLLBACK, ejecuta un SELECT y la fila sigue ahi; concluye que el ROLLBACK no funciona, cuando lo que ocurrio es que nunca hubo una transaccion abierta que deshacer. La instruccion practica por herramienta hay que darla antes de empezar el taller, no despues del fracaso. En DB Fiddle con PostgreSQL, todo el bloque BEGIN; INSERT INTO factura ...; ROLLBACK; SELECT COUNT(*) FROM factura; debe escribirse en el MISMO panel para que corra como una sola sesion, y entonces el conteo devuelve cero y la evidencia es perfecta. En MySQL hay que desactivarlo con SET autocommit = 0 o abrir con START TRANSACTION. En Oracle Live SQL cada script se ejecuta como una sesion, asi que un INSERT seguido de ROLLBACK y de un SELECT si demuestra el efecto, pero conviene verificarlo en la propia cuenta antes de la clase, porque la herramienta confirma al finalizar el script. Y existe una trampa adicional que sorprende hasta a gente con experiencia: en Oracle y en MySQL toda sentencia DDL, un CREATE TABLE o un ALTER TABLE, provoca un COMMIT implicito, de modo que si alguien crea una tabla en medio de su transaccion, todo lo anterior queda confirmado y ya no hay nada que deshacer; PostgreSQL es la excepcion, porque su DDL es transaccional y si se puede deshacer. Por eso el script del taller no debe mezclar CREATE TABLE con la demostracion del ROLLBACK.

Hay que separar dos tipos de fallo a mitad de transaccion, porque se atienden distinto. Un error del motor es la violacion de una regla que la base conoce: una restriccion CHECK, una clave foranea, un tipo incompatible, un interbloqueo. El motor lo detecta, lanza la excepcion y, segun el motor, aborta la sentencia o la transaccion completa; el programa se entera sin hacer nada. Un error de la aplicacion es la violacion de una regla que la base NO conoce: que no haya stock suficiente, que la mascota este inactiva, que el total no cuadre con el detalle. El motor no va a deshacer nada, porque desde su punto de vista todo salio bien, y si nadie escribe el ROLLBACK la transaccion se confirma con la inconsistencia dentro. De ahi la forma canonica del procedimiento de facturacion, que ademas reune todo lo visto en el curso: CREATE OR REPLACE PROCEDURE sp_facturar (p_id_factura IN NUMBER, p_id_insumo IN NUMBER, p_cant IN NUMBER) AS BEGIN INSERT INTO factura ...; INSERT INTO detalle_factura ...; UPDATE insumo SET stock = stock - p_cant WHERE id_insumo = p_id_insumo AND stock >= p_cant; IF SQL%ROWCOUNT = 0 THEN RAISE_APPLICATION_ERROR(-20010, 'Stock insuficiente'); END IF; COMMIT; EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE; END; Dos detalles que hay que exigir en el entregable: el RAISE final, porque una excepcion capturada y silenciada es la manera mas comun de fabricar inconsistencias invisibles, y que quien decide el COMMIT sea uno solo, el procedimiento o el llamador, nunca los dos. Cuando la transaccion es larga y solo una parte puede fallar existe el SAVEPOINT, una marca intermedia con nombre a la que se puede volver sin abortar todo: SAVEPOINT sp_linea3; y mas adelante ROLLBACK TO SAVEPOINT sp_linea3, que deshace lo hecho desde la marca, deja vivo el resto y mantiene la transaccion abierta. En VetCare sirve para una factura de cinco lineas donde el insumo de la tercera esta agotado: se deshace esa linea, se avisa y se cobran las otras cuatro. Hay que aclarar que ROLLBACK TO SAVEPOINT no confirma nada y que crear cientos de savepoints dentro de un ciclo tiene costo, asi que se usa con criterio y no por reflejo.

El ultimo bloque de la clase es el de tuning, y aqui tuning no significa tocar parametros del servidor, cosa imposible en un playground y peligrosa sin medicion, sino un conjunto de habitos con numeros. Primero: la transaccion debe ser corta. Una transaccion de negocio bien hecha vive en el orden de milisegundos a pocos cientos de milisegundos, y cualquier cosa que sostenga bloqueos durante segundos es sospechosa; la regla absoluta es no esperar nunca una accion humana con la transaccion abierta, porque el clasico BEGIN, mostrar un cuadro de confirmacion en pantalla y COMMIT convierte una pausa de almuerzo en 45 minutos de filas bloqueadas para el resto de la clinica. La forma correcta es hacer las lecturas y las validaciones primero y abrir la transaccion solo cuando ya se tienen todos los datos para escribir. Segundo: en cargas masivas, agrupar los COMMIT en lotes del orden de 1.000 a 5.000 filas, que es convencion de oficio y no regla dura, en lugar de uno por fila, que es lentisimo, o uno solo para un millon de filas, que hincha el area de undo y sostiene bloqueos enormes. Tercero: apoyarse en los indices de la Clase 7, porque UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 50 sobre la clave primaria bloquea una sola fila, mientras el mismo UPDATE filtrando por una columna sin indice puede recorrer y bloquear muchas mas de las que pretende. Cuarto: mantener frescas las estadisticas de la Clase 6 y evitar disparadores que hagan trabajo pesado dentro de la transaccion, de la Clase 4. Sobre el playground hay que ser explicito para que nadie pierda la clase intentando lo imposible. Se puede demostrar de verdad, con una sola sesion: la atomicidad completa, con INSERT, ROLLBACK y un SELECT COUNT(*) que devuelve cero; el CHECK rechazando el stock negativo; el SAVEPOINT con su vuelta parcial; y el guardia de cero filas afectadas. No se puede demostrar nada que exija dos sesiones simultaneas, porque tanto Oracle Live SQL como DB Fiddle ejecutan un script y cierran, y no hay manera de dejar una transaccion abierta en una ventana y conectarse desde otra; por eso la espera por bloqueo, el interbloqueo, la lectura sucia y la actualizacion perdida se documentan en papel como una linea de tiempo de T1 y T2 con lo que ve cada una en cada paso, que es exactamente el formato que usara la Clase 10. Tampoco se puede demostrar la durabilidad real, porque nadie puede apagar el servidor del playground, ni medir el costo del log. Tres preguntas cierran casi siempre la sesion. Si el motor confirma solo, para que sirve COMMIT: para poder agrupar varias sentencias en un unico hecho de negocio, que es justamente lo que el autocommit impide. Que pasa si me desconecto sin confirmar: el motor deshace la transaccion cuando la sesion muere de forma anormal, aunque algunos clientes confirman al salir de manera ordenada, asi que jamas se debe depender de eso. Y se puede hacer ROLLBACK despues de un COMMIT: no, un COMMIT es definitivo, y lo unico que queda es restaurar desde el respaldo de la Clase 4 con recuperacion a un punto en el tiempo, que es una operacion de administrador y no una correccion de rutina.

Error tipico del docente que no domina el tema: demostrar el ROLLBACK en un playground con autocommit activo y sin abrir la transaccion, ver que la fila sigue ahi y salir del paso diciendo que el playground no soporta transacciones. El estudiante concluye que las transacciones son teoria que no se puede comprobar; aguas abajo, en la Clase 10 no podra construir el escenario de T1 y T2 porque nunca vio una transaccion realmente abierta, y en la Clase 12, al conectar la aplicacion con la base, dejara el manejo de COMMIT y ROLLBACK repartido entre el procedimiento y el codigo cliente, que es la fuente numero uno de facturas a medias. El segundo error es ensenar que la atomicidad garantiza las reglas de negocio y omitir la restriccion CHECK (stock >= 0), confiando en que el codigo de la aplicacion siempre validara antes de descontar. Si eso se acepta hoy, el stock negativo aparecera en la Clase 11 cuando se llene el checklist del PI, o peor, en la sustentacion de la Clase 15, y el informe final afirmara que la base de datos garantiza una regla que en realidad solo esta escrita en un procedimiento que cualquier INSERT o UPDATE manual puede saltarse.


**Demo que usted debe poder repetir:** BEGIN... INSERT factura/detalle... UPDATE stock... COMMIT/ROLLBACK.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Transaccion de negocio (factura + stock) + notas de tuning.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde el ultimo COMMIT si algo salio mal (ej. el insumo no tenia stock suficiente). Sin ROLLBACK explicito ante el error, quedaria una factura registrada sin el descuento real de stock: inconsistencia de datos.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: BEGIN... INSERT factura/detalle... UPDATE stock... COMMIT/ROLLBACK.
Herramienta: Oracle Live SQL / DB Fiddle
📸 Transaccion con stock insuficiente: el ROLLBACK deja todo como estaba [[captura: salida-rollback-stock.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Implementar bloque/proc que facture y descuente stock atomicamente.
2. Probar fallo a mitad (stock insuficiente) -> ROLLBACK.
3. Completar checklist tuning del PI.
4. Actualizar informe PI: seccion transacciones.
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script transaccional + checklist tuning del PI (1 pag.)
📸 Pantallazo: [CAP: avance equipo / playground Clase 8]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 8 - VetCare.docx`. Clave para usted: `Quiz Clase 8 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: Transaccion de negocio (factura + stock) + notas de tuning. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 08_transacciones_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
