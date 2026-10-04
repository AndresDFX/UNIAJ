# Guion docente · Clase 7 · Indices y particionamiento · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** 3 indices justificados (uno parcial) + historico particionado por ano
- **Entregable de hoy:** Script CREATE INDEX + cita_hist particionada + tabla justificacion consulta->indice
- **Herramienta:** ExamLab (PostgreSQL/PGlite)
- **Slides:** Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx
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

**[Slide 4] De donde viene la clase: los Seq Scan de la Clase 6** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La Clase 6 dejo al grupo mirando planes que decian Seq Scan donde se esperaba algo mejor; hoy se construye la estructura que cambia esa linea.
  - Un indice es una estructura de datos auxiliar, redundante y opcional, que el motor crea a partir de una o mas columnas de una tabla, mantiene ordenada por esas columnas y sincroniza automaticamente con cada cambio de los datos.
  - Cada entrada guarda dos cosas: el valor de la clave y un puntero fisico a la fila completa, que en PostgreSQL se llama ctid y en Oracle ROWID.
  - Redundante: no agrega informacion nueva, duplica columnas que ya estan en la tabla, y por eso se puede borrar y volver a crear sin perder un dato.
  - Opcional: ninguna consulta deja de funcionar si el indice no existe, solo tarda mas.
  - Automatico: nadie escribe codigo para mantenerlo, el motor lo actualiza dentro de la misma operacion del INSERT, del UPDATE o del DELETE, y de ahi sale el costo del que habla la segunda mitad de la clase.
  - La base de hoy es la misma de la clase anterior: 30.010 citas del 5 de enero al 23 de julio de 2026, 5.008 mascotas, 2.006 duenos y 16 veterinarios, con estadisticas frescas y sin ningun indice salvo los de las claves primarias.
  - Sobre esa tabla, un indice de una columna sobre cita(fecha_hora) guarda 30.010 entradas de unos 20 a 25 bytes y ocupa del orden de 700 KB frente a los 2 MB de la tabla
  - Como orden de magnitud, cada indice de una columna cuesta entre el 10 % y el 30 % del tamano de la tabla, y esa cifra es estimacion de oficio, no constante del motor.
  - El numero real se lee con; y es el que hay que reportar, no el de esta linea.
  - NOTAS:
  - Los tres adjetivos de la definicion importan.
  - CÓDIGO CITADO (referencia):
  - SELECT pg_size_pretty(pg_relation_size('idx_cita_fecha_hora'))

**[Slide 5] El B-Tree por dentro, en cinco minutos** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El tipo de indice por omision en PostgreSQL, Oracle, MySQL y SQL Server es el B-Tree, arbol balanceado, y entenderlo por dentro toma cinco minutos bien invertidos.
  - Tiene tres clases de nodos: una raiz, cero o mas niveles intermedios o de rama, y un nivel de hojas donde estan todas las claves con sus punteros.
  - Cada nodo ocupa una pagina, tipicamente de 8 KB, y si cada entrada pesa unos 20 bytes, en una pagina caben del orden de 400 claves; ese numero se llama grado de ramificacion o fan-out.
  - Con 400 hijos por nodo, un arbol de un nivel cubre 400 filas, de dos niveles 160.000, de tres niveles 64 millones y de cuatro niveles mas de 25 mil millones.
  - El crecimiento es logaritmico: duplicar la tabla no duplica el tiempo de busqueda, apenas lo mueve.
  - El indice de cita de hoy, con 30.010 entradas, tiene apenas dos niveles: unas 75 paginas de hojas y una raiz que apunta a todas.
  - Un detalle mas explica la mitad de los usos reales: las hojas estan enlazadas entre si formando una lista, de modo que al llegar a la primera clave que cumple la condicion se puede seguir avanzando en orden
  - Por eso un B-Tree sirve para BETWEEN, para mayor que, para menor que y para devolver filas ya ordenadas sin ejecutar un ordenamiento aparte, no solo para igualdades.
  - NOTAS:
  - Balanceado significa que todas las hojas quedan a la misma profundidad, asi que cualquier busqueda cuesta lo mismo y no hay valores afortunados.
  - De ahi la afirmacion que el docente debe poder defender: tres o cuatro niveles alcanzan para tablas de millones de filas, y encontrar una fila cuesta tres o cuatro lecturas de pagina, sin importar si la tabla tiene cien mil filas o cincuenta millones.
  - Esa es exactamente la forma de la consulta C1 de la clase, que pide un rango de un dia.

**[Slide 6] El precio se paga en cada escritura, y se cuantifica** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El precio de indexar se paga en cada escritura y hay que cuantificarlo.
  - Un INSERT en cita con cuatro indices no es una operacion, son cinco: la fila en la tabla mas una insercion ordenada en cada arbol, cada una bajando dos o tres niveles y a veces partiendo en dos una pagina llena, lo que ademas fragmenta el indice.
  - Como orden de magnitud de oficio, cada indice adicional encarece las escrituras entre un 5 % y un 15 %
  - Y una tabla con diez indices puede escribir varias veces mas lento que la misma con dos; el numero exacto depende del motor y hay que medirlo, pero la direccion nunca cambia.
  - El UPDATE tiene un matiz util y muy citable: solo se actualizan los indices que contienen alguna columna modificada, asi que cambiar cita.estado de PROGRAMADA a ATENDIDA toca idx_cita_estado_fecha pero no idx_cita_fecha_hora
  - De donde sale la advertencia de no indexar columnas que cambian en cada operacion salvo que una consulta muy frecuente lo exija.
  - Ojo con una excepcion que aparece hoy: el indice PARCIAL sobre las citas PROGRAMADA si se toca cuando el estado cambia, porque la fila entra o sale del indice.
  - En espacio, no es raro que la suma de los indices supere el tamano de la tabla.
  - La guia es concreta: dos a cuatro indices por tabla caliente ademas de los que ya trae la clave primaria, cada uno con su consulta escrita al lado
  - Y la regla de descarte mas util que existe, si el estudiante no puede escribir la consulta que usa el indice, el indice se borra.
  - En produccion eso se decide con datos: PostgreSQL expone pg_stat_user_indexes, donde idx_scan en cero significa que el indice nunca se uso.
  - Fuera de la lamina (habla de la practica): El precio de indexar se paga en cada escritura y hay que cuantificarlo, porque es la mitad del veredicto que la pregunta 5 pide por escrito.
  - Fuera de la lamina (habla de la practica): En produccion eso se decide con datos: PostgreSQL expone pg_stat_user_indexes, donde idx_scan en cero significa que el indice nunca se uso; conviene mencionarlo aunque en una sesion de taller no de tiempo de acumular estadisticas de uso.

**[Slide 7] El costo de sobre-indexar, que casi nunca se menciona** — 11 vinetas.

**[Slide 8] Indice compuesto: la regla del prefijo izquierdo** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un indice compuesto es el creado sobre dos o mas columnas, y su regla de uso es la fuente de error mas frecuente del tema.
  - Las entradas se ordenan por la primera columna y solo dentro de los valores iguales de la primera se ordenan por la segunda; es el orden de un directorio telefonico por apellido y luego nombre.
  - En la clínica: idx_cita_estado_fecha sirve para WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-03-01 00:00:00' y para WHERE estado = 'PROGRAMADA' a secas, y no sirve para un filtro que solo trae fecha_hora; para eso existe idx_cita_fecha_hora.
  - Y un numero citable que desarma la idea de indexar todo por si acaso: un indice de k columnas atiende solamente los k prefijos, no las combinaciones, asi que uno de tres columnas atiende tres formas de consulta y no seis.
  - NOTAS:
  - De ahi la regla del prefijo mas a la izquierda: un indice sobre (estado, fecha_hora) resuelve una busqueda por estado, y una por estado junto con fecha_hora, pero NO resuelve eficientemente una busqueda solo por fecha_hora, igual que en el directorio no se pueden encontrar todas las personas llamadas Ana sin leerlo entero.
  - El corolario de diseno cabe en una linea, y es la que hay que dejar escrita en la pizarra: las columnas comparadas por igualdad van primero y la comparada por rango va al final, porque despues del primer rango el orden interno del indice deja de ser aprovechable.

**[Slide 9] Cuando el indice responde solo, sin tocar la tabla** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Cuando todas las columnas que la consulta necesita, las del WHERE y las del SELECT, estan dentro del indice, el motor responde sin tocar la tabla, y eso se llama index-only scan o indice cubridor.
  - Ejemplo exacto con los indices de hoy: SELECT estado, fecha_hora FROM cita WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-03-01 00:00:00' se puede responder entera desde idx_cita_estado_fecha, y el plan lo dice con las palabras Index Only Scan.
  - El ahorro es justamente la parte cara del acceso por indice: en lugar de dos o tres lecturas para bajar el arbol mas un centenar de lecturas dispersas a la tabla, quedan unas pocas lecturas de hojas contiguas.
  - Si la consulta agrega id_mascota la ventaja se pierde, y hay dos maneras de recuperarla: agregar la columna a la clave, o usar la clausula INCLUDE de PostgreSQL, INCLUDE (id_mascota)
  - Que guarda la columna en las hojas sin usarla para ordenar y por lo tanto sin engordar los niveles superiores
  - Un detalle honesto que evita una confusion en vivo: en PostgreSQL el index-only scan depende del mapa de visibilidad
  - Asi que inmediatamente despues de una carga masiva el plan puede seguir mostrando Index Scan hasta que pase VACUUM, y eso no significa que el indice este mal disenado.
  - NOTAS:
  - Oracle no tiene INCLUDE y la columna se agrega al final de la clave.
  - CÓDIGO CITADO (referencia):
  - CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora)
  - Fuera de la lamina (habla de la practica): Esto NO se califica hoy, pero es la respuesta a la pregunta que va a salir cuando alguien vea Index Only Scan en su plan y no sepa si esta bien.

**[Slide 10] Las siete razones por las que un indice existente no se usa** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un indice existente puede quedar sin usar por siete razones, y recitarlas separa al docente que responde del que dice que el motor es raro.
  - Uno, la tabla es demasiado pequena: dueno con 2.006 filas cabe en unas 20 paginas y ningun indice le gana a leer 20 paginas seguidas; con las 20 filas de prueba de una base propia jamas se usara un indice y el motor esta en lo correcto.
  - Dos, el predicado no es sargable, como se vio en la Clase 6: UPPER(nombre), EXTRACT(YEAR FROM fecha_hora) o una conversion implicita de tipo bloquean el indice
  - Y la salida es el indice funcional, CREATE INDEX idx_mascota_nombre_upper ON mascota (UPPER(nombre)).
  - Tres, la selectividad es mala: WHERE activa = 'S' devuelve mas del 90 % de mascota y el recorrido completo gana con razon.
  - Cuatro, las estadisticas estan viejas y el motor cree que la tabla es diminuta; se corrige con ANALYZE cita, y es el paso que se salta medio salon.
  - Con la base de hoy la excusa del volumen no aplica: 30.010 citas son suficientes para que el planeador prefiera el indice, asi que si el plan no cambia el problema esta en el predicado, en el nombre de la columna lider o en el ANALYZE que falto.
  - NOTAS:
  - Cinco, se violo el prefijo mas a la izquierda.
  - Seis, la condicion combina columnas de indices distintos con OR, caso en el que el motor arma una combinacion de mapas de bits o simplemente escanea.
  - Siete, el tipo de dato o la ordenacion no coincide con lo que el predicado compara.

**[Slide 11] Los cinco nombres que se califican, y la consulta que justifica cada uno** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Los tres de la medicion: idx_cita_fecha_hora sobre cita (fecha_hora), que atiende cualquier consulta por rango de fecha con o sin estado; idx_mascota_dueno sobre mascota (id_dueno)
  - Que atiende el historial de un dueno; y idx_cita_programada_fecha, el indice parcial sobre cita (fecha_hora) WHERE estado = 'PROGRAMADA', que atiende la agenda del dia de la recepcion.
  - Los dos del experimento de orden: idx_cita_estado_fecha sobre cita (estado, fecha_hora) e idx_cita_fecha_estado sobre cita (fecha_hora, estado), las mismas dos columnas en orden inverso, creados a proposito para medir la diferencia.
  - Un aviso concreto: idx_cita_fecha no es ninguno de los cinco, el sufijo es _fecha_hora como la columna, y ese fue durante un tiempo el nombre que aparecia en el material.
  - Primero: declarar PRIMARY KEY o UNIQUE crea automaticamente un indice unico para sostener la restriccion, asi que id_dueno, id_mascota e id_cita YA tienen indice y crear otro encima solo duplica espacio y trabajo de escritura.
  - Segundo, menos conocido: declarar una FOREIGN KEY NO crea indice en ninguno de los dos motores. mascota.id_dueno apunta a dueno, pero del lado de mascota no hay nada ordenado
  - Y por eso idx_mascota_dueno si es una adicion legitima; sin el, ademas, borrar un dueno obliga a recorrer mascota completa para verificar la integridad.
  - NOTAS:
  - El nombre de cada indice importa.
  - Dos hechos sobre claves evitan la mitad de los indices inutiles que se entregan en los proyectos.
  - Fuera de la lamina (habla de la practica): Aqui empieza la parte que se califica letra por letra, y conviene decirlo con esas palabras.
  - Fuera de la lamina (habla de la practica): El nombre de cada indice importa, porque el plan de ejecucion imprime literalmente Index Scan using seguido del nombre y porque la tabla de justificacion de la pregunta 5 se llena con esos mismos nombres.
  - Fuera de la lamina (habla de la practica): Un aviso concreto: idx_cita_fecha no es ninguno de los cinco, el sufijo es _fecha_hora como la columna, y ese fue durante un tiempo el nombre que aparecia en el material; si alguien lo escribe asi pierde puntos por el nombre y no por el concepto.

**[Slide 12] Un indice se justifica con la consulta que lo usa** — 11 vinetas.

**[Slide 13] La secuencia de medicion, y por que el ANALYZE del medio no es opcional** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La clase entera vive en una secuencia de cuatro pasos que hay que proyectar en ese orden, porque cambiarlo destruye la evidencia.
  - Primero, EXPLAIN ANALYZE de las dos consultas frecuentes ANTES de crear nada: tiene que salir Seq Scan on cita y Seq Scan on mascota, y ese es el punto de comparacion.
  - C1 es la agenda del dia, SELECT id_cita, fecha_hora, estado FROM cita WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00' AND estado = 'PROGRAMADA', y devuelve 91 filas de las 150 citas que tiene ese dia
  - Tercero, y este es el paso que se salta medio salon, ANALYZE cita; y ANALYZE mascota;: crear el indice NO actualiza las estadisticas, el planeador decide por costo estimado, y con numeros viejos puede ignorar un indice perfectamente bueno.
  - La mitad de los avisos de «cree el indice y no me sirvio» de la clase son este paso omitido.
  - Cuarto, las MISMAS dos consultas otra vez, sin cambiar una coma: si se cambia una fecha o un id la comparacion deja de valer.
  - Y el cierre es la evidencia de que existen: ORDER BY tablename, indexname; la columna indexdef devuelve el CREATE INDEX completo, asi que ahi se ve tambien la clausula WHERE del indice parcial, que es lo que confirma que se creo parcial y no completo.
  - El enunciado ademas exige comentar CUAL de los dos indices sobre fecha_hora eligio el planeador para C1.
  - NOTAS:
  - Segundo, los CREATE INDEX.
  - CÓDIGO CITADO (referencia):
  - SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234
  - SELECT indexname, tablename, indexdef FROM pg_indexes WHERE tablename IN ('cita','mascota')
  - Fuera de la lamina (habla de la practica): El enunciado ademas exige comentar CUAL de los dos indices sobre fecha_hora eligio el planeador para C1, y la rubrica descuenta si no se comenta: no basta pegar el plan, hay que leerlo.

**[Slide 14] Crear el indice y probar que se usa** — 11 vinetas.

**[Slide 15] El experimento del orden de columnas, paso a paso** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Se crean los dos compuestos, se corre ANALYZE cita, y se miden tres consultas.
  - Q1 filtra por estado con igualdad y por fecha_hora con rango: favorece a idx_cita_estado_fecha, porque la columna de igualdad es la lider y el rango queda al final.
  - Q2 filtra solo por rango de fecha_hora: favorece a idx_cita_fecha_estado, porque ahi fecha_hora si es la lider.
  - Q3 filtra solo por estado, sin fecha: idx_cita_fecha_estado no le sirve, porque su columna lider no aparece en el WHERE, y con CANCELADA siendo apenas 2.728 de 30.010 filas el motor puede elegir idx_cita_estado_fecha o resolver por conteo.
  - Despues viene la parte que convierte la observacion en experimento: se hace DROP INDEX idx_cita_fecha_estado y se vuelve a medir Q2.
  - El plan cae en idx_cita_fecha_hora, que tambien tiene fecha_hora como lider, o vuelve al recorrido completo, pero NO se pasa a idx_cita_estado_fecha.
  - Un matiz honesto: el planeador decide por costo y puede sorprender, sobre todo entre dos indices que compiten de cerca; la instruccion al grupo es reportar lo que VIO en su plan, no lo que decia la diapositiva, y explicar la eleccion.
  - NOTAS:
  - Eso es la regla del prefijo izquierdo vista en vivo, y es la unica manera de que no quede como una frase que se memoriza.
  - Un plan distinto bien leido vale mas que el plan esperado copiado.
  - Fuera de la lamina (habla de la practica): La pregunta 2 no pide creer la regla del prefijo izquierdo, pide demostrarla, y el docente tiene que poder anticipar los tres resultados.

**[Slide 16] El orden de columnas en un indice compuesto** — 10 vinetas.

**[Slide 17] Los cinco indices de hoy, con su nombre exacto** — 5 vinetas.

**[Slide 18] El indice parcial: que indexa, cuanto ahorra y cuando gana** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un indice parcial es el que solo contiene las filas que cumplen una condicion, y la sintaxis es WHERE estado = 'PROGRAMADA'.
  - Lo primero que hay que aclarar, porque es donde se confunde todo el mundo: ese WHERE no es el de la consulta, es parte de la DEFINICION del indice y decide que filas entran en el arbol.
  - Con los datos de hoy el ahorro se puede decir con numeros exactos: de las 30.010 citas, 18.187 estan PROGRAMADA, el 61 %; el indice completo indexa 30.010 entradas y el parcial 18.187, cuatro de cada diez menos.
  - Menos entradas es menos disco, menos memoria intermedia ocupada y menos trabajo en cada escritura de una cita que no este programada.
  - La condicion para que el planeador lo use es estricta: tiene que poder demostrar que la consulta trae la misma condicion del indice.
  - WHERE estado = 'PROGRAMADA' AND fecha_hora >=... si lo aprovecha; la misma consulta sin el filtro de estado no, porque el indice no contiene las filas atendidas ni las canceladas y el motor no puede arriesgarse a devolver un resultado incompleto.
  - Cuando el filtro es parte del caso de uso y no del capricho de una consulta, el parcial es la respuesta correcta.
  - Y en C1 los dos indices sobre fecha_hora compiten: se espera que gane el parcial
  - Porque recorre 91 entradas y ya sabe que todas cumplen el estado, mientras el completo recorreria las 150 del dia y tendria que descartar 59 despues de ir a la tabla a leer el estado.
  - La diferencia de costo es pequena con este volumen, asi que si en la corrida gana el completo la respuesta correcta sigue siendo la que reporta lo que se vio.
  - NOTAS:
  - El caso de la clínica que lo justifica hay que nombrarlo: la agenda del dia de la recepcion SIEMPRE filtra por PROGRAMADA, porque nadie abre esa pantalla para ver las citas que ya se atendieron.
  - CÓDIGO CITADO (referencia):
  - CREATE INDEX idx_cita_programada_fecha ON cita (fecha_hora)

**[Slide 19] El indice parcial: el mismo beneficio, una fraccion del tamano** — 5 vinetas.

**[Slide 20] Particionar: que es, y por que hoy si se implementa** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Particionar es dividir una sola tabla logica en fragmentos fisicos llamados particiones, segun una clave, de modo que el motor descarte de entrada las que no pueden contener lo buscado; ese descarte se llama poda de particiones o partition pruning.
  - La forma mas frecuente es por rango de fechas: una particion por ano, de manera que una consulta de 2026 lee unicamente la particion de 2026 y el plan lo muestra.
  - La frase que lo separa del tema anterior es corta: el indice ordena, la particion separa.
  - El particionamiento se implementa completo —DDL, dos particiones, migracion de las citas, prueba de enrutamiento y prueba de poda— sobre una base de 5.010 citas repartidas entre 2025 y 2026.
  - Si el docente anuncia que hoy no se implementa.
  - Error comun: declarar la clave primaria solo sobre id_cita.
  - NOTAS:
  - El umbral en el que empieza a pagar en produccion es alto y hay que decirlo con numeros para que nadie lo use de adorno: como convencion de oficio se piensa en particionar por encima de unas decenas de millones de filas o de tablas de decenas de gigabytes, y por debajo de eso un indice sobre fecha_hora hace el mismo trabajo con mucho menos mantenimiento.
  - Ahora la advertencia importante para el docente, porque es la que ha costado puntos: eso NO significa que hoy el particionamiento sea una idea conceptual que solo se cuenta.
  - Lo que si es cierto, y hay que decirlo en la misma frase, es que con 5.010 filas la ganancia de RENDIMIENTO no es apreciable: lo que se demuestra hoy es que el motor descarta particiones enteras antes de leer, y que archivar un ano se vuelve trivial.
  - En una tabla particionada PostgreSQL exige que la PK incluya la columna de particion, asi que la clave pasa a ser (id_cita, fecha_hora).
  - Fuera de la lamina (habla de la practica): Si el docente anuncia que hoy no se implementa, el estudiante llega al taller con una respuesta en prosa a una pregunta que pide SQL ejecutado.

**[Slide 21] Particionar el historico por rango de fecha** — 14 vinetas.

**[Slide 22] El DDL de la particion, con sus dos trampas** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El DDL son tres sentencias y dos trampas.
  - La primera sentencia declara la tabla particionada: PARTITION BY RANGE (fecha_hora)
  - Las otras dos crean las particiones: TO (TIMESTAMP '2026-01-01'); y su gemela de 2026.
  - Primera trampa, la que cuesta la pregunta: en una tabla particionada la clave primaria DEBE incluir la columna de particion, asi que PRIMARY KEY (id_cita, fecha_hora) y no PRIMARY KEY (id_cita) a secas.
  - Esto no es una rareza de MySQL, es la regla de PostgreSQL, y el mensaje de error del motor no dice «te falta la columna de particion» con esas palabras, asi que el estudiante que lo intenta se queda mirando un error que no entiende.
  - Segunda trampa, mas silenciosa: el rango es cerrado por abajo y abierto por arriba, de modo que el TO de una particion es exactamente el FROM de la siguiente y nunca se solapan
  - Quien escriba TO (TIMESTAMP '2025-12-31') se queda sin sitio donde poner las citas del 31 de diciembre y el INSERT falla con un error de que no se encontro particion.
  - Despues del DDL viene la migracion,, y la prueba de que el reparto ocurrio:, MIN(fecha_hora), MAX(fecha_hora) tableoid es una columna de sistema que dice en que tabla FISICA vive cada fila y::regclass la traduce a nombre.
  - La poda se comprueba con EXPLAIN ANALYZE de una consulta acotada a 2026: en el plan debe aparecer SOLO cita_hist_2026.
  - NOTAS:
  - Sin esa consulta no hay evidencia del enrutamiento, solo un INSERT que no dio error.
  - CÓDIGO CITADO (referencia):
  - CREATE TABLE cita_hist (id_cita INT, id_mascota INT, id_veterinario INT, fecha_hora TIMESTAMP NOT NULL, estado TEXT, PRIMARY KEY (id_cita, fecha_hora))
  - CREATE TABLE cita_hist_2025 PARTITION OF cita_hist FOR VALUES FROM (TIMESTAMP '2025-01-01')
  - INSERT INTO cita_hist SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita
  - SELECT tableoid::regclass AS particion, COUNT(*)
  - FROM cita_hist GROUP BY 1 ORDER BY 1
  - Fuera de la lamina (habla de la practica): Sin esa consulta no hay evidencia del enrutamiento, solo un INSERT que no dio error, y la rubrica lo pide explicitamente.

**[Slide 23] Particionar hoy de verdad: rango por ano, poda y archivado** — 5 vinetas.

**[Slide 24] El veredicto de particionamiento que pide la pregunta 5** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Primera: el volumen que espera la clínica, con numeros propios del estudiante, del estilo tantas citas por dia por tantos dias de operacion al ano por tantos anos de historia.
  - Un dato de referencia para calibrar: 40 citas diarias durante 300 dias son 12.000 citas al ano
  - Y a cinco anos son 60.000; eso esta tres ordenes de magnitud por debajo del umbral de particionamiento, asi que el veredicto honesto para la clínica es que NO se particiona, y decirlo con el numero al lado vale mas que decir que si por quedar bien.
  - Segunda: la ganancia de rendimiento con 5.010 filas no es apreciable.
  - Tercera: lo que si quedo comprobado, que son dos cosas concretas, la poda de particiones en el plan y la facilidad de archivado.
  - Y ahi esta el caso que no tiene alternativa, el que justifica aprender el tema aunque hoy no se aplique: borrar cinco anos de historia con DELETE FROM cita WHERE fecha_hora < TIMESTAMP '2021-01-01 00:00:00' toca millones de filas
  - Genera un registro de transacciones enorme, sostiene bloqueos largos y deja la tabla que hay que limpiar despues
  - En cambio DROP TABLE cita_hist_2021 es una operacion de metadatos que tarda un instante, y ALTER TABLE cita_hist DETACH PARTITION cita_hist_2021 la separa sin borrar los datos si hay que conservarlos aparte.
  - En Oracle la sentencia equivalente es ALTER TABLE cita DROP PARTITION cita_2021, y la diferencia de sintaxis conviene mencionarla porque el motor de hoy es PostgreSQL.
  - Ese contraste entre DROP de particion y DELETE masivo conecta directo con la Clase 8, donde el registro de transacciones y la duracion de los bloqueos son el tema.
  - NOTAS:
  - Un veredicto de particionamiento tiene tres exigencias distintas.
  - Fuera de la lamina (habla de la practica): Segunda: la ganancia de rendimiento con 5.010 filas no es apreciable, y reconocerlo suma puntos en vez de restarlos, porque la alternativa es inventar una mejora que el plan no muestra.

**[Slide 25] La demo, en el orden en que se proyecta** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La demo es el script Codigo/07_indices_clinica.sql y se corre, no en otra herramienta, porque el volumen sembrado es el que hace cambiar el plan.
  - Termina con una consulta de control que debe devolver 18.187 PROGRAMADA, 9.095 ATENDIDA y 2.728 CANCELADA; si esos numeros no salen, nada de lo que sigue cuadra y hay que parar ahi.
  - El bloque 1 es la linea base, con los dos Seq Scan.
  - El bloque 3 es el experimento del orden, con su DROP INDEX al final.
  - Si el bloque 0 no alcanza el tiempo.
  - NOTAS:
  - El script trae cinco bloques y el orden importa.
  - El bloque 2 crea los tres indices, corre ANALYZE y repite las dos consultas: ese es el momento de la clase, y conviene proyectar las dos salidas una debajo de la otra y leer en voz alta la linea del nodo.
  - El bloque 4 es el particionamiento completo, con una salvedad que hay que decir en vivo: como la siembra del bloque 0 pone todas las citas en 2026, todo cae en cita_hist_2026 y cita_hist_2025 queda vacia; eso ya demuestra el enrutamiento.
  - Lo que no se puede hacer es medir en una base de 20 filas: el plan no va a cambiar y el grupo se va a llevar la conclusion contraria.
  - Fuera de la lamina (habla de la practica): El bloque 0 crea las tablas y siembra la misma base de la actividad: 10 citas a mano mas 30.000 con generate_series, 30.010 en total; hay que advertir que ese bloque recrea las tablas, asi que se corre en una base vacia y no sobre la base de la clínica con datos que alguien quiera conservar.
  - Fuera de la lamina (habla de la practica): El bloque 4 es el particionamiento completo, con una salvedad que hay que decir en vivo: como la siembra del bloque 0 pone todas las citas en 2026, todo cae en cita_hist_2026 y cita_hist_2025 queda vacia; eso ya demuestra el enrutamiento, y la base de la pregunta 3 si reparte sus 5.010 citas entre los dos anos.
  - Fuera de la lamina (habla de la practica): Si el bloque 0 no alcanza el tiempo, la alternativa es abrir directamente la pregunta 1 de la clase, que ya trae la base sembrada, y correr los bloques 1 y 2 ahi.

**[Slide 26] Donde corre esto, y que no se puede medir aqui** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - En particular DB Fiddle queda fuera, aunque tambien tenga PostgreSQL, por un motivo concreto: la base sembrada con las 30.010 citas no existe alli.
  - Lo medible con confianza: el tipo de nodo, las filas estimadas contra reales y el numero de particiones leidas.
  - Los milisegundos no se comparan entre maquinas: cambian incluso entre 2 corridas seguidas en el mismo equipo.
  - NOTAS:
  - La herramienta de hoy es una sola y conviene decirlo sin ambiguedad: PostgreSQL en el navegador, que ejecuta PostgreSQL sobre PGlite dentro del navegador.
  - Ahi corre la demo.
  - Lo que si se puede medir aqui: el cambio de Seq Scan a Index Scan, la eleccion entre dos indices que compiten, el efecto del orden de columnas con su DROP INDEX, el particionamiento declarativo completo y la poda en el plan, y el tamano de cada indice con pg_relation_size.
  - Lo que NO se puede medir, y hay que declararlo en el informe en vez de inventarlo: los tiempos con la memoria intermedia vacia, porque vaciarla exige privilegios de administrador; el tiempo de creacion de un indice sobre decenas de millones de filas; la fragmentacion despues de meses de escrituras; la degradacion medible de un INSERT con diez indices, que necesita una carga sostenida; y cualquier cosa que exija dos sesiones simultaneas, porque PGlite corre una sola, que es el tema de la Clase 10.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - Primera, y la mas previsible: entonces creo (estado, fecha_hora) y tambien (fecha_hora, estado).
  - En produccion rara vez se justifica tener los dos, porque el segundo queda casi siempre cubierto por el indice de una sola columna sobre fecha_hora mas el filtro de estado aplicado sobre las pocas filas que sobreviven, y cada indice extra se paga en cada escritura.
  - Hoy se crean los dos a proposito, para medir, y el experimento termina con un DROP INDEX que muestra que pasa cuando falta uno: crear para medir y crear para dejar son dos cosas distintas, y esa distincion es la respuesta.
  - Segunda: cree el indice y el plan no cambio, entonces sirve o no sirve.
  - Con 20 filas el indice puede estar bien elegido y el motor tener razon en no usarlo; con las 30.010 de hoy el volumen ya no es excusa, asi que se revisa en este orden, el ANALYZE, el nombre de la columna lider, y si el predicado es sargable.
  - Tercera: si particionar no mejora nada con este volumen, para que lo hacemos.
  - Cuarta: el indice parcial y el completo indexan la misma columna, no es redundante.
  - No lo es mientras existan consultas que no traigan el filtro de estado: esas solo pueden usar el completo.
  - Quinta: puedo poner el indice y ya, sin medir.
  - Si todas las consultas del proyecto filtran por PROGRAMADA, entonces si sobra el completo.
  - No, porque hace falta la linea base con Seq Scan; sin el antes, el despues no demuestra nada.
  - Fuera de la lamina (habla de la practica): Ahi corre la demo, ahi se resuelve el taller y ahi se califica, asi que no hay razon para trabajar en otro sitio.
  - Fuera de la lamina (habla de la practica): En particular DB Fiddle queda fuera, aunque tambien tenga PostgreSQL, por un motivo concreto: la base sembrada con las 30.010 citas no existe alli, y sin ella no se puede reproducir ni el cambio de plan ni las 91 filas que la rubrica menciona.
  - Fuera de la lamina (habla de la practica): Un alterno que cuesta puntos no es un alterno.
  - Fuera de la lamina (habla de la practica): Google Docs se usa para la tabla de justificacion de la pregunta 5, que es prosa y no SQL.
  - Fuera de la lamina (habla de la practica): Esa lista de limites es la seccion 5 de la pregunta 5 y vale puntos: se pierde por omitirla, no por tenerla.


**Demo que usted debe poder repetir:** EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 7 · Indices y particionamiento · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. De donde viene la clase: los Seq Scan de la Clase 6
5. El B-Tree por dentro, en cinco minutos
6. El precio se paga en cada escritura, y se cuantifica
7. El costo de sobre-indexar, que casi nunca se menciona
8. Indice compuesto: la regla del prefijo izquierdo
9. Cuando el indice responde solo, sin tocar la tabla
10. Las siete razones por las que un indice existente no se usa
11. Los cinco indices, y la consulta que justifica cada uno
12. Un indice se justifica con la consulta que lo usa
13. La secuencia de medicion, y por que el ANALYZE del medio no es opcional
14. Crear el indice y probar que se usa
15. El experimento del orden de columnas, paso a paso
16. El orden de columnas en un indice compuesto
17. Los cinco indices de hoy, con su nombre exacto
18. El indice parcial: que indexa, cuanto ahorra y cuando gana
19. El indice parcial: el mismo beneficio, una fraccion del tamano
20. Particionar: que es, y por que hoy si se implementa
21. Particionar el historico por rango de fecha
22. El DDL de la particion, con sus dos trampas
23. Particionar hoy de verdad: rango por ano, poda y archivado
24. El veredicto de particionamiento
25. La demo, en el orden en que se proyecta
26. Donde corre esto, y que no se puede medir aqui
27. Demo del dia
28. Cierre · Clase 7

> Privado, no se proyecta: `Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Indices y particionamiento · VetCare.»
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
- Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.
- El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.
- Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.
- Candidatos reales en VetCare: cita(fecha_hora) para listar la agenda del dia, mascota(id_dueno) porque cada consulta de historial parte de un dueno, detalle_factura(id_factura) para armar el total de una factura sin escanear toda la tabla.
- Particionamiento (hoy SI se implementa, y es la pregunta 3 del taller): dividir una tabla logica en fragmentos fisicos por rango de fecha, de modo que la consulta de un ano no toque los datos del otro. PostgreSQL lo hace con PARTITION BY RANGE (fecha_hora) y una particion por ano. El indice ORDENA los datos; la particion los SEPARA.
- Con 5.010 filas la particion no acelera nada y hay que decirlo: lo que si se comprueba hoy es la poda de particiones en el plan (solo aparece cita_hist_2026) y el archivado, porque tirar un ano completo es un DROP TABLE de la particion en vez de un DELETE masivo.
- Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 27]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 El plan de C1 antes y despues: Seq Scan -> Index Scan using idx_cita_programada_fecha [[captura: salida-indice-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 7 - Indices y particionamiento/Taller PI - Clase 7 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: 3 indices justificados (uno parcial) + historico particionado por ano
Actividades:
1. Medir la linea base con EXPLAIN ANALYZE de las dos consultas frecuentes: hay que ver Seq Scan.
2. Crear los tres indices con el nombre exacto, incluido el parcial idx_cita_programada_fecha, y correr ANALYZE.
3. Repetir los EXPLAIN y decir cual indice eligio el planeador y por que.
4. Construir cita_hist particionada por ano, migrar las citas y demostrar el enrutamiento y la poda.
5. Llenar la tabla de justificacion consulta->indice (7 columnas) y el veredicto de particionamiento.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script CREATE INDEX + cita_hist particionada + tabla justificacion consulta->indice
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 7/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 7 - VetCare.docx`. Clave para usted: `Quiz Clase 7 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 28]
**Decir:** «Queda visto: Indices y particionamiento · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 28] slide de cierre. Dudas finales.


## Reparto del bloque y logistica (no se proyecta)

### El reparto de los 120 minutos y como acompanar el taller

El bloque de 120 minutos se reparte asi. Del minuto 0 al 10, encuadre y el enganche de la Clase 6: se proyecta un plan con Seq Scan y se anuncia que hoy esa linea cambia. Del 10 al 30, la teoria core: que es un indice, el B-Tree y el precio en cada escritura. Del 30 al 45, la diapositiva de justificacion, el prefijo izquierdo y las razones por las que un indice no se usa. Del 45 al 60, los cinco nombres y la secuencia de medicion, con la demo del bloque 2 en vivo: es el corazon de la sesion y no se debe recortar. Del 60 al 70, el indice parcial con sus numeros. Del 70 al 80, el particionamiento con el DDL y la trampa de la clave primaria. Del 80 al 115, el taller, que son 100 puntos en cinco preguntas: se abre ExamLab y se resuelve la pregunta 1 acompanada, en voz alta, hasta que aparezca el primer Index Scan del grupo, y las cuatro restantes de forma individual. Del 115 al 120, cierre y el amarre con la Clase 8. Tres avisos para el acompanamiento. Uno, el error mas frecuente no es conceptual sino de nombre: conviene proyectar los cinco nombres y dejarlos en pantalla mientras el grupo trabaja. Dos, cuando alguien diga que su indice no sirvio, la primera pregunta es si corrio el ANALYZE, no si el indice esta bien pensado. Tres, la pregunta 5 no es un relleno de cierre: son 20 puntos, la tabla tiene siete columnas y quien la deje para el ultimo minuto entrega tres columnas de siete. Vale la pena anunciar a mitad del taller que faltan 15 minutos y que la tabla de justificacion todavia no esta escrita.

## Codigo / scripts
Carpeta Codigo/ — archivo 07_indices_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 7/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
