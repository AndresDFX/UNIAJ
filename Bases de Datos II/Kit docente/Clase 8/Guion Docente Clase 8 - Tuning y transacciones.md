# Guion docente · Clase 8 · Tuning · Transacciones · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Transaccion de negocio (factura + stock) + notas de tuning
- **Entregable de hoy:** sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
- **Herramienta:** ExamLab (PostgreSQL/PGlite)
- **Slides:** Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx
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

**[Slide 4] Que es una transaccion, y las dos amenazas de las que protege** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Una transaccion es una unidad logica de trabajo formada por una o mas sentencias que el motor trata como indivisible frente a dos amenazas distintas: las fallas
  - Porque no puede quedar aplicada a medias, y las demas sesiones, porque nadie debe ver el estado intermedio.
  - Lo primero que hay que aclarar, porque el estudiante lo asume mal, es donde empieza y donde termina.
  - En PostgreSQL, si no se abre explicitamente con BEGIN, cada sentencia de nivel superior es su propia transaccion y se confirma sola; en Oracle empieza sola con la primera sentencia DML, sin que nadie escriba BEGIN, y termina con COMMIT o con ROLLBACK.
  - El ejemplo del proyecto es la facturacion de una consulta: se inserta la cabecera en factura, se insertan las lineas en detalle_factura y se descuenta el stock de cada insumo.
  - Son varias sentencias que describen UN hecho de negocio, cobrar una consulta con sus insumos, no varios hechos independientes que casualmente ocurren juntos.
  - Vale detenerse en la sentencia del descuento, porque es el centro de la clase
  - En PL/pgSQL, cuantas filas afecto la sentencia anterior se pregunta con GET DIAGNOSTICS v_filas = ROW_COUNT; no existe SQL%ROWCOUNT, que es de Oracle.
  - Los datos con los que se trabaja hoy son seis insumos: 1 Vacuna antirrabica con stock 12, 2 Vacuna triple felina con stock 3, 3 Antiparasitario oral con stock 40, 4 Suero fisiologico con stock 25, 5 Gasa esteril con stock 8 y 6 Jeringa 5ml con stock 60.
  - El insumo 2, con sus 3 unidades, es el que se va a quedar corto en la demo.
  - NOTAS:
  - La condicion stock >= 2 no es decoracion, es la que impide que el descuento se aplique cuando no hay existencias y hace que el motor informe cero filas afectadas en lugar de dejar un numero negativo.
  - CÓDIGO CITADO (referencia):
  - UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 2 AND stock >= 2
  - Fuera de la lamina (habla de la practica): En PL/pgSQL, cuantas filas afecto la sentencia anterior se pregunta con GET DIAGNOSTICS v_filas = ROW_COUNT; no existe SQL%ROWCOUNT, que es de Oracle, y esa sola diferencia decide si el codigo del entregable compila o no.

**[Slide 5] Atomicidad: el fallo concreto en VetCare** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Atomicidad significa que la transaccion se aplica completa o no se aplica en absoluto, sin estados intermedios visibles ni persistentes.
  - El fallo concreto en la clínica cuando falta: se ejecuta el INSERT en factura, se ejecuta el INSERT de la primera linea en detalle_factura, se descuenta el stock de ese primer insumo y justo antes de la segunda linea se cae la red del consultorio.
  - La consulta que detecta el descuadre conviene tenerla escrita porque es tambien buen ejercicio: AS vendido FROM detalle_factura d GROUP BY d.id_insumo, contrastada contra los movimientos registrados en insumo.
  - Con atomicidad, el corte de red deja la transaccion sin confirmar y el motor la deshace por su cuenta al detectar que la sesion murio: no queda factura, no queda detalle, no se descuenta nada, y la recepcionista repite la operacion.
  - NOTAS:
  - Sin atomicidad queda una factura cobrando dos productos con una sola linea registrada, y un insumo descontado que nadie entrego.
  - Nadie recibe un error, la clinica cobro, y el dano aparece semanas despues, cuando el inventario fisico no cuadra y ya no hay forma de saber que factura lo desajusto.
  - CÓDIGO CITADO (referencia):
  - SELECT d.id_insumo, SUM(d.cantidad)
  - Fuera de la lamina (habla de la practica): Esa es la razon por la que el entregable no pide tres sentencias sueltas sino un procedimiento que las agrupa, y por la que la pregunta 2 de la clase vale 25 puntos por demostrar con datos —foto inicial y foto final— que el descuento que SI habia alcanzado se deshizo.

**[Slide 6] Consistencia: valido es lo que las restricciones declaran** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Consistencia significa que la transaccion lleva la base de un estado valido a otro estado valido
  - Y valido no es palabra filosofica: valido es lo que cumplen las restricciones declaradas, claves primarias, claves foraneas, UNIQUE, NOT NULL, CHECK y los disparadores de la Clase 4.
  - Aqui esta el malentendido mas costoso del tema y hay que enunciarlo de frente: la atomicidad NO produce consistencia.
  - El fallo concreto: la regla de la clínica dice que el stock de un insumo nunca queda negativo
  - Pero si la tabla insumo no tiene la restriccion y la aplicacion factura 10 unidades de las 3 disponibles del insumo 2
  - El UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 deja stock en menos 7, confirma sin quejarse y el sistema queda vendiendo lo que no existe.
  - La regla se declara una vez y vale para siempre, sin importar quien escriba el SQL despues:.
  - Y hay una diferencia entre motores que conviene conocer antes de la demo porque desconcierta en vivo: cuando una restriccion falla
  - PostgreSQL aborta la transaccion completa y toda sentencia posterior responde que la transaccion actual esta abortada hasta que se deshaga
  - Mientras Oracle aborta solo la sentencia que fallo y deja la transaccion abierta, de modo que el programa decide si continua o si deshace.
  - NOTAS:
  - Si nadie declaro la restriccion, la transaccion puede ser perfectamente atomica y dejar la base en un estado absurdo.
  - Con eso el mismo UPDATE falla con un error del motor y la transaccion se puede deshacer entera.
  - Conviene notar como se combinan las dos defensas del dia: el CHECK es la red de seguridad declarativa, y el AND stock >= p_cantidad del WHERE es el guardia que evita llegar al error y permite dar un mensaje de negocio en lugar de un error de restriccion.
  - CÓDIGO CITADO (referencia):
  - ALTER TABLE insumo ADD CONSTRAINT ck_insumo_stock_no_negativo CHECK (stock >= 0)

**[Slide 7] Aislamiento: el fallo mas facil de reproducir** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El fallo concreto, el mas facil de contar: quedan 3 vacunas triples y dos recepcionistas facturan cada una 3 al mismo tiempo.
  - Ambas leen stock igual a 3, ambas calculan 3 menos 3 y ambas escriben 0; el resultado es stock 0 con seis vacunas vendidas y tres entregadas de aire.
  - La segunda defensa es el nivel de aislamiento, la perilla que decide cuanto ve una transaccion de lo que otra hace.
  - Numeros para citar: el estandar SQL define cuatro niveles, READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE
  - PostgreSQL acepta los cuatro nombres pero READ UNCOMMITTED se comporta como READ COMMITTED, y su valor por omision es READ COMMITTED
  - NOTAS:
  - Aislamiento significa que dos transacciones concurrentes producen un resultado equivalente al que darian ejecutadas una despues de la otra.
  - Eso se llama actualizacion perdida o lost update, y la primera defensa es de diseno, no de configuracion: no leer y luego escribir con el valor leido, sino dejar que el motor haga la resta en la misma sentencia, UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3, porque esa sentencia es atomica y toma un bloqueo sobre la fila mientras se ejecuta.
  - Oracle implementa solo dos, READ COMMITTED por omision y SERIALIZABLE
  - MySQL con InnoDB usa REPEATABLE READ por omision, valor distinto que explica diferencias reales al portar un script.
  - Aqui queda el gancho explicito, y hay que decirlo tal cual: hoy se garantiza que UNA transaccion sea correcta consigo misma, y la Clase 10 estudia que pasa cuando dos se cruzan, con la lectura sucia, la lectura no repetible, la lectura fantasma, los bloqueos y el interbloqueo o deadlock.
  - Tambien hay que decir que hoy no se puede demostrar, porque el motor de la clase corre una sola sesion.
  - Fuera de la lamina (habla de la practica): Esa es exactamente la decision que la pregunta 5 pide documentar en una frase defendible.

**[Slide 8] Durabilidad: el registro de transacciones** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Lo hace posible el registro de transacciones, llamado WAL o write-ahead log en PostgreSQL y redo log en Oracle: un archivo secuencial donde el motor escribe lo que va a cambiar ANTES de tocar las paginas de datos.
  - La consecuencia practica es contraintuitiva y muy citable: el COMMIT no necesita escribir en disco las paginas de datos modificadas, solo necesita que su registro del log quede fisicamente grabado
  - Por eso un COMMIT cuesta una escritura secuencial de unos cientos de bytes en lugar de varias escrituras dispersas
  - Y por eso mismo hacer un COMMIT por cada fila en una carga de 100.000 filas puede resultar entre cinco y veinte veces mas lento que agrupar, cifra que es orden de magnitud y hay que medir en cada motor.
  - El ROLLBACK tampoco es magia: el motor conserva la version anterior de cada fila modificada, como versiones antiguas de fila bajo MVCC en PostgreSQL o en el area de undo en Oracle, y deshacer consiste en descartar lo nuevo o restaurar lo viejo.
  - La recuperacion tras una caida usa el mismo mecanismo en dos fases: al arrancar, el motor relee el log, vuelve a aplicar todo lo confirmado y deshace todo lo que quedo sin confirmar.
  - Vale decirlo el mismo dia que se explica la reversion, porque conecta con el respaldo de la Clase 4: el respaldo restaura el estado hasta un punto y el log es lo que permite avanzar desde ese punto hasta el instante anterior a la falla.
  - NOTAS:
  - Durabilidad significa que despues de confirmar, el dato sobrevive incluso si el servidor se apaga un segundo mas tarde.
  - Fuera de la lamina (habla de la practica): Es tambien el ultimo item del checklist de la pregunta 5, el del restore probado.

**[Slide 9] La firma de sp_facturar, y por que recibe dos arreglos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Primera, los tipos son INT y NUMERIC, no NUMBER: NUMBER es de Oracle y en PostgreSQL no existe.
  - Uno: validar que los dos arreglos midan lo mismo, con IF array_length(p_insumos, 1) IS DISTINCT THEN RAISE EXCEPTION...; dos arreglos de longitud distinta significan que el llamador se equivoco, y eso se rechaza antes de tocar la base.
  - Se usa IS DISTINCT FROM y no el signo de distinto porque array_length puede devolver nulo si el arreglo viene vacio, y con nulo una comparacion normal no es verdadera ni falsa.
  - Dos: la cabecera, RETURNING id_factura INTO v_id_factura.
  - El total entra en cero porque todavia no se sabe, y RETURNING...
  - Tres: el bucle, FOR i IN 1.. array_length(p_insumos, 1) LOOP, que es la seccion siguiente.
  - Cuatro: al salir del bucle
  - El caso de prueba del enunciado da 22000 por 1 mas 900 por 2 mas 1200 por 3, o sea 27.400, y deja los stocks de los insumos 1, 6 y 5 en 11, 58 y 5.
  - NOTAS:
  - Tres observaciones.
  - Segunda, y es la que sorprende, recibe DOS ARREGLOS PARALELOS y no un insumo suelto, porque una factura real tiene varias lineas; se invoca, que significa una unidad del insumo 1, dos del 6 y tres del 5.
  - Tercera, el cuerpo va entre delimitadores de dolar, y conviene usar una etiqueta como $proc$ en lugar de $$ pelado para que no choque con otro bloque anidado.
  - El cuerpo tiene cuatro partes y vale recorrerlas en orden.
  - INTO evita ir a buscar con otro SELECT el identificador que se acaba de generar.
  - CÓDIGO CITADO (referencia):
  - CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3])
  - FROM array_length(p_cantidades, 1)
  - INSERT INTO factura (id_consulta, total) VALUES (p_id_consulta, 0)
  - UPDATE factura SET total = v_total WHERE id_factura = v_id_factura
  - Fuera de la lamina (habla de la practica): Aqui empieza lo que se califica, y la primera cosa que hay que proyectar es la firma exacta, porque no es la que uno escribiria de memoria: CREATE PROCEDURE sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[]) LANGUAGE plpgsql AS $proc$ ... $proc$.

**[Slide 10] Todo o nada: la transaccion de facturacion** — 18 vinetas.

**[Slide 11] sp_facturar en PL/pgSQL: el molde que se califica** — 5 vinetas.

**[Slide 12] El guardia del stock, sentencia por sentencia** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Dentro del bucle estan las cuatro sentencias que hay que saber defender.
  - Primera, el precio vigente: seguida de IF NOT FOUND THEN RAISE EXCEPTION 'ERROR: el insumo % no existe', p_insumos[i]
  - NOT FOUND es una variable especial de PL/pgSQL que dice si el SELECT INTO anterior trajo fila; sin esa comprobacion, un insumo inexistente deja v_precio nulo y la factura termina con total nulo, que es peor que un error.
  - Se lee el precio de la tabla y no se recibe por parametro a proposito: el precio que se cobra es el vigente, no el que la aplicacion crea recordar.
  - Segunda, el guardia, que es el corazon del dia
  - La comprobacion viaja DENTRO del WHERE, de modo que comprobar y escribir son una sola sentencia y nadie puede colarse entre las dos.
  - Tercera, como se sabe si alcanzo: GET DIAGNOSTICS v_filas = ROW_COUNT, que guarda cuantas filas toco el UPDATE anterior.
  - Uno significa que alcanzo; cero significa que no habia stock, y ese cero es un dato de negocio, no un error del motor: la sentencia se ejecuto perfectamente, simplemente no encontro ninguna fila que cumpliera la condicion.
  - Cuarta, el aborto: IF v_filas = 0 THEN RAISE EXCEPTION 'ERROR: stock insuficiente del insumo % (se pidieron %)', p_insumos[i], p_cantidades[i]
  - El signo de porcentaje es la marca de sustitucion de RAISE, y los argumentos van despues de la cadena en el orden en que aparecen.
  - No lleva RAISE_APPLICATION_ERROR ni un numero de error negativo: eso es Oracle.
  - Cierran el ciclo el INSERT de la linea en detalle_factura con el precio vigente y la acumulacion v_total:= v_total + (v_precio * p_cantidades[i]); notese el operador de asignacion de PL/pgSQL, dos puntos y un igual.
  - CÓDIGO CITADO (referencia):
  - SELECT precio_unit INTO v_precio FROM insumo WHERE id_insumo = p_insumos[i]
  - UPDATE insumo SET stock = stock - p_cantidades[i] WHERE id_insumo = p_insumos[i] AND stock >= p_cantidades[i]

**[Slide 13] Error del motor y error de negocio: se atienden distinto** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un error del motor es la violacion de una regla que la base conoce: una restriccion CHECK, una clave foranea, un tipo incompatible, un interbloqueo; el motor lo detecta, lanza la excepcion y aborta.
  - Un error de negocio es la violacion de una regla que la base NO conoce en esa forma: que no haya stock suficiente, que la mascota este inactiva, que el total no cuadre con el detalle.
  - El motor no va a deshacer nada por su cuenta, porque desde su punto de vista todo salio bien: el UPDATE que no afecta ninguna fila es una sentencia exitosa.
  - La primera: nada de capturar y silenciar.
  - Un EXCEPTION WHEN OTHERS THEN NULL convierte el fallo en silencio, la factura queda registrada, el stock no se descuenta y nadie se entera hasta el inventario; si se captura, se vuelve a lanzar con RAISE a secas, que relanza la excepcion actual.
  - La segunda: quien decide confirmar es uno solo, y en PostgreSQL ese uno solo NO es el procedimiento, que es lo que explica la diapositiva siguiente.
  - Existe ademas el SAVEPOINT para el caso en que la transaccion es larga y solo una parte puede fallar: una marca intermedia con nombre a la que se vuelve sin abortar todo, SAVEPOINT sp_linea3 y mas adelante ROLLBACK TO SAVEPOINT sp_linea3.
  - En la clínica serviria para una factura de cinco lineas donde el insumo de la tercera esta agotado: se deshace esa linea, se avisa y se cobran las otras cuatro.
  - NOTAS:
  - Hay que separar dos tipos de fallo a mitad de transaccion porque se atienden distinto, y esta distincion es la que ordena todo el procedimiento.
  - De ahi que el procedimiento tenga que convertir el cero filas en una excepcion, con el RAISE EXCEPTION de la seccion anterior, y de ahi tambien que el mensaje deba nombrar el insumo concreto: quien lea el error en la sustentacion tiene que poder decir cual linea fallo.
  - Hoy NO se usa.
  - Fuera de la lamina (habla de la practica): Dos exigencias del entregable salen de aqui.
  - Fuera de la lamina (habla de la practica): Hoy NO se usa, porque la regla del negocio que la actividad implementa es todo o nada, pero conviene nombrarlo para que nadie crea que la unica opcion es abortar la factura completa.

**[Slide 14] Donde empieza y termina la transaccion de un CALL** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La afirmacion central es corta: un CALL escrito por fuera de cualquier BEGIN es su propia transaccion.
  - Se demuestra con datos: el descuenta 2 unidades del insumo 3, que tiene 40 y por lo tanto alcanza, y se estrella en el insumo 2, que tiene 3 y no puede dar 10; al final el stock del insumo 3 vuelve a 40 sin intervencion de nadie.
  - La consecuencia practica hay que enunciarla como regla de diseno: quien decide el COMMIT es uno solo, el llamador.
  - Un procedimiento que confirma por su cuenta le quita al llamador la posibilidad de deshacer, y es la fuente numero uno de facturas a medias cuando la Clase 12 conecte la aplicacion con la base.
  - Y hay un detalle de sintaxis que conviene mencionar antes de que alguien lo intente: en PostgreSQL un procedimiento SI puede contener COMMIT y ROLLBACK
  - Pero solo cuando se invoca desde un contexto que lo permita; si el CALL esta dentro de un bloque con manejador de excepciones, el control de transaccion dentro del procedimiento no esta permitido y el motor lo rechaza.
  - O sea que la version con ROLLBACK adentro no es solo innecesaria: en el escenario de la clase ni siquiera corre.
  - NOTAS:
  - Si la excepcion se propaga hasta afuera del procedimiento, el motor deshace TODO lo que ese CALL habia hecho —la cabecera de la factura, las lineas ya insertadas y los descuentos de stock ya aplicados— y nadie escribio ROLLBACK.
  - CÓDIGO CITADO (referencia):
  - CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10])

**[Slide 15] Todo o nada: la transaccion explicita** — 11 vinetas.

**[Slide 16] Por que el procedimiento no lleva COMMIT ni ROLLBACK** — 5 vinetas.

**[Slide 17] El savepoint implicito del bloque EXCEPTION** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El segundo mecanismo es menos conocido: un bloque BEGIN...
  - Capturar no es lo mismo que dejar propagar, y la diferencia se ve en la practica: el
  - EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Fallo esperado: %', SQLERRM
  - END $$ del enunciado esta ahi para que el script no se detenga y se pueda seguir midiendo, no para arreglar nada.
  - Ese savepoint implicito tiene un costo que hay que mencionar: envolver cada iteracion de un bucle largo en su propio bloque con EXCEPTION crea un savepoint por vuelta y eso se paga
  - Asi que no se pone un manejador de excepciones «por si acaso» dentro de un ciclo de miles de iteraciones.
  - La regla practica: manejadores donde haya una decision que tomar, y en ningun otro sitio.
  - Consecuencia practica: dentro del bloque que captura el error, lo escrito antes del fallo en ese mismo bloque se deshace, pero lo escrito antes del BEGIN del bloque sigue en pie hasta que la transaccion termine.
  - NOTAS:
  - EXCEPTION WHEN...
  - END en PL/pgSQL crea un savepoint implicito al entrar.
  - Por eso, cuando el codigo captura el error, se revierte solo lo hecho DENTRO de ese bloque y el resto de la transaccion sigue vivo.
  - El savepoint implicito de ese DO deshace todo lo que el CALL habia hecho, el mensaje se imprime, y la foto final demuestra que la base quedo igual.
  - SQLERRM es la variable que trae el texto del error, y conviene nombrarla porque el estudiante la va a necesitar para que su NOTICE diga algo util en vez de «fallo».
  - CÓDIGO CITADO (referencia):
  - DO $$ BEGIN CALL sp_facturar(...)

**[Slide 18] SAVEPOINT: deshacer una parte sin perder el resto** — 10 vinetas.

**[Slide 19] El bloque EXCEPTION y la trampa de tragarse el error** — 15 vinetas.

**[Slide 20] El contraste con Oracle, que es la pregunta 4** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Por que la base quedo intacta: la respuesta correcta reune las dos ideas de las dos secciones anteriores: el CALL de nivel superior es su propia transaccion y al propagarse la excepcion se deshace todo, y ademas un bloque con EXCEPTION crea un savepoint implicito.
  - Es una respuesta razonable para quien aprendio PL/SQL, y es falsa aqui por dos motivos: el procedimiento de la clase no tiene ese bloque, y ese ROLLBACK no es lo que produjo la reversion.
  - Las otras tres opciones son falsas de forma mas simple, y vale enunciarlo para que nadie las considere: PostgreSQL no guarda una copia de seguridad de cada tabla antes de cada CALL, eso seria carisimo y no existe
  - PL/pgSQL no acumula los UPDATE en memoria para escribirlos al final, cada sentencia se aplica cuando se ejecuta y es visible dentro de la misma transaccion; y no hay ningun trigger de stock en el esquema de la clase, asi que no pudo deshacer nada.
  - El contraste con Oracle no se borra del curso, se coloca donde corresponde: como contraste.
  - Portar este procedimiento a Oracle exige cambiar los tipos, cambiar GET DIAGNOSTICS por SQL%ROWCOUNT, cambiar RAISE EXCEPTION por RAISE_APPLICATION_ERROR y anadir el control de transaccion
  - Que la misma logica de negocio necesite cuatro cambios de sintaxis es en si mismo el aprendizaje.
  - Resumen del contraste: en Oracle el COMMIT o ROLLBACK suele escribirse dentro del procedimiento; en PostgreSQL un CALL dentro de una transaccion abierta no puede hacer COMMIT, y es la excepcion propagada la que deshace.
  - En PostgreSQL ese responsable es siempre quien abrio la transaccion.
  - NOTAS:
  - La opcion incorrecta que mas gente marca es «porque el procedimiento incluia un ROLLBACK explicito en su bloque EXCEPTION, igual que en Oracle», y hay que decir de frente por que aparece: es la forma canonica en Oracle, donde el procedimiento es parte de la transaccion del llamador y si se escribe EXCEPTION WHEN OTHERS THEN ROLLBACK
  - Por eso el mismo procedimiento no se traduce linea por linea entre motores: cambia quien es responsable de confirmar, y con eso cambia donde se escribe el manejo del error.
  - Fuera de la lamina (habla de la practica): La pregunta 4 vale 10 puntos y es de seleccion unica, asi que conviene que el docente sepa exactamente que se pregunta y por que las otras opciones son falsas.

**[Slide 21] Abortar o informar: fn_descontar_stock** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - fn_descontar_stock aplica el mismo patron de descuento con un contrato distinto, que es una de las distinciones mas utiles del curso.
  - Misma regla de negocio, dos contratos, y hay que saber cual se esta pidiendo.
  - La firma: RETURNS BOOLEAN LANGUAGE plpgsql AS $fn$... $fn$.
  - RETURNS BOOLEAN y no PROCEDURE: devuelve verdadero si desconto y falso si no habia suficiente, SIN lanzar excepcion en ese segundo caso.
  - Adentro hay tres partes: validar que p_cantidad sea positiva, y si no, RAISE EXCEPTION; el mismo UPDATE con la condicion en el WHERE; y GET DIAGNOSTICS seguido de RETURN v_filas = 1
  - Que devuelve directamente el resultado de la comparacion sin necesidad de un IF.
  - Distinguir el dato invalido del resultado negativo es la mitad de la pregunta.
  - Se prueba en una sola consulta, AS caso_ok, fn_descontar_stock(2, 10) AS caso_sin_stock, fn_descontar_stock(2, 3) AS caso_limite, que devuelve verdadero, falso y verdadero.
  - El tercer caso es el interesante y conviene detenerse: pide EXACTAMENTE el stock que queda, y con el operador mayor o igual en el guardia tiene que pasar; si alguien escribio solo mayor, ese caso devuelve falso y ahi se ve el error.
  - El estado final deja el insumo 5 en 5 y el insumo 2 en 0, sin ningun negativo.
  - Y el comentario que cierra la pregunta es la decision documentada: leer primero y decidir despues deja una ventana entre la lectura y la escritura
  - Con dos recepcionistas las dos leen 3, las dos deciden que alcanza y el stock termina en menos 2 o el CHECK revienta; el UPDATE con la condicion en el WHERE no tiene ventana.
  - NOTAS:
  - El procedimiento ABORTA la factura completa cuando no hay stock; la funcion INFORMA y deja que el llamador decida.
  - Lo que hay que enfatizar es la linea que separa un caso del otro: una cantidad negativa o cero no es «no hay stock», es una llamada mal hecha, y eso SI es una excepcion; el resultado negativo legitimo se devuelve como dato.
  - Eso aqui no se puede demostrar, porque el motor corre una sola sesion.
  - CÓDIGO CITADO (referencia):
  - CREATE FUNCTION fn_descontar_stock(p_id_insumo INT, p_cantidad INT)
  - SELECT fn_descontar_stock(5, 3)
  - Fuera de la lamina (habla de la practica): Eso aqui no se puede demostrar, porque el motor corre una sola sesion, y ese es el gap que la pregunta 5 pide declarar.

**[Slide 22] fn_descontar_stock: cuando «no hay stock» es una respuesta, no un error** — 5 vinetas.

**[Slide 23] Tuning: habitos de escritura, no parametros del servidor** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El ultimo bloque conceptual es el de tuning, que aqui no significa tocar parametros del servidor —imposible en el navegador y peligroso sin medicion— sino habitos con numeros.
  - Primero: la transaccion debe ser corta.
  - Una transaccion de negocio bien hecha vive en el orden de milisegundos a pocos cientos de milisegundos, y cualquier cosa que sostenga bloqueos durante segundos es sospechosa; la regla absoluta es no esperar nunca una accion humana con la transaccion abierta
  - Porque el clasico de abrir, mostrar un cuadro de confirmacion y confirmar convierte una pausa de almuerzo en 45 minutos de filas bloqueadas para el resto de la clinica.
  - Lo correcto es hacer lecturas y validaciones primero y abrir la transaccion solo cuando ya se tienen todos los datos para escribir.
  - Segundo: en cargas masivas, agrupar los COMMIT en lotes del orden de 1.000 a 5.000 filas, convencion de oficio y no regla dura
  - En lugar de uno por fila, lentisimo, o uno solo para un millon de filas, que hincha las versiones antiguas y sostiene bloqueos enormes.
  - Tercero: apoyarse en los indices de la Clase 7, porque el UPDATE del descuento filtra por id_insumo, que es clave primaria, y por eso bloquea una sola fila; el mismo UPDATE filtrando por una columna sin indice puede recorrer y bloquear muchas mas.
  - Cuarto: estadisticas frescas de la Clase 6 y ningun disparador con trabajo pesado dentro de la transaccion, de la Clase 4.
  - NOTAS:
  - Esos cuatro habitos, mas el de no usar SELECT asterisco en los reportes, mas los predicados sargables, mas el respaldo con restore probado.
  - Fuera de la lamina (habla de la practica): Esos cuatro habitos, mas el de no usar SELECT asterisco en los reportes, mas los predicados sargables, mas el respaldo con restore probado, son literalmente los siete items del checklist que la pregunta 5 pide llenar, y cada item exige estado Y evidencia concreta —un nombre de indice, un archivo, una consulta— porque siete casillas marcadas sin evidencia no demuestran nada.

**[Slide 24] La demo, en el orden en que se proyecta** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La demo es el script Codigo/08_transacciones_clinica.sql y se corre.
  - Tiene cinco bloques y el valor esta en el tercero, asi que hay que administrar el tiempo para llegar ahi con calma.
  - El bloque 0 crea insumo, factura y detalle_factura y siembra los seis insumos con los stocks del enunciado; empieza con los DROP para que el script se pueda correr dos veces sin limpiar a mano.
  - El bloque 2 es el caso feliz:, factura por 27.400 y los stocks 1, 6 y 5 quedan en 11, 58 y 5.
  - El bloque 3 es la clase entera y tiene tres pasos que no se pueden desordenar: la foto inicial
  - Que debe dar una factura, tres lineas, el insumo 3 en 40 y el insumo 2 en 3; el intento que falla a mitad, envuelto en el DO con su manejador para que el script siga; y la foto final, que debe dar EXACTAMENTE los mismos cuatro numeros.
  - Ese es el momento de preguntarle al grupo donde quedo el descuento del insumo 3 y dejar que alguien diga que se deshizo solo.
  - El bloque 3 cierra con la version viable,, que crea la segunda factura por 112.000 y deja el insumo 3 en 38 y el 2 en 0.
  - El bloque 4 es la funcion, con su prueba de tres columnas que devuelve verdadero, falso, verdadero; ese bloque reinicia los stocks de los insumos 5 y 2 antes de probar, porque si no los numeros esperados no salen.
  - Si el tiempo aprieta, lo que se recorta es el bloque 4.
  - NOTAS:
  - El bloque 1 crea el procedimiento, y conviene proyectarlo leyendo en voz alta el guardia y el GET DIAGNOSTICS, no pasarlo de largo.
  - CÓDIGO CITADO (referencia):
  - CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3])
  - CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3])
  - Fuera de la lamina (habla de la practica): Si el tiempo aprieta, lo que se recorta es el bloque 4, que el estudiante rehace en la pregunta 3 de la clase; lo que NO se recorta es la pareja de fotos del bloque 3.

**[Slide 25] Donde corre esto, y por que el autocommit ya no es el enemigo** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - ROW_COUNT, RAISE EXCEPTION con porcentaje y una funcion que devuelve BOOLEAN.
  - Nadie escribe BEGIN ni COMMIT: el CALL de nivel superior ya es su propia transaccion, y la excepcion que se propaga la deshace entera.
  - La demostracion de atomicidad no depende de dejar una transaccion abierta entre dos ejecuciones, que es justamente lo que un playground no permite; depende de tomar una foto, correr el CALL que falla y volver a tomar la foto, todo en el mismo panel.
  - Por lo mismo, la vieja advertencia de que en Oracle y en MySQL cualquier DDL provoca un COMMIT implicito —y que por eso no hay que mezclar CREATE TABLE con la demostracion— no aplica aqui: en PostgreSQL el DDL es transaccional.
  - NOTAS:
  - La herramienta de hoy es PostgreSQL en el navegador, que ejecuta PostgreSQL sobre PGlite dentro del navegador, y hay que decirlo sin ambiguedad porque este es el tema donde la herramienta equivocada no da un resultado distinto sino que no compila.
  - Nada de eso corre en Oracle Live SQL.
  - Sobre el autocommit, que en versiones anteriores de este material era la advertencia central.
  - Se menciona como diferencia entre motores, no como precaucion de la clase.
  - Lo que si hay que declarar es el limite real: PGlite corre UNA SOLA sesion, asi que la espera por bloqueo, el interbloqueo, la lectura sucia y la actualizacion perdida no se pueden reproducir y se documentan en papel como una linea de tiempo de T1 y T2 con lo que ve cada una en cada paso, formato que usara la Clase 10.
  - Tampoco se demuestra la durabilidad real, porque nadie puede apagar el servidor.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - Primera: si el motor confirma solo, para que sirve COMMIT.
  - Para agrupar varias sentencias en un unico hecho de negocio, que es justamente lo que el modo de confirmacion automatica impide; y hoy no hace falta escribirlo porque el CALL ya agrupa todo el procedimiento en una transaccion.
  - Segunda: que pasa si me desconecto sin confirmar.
  - El motor deshace la transaccion cuando la sesion muere de forma anormal, aunque algunos clientes confirman al salir de manera ordenada, asi que jamas se debe depender de eso.
  - Tercera: se puede hacer ROLLBACK despues de un COMMIT.
  - No, confirmar es definitivo, y lo unico que queda es restaurar desde el respaldo de la Clase 4 con recuperacion a un punto en el tiempo, operacion de administrador y no correccion de rutina.
  - Cuarta, y la que sale siempre en esta clase: si no escribo ROLLBACK, como se deshizo.
  - Porque el CALL de nivel superior es su propia transaccion y la excepcion que sale del procedimiento la aborta completa; el motor conserva las versiones anteriores de las filas y descarta las nuevas.
  - Quinta: entonces nunca se escribe COMMIT en un procedimiento de PostgreSQL.
  - Se puede, en procedimientos disenados para ejecutar por lotes y solo si el contexto de la llamada lo permite, pero no en un procedimiento de negocio como este, donde quitarle al llamador la posibilidad de deshacer es un defecto.
  - Sexta: por que la funcion devuelve falso en vez de lanzar una excepcion, si tambien es un fallo.
  - Porque no es un fallo: es un resultado.
  - La funcion esta pensada para que el llamador decida si sigue con las demas lineas o cancela, y esa decision no se puede tomar si la excepcion ya aborto todo.
  - Septima: puedo probar dos recepcionistas al mismo tiempo abriendo dos pestanas.
  - No, cada pestana levanta su propia base en memoria y no comparten nada; ese escenario se documenta en papel y se estudia en la Clase 10.
  - Fuera de la lamina (habla de la practica): Las tres preguntas de SQL del dia suman 75 de los 100 puntos y son PL/pgSQL: CALL, GET DIAGNOSTICS ...
  - Fuera de la lamina (habla de la practica): Nada de eso corre en Oracle Live SQL, asi que Live SQL se queda solamente como el contraste de sintaxis de la pregunta 4.
  - Fuera de la lamina (habla de la practica): Sobre el autocommit, que en versiones anteriores de este material era la advertencia central: con la forma del entregable de hoy deja de ser un problema, y conviene explicar por que en lugar de repetir la advertencia.


**Demo que usted debe poder repetir:** CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 8 · Tuning · Transacciones · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es una transaccion, y las dos amenazas de las que protege
5. Atomicidad: el fallo concreto en la clínica
6. Consistencia: valido es lo que las restricciones declaran
7. Aislamiento: el fallo mas facil de reproducir
8. Durabilidad: el registro de transacciones
9. La firma de sp_facturar, y por que recibe dos arreglos
10. Todo o nada: la transaccion de facturacion
11. sp_facturar en PL/pgSQL
12. El guardia del stock, sentencia por sentencia
13. Error del motor y error de negocio: se atienden distinto
14. Donde empieza y termina la transaccion de un CALL
15. Todo o nada: la transaccion explicita
16. Por que el procedimiento no lleva COMMIT ni ROLLBACK
17. El savepoint implicito del bloque EXCEPTION
18. SAVEPOINT: deshacer una parte sin perder el resto
19. El bloque EXCEPTION y la trampa de tragarse el error
20. El contraste con Oracle
21. Abortar o informar: fn_descontar_stock
22. fn_descontar_stock: cuando «no hay stock» es una respuesta, no un error
23. Tuning: habitos de escritura, no parametros del servidor
24. La demo, en el orden en que se proyecta
25. Donde corre esto, y por que el autocommit ya no es el enemigo
26. Demo del dia
27. Cierre · Clase 8

> Privado, no se proyecta: `Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Tuning · Transacciones · VetCare.»
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
- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde que se abrio. En PostgreSQL no hace falta escribir ROLLBACK dentro del procedimiento: el CALL de nivel superior es su propia transaccion, y si la excepcion se propaga hasta afuera, el motor deshace todo lo que el procedimiento habia hecho. En Oracle si hay que escribirlo, y ese contraste es la pregunta 4 del taller.
- Lo que si hay que escribir es el guardia: UPDATE insumo SET stock = stock - p_cantidades[i] WHERE id_insumo = p_insumos[i] AND stock >= p_cantidades[i], y despues GET DIAGNOSTICS v_filas = ROW_COUNT. Si v_filas es 0 no hubo stock, y ahi se decide: RAISE EXCEPTION si el fallo debe abortar la factura, o devolver FALSE si el 'no hay stock' es una respuesta y no un error.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 26]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 CALL sp_facturar que falla a mitad: foto inicial y foto final identicas, sin ROLLBACK escrito [[captura: salida-rollback-stock.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 8 - Tuning y transacciones/Taller PI - Clase 8 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Transaccion de negocio (factura + stock) + notas de tuning
Actividades:
1. Escribir sp_facturar(p_id_consulta, p_insumos INT[], p_cantidades INT[]) en PL/pgSQL: cabecera con total 0, bucle por linea con el guardia stock >= cantidad, y UPDATE del total al final.
2. Probar el fallo a mitad con ARRAY[3,2] / ARRAY[2,10] y demostrar con foto inicial y final que el stock del insumo 3 volvio a 40.
3. Encapsular el descuento en fn_descontar_stock, que devuelve BOOLEAN y no lanza excepcion.
4. Llenar la seccion Transacciones y tuning del informe: inventario de 3 transacciones y checklist de 7 items.
5. Declarar el gap de concurrencia: PGlite corre una sola sesion, y eso es la Clase 10.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 8/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 8 - VetCare.docx`. Clave para usted: `Quiz Clase 8 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 27]
**Decir:** «Queda visto: Tuning · Transacciones · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 27] slide de cierre. Dudas finales.


## Reparto del bloque y logistica (no se proyecta)

### El reparto de los 120 minutos y como acompanar el taller

El bloque de 120 minutos se reparte asi. Del minuto 0 al 10, encuadre y el amarre con la Clase 7: ayer se hizo que las consultas leyeran menos, hoy se hace que las escrituras no queden a medias. Del 10 al 30, ACID con sus cuatro fallos concretos, uno por letra, cada uno nombrando la tabla de VetCare donde ocurre; conviene no dedicar mas de cinco minutos por letra y no entrar en niveles de aislamiento mas alla de nombrarlos. Del 30 al 50, la firma del procedimiento y el guardia, sentencia por sentencia, con el codigo en pantalla. Del 50 al 60, por que no lleva COMMIT ni ROLLBACK, con el savepoint implicito y el contraste con Oracle: son los 10 puntos de la pregunta 4 y se resuelven en esta diapositiva. Del 60 al 70, la funcion y la distincion entre abortar e informar. Del 70 al 80, tuning y el checklist. Del 80 al 115, el taller. Del 115 al 120, cierre y el gancho de la Clase 10. Cuatro avisos para el acompanamiento. Uno, la pregunta 1 es la mas larga del taller y vale 35 puntos: conviene resolver en voz alta con el grupo la validacion de los arreglos y la cabecera con RETURNING, y dejar el bucle para el trabajo individual. Dos, el error de sintaxis mas frecuente es el delimitador de dolar mal cerrado; si alguien reporta un error incomprensible, lo primero que se revisa es que el $proc$ del final este igual al del principio. Tres, quien escriba COMMIT dentro del procedimiento tiene que entender por que sobra, no solo borrarlo, porque es la pregunta 4. Cuatro, la pregunta 5 son 15 puntos de prosa estructurada y se queda sin tiempo si nadie la anuncia: a los 100 minutos hay que decir en voz alta que faltan 15 y que el checklist necesita evidencias, no casillas.

## Codigo / scripts
Carpeta Codigo/ — archivo 08_transacciones_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 8/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
