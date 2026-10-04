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


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] SQL es declarativo: quien decide el como es el optimizador** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - SQL es un lenguaje declarativo: la consulta describe QUE datos se quieren y nunca COMO obtenerlos.
  - Quien decide el como es el optimizador, un componente del motor que convierte la sentencia en un plan de ejecucion
  - Es decir el arbol de operaciones fisicas que se ejecutara de verdad: que tabla se lee primero, si completa o por indice, con que algoritmo se cruzan dos tablas y donde se ordena.
  - Son tres etapas: el analizador verifica sintaxis y existencia de tablas y columnas; el optimizador genera planes candidatos, estima el costo de cada uno y elige el mas barato; el ejecutor corre el elegido.
  - Lo decisivo es que todos devuelven EXACTAMENTE el mismo resultado y pueden diferir en tiempo por factores de cien o de mil.
  - Optimizar es ayudar al optimizador a encontrar el plan bueno, no reescribir SQL por gusto estetico.
  - NOTAS:
  - El numero que hace visible el problema, y conviene decirlo con la consulta de la clase en pantalla, que cruza cuatro tablas: con tres tablas hay 6 ordenes de cruce posibles (3 factorial), con las cuatro de la agenda hay 24, con cinco 120, y al multiplicar metodos de acceso y algoritmos de cruce el espacio pasa del millar de planes; el optimizador no los prueba todos, poda con heuristicas y decide en milisegundos.

**[Slide 5] Leer un plan: es un arbol y se lee de adentro hacia afuera** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - De cada plan se leen tres cosas concretas: el nodo mas costoso, las filas estimadas frente a las reales y el tiempo total.
  - Leer un plan tiene una regla de orden que casi nadie explica: es un arbol y se lee de adentro hacia afuera, empezando por los nodos mas indentados, que son las hojas; cada nodo consume las filas de sus hijos, y la primera linea impresa es la ULTIMA operacion.
  - En PostgreSQL se escribe EXPLAIN antes de la consulta, y para la agenda de la clase aparece algo de esta forma: un Hash Join en la primera linea con su cost=... rows=... width=...
  - Y debajo, mas indentado, un Seq Scan on cita c con el filtro del dia y un Hash construido sobre un Seq Scan on mascota m.
  - Los cuatro campos hay que saber nombrarlos: cost trae el costo de arranque y el costo total separados por dos puntos; rows son las filas que el motor ESTIMA
  - Width es el ancho promedio de la fila en bytes; y loops, que solo aparece con ANALYZE, dice cuantas veces se ejecuto ese nodo.
  - El costo NO esta en milisegundos, es una unidad relativa donde 1.0 equivale por convencion a leer secuencialmente una pagina de 8 KB, y solo sirve para comparar planes del mismo motor.
  - Los tiempos reales los da EXPLAIN ANALYZE, que agrega actual time, actual rows, loops y el Execution Time del final; con la opcion BUFFERS agrega ademas cuantos bloques de 8 KB se leyeron y cuantos se acertaron en memoria
  - Que es de donde sale el numero exacto de paginas de cada tabla sin tener que estimarlo.
  - Advertencia que evita un accidente en clase: ANALYZE EJECUTA la sentencia, asi que sobre un UPDATE o un DELETE hay que envolverlo en BEGIN y ROLLBACK, lo cual ya anticipa la Clase 8.
  - Un nodo de 0,5 ms con loops=2006 cuesta un segundo entero y aparece impreso como el mas barato de la pantalla.
  - En Oracle la misma lectura son dos pasos, EXPLAIN PLAN FOR y luego SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY), que imprime Id, Operation, Name, Rows, Bytes, Cost y Time con la indentacion como jerarquia; se menciona como contraste, no como herramienta del dia.
  - NOTAS:
  - Y hay dos trampas al senalar el nodo mas costoso.
  - Fuera de la lamina (habla de la practica): El costo NO esta en milisegundos, es una unidad relativa donde 1.0 equivale por convencion a leer secuencialmente una pagina de 8 KB, y solo sirve para comparar planes del mismo motor; confundir cost con tiempo es el error mas frecuente al calificar esta pregunta.
  - Fuera de la lamina (habla de la practica): Advertencia que evita un accidente en clase: ANALYZE EJECUTA la sentencia, asi que sobre un UPDATE o un DELETE hay que envolverlo en BEGIN y ROLLBACK, lo cual ya anticipa la Clase 8; con SELECT no hay riesgo y el taller es solo de SELECT.
  - Fuera de la lamina (habla de la practica): Y hay dos trampas al senalar el nodo mas costoso, que el docente tiene que conocer antes de calificar: el tiempo que muestra un nodo INCLUYE el de sus hijos, de modo que la primera linea siempre parece la mas cara sin serlo, y actual time es POR VUELTA, asi que el costo real de un nodo es su tiempo multiplicado por loops.
  - Fuera de la lamina (habla de la practica): Un nodo de 0,5 ms con loops=2006 cuesta un segundo entero y aparece impreso como el mas barato de la pantalla; es exactamente lo que va a pasar en la pregunta 3.

**[Slide 6] EXPLAIN ANALYZE: la evidencia, no la opinion** — 11 vinetas.

**[Slide 7] Un plan, campo por campo** — 5 vinetas.

**[Slide 8] Las estadisticas: metadatos que describen los datos sin leerlos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Las estadisticas del optimizador son los metadatos que describen los datos sin leerlos: filas de la tabla, bloques que ocupa
  - Valores distintos por columna, fraccion de nulos y un histograma que reparte los valores en cubos para saber si estan parejos o concentrados.
  - PostgreSQL las recolecta con ANALYZE cita, con 100 cubos por columna por omision
  - Oracle usa DBMS_STATS.GATHER_TABLE_STATS(USER, 'CITA') y las expone en USER_TABLES.NUM_ROWS.
  - En la base de la clase el ANALYZE ya esta corrido, y eso es deliberado: si faltara.
  - De aqui sale la explicacion de un fenomeno que desconcierta: la misma consulta, sin cambiar una letra, puede tener hoy un plan distinto al de ayer
  - Porque la tabla crecio, porque se recolectaron estadisticas nuevas, porque alguien creo un indice o porque el valor comparado cambio la selectividad estimada.
  - El plan no es propiedad del texto SQL, es una decision tomada con la informacion disponible en ese instante.
  - Correlacionados quiere decir que el motor multiplica las selectividades de dos filtros como si fueran independientes y no lo son: en la clínica
  - Fecha_hora del 2026-03-10 y estado = 'PROGRAMADA' no lo son, porque el reparto de estados no es igual en todos los dias.
  - NOTAS:
  - De ahi que se comparen rows estimadas contra actual rows.
  - Conviene marcar la diferencia de palabras en voz alta, porque van a aparecer las dos hoy: predicados correlacionados es esto, un asunto de estimacion; subconsulta correlacionada.
  - Fuera de la lamina (habla de la practica): En la base de la clase el ANALYZE ya esta corrido, y eso es deliberado: si faltara, el estimado contra real de la pregunta 2 saldria disparatado por una razon que no es el tema de la clase y el estudiante concluiria lo contrario de lo que hay que aprender.
  - Fuera de la lamina (habla de la practica): De ahi que se comparen rows estimadas contra actual rows, que es literalmente una de las tres columnas que pide la pregunta 2: una divergencia de 2 veces es normal, una de 10 veces o mas es la senal clasica de estadisticas viejas o de predicados correlacionados, y esa es tambien la sexta afirmacion de la pregunta 4, que es correcta.
  - Fuera de la lamina (habla de la practica): Conviene marcar la diferencia de palabras en voz alta, porque van a aparecer las dos hoy: predicados correlacionados es esto, un asunto de estimacion; subconsulta correlacionada, la de la pregunta 3, es otra cosa completamente distinta y es un asunto de numero de ejecuciones.

**[Slide 9] Cardinalidad y selectividad: por que el motor decide lo que decide** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La cardinalidad de una columna es la cantidad de valores distintos que contiene, y conviene advertir que la palabra se usa tambien para las filas que entrega un nodo del plan.
  - La selectividad de un predicado es la fraccion de filas que sobreviven al filtro, entre 0 y 1, y es lo que el optimizador calcula con las estadisticas.
  - Las cifras que hay que usar son las de la base de la clase, no unas inventadas
  - Porque el estudiante las va a ver en su pantalla: 2.006 duenos, 5.008 mascotas, 16 veterinarios y 30.010 citas repartidas entre el 2026-01-05 y el 2026-07-23, o sea 200 dias distintos con exactamente 150 citas cada uno.
  - Con eso, WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND c.fecha_hora < TIMESTAMP '2026-03-11 00:00:00' tiene selectividad 150 sobre 30.010, o sea 0,5 %: filtro excelente.
  - WHERE c.estado = 'PROGRAMADA', sobre tres valores distintos (PROGRAMADA, ATENDIDA, CANCELADA), no filtra casi nada: son 18.187 filas, el 60,6 %, porque la siembra hace CANCELADA una de cada once citas y ATENDIDA una de cada tres de las que quedan.
  - Y WHERE m.activa = 'S', con 4.712 de las 5.008 mascotas activas, tiene selectividad 0,94: no filtra nada.
  - Los dos filtros juntos dejan 91 filas de 30.010, el 0,3 %.
  - La regla practica, convencion de oficio y no regla dura, dice que por debajo del 5 % de las filas conviene el indice, entre 5 % y 20 % depende del motor, y por encima del 20 % o 25 % gana leer la tabla completa.
  - Su origen es medible: PostgreSQL valora una lectura aleatoria de pagina en 4,0 y una secuencial en 1,0 (parametros random_page_cost y seq_page_cost), y por eso la regla se enuncia en filas pero el motor decide en costos, que no es lo mismo.
  - NOTAS:
  - Dos terminos explican por que el motor decide lo que decide.
  - Fuera de la lamina (habla de la practica): Los dos filtros juntos dejan 91 filas de 30.010, el 0,3 %, y ese 91 es el numero que el estudiante tiene que ver dos veces en la pregunta 1.

**[Slide 10] Full table scan contra index scan, sin caricaturas** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un full table scan, que en PostgreSQL se imprime Seq Scan y en Oracle TABLE ACCESS FULL, lee todos los bloques de principio a fin y descarta en memoria lo que no cumple el filtro; su ventaja es que la lectura es secuencial.
  - Un index scan desciende por el indice y, por cada coincidencia, va a buscar la fila a la tabla, lo cual son lecturas dispersas.
  - Las cuentas de la base de la clase: cita con 30.010 filas de unos 60 bytes ocupa del orden de 2 MB, unas 230 a 250 paginas de 8 KB —el numero exacto lo dice el Buffers del EXPLAIN, no hace falta estimarlo—
  - Y el Seq Scan cuesta esas paginas; buscar el 2026-03-10 por un indice sobre fecha_hora costaria 2 o 3 lecturas para bajar el arbol mas una por cada una de las 150 filas del dia, unas 153 en total.
  - Aqui hay que ser honesto y es mas interesante que la caricatura: a este volumen el indice no es veinte veces mejor, es del mismo orden de magnitud
  - Y medido en la unidad del planeador —donde una pagina dispersa vale cuatro secuenciales— puede incluso salir perdiendo.
  - La ventaja del indice crece con el tamano, no con el porcentaje: si la clínica acumulara 300.000 citas, el Seq Scan pasaria a 2.400 paginas y el indice seguiria costando unas 153, y ahi si son dieciseis veces menos.
  - Sobre 20 filas todo es instantaneo y todo se resuelve con Seq Scan, porque una tabla de 20 filas ocupa una sola pagina y no hay plan mas barato que leer una pagina
  - En ese tamano la consulta pesima y la optima miden lo mismo, entre 0,02 y 0,3 milisegundos, y la diferencia se esconde en el ruido de medicion.
  - Optimizar sobre 20 filas no es optimizar: es adivinar.
  - Justamente por eso hoy no se mide sobre la base propia sino sobre una base sembrada con 30.010 citas, y por eso el script de la demo tambien las siembra: para que el docente y el estudiante midan sobre lo mismo.
  - Si alguien pide medir en su propia base, la respuesta es que primero tiene que fabricar volumen con generate_series, y que sin eso los numeros que reporte no significan nada.
  - NOTAS:
  - Con eso se explica full table scan contra index scan sin caricaturas.
  - Por eso la Clase 7 tiene que MEDIRLO y no suponerlo.
  - Y aqui esta el punto pedagogico central, que cambio de sitio y hay que decirlo bien: el problema de las 20 filas es el de la base propia del estudiante, la que cargo en la Clase 1, no el de la clase.

**[Slide 11] Predicado sargable: el antipatron que conecta con la Clase 7** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un predicado es sargable, de Search ARGument ABLE, cuando el motor puede resolverlo navegando un indice, y para eso la columna indexada debe aparecer sola a un lado de la comparacion.
  - Las dos formas no sargables estan las dos en la consulta ANTES de la clase: to_char(c.fecha_hora, 'YYYY-MM-DD') = '2026-03-10' y UPPER(c.estado) = 'PROGRAMADA'.
  - Ninguna de las dos puede usar un indice sobre esa columna, porque el indice guarda el valor tal como se escribio y el motor no puede saber, sin evaluar la funcion, cuales entradas darian ese resultado; asi que la evalua 30.010 veces, una por fila.
  - WHERE UPPER(m.nombre) = 'LUNA' es el mismo caso frente a un indice sobre mascota(nombre) y obliga a aplicar la funcion a las 5.008 filas.
  - Igual ocurre con WHERE EXTRACT(YEAR FROM c.fecha_hora) = 2026, con WHERE SUBSTR(d.telefono, 1, 3) = '300' y con la conversion implicita: si id_mascota es numerico y se escribe WHERE c.id_mascota = '10', algunos motores convierten la columna y no el literal.
  - La reescritura correcta casi siempre es un rango: WHERE c.fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND c.fecha_hora < TIMESTAMP '2026-03-11 00:00:00'.
  - Un caso mas: LIKE 'Lu%' si usa indice porque el comodin va al final, y LIKE '%una%' no, porque no hay prefijo por donde bajar el arbol.
  - Cuando la funcion es necesaria para el negocio existe la salida de la clase siguiente, el indice funcional,, que existe en PostgreSQL y en Oracle; hoy se menciona solo como adelanto, para que nadie crea que las funciones estan prohibidas en el WHERE.
  - Y hay que cerrar con la verdad incomoda, que es el mejor bono conceptual de la clase: hoy el rango tampoco evita el Seq Scan
  - Porque en esta base no hay ningun indice sobre fecha_hora; lo que gana el rango hoy es dejar de calcular la funcion 30.010 veces y darle al planeador una estimacion correcta de cuantas filas van a pasar.
  - NOTAS:
  - El caso de UPPER(c.estado) tiene una reescritura mas simple todavia y hay que decirla porque el estudiante duda: se elimina la funcion, porque el dominio ya esta normalizado por el CHECK (estado IN ('PROGRAMADA','ATENDIDA','CANCELADA')), de modo que no existe ninguna fila en minusculas que UPPER pudiera rescatar.
  - CÓDIGO CITADO (referencia):
  - CREATE INDEX idx_mascota_nombre_upper ON mascota (UPPER(nombre))
  - Fuera de la lamina (habla de la practica): El antipatron de la funcion sobre la columna merece parrafo propio porque conecta con la Clase 7 y porque es el que la pregunta 4 pone de primero.

**[Slide 12] El antipatron y su reescritura** — 12 vinetas.

**[Slide 13] Optimizar es un ANTES medible, no una opinion** — 9 vinetas.

**[Slide 14] La subconsulta correlacionada: 2.006 pasadas o una sola** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Una subconsulta es correlacionada cuando menciona una columna de la consulta exterior; si ademas esta en la lista de columnas, el motor no puede calcularla una vez y reusarla
  - Porque depende de la fila que se este mirando, asi que la ejecuta una vez por cada fila del exterior.
  - El reporte de ranking de duenos de la clase la tiene: (SELECT COUNT(*) FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota WHERE m.id_dueno = d.id_dueno) AS total_citas, con FROM dueno d.
  - Como hay 2.006 duenos, se ejecuta 2.006 veces, y cada ejecucion recorre mascota y cita completas: del orden de 70 millones de filas procesadas para producir 2.006.
  - El plan lo dice con un nodo SubPlan y con loops=2006, y loops es el unico lugar del plan donde se lee «esto se repitio»
  - Si el docente no ensena a buscar ese campo, el estudiante va a senalar como nodo mas costoso el Seq Scan de arriba, que aparece con un tiempo mayor solo porque incluye a sus hijos.
  - La reescritura es dueno LEFT JOIN mascota LEFT JOIN cita, con GROUP BY d.id_dueno, d.nombre y COUNT(c.id_cita): el SubPlan desaparece y en su lugar queda un HashAggregate sobre una sola pasada.
  - Es la unica mejora del dia que es de ordenes de magnitud, y no necesita ningun indice, porque lo que se elimino no fue un escaneo sino 2.005 escaneos.
  - Primero, COUNT(c.id_cita) y nunca COUNT(*): el LEFT JOIN fabrica una fila llena de NULL por cada dueno que no tiene citas, COUNT(*) cuenta filas y reportaria 1, y COUNT de una columna ignora los NULL y reporta 0.
  - El sintoma es exacto y se puede proyectar en treinta segundos: los duenos 2001 a 2006 de la base de la clase no tienen mascotas, asi que su respuesta correcta es 0 y con COUNT(*) dicen 1.
  - Segundo, LEFT y no INNER: el INNER JOIN es mas rapido y esta mal, porque borra del ranking a esos seis duenos y el reporte deja de cuadrar con el total de clientes de la clinica.
  - Mas rapido devolviendo otra cosa no es optimizar, y esa frase es la bisagra con la seccion siguiente.
  - Salida esperada: los dos rankings devuelven las mismas filas, los duenos sin citas aparecen con 0 en los dos, y el plan de la reescritura ya no muestra un nodo repetido 2.006 veces.
  - NOTAS:
  - Aviso operativo que hay que dar antes de que el grupo empiece, porque si no media clase recarga la pagina y pierde sus respuestas: la version ANTES de esta pregunta ejecuta 2.006 veces una consulta que recorre 30.010 filas, y en el navegador puede tardar de varios segundos a mas de un minuto.
  - No esta colgada.
  - En la demo en vivo, si el docente no quiere esperar, la variante honesta es correr la version ANTES con WHERE d.id_dueno <= 200 en el exterior, mostrar que el plan dice loops=200 y decir en voz alta que la version completa es diez veces esa; lo que no se puede hacer es saltarse la medicion y afirmar el resultado.
  - Fuera de la lamina (habla de la practica): Es la pregunta 3, otros 20 puntos, y la cuarta afirmacion de la pregunta 4 dice lo mismo.
  - Fuera de la lamina (habla de la practica): Dos detalles que valen puntos y que el docente tiene que poder justificar en el momento.

**[Slide 15] Matar la subconsulta correlacionada** — 13 vinetas.

**[Slide 16] La subconsulta correlacionada en el plan: loops** — 5 vinetas.

**[Slide 17] Optimizar no cambia el resultado, y eso se demuestra** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Correccion y tiempo son ejes independientes, y la consecuencia practica es que una version «optimizada» que devuelve algo distinto no es una optimizacion peor: no es una optimizacion.
  - Para una consulta con filtro sirve el conteo: se envuelve cada version en un SELECT COUNT(*) y se comparan los dos numeros en la misma corrida, y en la agenda del 2026-03-10 las dos tienen que decir 91.
  - Un conteo distinto no es una version mas rapida, es la respuesta equivocada.
  - La prueba va sin LIMIT, porque comparar solo las primeras 20 filas deja fuera justamente las que fallan, que son las de los duenos con cero citas.
  - EXCEPT elimina duplicados, de modo que si el conjunto puede traer filas repetidas hay que usar EXCEPT ALL o incluir la llave; en el ranking de la clase no ocurre, porque hay una fila por dueno.
  - Y no cuentan como prueba «se ve igual», «trae mas o menos lo mismo» ni mirar la primera pantalla de resultados: la equivalencia se afirma con una consulta cuyo resultado se conoce de antemano, un numero que coincide o un conjunto vacio.
  - NOTAS:
  - Y se rompe sin avisar, porque ningun motor va a lanzar un error por eso.
  - Para conjuntos completos, donde el conteo puede coincidir con filas distintas, se usa EXCEPT en los DOS sentidos, y el docente tiene que saber por que son dos: A EXCEPT B devuelve lo que esta en A y no esta en B, asi que si sale vacio todavia puede haber filas de mas en B; se corren las dos direcciones unidas con UNION ALL y se exige cero filas en total.
  - Fuera de la lamina (habla de la practica): Por eso el taller cobra la prueba dos veces, unos 6 de los 100 puntos, y hay dos formas segun lo que se compare.
  - Fuera de la lamina (habla de la practica): Tres advertencias al calificar.

**[Slide 18] Optimizar no cambia el resultado: como se prueba** — 5 vinetas.

**[Slide 19] El antes y el despues del script de la clase** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El script Codigo/06_opt_consultas.sql es autocontenido y siembra el mismo volumen que PostgreSQL en el navegador, de modo que los numeros de la demo son los que el estudiante va a ver en su pantalla
  - Empieza con dos conteos de control que conviene proyectar antes de tocar nada: 30.010 citas en total y, para el 2026-03-10, 91 PROGRAMADA, 45 ATENDIDA y 14 CANCELADA.
  - Y el cruce implicito con comas es peligroso por aritmetica, no por estilo: si alguien olvida una de las tres condiciones de union
  - El resultado no es un error sino un producto cartesiano —30.010 por 5.008 filas son mas de 150 millones— que en el navegador acaba en una pestana bloqueada.
  - ON, filtra con el rango de fecha y con la comparacion directa del estado, y ordena por c.fecha_hora.
  - La tercera sentencia de la demo agrega LIMIT 50, que es lo que la pantalla de agenda realmente necesita: el motor deja de producir filas en cuanto tiene 50, y por eso el tiempo baja aunque el plan sea el mismo.
  - El script cierra con los bloques de la subconsulta correlacionada y con las dos pruebas de equivalencia, incluido el contraejemplo de COUNT(*) contra COUNT(c.id_cita) sobre los duenos 2001 a 2006.
  - NOTAS:
  - La version ANTES es SELECT * FROM cita c, mascota m, dueno d, veterinario v con las cuatro condiciones de union en el WHERE, to_char sobre la fecha y UPPER sobre el estado, y el docente debe saber que esta mal en cada linea.
  - SELECT * arrastra todas las columnas de las cuatro tablas cuando la pantalla de agenda necesita seis, lo cual multiplica el ancho de la fila y con el la memoria de trabajo del ordenamiento.
  - Las dos funciones sobre columnas se explicaron en el parrafo del predicado sargable.
  - Hay que decir aqui, y no despues.
  - ON no acelera nada, porque PostgreSQL normaliza las dos formas al mismo plan interno; se gana legibilidad y se gana que un ON faltante salte a la vista, o sea seguridad, no milisegundos.
  - Si el docente lo presenta como una mejora de rendimiento, esta ensenando justo la opcion por la que va a descontar.
  - La version DESPUES proyecta las seis columnas, escribe los tres JOIN...
  - Filtrar temprano se llama empuje de predicados o predicate pushdown, y hay que decir con honestidad que el optimizador moderno lo hace solo casi siempre; lo que si cambia el plan es dejar de esconder el filtro donde no puede moverlo, y los dos casos clasicos son escribirlo en HAVING cuando cabia en WHERE, y ponerlo en el WHERE de un LEFT JOIN cuando corresponde al ON, lo que ademas cambia el significado de la consulta.
  - Fuera de la lamina (habla de la practica): Hay que decir aqui, y no despues, lo que la quinta afirmacion de la pregunta 4 castiga: cambiar la coma por JOIN ...
  - Fuera de la lamina (habla de la practica): El script cierra con los bloques de la subconsulta correlacionada y con las dos pruebas de equivalencia, incluido el contraejemplo de COUNT(*) contra COUNT(c.id_cita) sobre los duenos 2001 a 2006, que es medio minuto de demo y ahorra la mitad de los reclamos de la pregunta 3.

**[Slide 20] Donde se corre todo esto, y que no se puede medir aqui** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La herramienta del dia es PostgreSQL compilado para el navegador: es el unico entorno de la clase que trae las 30.010 citas ya sembradas y las estadisticas ya recolectadas.
  - La justificacion de media pagina y la matriz de cambios se escriben en Google Docs.
  - Hoy no se ofrece ningun playground externo como alterno, y conviene que lo digas asi de claro: en DB Fiddle o en cualquier otro no existe la base sembrada, de modo que quien mida ahi obtiene otros numeros.
  - Tampoco tiene sentido hoy un comparador de motores, porque el motor de hoy es uno solo.
  - Los milisegundos, ademas, cambian entre dos corridas seguidas en la misma maquina: lo que no cambia son los conteos de filas.
  - NOTAS:
  - Soporta EXPLAIN, EXPLAIN ANALYZE y la opcion BUFFERS; si en alguna maquina BUFFERS no responde.
  - Lo que hay que documentar en papel.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - Si la consulta ya devuelve el resultado correcto, para que reescribirla: correccion y costo son ejes independientes, el motor garantiza el resultado pero no el tiempo
  - Y una consulta correcta que tarda 40 segundos congela la pantalla de recepcion igual que si estuviera mal.
  - Cuanto debe bajar el tiempo para que cuente como optimizada: la evidencia no es un porcentaje sino un cambio verificable y leido del plan
  - Y hoy ese cambio es de dos clases, menos filas procesadas y menos pasadas sobre la tabla —el SubPlan con loops=2006 que se convierte en un HashAggregate—; lo que hoy NO va a pasar
  - Y hay que anticiparlo porque es la confusion mas frecuente de la clase, es que un Seq Scan se convierta en Index Scan, porque en esta base no hay ningun indice y no puede aparecer uno de la nada: eso es la Clase 7.
  - Por que la misma consulta tarda mas la primera vez: la primera ejecucion trae las paginas de disco y la segunda las encuentra en memoria, asi que se mide tres veces y se reporta la segunda o la tercera
  - Y EXPLAIN (ANALYZE, BUFFERS) muestra cuantas paginas se leyeron y cuantas se acertaron en cache.
  - Y por que el estimado no coincide con el real: siempre que la diferencia sea de dos o tres veces esta bien y no hay nada que corregir, la senal de alarma es un orden de magnitud
  - Y en esta base, con ANALYZE recien corrido, las divergencias grandes vienen de que dos filtros no son independientes y no de estadisticas viejas.
  - La clase se apoya en la Clase 4, donde se vio que un disparador corre fila por fila y encarece una carga masiva —es la misma aritmetica del loops=2006 de hoy—
  - Y entrega el testigo a la Clase 7, que crea los indices que hoy se echaron de menos, y a la Clase 8, que suma transacciones y bloqueos al mismo analisis.
  - Cuatro preguntas aparecen siempre.
  - Fuera de la lamina (habla de la practica): Soporta EXPLAIN, EXPLAIN ANALYZE y la opcion BUFFERS; si en alguna maquina BUFFERS no responde, el enunciado ya autoriza usar EXPLAIN ANALYZE a secas y declararlo en la seccion 5 de la pregunta 5, asi que eso no cuesta puntos.
  - Fuera de la lamina (habla de la practica): Hoy no se ofrece ningun playground externo como alterno, y conviene que lo digas asi de claro: en DB Fiddle o en cualquier otro no existe la base sembrada, de modo que quien mida ahi obtiene otros numeros, y la rubrica pide los del plan real -- el «Rows Removed by Filter: 29919» y las 91 filas son justo las dos anclas con las que se verifica.
  - Fuera de la lamina (habla de la practica): Un alterno que cuesta puntos no es un alterno.
  - Fuera de la lamina (habla de la practica): Lo que hay que documentar en papel, porque el entorno no lo permite y es literalmente la seccion 5 de la pregunta 5: los tiempos con la memoria intermedia vacia, ya que vaciarla exige privilegios de administrador; el comportamiento con varias sesiones compitiendo, que es la Clase 10; y cualquier comparacion por encima de unos cientos de miles de filas.
  - Fuera de la lamina (habla de la practica): Los milisegundos, ademas, cambian entre dos corridas seguidas en la misma maquina: lo que no cambia son los conteos de filas, y por eso los conteos son lo que se califica y los milisegundos solo tienen que ser coherentes entre si.


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
