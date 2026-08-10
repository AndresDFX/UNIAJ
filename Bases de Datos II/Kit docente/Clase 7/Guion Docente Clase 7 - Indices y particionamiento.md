# Guion docente · Clase 7 · Indices y particionamiento · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=2 indices justificados sobre tablas calientes del PI
- **Entregable de hoy:** Script CREATE INDEX + tabla justificacion consulta->indice
- **Herramienta:** DB Fiddle + draw.io (opcional)
- **Slides:** Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.
- El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.
- Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.
- Candidatos reales en VetCare: Cita(fecha_hora) para listar la agenda del dia, Mascota(id_dueno) porque cada consulta de historial parte de un dueno, DetalleFactura(id_factura) para armar el total de una factura sin escanear toda la tabla.
- Particionamiento (idea conceptual, no se implementa hoy): dividir fisicamente una tabla muy grande en fragmentos (ej. Cita por mes o por anio) para que las consultas que solo piden 'las citas de este mes' lean unicamente esa porcion, no la tabla historica completa. Es una tecnica de escala, distinta del indice, mientras el indice ordena datos, la particion los separa fisicamente en bloques.
- Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha.

### Desarrollo del tema (para dictar sin consultar otra fuente)

La Clase 6 dejo al grupo mirando planes que decian Seq Scan o TABLE ACCESS FULL donde se esperaba algo mejor; hoy se construye la estructura que cambia esa linea. Un indice es una estructura de datos auxiliar, redundante y opcional, que el motor crea a partir de una o mas columnas de una tabla, mantiene ordenada por esas columnas y sincroniza automaticamente con cada cambio de los datos. Cada entrada del indice guarda dos cosas: el valor de la clave y un puntero fisico a la fila completa, que en Oracle se llama ROWID y en PostgreSQL ctid. Los tres adjetivos de esa definicion importan y conviene subrayarlos uno por uno. Redundante: el indice no agrega informacion nueva, duplica columnas que ya estan en la tabla, y por eso se puede borrar y volver a crear sin perder un solo dato. Opcional: ninguna consulta deja de funcionar si el indice no existe, solamente tarda mas. Automatico: nadie escribe codigo para mantenerlo, el motor lo actualiza dentro de la misma operacion del INSERT, del UPDATE o del DELETE, y de ahi sale el costo del que habla la segunda mitad de la clase. Con las cifras de VetCare que ya se usaron en la clase anterior, un indice sobre cita(fecha_hora) con 200.000 entradas de unos 20 a 25 bytes cada una ocupa entre 4 y 6 MB, frente a los 20 MB de la tabla; como orden de magnitud, cada indice de una sola columna cuesta entre el 10 % y el 30 % del tamano de la tabla, y esa cifra es estimacion de oficio, no una constante del motor.

El tipo de indice que se usa por omision en Oracle, PostgreSQL, MySQL y SQL Server es el B-Tree, arbol balanceado, y entenderlo por dentro toma cinco minutos bien invertidos. El arbol tiene tres clases de nodos: una raiz, cero o mas niveles de nodos intermedios o de rama, y un nivel de hojas donde estan todas las claves con sus punteros. Balanceado significa que todas las hojas quedan a la misma profundidad, asi que cualquier busqueda cuesta lo mismo y no hay valores afortunados. Cada nodo ocupa una pagina, tipicamente de 8 KB, y si cada entrada pesa unos 20 bytes, en una pagina caben del orden de 400 claves; ese numero se llama grado de ramificacion o fan-out. Con 400 hijos por nodo, un arbol de un nivel apunta a 400 filas, de dos niveles a 160.000, de tres niveles a 64 millones y de cuatro niveles a mas de 25 mil millones. De ahi la afirmacion que el docente debe poder defender: tres o cuatro niveles alcanzan para tablas de millones de filas, y por lo tanto encontrar una fila cuesta tres o cuatro lecturas de pagina, sin importar si la tabla tiene cien mil filas o cincuenta millones. El crecimiento es logaritmico, y eso significa en la practica que duplicar el tamano de la tabla no duplica el tiempo de busqueda: apenas lo mueve. El indice de cita con 200.000 filas tiene dos o tres niveles. Un detalle mas que explica la mitad de los usos reales: las hojas estan enlazadas entre si formando una lista, de modo que al llegar a la primera clave que cumple una condicion se puede seguir avanzando en orden; por eso un B-Tree sirve para BETWEEN, para mayor que, para menor que y para devolver filas ya ordenadas sin ejecutar un ordenamiento aparte, y no solamente para igualdades.

En VetCare los tres indices del script de la clase son CREATE INDEX idx_cita_fecha ON cita (fecha_hora); CREATE INDEX idx_mascota_dueno ON mascota (id_dueno); y CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora); Cada uno tiene que poder justificarse con la consulta concreta que lo aprovecha, y las tres consultas son reales del PI: la agenda del dia filtra por fecha_hora, el historial de un dueno entra siempre por mascota.id_dueno, y la pantalla de recepcion combina estado con un rango de fechas. Al ejecutar el CREATE INDEX el motor lee la tabla completa una vez, ordena las claves y arma el arbol; sobre 200.000 filas eso tarda uno o dos segundos, pero conviene decir que en una tabla real de 50 millones de filas son minutos y que la creacion normal bloquea las escrituras, razon por la cual existen las variantes CREATE INDEX CONCURRENTLY en PostgreSQL y ONLINE en Oracle. Hay dos hechos sobre claves que evitan la mitad de los indices inutiles que entregan los equipos. El primero: declarar una PRIMARY KEY o una restriccion UNIQUE crea automaticamente un indice unico para sostenerla, asi que id_dueno en dueno, id_mascota en mascota y id_cita en cita YA tienen indice, y crear otro encima solo duplica espacio y trabajo de escritura sin ganar nada. Un indice unico es el que rechaza claves repetidas, y en ese caso el indice no es solo rendimiento, es la restriccion misma; un indice no unico apenas acelera. El segundo hecho, mucho menos conocido: declarar una FOREIGN KEY NO crea indice en ninguno de los dos motores. mascota.id_dueno apunta a dueno, pero del lado de mascota no hay nada ordenado, y por eso idx_mascota_dueno si es una adicion legitima; ademas, sin ese indice, borrar un dueno obliga al motor a recorrer mascota completa para verificar la integridad referencial.

Un indice compuesto es el creado sobre dos o mas columnas, y su regla de uso es la fuente de error mas frecuente de todo el tema. Las entradas se ordenan por la primera columna y solo dentro de los valores iguales de la primera se ordenan por la segunda, y asi sucesivamente; es exactamente el orden de un directorio telefonico por apellido y luego nombre. De ahi la regla del prefijo mas a la izquierda: un indice sobre (estado, fecha_hora) puede resolver una busqueda por estado, y tambien una por estado junto con fecha_hora, pero NO puede resolver eficientemente una busqueda solo por fecha_hora, igual que en el directorio no se pueden encontrar todas las personas llamadas Ana sin leerlo entero. Traducido a VetCare: idx_cita_estado_fecha sirve para WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-09-01 00:00:00', sirve para WHERE estado = 'PROGRAMADA' a secas, y no sirve para la agenda del dia si esta se escribe unicamente con fecha_hora; para eso existe idx_cita_fecha. El corolario de diseno se enuncia en una linea: las columnas comparadas por igualdad van primero y la columna comparada por rango va al final, porque despues del primer rango el orden interno del indice deja de ser aprovechable. Y un numero citable que desarma la idea de crear un indice con todas las columnas por si acaso: un indice de k columnas atiende solamente los k prefijos, no las combinaciones, asi que uno de tres columnas atiende tres formas de consulta y no seis. Aqui llega la primera pregunta previsible: entonces creo (estado, fecha_hora) y tambien (fecha_hora, estado). Respuesta del docente: rara vez se justifica, porque el segundo queda casi siempre cubierto por el indice de una sola columna sobre fecha_hora mas el filtro de estado aplicado sobre las pocas filas que sobreviven, y cada indice extra se paga en cada escritura; primero se mide con el plan y despues se crea.

Cuando todas las columnas que la consulta necesita, tanto las del WHERE como las del SELECT, estan dentro del indice, el motor puede responder sin tocar la tabla, y eso se llama index-only scan o indice cubridor. Ejemplo exacto en VetCare: SELECT estado, fecha_hora FROM cita WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-09-01 00:00:00' se responde entera desde idx_cita_estado_fecha, y el plan lo dice con las palabras Index Only Scan. El ahorro es justamente la parte cara del acceso por indice: en lugar de 3 o 4 lecturas para bajar el arbol mas 110 lecturas dispersas a la tabla, quedan las 3 o 4 mas unas pocas paginas de hojas contiguas, o sea del orden de 5 lecturas contra 114. Si la consulta agrega id_mascota la ventaja se pierde, y hay dos maneras de recuperarla: agregar la columna a la clave del indice, o usar la clausula INCLUDE de PostgreSQL, CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora) INCLUDE (id_mascota), que guarda la columna en las hojas sin usarla para ordenar y por lo tanto sin engordar los niveles superiores. Oracle no tiene INCLUDE y la columna se agrega al final de la clave. Un detalle honesto que evita una confusion en vivo: en PostgreSQL el index-only scan depende del mapa de visibilidad, asi que inmediatamente despues de una carga masiva el plan puede seguir mostrando Index Scan hasta que pase VACUUM o ANALYZE, y eso no significa que el indice este mal disenado.

Un indice existente puede quedar sin usar por siete razones, y saber recitarlas es lo que separa al docente que responde del que dice que el motor es raro. Uno, la tabla es demasiado pequena: dueno con 3.000 filas cabe en unas 40 paginas y ningun indice le gana a leer 40 paginas seguidas; con las 20 filas de prueba del PI jamas se usara un indice, y el motor esta en lo correcto. Dos, el predicado no es sargable, tal como se vio en la Clase 6: UPPER(nombre), EXTRACT(YEAR FROM fecha_hora) o una conversion implicita de tipo bloquean el indice, y la salida es el indice funcional, CREATE INDEX idx_mascota_nombre_upper ON mascota (UPPER(nombre)), disponible en Oracle y PostgreSQL y ausente en las versiones antiguas de MySQL, donde se resuelve con una columna generada. Tres, la selectividad es mala: WHERE activa = 'S' devuelve el 90 % de mascota y el full scan gana con razon. Cuatro, las estadisticas estan desactualizadas y el motor cree que la tabla tiene 20 filas; se corrige con ANALYZE cita o con DBMS_STATS.GATHER_TABLE_STATS. Cinco, se violo la regla del prefijo mas a la izquierda. Seis, la condicion combina columnas de indices distintos con OR, caso en el que algunos motores arman una combinacion de mapas de bits y otros simplemente escanean. Siete, el tipo de dato o la ordenacion de la columna no coincide con lo que el predicado compara. La segunda pregunta frecuente cae justo aqui: cree el indice y el plan no cambio, entonces el indice sirve o no sirve. Respuesta: el indice puede estar bien elegido y el motor tener razon en no usarlo hoy con 20 filas; la prueba se hace con volumen, y si con 200.000 filas el plan sigue igual, entonces el problema esta en el predicado y no en el indice.

El precio de indexar se paga en cada escritura y hay que poder cuantificarlo. Un INSERT en cita con cuatro indices no es una operacion, son cinco: la fila en la tabla mas una insercion ordenada en cada arbol, cada una bajando tres niveles y a veces partiendo en dos una pagina llena, lo cual ademas fragmenta el indice. Como orden de magnitud de oficio, cada indice adicional encarece las escrituras entre un 5 % y un 15 %, y una tabla con diez indices puede escribir varias veces mas lento que la misma con dos; el numero exacto depende del motor y hay que medirlo, pero la direccion nunca cambia. El UPDATE tiene un matiz util: solo se actualizan los indices que contienen alguna de las columnas modificadas, asi que cambiar cita.estado de PROGRAMADA a ATENDIDA toca idx_cita_estado_fecha pero no idx_cita_fecha, y de ahi la advertencia de no indexar columnas que cambian en cada operacion salvo que una consulta muy frecuente lo exija. En espacio no es raro que la suma de los indices supere el tamano de la tabla. Para el entregable de hoy la guia practica es concreta: dos a cuatro indices por tabla caliente ademas de los que ya trae la clave primaria, cada uno con la consulta escrita al lado, y la regla de descarte mas util que existe, si el equipo no puede escribir la consulta que usa el indice, el indice se borra. En produccion esa decision se toma con datos y no con opinion: PostgreSQL expone pg_stat_user_indexes, donde un valor de idx_scan en cero significa que el indice nunca se uso, y Oracle permite monitorear el uso de indices; conviene mencionarlo aunque no se pueda comprobar en el playground.

El particionamiento es la otra tecnica de diseno fisico y conviene definirla sin exagerar su utilidad. Particionar es dividir una sola tabla logica en varios fragmentos fisicos llamados particiones, segun una clave, de modo que el motor descarte de entrada las particiones que no pueden contener lo buscado; ese descarte se llama poda de particiones o partition pruning. La forma mas frecuente es por rango de fechas: cita particionada por anio, con una particion para 2022, otra para 2023 y asi hasta 2026, de manera que la consulta de la agenda de septiembre de 2026 lee unicamente la particion de 2026 y el plan lo muestra. Es distinto de un indice: el indice ordena, la particion separa. El umbral en el que empieza a pagar es alto y hay que decirlo con numeros para que nadie lo use de adorno: como convencion de oficio se piensa en particionar por encima de unas decenas de millones de filas o de tablas de decenas de gigabytes, y por debajo de eso un indice sobre fecha_hora hace el mismo trabajo con muchisima menos complejidad de mantenimiento. VetCare con 200.000 citas ocupa 20 MB y cabe entero en memoria: particionar ahi no mejora nada. Entonces por que aprenderlo, que es la tercera pregunta previsible. Porque existe un caso donde no hay alternativa, el archivado: borrar cinco anios de historia con DELETE FROM cita WHERE fecha_hora < TIMESTAMP '2023-01-01 00:00:00' toca millones de filas, genera un registro de transacciones enorme y sostiene bloqueos largos, mientras ALTER TABLE cita DROP PARTITION cita_2022 lo resuelve en un instante como operacion de metadatos, y ese contraste conecta directo con la Clase 8. Sobre el playground hay buenas noticias y limites claros. En DB Fiddle con PostgreSQL si se puede demostrar practicamente todo lo de hoy, porque soporta CREATE INDEX, indices funcionales, INCLUDE y particionamiento declarativo con CREATE TABLE cita PARTITION BY RANGE (fecha_hora) y sus CREATE TABLE cita_2026 PARTITION OF cita FOR VALUES FROM ... TO ..., ademas de EXPLAIN para ver la poda; y con el generate_series de la Clase 6 se consigue el volumen necesario para que el plan cambie de Seq Scan a Index Scan, que es la evidencia antes y despues que pide el entregable. Lo que hay que documentar en papel es todo lo que depende de escala o de privilegios: el tiempo de creacion de un indice en una tabla de decenas de millones de filas, el efecto de la fragmentacion tras meses de escrituras, la degradacion medible de un INSERT con diez indices y cualquier medicion con la memoria intermedia vacia. Y hay una trampa de forma que conviene anticipar: en MySQL toda clave unica debe incluir la columna de particionamiento, asi que un DDL de particiones que funciona en PostgreSQL falla alli, y si el equipo cambio de motor a mitad del taller va a culpar al ejemplo en lugar de al motor.

Error tipico del docente que no domina el tema: crear indices sobre las columnas de las claves primarias, o sobre todas las columnas por si acaso, y presentar eso como estrategia. Duplicar el indice de la clave primaria no acelera nada y el estudiante se lleva una idea falsa de causalidad; aguas abajo, cuando en la Clase 8 su transaccion de facturacion escriba en factura, detalle_factura e insumo, no tendra manera de explicar por que la operacion se volvio mas lenta al agregar indices, y en el Parcial 2 defendera un indice sin poder nombrar la consulta que lo usa, que es exactamente lo que la rubrica evalua. El segundo error es afirmar que un indice compuesto sirve para cualquier combinacion de sus columnas, omitiendo la regla del prefijo mas a la izquierda; si eso se aprueba hoy, el equipo creara idx_cita_estado_fecha y creera cubierta la agenda del dia, la consulta seguira resolviendose con full table scan porque solo filtra por fecha_hora, y en la Clase 12, cuando la aplicacion llame al procedimiento de agenda, el diagnostico sera imposible para el grupo: el indice existe, el plan lo ignora y nadie sabe por que.


**Demo que usted debe poder repetir:** CREATE INDEX idx_cita_fecha; consulta que lo usaria.

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
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=2 indices justificados sobre tablas calientes del PI.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.
- El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.
- Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.
- Candidatos reales en VetCare: Cita(fecha_hora) para listar la agenda del dia, Mascota(id_dueno) porque cada consulta de historial parte de un dueno, DetalleFactura(id_factura) para armar el total de una factura sin escanear toda la tabla.
- Particionamiento (idea conceptual, no se implementa hoy): dividir fisicamente una tabla muy grande en fragmentos (ej. Cita por mes o por anio) para que las consultas que solo piden 'las citas de este mes' lean unicamente esa porcion, no la tabla historica completa. Es una tecnica de escala, distinta del indice, mientras el indice ordena datos, la particion los separa fisicamente en bloques.
- Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CREATE INDEX idx_cita_fecha; consulta que lo usaria.
Herramienta: DB Fiddle + draw.io (opcional)
📸 Pantallazo: [CAP: demo VetCare Clase 7]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Identificar 2 consultas frecuentes del PI.
2. Proponer y crear >=2 indices con nombre claro.
3. Justificar columna, cardinalidad y riesgo de sobre-indexar.
4. Opcional: diagrama tabla caliente -> indices en Excalidraw.
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script CREATE INDEX + tabla justificacion consulta->indice
📸 Pantallazo: [CAP: avance equipo / playground Clase 7]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 7 - VetCare.docx`. Clave para usted: `Quiz Clase 7 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: >=2 indices justificados sobre tablas calientes del PI. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 07_indices_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
