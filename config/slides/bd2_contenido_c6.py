# -*- coding: utf-8 -*-
"""BD II Clase 6 · Optimizacion de consultas: ideas proyectadas y GUION de cada lamina.

Formato y uso: `bd2_contenido_data.py` y `notas_guion.py` (se fusiona solo). Cifras y salidas
verificadas en PGlite (PostgreSQL 18 en Node) sobre la siembra de la clase: 30.010 citas,
5.008 mascotas, 2.006 duenos, 16 veterinarios; el 2026-03-10 tiene 150 citas (91 PROGRAMADA,
45 ATENDIDA, 14 CANCELADA). Los milisegundos son de una corrida y cambian por maquina.

Los pasos de cada animacion estan en `config/animaciones/bd2/clase6/<huella>.js`.
"""

CONTENIDO = {
    6: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "Hasta ahora la pregunta era si una consulta funciona. Hoy es otra: "
                           "cuánto trabajo le cuesta al motor responderla, cómo se lee ese "
                           "trabajo en el plan de ejecución y cómo se demuestra que una versión "
                           "más rápida devuelve exactamente lo mismo.",
                "pasos": [
                    "Lee el tema y pregunta: «si dos consultas devuelven lo mismo, ¿cómo sabemos "
                    "cuál es mejor?». Deja que respondan una o dos personas; casi siempre dirán "
                    "«la que tarde menos».",
                    ("Después", "Cierra: «al final de hoy lo van a decir con evidencia: el plan "
                     "de ejecución, cuántas filas pasa cada paso y cuántas veces se repite»."),
                ],
                "puente": "Empezamos por quién decide cómo se ejecuta una consulta: el optimizador.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El recorrido de las dos horas: teoría con una lámina por concepto, "
                           "demo sobre la base de la clínica y práctica opcional.",
                "pasos": ["Señala solo los tramos; no te detengas. La práctica está en la carpeta "
                          "de la clase y es opcional."],
            },
        },
        "SQL es declarativo": {
            "ideas": [
                "SQL es **declarativo**: la consulta dice qué datos quiere y nunca cómo "
                "obtenerlos.",
                "El **optimizador** arma varios planes posibles, estima el costo de cada uno y "
                "elige el más barato.",
                "Un **plan de ejecución** es el árbol de operaciones que de verdad corre: qué "
                "tabla leer, cómo y en qué orden.",
                "Todos los planes devuelven **el mismo resultado**; cambia el tiempo, a veces "
                "cien o mil veces.",
            ],
            "notas": {
                "min": 4,
                "explica": "Cuando escribimos una consulta solo describimos el resultado. El "
                           "motor la pasa por tres etapas: el analizador revisa que esté bien "
                           "escrita y que existan las tablas y columnas; el optimizador arma "
                           "varios planes, les calcula un costo y elige el más barato; el "
                           "ejecutor corre ese plan. Optimizar es ayudar al optimizador a "
                           "encontrar el plan bueno.",
                "pasos": [
                    "Arriba, la consulta dice QUÉ; debajo, el analizador. Di: «antes de pensar "
                    "en velocidad, el motor comprueba que la consulta tenga sentido: sintaxis, "
                    "tablas y columnas». Si falla aquí, el error sale antes de leer un dato.",
                    "El optimizador y tres planes candidatos con su costo: 1.240, 85 y 9.600, en "
                    "unidades del motor, no en milisegundos. Elige el B, el más barato. "
                    "Pregunta: «¿los tres devuelven lo mismo?».",
                    "El ejecutor corre solo el plan elegido. Lee la conclusión: los tres planes "
                    "devuelven exactamente las mismas filas; lo único que cambia es el trabajo.",
                ],
                "ejemplo": "La agenda del día cruza cita, mascota, dueno y veterinario: con 4 "
                           "tablas hay 24 órdenes posibles de unión (4 × 3 × 2 × 1), y "
                           "multiplicados por las formas de leer y de cruzar pasan del millar de "
                           "planes. El optimizador no los prueba todos: poda y decide en "
                           "milisegundos.",
                "preguntas": [
                    ("¿Puedo obligar al motor a usar un plan?",
                     "PostgreSQL no trae «hints» como Oracle. Se le ayuda escribiendo la "
                     "consulta para que pueda usar lo que existe: filtros sobre columnas "
                     "desnudas, estadísticas al día e índices adecuados."),
                    ("¿El costo está en milisegundos?",
                     "No. Es una unidad relativa del motor (1 = leer una página de forma "
                     "secuencial); sirve para comparar planes, no para medir tiempo."),
                ],
                "cuidado": "No digas que el optimizador «prueba todos los planes»: estima con "
                           "estadísticas, poda y elige; por eso a veces se equivoca.",
                "puente": "Para saber qué plan eligió hay que aprender a leerlo: es un árbol.",
            },
        },
        "Leer un plan": {
            "ideas": [
                "EXPLAIN muestra el **plan** que el motor eligió, sin ejecutar la consulta.",
                "El plan es un **árbol**: las líneas más indentadas son las hojas y se ejecutan "
                "primero.",
                "Cada nodo recibe las filas de sus hijos; la **primera línea** impresa es la "
                "última operación.",
                "De un plan se leen el **nodo más costoso**, las filas estimadas contra las "
                "reales y el tiempo total.",
            ],
            "notas": {
                "min": 4,
                "explica": "EXPLAIN delante de una consulta no la ejecuta: muestra el plan que "
                           "el optimizador eligió. Se imprime como una lista con sangrías, pero "
                           "es un árbol: cada línea con más sangría es hija de la de arriba. "
                           "Primero corren las hojas, que leen las tablas, y la primera línea es "
                           "la última operación, la que entrega el resultado.",
                "pasos": [
                    "Lee en voz alta lo que imprime EXPLAIN para la consulta del día (cita con "
                    "mascota, citas del 2026-03-10): Hash Join arriba; debajo y más adentro, el "
                    "Seq Scan sobre cita con su filtro y el Hash armado sobre el Seq Scan de "
                    "mascota. Pregunta: «¿qué ocurre primero?». La mayoría dirá «el Hash Join».",
                    "Las mismas líneas dibujadas como árbol: el Hash Join es la raíz y los dos "
                    "Seq Scan son las hojas. La sangría decide quién es hijo de quién.",
                    "Los números marcan el orden real: 1) se lee cita, 2) se lee mascota, 3) con "
                    "mascota se arma la tabla hash, 4) el Hash Join cruza. Lee la regla: la "
                    "primera línea es la ÚLTIMA operación.",
                ],
                "ejemplo": "En la base de la clase ese plan dice Hash Join (cost=149.68..851.22 "
                           "rows=150): 150 filas estimadas, que son las 150 citas del "
                           "2026-03-10.",
                "preguntas": [
                    ("¿EXPLAIN ejecuta la consulta?",
                     "No: solo muestra el plan con estimaciones. EXPLAIN ANALYZE sí la ejecuta "
                     "y agrega tiempos y filas reales; por eso sobre un UPDATE o un DELETE se "
                     "envuelve en BEGIN … ROLLBACK."),
                    ("¿Qué es el Hash?",
                     "Una tabla en memoria armada con las filas de mascota, organizada por "
                     "id_mascota, para encontrar rápido la mascota de cada cita al cruzar."),
                ],
                "cuidado": "El error más común, también del docente, es leer el plan de arriba "
                           "hacia abajo como una lista de pasos. Si se enseña así, el grupo "
                           "interpretará al revés todos los planes del curso.",
                "puente": "Con ANALYZE el plan deja de ser una predicción y se vuelve evidencia.",
            },
        },
        "EXPLAIN ANALYZE: la evidencia": {
            "notas": {
                "min": 3,
                "explica": "EXPLAIN (ANALYZE, BUFFERS) ejecuta la consulta de verdad y muestra, "
                           "nodo por nodo, lo que pasó: filas reales, tiempo y páginas leídas. "
                           "Es la evidencia de una optimización; sin ella, «es más rápida» es "
                           "una opinión.",
                "pasos": [
                    ("Al entrar", "Líneas 1-5: la consulta del día (cita con mascota, rango del "
                     "2026-03-10) precedida de EXPLAIN (ANALYZE, BUFFERS). Si puedes, "
                     "ejecútala en vivo."),
                    ("Líneas 7-9", "El nodo: hoy sale Seq Scan on cita c, porque la base no tiene "
                     "índices fuera de las claves primarias. Las filas: el motor estimó 150 y "
                     "salieron 150 (actual rows=150)."),
                    ("Líneas 10-12", "Rows Removed by Filter: 29860 es lo que leyó para nada; "
                     "Buffers: shared hit=251 son las 251 páginas de 8 KB de cita. El "
                     "Execution Time cambia entre corridas: lo estable son filas y páginas."),
                ],
                "ejemplo": "Una corrida en el navegador: Seq Scan on cita c … rows=150 … Rows "
                           "Removed by Filter: 29860 · Buffers: shared hit=251 · Execution Time "
                           "≈ 35 ms. Las dos primeras cifras salen idénticas en cualquier "
                           "equipo; el tiempo no.",
                "preguntas": [
                    ("¿Qué significa «shared hit»?",
                     "Que la página ya estaba en memoria; «read» significaría que hubo que "
                     "traerla del disco. En el navegador todo vive en memoria, así que casi "
                     "siempre verás hit."),
                    ("¿Puedo usar EXPLAIN ANALYZE con un DELETE?",
                     "Sí, pero lo ejecuta de verdad: envuélvelo en BEGIN y ROLLBACK para no "
                     "borrar nada."),
                ],
                "cuidado": "Si BUFFERS no responde en algún equipo, EXPLAIN ANALYZE a secas sirve "
                           "igual. Lo que no sirve es comparar milisegundos entre máquinas "
                           "distintas.",
                "puente": "Ahora cada campo de una línea del plan, uno por uno.",
            },
        },
        "Un plan, campo por campo": {
            "ideas": [
                "El campo **cost** está en una unidad relativa del motor, no en milisegundos.",
                "Las filas estimadas (**rows**) se comparan con las reales (**actual rows**).",
                "El tiempo real (**actual time**) es por vuelta: se multiplica por **loops**.",
                "Diez veces o más entre estimado y real delata **estadísticas** viejas o filtros "
                "que dependen entre sí.",
            ],
            "notas": {
                "min": 3,
                "explica": "Cada línea del plan trae dos grupos de números. En el primer "
                           "paréntesis, lo que el motor estimó antes de ejecutar: costo, filas y "
                           "ancho de la fila. En el segundo, lo que pasó: tiempo real, filas "
                           "reales y cuántas veces se repitió ese nodo (loops). Leer un plan es "
                           "comparar los dos grupos.",
                "pasos": [
                    ("Al entrar", "Arriba, una línea real del plan de hoy: Seq Scan on cita c "
                     "(cost=0.00..701.15 rows=150 width=16) y su parte real (actual time … "
                     "rows=150 loops=1)."),
                    ("Columna izquierda", "Lo estimado: cost es arranque..total en la unidad del "
                     "motor (1 = leer una página), no milisegundos; rows, las filas que cree "
                     "que saldrán; width, los bytes promedio por fila."),
                    ("Columna derecha", "Lo real: actual time en milisegundos POR VUELTA; rows, "
                     "las filas que salieron; loops, cuántas veces se ejecutó el nodo."),
                    ("Abajo", "La regla del nodo más costoso: tiempo por loops, sabiendo que el "
                     "tiempo de un nodo ya incluye el de sus hijos. Un nodo de 0,5 ms con "
                     "loops=2006 cuesta un segundo aunque parezca el más barato."),
                ],
                "ejemplo": "La versión ANTES de la agenda (con to_char y UPPER sobre las "
                           "columnas) estima rows=1 y entrega 91: con una función sobre la "
                           "columna el motor no puede usar sus estadísticas y aplica una "
                           "selectividad por omisión. Esa diferencia de 91 veces es la señal que "
                           "hay que saber leer.",
                "preguntas": [
                    ("¿Una diferencia de 2 veces entre estimado y real es grave?",
                     "No, es normal. La alarma es de 10 veces o más: estadísticas viejas o dos "
                     "filtros que el motor cree independientes y no lo son."),
                    ("¿Por qué la primera línea muestra el tiempo más alto?",
                     "Porque el tiempo de cada nodo incluye el de sus hijos y la raíz los "
                     "acumula todos. El culpable se busca por el tiempo propio de cada nodo "
                     "multiplicado por loops."),
                ],
                "cuidado": "Confundir cost con milisegundos es el error más frecuente al leer "
                           "planes: el costo solo sirve para comparar planes del mismo motor.",
                "puente": "¿De dónde saca el motor sus estimaciones? De las estadísticas.",
            },
        },
        "Las estadisticas": {
            "ideas": [
                "Las **estadísticas** describen los datos sin leerlos: filas, páginas, valores "
                "distintos y nulos.",
                "Se recolectan con **ANALYZE**; en la base de hoy ya están al día.",
                "También guardan cómo se **reparten** los valores: estado concentrado, "
                "fecha_hora pareja.",
                "Por eso el **plan** puede cambiar sin tocar la consulta: cambiaron los datos o "
                "sus estadísticas.",
            ],
            "notas": {
                "min": 3,
                "explica": "El optimizador no lee la tabla para decidir: consulta una ficha que "
                           "la describe. Cuántas filas tiene, cuántas páginas ocupa, cuántos "
                           "valores distintos hay en cada columna, qué fracción es nula y cómo "
                           "se reparten los valores. Esa ficha son las estadísticas, y las "
                           "actualiza el comando ANALYZE.",
                "pasos": [
                    "La tabla cita, ANALYZE y la ficha con las cifras reales de la base de hoy: "
                    "30.010 filas, 251 páginas de 8 KB, 3 valores distintos en estado, 1.810 en "
                    "fecha_hora y ningún nulo.",
                    "El reparto: estado está concentrado (61 % PROGRAMADA, 30 % ATENDIDA, 9 % "
                    "CANCELADA) y fecha_hora es pareja (150 citas cada día). Con eso el motor "
                    "calcula cuántas filas dejará pasar cada filtro.",
                    "Lee la conclusión y remata: el plan no es propiedad del texto SQL; es una "
                    "decisión tomada con las estadísticas de ese momento.",
                ],
                "ejemplo": "SELECT relpages, reltuples FROM pg_class WHERE relname = 'cita'; "
                           "devuelve 251 y 30010. SELECT attname, n_distinct FROM pg_stats WHERE "
                           "tablename = 'cita'; muestra 3 para estado y 1810 para fecha_hora.",
                "preguntas": [
                    ("¿Cada cuánto hay que correr ANALYZE?",
                     "En un servidor, PostgreSQL lo hace solo en segundo plano (autovacuum) "
                     "cuando la tabla cambia bastante. Después de una carga grande o de crear "
                     "un índice conviene correrlo a mano."),
                    ("¿Por qué la misma consulta cambia de plan de un día a otro?",
                     "Porque la tabla creció, se recolectaron estadísticas nuevas, alguien "
                     "creó un índice o el valor buscado es más o menos frecuente."),
                ],
                "cuidado": "No confundas «predicados correlacionados» (dos filtros que no son "
                           "independientes y engañan la estimación) con la «subconsulta "
                           "correlacionada» que viene después, que es un problema de cuántas "
                           "veces se ejecuta algo.",
                "puente": "Con esas estadísticas el motor calcula dos números: cardinalidad y "
                          "selectividad.",
            },
        },
        "Cardinalidad y selectividad": {
            "ideas": [
                "La **cardinalidad** de una columna es cuántos valores distintos tiene: estado "
                "tiene 3.",
                "La **selectividad** de un filtro es la fracción de filas que deja pasar, entre "
                "0 y 1.",
                "El filtro **estado = 'PROGRAMADA'** deja pasar el 61 %, y la fecha del "
                "2026-03-10 apenas el 0,5 %.",
                "Pocas filas favorecen un **índice**; muchas, leer la **tabla entera**.",
            ],
            "notas": {
                "min": 4,
                "explica": "Cardinalidad es cuántos valores distintos tiene una columna. "
                           "Selectividad es qué fracción de las filas sobrevive a un filtro: 0 es "
                           "ninguna, 1 es todas. Con ellas el motor estima cuántas filas saldrán "
                           "de cada filtro, y de eso depende si conviene ir por un índice o leer "
                           "la tabla completa.",
                "pasos": [
                    "Cardinalidad: cita.estado tiene 3 valores (baja); dueno.id_dueno tiene "
                    "2.006, uno por fila (alta).",
                    "Selectividad con tres filtros reales de la base de hoy: estado = "
                    "'PROGRAMADA' deja 18.187 de 30.010 (0,61); la fecha del 2026-03-10 deja 150 "
                    "(0,005); los dos juntos, 91 (0,003). Pregunta: «¿a cuál le serviría un "
                    "índice?».",
                    "La decisión: muchas filas, leer la tabla entera; pocas, ir por un índice. "
                    "Como convención de oficio, por debajo del 5 % suele ganar el índice y por "
                    "encima del 20 % la tabla entera; el motor no usa porcentajes, compara "
                    "costos.",
                ],
                "ejemplo": "De 30.010 citas, 91 son el 0,3 %: un índice ayudaría mucho. 18.187 "
                           "son el 61 %: un índice solo sobre estado no ayudaría.",
                "preguntas": [
                    ("¿Por qué no indexar estado si se filtra tanto por él?",
                     "Porque deja pasar el 61 % de las filas: leer la tabla de corrido sale más "
                     "barato que saltar a la tabla 18.187 veces desde un índice."),
                    ("¿Cómo sabe el motor que la fecha deja 150?",
                     "Por las estadísticas de fecha_hora: sus valores distintos y su reparto. "
                     "Si estuvieran viejas, la estimación fallaría."),
                ],
                "cuidado": "«Cardinalidad» también se usa para las filas que entrega un nodo del "
                           "plan: aclara en qué sentido la estás usando.",
                "puente": "Con esas cifras, los dos caminos para leer una tabla: completa o por "
                          "índice.",
            },
        },
        "Full table scan contra index scan": {
            "ideas": [
                "Un **Seq Scan** lee todas las páginas de la tabla en orden y descarta lo que no "
                "cumple.",
                "Un **Index Scan** baja por el índice y salta a la tabla por cada fila "
                "encontrada.",
                "Para un día de citas: 251 páginas seguidas contra unas 153 lecturas "
                "**dispersas**.",
                "A este volumen la diferencia es pequeña: la ventaja del índice crece con el "
                "**tamaño**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Hay dos maneras básicas de leer una tabla. El recorrido completo "
                           "(Seq Scan) lee todas las páginas una tras otra y descarta en memoria "
                           "lo que no cumple. El acceso por índice baja por el árbol del índice "
                           "y, por cada coincidencia, va a buscar la fila a la tabla: pocas "
                           "lecturas, pero dispersas. Cuál conviene depende de cuántas filas "
                           "salen.",
                "pasos": [
                    "Seq Scan: las páginas se leen de corrido. En la base de hoy, cita ocupa 251 "
                    "páginas de 8 KB, y se leen todas aunque solo sirvan 150 filas.",
                    "Index Scan: 2 o 3 lecturas para bajar el árbol y una lectura dispersa por "
                    "cada fila encontrada. Para las 150 citas de un día, unas 153 lecturas.",
                    "Lee la regla y di lo honesto: 251 contra 153 es del mismo orden. Con "
                    "300.000 citas el Seq Scan pasaría a unas 2.500 páginas y el índice seguiría "
                    "en unas 153: ahí sí gana por mucho.",
                ],
                "ejemplo": "Hoy la base no tiene índice sobre fecha_hora: el plan de las citas "
                           "del 2026-03-10 siempre dirá Seq Scan on cita. El cambio a un acceso "
                           "por índice es el tema de la Clase 7.",
                "preguntas": [
                    ("Si el índice es mejor, ¿por qué el motor a veces lo ignora?",
                     "Porque cuando salen muchas filas, saltar a la tabla por cada una cuesta "
                     "más que leerla de corrido. El motor compara costos, no aplica una regla "
                     "fija."),
                    ("¿Qué es una lectura dispersa?",
                     "Leer una página que no es la siguiente de la anterior. En disco cuesta "
                     "más: un PostgreSQL de servidor la valora en 4 y la secuencial en 1."),
                ],
                "cuidado": "No prometas un Index Scan para hoy: en esta base no hay índices fuera "
                           "de las claves primarias. Hoy se miden filas procesadas y pasadas "
                           "sobre la tabla.",
                "puente": "Hay una forma de escribir el filtro que impide usar cualquier índice: "
                          "la función sobre la columna.",
            },
        },
        "Predicado sargable": {
            "ideas": [
                "Un filtro es **sargable** si el motor puede resolverlo navegando un índice.",
                "Para eso la **columna** tiene que quedar sola a un lado de la comparación.",
                "to_char(fecha_hora, …) o UPPER(estado) obligan a calcular la **función** en "
                "cada fila.",
                "Se reescribe como **rango** sobre la columna, o sin la función si el dato ya "
                "está normalizado.",
            ],
            "notas": {
                "min": 4,
                "explica": "Un índice guarda los valores de la columna tal como están. Si el "
                           "filtro le aplica una función —to_char a la fecha, UPPER al estado— "
                           "el motor no puede saber qué entradas cumplen sin calcular la función "
                           "fila por fila: el filtro no es sargable. Se arregla dejando la "
                           "columna sola y pasando el cálculo al otro lado.",
                "pasos": [
                    "Las dos formas no sargables de la consulta de agenda: to_char(c.fecha_hora, "
                    "'YYYY-MM-DD') = '2026-03-10' y UPPER(c.estado) = 'PROGRAMADA'. El índice "
                    "guarda fecha_hora, no to_char(fecha_hora).",
                    "La reescritura: un rango sobre la columna desnuda (>= '2026-03-10 00:00:00' "
                    "y < '2026-03-11 00:00:00') y la comparación directa del estado. UPPER se "
                    "puede quitar porque el CHECK solo admite PROGRAMADA, ATENDIDA o CANCELADA, "
                    "en mayúsculas.",
                    "Lee la conclusión y aclara: hoy no hay índice sobre fecha_hora, así que el "
                    "plan sigue en Seq Scan. Lo que se gana hoy es no calcular la función 30.010 "
                    "veces y que el motor estime bien cuántas filas vienen.",
                ],
                "ejemplo": "Tampoco son sargables EXTRACT(YEAR FROM fecha_hora) = 2026 ni "
                           "UPPER(m.nombre) = 'LUNA'. El primero se reescribe como rango del año; "
                           "el segundo, si el negocio lo necesita, con un índice sobre la "
                           "expresión, que es de la Clase 7.",
                "preguntas": [
                    ("¿Entonces nunca puedo usar funciones en el WHERE?",
                     "Sí puedes, sobre el valor constante, no sobre la columna. Y si la "
                     "función sobre la columna es necesaria, existe el índice sobre la "
                     "expresión: CREATE INDEX … ON mascota (UPPER(nombre))."),
                    ("¿Por qué el rango termina en < '2026-03-11' y no en <= '2026-03-10 "
                     "23:59:59'?",
                     "Porque el rango semiabierto no deja huecos: una cita a las 23:59:59.5 "
                     "quedaría fuera del segundo."),
                ],
                "cuidado": "No afirmes que la versión sargable ya usa un índice: sin índice "
                           "sobre fecha_hora, hoy las dos versiones hacen Seq Scan.",
                "puente": "Veámoslo en código: las dos versiones devuelven exactamente lo mismo.",
            },
        },
        "El antipatron y su reescritura": {
            "notas": {
                "min": 3,
                "explica": "Las dos consultas buscan las citas del 2026-03-10. La primera aplica "
                           "una función a la columna; la segunda compara la columna desnuda con "
                           "un rango. Devuelven las mismas 150 citas, pero solo la segunda deja "
                           "abierta la puerta a un índice.",
                "pasos": [
                    ("Al entrar", "Líneas 1-3: la versión ANTES. Subraya TO_CHAR(fecha_hora, …): "
                     "el motor lo calcula en las 30.010 filas antes de comparar."),
                    ("Líneas 5-8", "La versión DESPUÉS: mismo SELECT y el filtro como rango "
                     "semiabierto, >= el día y < el día siguiente."),
                    ("Líneas 10-11", "Lee el comentario: mismas 150 citas. Si preguntan por la "
                     "velocidad, hoy las dos hacen Seq Scan; en una corrida en el navegador la "
                     "primera tardó unos 130 ms y la segunda unos 40 ms, solo por no calcular "
                     "la función."),
                ],
                "ejemplo": "SELECT COUNT(*) de cada versión devuelve 150 en las dos, y un EXCEPT "
                           "entre ellas devuelve 0 filas.",
                "cuidado": "Los milisegundos cambian entre corridas y entre equipos. Lo que se "
                           "afirma con seguridad es el conteo de filas y que el Filter de la "
                           "segunda ya no contiene to_char.",
                "puente": "Juntemos todos los cambios de la consulta de agenda en una sola "
                          "comparación ANTES/DESPUÉS.",
            },
        },
        "Optimizar es un ANTES medible": {
            "notas": {
                "min": 3,
                "explica": "La consulta de agenda del día tiene cuatro defectos, y cada uno su "
                           "arreglo. No es una cuestión de gusto: las dos versiones devuelven las "
                           "mismas 91 filas y lo que cambia se mide en el plan, en filas "
                           "procesadas y pasadas sobre la tabla.",
                "pasos": [
                    ("Al entrar", "Columna ANTES, de arriba abajo: SELECT * arrastra todas las "
                     "columnas de 4 tablas; to_char y UPPER esconden las columnas; las comas "
                     "permiten un producto cartesiano si falta una condición; la subconsulta "
                     "por fila se repite 2.006 veces."),
                    ("Columna DESPUÉS", "Los arreglos en el mismo orden: solo las 6 columnas que "
                     "usa la pantalla, rango y comparación directa, JOIN … ON y LEFT JOIN con "
                     "GROUP BY."),
                    ("Abajo", "El subtítulo: mismas 91 filas, y sin índices no hay Index Scan. "
                     "Subraya que JOIN … ON no acelera: da el mismo plan que las comas; lo que "
                     "gana es que un ON olvidado sea un error de sintaxis y no un cartesiano."),
                ],
                "ejemplo": "Plan del ANTES de la agenda: Seq Scan on cita c con rows=1 estimada y "
                           "91 reales. Plan del DESPUÉS: el mismo Seq Scan, con rows=91 estimada "
                           "y 91 reales. Mismo recorrido, pero ahora el motor sabe cuántas filas "
                           "vienen.",
                "preguntas": [
                    ("¿Cambiar las comas por JOIN … ON no hace la consulta más rápida?",
                     "No. PostgreSQL convierte las dos formas al mismo plan interno; se gana "
                     "legibilidad y seguridad, no milisegundos."),
                ],
                "cuidado": "Si presentas JOIN … ON como mejora de rendimiento, enseñas algo "
                           "falso: es una mejora de seguridad y de legibilidad.",
                "puente": "El cambio que sí es de órdenes de magnitud: la subconsulta "
                          "correlacionada.",
            },
        },
        "La subconsulta correlacionada: 2": {
            "ideas": [
                "Una subconsulta es **correlacionada** si menciona una columna de la consulta de "
                "afuera.",
                "En el SELECT se ejecuta **una vez por cada fila** de afuera: 2.006 dueños, "
                "2.006 veces.",
                "El plan lo delata con un nodo **SubPlan** y **loops=2006**.",
                "Con **LEFT JOIN** y GROUP BY el mismo resultado sale en una sola pasada.",
            ],
            "notas": {
                "min": 4,
                "explica": "Una subconsulta correlacionada usa un valor de la fila de afuera "
                           "(aquí, d.id_dueno). Como su resultado cambia con cada fila, el motor "
                           "no puede calcularla una vez y reutilizarla: la ejecuta una vez por "
                           "cada fila de la consulta exterior. Con 2.006 dueños son 2.006 "
                           "ejecuciones. La misma pregunta se responde en una sola pasada "
                           "uniendo y agrupando.",
                "pasos": [
                    "ANTES: por cada uno de los 2.006 dueños, la subconsulta cuenta sus mascotas "
                    "recorriendo las 5.008 de la tabla. Son 2.006 ejecuciones y unos 10 "
                    "millones de filas leídas para producir 2.006 números.",
                    "DESPUÉS: dueno LEFT JOIN mascota y GROUP BY por dueño. Cada tabla se lee "
                    "una sola vez y se agrupa: una pasada.",
                    "Las dos devuelven las mismas 2.006 filas. Es la única mejora del día de "
                    "órdenes de magnitud, y no necesita ningún índice: se eliminaron 2.005 "
                    "recorridos.",
                ],
                "ejemplo": "En una corrida en el navegador, la versión ANTES tardó unos 4,9 s y la "
                           "reescrita unos 0,19 s: más de 25 veces menos. Los segundos cambian "
                           "por máquina; el loops=2006 no.",
                "preguntas": [
                    ("¿Toda subconsulta es lenta?",
                     "No. Una subconsulta que no depende de la fila de afuera se calcula una "
                     "sola vez. El problema es la correlacionada en la lista de columnas, que se "
                     "repite por fila."),
                    ("¿Por qué LEFT JOIN y no JOIN?",
                     "Porque con JOIN desaparecen los 6 dueños que no tienen mascotas: el "
                     "reporte pasa de 2.006 a 2.000 filas."),
                ],
                "cuidado": "No uses «correlacionada» a secas para dos cosas distintas: los "
                           "predicados correlacionados (un problema de estimación) no tienen "
                           "nada que ver con esto.",
                "puente": "Así se ve en código, con los dos detalles que deciden si el resultado "
                          "es el mismo.",
            },
        },
        "Matar la subconsulta": {
            "notas": {
                "min": 3,
                "explica": "La reescritura completa: la versión que repite la subconsulta por "
                           "dueño y la que une y agrupa una sola vez. Dos detalles deciden que "
                           "el resultado sea idéntico: LEFT JOIN y COUNT de una columna.",
                "pasos": [
                    ("Al entrar", "Líneas 1-5: ANTES. La subconsulta está en la lista de "
                     "columnas y menciona d.id_dueno, de afuera: se ejecuta una vez por dueño "
                     "(loops=2006 en el plan)."),
                    ("Líneas 7-12", "DESPUÉS: LEFT JOIN mascota, GROUP BY d.id_dueno, d.nombre y "
                     "COUNT(m.id_mascota). Se agrupa por id_dueno para no sumar como uno a dos "
                     "dueños que se llamen igual."),
                    ("Líneas 14-15", "Los dos detalles. LEFT y no JOIN: con JOIN se pierden los 6 "
                     "dueños sin mascotas. COUNT(m.id_mascota) y no COUNT(*): el LEFT JOIN deja "
                     "una fila con NULL para esos dueños; COUNT(*) la cuenta como 1 y COUNT de "
                     "la columna da 0."),
                ],
                "ejemplo": "Los dueños 2001 a 2006 de la base de hoy no tienen mascotas: con "
                           "COUNT(m.id_mascota) dan 0 y con COUNT(*) dan 1. El primero del "
                           "ranking es Marcela Diaz, con 5 mascotas.",
                "preguntas": [
                    ("¿Por qué agrupar por d.id_dueno y no solo por d.nombre?",
                     "Porque dos dueños pueden llamarse igual: agrupar solo por nombre los "
                     "sumaría como si fueran uno."),
                ],
                "cuidado": "Aceptar COUNT(*) «porque el total sale igual» es el error típico al "
                           "revisar: solo cambia en los dueños sin mascotas, que quedan al final "
                           "del ranking.",
                "puente": "¿Cómo se ve ese 2.006 en el plan? En un campo: loops.",
            },
        },
        "La subconsulta correlacionada en el plan": {
            "ideas": [
                "En el plan, la subconsulta es un nodo **SubPlan** con **loops=2006**.",
                "Su **actual time** es por vuelta: 2,3 ms × 2.006 vueltas son unos 4,6 "
                "segundos.",
                "La reescritura deja un solo **HashAggregate** y todos los nodos con loops=1.",
                "Va **LEFT JOIN** para no perder a los dueños sin mascotas, y COUNT de la "
                "columna para que den 0.",
            ],
            "notas": {
                "min": 2,
                "explica": "loops es el único campo del plan que dice «esto se repitió». Un "
                           "nodo puede mostrar un tiempo pequeño y ser el más caro, porque ese "
                           "tiempo es por vuelta. La lámina muestra el plan real de la versión "
                           "ANTES y el de la reescritura.",
                "pasos": [
                    ("Al entrar", "Arriba, el ANTES: Seq Scan on dueno d y, colgado de él, "
                     "SubPlan 1 con un Aggregate de 2,3 ms y loops=2006 (resaltado). Debajo, el "
                     "Seq Scan on mascota con Rows Removed by Filter: 5006 en cada vuelta."),
                    ("La cuenta", "2,3 ms por 2.006 vueltas ≈ 4,6 s: el nodo que parece barato es "
                     "el culpable. Quien solo mira el número más grande señala el nodo "
                     "equivocado."),
                    ("Abajo", "El DESPUÉS: HashAggregate sobre un Hash Right Join; mascota y "
                     "dueno se leen una vez (loops=1). Cierra con los dos recuadros: LEFT JOIN "
                     "y COUNT(m.id_mascota)."),
                ],
                "ejemplo": "Plan real en el navegador: Aggregate (actual time=2.298..2.300 rows=1 "
                           "loops=2006) y Execution Time: 4909 ms; la reescritura, Execution "
                           "Time: 188 ms.",
                "preguntas": [
                    ("¿Dónde aparece loops?",
                     "Al final del paréntesis de tiempos reales de cada nodo: (actual time=… "
                     "rows=… loops=…). Solo sale con EXPLAIN ANALYZE."),
                ],
                "cuidado": "La versión de la demo cuenta citas, no mascotas: cada vuelta recorre "
                           "las 30.010 citas y la consulta completa tarda minutos en el "
                           "navegador. Avisa antes, o acótala con WHERE d.id_dueno <= 200 "
                           "(loops=200).",
                "puente": "Más rápido no sirve de nada si el resultado cambió: hay que probar que "
                          "es el mismo.",
            },
        },
        "Optimizar no cambia el resultado, y eso": {
            "ideas": [
                "Corrección y tiempo son **independientes**: más rápido devolviendo otra cosa "
                "no es optimizar.",
                "Ningún motor avisa de ese error: la consulta **corre sin fallar** y entrega otra "
                "respuesta.",
                "Con un filtro se prueba con dos **COUNT(*)** en la misma corrida: 91 y 91.",
                "Si la versión nueva da 150, perdió un filtro: es la **respuesta equivocada**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Optimizar es obtener la MISMA respuesta con menos trabajo. Si la "
                           "versión nueva devuelve filas distintas, se rompió la consulta, y se "
                           "rompió sin aviso: ningún motor lanza un error porque una consulta "
                           "devuelva otra cosa. Por eso toda optimización va acompañada de una "
                           "prueba de equivalencia.",
                "pasos": [
                    "La prueba más simple: SELECT COUNT(*) de cada versión, en la misma corrida. "
                    "En la agenda del 2026-03-10 las dos dicen 91: es una optimización.",
                    "El caso equivocado: la versión nueva devuelve 150. Pregunta: «¿qué se "
                    "perdió?». El filtro de estado: 150 son todas las citas del día y 91 solo "
                    "las programadas.",
                    "Lee la regla: corrección y tiempo son ejes independientes.",
                ],
                "ejemplo": "Agenda del 2026-03-10: 150 citas en total, 91 PROGRAMADA, 45 "
                           "ATENDIDA y 14 CANCELADA. Una versión que olvida AND c.estado = "
                           "'PROGRAMADA' devuelve 150.",
                "preguntas": [
                    ("Si los conteos coinciden, ¿ya es la misma respuesta?",
                     "Para una consulta con filtro es una buena prueba; para un conjunto "
                     "completo no basta, porque pueden coincidir en número y ser filas "
                     "distintas. Para eso está EXCEPT en los dos sentidos."),
                ],
                "cuidado": "«Se ve igual» o «trae más o menos lo mismo» no son prueba.",
                "puente": "La prueba fuerte para conjuntos completos: EXCEPT en los dos "
                          "sentidos.",
            },
        },
        "Optimizar no cambia el resultado: como": {
            "ideas": [
                "Con un filtro bastan dos **COUNT(*)** en la misma corrida: los dos deben dar "
                "91.",
                "Para un conjunto completo se usa **EXCEPT** en los dos sentidos y se exige cero "
                "filas.",
                "Un solo sentido no prueba nada: la otra versión puede traer **filas de más**.",
                "La prueba va **sin LIMIT**: las filas que fallan suelen quedar fuera de las "
                "primeras.",
            ],
            "notas": {
                "min": 2,
                "explica": "Hay dos pruebas, según lo que se compare. Para una consulta con "
                           "filtro, contar las filas de cada versión en la misma corrida. Para "
                           "un conjunto completo, como un ranking, se restan los conjuntos con "
                           "EXCEPT en los dos sentidos: lo que está en A y no en B, más lo que "
                           "está en B y no en A. Si salen cero filas, son iguales.",
                "pasos": [
                    ("Al entrar", "Izquierda, prueba 1: dos COUNT(*) en una misma consulta; "
                     "91 = 91."),
                    ("Derecha", "Prueba 2: (ANTES EXCEPT DESPUÉS) UNION ALL (DESPUÉS EXCEPT "
                     "ANTES) devuelve 0 filas. Explica los dos sentidos: A EXCEPT B vacío solo "
                     "dice que todo A está en B; B podría tener filas de más."),
                    ("Abajo", "El contraejemplo real: si la reescritura usa COUNT(*) en vez de "
                     "COUNT(m.id_mascota), la prueba 2 devuelve 12 filas, los 6 dueños sin "
                     "mascotas con 0 de un lado y 1 del otro. Cierra: sin LIMIT y sin «se ve "
                     "igual»."),
                ],
                "ejemplo": "WITH antes AS (…), despues AS (…) SELECT 'sobra en ANTES', * FROM "
                           "(SELECT * FROM antes EXCEPT SELECT * FROM despues) a UNION ALL "
                           "SELECT 'sobra en DESPUES', * FROM (SELECT * FROM despues EXCEPT "
                           "SELECT * FROM antes) b; devuelve 0 filas.",
                "preguntas": [
                    ("¿Y si una versión puede traer filas repetidas?",
                     "EXCEPT elimina duplicados; en ese caso se usa EXCEPT ALL o se incluye la "
                     "clave en el SELECT. En el ranking no pasa: hay una fila por dueño."),
                ],
                "cuidado": "Comparar solo las primeras 20 filas deja fuera justo las que fallan: "
                           "los dueños con 0 quedan al final del ranking.",
                "puente": "Ahora el script de la clase, que junta todo lo visto.",
            },
        },
        "El antes y el despues del script": {
            "ideas": [
                "Antes de medir se proyectan los **conteos de control**: 30.010 citas y 91 "
                "programadas el 2026-03-10.",
                "Con comas, una condición olvidada no da error: produce un **producto "
                "cartesiano**.",
                "**JOIN … ON** no acelera nada, pero convierte un ON olvidado en un error de "
                "sintaxis.",
                "Con ORDER BY y sin índice, un **LIMIT 50** igual lee la tabla y ordena las 91.",
            ],
            "notas": {
                "min": 2,
                "explica": "El script de la demo es autocontenido: crea las tablas, siembra el "
                           "mismo volumen que el estudiante tiene en su pantalla y deja las "
                           "estadísticas listas. Antes de optimizar se proyectan los conteos de "
                           "control; después se corren la agenda ANTES y DESPUÉS, el ranking y "
                           "las pruebas.",
                "pasos": [
                    ("Al entrar", "Arriba a la izquierda, los conteos de control: 30.010 citas; "
                     "el 2026-03-10, 91 PROGRAMADA, 45 ATENDIDA y 14 CANCELADA. Si no salen esos "
                     "números, nada de lo demás cuadra."),
                    ("Arriba a la derecha", "La coma: sin la condición de unión, 30.010 × 5.008 "
                     "≈ 150 millones de filas, y el motor no da ningún error."),
                    ("Abajo", "JOIN … ON da el mismo plan que la coma: no acelera, pero el "
                     "olvido salta a la vista. Y el LIMIT 50: con ORDER BY fecha_hora y sin "
                     "índice, el motor igual lee toda la tabla, encuentra las 91 y las ordena; "
                     "el LIMIT solo ahorra entregar 41."),
                ],
                "ejemplo": "Plan con LIMIT 50: Limit, luego Sort de 91 filas y, al fondo, Seq "
                           "Scan on cita c con Rows Removed by Filter: 29919. El recorrido "
                           "completo sigue ahí.",
                "preguntas": [
                    ("¿Entonces para qué el LIMIT?",
                     "Para no transportar ni pintar filas que la pantalla no usa. Lo que "
                     "evitaría leer toda la tabla es un índice sobre fecha_hora que entregue "
                     "las filas ya ordenadas: Clase 7."),
                ],
                "cuidado": "La siembra recrea las tablas: córrela en una base vacía, nunca sobre "
                           "una base con datos que alguien quiera conservar.",
                "puente": "¿Dónde se corre todo esto, y qué no se puede medir ahí?",
            },
        },
        "Donde se corre todo esto": {
            "ideas": [
                "Todo lo de hoy corre en **PostgreSQL dentro del navegador**, con las 30.010 "
                "citas sembradas.",
                "Ahí se miden planes, filas estimadas y reales, **páginas leídas** y loops.",
                "No se miden la memoria vacía, **varias sesiones** a la vez ni volúmenes mucho "
                "mayores.",
                "Los **conteos** no cambian entre corridas; los milisegundos sí.",
            ],
            "notas": {
                "min": 2,
                "explica": "La herramienta del día es PostgreSQL compilado para ejecutarse dentro "
                           "del navegador. Trae la base con volumen sembrado y soporta EXPLAIN, "
                           "EXPLAIN ANALYZE y BUFFERS. Hay cosas que ahí no se pueden medir, y "
                           "lo correcto es declararlas en vez de inventar un número.",
                "pasos": [
                    ("Al entrar", "Izquierda: lo que se mide y se ve en la salida. Subraya las "
                     "30.010 citas: medir sobre una base de 20 filas no sirve, porque todo cabe "
                     "en una página y cualquier consulta tarda lo mismo."),
                    ("Derecha", "Lo que no se puede medir: tiempos con la memoria vacía "
                     "(vaciarla exige ser administrador), varias sesiones compitiendo (eso es "
                     "la Clase 10) y volúmenes de cientos de miles de filas."),
                    ("Abajo", "La frase final: filas y páginas son estables; los milisegundos "
                     "varían incluso entre dos corridas seguidas."),
                ],
                "ejemplo": "Dos corridas seguidas de la agenda pueden diferir en milisegundos, "
                           "incluso al doble; las dos dirán rows=91 y Rows Removed by Filter: "
                           "29919.",
                "preguntas": [
                    ("¿Puedo medir en mi propia base de la Clase 1?",
                     "Solo si antes le fabricas volumen con generate_series. Con 20 filas el "
                     "plan siempre es Seq Scan y las diferencias son ruido."),
                ],
                "cuidado": "No ofrezcas otra herramienta en línea como alterna: no tiene la base "
                           "sembrada y da otros números.",
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "La agenda del día ANTES y DESPUÉS: las mismas **91 filas**, con su plan.",
                "El ranking de dueños: de un SubPlan con **loops=2006** a una sola pasada.",
                "La **prueba de equivalencia**: 91 = 91, y EXCEPT en los dos sentidos con cero "
                "filas.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo corre el script de la clase y muestra con salidas reales lo "
                           "que se explicó: la agenda optimizada devuelve lo mismo, el ranking "
                           "deja de repetirse por dueño y la equivalencia se prueba con "
                           "consultas.",
                "pasos": [
                    ("Al entrar", "1) Siembra y conteos de control (30.010; 91/45/14). 2) Agenda "
                     "ANTES y DESPUÉS con EXPLAIN (ANALYZE, BUFFERS): el ANTES estima rows=1 y "
                     "entrega 91; el DESPUÉS estima 91. 3) La misma consulta con LIMIT 50: el "
                     "Seq Scan sigue ahí."),
                    ("Después", "4) El ranking: corre primero la versión ANTES acotada a 200 "
                     "dueños (WHERE d.id_dueno <= 200) y muestra loops=200; di que la completa "
                     "es diez veces eso. 5) La reescritura con LEFT JOIN y GROUP BY. 6) Las "
                     "pruebas: 91 = 91, EXCEPT con 0 filas y el contraejemplo COUNT(*) contra "
                     "COUNT(c.id_cita)."),
                ],
                "ejemplo": "En el contraejemplo, los dueños 2001 a 2006 dan 0 con COUNT(c.id_cita) "
                           "y 1 con COUNT(*).",
                "cuidado": "La versión ANTES completa del ranking tarda minutos en el navegador "
                           "(en una prueba, unos tres minutos y medio; la acotada, unos 20 s). "
                           "Avisa antes de correrla: si alguien recarga la página, pierde lo que "
                           "tenía.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 6 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: optimizar es ayudar al optimizador a encontrar un plan mejor "
                           "sin cambiar la respuesta, y demostrarlo con el plan y con un conteo.",
                "pasos": [
                    "Pregunta de salida: «nombren un cambio que acelera y uno que no». Se espera: "
                    "quitar la función de la columna o la subconsulta por fila (acelera); "
                    "cambiar comas por JOIN … ON (no acelera). Anuncia que la Clase 7 crea los "
                    "índices que hoy se echaron de menos.",
                ],
            },
        },
    },
}
