# -*- coding: utf-8 -*-
"""BD II Clase 7 · Indices y particionamiento: ideas proyectadas y GUION de cada lamina.

Formato y uso: `bd2_contenido_data.py` y `notas_guion.py` (se fusiona solo). Planes, tamanos y
mensajes verificados en PGlite (PostgreSQL 18 en Node) sobre la siembra de la clase: 30.010
citas (18.187 PROGRAMADA, 9.095 ATENDIDA, 2.728 CANCELADA), 5.008 mascotas, 2.006 duenos. En
PGlite el acceso por indice suele imprimirse como Bitmap Heap Scan + Bitmap Index Scan on
<indice>; en un servidor puede salir como Index Scan using <indice>: es el mismo acceso.

Los pasos de cada animacion estan en `config/animaciones/bd2/clase7/<huella>.js`.
"""

CONTENIDO = {
    7: {
        "Encuadre de hoy": {
            "notas": {
                "min": 4,
                "explica": "La clase anterior terminó con planes que decían Seq Scan: el motor "
                           "leía la tabla entera porque no tenía otra forma de llegar a las filas. "
                           "Hoy se construye esa otra forma, el índice, se mide cuándo sirve y "
                           "cuánto cuesta, y se ve una herramienta distinta para tablas enormes: "
                           "la partición.",
                "pasos": [
                    "Proyecta mentalmente el plan de la Clase 6 y pregunta: «¿por qué el motor "
                    "leyó las 30.010 citas para encontrar 150?». Deja que respondan: no había "
                    "otra forma de encontrarlas.",
                    ("Después", "Cierra: «hoy esa línea del plan cambia, y lo vamos a demostrar "
                     "con el antes y el después, no con una opinión»."),
                ],
                "puente": "Empecemos por qué es exactamente un índice.",
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
        "De donde viene la clase": {
            "ideas": [
                "Un **índice** es una estructura aparte que guarda una columna ordenada.",
                "Cada entrada tiene el **valor** y un **puntero** a la fila: ctid en PostgreSQL, "
                "ROWID en Oracle.",
                "Es **redundante**: si se borra, ningún dato se pierde y ninguna consulta deja de "
                "funcionar.",
                "El motor lo **mantiene solo** en cada INSERT, UPDATE y DELETE.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un índice es como el índice de un libro: no agrega información, "
                           "repite una columna en orden y dice en qué página está cada valor. El "
                           "motor lo crea a partir de la tabla, lo mantiene sincronizado solo y "
                           "lo usa si le conviene. Si se borra, los datos siguen intactos; solo "
                           "las consultas se vuelven más lentas.",
                "pasos": [
                    "La tabla cita con sus filas en el orden en que llegaron: el 12, el 9, el 15, "
                    "el 10, el 11. Cada fila tiene su dirección física, (0,1), (0,2)…, que en "
                    "PostgreSQL se llama ctid.",
                    "El índice: las fechas ordenadas, cada una con la dirección de su fila. Para "
                    "buscar el 2026-03-10 basta encontrar la entrada y seguir la flecha a (0,4). "
                    "Lee los dos recuadros: valor + puntero; ctid o ROWID.",
                    "Lee la conclusión: auxiliar, redundante y opcional. Subraya «opcional»: "
                    "ninguna consulta falla si el índice no existe.",
                ],
                "ejemplo": "En la base de hoy, el índice sobre cita(fecha_hora) mide 256 kB "
                           "frente a los 2 MB de la tabla: PostgreSQL deduplica las claves "
                           "repetidas y fecha_hora tiene solo 1.810 valores distintos. Se mide con "
                           "SELECT pg_size_pretty(pg_relation_size('idx_cita_fecha_hora'));",
                "preguntas": [
                    ("Si es redundante, ¿por qué no se crean índices para todo?",
                     "Porque cada índice se actualiza en cada escritura y ocupa espacio. Se "
                     "crea el que una consulta frecuente necesita; lo vemos en dos láminas."),
                    ("¿Puedo ver el ctid?",
                     "Sí: SELECT ctid, id_cita FROM cita LIMIT 5; muestra la dirección física "
                     "de cada fila. Cambia si la fila se actualiza, así que no sirve como "
                     "identificador."),
                ],
                "cuidado": "No digas que el índice «ordena la tabla»: la tabla queda igual; el "
                           "índice es una estructura aparte.",
                "puente": "¿Cómo encuentra el motor una clave dentro del índice sin leerlo "
                          "entero? Con un árbol.",
            },
        },
        "El B-Tree por dentro": {
            "ideas": [
                "El **B-Tree** tiene raíz, ramas y hojas; todas las hojas a la misma profundidad.",
                "Cada nodo es una **página** de 8 KB con cientos de claves.",
                "Buscar un valor cuesta **una lectura por nivel**: tres o cuatro alcanzan para "
                "millones de filas.",
                "Las hojas están **enlazadas**: sirven para rangos y para entregar filas ya "
                "ordenadas.",
            ],
            "notas": {
                "min": 3,
                "explica": "El índice por omisión en PostgreSQL, Oracle, MySQL y SQL Server es "
                           "el B-Tree, un árbol balanceado. Cada nodo ocupa una página y guarda "
                           "cientos de claves, así que el árbol es muy ancho y muy bajo. Encontrar "
                           "una clave es bajar de la raíz a una hoja: una lectura por nivel. "
                           "Duplicar la tabla casi no cambia ese número.",
                "pasos": [
                    "El árbol: raíz (50), ramas (30 y 70) y hojas con todas las claves y sus "
                    "punteros. Balanceado: todas las hojas a la misma profundidad, así que "
                    "ninguna búsqueda tiene suerte ni mala suerte.",
                    "Buscar 60: la raíz dice «mayor que 50, a la derecha»; la rama dice «menor "
                    "que 70»; la hoja 55·60 lo tiene. Tres lecturas, una por nivel.",
                    "Cada nodo es una página de 8 KB. Con entradas de unos 20 bytes caben del "
                    "orden de 400 claves: dos niveles cubren 160.000 filas, tres, 64 millones.",
                ],
                "ejemplo": "El índice de hoy sobre cita(fecha_hora) tiene 32 páginas en total: "
                           "una raíz y unas 31 hojas, o sea dos niveles. Encontrar una fecha "
                           "cuesta dos lecturas de índice.",
                "preguntas": [
                    ("¿Por qué sirve para BETWEEN o para ORDER BY?",
                     "Porque las hojas están enlazadas en orden: al llegar a la primera clave "
                     "del rango, el motor sigue avanzando por las hojas sin volver a la raíz."),
                    ("¿Hay otros tipos de índice?",
                     "Sí (hash, GIN, GiST, BRIN), pero el B-Tree es el que se usa salvo que se "
                     "pida otro, y es el de hoy."),
                ],
                "cuidado": "No confundas «B-Tree» con «árbol binario»: cada nodo tiene cientos "
                           "de hijos, no dos; por eso el árbol es tan bajo.",
                "puente": "Leer es más rápido; escribir, no. El precio se paga en cada escritura.",
            },
        },
        "El precio se paga en cada escritura": {
            "ideas": [
                "Un **INSERT** en una tabla con cuatro índices son cinco escrituras: la fila y "
                "una por índice.",
                "Un **UPDATE** solo toca los índices que contienen alguna columna modificada.",
                "Cada índice ocupa **espacio**: la suma de los índices puede superar a la tabla.",
                "Regla de descarte: si no hay una **consulta** que lo use, el índice sobra.",
            ],
            "notas": {
                "min": 3,
                "explica": "El índice acelera lecturas, pero se mantiene en cada escritura: cada "
                           "INSERT agrega una entrada ordenada en cada índice de la tabla, y cada "
                           "DELETE la quita. Por eso indexar tiene un costo que se paga siempre, "
                           "se use o no se use el índice.",
                "pasos": [
                    "INSERT INTO cita: la fila va a la tabla y además a cada uno de los cuatro "
                    "índices. Lee la frase: un INSERT con cuatro índices no es una operación, son "
                    "cinco.",
                    "Cuánto pesa, medido en el navegador: copiar las 30.010 citas a una tabla "
                    "sin índices tardó unos 250 ms; a una con cuatro índices, unos 1.230 ms. Di "
                    "que el número exacto cambia por motor y por carga, pero la dirección "
                    "nunca. Cierra con la regla: se indexa lo que se consulta.",
                ],
                "ejemplo": "Cambiar cita.estado de PROGRAMADA a ATENDIDA actualiza "
                           "idx_cita_estado_fecha, que contiene estado, pero no "
                           "idx_cita_fecha_hora. Ojo: el índice parcial de las PROGRAMADA sí se "
                           "toca, porque la fila sale de él.",
                "preguntas": [
                    ("¿Cuántos índices son demasiados?",
                     "Como guía de oficio, dos a cuatro por tabla muy escrita además de la clave "
                     "primaria, cada uno con su consulta escrita al lado."),
                ],
                "cuidado": "No prometas porcentajes exactos («cada índice cuesta un 10 %»): "
                           "depende del motor y de la carga; lo honesto es medirlo.",
                "puente": "¿Cómo se sabe qué índices existen, cuánto pesan y si alguien los usa?",
            },
        },
        "El costo de sobre-indexar": {
            "notas": {
                "min": 2,
                "explica": "PostgreSQL lleva la cuenta de cuántas veces se usó cada índice. Con "
                           "esa cuenta y el tamaño se detecta el índice que se paga en cada "
                           "escritura y no le sirve a nadie.",
                "pasos": [
                    ("Al entrar", "Líneas 1-2: el recordatorio del precio. Seis índices sobre "
                     "cita son seis escrituras extra por cada cita agendada."),
                    ("Líneas 4-9", "La consulta a pg_stat_user_indexes: nombre del índice, "
                     "idx_scan (cuántas veces se usó) y su tamaño, ordenados del menos usado al "
                     "más usado."),
                    ("Líneas 11-12", "La lectura: idx_scan = 0 después de días de uso real "
                     "significa que ninguna consulta lo necesita. Candidato a DROP INDEX."),
                ],
                "ejemplo": "En la base de hoy, idx_cita_fecha_hora mide 256 kB y "
                           "idx_cita_estado_fecha 368 kB; la tabla cita, 2 MB. Con los cinco "
                           "índices de la clase, los índices de cita ya suman más que la mitad "
                           "de la tabla.",
                "preguntas": [
                    ("¿Por qué en el navegador idx_scan sale en 0 aunque acabo de usar el "
                     "índice?",
                     "Porque las estadísticas de uso se vuelcan con retraso y en una sesión "
                     "corta casi no se acumulan. Esta consulta tiene sentido en un servidor con "
                     "días de tráfico."),
                ],
                "cuidado": "No borres un índice por idx_scan = 0 en una base recién creada: "
                           "solo dice algo después de un período de uso real.",
                "puente": "Ahora el índice de varias columnas y su regla, la fuente de error más "
                          "frecuente del tema.",
            },
        },
        "Indice compuesto: la regla del prefijo": {
            "ideas": [
                "Un índice **compuesto** se ordena por la primera columna y, dentro de ella, por "
                "la segunda.",
                "Sirve si el filtro empieza por la **columna líder**: estado, o estado y "
                "fecha_hora.",
                "Solo por fecha_hora **no hay búsqueda directa**: es buscar «Ana» en un "
                "directorio por apellido.",
                "Diseño: la columna de **igualdad** primero, la de **rango** al final.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un índice compuesto sobre (estado, fecha_hora) se ordena como un "
                           "directorio telefónico por apellido y luego por nombre: primero todas "
                           "las ATENDIDA en orden de fecha, después las CANCELADA, después las "
                           "PROGRAMADA. Por eso sirve para buscar por estado, o por estado y "
                           "fecha; pero no para buscar solo por fecha, igual que en el "
                           "directorio no se encuentran todas las Ana sin leerlo entero.",
                "pasos": [
                    "El índice idx_cita_estado_fecha: primero agrupado por estado y, dentro de "
                    "cada estado, ordenado por fecha. Señala los corchetes de la derecha.",
                    "Las dos consultas que empiezan por la columna líder: estado = 'PROGRAMADA' "
                    "con un rango de fecha (resaltada la fila PROGRAMADA · 03-10) y estado = "
                    "'PROGRAMADA' a secas. Las dos sirven.",
                    "La tercera filtra solo por fecha_hora: no hay búsqueda directa. Lee la nota: "
                    "PostgreSQL 18 puede usar el índice «saltando» una vez por cada estado (skip "
                    "scan), pero es un recurso del motor, no un diseño. Lee la regla.",
                ],
                "ejemplo": "Sin un índice que empiece por fecha_hora, una consulta solo por fecha "
                           "usó idx_cita_estado_fecha con Index Searches: 7 en lugar de 1: siete "
                           "búsquedas en el árbol, una por cada salto entre estados.",
                "preguntas": [
                    ("Un índice de tres columnas, ¿sirve para cualquier combinación?",
                     "No: atiende sus prefijos (la primera; la primera y la segunda; las tres). "
                     "Tres formas de consulta, no seis."),
                    ("Entonces, ¿el skip scan hace innecesaria la regla?",
                     "No. Solo sale barato cuando la columna líder tiene muy pocos valores, y "
                     "existe desde PostgreSQL 18; en versiones anteriores ese filtro termina en "
                     "Seq Scan."),
                ],
                "cuidado": "Decir que un índice compuesto sirve para cualquier combinación de sus "
                           "columnas es el error más caro de la clase: el estudiante crea "
                           "(estado, fecha_hora) y cree cubierta una consulta que solo filtra por "
                           "fecha.",
                "puente": "A veces el índice basta para responder sin tocar la tabla.",
            },
        },
        "Cuando el indice responde solo": {
            "ideas": [
                "Si todas las columnas que pide la consulta están en el índice, hay **Index Only "
                "Scan**.",
                "Ahí el motor **no toca la tabla**: lee solo hojas del índice.",
                "Si se pide una columna que no está, vuelve a la tabla **por cada fila**.",
                "**INCLUDE** guarda esa columna en las hojas sin usarla para ordenar.",
            ],
            "notas": {
                "min": 3,
                "explica": "El acceso por índice normal tiene dos partes: buscar en el índice y "
                           "luego ir a la tabla por cada fila encontrada. Si la consulta solo "
                           "pide columnas que el índice ya tiene, la segunda parte sobra y el "
                           "plan dice Index Only Scan. Es la forma más barata de leer.",
                "pasos": [
                    "SELECT estado, fecha_hora con filtro por estado y fecha: todo está en "
                    "idx_cita_estado_fecha. El plan real: Index Only Scan using "
                    "idx_cita_estado_fecha, Heap Fetches: 0, 13.187 filas.",
                    "Se agrega id_mascota al SELECT: ya no está en el índice. El plan pasa a "
                    "Bitmap Heap Scan: va a la tabla a buscar cada fila.",
                    "La salida: CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora) "
                    "INCLUDE (id_mascota). El plan vuelve a Index Only Scan, ahora usando "
                    "idx_cita_cubridor.",
                ],
                "ejemplo": "Con INCLUDE, las 13.187 filas salen con Heap Fetches: 0: ninguna "
                           "lectura de la tabla. Oracle no tiene INCLUDE; ahí la columna se "
                           "agrega al final de la clave.",
                "preguntas": [
                    ("Creé el índice y el plan dice Index Scan, no Index Only Scan. ¿Está mal?",
                     "No necesariamente. En PostgreSQL el Index Only Scan necesita el mapa de "
                     "visibilidad al día: justo después de una carga sale Index Scan hasta que "
                     "corre VACUUM. En la prueba, antes del VACUUM salió Bitmap Heap Scan; "
                     "después, Index Only Scan."),
                ],
                "cuidado": "Esto es un adelanto útil, no algo para exigir: si alguien ve Index "
                           "Only Scan en su plan, que sepa qué significa.",
                "puente": "¿Y si el índice existe y el plan no lo usa? Hay siete razones.",
            },
        },
        "Las siete razones": {
            "ideas": [
                "Si la tabla es **pequeña**, leerla entera gana: dueno ocupa 20 páginas.",
                "Una **función** sobre la columna, o un filtro que deja pasar casi todo, "
                "anulan el índice.",
                "Sin **ANALYZE**, el motor decide con estadísticas viejas.",
                "También lo anulan la **columna líder** ausente, un OR entre columnas o tipos "
                "que no coinciden.",
            ],
            "notas": {
                "min": 2,
                "explica": "Que un índice exista no obliga al motor a usarlo: lo usa si le sale "
                           "más barato. Hay siete razones típicas por las que no le sale, y "
                           "conocerlas permite responder «¿por qué no usa mi índice?» sin decir "
                           "que el motor es raro.",
                "pasos": [
                    ("Al entrar", "Recorre la lista de arriba abajo. 1 tabla pequeña (dueno, 20 "
                     "páginas); 2 función sobre la columna; 3 selectividad mala (activa = 'S' "
                     "deja pasar el 94 % de mascota); 4 estadísticas viejas, resaltada porque "
                     "es la más frecuente."),
                    ("Luego", "5 falta la columna líder; 6 un OR entre columnas de índices "
                     "distintos; 7 el valor comparado no es del tipo de la columna."),
                    ("Abajo", "El orden de revisión cuando algo no cambia: primero ANALYZE, "
                     "después la columna líder, después si el predicado es sargable."),
                ],
                "ejemplo": "SELECT * FROM mascota WHERE activa = 'S'; sale con Seq Scan aunque "
                           "hubiera índice sobre activa: devuelve 4.712 de 5.008 filas.",
                "preguntas": [
                    ("Con mis 20 filas de la Clase 1 el plan nunca usa el índice. ¿Lo hice "
                     "mal?",
                     "No: con 20 filas todo cabe en una página y leerla es lo más barato. El "
                     "motor tiene razón. Por eso hoy se mide sobre 30.010 citas."),
                ],
                "cuidado": "No respondas «el motor es impredecible»: casi siempre es una de "
                           "estas siete, y la primera que hay que revisar es el ANALYZE.",
                "puente": "Los cinco índices de hoy, cada uno con la consulta que lo justifica.",
            },
        },
        "Los cinco indices, y la consulta": {
            "ideas": [
                "Tres índices para **medir**: fecha_hora, el dueño de la mascota y la agenda de "
                "las PROGRAMADA.",
                "Dos **compuestos** con las mismas columnas en orden inverso, para el "
                "experimento.",
                "La **clave primaria** ya trae su índice: crear otro encima solo duplica.",
                "Una **clave foránea** no crea índice: por eso idx_mascota_dueno sí suma.",
            ],
            "notas": {
                "min": 2,
                "explica": "Cada índice de la clase existe porque una consulta concreta lo "
                           "necesita. Tres sirven para la medición del antes y el después; dos "
                           "existen a propósito para demostrar que el orden de las columnas "
                           "importa.",
                "pasos": [
                    ("Al entrar", "Los tres de la medición: idx_cita_fecha_hora (cualquier "
                     "rango de fechas), idx_mascota_dueno (las mascotas de un dueño) e "
                     "idx_cita_programada_fecha, parcial, para la agenda de recepción. A la "
                     "derecha, su tamaño real."),
                    ("Abajo", "Los dos del experimento: idx_cita_estado_fecha e "
                     "idx_cita_fecha_estado, las mismas columnas al revés. Cierra con la línea "
                     "final: PK sí trae índice, FK no."),
                ],
                "ejemplo": "SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = "
                           "1234; devuelve 2 filas. Sin índice es Seq Scan sobre las 5.008 "
                           "mascotas; con idx_mascota_dueno, Bitmap Index Scan on "
                           "idx_mascota_dueno.",
                "preguntas": [
                    ("¿Por qué el índice sobre la FK ayuda también al borrar un dueño?",
                     "Porque al borrar el dueño el motor tiene que verificar que ninguna "
                     "mascota lo referencia; sin índice en mascota.id_dueno recorre la tabla "
                     "entera."),
                ],
                "cuidado": "El nombre se escribe exacto: idx_cita_fecha_hora, no "
                           "idx_cita_fecha. No lo dictes de memoria: cópialo de la lámina.",
                "puente": "Así se ve en código un índice justificado por su consulta.",
            },
        },
        "Un indice se justifica con la consulta": {
            "notas": {
                "min": 2,
                "explica": "Un índice se justifica escribiendo al lado la consulta frecuente que "
                           "lo usa. Aquí, la agenda del día: siempre filtra por fecha y por "
                           "estado PROGRAMADA.",
                "pasos": [
                    ("Al entrar", "Líneas 1-4: la consulta frecuente, la agenda del 2026-03-10 "
                     "en estado PROGRAMADA: 91 filas."),
                    ("Líneas 6-8", "Los dos índices que la atienden: el completo sobre "
                     "fecha_hora y el parcial, que solo contiene las PROGRAMADA."),
                    ("Líneas 10-11", "El mal candidato, comentado a propósito: activa solo toma "
                     "'S' o 'N' y deja pasar casi todas las filas; un índice ahí no ayuda."),
                ],
                "ejemplo": "Con los dos índices creados y ANALYZE, el plan de esa consulta es "
                           "Bitmap Heap Scan on cita con Bitmap Index Scan on "
                           "idx_cita_programada_fecha debajo: gana el parcial, y salen las 91 "
                           "filas.",
                "cuidado": "Lee la leyenda de abajo: el nombre es el que aparece en el plan. En "
                           "el navegador suele salir como «Bitmap Index Scan on <nombre>».",
                "puente": "Para demostrar que un índice sirve hay una secuencia que no se puede "
                          "alterar.",
            },
        },
        "La secuencia de medicion": {
            "ideas": [
                "Primero **EXPLAIN ANALYZE** sin índices: el Seq Scan es la línea base.",
                "Después el **CREATE INDEX**, con el nombre exacto.",
                "Después **ANALYZE**: crear el índice no actualiza las estadísticas.",
                "Al final la **misma consulta**, sin cambiar una coma.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un índice se demuestra con un antes y un después de la misma "
                           "consulta. Son cuatro pasos y en este orden: si se cambia el orden o "
                           "la consulta, la comparación deja de valer.",
                "pasos": [
                    "Paso 1: EXPLAIN ANALYZE antes de crear nada. Tiene que salir Seq Scan on "
                    "cita: ese es el punto de comparación.",
                    "Paso 2: los CREATE INDEX, con el nombre exacto, porque ese nombre es el que "
                    "imprimirá el plan.",
                    "Paso 3, resaltado: ANALYZE cita; ANALYZE mascota;. Es el paso que se salta "
                    "medio salón; con estadísticas viejas el planeador puede ignorar un índice "
                    "perfectamente bueno.",
                    "Paso 4: la misma consulta otra vez. Si se cambia una fecha o un id, ya no "
                    "es la misma medición. Lee la frase final.",
                ],
                "ejemplo": "Agenda del 2026-03-10: antes, Seq Scan on cita con Rows Removed by "
                           "Filter: 29919; después, Bitmap Heap Scan on cita con Bitmap Index "
                           "Scan on idx_cita_programada_fecha debajo. Las 91 filas, iguales.",
                "preguntas": [
                    ("¿Cómo compruebo qué índices existen?",
                     "SELECT indexname, tablename, indexdef FROM pg_indexes WHERE tablename IN "
                     "('cita','mascota') ORDER BY tablename, indexname; indexdef muestra el "
                     "CREATE INDEX completo, con el WHERE del parcial."),
                ],
                "cuidado": "Cuando alguien diga «creé el índice y no sirvió», lo primero que se "
                           "pregunta es si corrió el ANALYZE.",
                "puente": "La secuencia en código, con su salida real.",
            },
        },
        "Crear el indice y probar que se usa": {
            "notas": {
                "min": 2,
                "explica": "La secuencia completa sobre la agenda de un día: crear los índices, "
                           "actualizar estadísticas y volver a medir la misma consulta.",
                "pasos": [
                    ("Al entrar", "Líneas 1-4: los dos índices de una columna y los ANALYZE de "
                     "las dos tablas."),
                    ("Líneas 6-9", "La consulta: todas las citas del 2026-03-10 con rango "
                     "semiabierto. Es la misma que se midió antes de crear nada."),
                    ("Líneas 11-13", "La salida real. Antes: Seq Scan on cita, 150 filas y "
                     "29.860 descartadas. Después: Bitmap Heap Scan on cita con Bitmap Index "
                     "Scan on idx_cita_fecha_hora. El nombre del índice aparece en el plan."),
                ],
                "ejemplo": "En una corrida en el navegador la misma consulta pasó de unos 22 ms "
                           "a unos 8 ms. Lo que se afirma con seguridad es el cambio de nodo; los "
                           "milisegundos varían.",
                "preguntas": [
                    ("¿Por qué Bitmap y no Index Scan?",
                     "Es otra forma de usar el mismo índice: primero marca todas las filas que "
                     "cumplen y luego visita la tabla en orden físico. El planeador la elige "
                     "cuando salen decenas o cientos de filas."),
                ],
                "cuidado": "Si el plan no cambia, revisa en este orden: el ANALYZE, que la "
                           "consulta sea exactamente la misma y que el filtro sea sargable.",
                "puente": "Con dos índices compuestos se demuestra la regla del prefijo.",
            },
        },
        "El experimento del orden de columnas": {
            "ideas": [
                "Se crean **(estado, fecha_hora)** y **(fecha_hora, estado)**, se corre ANALYZE "
                "y se miden tres consultas.",
                "Estado más rango de fecha: le sirve más el que empieza por **estado**.",
                "Solo el rango de fecha: le sirve el que empieza por **fecha_hora**.",
                "Solo estado: el que empieza por fecha **no sirve**.",
            ],
            "notas": {
                "min": 3,
                "explica": "La regla del prefijo no se cree: se demuestra. Se crean dos índices "
                           "con las mismas columnas en orden inverso y se miran tres consultas, "
                           "cada una con un filtro distinto. El plan dice cuál índice le sirve a "
                           "cuál.",
                "pasos": [
                    "Q1, estado por igualdad y fecha por rango: idx_cita_estado_fecha le sirve "
                    "plenamente; idx_cita_fecha_estado, menos.",
                    "Q2, solo rango de fecha: ahora es al revés, sirve el que empieza por "
                    "fecha_hora.",
                    "Q3, solo estado: idx_cita_estado_fecha sirve; el que empieza por fecha no "
                    "le sirve, porque su columna líder no aparece en el filtro.",
                    "La regla y el procedimiento: igualdad primero, rango al final; ANALYZE "
                    "entre medición y medición, y DROP INDEX del que sobra al terminar.",
                ],
                "ejemplo": "En la demo, con los tres índices de la medición todavía creados, "
                           "el motor del navegador eligió el parcial idx_cita_programada_fecha para Q1, "
                           "idx_cita_fecha_hora para Q2 e idx_cita_estado_fecha para Q3. Con solo "
                           "los dos compuestos, Q1 fue a idx_cita_estado_fecha y Q2 a "
                           "idx_cita_fecha_estado.",
                "preguntas": [
                    ("¿Entonces creo los dos compuestos y listo?",
                     "Hoy se crean los dos para medir; en producción rara vez se justifica "
                     "tener ambos. Crear para medir y crear para dejar son cosas distintas."),
                    ("Mi plan eligió otro índice. ¿Me equivoqué?",
                     "No necesariamente: el planeador decide por costo entre índices que "
                     "compiten de cerca. Se reporta lo que se vio y se explica."),
                ],
                "cuidado": "Si el plan del grupo no coincide con la lámina, no lo corrijas hacia "
                           "la lámina: un plan distinto bien leído vale más que el esperado "
                           "copiado.",
                "puente": "La misma regla sobre otro par de columnas, en código.",
            },
        },
        "El orden de columnas en un indice compuesto": {
            "notas": {
                "min": 2,
                "explica": "La agenda de un veterinario usa igualdad en id_veterinario y rango u "
                           "orden en fecha_hora. Por eso el índice va en ese orden: primero la "
                           "igualdad, después el rango.",
                "pasos": [
                    ("Al entrar", "Líneas 1-3: el índice (id_veterinario, fecha_hora) y su "
                     "ANALYZE."),
                    ("Líneas 5-9", "Veterinario 5 el 2026-03-10: el Index Cond usa las DOS "
                     "columnas y una sola búsqueda en el árbol (Index Searches: 1). Salen 50 "
                     "citas."),
                    ("Líneas 11-13", "El mismo veterinario ordenado por fecha con LIMIT 10: "
                     "Index Scan using idx_cita_vet_fecha y ningún Sort, porque las hojas ya "
                     "están en ese orden."),
                    ("Líneas 15-16", "Sin la columna líder no hay búsqueda directa. En la prueba, "
                     "sin otro índice disponible, PostgreSQL 18 lo usó saltando por cada "
                     "veterinario: Index Searches: 13."),
                ],
                "ejemplo": "Veterinarios con citas el 2026-03-10 en la base sembrada: el 1, el 5 "
                           "y el 9, con 50 citas cada uno.",
                "preguntas": [
                    ("¿Qué es Index Searches?",
                     "Cuántas veces el motor bajó por el árbol. Una búsqueda directa da 1; un "
                     "skip scan da una por cada valor de la columna líder que salta."),
                ],
                "cuidado": "El skip scan existe desde PostgreSQL 18; si el motor de alguien es "
                           "más viejo, el filtro solo por fecha termina en Seq Scan. La regla de "
                           "diseño es la misma en las dos versiones.",
                "puente": "Los nombres exactos, y dónde se leen.",
            },
        },
        "Los cinco indices de hoy": {
            "ideas": [
                "El plan imprime el **nombre del índice** junto al nodo que lo usa.",
                "En el navegador suele verse como **Bitmap Index Scan on** seguido del nombre.",
                "**pg_indexes** trae el CREATE INDEX completo, con el WHERE del parcial.",
                "El sufijo es el de la columna: **idx_cita_fecha_hora**, no idx_cita_fecha.",
            ],
            "notas": {
                "min": 2,
                "explica": "El nombre de un índice no es decorativo: es lo que el plan imprime "
                           "cuando lo usa y lo que se escribe en cualquier documento que lo "
                           "justifique. Por eso se lee de la salida, no de la memoria.",
                "pasos": [
                    ("Al entrar", "Arriba, el plan real de la agenda: Bitmap Heap Scan on cita "
                     "(rows=91) y, debajo, Bitmap Index Scan on idx_cita_programada_fecha, "
                     "resaltado. En un servidor también puede salir como «Index Scan using "
                     "<nombre>»: es el mismo acceso por índice."),
                    ("En el medio", "pg_indexes: su columna indexdef devuelve el CREATE INDEX "
                     "completo. En el parcial termina en WHERE (estado = "
                     "'PROGRAMADA'::text): esa es la prueba de que se creó parcial."),
                    ("Abajo", "El nombre que no es: idx_cita_fecha está tachado; el bueno es "
                     "idx_cita_fecha_hora, con el sufijo de la columna."),
                ],
                "ejemplo": "La consulta a pg_indexes sobre cita y mascota devuelve 7 filas: los "
                           "5 índices de hoy más cita_pkey y mascota_pkey, que creó la clave "
                           "primaria.",
                "cuidado": "Es el error que más cuesta y no es conceptual: un nombre mal "
                           "copiado de la pizarra. Deja los cinco nombres proyectados mientras "
                           "el grupo trabaja.",
                "puente": "Uno de los cinco es especial: el índice parcial.",
            },
        },
        "El indice parcial: que indexa": {
            "ideas": [
                "Un índice **parcial** solo contiene las filas que cumplen una condición.",
                "Su **WHERE** es parte de la definición del índice, no de la consulta.",
                "De 30.010 citas, solo **18.187** están programadas: cuatro de cada diez "
                "entradas menos.",
                "Se usa solo si la consulta trae **la misma condición**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Un índice parcial indexa solo una parte de la tabla: la que cumple "
                           "el WHERE de su definición. Si la pantalla de recepción siempre busca "
                           "citas PROGRAMADA, no tiene sentido indexar las atendidas ni las "
                           "canceladas.",
                "pasos": [
                    "CREATE INDEX idx_cita_programada_fecha ON cita (fecha_hora) WHERE estado = "
                    "'PROGRAMADA'. Lee el recuadro: ese WHERE no filtra una consulta, decide "
                    "qué filas entran al índice.",
                    "Las barras: el índice completo indexa 30.010 entradas; el parcial, 18.187, "
                    "el 61 %. Cuatro de cada diez entradas menos.",
                    "El beneficio: menos disco, menos memoria y menos trabajo en las escrituras "
                    "de citas que no están programadas. Y la condición para usarlo: que la "
                    "consulta diga estado = 'PROGRAMADA'.",
                ],
                "ejemplo": "En bytes: el parcial mide 168 kB y el completo 256 kB.",
                "preguntas": [
                    ("Si la consulta pide estado IN ('PROGRAMADA', 'ATENDIDA'), ¿lo usa?",
                     "No: el índice no tiene las atendidas, y el motor no puede arriesgarse a "
                     "devolver un resultado incompleto."),
                ],
                "cuidado": "El error típico es leer el WHERE del CREATE INDEX como si fuera el "
                           "filtro de una consulta.",
                "puente": "¿Y cuál gana cuando el completo y el parcial compiten por la misma "
                          "consulta?",
            },
        },
        "El indice parcial: el mismo beneficio": {
            "ideas": [
                "En la agenda del día el completo encuentra **150** entradas y descarta 59 en la "
                "tabla.",
                "El parcial encuentra las **91** que sirven: ya sabe que están programadas.",
                "El plan nombra al ganador: **Bitmap Index Scan on idx_cita_programada_fecha**.",
                "Sin el filtro de estado, el parcial **no se puede usar**.",
            ],
            "notas": {
                "min": 2,
                "explica": "Con el índice completo y el parcial creados, la agenda del día tiene "
                           "dos caminos. El completo encuentra todas las citas del día y luego "
                           "debe descartar las que no están programadas; el parcial solo tiene "
                           "programadas y va directo a las 91.",
                "pasos": [
                    ("Al entrar", "Izquierda, idx_cita_fecha_hora: 150 entradas encontradas y 59 "
                     "descartadas después de ir a la tabla a leer el estado. Derecha, "
                     "idx_cita_programada_fecha: 91 entradas, todas útiles, y un índice más "
                     "chico."),
                    ("En el medio", "El plan real: Bitmap Index Scan on idx_cita_programada_fecha "
                     "(rows=91). Si en otra corrida gana el completo, se reporta lo que salió: "
                     "con este volumen la diferencia de costo es pequeña."),
                    ("Abajo", "La condición: la consulta tiene que traer el mismo filtro de "
                     "estado."),
                ],
                "ejemplo": "SELECT id_cita, fecha_hora, estado FROM cita WHERE fecha_hora >= "
                           "TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP "
                           "'2026-03-11 00:00:00' AND estado = 'PROGRAMADA'; devuelve 91 filas "
                           "usando el parcial.",
                "preguntas": [
                    ("¿Tener el completo y el parcial sobre la misma columna es redundante?",
                     "No mientras haya consultas sin el filtro de estado: esas solo pueden usar "
                     "el completo. Si todas filtraran por PROGRAMADA, el completo sobraría."),
                ],
                "cuidado": "No fuerces la respuesta «gana el parcial»: lo que se exige es leer el "
                           "plan y escribir cuál salió.",
                "puente": "Cambiamos de herramienta: partir una tabla en pedazos.",
            },
        },
        "Particionar: que es": {
            "ideas": [
                "**Particionar** es dividir una tabla lógica en tablas físicas por una clave.",
                "Lo más común es **por rango de fechas**: una partición por año.",
                "Una consulta de 2026 lee solo la partición de 2026: eso es la **poda**.",
                "El **índice** ordena; la **partición** separa.",
            ],
            "notas": {
                "min": 3,
                "explica": "Particionar es partir una tabla en varias tablas físicas, llamadas "
                           "particiones, según una clave como la fecha. Para quien consulta "
                           "sigue siendo una sola tabla; el motor, al ver el filtro, descarta de "
                           "entrada las particiones que no pueden tener lo buscado.",
                "pasos": [
                    "Una sola tabla lógica, cita_hist, partida en dos particiones por año: "
                    "cita_hist_2025 y cita_hist_2026, cada una con su rango.",
                    "Una consulta de 2026: el motor descarta cita_hist_2025 sin leerla (queda "
                    "atenuada) y el plan solo nombra cita_hist_2026. Eso es la poda de "
                    "particiones.",
                    "La frase para recordar: el índice ordena, la partición separa.",
                ],
                "ejemplo": "SELECT COUNT(*) FROM cita_hist WHERE fecha_hora >= TIMESTAMP "
                           "'2026-01-01'; produce un plan con Seq Scan on cita_hist_2026 y "
                           "ninguna mención de cita_hist_2025.",
                "preguntas": [
                    ("¿Cuándo vale la pena particionar?",
                     "Como convención de oficio, por encima de decenas de millones de filas o "
                     "decenas de gigabytes. Por debajo, un índice sobre fecha_hora hace lo mismo "
                     "con menos mantenimiento."),
                ],
                "cuidado": "No digas que hoy es solo teoría: hoy se implementa completo (DDL, "
                           "migración, prueba de reparto y de poda). Lo que no se aprecia con este "
                           "volumen es la ganancia de rendimiento.",
                "puente": "El DDL que la crea, con sus dos trampas.",
            },
        },
        "Particionar el historico": {
            "notas": {
                "min": 2,
                "explica": "Tres sentencias: la tabla particionada, que no guarda filas, y una "
                           "partición por año, que sí las guarda.",
                "pasos": [
                    ("Al entrar", "Líneas 1-8: la tabla cita_hist con PARTITION BY RANGE "
                     "(fecha_hora). Subraya la línea 7: la clave primaria incluye fecha_hora, "
                     "que es la clave de partición; sin eso el motor rechaza la tabla."),
                    ("Líneas 10-13", "Las dos particiones con FOR VALUES FROM … TO …: 2025 y "
                     "2026."),
                    ("Línea 15", "El rango: FROM incluye, TO excluye. El TO de 2025 es el FROM "
                     "de 2026, así que no hay huecos ni solapes."),
                ],
                "ejemplo": "Después del DDL, INSERT INTO cita_hist SELECT id_cita, id_mascota, "
                           "id_veterinario, fecha_hora, estado FROM cita; mueve las 30.010 citas. "
                           "Como todas son de 2026, todas caen en cita_hist_2026.",
                "preguntas": [
                    ("¿Por qué la PK tiene que incluir la fecha?",
                     "Porque PostgreSQL garantiza la unicidad dentro de cada partición; para "
                     "garantizarla en toda la tabla, la clave tiene que contener la columna que "
                     "decide la partición."),
                ],
                "cuidado": "Con PRIMARY KEY (id_cita) a secas el motor responde «unique "
                           "constraint on partitioned table must include all partitioning "
                           "columns»: tradúcelo en voz alta cuando aparezca.",
                "puente": "¿Cómo se prueba que el reparto y la poda ocurrieron?",
            },
        },
        "El DDL de la particion": {
            "ideas": [
                "Tres sentencias: la tabla **PARTITION BY RANGE** y una partición por año.",
                "La **clave primaria** tiene que incluir la columna de partición: (id_cita, "
                "fecha_hora).",
                "El **rango** incluye el FROM y excluye el TO: el TO de una es el FROM de la "
                "siguiente.",
                "Un hueco en los rangos hace fallar el **INSERT** de esas fechas.",
            ],
            "notas": {
                "min": 3,
                "explica": "El DDL de una tabla particionada tiene dos trampas que dan error de "
                           "una vez o, peor, más tarde. La primera es la clave primaria; la "
                           "segunda, los límites de los rangos.",
                "pasos": [
                    "Las tres sentencias: CREATE TABLE cita_hist ( …, PRIMARY KEY (id_cita, "
                    "fecha_hora)) PARTITION BY RANGE (fecha_hora) y las dos particiones.",
                    "Trampa 1: la PK debe incluir fecha_hora. Con PRIMARY KEY (id_cita) a secas, "
                    "el motor responde «unique constraint on partitioned table must include all "
                    "partitioning columns».",
                    "Trampa 2: FROM incluye y TO excluye. Si alguien escribe TO (TIMESTAMP "
                    "'2025-12-31'), las citas del 31 de diciembre no tienen partición y el "
                    "INSERT falla con «no partition of relation … found for row».",
                ],
                "ejemplo": "Prueba real: con la partición de 2025 cerrada en '2025-12-31', una "
                           "cita del 2025-12-31 a las 10:00 fue rechazada: «no partition of "
                           "relation \"cita_hist\" found for row».",
                "preguntas": [
                    ("¿Puedo agregar la partición de 2027 después?",
                     "Sí: CREATE TABLE cita_hist_2027 PARTITION OF cita_hist FOR VALUES FROM "
                     "(TIMESTAMP '2027-01-01') TO (TIMESTAMP '2028-01-01'); y desde ahí las "
                     "citas de 2027 caen solas en ella."),
                ],
                "cuidado": "La trampa 2 no da error al crear la tabla, sino el día que llega una "
                           "fila del hueco.",
                "puente": "El DDL completo, en código, listo para correr.",
            },
        },
        "Particionar hoy de verdad": {
            "ideas": [
                "**tableoid::regclass** dice en qué partición física quedó cada fila.",
                "En el plan de una consulta de 2026 solo aparece **cita_hist_2026**: eso es la "
                "poda.",
                "Archivar un año es **DROP TABLE** de su partición: un instante.",
                "Sin particiones sería un **DELETE** masivo: millones de filas y bloqueos "
                "largos.",
            ],
            "notas": {
                "min": 2,
                "explica": "Particionar se demuestra con tres pruebas: dónde quedó cada fila, "
                           "qué particiones lee una consulta y cuánto cuesta archivar un año. La "
                           "tercera es la razón que no tiene alternativa.",
                "pasos": [
                    ("Al entrar", "Arriba, el reparto: SELECT tableoid::regclass AS particion, "
                     "COUNT(*) FROM cita_hist GROUP BY 1; con la siembra de la demo devuelve "
                     "una sola fila, cita_hist_2026 con 30.010, porque todas las citas son de "
                     "2026."),
                    ("En el medio", "La poda: el plan de una consulta acotada a 2026 solo "
                     "nombra cita_hist_2026."),
                    ("Abajo", "El archivado: DROP TABLE cita_hist_2025 es una operación de "
                     "metadatos y tarda un instante; DETACH PARTITION la separa sin borrarla. "
                     "Sin particiones, el DELETE equivalente toca fila por fila, llena el "
                     "registro de transacciones y sostiene bloqueos."),
                ],
                "ejemplo": "Sin filtro, SELECT COUNT(*) FROM cita_hist recorre las dos "
                           "particiones (el plan muestra un Append con ambas); con el filtro de "
                           "2026, solo una.",
                "preguntas": [
                    ("Si cita_hist_2025 queda vacía, ¿se probó algo?",
                     "Sí: que el motor envió cada fila a la partición que le corresponde. Con "
                     "datos de dos años aparecerían las dos filas en el conteo."),
                ],
                "cuidado": "Sin la consulta de tableoid no hay evidencia del reparto: un INSERT "
                           "que no dio error no prueba dónde quedaron las filas.",
                "puente": "Entonces, ¿la clínica debería particionar?",
            },
        },
        "El veredicto de particionamiento": {
            "ideas": [
                "La cuenta de la clínica: 40 citas al día × 300 días × 5 años = **60.000** citas.",
                "Particionar empieza a pagar en **decenas de millones** de filas.",
                "Veredicto honesto: **no se particiona**, y se dice con el número al lado.",
                "Lo probado hoy es la **poda** y el **archivado**, no una ganancia de tiempo.",
            ],
            "notas": {
                "min": 2,
                "explica": "Saber particionar no obliga a particionar. La decisión se toma con "
                           "el volumen esperado al lado del umbral, y para una clínica de este "
                           "tamaño el número dice que no.",
                "pasos": [
                    ("Al entrar", "La cuenta: 40 citas al día por 300 días son 12.000 al año; en "
                     "cinco años, 60.000."),
                    ("En el medio", "La escala va de mil a cien millones, y cada marca es diez "
                     "veces la anterior. La base de hoy y la clínica a cinco años están juntas a "
                     "la izquierda; el umbral, en decenas de millones, a la derecha: entre 10 "
                     "millones y 60.000 hay más de 160 veces, y con 50 millones, más de 800."),
                    ("Abajo", "El veredicto: no se particiona. Reconocer que con este volumen la "
                     "ganancia no se aprecia es la respuesta correcta; inventar una mejora que el "
                     "plan no muestra, no."),
                ],
                "ejemplo": "Con 60.000 citas, un índice sobre fecha_hora encuentra un día en dos "
                           "o tres lecturas: no hay nada que la partición mejore en lectura.",
                "preguntas": [
                    ("Entonces, ¿para qué lo aprendimos?",
                     "Porque el archivado no tiene alternativa en tablas grandes: un DROP de "
                     "partición contra un DELETE de millones de filas. Y porque la poda se lee "
                     "en el plan igual que un índice."),
                ],
                "cuidado": "No digas «sí conviene» para quedar bien: el número manda.",
                "puente": "Vamos a la demo, en el orden en que se proyecta.",
            },
        },
        "La demo, en el orden": {
            "ideas": [
                "Bloque 0: siembra y **conteo de control** (18.187 · 9.095 · 2.728).",
                "Bloque 1: la **línea base**, con los dos Seq Scan.",
                "Bloque 2: **índices + ANALYZE** y las mismas consultas: el plan nombra el "
                "índice.",
                "Bloques 3 y 4: el **orden de columnas** y la **partición**.",
            ],
            "notas": {
                "min": 1,
                "explica": "El script de la demo tiene cinco bloques y el orden importa: cada "
                           "uno se apoya en el anterior.",
                "pasos": [
                    ("Al entrar", "Recorre los bloques de arriba abajo. El 0 recrea las tablas: "
                     "se corre en una base vacía. Si el conteo de control no da 18.187, 9.095 y "
                     "2.728, se para ahí."),
                    ("Bloque 2", "Es el corazón de la clase: proyecta las dos salidas, antes y "
                     "después, una debajo de la otra, y lee en voz alta la línea del nodo."),
                ],
                "ejemplo": "En el bloque 4, como la siembra pone todas las citas en 2026, "
                           "cita_hist_2025 queda vacía: igual demuestra el reparto.",
                "cuidado": "Si el tiempo aprieta, se recorta el bloque 3, nunca el 2.",
                "puente": "Qué se puede medir en el navegador y qué no.",
            },
        },
        "Donde corre esto": {
            "ideas": [
                "En el navegador se mide el cambio de **Seq Scan** a acceso por índice.",
                "También cuál índice **gana**, el orden de columnas y la **poda** de "
                "particiones.",
                "No se mide la memoria vacía, la **fragmentación** de meses ni dos sesiones a la "
                "vez.",
                "El **tipo de nodo** y las filas son estables; los milisegundos no.",
            ],
            "notas": {
                "min": 1,
                "explica": "Todo lo de hoy corre en PostgreSQL dentro del navegador, con la base "
                           "de 30.010 citas ya sembrada. Hay cosas que ahí no se pueden medir, y "
                           "se declaran en vez de inventarlas.",
                "pasos": [
                    ("Al entrar", "Izquierda, lo que se mide y se ve en el plan; derecha, lo que "
                     "no: tiempos con memoria vacía, índices sobre millones de filas, "
                     "fragmentación tras meses de escrituras y dos sesiones a la vez (Clase "
                     "10). Cierra con la frase de abajo."),
                ],
                "cuidado": "No ofrezcas otra herramienta en línea: no tiene la base sembrada, "
                           "así que ni el cambio de plan ni las 91 filas se pueden reproducir.",
                "puente": "Vamos a la demo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "La agenda del día: **Seq Scan** antes y acceso por índice después, con las "
                "mismas 91 filas.",
                "Entre medio, **ANALYZE**: sin él el plan puede ignorar el índice.",
                "La partición: el plan de una consulta de 2026 solo nombra **cita_hist_2026**.",
            ],
            "notas": {
                "min": 15,
                "explica": "La demo corre el script de la clase y muestra el antes y el después "
                           "con planes reales: el mismo resultado, otro camino.",
                "pasos": [
                    ("Al entrar", "1) Siembra y control. 2) Línea base: C1 (agenda del "
                     "2026-03-10, 91 filas) y C2 (mascotas del dueño 1234, 2 filas), las dos con "
                     "Seq Scan. 3) Los tres CREATE INDEX, ANALYZE cita y ANALYZE mascota, y las "
                     "mismas dos consultas."),
                    ("Después", "4) Lee los planes nuevos: C1 con Bitmap Index Scan on "
                     "idx_cita_programada_fecha; C2 con Bitmap Index Scan on idx_mascota_dueno. "
                     "5) pg_indexes con el WHERE del parcial. 6) Si hay tiempo, el orden de "
                     "columnas y la partición con su poda."),
                ],
                "ejemplo": "C1 antes: Seq Scan on cita, Rows Removed by Filter: 29919. C1 "
                           "después: Bitmap Heap Scan on cita, Bitmap Index Scan on "
                           "idx_cita_programada_fecha, 91 filas.",
                "cuidado": "Nunca hagas la demo sobre una base de 20 filas «porque es lo mismo»: "
                           "el plan no cambia y el grupo concluye que indexar no sirve.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 7 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: un índice se justifica con la consulta que lo usa y se "
                           "demuestra con el antes y el después del mismo plan; la partición "
                           "separa, y hoy no hace falta.",
                "pasos": [
                    "Pregunta de salida: «nombren un índice de hoy y la consulta que lo "
                    "justifica». Corrige el nombre si sale mal escrito. Anuncia que la Clase 8 "
                    "pasa de las lecturas a las escrituras: transacciones.",
                ],
            },
        },
    },
}
