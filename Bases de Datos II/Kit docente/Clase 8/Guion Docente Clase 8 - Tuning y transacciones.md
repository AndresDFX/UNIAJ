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


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): Las dos clases anteriores hicieron que las consultas leyeran menos. Hoy el foco pasa a las escrituras: que una factura con sus líneas y sus descuentos de stock quede completa o no quede, aunque algo falle a mitad.

CÓMO DARLA (≈4 min):
- Al entrar: Pregunta de arranque: «si el sistema registra la factura, descuenta una vacuna y se cae antes de la segunda línea, ¿qué queda en la base?». Deja que respondan; casi siempre dirán «la mitad».
- Después: Cierra: «hoy vamos a ver por qué no queda nada, y a demostrarlo con una foto antes y una foto después».

PASA A LA SIGUIENTE: Primero, qué es exactamente una transacción.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido de las dos horas: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] Que es una transaccion, y las dos amenazas de las que protege

QUÉ ES (dilo así): Una transacción es un grupo de sentencias que el motor trata como una sola: se aplican todas o ninguna. Facturar una consulta son varias sentencias (la cabecera, las líneas y los descuentos de stock), pero es un solo hecho de negocio, y por eso va en una sola transacción.

CÓMO DARLA (≈4 min):
- Al entrar: El bloque: BEGIN, el INSERT de la factura, el de su detalle, el UPDATE del stock y COMMIT o ROLLBACK. Lee la etiqueta: un solo hecho de negocio.
- Clic 1: Amenaza 1, la falla: si algo se cae a mitad, la transacción no puede quedar aplicada a medias.
- Clic 2: Amenaza 2, las otras sesiones: mientras la transacción trabaja, nadie más debe ver el estado intermedio, por ejemplo una factura sin líneas.
- Clic 3: Dónde empieza y termina: en PostgreSQL, sin BEGIN cada sentencia es su propia transacción y se confirma sola; en Oracle la transacción empieza sola con la primera sentencia que modifica datos y dura hasta el COMMIT o el ROLLBACK.

EJEMPLO: Facturar la consulta 4 con tres insumos son cinco sentencias: la cabecera, tres líneas con su descuento de stock y la actualización del total. Si una falla, no debe quedar ninguna.

SI PREGUNTAN:
- «Si PostgreSQL confirma solo, ¿para qué sirve COMMIT?» → Para agrupar varias sentencias en un único hecho: con BEGIN … COMMIT, todas se confirman juntas o ninguna.

CUIDADO: No enseñes la regla de Oracle («la transacción empieza sola») como si fuera la de PostgreSQL: aquí, sin BEGIN, cada sentencia ya quedó confirmada.

PASA A LA SIGUIENTE: Las cuatro propiedades de una transacción, empezando por la atomicidad.

### [Slide 5] Atomicidad: el fallo concreto en la clínica

QUÉ ES (dilo así): Atómico quiere decir indivisible. Si la facturación tiene cuatro pasos y el tercero falla, la base no debe guardar los dos primeros: o están los cuatro o no está ninguno.

CÓMO DARLA (≈3 min):
- Al entrar: La línea de tiempo: INSERT de la factura, INSERT de la línea 1, UPDATE del stock del insumo 1… y se cae la red antes de la línea 2.
- Clic 1: Sin atomicidad: la factura queda, la línea 1 queda, el stock quedó descontado y la línea 2 nunca llegó. Nadie recibe un error; el descuadre aparece semanas después en el inventario.
- Clic 2: Con atomicidad: la sesión murió sin COMMIT, así que el motor deshace todo. Cero facturas, cero líneas, stock intacto. La recepcionista repite la operación. Lee la conclusión.

EJEMPLO: Una factura que cobra dos productos con una sola línea registrada y un insumo descontado que nadie entregó: eso es lo que evita la atomicidad.

SI PREGUNTAN:
- «¿Qué pasa si me desconecto sin COMMIT?» → Si la sesión muere de forma anormal, el motor deshace la transacción. Algunos clientes confirman al cerrar de forma ordenada, así que nunca hay que depender de eso.

CUIDADO: Atomicidad no garantiza que los datos sean válidos; solo que no queden a medias. Eso es la lámina siguiente.

PASA A LA SIGUIENTE: Completa no quiere decir correcta: eso es la consistencia.

### [Slide 6] Consistencia: valido es lo que las restricciones declaran

QUÉ ES (dilo así): Consistencia quiere decir que después de la transacción la base sigue cumpliendo sus reglas. Pero el motor solo conoce las reglas que alguien declaró: si nadie escribió el CHECK, una transacción perfectamente atómica puede guardar un absurdo.

CÓMO DARLA (≈3 min):
- Al entrar: Sin restricción: UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 sobre un stock de 3. El contador baja a −7 y el COMMIT pasa sin quejarse: atómico, pero inválido.
- Clic 1: Con CHECK (stock >= 0) en la tabla: el mismo UPDATE se rechaza y el stock sigue en 3.
- Clic 2: Lee la idea: la atomicidad NO produce consistencia. La regla se declara una vez y vale para quien escriba SQL después.

EJEMPLO: Con el CHECK declarado, el motor responde: «new row for relation "insumo" violates check constraint "insumo_stock_check"» y en el detalle muestra la fila que habría quedado, con stock −7.

SI PREGUNTAN:
- «Si el procedimiento ya revisa el stock, ¿para qué el CHECK?» → Porque el CHECK vale también para el UPDATE manual o para otro programa que no use el procedimiento. El guardia del procedimiento evita llegar al error; el CHECK es la red de seguridad.
- «¿Y después del error puedo seguir en la misma transacción?» → En PostgreSQL no: toda sentencia siguiente responde «current transaction is aborted, commands ignored until end of transaction block» hasta el ROLLBACK. Oracle, en cambio, solo aborta la sentencia que falló.

CUIDADO: El malentendido más caro del tema es creer que la transacción garantiza las reglas de negocio. Solo garantiza las que están declaradas.

PASA A LA SIGUIENTE: La tercera letra: qué pasa cuando dos transacciones se cruzan.

### [Slide 7] Aislamiento: el fallo mas facil de reproducir

QUÉ ES (dilo así): Aislamiento quiere decir que, aunque dos transacciones trabajen a la vez, el resultado debe ser el mismo que si hubieran ido una detrás de la otra. El fallo más fácil de contar es la actualización perdida.

CÓMO DARLA (≈3 min):
- Al entrar: Quedan 3 vacunas. Recepción 1 y recepción 2 facturan 3 cada una, al mismo tiempo, y las dos leen stock = 3.
- Clic 1: Las dos calculan 3 − 3 = 0 y las dos escriben 0. Cada una confirmó una venta válida según lo que leyó.
- Clic 2: El resultado: stock 0 con seis vacunas vendidas y tres entregadas de aire. Lee la definición de aislamiento.

EJEMPLO: La defensa de diseño: UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3. La resta y la comprobación ocurren en una sola sentencia, que bloquea la fila mientras se ejecuta: la segunda recepción encuentra 0 y no descuenta.

SI PREGUNTAN:
- «¿Cuáles son los niveles de aislamiento?» → El estándar define cuatro: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ y SERIALIZABLE. PostgreSQL acepta los cuatro nombres, pero READ UNCOMMITTED se comporta como READ COMMITTED, que es el valor por omisión.
- «¿Lo podemos ver hoy en el navegador?» → No: ahí corre una sola sesión. Se documenta como una línea de tiempo de dos transacciones y se estudia en la Clase 10.

CUIDADO: Hoy solo se nombran los niveles; los fenómenos (lectura sucia, no repetible, fantasma, interbloqueo) son la Clase 10.

PASA A LA SIGUIENTE: La última letra: qué asegura que lo confirmado no se pierda.

### [Slide 8] Durabilidad: el registro de transacciones

QUÉ ES (dilo así): Durable quiere decir que, una vez que el motor dijo «confirmado», el dato no se pierde aunque se caiga el servidor. Lo logra con un registro de transacciones (WAL en PostgreSQL, redo log en Oracle) donde anota cada cambio antes de tocar las páginas de datos.

CÓMO DARLA (≈2 min):
- Al entrar: El cambio va primero al WAL, un archivo que solo se escribe al final, de corrido. El COMMIT termina cuando su registro (el verde) quedó grabado.
- Clic 1: Las páginas de datos se escriben después, sin prisa: el COMMIT no las esperó.
- Clic 2: Se cae el servidor. Al volver, el motor relee el WAL: aplica lo confirmado y descarta lo que quedó sin confirmar.
- Clic 3: La consecuencia práctica: confirmar fila por fila en una carga de 100.000 filas puede ser de 5 a 20 veces más lento que agrupar. Es orden de magnitud: se mide en cada motor.

EJEMPLO: El ROLLBACK tampoco es magia: PostgreSQL conserva la versión anterior de cada fila modificada y, al deshacer, se queda con ella.

SI PREGUNTAN:
- «¿Puedo hacer ROLLBACK después de un COMMIT?» → No. Confirmar es definitivo; lo único que queda es restaurar desde un respaldo (Clase 4).

CUIDADO: En el navegador no se puede demostrar la durabilidad: nadie puede apagar el servidor. Se explica, no se mide.

PASA A LA SIGUIENTE: Con ACID claro, el procedimiento que factura: su firma.

### [Slide 9] La firma de sp_facturar, y por que recibe dos arreglos

QUÉ ES (dilo así): Una factura tiene varias líneas, así que el procedimiento no recibe un insumo suelto: recibe dos arreglos emparejados por posición. El insumo de la posición 1 va con la cantidad de la posición 1, y así sucesivamente.

CÓMO DARLA (≈3 min):
- Al entrar: CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]): consulta 4, una unidad del insumo 1, dos del 6 y tres del 5. Las líneas punteadas emparejan cada posición.
- Clic 1: Lo primero del cuerpo: si los arreglos no miden lo mismo, RAISE EXCEPTION antes de tocar la base. Se usa IS DISTINCT FROM porque con un arreglo vacío array_length devuelve NULL, y con NULL el signo de distinto no da ni verdadero ni falso.
- Clic 2: La cabecera entra con total 0, porque todavía no se sabe, y RETURNING id_factura INTO v_id_factura evita otro SELECT. El total sale del bucle: 27.400.

EJEMPLO: CALL sp_facturar(4, ARRAY[1, 2], ARRAY[1]); se rechaza con «ERROR: insumos y cantidades deben tener la misma longitud» y no deja nada escrito.

SI PREGUNTAN:
- «¿Por qué INT y no NUMBER?» → NUMBER es de Oracle y en PostgreSQL no existe: se usa INT para los ids y NUMERIC para el dinero.
- «¿Por qué $proc$ y no $$?» → Cualquier etiqueta entre signos de dólar sirve; una con nombre evita choques si adentro hay otro bloque entre $$.

CUIDADO: Si se proyecta una firma con un solo insumo, la llamada con dos arreglos no compila contra ella.

PASA A LA SIGUIENTE: El procedimiento en código.

### [Slide 10] Todo o nada: la transaccion de facturacion

QUÉ ES (dilo así): Una versión corta de sp_facturar para ver el esqueleto: cabecera, bucle con el descuento condicional, el total al final y ningún COMMIT ni ROLLBACK adentro. La versión completa está en la lámina siguiente.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-4: la firma con los dos arreglos, LANGUAGE plpgsql y las variables v_id_factura y v_filas.
- Líneas 5-6: La cabecera con RETURNING id_factura INTO v_id_factura.
- Líneas 7-11: El bucle: el UPDATE con stock >= p_cantidades[i] en el WHERE, GET DIAGNOSTICS para saber cuántas filas tocó y RAISE EXCEPTION si fueron 0.
- Líneas 12-15: La línea de detalle con el precio leído de insumo, y el comentario clave de la línea 15: sin COMMIT ni ROLLBACK.
- Líneas 16-18: Al salir del bucle, el total de la cabecera es la suma de sus líneas: cantidad por precio.

EJEMPLO: Con el caso feliz, CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]) inserta tres líneas a 22.000, 900 y 1.200 y deja la factura con total 27.400,00. Con ARRAY[3, 2] y ARRAY[2, 10] responde «ERROR: stock insuficiente» y no queda nada: ni cabecera ni el descuento del insumo 3.

CUIDADO: No la presentes como la versión final: le faltan la validación de los arreglos y el NOT FOUND del insumo, y su mensaje de error no dice qué insumo faltó.

PASA A LA SIGUIENTE: La versión completa, parte por parte.

### [Slide 11] sp_facturar en PL/pgSQL

QUÉ ES (dilo así): La versión completa del procedimiento, recorrida de arriba abajo. Cada parte tiene una razón: rechazar una llamada mal hecha, registrar la cabecera, cobrar línea por línea con el precio vigente y dejar el total correcto.

CÓMO DARLA (≈2 min):
- Al entrar: La llamada de prueba arriba y la parte 1: validar que los arreglos midan lo mismo.
- Parte 2 y 3: La cabecera con total 0 y el bucle: SELECT precio_unit INTO v_precio con IF NOT FOUND; el UPDATE con el guardia; GET DIAGNOSTICS; RAISE si fue 0; INSERT de la línea; v_total := v_total + v_precio * cantidad (el := es la asignación de PL/pgSQL).
- Parte 4 y abajo: UPDATE factura SET total = v_total. Resultado: 27.400, y los stocks de los insumos 1, 6 y 5 pasan de 12, 60 y 8 a 11, 58 y 5.

EJEMPLO: CALL sp_facturar(4, ARRAY[99], ARRAY[1]); responde «ERROR: el insumo 99 no existe»: sin el NOT FOUND, v_precio quedaría NULL y la factura terminaría con total NULL.

SI PREGUNTAN:
- «¿Por qué el precio se lee de la tabla y no se recibe como parámetro?» → Porque se cobra el precio vigente, no el que la aplicación crea recordar.
- «¿Por qué el mensaje sale como «ERROR: ERROR: …»?» → Porque el texto del RAISE ya empieza con «ERROR:» y el motor antepone el suyo. Es solo el texto; no son dos errores.

CUIDADO: El error de sintaxis más común es cerrar el cuerpo con una etiqueta distinta de la que lo abrió: $proc$ al principio y $proc$ al final.

PASA A LA SIGUIENTE: El corazón del procedimiento: el guardia del stock.

### [Slide 12] El guardia del stock, sentencia por sentencia

QUÉ ES (dilo así): El descuento de stock no se hace en dos pasos (leer y luego escribir) sino en uno: el UPDATE solo toca la fila si alcanza. Después, ROW_COUNT dice si la tocó. Ese cero no es un error del motor: es la señal de que no había stock, y el procedimiento la convierte en excepción.

CÓMO DARLA (≈3 min):
- Al entrar: Las cuatro sentencias dentro del bucle, numeradas, con la condición del WHERE resaltada: comprobar y escribir en una sola sentencia.
- Clic 1: Caso que alcanza: insumo 3, hay 40 y se piden 2. ROW_COUNT = 1, el stock pasa a 38 y el bucle sigue.
- Clic 2: Caso que no alcanza: insumo 2, hay 3 y se piden 10. ROW_COUNT = 0, el stock queda intacto y se lanza la excepción. Lee la nota: el precio se lee de la tabla.

EJEMPLO: El mensaje real: «ERROR: stock insuficiente del insumo 2 (se pidieron 10)». Cada % del RAISE se reemplaza por los argumentos, en orden.

SI PREGUNTAN:
- «¿Por qué no SQL%ROWCOUNT?» → Es de Oracle. En PL/pgSQL se pregunta con GET DIAGNOSTICS v_filas = ROW_COUNT, y esa diferencia decide si el código compila.

CUIDADO: Si alguien escribe stock > cantidad en vez de >=, pedir exactamente lo que queda falla: el caso límite lo delata.

PASA A LA SIGUIENTE: Ese cero filas no es un error para el motor: hay dos clases de error.

### [Slide 13] Error del motor y error de negocio: se atienden distinto

QUÉ ES (dilo así): Hay dos clases de fallo a mitad de transacción. El motor detecta solo lo que viola sus reglas declaradas y aborta por su cuenta. Lo que solo es una regla de negocio, como «no hay stock suficiente», el motor no lo ve: hay que convertirlo en excepción.

CÓMO DARLA (≈3 min):
- Al entrar: Error del motor: CHECK, clave foránea, tipo incompatible, interbloqueo. El motor lanza y aborta solo.
- Clic 1: Error de negocio: stock insuficiente, mascota inactiva, un total que no cuadra. Un UPDATE que no toca filas es una sentencia exitosa: el RAISE EXCEPTION lo pones tú.
- Clic 2: Nada de capturar y silenciar: EXCEPTION WHEN OTHERS THEN NULL convierte el fallo en silencio. Si se captura, se relanza con RAISE a secas.

EJEMPLO: Un UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 AND stock >= 10 devuelve «0 filas afectadas», sin error. Solo el procedimiento sabe que eso significa «no hay stock».

SI PREGUNTAN:
- «¿Y si quiero cobrar las demás líneas aunque una falle?» → Existe el SAVEPOINT: deshacer solo esa línea y seguir. Hoy la regla es todo o nada, pero conviene saber que la opción existe.

CUIDADO: El mensaje debe nombrar el insumo concreto: quien lea el error tiene que poder decir qué línea falló.

PASA A LA SIGUIENTE: Cuando la excepción sale del procedimiento, ¿qué se deshace y quién lo hace?

### [Slide 14] Donde empieza y termina la transaccion de un CALL

QUÉ ES (dilo así): Un CALL escrito por fuera de cualquier BEGIN es una transacción completa. Si dentro del procedimiento salta una excepción y nadie la atrapa, sale del CALL y el motor deshace todo lo que ese CALL había hecho: cabecera, líneas y descuentos.

CÓMO DARLA (≈3 min):
- Al entrar: CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]) dentro de su recuadro: una sola transacción. Se inserta la cabecera y el insumo 3 baja de 40 a 38: alcanzaba.
- Clic 1: El insumo 2 tiene 3 y se piden 10: RAISE EXCEPTION, y la excepción sale del CALL.
- Clic 2: El motor deshace todo: no queda factura y el insumo 3 vuelve a 40 solo. Lee la conclusión: confirma el llamador.

EJEMPLO: Fotos reales: antes del CALL, 1 factura, 3 líneas, stock_3 = 40 y stock_2 = 3; después, exactamente lo mismo. La siguiente factura que sí se crea sale con id_factura 3, no 2: el intento fallido consumió el 2 de la secuencia, y las secuencias no se deshacen.

SI PREGUNTAN:
- «¿Por qué el id saltó del 1 al 3?» → Porque nextval de una secuencia no se deshace con el ROLLBACK, para que dos sesiones nunca reciban el mismo número. Los huecos son normales.

CUIDADO: No digas que la reversión «no se puede demostrar en el navegador»: se demuestra con una foto antes y una después del CALL que falla.

PASA A LA SIGUIENTE: Y cuando sí se quiere agrupar a mano: la transacción explícita.

### [Slide 15] Todo o nada: la transaccion explicita

QUÉ ES (dilo así): La misma idea sin procedimiento: BEGIN abre la transacción, las sentencias se acumulan y COMMIT las confirma juntas. Hasta el COMMIT, nadie más ve los cambios.

CÓMO DARLA (≈2 min):
- Al entrar: Línea 1: BEGIN. Líneas 3-4: la cabecera con RETURNING, que muestra el id generado.
- Líneas 6-11: La línea de detalle (2 gasas a 1.200), el descuento de stock y el total de la cabecera, 2.400. currval devuelve el id que esta misma sesión acaba de generar.
- Línea 13: COMMIT: las cuatro sentencias quedan juntas. Con ROLLBACK, o si cualquiera falla, no queda ninguna.

EJEMPLO: Con los datos de la clase, después del COMMIT la factura queda con total 2.400,00 y la gasa estéril baja de 8 a 6.

SI PREGUNTAN:
- «¿currval puede devolver el id de otra persona?» → No: currval es por sesión; devuelve el último valor que generó ESTA sesión.

CUIDADO: Entre el BEGIN y el COMMIT no se espera a nadie: una transacción abierta sostiene bloqueos.

PASA A LA SIGUIENTE: ¿Y si eso mismo se pone dentro del procedimiento?

### [Slide 16] Por que el procedimiento no lleva COMMIT ni ROLLBACK

QUÉ ES (dilo así): El procedimiento no decide cuándo confirmar: lo decide quien lo llama. Llamado con un CALL suelto, el CALL es la transacción y la excepción la deshace. Llamado dentro de una transacción abierta, intentar confirmar desde adentro es un error.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba, el CALL suelto: es su propia transacción; la excepción que sale deshace cabecera, líneas y stock, y nadie escribió ROLLBACK.
- En el medio: El CALL dentro de BEGIN … COMMIT: el que decide es ese COMMIT de afuera. Si el procedimiento intenta un COMMIT propio, el motor responde «invalid transaction termination»; lo mismo dentro de un bloque con EXCEPTION.
- Abajo: La regla: confirma uno solo, el llamador. Y si se atrapa el error, se relanza con RAISE; nunca WHEN OTHERS THEN NULL.

EJEMPLO: Prueba real con un CALL suelto: un procedimiento que descuenta el insumo 3, hace COMMIT, descuenta el insumo 4 y después falla deja el 3 descontado (40 → 39) y el 4 intacto: justo la factura a medias que se quería evitar. Y con BEGIN; CALL …; el COMMIT de adentro responde «invalid transaction termination».

SI PREGUNTAN:
- «Entonces, ¿nunca se escribe COMMIT en un procedimiento de PostgreSQL?» → Se puede en procesos por lotes y solo si el CALL es de nivel superior. En un procedimiento de negocio como este es un defecto: le quita al llamador la posibilidad de deshacer.

CUIDADO: No afirmes que PostgreSQL prohíbe siempre el ROLLBACK dentro de un procedimiento: con un CALL suelto lo permite. Lo que no permite es terminar la transacción desde adentro cuando el CALL está dentro de otra o de un bloque con EXCEPTION.

PASA A LA SIGUIENTE: El otro mecanismo que deshace sin que nadie lo escriba: el savepoint implícito.

### [Slide 17] El savepoint implicito del bloque EXCEPTION

QUÉ ES (dilo así): En PL/pgSQL, un bloque que tiene sección EXCEPTION marca un punto de retorno al entrar. Si algo falla adentro, el motor vuelve a ese punto (deshace lo del bloque) y ejecuta el manejador. Lo que se escribió antes del bloque no se toca.

CÓMO DARLA (≈3 min):
- Al entrar: La transacción: la escritura A, y luego el bloque BEGIN … EXCEPTION con su bandera (el savepoint implícito) y la escritura B adentro.
- Clic 1: Algo falla dentro del bloque: se vuelve al savepoint, B se deshace y corre el manejador. A se conserva.
- Clic 2: La lección: capturar no es lo mismo que dejar propagar. Y el costo: dentro de un bucle, un savepoint por vuelta; manejadores solo donde hay una decisión que tomar.

EJEMPLO: DO $$ BEGIN CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 10]); EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Fallo esperado: %', SQLERRM; END $$; imprime «Fallo esperado: ERROR: stock insuficiente del insumo 2 (se pidieron 10)» y la base queda igual: el savepoint deshizo lo del CALL.

SI PREGUNTAN:
- «¿Qué es SQLERRM?» → La variable con el texto del error que se atrapó. Sirve para que el aviso diga algo útil en vez de «falló».

CUIDADO: Ese DO con manejador es para que un script siga corriendo y se pueda medir, no para arreglar el error.

PASA A LA SIGUIENTE: El savepoint también se puede escribir a mano.

### [Slide 18] SAVEPOINT: deshacer una parte sin perder el resto

QUÉ ES (dilo así): Un SAVEPOINT es una marca con nombre dentro de la transacción. ROLLBACK TO SAVEPOINT vuelve a esa marca sin deshacer lo anterior, y la transacción sigue viva.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-3: BEGIN, la cabecera y la marca antes_del_detalle.
- Líneas 4-7: Una línea con el insumo 9999, que no existe: la clave foránea la rechaza con el error de las líneas 6 y 7.
- Líneas 8-11: ROLLBACK TO SAVEPOINT: la cabecera sigue viva. Se inserta la línea correcta (insumo 5) y COMMIT.

EJEMPLO: Resultado: la factura con una línea de 1 gasa. Sin el ROLLBACK TO SAVEPOINT, cualquier sentencia después del error respondería «current transaction is aborted».

SI PREGUNTAN:
- «¿Cuándo usaría esto en la clínica?» → En una factura de varias líneas donde se acepta cobrar las que sí alcanzan y avisar de la que no. Hoy la regla es todo o nada, así que no se usa.

CUIDADO: En esta versión la cabecera queda con total 0: el ejemplo muestra el SAVEPOINT, no el cálculo del total.

PASA A LA SIGUIENTE: Y la trampa de atrapar el error sin relanzarlo.

### [Slide 19] El bloque EXCEPTION y la trampa de tragarse el error

QUÉ ES (dilo así): Un bloque que atrapa el error y solo avisa deshace su parte, pero deja confirmado lo que estaba antes. El resultado puede ser una factura sin líneas que nadie notó.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-3: el DO y la cabecera, fuera del bloque interno.
- Líneas 4-10: El bloque con EXCEPTION: descuenta una gasa e inserta una línea con un insumo que no existe. El manejador solo imprime un aviso: es la trampa.
- Líneas 12-15: El efecto: el bloque se deshizo (el stock quedó igual), pero el DO terminó bien y la cabecera quedó guardada sin líneas. La corrección: EXCEPTION WHEN OTHERS THEN RAISE;

EJEMPLO: Prueba real: el aviso dice «algo fallo: insert or update on table "detalle_factura" violates foreign key constraint …», queda una factura con 0 líneas y la gasa conserva su stock. Con RAISE en el manejador, el DO falla y no queda ninguna factura nueva.

CUIDADO: El síntoma de esta trampa no es un error: es una factura con total 0 y sin líneas que aparece días después.

PASA A LA SIGUIENTE: Por qué todo esto se escribe distinto en Oracle.

### [Slide 20] El contraste con Oracle

QUÉ ES (dilo así): Oracle sigue siendo un motor importante y por eso se compara, pero el motor del curso es PostgreSQL. La misma lógica de facturación necesita cuatro cambios de sintaxis para pasar de un motor al otro, y además cambia quién confirma.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre fila por fila: tipos, filas afectadas, cómo se aborta, qué se hace al fallar y quién confirma.
- Abajo: La respuesta a «¿por qué la base quedó intacta?»: el CALL es su propia transacción y la excepción propagada la deshace entera. Ningún ROLLBACK escrito lo hizo.

EJEMPLO: En Oracle: EXCEPTION WHEN OTHERS THEN ROLLBACK; RAISE;. En PostgreSQL ese bloque no hace falta: sin manejador, la excepción sale del CALL y deshace todo.

SI PREGUNTAN:
- «¿PostgreSQL guarda una copia de cada tabla antes del CALL?» → No. Conserva la versión anterior de cada fila que cambia (MVCC) y, al deshacer, se queda con ella.
- «¿Los UPDATE se acumulan en memoria y se escriben al final?» → No. Cada sentencia se aplica cuando se ejecuta y se ve dentro de la misma transacción; lo que se decide al final es confirmarla o no.

CUIDADO: Enseñar la forma de Oracle como si fuera la del curso es el error que más cuesta: no compila en PostgreSQL.

PASA A LA SIGUIENTE: La misma regla de stock con otro contrato: informar en vez de abortar.

### [Slide 21] Abortar o informar: fn_descontar_stock

QUÉ ES (dilo así): Hay dos maneras de responder «no hay stock». El procedimiento lo trata como un fallo y aborta todo. La función lo trata como un resultado: devuelve verdadero o falso y deja que quien la llama decida si sigue con las demás líneas.

CÓMO DARLA (≈3 min):
- Al entrar: La misma regla arriba (el UPDATE con el guardia) y el primer contrato: sp_facturar, 0 filas → RAISE EXCEPTION, se deshace toda la factura.
- Clic 1: El segundo contrato: fn_descontar_stock RETURNS BOOLEAN, RETURN v_filas = 1. Si no alcanza devuelve false, sin excepción.
- Clic 2: Cuatro llamadas reales: (5, 3) → true, hay 8 y quedan 5; (2, 10) → false, hay 3; (2, 3) → true, pide justo lo que queda; (5, 0) → error, porque una cantidad no positiva es una llamada mal hecha.

EJEMPLO: fn_descontar_stock(5, 0) responde «ERROR: la cantidad debe ser positiva (llego 0)». El false se reserva para «no alcanza».

SI PREGUNTAN:
- «¿Por qué devolver false si también es un fallo?» → Porque para quien llama es un resultado: puede decidir seguir con otras líneas o cancelar. Si la función lanzara la excepción, esa decisión ya no se podría tomar.

CUIDADO: El caso límite (2, 3) es el que delata un guardia escrito con > en vez de >=: devolvería false.

PASA A LA SIGUIENTE: La función completa y su prueba en una sola consulta.

### [Slide 22] fn_descontar_stock: cuando «no hay stock» es una respuesta, no un error

QUÉ ES (dilo así): La función tiene tres partes cortas y se prueba en una sola consulta con tres casos. Lo que la hace segura es lo mismo que en el procedimiento: la condición viaja dentro del UPDATE.

CÓMO DARLA (≈2 min):
- Al entrar: La firma y las tres partes: p_cantidad <= 0 → RAISE; el UPDATE con el guardia; GET DIAGNOSTICS y RETURN v_filas = 1, que devuelve directamente el resultado de la comparación.
- En el medio: La prueba con stocks 8 y 3: SELECT fn_descontar_stock(5, 3) AS caso_ok, fn_descontar_stock(2, 10) AS caso_sin_stock, fn_descontar_stock(2, 3) AS caso_limite; → true | false | true. Después: insumo 5 en 5 e insumo 2 en 0.
- Abajo: La ventana: si se lee el stock y luego se decide, dos recepciones pueden leer 3 a la vez y las dos descontar. Con la condición en el WHERE no hay ventana.

EJEMPLO: Antes de la prueba se reinician los stocks (insumo 5 en 8 e insumo 2 en 3); si no, los valores esperados no salen.

SI PREGUNTAN:
- «¿Puedo probar la ventana con dos pestañas del navegador?» → No: cada pestaña levanta su propia base en memoria y no comparten nada. Se documenta en papel y se estudia en la Clase 10.

CUIDADO: Distinguir el dato inválido (cantidad cero o negativa, excepción) del resultado negativo (no alcanza, false) es la mitad del tema.

PASA A LA SIGUIENTE: Tuning: hábitos de escritura que evitan problemas.

### [Slide 23] Tuning: habitos de escritura, no parametros del servidor

QUÉ ES (dilo así): Aquí tuning no es mover parámetros del servidor, que en el navegador no se puede y sin medición es peligroso. Son hábitos de escritura con números: transacciones cortas, lotes razonables y filtros que tocan pocas filas.

CÓMO DARLA (≈3 min):
- Al entrar: Bien: leer y validar primero, sin transacción, y abrir BEGIN … COMMIT solo para escribir. Dura milisegundos.
- Clic 1: Mal: abrir la transacción, mostrar un «¿confirmar?» y que la recepcionista se vaya a almorzar. Esas filas quedan bloqueadas para el resto de la clínica mientras nadie vuelve.
- Clic 2: Cargas masivas: COMMIT por lotes, del orden de 1.000 a 5.000 filas como convención de oficio. Ni uno por fila, que es lentísimo, ni uno solo para un millón.

EJEMPLO: UPDATE insumo SET stock = stock - 2 WHERE id_insumo = 3 filtra por la clave primaria y bloquea una sola fila; el mismo UPDATE filtrando por una columna sin índice tiene que recorrer la tabla para encontrar las filas.

SI PREGUNTAN:
- «¿Cuánto es «corta»?» → Del orden de milisegundos a unos cientos de milisegundos. Cualquier cosa que sostenga bloqueos durante segundos es sospechosa.

CUIDADO: No prometas cifras exactas de mejora: los tamaños de lote y los tiempos se miden en cada motor.

PASA A LA SIGUIENTE: Vamos a la demo, en el orden en que se proyecta.

### [Slide 24] La demo, en el orden en que se proyecta

QUÉ ES (dilo así): El script tiene cinco bloques y el valor está en el tercero: hay que administrar el tiempo para llegar ahí con calma.

CÓMO DARLA (≈1 min):
- Al entrar: Bloques 0 a 2: el esquema (se puede correr dos veces porque empieza con los DROP), el procedimiento leído en voz alta y el caso feliz, 27.400.
- Bloque 3: Foto inicial (1 | 3 | 40 | 3), el CALL que falla dentro de un DO con manejador y la foto final idéntica. Pregunta al grupo dónde quedó el descuento del insumo 3. Cierra con la factura viable: 112.000, insumo 3 en 38 e insumo 2 en 0.

EJEMPLO: La factura viable sale con id_factura 3: el intento fallido consumió el 2 de la secuencia.

CUIDADO: Si el tiempo aprieta se recorta el bloque 4; nunca la pareja de fotos del bloque 3.

PASA A LA SIGUIENTE: Qué se puede demostrar en el navegador y qué no.

### [Slide 25] Donde corre esto, y por que el autocommit ya no es el enemigo

QUÉ ES (dilo así): Todo el código de hoy es PL/pgSQL y corre en PostgreSQL dentro del navegador. Como el CALL ya es su propia transacción, no hace falta dejar una transacción abierta entre dos ejecuciones para demostrar la atomicidad.

CÓMO DARLA (≈1 min):
- Al entrar: Izquierda, lo que corre: CALL, GET DIAGNOSTICS, RAISE, la función BOOLEAN, las fotos y el DDL dentro de una transacción. Derecha, lo que no: dos sesiones a la vez (espera por bloqueo, interbloqueo, actualización perdida) y apagar el servidor. Eso se documenta en papel y es la Clase 10.

CUIDADO: En PostgreSQL el DDL es transaccional: la vieja advertencia de que un CREATE TABLE confirma solo (Oracle, MySQL) no aplica aquí; se menciona como diferencia entre motores.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 26] Demo del dia

QUÉ ES (dilo así): La demo corre el script de la clase y demuestra la atomicidad con dos fotos de la misma consulta, antes y después de un CALL que falla a mitad.

CÓMO DARLA (≈15 min):
- Al entrar: 1) Esquema y seis insumos. 2) El procedimiento, leyendo el guardia y el GET DIAGNOSTICS. 3) CALL sp_facturar(4, ARRAY[1, 6, 5], ARRAY[1, 2, 3]): 27.400 y stocks 11, 58 y 5.
- Después: 4) Foto inicial: 1 | 3 | 40 | 3. 5) El CALL con ARRAY[3, 2] y ARRAY[2, 10] dentro de un DO con manejador: «Fallo esperado: ERROR: stock insuficiente del insumo 2 (se pidieron 10)». 6) Foto final: 1 | 3 | 40 | 3. 7) Si hay tiempo, la función: true | false | true.

EJEMPLO: Después de las fotos, CALL sp_facturar(4, ARRAY[3, 2], ARRAY[2, 3]) crea la factura por 112.000 (9.500×2 + 31.000×3) y deja el insumo 3 en 38 y el 2 en 0.

CUIDADO: Sin la foto inicial no hay demostración: hay que tomarla antes del CALL que falla, con exactamente la misma consulta que la final.

PASA A LA SIGUIENTE: Cierre de la clase.


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
