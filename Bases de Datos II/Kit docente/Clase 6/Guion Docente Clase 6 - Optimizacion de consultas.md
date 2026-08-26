# Guion docente · Clase 6 · Optimizacion de consultas · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Primera pareja de consultas antes/despues del PI
- **Entregable de hoy:** 2 consultas (antes/despues) + justificacion (media pag.)
- **Herramienta:** DB Fiddle / SQLTest.online
- **Slides:** Clases/Clase 6 - Optimizacion de consultas/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Optimizar consultas parte de entender que el motor NO ejecuta el SQL tal cual se escribe: primero lo transforma en un plan de ejecucion (que tablas leer, en que orden, con o sin indice) y ese plan es lo que realmente determina el tiempo de respuesta.
- Tres cuellos de botella clasicos: (1) SELECT * trae columnas que nadie usa y aumenta el trafico/memoria; (2) JOIN sin filtro temprano obliga a cruzar tablas completas antes de descartar filas; (3) aplicar una funcion sobre la columna en el WHERE (ej. WHERE UPPER(nombre)='LUNA') impide que el motor use un indice normal sobre esa columna (esto se llama 'no-sargable').
- Reescritura tipica: proyectar solo columnas necesarias (SELECT nombre, fecha en vez de SELECT *), aplicar el filtro mas selectivo primero (WHERE fecha >= hoy antes del JOIN si reduce mucho el conjunto), y mover comparaciones a la forma que el motor pueda usar con indice.
- EXPLAIN (o EXPLAIN PLAN segun el motor) muestra COMO el motor piensa ejecutar la consulta: si dice 'Seq Scan'/'Full Table Scan' sobre una tabla grande donde se esperaba usar un indice, esa es la senal de que algo en el WHERE o el tipo de dato esta bloqueando el uso del indice.
- Conexion con Clase 7: optimizar consultas y crear indices son las dos caras de la misma moneda — una consulta mal escrita no aprovecha ni el mejor indice, y el mejor indice no compensa una consulta que fuerza un escaneo completo.
- Error de docente que no domina el tema: pedir 'la consulta más rápida' sin definir contra que se compara (volumen de datos, indices existentes) — optimizar siempre es relativo a un antes medible, por eso el taller pide guardar la version antes Y despues, no solo la version final.

### Desarrollo del tema (para dictar sin consultar otra fuente)

SQL es un lenguaje declarativo: la consulta describe QUE datos se quieren y nunca COMO obtenerlos. Quien decide el como es el optimizador, un componente del motor que convierte la sentencia en un plan de ejecucion, es decir el arbol de operaciones fisicas que se ejecutara de verdad: que tabla se lee primero, si completa o por indice, con que algoritmo se cruzan dos tablas y donde se ordena. Son tres etapas: el analizador verifica sintaxis y existencia de tablas y columnas; el optimizador genera planes candidatos, estima el costo de cada uno y elige el mas barato; el ejecutor corre el elegido. El numero que hace visible el problema: con tres tablas hay 6 ordenes de cruce posibles (3 factorial), con cinco tablas 120, y al multiplicar metodos de acceso y algoritmos de cruce el espacio pasa del millar de planes; el optimizador no los prueba todos, poda con heuristicas y decide en milisegundos. Lo decisivo es que todos devuelven EXACTAMENTE el mismo resultado y pueden diferir en tiempo por factores de cien o de mil. Optimizar es ayudar al optimizador a encontrar el plan bueno, no reescribir SQL por gusto estetico.

Leer un plan tiene una regla de orden que casi nadie explica: es un arbol y se lee de adentro hacia afuera, empezando por los nodos mas indentados, que son las hojas; cada nodo consume las filas de sus hijos, y la primera linea impresa es la ULTIMA operacion. En PostgreSQL, el motor con mejor soporte de planes en DB Fiddle, se escribe EXPLAIN antes de la consulta, y para la agenda del PI aparece algo como Hash Join (cost=270.00..4821.50 rows=1187 width=28) y debajo, mas indentado, Seq Scan on cita c con su filtro y un Hash sobre Seq Scan on mascota m. Los tres numeros hay que saber nombrarlos: cost trae el costo de arranque y el costo total separados por dos puntos; rows son las filas que el motor ESTIMA; width es el ancho promedio de la fila en bytes. El costo NO esta en milisegundos, es una unidad relativa donde 1.0 equivale por convencion a leer secuencialmente una pagina de 8 KB, y solo sirve para comparar planes del mismo motor. Los tiempos reales los da EXPLAIN ANALYZE, que agrega actual time, actual rows y loops; advertencia que evita un accidente en clase: EJECUTA la sentencia, asi que sobre un UPDATE hay que envolverlo en BEGIN y ROLLBACK, lo cual ya anticipa la Clase 8. En Oracle son dos pasos, EXPLAIN PLAN FOR y luego SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY), que imprime Id, Operation, Name, Rows, Bytes, Cost y Time con la indentacion como jerarquia.

Las estadisticas del optimizador son los metadatos que describen los datos sin leerlos: filas de la tabla, bloques que ocupa, valores distintos por columna, fraccion de nulos y un histograma que reparte los valores en cubos para saber si estan parejos o concentrados. PostgreSQL las recolecta con ANALYZE cita, con 100 cubos por columna por omision; Oracle usa DBMS_STATS.GATHER_TABLE_STATS(USER, 'CITA') y las expone en USER_TABLES.NUM_ROWS. De aqui sale la explicacion de un fenomeno que desconcierta: la misma consulta, sin cambiar una letra, puede tener hoy un plan distinto al de ayer, porque la tabla crecio, porque se recolectaron estadisticas nuevas, porque alguien creo un indice o porque el valor comparado cambio la selectividad estimada. El plan no es propiedad del texto SQL, es una decision tomada con la informacion disponible en ese instante. De ahi que se comparen rows estimadas contra actual rows: una divergencia de 2 veces es normal, una de 10 veces o mas es la senal clasica de estadisticas viejas o de predicados correlacionados. La correlacion se muestra facil en VetCare: estado = 'PROGRAMADA' y fecha_hora >= CURRENT_DATE no son independientes, porque casi toda cita futura esta programada, pero el optimizador multiplica ambas selectividades como si lo fueran y estima 30 filas donde salen 110.

Dos terminos explican por que el motor decide lo que decide. La cardinalidad de una columna es la cantidad de valores distintos que contiene, y conviene advertir que la palabra se usa tambien para las filas que entrega un nodo del plan. La selectividad de un predicado es la fraccion de filas que sobreviven al filtro, entre 0 y 1, y es lo que el optimizador calcula con las estadisticas. Cifras verosimiles de la clinica Huellitas para poder argumentar: 3.000 filas en dueno, 8.000 en mascota, 200.000 en cita acumuladas en cinco anios, unas 110 citas por dia habil, 300 en insumo y 250.000 en detalle_factura. Con eso, WHERE c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00' AND c.fecha_hora < TIMESTAMP '2026-09-02 00:00:00' tiene selectividad 110 sobre 200.000, o sea 0,055 %: filtro excelente. WHERE c.estado = 'PROGRAMADA', sobre cuatro valores distintos (PROGRAMADA, ATENDIDA, CANCELADA, NO_ASISTIO), ronda el 25 % y en la practica peor, porque el historico esta lleno de ATENDIDA. Y WHERE m.activa = 'S', con el 90 % de las mascotas activas, tiene selectividad 0,9: no filtra nada. La regla practica, convencion de oficio y no regla dura, dice que por debajo del 5 % de las filas conviene el indice, entre 5 % y 20 % depende del motor, y por encima del 20 % o 25 % gana leer la tabla completa. Su origen es medible: PostgreSQL valora una lectura aleatoria de pagina en 4,0 y una secuencial en 1,0 (parametros random_page_cost y seq_page_cost).

Con eso se explica full table scan contra index scan sin caricaturas. Un full table scan (Seq Scan en PostgreSQL, TABLE ACCESS FULL en Oracle) lee todos los bloques de principio a fin y descarta en memoria lo que no cumple el filtro; su ventaja es que la lectura es secuencial. Un index scan desciende por el indice y, por cada coincidencia, va a buscar la fila a la tabla (TABLE ACCESS BY INDEX ROWID en Oracle), lo cual son lecturas dispersas. Las cuentas de VetCare: cita con 200.000 filas de unos 100 bytes ocupa cerca de 20 MB, unas 2.500 paginas de 8 KB, y el full scan cuesta esas 2.500 lecturas; buscar el dia de hoy por un indice sobre fecha_hora cuesta 3 o 4 lecturas para bajar el arbol mas una por cada una de las 110 filas, unas 114 en total, veinte veces menos. Pero si el filtro fuera WHERE estado = 'ATENDIDA' y devolviera 120.000 filas, el indice costaria 120.000 accesos dispersos, mucho peor que 2.500 secuenciales, y el optimizador que elige el full scan esta acertando. Aqui esta el punto pedagogico central, y el docente debe decirlo ANTES de abrir el playground: con las 20 filas de prueba cargadas en la Clase 1 todo es instantaneo y todo se resuelve con full table scan, porque una tabla de 20 filas ocupa una sola pagina y no hay plan mas barato que leer una pagina. En ese tamano la consulta pesima y la optima miden lo mismo, entre 0,02 y 0,3 milisegundos, y la diferencia se esconde en el ruido de medicion. Optimizar sobre 20 filas no es optimizar: es adivinar.

El script 06_opt_consultas.sql trae la pareja antes y despues, y el docente debe saber que esta mal en la primera: SELECT * FROM cita c, mascota m, dueno d WHERE c.id_mascota = m.id_mascota AND m.id_dueno = d.id_dueno; acumula tres defectos. SELECT * trae las cuatro columnas de dueno, las cinco de mascota y las cuatro de cita, unos 250 bytes por fila, cuando recepcion necesita cuatro columnas y unos 40 bytes: seis veces mas trafico y memoria de trabajo. No hay filtro, asi que se cruzan las 200.000 citas historicas para mostrar la agenda de un dia. Y el cruce implicito con comas es peligroso por aritmetica, no por estilo: si alguien olvida una condicion del WHERE, el resultado no es un error sino un producto cartesiano de 200.000 por 8.000 filas, 1.600 millones de filas, que en un playground acaba en tiempo de espera agotado. La version despues escribe el cruce explicito y filtra temprano: SELECT c.id_cita, c.fecha_hora, m.nombre AS mascota, d.nombre AS dueno FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota JOIN dueno d ON d.id_dueno = m.id_dueno WHERE c.fecha_hora >= TIMESTAMP '2026-09-01 00:00:00' AND c.fecha_hora < TIMESTAMP '2026-09-02 00:00:00' AND c.estado = 'PROGRAMADA'; Filtrar temprano se llama empuje de predicados o predicate pushdown. Hay que decir con honestidad que el optimizador moderno lo hace solo casi siempre, y que lo que si cambia el plan es dejar de esconder el filtro donde no puede moverlo: los dos casos clasicos son escribirlo en HAVING cuando cabia en WHERE, y ponerlo en el WHERE de un LEFT JOIN cuando corresponde al ON, lo que ademas cambia el significado de la consulta.

El tercer antipatron merece parrafo propio porque conecta con la Clase 7. Un predicado es sargable, de Search ARGument ABLE, cuando el motor puede resolverlo navegando un indice, y para eso la columna indexada debe aparecer sola a un lado de la comparacion. WHERE UPPER(m.nombre) = 'LUNA' no lo es frente a un indice sobre mascota(nombre): el indice guarda Luna tal como se escribio y el motor no puede saber, sin evaluar la funcion, cuales entradas dan LUNA, asi que la aplica a las 8.000 filas. Igual ocurre con WHERE EXTRACT(YEAR FROM c.fecha_hora) = 2026, con WHERE SUBSTR(d.telefono, 1, 3) = '300' y con la conversion implicita: si id_mascota es numerico y se escribe WHERE c.id_mascota = '10', algunos motores convierten la columna y no el literal. La reescritura correcta casi siempre es un rango: WHERE c.fecha_hora >= TIMESTAMP '2026-01-01 00:00:00' AND c.fecha_hora < TIMESTAMP '2027-01-01 00:00:00'. Un caso mas: LIKE 'Lu%' si usa indice porque el comodin va al final, y LIKE '%una%' no, porque no hay prefijo por donde bajar el arbol. Cuando la funcion es necesaria para el negocio existe la salida de la clase siguiente, el indice funcional, CREATE INDEX idx_mascota_nombre_upper ON mascota (UPPER(nombre)), en Oracle y PostgreSQL; hoy se menciona solo como adelanto, para que nadie crea que las funciones estan prohibidas en el WHERE.

Tres preguntas aparecen siempre. Si la consulta ya devuelve el resultado correcto, para que reescribirla: correccion y costo son ejes independientes, el motor garantiza el resultado pero no el tiempo, y una consulta correcta que tarda 40 segundos congela la pantalla de recepcion igual que si estuviera mal. Cuanto debe bajar el tiempo para que cuente como optimizada: la evidencia que pide el entregable no es un porcentaje sino un cambio verificable del plan, que un nodo desaparezca, que Seq Scan pase a Index Scan o que las filas procesadas bajen de 200.000 a 110; en un playground compartido, una diferencia menor al 20 % es ruido. Por que la misma consulta tarda mas la primera vez: la primera ejecucion trae las paginas de disco y la segunda las encuentra en memoria, asi que se mide tres veces y se reporta la segunda o la tercera, y en PostgreSQL EXPLAIN (ANALYZE, BUFFERS) muestra cuantas paginas se leyeron y cuantas se acertaron en cache. Sobre lo demostrable: DB Fiddle con PostgreSQL soporta EXPLAIN y EXPLAIN ANALYZE completos y permite fabricar volumen en el mismo panel, unico modo de que el tema se vea; INSERT INTO cita (id_cita, id_mascota, fecha_hora, estado) SELECT g, 1 + (g % 8000), TIMESTAMP '2022-01-01 08:00:00' + (g * INTERVAL '3 minute'), CASE WHEN g % 4 = 0 THEN 'CANCELADA' ELSE 'PROGRAMADA' END FROM generate_series(1, 200000) AS g llena 200.000 citas en pocos segundos, siempre que existan antes las 8.000 mascotas o que la demo use una tabla cita_perf sin clave foranea; en Oracle Live SQL el equivalente es SELECT LEVEL FROM dual CONNECT BY LEVEL <= 200000. Hay que documentar en papel lo que el playground no permite: los tiempos con la memoria intermedia vacia, porque vaciarla exige privilegios de administrador; el comportamiento con varias sesiones compitiendo, que es la Clase 10; y cualquier comparacion por encima de unos cientos de miles de filas, porque DB Fiddle corta la ejecucion a los pocos segundos y Live SQL limita la duracion del script. La clase se apoya en la Clase 4, donde se vio que un disparador corre fila por fila y encarece una carga masiva, y entrega el testigo a la Clase 7, que crea los indices que hoy se echaron de menos, y a la Clase 8, que suma transacciones y bloqueos al mismo analisis.

Error tipico del docente que no domina el tema: mostrar la consulta antes y la consulta despues sobre las 20 filas de prueba, celebrar que el tiempo bajo de 0,9 a 0,4 milisegundos y presentar eso como evidencia de optimizacion. Es ruido de medicion, y el estudiante aprende que optimizar es una ceremonia sin sustento; aguas abajo, en la Clase 7 justificara sus indices con opiniones en lugar de con planes, y en el Parcial 2 no sabra responder por que el motor eligio un full table scan, porque nunca vio uno justificado con numeros. El segundo error es leer el plan como una lista de pasos en el orden impreso, de arriba hacia abajo, afirmando que la primera linea es lo primero que ocurre; en realidad la primera linea es la ultima operacion y las hojas mas indentadas se ejecutan primero. Si el docente instala ese error, el estudiante interpretara al reves todos los planes del curso, creera que el cruce sucede antes de leer las tablas y llegara a la sustentacion de la Clase 15 sin poder senalar cual nodo del plan cambio gracias a su indice, que es justamente la evidencia que la rubrica pide.


**Demo que usted debe poder repetir:** Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 6 - Optimizacion de consultas/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 6 · Optimizacion de consultas · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Optimizar es un ANTES medible, no una opinion
6. Demo del dia
7. Herramientas de hoy
8. Taller PI VetCare — contexto / por que importa
9. Taller PI VetCare — objetivo y criterios
10. Taller PI VetCare — escenario / datos de partida
11. Taller PI VetCare — pasos guiados
12. Taller PI VetCare — pistas (checklist vacio)
13. Criterios de exito / entregable
14. Para el PI esta semana
15. Cierre · Clase 6

> Privado, no se proyecta: `Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Primera pareja de consultas antes/despues del PI.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · [Slide 4]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyectar [Slide 4] «Teoria Core (breve)». El desarrollo completo de cada punto esta
arriba, en «Fundamento teorico», dividido por diapositiva.
Cubrir:
- Optimizar consultas parte de entender que el motor NO ejecuta el SQL tal cual se escribe: primero lo transforma en un plan de ejecucion (que tablas leer, en que orden, con o sin indice) y ese plan es lo que realmente determina el tiempo de respuesta.
- Tres cuellos de botella clasicos: (1) SELECT * trae columnas que nadie usa y aumenta el trafico/memoria; (2) JOIN sin filtro temprano obliga a cruzar tablas completas antes de descartar filas; (3) aplicar una funcion sobre la columna en el WHERE (ej. WHERE UPPER(nombre)='LUNA') impide que el motor use un indice normal sobre esa columna (esto se llama 'no-sargable').
- Reescritura tipica: proyectar solo columnas necesarias (SELECT nombre, fecha en vez de SELECT *), aplicar el filtro mas selectivo primero (WHERE fecha >= hoy antes del JOIN si reduce mucho el conjunto), y mover comparaciones a la forma que el motor pueda usar con indice.
- EXPLAIN (o EXPLAIN PLAN segun el motor) muestra COMO el motor piensa ejecutar la consulta: si dice 'Seq Scan'/'Full Table Scan' sobre una tabla grande donde se esperaba usar un indice, esa es la senal de que algo en el WHERE o el tipo de dato esta bloqueando el uso del indice.
- Conexion con Clase 7: optimizar consultas y crear indices son las dos caras de la misma moneda — una consulta mal escrita no aprovecha ni el mejor indice, y el mejor indice no compensa una consulta que fuerza un escaneo completo.
- Error de docente que no domina el tema: pedir 'la consulta más rápida' sin definir contra que se compara (volumen de datos, indices existentes) — optimizar siempre es relativo a un antes medible, por eso el taller pide guardar la version antes Y despues, no solo la version final.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 6]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada.
Herramienta: DB Fiddle / SQLTest.online
📸 Plan de ejecucion ANTES vs DESPUES (FULL SCAN -> INDEX RANGE SCAN) [[captura: salida-explain-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 11]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Tomar 1 consulta real del PI (citas del dia / historial).
2. Escribir version antes e ineficiente o real.
3. Reescribir despues y justificar 3 cambios.
4. Guardar 06_opt_antes.sql / 06_opt_despues.sql en la carpeta del PI.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 consultas (antes/despues) + justificacion (media pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 6/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 13]
Repasar checklist del dia con [Slide 13] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 6 - VetCare.docx`. Clave para usted: `Quiz Clase 6 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 15]
**Decir:** «Queda avanzado: Primera pareja de consultas antes/despues del PI. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 15] slide de cierre. Dudas finales.


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
