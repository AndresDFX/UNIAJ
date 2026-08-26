# Guion docente · Clase 7 · Indices y particionamiento · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
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

La Clase 6 dejo al grupo mirando planes que decian Seq Scan o TABLE ACCESS FULL donde se esperaba algo mejor; hoy se construye la estructura que cambia esa linea. Un indice es una estructura de datos auxiliar, redundante y opcional, que el motor crea a partir de una o mas columnas de una tabla, mantiene ordenada por esas columnas y sincroniza automaticamente con cada cambio de los datos. Cada entrada guarda dos cosas: el valor de la clave y un puntero fisico a la fila completa, que en Oracle se llama ROWID y en PostgreSQL ctid. Los tres adjetivos de la definicion importan. Redundante: no agrega informacion nueva, duplica columnas que ya estan en la tabla, y por eso se puede borrar y volver a crear sin perder un dato. Opcional: ninguna consulta deja de funcionar si el indice no existe, solo tarda mas. Automatico: nadie escribe codigo para mantenerlo, el motor lo actualiza dentro de la misma operacion del INSERT, del UPDATE o del DELETE, y de ahi sale el costo del que habla la segunda mitad de la clase. Con las cifras de VetCare de la clase anterior, un indice sobre cita(fecha_hora) con 200.000 entradas de unos 20 a 25 bytes ocupa entre 4 y 6 MB, frente a los 20 MB de la tabla; como orden de magnitud, cada indice de una columna cuesta entre el 10 % y el 30 % del tamano de la tabla, y esa cifra es estimacion de oficio, no constante del motor.

El tipo de indice por omision en Oracle, PostgreSQL, MySQL y SQL Server es el B-Tree, arbol balanceado, y entenderlo por dentro toma cinco minutos bien invertidos. Tiene tres clases de nodos: una raiz, cero o mas niveles intermedios o de rama, y un nivel de hojas donde estan todas las claves con sus punteros. Balanceado significa que todas las hojas quedan a la misma profundidad, asi que cualquier busqueda cuesta lo mismo y no hay valores afortunados. Cada nodo ocupa una pagina, tipicamente de 8 KB, y si cada entrada pesa unos 20 bytes, en una pagina caben del orden de 400 claves; ese numero se llama grado de ramificacion o fan-out. Con 400 hijos por nodo, un arbol de un nivel cubre 400 filas, de dos niveles 160.000, de tres niveles 64 millones y de cuatro niveles mas de 25 mil millones. De ahi la afirmacion que el docente debe poder defender: tres o cuatro niveles alcanzan para tablas de millones de filas, y encontrar una fila cuesta tres o cuatro lecturas de pagina, sin importar si la tabla tiene cien mil filas o cincuenta millones. El crecimiento es logaritmico: duplicar la tabla no duplica el tiempo de busqueda, apenas lo mueve. El indice de cita con 200.000 filas tiene dos o tres niveles. Un detalle mas explica la mitad de los usos reales: las hojas estan enlazadas entre si formando una lista, de modo que al llegar a la primera clave que cumple la condicion se puede seguir avanzando en orden; por eso un B-Tree sirve para BETWEEN, para mayor que, para menor que y para devolver filas ya ordenadas sin ejecutar un ordenamiento aparte, no solo para igualdades.

En VetCare los tres indices del script de la clase son CREATE INDEX idx_cita_fecha ON cita (fecha_hora); CREATE INDEX idx_mascota_dueno ON mascota (id_dueno); y CREATE INDEX idx_cita_estado_fecha ON cita (estado, fecha_hora); Cada uno debe justificarse con la consulta concreta que lo aprovecha, y las tres son reales del PI: la agenda del dia filtra por fecha_hora, el historial entra siempre por mascota.id_dueno, y la pantalla de recepcion combina estado con un rango de fechas. Al ejecutar el CREATE INDEX el motor lee la tabla completa una vez, ordena las claves y arma el arbol; sobre 200.000 filas eso tarda uno o dos segundos, pero en una tabla real de 50 millones son minutos y la creacion normal bloquea las escrituras, razon por la cual existen CREATE INDEX CONCURRENTLY en PostgreSQL y ONLINE en Oracle. Dos hechos sobre claves evitan la mitad de los indices inutiles que se entregan en los proyectos. Primero: declarar PRIMARY KEY o UNIQUE crea automaticamente un indice unico para sostener la restriccion, asi que id_dueno en dueno, id_mascota en mascota e id_cita en cita YA tienen indice, y crear otro encima solo duplica espacio y trabajo de escritura. Un indice unico rechaza claves repetidas y por lo tanto es la restriccion misma, no solo rendimiento; uno no unico apenas acelera. Segundo, menos conocido: declarar una FOREIGN KEY NO crea indice en ninguno de los dos motores. mascota.id_dueno apunta a dueno, pero del lado de mascota no hay nada ordenado, y por eso idx_mascota_dueno si es una adicion legitima; sin el, ademas, borrar un dueno obliga a recorrer mascota completa para verificar la integridad.

Un indice compuesto es el creado sobre dos o mas columnas, y su regla de uso es la fuente de error mas frecuente del tema. Las entradas se ordenan por la primera columna y solo dentro de los valores iguales de la primera se ordenan por la segunda; es el orden de un directorio telefonico por apellido y luego nombre. De ahi la regla del prefijo mas a la izquierda: un indice sobre (estado, fecha_hora) resuelve una busqueda por estado, y una por estado junto con fecha_hora, pero NO resuelve eficientemente una busqueda solo por fecha_hora, igual que en el directorio no se pueden encontrar todas las personas llamadas Ana sin leerlo entero. En VetCare: idx_cita_estado_fecha sirve para WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-09-01 00:00:00' y para WHERE estado = 'PROGRAMADA' a secas, y no sirve para la agenda del dia si esta se escribe solo con fecha_hora; para eso existe idx_cita_fecha. El corolario de diseno cabe en una linea: las columnas comparadas por igualdad van primero y la comparada por rango va al final, porque despues del primer rango el orden interno del indice deja de ser aprovechable. Y un numero citable que desarma la idea de indexar todo por si acaso: un indice de k columnas atiende solamente los k prefijos, no las combinaciones, asi que uno de tres columnas atiende tres formas de consulta y no seis. Aqui llega la primera pregunta previsible: entonces creo (estado, fecha_hora) y tambien (fecha_hora, estado). Respuesta: rara vez se justifica, porque el segundo queda casi siempre cubierto por el indice de una sola columna sobre fecha_hora mas el filtro de estado aplicado sobre las pocas filas que sobreviven, y cada indice extra se paga en cada escritura; primero se mide con el plan y despues se crea.

Cuando todas las columnas que la consulta necesita, las del WHERE y las del SELECT, estan dentro del indice, el motor responde sin tocar la tabla, y eso se llama index-only scan o indice cubridor. Ejemplo exacto: SELECT estado, fecha_hora FROM cita WHERE estado = 'PROGRAMADA' AND fecha_hora >= TIMESTAMP '2026-09-01 00:00:00' se responde entera desde idx_cita_estado_fecha, y el plan lo dice con las palabras Index Only Scan. El ahorro es justamente la parte cara del acceso por indice: en lugar de 3 o 4 lecturas para bajar el arbol mas 110 lecturas dispersas a la tabla, quedan unas 5 lecturas de hojas contiguas. Si la consulta agrega id_mascota la ventaja se pierde, y hay dos maneras de recuperarla: agregar la columna a la clave, o usar la clausula INCLUDE de PostgreSQL, CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora) INCLUDE (id_mascota), que guarda la columna en las hojas sin usarla para ordenar y por lo tanto sin engordar los niveles superiores; Oracle no tiene INCLUDE y la columna se agrega al final de la clave. Un detalle honesto que evita una confusion en vivo: en PostgreSQL el index-only scan depende del mapa de visibilidad, asi que inmediatamente despues de una carga masiva el plan puede seguir mostrando Index Scan hasta que pase VACUUM o ANALYZE, y eso no significa que el indice este mal disenado.

Un indice existente puede quedar sin usar por siete razones, y recitarlas separa al docente que responde del que dice que el motor es raro. Uno, la tabla es demasiado pequena: dueno con 3.000 filas cabe en unas 40 paginas y ningun indice le gana a leer 40 paginas seguidas; con las 20 filas de prueba del PI jamas se usara un indice y el motor esta en lo correcto. Dos, el predicado no es sargable, como se vio en la Clase 6: UPPER(nombre), EXTRACT(YEAR FROM fecha_hora) o una conversion implicita de tipo bloquean el indice, y la salida es el indice funcional, CREATE INDEX idx_mascota_nombre_upper ON mascota (UPPER(nombre)), disponible en Oracle y PostgreSQL y ausente en versiones antiguas de MySQL, donde se resuelve con una columna generada. Tres, la selectividad es mala: WHERE activa = 'S' devuelve el 90 % de mascota y el full scan gana con razon. Cuatro, las estadisticas estan viejas y el motor cree que la tabla tiene 20 filas; se corrige con ANALYZE cita o DBMS_STATS.GATHER_TABLE_STATS. Cinco, se violo el prefijo mas a la izquierda. Seis, la condicion combina columnas de indices distintos con OR, caso en el que algunos motores arman una combinacion de mapas de bits y otros simplemente escanean. Siete, el tipo de dato o la ordenacion no coincide con lo que el predicado compara. La segunda pregunta frecuente cae aqui: cree el indice y el plan no cambio, entonces sirve o no sirve. Respuesta: el indice puede estar bien elegido y el motor tener razon en no usarlo hoy con 20 filas; la prueba se hace con volumen, y si con 200.000 filas el plan sigue igual, el problema esta en el predicado y no en el indice.

El precio de indexar se paga en cada escritura y hay que cuantificarlo. Un INSERT en cita con cuatro indices no es una operacion, son cinco: la fila en la tabla mas una insercion ordenada en cada arbol, cada una bajando tres niveles y a veces partiendo en dos una pagina llena, lo que ademas fragmenta el indice. Como orden de magnitud de oficio, cada indice adicional encarece las escrituras entre un 5 % y un 15 %, y una tabla con diez indices puede escribir varias veces mas lento que la misma con dos; el numero exacto depende del motor y hay que medirlo, pero la direccion nunca cambia. El UPDATE tiene un matiz util: solo se actualizan los indices que contienen alguna columna modificada, asi que cambiar cita.estado de PROGRAMADA a ATENDIDA toca idx_cita_estado_fecha pero no idx_cita_fecha, de donde sale la advertencia de no indexar columnas que cambian en cada operacion salvo que una consulta muy frecuente lo exija. En espacio, no es raro que la suma de los indices supere el tamano de la tabla. Para el entregable la guia es concreta: dos a cuatro indices por tabla caliente ademas de los que ya trae la clave primaria, cada uno con su consulta escrita al lado, y la regla de descarte mas util que existe, si el estudiante no puede escribir la consulta que usa el indice, el indice se borra. En produccion eso se decide con datos: PostgreSQL expone pg_stat_user_indexes, donde idx_scan en cero significa que el indice nunca se uso, y Oracle permite monitorear el uso de indices; conviene mencionarlo aunque no se pueda comprobar en el playground.

Particionar es dividir una sola tabla logica en fragmentos fisicos llamados particiones, segun una clave, de modo que el motor descarte de entrada las que no pueden contener lo buscado; ese descarte se llama poda de particiones o partition pruning. La forma mas frecuente es por rango de fechas: cita particionada por anio, una particion para 2022, otra para 2023 y asi hasta 2026, de manera que la consulta de septiembre de 2026 lee unicamente la particion de 2026 y el plan lo muestra. Es distinto de un indice: el indice ordena, la particion separa. El umbral en el que empieza a pagar es alto y hay que decirlo con numeros para que nadie lo use de adorno: como convencion de oficio se piensa en particionar por encima de unas decenas de millones de filas o de tablas de decenas de gigabytes, y por debajo de eso un indice sobre fecha_hora hace el mismo trabajo con mucho menos mantenimiento. VetCare con 200.000 citas ocupa 20 MB y cabe entero en memoria: particionar ahi no mejora nada. Entonces por que aprenderlo, tercera pregunta previsible. Porque hay un caso sin alternativa, el archivado: borrar cinco anios de historia con DELETE FROM cita WHERE fecha_hora < TIMESTAMP '2023-01-01 00:00:00' toca millones de filas, genera un registro de transacciones enorme y sostiene bloqueos largos, mientras ALTER TABLE cita DROP PARTITION cita_2022 lo resuelve en un instante como operacion de metadatos, contraste que conecta directo con la Clase 8. En el playground si se puede demostrar casi todo lo de hoy: DB Fiddle con PostgreSQL soporta CREATE INDEX, indices funcionales, INCLUDE, particionamiento declarativo con CREATE TABLE cita PARTITION BY RANGE (fecha_hora) y sus CREATE TABLE cita_2026 PARTITION OF cita FOR VALUES FROM ... TO ..., y EXPLAIN para ver la poda; con el generate_series de la Clase 6 se consigue el volumen que hace cambiar el plan de Seq Scan a Index Scan, que es la medicion antes y despues del entregable. Hay que documentar en papel lo que depende de escala o de privilegios: el tiempo de creacion de un indice sobre decenas de millones de filas, la fragmentacion tras meses de escrituras, la degradacion medible de un INSERT con diez indices y cualquier medicion con la memoria intermedia vacia. Y conviene anticipar una trampa de forma: en MySQL toda clave unica debe incluir la columna de particionamiento, asi que un DDL de particiones valido en PostgreSQL falla alli.

Error tipico del docente que no domina el tema: crear indices sobre las columnas de las claves primarias, o sobre todas las columnas por si acaso, y presentar eso como estrategia. Duplicar el indice de la clave primaria no acelera nada y el estudiante se lleva una idea falsa de causalidad; aguas abajo, cuando en la Clase 8 su transaccion de facturacion escriba en factura, detalle_factura e insumo, no podra explicar por que la operacion se volvio mas lenta al agregar indices, y en el Parcial 2 defendera un indice sin poder nombrar la consulta que lo usa, que es exactamente lo que la rubrica evalua. El segundo error es afirmar que un indice compuesto sirve para cualquier combinacion de sus columnas, omitiendo la regla del prefijo mas a la izquierda; si eso se aprueba hoy, el estudiante creara idx_cita_estado_fecha y creera cubierta la agenda del dia, la consulta seguira resolviendose con full table scan porque solo filtra por fecha_hora, y en la Clase 12, cuando la aplicacion llame al procedimiento de agenda, el diagnostico sera imposible para el grupo: el indice existe, el plan lo ignora y nadie sabe por que.


**Demo que usted debe poder repetir:** CREATE INDEX idx_cita_fecha; consulta que lo usaria.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 7 · Indices y particionamiento · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Un indice se justifica con la consulta que lo usa
6. Demo del dia
7. Herramientas de hoy
8. Taller PI VetCare — contexto / por que importa
9. Taller PI VetCare — objetivo y criterios
10. Taller PI VetCare — escenario / datos de partida
11. Taller PI VetCare — pasos guiados
12. Taller PI VetCare — pistas (checklist vacio)
13. Criterios de exito / entregable
14. Para el PI esta semana
15. Cierre · Clase 7

> Privado, no se proyecta: `Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=2 indices justificados sobre tablas calientes del PI.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · [Slide 4]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyectar [Slide 4] «Teoria Core (breve)». El desarrollo completo de cada punto esta
arriba, en «Fundamento teorico», dividido por diapositiva.
Cubrir:
- Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.
- El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.
- Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.
- Candidatos reales en VetCare: Cita(fecha_hora) para listar la agenda del dia, Mascota(id_dueno) porque cada consulta de historial parte de un dueno, DetalleFactura(id_factura) para armar el total de una factura sin escanear toda la tabla.
- Particionamiento (idea conceptual, no se implementa hoy): dividir fisicamente una tabla muy grande en fragmentos (ej. Cita por mes o por anio) para que las consultas que solo piden 'las citas de este mes' lean unicamente esa porcion, no la tabla historica completa. Es una tecnica de escala, distinta del indice, mientras el indice ordena datos, la particion los separa fisicamente en bloques.
- Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 6]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CREATE INDEX idx_cita_fecha; consulta que lo usaria.
Herramienta: DB Fiddle + draw.io (opcional)
📸 Salida esperada de la demo de la Clase 7 [[captura: cap01_demo.png | receta: 1) Abra DB Fiddle + draw.io (opcional) y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 7/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 11]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Identificar 2 consultas frecuentes del PI.
2. Proponer y crear >=2 indices con nombre claro.
3. Justificar columna, cardinalidad y riesgo de sobre-indexar.
4. Opcional: diagrama tabla caliente -> indices en Excalidraw.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script CREATE INDEX + tabla justificacion consulta->indice
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 7/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 13]
Repasar checklist del dia con [Slide 13] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 7 - VetCare.docx`. Clave para usted: `Quiz Clase 7 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 15]
**Decir:** «Queda avanzado: >=2 indices justificados sobre tablas calientes del PI. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 15] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 07_indices_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 7/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
