# Guion docente · Clase 10 · Control de concurrencia · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Escenarios de concurrencia del PI documentados
- **Entregable de hoy:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion
- **Herramienta:** ExamLab (PostgreSQL/PGlite) + Google Docs
- **Slides:** Clases/Clase 10 - Control de concurrencia/Presentacion.pptx
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

QUÉ ES (dilo así): Hoy la pregunta es qué pasa cuando dos personas modifican el mismo dato al mismo tiempo. La base no se daña: cumple las dos órdenes aunque se contradigan. La clase muestra las cuatro formas de decirle que no.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema y haz la pregunta de arranque: «dos recepcionistas agendan con la misma veterinaria a la misma hora, en el mismo segundo: ¿qué guarda la base?». Toma una o dos respuestas sin corregir todavía.
- Después: Cierra: «al final van a poder nombrar el fenómeno, el nivel de aislamiento que lo tapa y la línea de SQL que lo hace imposible».

CUIDADO: Esta clase cae en festivo y es autónoma: si la grabas, este guion es el de la grabación; si no, el estudiante la estudia con las láminas y estas notas, así que cada una tiene que entenderse sola.

PASA A LA SIGUIENTE: Empezamos por lo que ya se vio en la Clase 8: la transacción.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido de las dos horas: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] La transaccion como unidad de todo o nada

QUÉ ES (dilo así): Una transacción es un grupo de sentencias que el motor trata como un solo hecho: o se confirman todas con COMMIT o se deshacen todas con ROLLBACK. Eso la protege de quedar a medias, pero no de otra transacción que trabaja al mismo tiempo sobre los mismos datos. Cuando hay dos a la vez, el motor intercala sus operaciones, y de ese intercalado salen todos los problemas de hoy.

CÓMO DARLA (≈5 min):
- Al entrar: Todo o nada: agendar la cita (INSERT INTO cita) y descontar la vacuna (UPDATE insumo) son un solo hecho. Con COMMIT quedan las dos; si la segunda falla, ROLLBACK y no queda ninguna. Pregunta: «¿qué pasa si queda la cita y no el descuento?» (el inventario miente).
- Clic 1: Dos transacciones a la vez: la recepción A (T1) y la recepción B (T2) preguntan si la veterinaria Restrepo tiene libre las 10:00. Las dos reciben 0 filas. Subraya que las dos leen antes de que ninguna escriba.
- Clic 2: Las dos insertan su cita (Mishi y Toby) y las dos confirman con COMMIT, sin ningún error. Cada una decidió con un dato que la otra estaba a punto de cambiar.
- Clic 3: El resultado: dos filas en cita a las 10:00 con la misma veterinaria. La base no está dañada: cumplió dos órdenes contradictorias porque nada le dijo que no podía. El resto de la clase son las formas de decírselo.

EJEMPLO: Con varias recepcionistas y unas 150 citas al día, que dos agenden la misma franja en el mismo segundo no es una rareza: es cuestión de tiempo.

SI PREGUNTAN:
- «¿Y si pongo BEGIN y COMMIT alrededor del SELECT y el INSERT?» → Sigue pasando. En READ COMMITTED, el nivel por omisión de PostgreSQL, cada transacción solo ve lo confirmado: las dos leen «libre» antes de que la otra confirme. La transacción da atomicidad, no exclusión.
- «¿El motor no debería detectar la doble cita?» → Solo si se le dice qué es inválido, con una restricción UNIQUE sobre (id_veterinario, fecha_hora). Sin ella, dos citas a la misma hora son datos perfectamente válidos.

CUIDADO: El error típico del docente es afirmar que «poner una transacción» resuelve la concurrencia. No la resuelve: garantiza que las sentencias de UNA transacción se apliquen juntas, nada más.

PASA A LA SIGUIENTE: Si el problema es que se intercalan, ¿por qué no ejecutar una detrás de otra? Existe, y cuesta.

### [Slide 5] Serializar de verdad existe, y cuesta

QUÉ ES (dilo así): La solución obvia es no intercalar: ejecutar las transacciones una detrás de otra. Eso se llama serializar, y funciona, pero convierte ocho operaciones simultáneas en una fila de ocho. Por eso el estándar SQL ofrece una perilla, el nivel de aislamiento, para elegir cuánto se protege cada transacción de las demás a cambio de cuánto rendimiento.

CÓMO DARLA (≈3 min):
- Al entrar: Ocho agendamientos a la vez terminan juntos: una unidad de tiempo para todos.
- Clic 1: Los mismos ocho en fila: cada uno espera al anterior y el último tarda ocho veces más. En recepción eso se siente como «el sistema está lento».
- Clic 2: La pregunta que define el aislamiento: ¿qué puede ver mi transacción de las otras que todavía no terminan? Es la I de ACID y la única de las cuatro que el desarrollador configura; atomicidad, consistencia y durabilidad las garantiza el motor siempre.

EJEMPLO: En PostgreSQL se pide con BEGIN ISOLATION LEVEL SERIALIZABLE. El motor no pone a todas en fila literalmente: las deja correr en paralelo y, si el resultado no equivale a ningún orden de una tras otra, aborta una con un error de serialización que la aplicación debe reintentar.

SI PREGUNTAN:
- «¿Entonces siempre conviene SERIALIZABLE?» → No: se paga en transacciones abortadas que hay que reintentar. Se usa donde la anomalía cuesta más que el reintento.
- «¿Qué significa cada letra de ACID?» → Atomicidad (todo o nada), Consistencia (las reglas se cumplen), Aislamiento (qué se ve de las otras) y Durabilidad (lo confirmado sobrevive a una caída).

CUIDADO: No presentes SERIALIZABLE como la respuesta universal: el estudiante aprende que el aislamiento es gratis y no reconoce el síntoma opuesto (esperas, reintentos, tiempos de espera agotados).

PASA A LA SIGUIENTE: Para elegir el nivel hay que conocer las anomalías que existen: son tres.

### [Slide 6] Los tres fenomenos indeseables, en escenas de la clinica

QUÉ ES (dilo así): El estándar SQL nombra tres cosas que pueden salir mal cuando una transacción ve el trabajo de otra. Se entienden mejor con una escena de la clínica, y la diferencia entre las dos últimas es la pregunta de examen más fallada.

CÓMO DARLA (≈5 min):
- Al entrar: Lectura sucia: T1 inserta la cita de las 10:00 sin hacer COMMIT; T2 la ve y le dice al dueño que la franja está ocupada; luego T1 hace ROLLBACK porque el pago no pasó. T2 decidió con un dato que nunca existió.
- Clic 1: Lectura no repetible: dentro de una facturación, T1 lee el stock del insumo 2 (Vacuna triple felina) y obtiene 3; T2 vende 3 y confirma; T1 relee la misma fila y obtiene 0. Misma consulta, misma transacción, dos valores.
- Clic 2: Fantasma: T1 cuenta las citas del martes y obtiene 4; T2 inserta otra y confirma; T1 vuelve a contar y obtiene 5. Ninguna fila vieja cambió: apareció una nueva que cumple el WHERE.

EJEMPLO: La doble reserva del comienzo se parece al fantasma: las dos preguntan «¿hay alguna cita a esa hora?» y la fila que cambiaría la respuesta todavía no existe cuando preguntan.

SI PREGUNTAN:
- «¿En PostgreSQL puede pasar la lectura sucia?» → No. Aunque se pida READ UNCOMMITTED, PostgreSQL nunca muestra datos sin confirmar: lo trata como READ COMMITTED.
- «¿Cómo distingo no repetible de fantasma en un ejercicio?» → Pregunta si la fila ya existía. Si existía y cambió su valor, es no repetible; si apareció o desapareció una fila del resultado, es fantasma.

CUIDADO: No digas que la lectura sucia es la más común: en PostgreSQL es imposible. Las que sí aparecen con el nivel por omisión son la no repetible y la fantasma.

PASA A LA SIGUIENTE: Veamos la doble reserva en dos líneas de tiempo.

### [Slide 7] Doble reserva sin control de concurrencia

QUÉ ES (dilo así): La misma doble reserva, en dos líneas de tiempo: cada transacción lee «libre», inserta y confirma. Es una condición de carrera: el resultado depende de quién llega primero, y aquí las dos llegan antes de que la otra confirme.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba T1: lee la franja libre, inserta y su COMMIT sale bien. Abajo T2 hace exactamente lo mismo y su COMMIT deja la doble reserva. Subraya que ningún paso de T2 da error.
- Nota inferior: Lee la mitigación: con UNIQUE (id_veterinario, fecha_hora) el segundo INSERT falla en vez de crear la doble reserva. Se ve en código al final del bloque.

EJEMPLO: Así se documenta un escenario de concurrencia que no se puede ejecutar: una tabla con columnas paso, T1, T2 y estado de la fila, en orden de tiempo.

SI PREGUNTAN:
- «¿Por qué no se puede ver esto en la base del curso?» → Porque PostgreSQL en el navegador tiene una sola sesión: no hay dos transacciones abiertas a la vez. Se demuestra lo que sí se puede (que la base acepta el dato inválido y que la restricción lo rechaza) y el cruce se documenta en la línea de tiempo.

CUIDADO: Validar con «si COUNT(*) = 0, inserto» dentro de un procedimiento tampoco lo evita: entre el SELECT y el INSERT cabe la otra transacción.

PASA A LA SIGUIENTE: ¿Qué nivel de aislamiento tapa cada fenómeno? Los cuatro niveles.

### [Slide 8] Los cuatro niveles de aislamiento se definen por lo que permiten

QUÉ ES (dilo así): Los cuatro niveles del estándar no se memorizan como lista: se definen por cuáles de los tres fenómenos permiten, y cada uno tapa uno más que el anterior. Subir de nivel nunca es gratis: se paga en esperas o en transacciones abortadas.

CÓMO DARLA (≈5 min):
- Al entrar: La tabla tiene las tres anomalías como columnas; rojo significa «puede ocurrir». READ UNCOMMITTED: rojo en las tres. En PostgreSQL se puede pedir, pero se comporta como READ COMMITTED: nunca muestra datos sin confirmar.
- Clic 1: READ COMMITTED: verde en lectura sucia, rojo en las otras dos. Es el nivel por omisión de PostgreSQL (también de Oracle y SQL Server): el que tiene cualquier base que nadie configuró. Cada sentencia ve una foto nueva de lo confirmado.
- Clic 2: REPEATABLE READ: impide también la no repetible, porque toda la transacción trabaja sobre la foto tomada al empezar. El estándar todavía permite fantasmas; PostgreSQL no los deja ver, por esa misma foto.
- Clic 3: SERIALIZABLE: verde en las tres; el resultado equivale a ejecutar una tras otra. Cuando PostgreSQL detecta que eso no se cumple, aborta una con un error de serialización y la aplicación debe reintentarla.

EJEMPLO: Pregunta al grupo: con READ COMMITTED, si en una facturación leo dos veces el stock del insumo 2, ¿puedo obtener 3 y luego 0? (Sí: lectura no repetible.) ¿Y con REPEATABLE READ? (No: las dos lecturas ven la misma foto.)

SI PREGUNTAN:
- «¿REPEATABLE READ evita la doble reserva?» → No. Cada transacción ve su foto, las dos ven la franja libre e insertan filas distintas. Solo SERIALIZABLE la detecta (abortando una) o una restricción UNIQUE la impide siempre.
- «¿Por qué en MySQL REPEATABLE READ tampoco muestra fantasmas?» → Porque su motor InnoDB usa una foto para las lecturas y candados de rango (gap locks) para las lecturas con bloqueo. Es una desviación del estándar, como la de PostgreSQL.

CUIDADO: Rojo en la tabla significa «la anomalía puede ocurrir», no «el nivel está mal». Dilo al entrar: la X confunde.

PASA A LA SIGUIENTE: Así se consulta y se cambia el nivel en PostgreSQL.

### [Slide 9] Niveles de aislamiento: que anomalia tapa cada uno

QUÉ ES (dilo así): Cómo se consulta y cómo se cambia el nivel de aislamiento en PostgreSQL. El nivel se elige por transacción, al abrirla.

CÓMO DARLA (≈3 min):
- Línea 1: SHOW transaction_isolation responde read committed: el nivel por omisión.
- Líneas 3-5: BEGIN ISOLATION LEVEL REPEATABLE READ abre una transacción que trabaja sobre una foto fija: la misma consulta devuelve lo mismo hasta el COMMIT.
- Líneas 7-10: SERIALIZABLE: si dos transacciones no se pueden ordenar, PostgreSQL aborta una con «could not serialize access due to read/write dependencies among transactions» (SQLSTATE 40001).
- Líneas 12-13: READ UNCOMMITTED existe en la sintaxis pero se comporta como READ COMMITTED. Y SERIALIZABLE no evita el error: obliga a reintentar.

EJEMPLO: La otra forma de pedirlo: BEGIN; SET TRANSACTION ISOLATION LEVEL SERIALIZABLE; como primera sentencia de la transacción.

SI PREGUNTAN:
- «Si pido READ UNCOMMITTED, ¿SHOW dice read committed?» → No: SHOW transaction_isolation dice read uncommitted, porque informa lo que se pidió; lo que cambia es el comportamiento, que es el de READ COMMITTED.
- «¿El nivel queda para toda la sesión?» → Con BEGIN ISOLATION LEVEL vale solo para esa transacción. Para la sesión: SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL …

CUIDADO: En una sola sesión no se ve ningún aborto de serialización: hacen falta dos transacciones concurrentes. El código corre sin error y es todo lo que se puede mostrar aquí.

PASA A LA SIGUIENTE: Otra forma de evitar el choque: no dejar que la segunda lea. El bloqueo pesimista.

### [Slide 10] Control pesimista: SELECT... FOR UPDATE

QUÉ ES (dilo así): El control pesimista parte de que el conflicto va a ocurrir, así que bloquea el recurso antes de usarlo. SELECT … FOR UPDATE lee la fila y la deja tomada hasta el COMMIT o el ROLLBACK: otra transacción que la pida con FOR UPDATE, o que intente modificarla, espera. Cuando la primera termina, la segunda entra y ve el valor ya actualizado.

CÓMO DARLA (≈4 min):
- Al entrar: T1 ejecuta SELECT stock FROM insumo WHERE id_insumo = 2 FOR UPDATE: lee stock 3 y la fila queda con bloqueo exclusivo (en rojo). T2 pide la misma fila con FOR UPDATE y queda esperando (el reloj).
- Clic 1: T1 descuenta 3 (UPDATE insumo SET stock = stock - 3) y confirma. El stock queda en 0 y el COMMIT libera la fila.
- Clic 2: T2 por fin entra y lee stock 0, no 3. Su validación «¿alcanza para 3?» dice que no y rechaza la venta. Sin el bloqueo, T2 habría decidido con el 3 que leyó antes y vendido unidades que ya no existen.
- Clic 3: El costo es la espera. Regla de diseño: entre el FOR UPDATE y el COMMIT no va ninguna llamada externa ni una pantalla esperando al usuario. Si no se quiere esperar: NOWAIT falla de inmediato y SKIP LOCKED salta la fila tomada.

EJEMPLO: Dos auxiliares facturan la última Vacuna triple felina (stock 3) y las dos piden 3. Con FOR UPDATE solo una la vende; la otra recibe «no alcanza» en vez de vender unidades que no hay.

SI PREGUNTAN:
- «¿Un SELECT normal también espera?» → No. En PostgreSQL un SELECT sin FOR UPDATE nunca espera: lee la última versión confirmada (aquí, 3). Solo esperan quienes piden la fila con FOR UPDATE o intentan modificarla.
- «¿Y si T1 nunca confirma?» → T2 espera indefinidamente, salvo que use NOWAIT, SKIP LOCKED o SET lock_timeout = '5s', que hace fallar la espera a los cinco segundos.

CUIDADO: FOR UPDATE WAIT 5 es sintaxis de Oracle: en PostgreSQL da error de sintaxis. El equivalente es SET lock_timeout.

PASA A LA SIGUIENTE: En código: el bloqueo explícito y una alternativa que no bloquea nada.

### [Slide 11] El bloqueo explicito y la actualizacion condicional

QUÉ ES (dilo así): Dos maneras de que el doble descuento no ocurra. La A bloquea la fila y obliga a esperar; la B no bloquea nada: mete la condición dentro del UPDATE para que comprobar y escribir sean una sola sentencia.

CÓMO DARLA (≈3 min):
- Líneas 1-5: Opción A: BEGIN, SELECT … FOR UPDATE (devuelve 3 y toma la fila), UPDATE que resta 3 y COMMIT, que la libera. Es la que hace falta cuando hay que leer, calcular con datos de varias tablas y después escribir.
- Líneas 7-9: Opción B: UPDATE … WHERE id_insumo = 2 AND stock >= 3. Si alcanza, resta y responde UPDATE 1; si no, no toca nada y responde UPDATE 0. Comprobar y escribir son atómicos.
- Líneas 10-11: Ejecutadas en orden, la B responde UPDATE 0 porque la A ya dejó el stock en 0: ese 0 es la señal de que otro llegó primero. En PL/pgSQL se lee con GET DIAGNOSTICS v_filas = ROW_COUNT.

EJEMPLO: Después de las dos: SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo = 2; → 2 | Vacuna triple felina | 0.

SI PREGUNTAN:
- «¿Cuál es mejor?» → Para un descuento de stock, la B: una sola sentencia y sin esperas largas. La A cuando la decisión necesita leer y calcular antes de escribir.
- «¿El UPDATE de la B no bloquea también?» → Sí, pero solo lo que dura la sentencia: la segunda transacción que quiera la fila espera ese instante y vuelve a evaluar la condición con el valor nuevo.

CUIDADO: En una sola sesión FOR UPDATE nunca espera, porque nadie más tiene la fila: que corra sin error no demuestra el bloqueo. La espera se explica con la línea de tiempo.

PASA A LA SIGUIENTE: El enfoque opuesto: no bloquear nada y verificar al escribir.

### [Slide 12] Control optimista: verificar unicamente al escribir

QUÉ ES (dilo así): El control optimista hace la apuesta contraria: deja que todos lean sin bloquear y solo comprueba, al escribir, que nadie cambió el dato mientras tanto. Para eso la tabla lleva una columna version (un entero, o una fecha de última modificación) que sube en cada cambio.

CÓMO DARLA (≈4 min):
- Al entrar: Se lee la cita 812 con version 7, sin bloquear nada; el usuario cambia la hora en pantalla. Al guardar: UPDATE cita SET fecha_hora = …, version = version + 1 WHERE id_cita = 812 AND version = 7.
- Clic 1: Sin conflicto: nadie tocó la cita, la versión guardada sigue en 7, el UPDATE encuentra la fila (UPDATE 1) y la deja en version 8.
- Clic 2: Con conflicto: otra transacción guardó primero y la dejó en 8. El WHERE version = 7 ya no encuentra nada: UPDATE 0. Cero filas afectadas es la señal; no hay error.
- Clic 3: La aplicación lee ese 0 y decide: reintenta o avisa «la cita cambió mientras la editabas». Criterio: si la misma fila se disputa muchas veces al día (el stock del insumo más vendido), pesimista; si el choque es raro (el teléfono de un dueño), optimista, porque nadie espera.

EJEMPLO: La columna no existe en el esquema del curso; se agregaría con ALTER TABLE cita ADD COLUMN version INT NOT NULL DEFAULT 1;

SI PREGUNTAN:
- «¿Por qué no comparar todas las columnas en vez de una versión?» → Se puede, pero es largo y frágil. Un entero que sube en cada UPDATE resume «alguien cambió esta fila» en una sola comparación.
- «¿Quién sube la versión?» → El mismo UPDATE que guarda: version = version + 1. Si alguna ruta del código actualiza sin subirla, el mecanismo deja de detectar conflictos.

CUIDADO: El optimista no da error cuando hay conflicto: da 0 filas. Si la aplicación no revisa cuántas filas afectó, el cambio del usuario se pierde en silencio.

PASA A LA SIGUIENTE: Cuando dos transacciones se bloquean entre sí aparece el último problema: el deadlock.

### [Slide 13] Deadlock: la escena de la clínica y como se evita

QUÉ ES (dilo así): Un deadlock, o interbloqueo, es un ciclo de esperas: cada transacción tiene algo que la otra necesita y espera lo que la otra tiene. Ninguna espera termina sola, así que el motor rompe el ciclo abortando una.

CÓMO DARLA (≈4 min):
- Al entrar: Facturación toma la fila de factura y luego pide la de insumo; devolución toma la de insumo y luego pide la de factura. Flechas sólidas: lo que tiene; punteadas: lo que espera. Es un ciclo: ninguna avanza.
- Clic 1: PostgreSQL revisa su grafo de esperas (después de un segundo de espera, por omisión), encuentra el ciclo y aborta una con «deadlock detected», código 40P01. Facturación obtiene la fila y termina. La abortada se deshace completa y debe reintentarse.
- Clic 2: Prevención: un orden fijo. Si todos los procedimientos tocan factura antes que insumo, el ciclo no puede formarse. Se escribe una vez en el documento de diseño y no cuesta rendimiento.

EJEMPLO: En Oracle el mismo error es ORA-00060 y en MySQL el 1213: cambia el número, no el mecanismo.

SI PREGUNTAN:
- «¿Cuál transacción elige como víctima?» → La documentación de PostgreSQL dice que es difícil de predecir y que no hay que depender de eso. Por eso cualquier transacción que participe debe estar lista para reintentar.
- «¿El deadlock deja datos a medias?» → No: la víctima se deshace completa, como cualquier transacción abortada.

CUIDADO: No presentes el deadlock como una catástrofe que se evita a toda costa: lo correcto es prevenirlo con un orden fijo y, si igual ocurre, capturar el error y reintentar.

PASA A LA SIGUIENTE: Antes de todos estos mecanismos hay una solución de una sola línea para el caso estrella.

### [Slide 14] Antes de los niveles: la restriccion que cuesta una linea

QUÉ ES (dilo así): Antes de pensar en niveles o bloqueos, la doble reserva tiene una solución declarativa: decirle al motor que no pueden existir dos citas vigentes del mismo veterinario a la misma hora. Una regla escrita así se cumple siempre, venga la escritura de la aplicación, de un script de carga o de alguien corrigiendo a mano.

CÓMO DARLA (≈4 min):
- Al entrar: La regla: CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA'. Una sentencia, y el motor la revisa en cada INSERT y UPDATE.
- Clic 1: Las dos recepciones insertan la misma franja (veterinario 1, 2026-09-01 08:00). La primera entra; la segunda choca: «duplicate key value violates unique constraint "uq_cita_vet_franja"», SQLSTATE 23505. Da igual el orden o la velocidad: alguna llega segunda.
- Clic 2: El procedimiento captura esa excepción (EXCEPTION WHEN unique_violation) y responde «Ese horario acaba de ser tomado, elija otro». Nadie tuvo que razonar sobre aislamiento.
- Clic 3: Por qué es parcial: una cita CANCELADA no ocupa la franja, así que esa sí entra aunque haya una vigente a la misma hora. Un UNIQUE de tabla no admite WHERE: también contaría las canceladas y una franja cancelada no se podría volver a agendar.

EJEMPLO: Con dos sesiones simultáneas, la segunda espera un instante a que la primera confirme y solo entonces recibe la violación de unicidad: la regla funciona también en concurrencia, que es lo que un trigger que cuenta citas no logra.

SI PREGUNTAN:
- «¿Un índice es una restricción?» → Un índice único hace el mismo trabajo que una restricción UNIQUE (el error incluso dice «unique constraint»), pero admite WHERE. Por eso se usa aquí.
- «¿Y si ya existe un ALTER TABLE … ADD CONSTRAINT uq_cita_vet_franja?» → El nombre es de un solo objeto: el CREATE UNIQUE INDEX responde «relation "uq_cita_vet_franja" already exists». Se borra la restricción (ALTER TABLE cita DROP CONSTRAINT uq_cita_vet_franja) y se crea el índice.

CUIDADO: Si la tabla ya tiene duplicados, el índice no se crea («could not create unique index … is duplicated»): primero se detectan y se limpian. Es lo que hace la lámina siguiente.

PASA A LA SIGUIENTE: Primero, el problema reproducido y detectado en código.

### [Slide 15] La doble reserva, reproducida y detectada

QUÉ ES (dilo así): En una sola sesión no se pueden ver dos transacciones cruzándose, pero sí lo esencial: sin restricción, la base acepta dos citas en la misma franja sin quejarse. Esta lámina reproduce el dato inválido, lo detecta y lo limpia.

CÓMO DARLA (≈3 min):
- Líneas 1-4: Un INSERT con dos filas: Mishi (4) y Bobby (5), veterinario 2, 2026-09-15 10:00. Responde INSERT 0 2: las dos entran y no hay ningún error.
- Líneas 6-11: La consulta de detección agrupa las citas vigentes por veterinario y hora y se queda con los grupos de más de una: devuelve 1 fila, veterinario 2, 2026-09-15 10:00, 2 citas. Es la que se corre antes de crear la restricción en una base que ya tiene datos.
- Líneas 13-14: Se borra la cita de mayor id_cita, la duplicada. Si no se borra, el CREATE UNIQUE INDEX de la lámina siguiente falla con «could not create unique index "uq_cita_vet_franja"» porque la clave está repetida.

EJEMPLO: Con los datos sembrados, antes de estos INSERT la consulta de detección devuelve 0 filas: no hay ninguna franja duplicada.

SI PREGUNTAN:
- «¿Por qué el WHERE estado <> 'CANCELADA'?» → Porque una cita cancelada no ocupa la franja: una cancelada y una vigente a la misma hora no son doble reserva.
- «¿Borrar la de mayor id no es arbitrario?» → Sí. En una base real se decide con el negocio a quién se le reprograma; aquí sobra la segunda que entró.

CUIDADO: SELECT MAX(id_cita) borra la última cita de toda la tabla: sirve justo después de este INSERT, no como limpieza general.

PASA A LA SIGUIENTE: Con la tabla limpia, el índice que lo hace imposible.

### [Slide 16] El indice unico parcial que hace imposible la doble reserva

QUÉ ES (dilo así): La regla que la clínica necesita y la prueba de que funciona: dos citas vigentes del mismo veterinario a la misma hora ya no pueden existir, y una cancelada no estorba.

CÓMO DARLA (≈3 min):
- Líneas 1-4: CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA'. Con los datos limpios por la lámina anterior se crea sin error.
- Líneas 6-8: Una cita CANCELADA en la franja que ya tiene la cita 1 (Firulais, veterinario 1, 2026-09-01 08:00) entra: INSERT 0 1. El índice no mira las canceladas.
- Líneas 10-14: La misma franja, ahora vigente (PROGRAMADA): ERROR: duplicate key value violates unique constraint "uq_cita_vet_franja", con el detalle Key (id_veterinario, fecha_hora)=(1, 2026-09-01 08:00:00) already exists. SQLSTATE 23505.
- Leyenda: BEGIN y COMMIT no bastaban porque las dos leían «libre»; el índice se verifica al escribir, el único momento que no depende de quién leyó primero.

EJEMPLO: Para dar el mensaje de negocio: DO $$ BEGIN INSERT … ; EXCEPTION WHEN unique_violation THEN RAISE NOTICE 'Ese horario acaba de ser tomado, elija otro'; END $$; responde con ese NOTICE y la cita no entra.

SI PREGUNTAN:
- «¿El error deshace algo más?» → Deshace la sentencia que falló, y la transacción en curso queda abortada hasta su ROLLBACK si no se captura el error.
- «¿Por qué el error dice «unique constraint» si es un índice?» → Porque PostgreSQL informa igual cualquier violación de unicidad, venga de una restricción UNIQUE o de un índice único.

CUIDADO: El nombre uq_cita_vet_franja es exacto y se usa una sola vez: si antes se creó una restricción con ese nombre, este CREATE falla con «relation "uq_cita_vet_franja" already exists».

PASA A LA SIGUIENTE: Ahora todo esto ejecutado en la demo.

### [Slide 17] Demo del dia

QUÉ ES (dilo así): La demo ejecuta lo que se proyectó: el dato inválido aceptado, la restricción que lo rechaza y el bloqueo que, en una sola sesión, corre pero no se ve esperar.

CÓMO DARLA (≈15 min):
- 1 · Problema: Ejecuta la lámina «La doble reserva, reproducida y detectada»: el INSERT de dos filas (INSERT 0 2), la detección (1 fila: veterinario 2, 2026-09-15 10:00, 2 citas) y el DELETE del duplicado.
- 2 · Solución: Ejecuta la lámina del índice único parcial: el CREATE UNIQUE INDEX, la cancelada que sí entra y el INSERT vigente del veterinario 1 a las 08:00 del 2026-09-01, que sale con duplicate key value violates unique constraint. Muestra el SELECT de cita para que se vea que no entró.
- 3 · Bloqueo: Ejecuta las opciones A y B: A devuelve stock 3 y descuenta; B responde UPDATE 0. Cierra con SELECT stock FROM insumo WHERE id_insumo = 2; → 0.
- 4 · Lo que no se ve: Dibuja en una tabla paso / T1 / T2 / estado de la fila la espera de T2 durante el FOR UPDATE: en una sola sesión nadie más tiene la fila, así que nunca hay espera visible.

EJEMPLO: Tiempos sugeridos: problema 4 min, solución 4 min, bloqueo 4 min, línea de tiempo 3 min.

SI PREGUNTAN:
- «¿Puedo abrir dos pestañas para simular dos recepcionistas?» → No: cada pestaña levanta su propia base en memoria y no comparten nada. Para ver la espera real hacen falta dos sesiones de psql contra un servidor, y las vistas pg_locks y pg_stat_activity.

CUIDADO: Sin el DELETE del duplicado el índice no se crea («could not create unique index … is duplicated») y el INSERT siguiente entra como una cita más: borra el duplicado antes de crear el índice. El script del Kit (Codigo/10_concurrencia_clinica.sql) hace la misma secuencia sobre una tabla propia y termina en el INSERT que falla a propósito.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Narrativa paso a paso T1/T2 sobre tabla Cita.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 10 - Control de concurrencia/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 10 · Control de concurrencia · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. La transaccion como unidad de todo o nada
5. Serializar de verdad existe, y cuesta
6. Los tres fenomenos indeseables, en escenas de la clinica
7. Doble reserva sin control de concurrencia
8. Los cuatro niveles de aislamiento se definen por lo que permiten
9. Niveles de aislamiento: que anomalia tapa cada uno
10. Control pesimista: SELECT... FOR UPDATE
11. El bloqueo explicito y la actualizacion condicional
12. Control optimista: verificar unicamente al escribir
13. Deadlock: la escena de la clínica y como se evita
14. Antes de los niveles: la restriccion que cuesta una linea
15. La doble reserva, reproducida y detectada
16. El indice unico parcial que hace imposible la doble reserva
17. Demo del dia
18. Cierre · Clase 10

> Privado, no se proyecta: `Kit docente/Clase 10/Solucion Taller Clase 10 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Escenarios de concurrencia del PI documentados. No es un taller suelto.»
Referencia slides: Encuadre + Mapa del bloque.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: ExamLab (PostgreSQL/PGlite) + Google Docs.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Evidencia del problema: dos citas en la misma franja (sin restriccion) [[captura: salida-doble-reserva.png]]
📸 El MISMO INSERT ya con UNIQUE: la BD lo rechaza sola [[captura: salida-unique-rechaza.png]]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar el checklist PI del proyecto.


## Codigo / scripts
Carpeta Codigo/ — archivo 10_concurrencia_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 10/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
