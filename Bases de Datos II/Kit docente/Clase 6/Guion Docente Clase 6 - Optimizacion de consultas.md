# Guion docente · Clase 6 · Optimizacion de consultas · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Primera pareja de consultas antes/despues del PI
- **Entregable de hoy:** 2 consultas (antes/despues) + justificacion (media pag.)
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 6 - Optimizacion de consultas/Presentacion.pptx
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

QUÉ ES (dilo así): Hasta ahora la pregunta era si una consulta funciona. Hoy es otra: cuánto trabajo le cuesta al motor responderla, cómo se lee ese trabajo en el plan de ejecución y cómo se demuestra que una versión más rápida devuelve exactamente lo mismo.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema y pregunta: «si dos consultas devuelven lo mismo, ¿cómo sabemos cuál es mejor?». Deja que respondan una o dos personas; casi siempre dirán «la que tarde menos».
- Después: Cierra: «al final de hoy lo van a decir con evidencia: el plan de ejecución, cuántas filas pasa cada paso y cuántas veces se repite».

PASA A LA SIGUIENTE: Empezamos por quién decide cómo se ejecuta una consulta: el optimizador.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido de las dos horas: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] SQL es declarativo: quien decide el como es el optimizador

QUÉ ES (dilo así): Cuando escribimos una consulta solo describimos el resultado. El motor la pasa por tres etapas: el analizador revisa que esté bien escrita y que existan las tablas y columnas; el optimizador arma varios planes, les calcula un costo y elige el más barato; el ejecutor corre ese plan. Optimizar es ayudar al optimizador a encontrar el plan bueno.

CÓMO DARLA (≈4 min):
- Al entrar: Arriba, la consulta dice QUÉ; debajo, el analizador. Di: «antes de pensar en velocidad, el motor comprueba que la consulta tenga sentido: sintaxis, tablas y columnas». Si falla aquí, el error sale antes de leer un dato.
- Clic 1: El optimizador y tres planes candidatos con su costo: 1.240, 85 y 9.600, en unidades del motor, no en milisegundos. Elige el B, el más barato. Pregunta: «¿los tres devuelven lo mismo?».
- Clic 2: El ejecutor corre solo el plan elegido. Lee la conclusión: los tres planes devuelven exactamente las mismas filas; lo único que cambia es el trabajo.

EJEMPLO: La agenda del día cruza cita, mascota, dueno y veterinario: con 4 tablas hay 24 órdenes posibles de unión (4 × 3 × 2 × 1), y multiplicados por las formas de leer y de cruzar pasan del millar de planes. El optimizador no los prueba todos: poda y decide en milisegundos.

SI PREGUNTAN:
- «¿Puedo obligar al motor a usar un plan?» → PostgreSQL no trae «hints» como Oracle. Se le ayuda escribiendo la consulta para que pueda usar lo que existe: filtros sobre columnas desnudas, estadísticas al día e índices adecuados.
- «¿El costo está en milisegundos?» → No. Es una unidad relativa del motor (1 = leer una página de forma secuencial); sirve para comparar planes, no para medir tiempo.

CUIDADO: No digas que el optimizador «prueba todos los planes»: estima con estadísticas, poda y elige; por eso a veces se equivoca.

PASA A LA SIGUIENTE: Para saber qué plan eligió hay que aprender a leerlo: es un árbol.

### [Slide 5] Leer un plan: es un arbol y se lee de adentro hacia afuera

QUÉ ES (dilo así): EXPLAIN delante de una consulta no la ejecuta: muestra el plan que el optimizador eligió. Se imprime como una lista con sangrías, pero es un árbol: cada línea con más sangría es hija de la de arriba. Primero corren las hojas, que leen las tablas, y la primera línea es la última operación, la que entrega el resultado.

CÓMO DARLA (≈4 min):
- Al entrar: Lee en voz alta lo que imprime EXPLAIN para la consulta del día (cita con mascota, citas del 2026-03-10): Hash Join arriba; debajo y más adentro, el Seq Scan sobre cita con su filtro y el Hash armado sobre el Seq Scan de mascota. Pregunta: «¿qué ocurre primero?». La mayoría dirá «el Hash Join».
- Clic 1: Las mismas líneas dibujadas como árbol: el Hash Join es la raíz y los dos Seq Scan son las hojas. La sangría decide quién es hijo de quién.
- Clic 2: Los números marcan el orden real: 1) se lee cita, 2) se lee mascota, 3) con mascota se arma la tabla hash, 4) el Hash Join cruza. Lee la regla: la primera línea es la ÚLTIMA operación.

EJEMPLO: En la base de la clase ese plan dice Hash Join (cost=149.68..851.22 rows=150): 150 filas estimadas, que son las 150 citas del 2026-03-10.

SI PREGUNTAN:
- «¿EXPLAIN ejecuta la consulta?» → No: solo muestra el plan con estimaciones. EXPLAIN ANALYZE sí la ejecuta y agrega tiempos y filas reales; por eso sobre un UPDATE o un DELETE se envuelve en BEGIN … ROLLBACK.
- «¿Qué es el Hash?» → Una tabla en memoria armada con las filas de mascota, organizada por id_mascota, para encontrar rápido la mascota de cada cita al cruzar.

CUIDADO: El error más común, también del docente, es leer el plan de arriba hacia abajo como una lista de pasos. Si se enseña así, el grupo interpretará al revés todos los planes del curso.

PASA A LA SIGUIENTE: Con ANALYZE el plan deja de ser una predicción y se vuelve evidencia.

### [Slide 6] EXPLAIN ANALYZE: la evidencia, no la opinion

QUÉ ES (dilo así): EXPLAIN (ANALYZE, BUFFERS) ejecuta la consulta de verdad y muestra, nodo por nodo, lo que pasó: filas reales, tiempo y páginas leídas. Es la evidencia de una optimización; sin ella, «es más rápida» es una opinión.

CÓMO DARLA (≈3 min):
- Al entrar: Líneas 1-5: la consulta del día (cita con mascota, rango del 2026-03-10) precedida de EXPLAIN (ANALYZE, BUFFERS). Si puedes, ejecútala en vivo.
- Líneas 7-9: El nodo: hoy sale Seq Scan on cita c, porque la base no tiene índices fuera de las claves primarias. Las filas: el motor estimó 150 y salieron 150 (actual rows=150).
- Líneas 10-12: Rows Removed by Filter: 29860 es lo que leyó para nada; Buffers: shared hit=251 son las 251 páginas de 8 KB de cita. El Execution Time cambia entre corridas: lo estable son filas y páginas.

EJEMPLO: Una corrida en el navegador: Seq Scan on cita c … rows=150 … Rows Removed by Filter: 29860 · Buffers: shared hit=251 · Execution Time ≈ 35 ms. Las dos primeras cifras salen idénticas en cualquier equipo; el tiempo no.

SI PREGUNTAN:
- «¿Qué significa «shared hit»?» → Que la página ya estaba en memoria; «read» significaría que hubo que traerla del disco. En el navegador todo vive en memoria, así que casi siempre verás hit.
- «¿Puedo usar EXPLAIN ANALYZE con un DELETE?» → Sí, pero lo ejecuta de verdad: envuélvelo en BEGIN y ROLLBACK para no borrar nada.

CUIDADO: Si BUFFERS no responde en algún equipo, EXPLAIN ANALYZE a secas sirve igual. Lo que no sirve es comparar milisegundos entre máquinas distintas.

PASA A LA SIGUIENTE: Ahora cada campo de una línea del plan, uno por uno.

### [Slide 7] Un plan, campo por campo

QUÉ ES (dilo así): Cada línea del plan trae dos grupos de números. En el primer paréntesis, lo que el motor estimó antes de ejecutar: costo, filas y ancho de la fila. En el segundo, lo que pasó: tiempo real, filas reales y cuántas veces se repitió ese nodo (loops). Leer un plan es comparar los dos grupos.

CÓMO DARLA (≈3 min):
- Al entrar: Arriba, una línea real del plan de hoy: Seq Scan on cita c (cost=0.00..701.15 rows=150 width=16) y su parte real (actual time … rows=150 loops=1).
- Columna izquierda: Lo estimado: cost es arranque..total en la unidad del motor (1 = leer una página), no milisegundos; rows, las filas que cree que saldrán; width, los bytes promedio por fila.
- Columna derecha: Lo real: actual time en milisegundos POR VUELTA; rows, las filas que salieron; loops, cuántas veces se ejecutó el nodo.
- Abajo: La regla del nodo más costoso: tiempo por loops, sabiendo que el tiempo de un nodo ya incluye el de sus hijos. Un nodo de 0,5 ms con loops=2006 cuesta un segundo aunque parezca el más barato.

EJEMPLO: La versión ANTES de la agenda (con to_char y UPPER sobre las columnas) estima rows=1 y entrega 91: con una función sobre la columna el motor no puede usar sus estadísticas y aplica una selectividad por omisión. Esa diferencia de 91 veces es la señal que hay que saber leer.

SI PREGUNTAN:
- «¿Una diferencia de 2 veces entre estimado y real es grave?» → No, es normal. La alarma es de 10 veces o más: estadísticas viejas o dos filtros que el motor cree independientes y no lo son.
- «¿Por qué la primera línea muestra el tiempo más alto?» → Porque el tiempo de cada nodo incluye el de sus hijos y la raíz los acumula todos. El culpable se busca por el tiempo propio de cada nodo multiplicado por loops.

CUIDADO: Confundir cost con milisegundos es el error más frecuente al leer planes: el costo solo sirve para comparar planes del mismo motor.

PASA A LA SIGUIENTE: ¿De dónde saca el motor sus estimaciones? De las estadísticas.

### [Slide 8] Las estadisticas: metadatos que describen los datos sin leerlos

QUÉ ES (dilo así): El optimizador no lee la tabla para decidir: consulta una ficha que la describe. Cuántas filas tiene, cuántas páginas ocupa, cuántos valores distintos hay en cada columna, qué fracción es nula y cómo se reparten los valores. Esa ficha son las estadísticas, y las actualiza el comando ANALYZE.

CÓMO DARLA (≈3 min):
- Al entrar: La tabla cita, ANALYZE y la ficha con las cifras reales de la base de hoy: 30.010 filas, 251 páginas de 8 KB, 3 valores distintos en estado, 1.810 en fecha_hora y ningún nulo.
- Clic 1: El reparto: estado está concentrado (61 % PROGRAMADA, 30 % ATENDIDA, 9 % CANCELADA) y fecha_hora es pareja (150 citas cada día). Con eso el motor calcula cuántas filas dejará pasar cada filtro.
- Clic 2: Lee la conclusión y remata: el plan no es propiedad del texto SQL; es una decisión tomada con las estadísticas de ese momento.

EJEMPLO: SELECT relpages, reltuples FROM pg_class WHERE relname = 'cita'; devuelve 251 y 30010. SELECT attname, n_distinct FROM pg_stats WHERE tablename = 'cita'; muestra 3 para estado y 1810 para fecha_hora.

SI PREGUNTAN:
- «¿Cada cuánto hay que correr ANALYZE?» → En un servidor, PostgreSQL lo hace solo en segundo plano (autovacuum) cuando la tabla cambia bastante. Después de una carga grande o de crear un índice conviene correrlo a mano.
- «¿Por qué la misma consulta cambia de plan de un día a otro?» → Porque la tabla creció, se recolectaron estadísticas nuevas, alguien creó un índice o el valor buscado es más o menos frecuente.

CUIDADO: No confundas «predicados correlacionados» (dos filtros que no son independientes y engañan la estimación) con la «subconsulta correlacionada» que viene después, que es un problema de cuántas veces se ejecuta algo.

PASA A LA SIGUIENTE: Con esas estadísticas el motor calcula dos números: cardinalidad y selectividad.

### [Slide 9] Cardinalidad y selectividad: por que el motor decide lo que decide

QUÉ ES (dilo así): Cardinalidad es cuántos valores distintos tiene una columna. Selectividad es qué fracción de las filas sobrevive a un filtro: 0 es ninguna, 1 es todas. Con ellas el motor estima cuántas filas saldrán de cada filtro, y de eso depende si conviene ir por un índice o leer la tabla completa.

CÓMO DARLA (≈4 min):
- Al entrar: Cardinalidad: cita.estado tiene 3 valores (baja); dueno.id_dueno tiene 2.006, uno por fila (alta).
- Clic 1: Selectividad con tres filtros reales de la base de hoy: estado = 'PROGRAMADA' deja 18.187 de 30.010 (0,61); la fecha del 2026-03-10 deja 150 (0,005); los dos juntos, 91 (0,003). Pregunta: «¿a cuál le serviría un índice?».
- Clic 2: La decisión: muchas filas, leer la tabla entera; pocas, ir por un índice. Como convención de oficio, por debajo del 5 % suele ganar el índice y por encima del 20 % la tabla entera; el motor no usa porcentajes, compara costos.

EJEMPLO: De 30.010 citas, 91 son el 0,3 %: un índice ayudaría mucho. 18.187 son el 61 %: un índice solo sobre estado no ayudaría.

SI PREGUNTAN:
- «¿Por qué no indexar estado si se filtra tanto por él?» → Porque deja pasar el 61 % de las filas: leer la tabla de corrido sale más barato que saltar a la tabla 18.187 veces desde un índice.
- «¿Cómo sabe el motor que la fecha deja 150?» → Por las estadísticas de fecha_hora: sus valores distintos y su reparto. Si estuvieran viejas, la estimación fallaría.

CUIDADO: «Cardinalidad» también se usa para las filas que entrega un nodo del plan: aclara en qué sentido la estás usando.

PASA A LA SIGUIENTE: Con esas cifras, los dos caminos para leer una tabla: completa o por índice.

### [Slide 10] Full table scan contra index scan, sin caricaturas

QUÉ ES (dilo así): Hay dos maneras básicas de leer una tabla. El recorrido completo (Seq Scan) lee todas las páginas una tras otra y descarta en memoria lo que no cumple. El acceso por índice baja por el árbol del índice y, por cada coincidencia, va a buscar la fila a la tabla: pocas lecturas, pero dispersas. Cuál conviene depende de cuántas filas salen.

CÓMO DARLA (≈3 min):
- Al entrar: Seq Scan: las páginas se leen de corrido. En la base de hoy, cita ocupa 251 páginas de 8 KB, y se leen todas aunque solo sirvan 150 filas.
- Clic 1: Index Scan: 2 o 3 lecturas para bajar el árbol y una lectura dispersa por cada fila encontrada. Para las 150 citas de un día, unas 153 lecturas.
- Clic 2: Lee la regla y di lo honesto: 251 contra 153 es del mismo orden. Con 300.000 citas el Seq Scan pasaría a unas 2.500 páginas y el índice seguiría en unas 153: ahí sí gana por mucho.

EJEMPLO: Hoy la base no tiene índice sobre fecha_hora: el plan de las citas del 2026-03-10 siempre dirá Seq Scan on cita. El cambio a un acceso por índice es el tema de la Clase 7.

SI PREGUNTAN:
- «Si el índice es mejor, ¿por qué el motor a veces lo ignora?» → Porque cuando salen muchas filas, saltar a la tabla por cada una cuesta más que leerla de corrido. El motor compara costos, no aplica una regla fija.
- «¿Qué es una lectura dispersa?» → Leer una página que no es la siguiente de la anterior. En disco cuesta más: un PostgreSQL de servidor la valora en 4 y la secuencial en 1.

CUIDADO: No prometas un Index Scan para hoy: en esta base no hay índices fuera de las claves primarias. Hoy se miden filas procesadas y pasadas sobre la tabla.

PASA A LA SIGUIENTE: Hay una forma de escribir el filtro que impide usar cualquier índice: la función sobre la columna.

### [Slide 11] Predicado sargable: el antipatron que conecta con la Clase 7

QUÉ ES (dilo así): Un índice guarda los valores de la columna tal como están. Si el filtro le aplica una función —to_char a la fecha, UPPER al estado— el motor no puede saber qué entradas cumplen sin calcular la función fila por fila: el filtro no es sargable. Se arregla dejando la columna sola y pasando el cálculo al otro lado.

CÓMO DARLA (≈4 min):
- Al entrar: Las dos formas no sargables de la consulta de agenda: to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10' y UPPER(c.estado) = 'PROGRAMADA'. El índice guarda fecha_hora, no to_char(fecha_hora).
- Clic 1: La reescritura: un rango sobre la columna desnuda (>= '2026-03-10 00:00:00' y < '2026-03-11 00:00:00') y la comparación directa del estado. UPPER se puede quitar porque el CHECK solo admite PROGRAMADA, ATENDIDA o CANCELADA, en mayúsculas.
- Clic 2: Lee la conclusión y aclara: hoy no hay índice sobre fecha_hora, así que el plan sigue en Seq Scan. Lo que se gana hoy es no calcular la función 30.010 veces y que el motor estime bien cuántas filas vienen.

EJEMPLO: Tampoco son sargables EXTRACT(YEAR FROM fecha_hora) = 2026 ni UPPER(m.nombre) = 'LUNA'. El primero se reescribe como rango del año; el segundo, si el negocio lo necesita, con un índice sobre la expresión, que es de la Clase 7.

SI PREGUNTAN:
- «¿Entonces nunca puedo usar funciones en el WHERE?» → Sí puedes, sobre el valor constante, no sobre la columna. Y si la función sobre la columna es necesaria, existe el índice sobre la expresión: CREATE INDEX … ON mascota (UPPER(nombre)).
- «¿Por qué el rango termina en < '2026-03-11' y no en <= '2026-03-10 23:59:59'?» → Porque el rango semiabierto no deja huecos: una cita a las 23:59:59.5 quedaría fuera del segundo.

CUIDADO: No afirmes que la versión sargable ya usa un índice: sin índice sobre fecha_hora, hoy las dos versiones hacen Seq Scan.

PASA A LA SIGUIENTE: Veámoslo en código: las dos versiones devuelven exactamente lo mismo.

### [Slide 12] El antipatron y su reescritura

QUÉ ES (dilo así): Las dos consultas buscan las citas del 2026-03-10. La primera aplica una función a la columna; la segunda compara la columna desnuda con un rango. Devuelven las mismas 150 citas, pero solo la segunda deja abierta la puerta a un índice.

CÓMO DARLA (≈3 min):
- Al entrar: Líneas 1-3: la versión ANTES. Subraya TO_CHAR(fecha_hora, …): el motor lo calcula en las 30.010 filas antes de comparar.
- Líneas 5-8: La versión DESPUÉS: mismo SELECT y el filtro como rango semiabierto, >= el día y < el día siguiente.
- Líneas 10-11: Lee el comentario: mismas 150 citas. Si preguntan por la velocidad, hoy las dos hacen Seq Scan; en una corrida en el navegador la primera tardó unos 130 ms y la segunda unos 40 ms, solo por no calcular la función.

EJEMPLO: SELECT COUNT(*) de cada versión devuelve 150 en las dos, y un EXCEPT entre ellas devuelve 0 filas.

CUIDADO: Los milisegundos cambian entre corridas y entre equipos. Lo que se afirma con seguridad es el conteo de filas y que el Filter de la segunda ya no contiene to_char.

PASA A LA SIGUIENTE: Juntemos todos los cambios de la consulta de agenda en una sola comparación ANTES/DESPUÉS.

### [Slide 13] Optimizar es un ANTES medible, no una opinion

QUÉ ES (dilo así): La consulta de agenda del día tiene cuatro defectos, y cada uno su arreglo. No es una cuestión de gusto: las dos versiones devuelven las mismas 91 filas y lo que cambia se mide en el plan, en filas procesadas y pasadas sobre la tabla.

CÓMO DARLA (≈3 min):
- Al entrar: Columna ANTES, de arriba abajo: SELECT * arrastra todas las columnas de 4 tablas; to_char y UPPER esconden las columnas; las comas permiten un producto cartesiano si falta una condición; la subconsulta por fila se repite 2.006 veces.
- Columna DESPUÉS: Los arreglos en el mismo orden: solo las 6 columnas que usa la pantalla, rango y comparación directa, JOIN … ON y LEFT JOIN con GROUP BY.
- Abajo: El subtítulo: mismas 91 filas, y sin índices no hay Index Scan. Subraya que JOIN … ON no acelera: da el mismo plan que las comas; lo que gana es que un ON olvidado sea un error de sintaxis y no un cartesiano.

EJEMPLO: Plan del ANTES de la agenda: Seq Scan on cita c con rows=1 estimada y 91 reales. Plan del DESPUÉS: el mismo Seq Scan, con rows=91 estimada y 91 reales. Mismo recorrido, pero ahora el motor sabe cuántas filas vienen.

SI PREGUNTAN:
- «¿Cambiar las comas por JOIN … ON no hace la consulta más rápida?» → No. PostgreSQL convierte las dos formas al mismo plan interno; se gana legibilidad y seguridad, no milisegundos.

CUIDADO: Si presentas JOIN … ON como mejora de rendimiento, enseñas algo falso: es una mejora de seguridad y de legibilidad.

PASA A LA SIGUIENTE: El cambio que sí es de órdenes de magnitud: la subconsulta correlacionada.

### [Slide 14] La subconsulta correlacionada: 2.006 pasadas o una sola

QUÉ ES (dilo así): Una subconsulta correlacionada usa un valor de la fila de afuera (aquí, d.id_dueno). Como su resultado cambia con cada fila, el motor no puede calcularla una vez y reutilizarla: la ejecuta una vez por cada fila de la consulta exterior. Con 2.006 dueños son 2.006 ejecuciones. La misma pregunta se responde en una sola pasada uniendo y agrupando.

CÓMO DARLA (≈4 min):
- Al entrar: ANTES: por cada uno de los 2.006 dueños, la subconsulta cuenta sus mascotas recorriendo las 5.008 de la tabla. Son 2.006 ejecuciones y unos 10 millones de filas leídas para producir 2.006 números.
- Clic 1: DESPUÉS: dueno LEFT JOIN mascota y GROUP BY por dueño. Cada tabla se lee una sola vez y se agrupa: una pasada.
- Clic 2: Las dos devuelven las mismas 2.006 filas. Es la única mejora del día de órdenes de magnitud, y no necesita ningún índice: se eliminaron 2.005 recorridos.

EJEMPLO: En una corrida en el navegador, la versión ANTES tardó unos 4,9 s y la reescrita unos 0,19 s: más de 25 veces menos. Los segundos cambian por máquina; el loops=2006 no.

SI PREGUNTAN:
- «¿Toda subconsulta es lenta?» → No. Una subconsulta que no depende de la fila de afuera se calcula una sola vez. El problema es la correlacionada en la lista de columnas, que se repite por fila.
- «¿Por qué LEFT JOIN y no JOIN?» → Porque con JOIN desaparecen los 6 dueños que no tienen mascotas: el reporte pasa de 2.006 a 2.000 filas.

CUIDADO: No uses «correlacionada» a secas para dos cosas distintas: los predicados correlacionados (un problema de estimación) no tienen nada que ver con esto.

PASA A LA SIGUIENTE: Así se ve en código, con los dos detalles que deciden si el resultado es el mismo.

### [Slide 15] Matar la subconsulta correlacionada

QUÉ ES (dilo así): La reescritura completa: la versión que repite la subconsulta por dueño y la que une y agrupa una sola vez. Dos detalles deciden que el resultado sea idéntico: LEFT JOIN y COUNT de una columna.

CÓMO DARLA (≈3 min):
- Al entrar: Líneas 1-5: ANTES. La subconsulta está en la lista de columnas y menciona d.id_dueno, de afuera: se ejecuta una vez por dueño (loops=2006 en el plan).
- Líneas 7-12: DESPUÉS: LEFT JOIN mascota, GROUP BY d.id_dueno, d.nombre y COUNT(m.id_mascota). Se agrupa por id_dueno para no sumar como uno a dos dueños que se llamen igual.
- Líneas 14-15: Los dos detalles. LEFT y no JOIN: con JOIN se pierden los 6 dueños sin mascotas. COUNT(m.id_mascota) y no COUNT(*): el LEFT JOIN deja una fila con NULL para esos dueños; COUNT(*) la cuenta como 1 y COUNT de la columna da 0.

EJEMPLO: Los dueños 2001 a 2006 de la base de hoy no tienen mascotas: con COUNT(m.id_mascota) dan 0 y con COUNT(*) dan 1. El primero del ranking es Marcela Diaz, con 5 mascotas.

SI PREGUNTAN:
- «¿Por qué agrupar por d.id_dueno y no solo por d.nombre?» → Porque dos dueños pueden llamarse igual: agrupar solo por nombre los sumaría como si fueran uno.

CUIDADO: Aceptar COUNT(*) «porque el total sale igual» es el error típico al revisar: solo cambia en los dueños sin mascotas, que quedan al final del ranking.

PASA A LA SIGUIENTE: ¿Cómo se ve ese 2.006 en el plan? En un campo: loops.

### [Slide 16] La subconsulta correlacionada en el plan: loops

QUÉ ES (dilo así): loops es el único campo del plan que dice «esto se repitió». Un nodo puede mostrar un tiempo pequeño y ser el más caro, porque ese tiempo es por vuelta. La lámina muestra el plan real de la versión ANTES y el de la reescritura.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba, el ANTES: Seq Scan on dueno d y, colgado de él, SubPlan 1 con un Aggregate de 2,3 ms y loops=2006 (resaltado). Debajo, el Seq Scan on mascota con Rows Removed by Filter: 5006 en cada vuelta.
- La cuenta: 2,3 ms por 2.006 vueltas ≈ 4,6 s: el nodo que parece barato es el culpable. Quien solo mira el número más grande señala el nodo equivocado.
- Abajo: El DESPUÉS: HashAggregate sobre un Hash Right Join; mascota y dueno se leen una vez (loops=1). Cierra con los dos recuadros: LEFT JOIN y COUNT(m.id_mascota).

EJEMPLO: Plan real en el navegador: Aggregate (actual time=2.298..2.300 rows=1 loops=2006) y Execution Time: 4909 ms; la reescritura, Execution Time: 188 ms.

SI PREGUNTAN:
- «¿Dónde aparece loops?» → Al final del paréntesis de tiempos reales de cada nodo: (actual time=… rows=… loops=…). Solo sale con EXPLAIN ANALYZE.

CUIDADO: La versión de la demo cuenta citas, no mascotas: cada vuelta recorre las 30.010 citas y la consulta completa tarda minutos en el navegador. Avisa antes, o acótala con WHERE d.id_dueno <= 200 (loops=200).

PASA A LA SIGUIENTE: Más rápido no sirve de nada si el resultado cambió: hay que probar que es el mismo.

### [Slide 17] Optimizar no cambia el resultado, y eso se demuestra

QUÉ ES (dilo así): Optimizar es obtener la MISMA respuesta con menos trabajo. Si la versión nueva devuelve filas distintas, se rompió la consulta, y se rompió sin aviso: ningún motor lanza un error porque una consulta devuelva otra cosa. Por eso toda optimización va acompañada de una prueba de equivalencia.

CÓMO DARLA (≈3 min):
- Al entrar: La prueba más simple: SELECT COUNT(*) de cada versión, en la misma corrida. En la agenda del 2026-03-10 las dos dicen 91: es una optimización.
- Clic 1: El caso equivocado: la versión nueva devuelve 150. Pregunta: «¿qué se perdió?». El filtro de estado: 150 son todas las citas del día y 91 solo las programadas.
- Clic 2: Lee la regla: corrección y tiempo son ejes independientes.

EJEMPLO: Agenda del 2026-03-10: 150 citas en total, 91 PROGRAMADA, 45 ATENDIDA y 14 CANCELADA. Una versión que olvida AND c.estado = 'PROGRAMADA' devuelve 150.

SI PREGUNTAN:
- «Si los conteos coinciden, ¿ya es la misma respuesta?» → Para una consulta con filtro es una buena prueba; para un conjunto completo no basta, porque pueden coincidir en número y ser filas distintas. Para eso está EXCEPT en los dos sentidos.

CUIDADO: «Se ve igual» o «trae más o menos lo mismo» no son prueba.

PASA A LA SIGUIENTE: La prueba fuerte para conjuntos completos: EXCEPT en los dos sentidos.

### [Slide 18] Optimizar no cambia el resultado: como se prueba

QUÉ ES (dilo así): Hay dos pruebas, según lo que se compare. Para una consulta con filtro, contar las filas de cada versión en la misma corrida. Para un conjunto completo, como un ranking, se restan los conjuntos con EXCEPT en los dos sentidos: lo que está en A y no en B, más lo que está en B y no en A. Si salen cero filas, son iguales.

CÓMO DARLA (≈2 min):
- Al entrar: Izquierda, prueba 1: dos COUNT(*) en una misma consulta; 91 = 91.
- Derecha: Prueba 2: (ANTES EXCEPT DESPUÉS) UNION ALL (DESPUÉS EXCEPT ANTES) devuelve 0 filas. Explica los dos sentidos: A EXCEPT B vacío solo dice que todo A está en B; B podría tener filas de más.
- Abajo: El contraejemplo real: si la reescritura usa COUNT(*) en vez de COUNT(m.id_mascota), la prueba 2 devuelve 12 filas, los 6 dueños sin mascotas con 0 de un lado y 1 del otro. Cierra: sin LIMIT y sin «se ve igual».

EJEMPLO: WITH antes AS (…), despues AS (…) SELECT 'sobra en ANTES', * FROM (SELECT * FROM antes EXCEPT SELECT * FROM despues) a UNION ALL SELECT 'sobra en DESPUES', * FROM (SELECT * FROM despues EXCEPT SELECT * FROM antes) b; devuelve 0 filas.

SI PREGUNTAN:
- «¿Y si una versión puede traer filas repetidas?» → EXCEPT elimina duplicados; en ese caso se usa EXCEPT ALL o se incluye la clave en el SELECT. En el ranking no pasa: hay una fila por dueño.

CUIDADO: Comparar solo las primeras 20 filas deja fuera justo las que fallan: los dueños con 0 quedan al final del ranking.

PASA A LA SIGUIENTE: Ahora el script de la clase, que junta todo lo visto.

### [Slide 19] El antes y el despues del script de la clase

QUÉ ES (dilo así): El script de la demo es autocontenido: crea las tablas, siembra el mismo volumen que el estudiante tiene en su pantalla y deja las estadísticas listas. Antes de optimizar se proyectan los conteos de control; después se corren la agenda ANTES y DESPUÉS, el ranking y las pruebas.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba a la izquierda, los conteos de control: 30.010 citas; el 2026-03-10, 91 PROGRAMADA, 45 ATENDIDA y 14 CANCELADA. Si no salen esos números, nada de lo demás cuadra.
- Arriba a la derecha: La coma: sin la condición de unión, 30.010 × 5.008 ≈ 150 millones de filas, y el motor no da ningún error.
- Abajo: JOIN … ON da el mismo plan que la coma: no acelera, pero el olvido salta a la vista. Y el LIMIT 50: con ORDER BY fecha_hora y sin índice, el motor igual lee toda la tabla, encuentra las 91 y las ordena; el LIMIT solo ahorra entregar 41.

EJEMPLO: Plan con LIMIT 50: Limit, luego Sort de 91 filas y, al fondo, Seq Scan on cita c con Rows Removed by Filter: 29919. El recorrido completo sigue ahí.

SI PREGUNTAN:
- «¿Entonces para qué el LIMIT?» → Para no transportar ni pintar filas que la pantalla no usa. Lo que evitaría leer toda la tabla es un índice sobre fecha_hora que entregue las filas ya ordenadas: Clase 7.

CUIDADO: La siembra recrea las tablas: córrela en una base vacía, nunca sobre una base con datos que alguien quiera conservar.

PASA A LA SIGUIENTE: ¿Dónde se corre todo esto, y qué no se puede medir ahí?

### [Slide 20] Donde se corre todo esto, y que no se puede medir aqui

QUÉ ES (dilo así): La herramienta del día es PostgreSQL compilado para ejecutarse dentro del navegador. Trae la base con volumen sembrado y soporta EXPLAIN, EXPLAIN ANALYZE y BUFFERS. Hay cosas que ahí no se pueden medir, y lo correcto es declararlas en vez de inventar un número.

CÓMO DARLA (≈2 min):
- Al entrar: Izquierda: lo que se mide y se ve en la salida. Subraya las 30.010 citas: medir sobre una base de 20 filas no sirve, porque todo cabe en una página y cualquier consulta tarda lo mismo.
- Derecha: Lo que no se puede medir: tiempos con la memoria vacía (vaciarla exige ser administrador), varias sesiones compitiendo (eso es la Clase 10) y volúmenes de cientos de miles de filas.
- Abajo: La frase final: filas y páginas son estables; los milisegundos varían incluso entre dos corridas seguidas.

EJEMPLO: Dos corridas seguidas de la agenda pueden diferir en milisegundos, incluso al doble; las dos dirán rows=91 y Rows Removed by Filter: 29919.

SI PREGUNTAN:
- «¿Puedo medir en mi propia base de la Clase 1?» → Solo si antes le fabricas volumen con generate_series. Con 20 filas el plan siempre es Seq Scan y las diferencias son ruido.

CUIDADO: No ofrezcas otra herramienta en línea como alterna: no tiene la base sembrada y da otros números.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 21] Demo del dia

QUÉ ES (dilo así): La demo corre el script de la clase y muestra con salidas reales lo que se explicó: la agenda optimizada devuelve lo mismo, el ranking deja de repetirse por dueño y la equivalencia se prueba con consultas.

CÓMO DARLA (≈15 min):
- Al entrar: 1) Siembra y conteos de control (30.010; 91/45/14). 2) Agenda ANTES y DESPUÉS con EXPLAIN (ANALYZE, BUFFERS): el ANTES estima rows=1 y entrega 91; el DESPUÉS estima 91. 3) La misma consulta con LIMIT 50: el Seq Scan sigue ahí.
- Después: 4) El ranking: corre primero la versión ANTES acotada a 200 dueños (WHERE d.id_dueno <= 200) y muestra loops=200; di que la completa es diez veces eso. 5) La reescritura con LEFT JOIN y GROUP BY. 6) Las pruebas: 91 = 91, EXCEPT con 0 filas y el contraejemplo COUNT(*) contra COUNT(c.id_cita).

EJEMPLO: En el contraejemplo, los dueños 2001 a 2006 dan 0 con COUNT(c.id_cita) y 1 con COUNT(*).

CUIDADO: La versión ANTES completa del ranking tarda minutos en el navegador (en una prueba, unos tres minutos y medio; la acotada, unos 20 s). Avisa antes de correrla: si alguien recarga la página, pierde lo que tenía.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada, con EXPLAIN ANALYZE antes y despues, en ExamLab.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 6 - Optimizacion de consultas/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 6 · Optimizacion de consultas · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. SQL es declarativo: quien decide el como es el optimizador
5. Leer un plan: es un arbol y se lee de adentro hacia afuera
6. EXPLAIN ANALYZE: la evidencia, no la opinion
7. Un plan, campo por campo
8. Las estadisticas: metadatos que describen los datos sin leerlos
9. Cardinalidad y selectividad: por que el motor decide lo que decide
10. Full table scan contra index scan, sin caricaturas
11. Predicado sargable: el antipatron que conecta con la Clase 7
12. El antipatron y su reescritura
13. Optimizar es un ANTES medible, no una opinion
14. La subconsulta correlacionada: 2.006 pasadas o una sola
15. Matar la subconsulta correlacionada
16. La subconsulta correlacionada en el plan: loops
17. Optimizar no cambia el resultado, y eso se demuestra
18. Optimizar no cambia el resultado: como se prueba
19. El antes y el despues del script de la clase
20. Donde se corre todo esto, y que no se puede medir aqui
21. Demo del dia
22. Cierre · Clase 6

> Privado, no se proyecta: `Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Optimizacion de consultas · VetCare.»
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
- Optimizar consultas parte de entender que el motor NO ejecuta el SQL tal cual se escribe: primero lo transforma en un plan de ejecucion (que tablas leer, en que orden, con o sin indice) y ese plan es lo que realmente determina el tiempo de respuesta.
- Tres cuellos de botella clasicos: (1) SELECT * trae columnas que nadie usa y aumenta el trafico/memoria; (2) JOIN sin filtro temprano obliga a cruzar tablas completas antes de descartar filas; (3) aplicar una funcion sobre la columna en el WHERE (ej. WHERE UPPER(nombre)='LUNA') impide que el motor use un indice normal sobre esa columna (esto se llama 'no-sargable').
- Reescritura tipica: proyectar solo columnas necesarias (SELECT nombre, fecha en vez de SELECT *), aplicar el filtro mas selectivo primero (WHERE fecha >= hoy antes del JOIN si reduce mucho el conjunto), y mover comparaciones a la forma que el motor pueda usar con indice.
- El cuarto cuello de botella, y el mas caro: una subconsulta correlacionada en la lista de columnas se evalua UNA VEZ POR FILA del exterior — el plan lo dice con loops=2006 —, y se elimina reescribiendola como LEFT JOIN + GROUP BY, que hace una sola pasada. Con LEFT JOIN hay que contar la columna, COUNT(c.id_cita), y no COUNT(*): el LEFT JOIN fabrica una fila de NULL por cada dueno sin citas, y COUNT(*) cuenta filas, asi que reportaria 1 donde la respuesta es 0.
- Optimizar NO puede cambiar el resultado, y eso se demuestra, no se afirma: un COUNT(*) de cada version que coincida, y para conjuntos completos un EXCEPT en los DOS sentidos que devuelva cero filas (EXCEPT no es simetrico: A EXCEPT B vacio no dice nada sobre filas de mas en B).
- EXPLAIN muestra el plan que el motor ESTIMA; EXPLAIN ANALYZE lo ejecuta de verdad y agrega actual rows, loops y Execution Time. En PostgreSQL el recorrido completo de tabla se llama Seq Scan (en Oracle, TABLE ACCESS FULL): verlo sobre una tabla grande donde se esperaba un indice es la senal de que el WHERE o el tipo de dato bloquea el indice.
- Conexion con Clase 7: optimizar consultas y crear indices son las dos caras de la misma moneda — una consulta mal escrita no aprovecha ni el mejor indice, y el mejor indice no compensa una consulta que fuerza un escaneo completo. Hoy NO se crea ningun indice: por eso la mejora que se mide es la de filas procesadas y pasadas sobre la tabla, no un cambio de Seq Scan a Index Scan.
- Error de docente que no domina el tema: pedir 'la consulta más rápida' sin definir contra que se compara (volumen de datos, indices existentes) — optimizar siempre es relativo a un antes medible, por eso el taller pide guardar la version antes Y despues, no solo la version final.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 21]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada, con EXPLAIN ANALYZE antes y despues, en ExamLab.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 EXPLAIN ANALYZE ANTES vs DESPUES: el nodo no cambia, las pasadas si (loops 2006 -> 1) [[captura: salida-explain-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 6 - Optimizacion de consultas/Taller PI - Clase 6 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Primera pareja de consultas antes/despues del PI
Actividades:
1. Reescribir la agenda del dia corrigiendo sus 4 antipatrones (SELECT *, joins con coma, to_char sobre la fecha, UPPER sobre el estado) y probar con COUNT(*) que las dos versiones devuelven las mismas 91 filas.
2. Medir con EXPLAIN (ANALYZE, BUFFERS) las dos versiones, y con EXPLAIN ANALYZE una tercera que le anada LIMIT 50, y anotar las tres en comentarios: nodo mas costoso, filas estimadas vs reales y tiempo.
3. Matar la subconsulta correlacionada del ranking de duenos: LEFT JOIN + GROUP BY + COUNT(c.id_cita), y demostrar la equivalencia con EXCEPT en los dos sentidos.
4. Responder la de seleccion multiple sobre antipatrones (6 afirmaciones, 4 correctas).
5. Escribir la justificacion tecnica de media pagina y guardar 06_opt_antes.sql / 06_opt_despues.sql en la carpeta del PI.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 consultas (antes/despues) + justificacion (media pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 6/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 6 - VetCare.docx`. Clave para usted: `Quiz Clase 6 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 22]
**Decir:** «Queda visto: Optimizacion de consultas · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 22] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 06_opt_consultas.sql.

## Capturas
Carpeta `Kit docente/Clase 6/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
