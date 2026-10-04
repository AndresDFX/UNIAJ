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


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): La clase anterior terminó con planes que decían Seq Scan: el motor leía la tabla entera porque no tenía otra forma de llegar a las filas. Hoy se construye esa otra forma, el índice, se mide cuándo sirve y cuánto cuesta, y se ve una herramienta distinta para tablas enormes: la partición.

CÓMO DARLA (≈4 min):
- Al entrar: Proyecta mentalmente el plan de la Clase 6 y pregunta: «¿por qué el motor leyó las 30.010 citas para encontrar 150?». Deja que respondan: no había otra forma de encontrarlas.
- Después: Cierra: «hoy esa línea del plan cambia, y lo vamos a demostrar con el antes y el después, no con una opinión».

PASA A LA SIGUIENTE: Empecemos por qué es exactamente un índice.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido de las dos horas: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] De donde viene la clase: los Seq Scan de la Clase 6

QUÉ ES (dilo así): Un índice es como el índice de un libro: no agrega información, repite una columna en orden y dice en qué página está cada valor. El motor lo crea a partir de la tabla, lo mantiene sincronizado solo y lo usa si le conviene. Si se borra, los datos siguen intactos; solo las consultas se vuelven más lentas.

CÓMO DARLA (≈3 min):
- Al entrar: La tabla cita con sus filas en el orden en que llegaron: el 12, el 9, el 15, el 10, el 11. Cada fila tiene su dirección física, (0,1), (0,2)…, que en PostgreSQL se llama ctid.
- Clic 1: El índice: las fechas ordenadas, cada una con la dirección de su fila. Para buscar el 2026-03-10 basta encontrar la entrada y seguir la flecha a (0,4). Lee los dos recuadros: valor + puntero; ctid o ROWID.
- Clic 2: Lee la conclusión: auxiliar, redundante y opcional. Subraya «opcional»: ninguna consulta falla si el índice no existe.

EJEMPLO: En la base de hoy, el índice sobre cita(fecha_hora) mide 256 kB frente a los 2 MB de la tabla: PostgreSQL deduplica las claves repetidas y fecha_hora tiene solo 1.810 valores distintos. Se mide con SELECT pg_size_pretty(pg_relation_size('idx_cita_fecha_hora'));

SI PREGUNTAN:
- «Si es redundante, ¿por qué no se crean índices para todo?» → Porque cada índice se actualiza en cada escritura y ocupa espacio. Se crea el que una consulta frecuente necesita; lo vemos en dos láminas.
- «¿Puedo ver el ctid?» → Sí: SELECT ctid, id_cita FROM cita LIMIT 5; muestra la dirección física de cada fila. Cambia si la fila se actualiza, así que no sirve como identificador.

CUIDADO: No digas que el índice «ordena la tabla»: la tabla queda igual; el índice es una estructura aparte.

PASA A LA SIGUIENTE: ¿Cómo encuentra el motor una clave dentro del índice sin leerlo entero? Con un árbol.

### [Slide 5] El B-Tree por dentro, en cinco minutos

QUÉ ES (dilo así): El índice por omisión en PostgreSQL, Oracle, MySQL y SQL Server es el B-Tree, un árbol balanceado. Cada nodo ocupa una página y guarda cientos de claves, así que el árbol es muy ancho y muy bajo. Encontrar una clave es bajar de la raíz a una hoja: una lectura por nivel. Duplicar la tabla casi no cambia ese número.

CÓMO DARLA (≈3 min):
- Al entrar: El árbol: raíz (50), ramas (30 y 70) y hojas con todas las claves y sus punteros. Balanceado: todas las hojas a la misma profundidad, así que ninguna búsqueda tiene suerte ni mala suerte.
- Clic 1: Buscar 60: la raíz dice «mayor que 50, a la derecha»; la rama dice «menor que 70»; la hoja 55·60 lo tiene. Tres lecturas, una por nivel.
- Clic 2: Cada nodo es una página de 8 KB. Con entradas de unos 20 bytes caben del orden de 400 claves: dos niveles cubren 160.000 filas, tres, 64 millones.

EJEMPLO: El índice de hoy sobre cita(fecha_hora) tiene 32 páginas en total: una raíz y unas 31 hojas, o sea dos niveles. Encontrar una fecha cuesta dos lecturas de índice.

SI PREGUNTAN:
- «¿Por qué sirve para BETWEEN o para ORDER BY?» → Porque las hojas están enlazadas en orden: al llegar a la primera clave del rango, el motor sigue avanzando por las hojas sin volver a la raíz.
- «¿Hay otros tipos de índice?» → Sí (hash, GIN, GiST, BRIN), pero el B-Tree es el que se usa salvo que se pida otro, y es el de hoy.

CUIDADO: No confundas «B-Tree» con «árbol binario»: cada nodo tiene cientos de hijos, no dos; por eso el árbol es tan bajo.

PASA A LA SIGUIENTE: Leer es más rápido; escribir, no. El precio se paga en cada escritura.

### [Slide 6] El precio se paga en cada escritura, y se cuantifica

QUÉ ES (dilo así): El índice acelera lecturas, pero se mantiene en cada escritura: cada INSERT agrega una entrada ordenada en cada índice de la tabla, y cada DELETE la quita. Por eso indexar tiene un costo que se paga siempre, se use o no se use el índice.

CÓMO DARLA (≈3 min):
- Al entrar: INSERT INTO cita: la fila va a la tabla y además a cada uno de los cuatro índices. Lee la frase: un INSERT con cuatro índices no es una operación, son cinco.
- Clic 1: Cuánto pesa, medido en el navegador: copiar las 30.010 citas a una tabla sin índices tardó unos 250 ms; a una con cuatro índices, unos 1.230 ms. Di que el número exacto cambia por motor y por carga, pero la dirección nunca. Cierra con la regla: se indexa lo que se consulta.

EJEMPLO: Cambiar cita.estado de PROGRAMADA a ATENDIDA actualiza idx_cita_estado_fecha, que contiene estado, pero no idx_cita_fecha_hora. Ojo: el índice parcial de las PROGRAMADA sí se toca, porque la fila sale de él.

SI PREGUNTAN:
- «¿Cuántos índices son demasiados?» → Como guía de oficio, dos a cuatro por tabla muy escrita además de la clave primaria, cada uno con su consulta escrita al lado.

CUIDADO: No prometas porcentajes exactos («cada índice cuesta un 10 %»): depende del motor y de la carga; lo honesto es medirlo.

PASA A LA SIGUIENTE: ¿Cómo se sabe qué índices existen, cuánto pesan y si alguien los usa?

### [Slide 7] El costo de sobre-indexar, que casi nunca se menciona

QUÉ ES (dilo así): PostgreSQL lleva la cuenta de cuántas veces se usó cada índice. Con esa cuenta y el tamaño se detecta el índice que se paga en cada escritura y no le sirve a nadie.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-2: el recordatorio del precio. Seis índices sobre cita son seis escrituras extra por cada cita agendada.
- Líneas 4-9: La consulta a pg_stat_user_indexes: nombre del índice, idx_scan (cuántas veces se usó) y su tamaño, ordenados del menos usado al más usado.
- Líneas 11-12: La lectura: idx_scan = 0 después de días de uso real significa que ninguna consulta lo necesita. Candidato a DROP INDEX.

EJEMPLO: En la base de hoy, idx_cita_fecha_hora mide 256 kB y idx_cita_estado_fecha 368 kB; la tabla cita, 2 MB. Con los cinco índices de la clase, los índices de cita ya suman más que la mitad de la tabla.

SI PREGUNTAN:
- «¿Por qué en el navegador idx_scan sale en 0 aunque acabo de usar el índice?» → Porque las estadísticas de uso se vuelcan con retraso y en una sesión corta casi no se acumulan. Esta consulta tiene sentido en un servidor con días de tráfico.

CUIDADO: No borres un índice por idx_scan = 0 en una base recién creada: solo dice algo después de un período de uso real.

PASA A LA SIGUIENTE: Ahora el índice de varias columnas y su regla, la fuente de error más frecuente del tema.

### [Slide 8] Indice compuesto: la regla del prefijo izquierdo

QUÉ ES (dilo así): Un índice compuesto sobre (estado, fecha_hora) se ordena como un directorio telefónico por apellido y luego por nombre: primero todas las ATENDIDA en orden de fecha, después las CANCELADA, después las PROGRAMADA. Por eso sirve para buscar por estado, o por estado y fecha; pero no para buscar solo por fecha, igual que en el directorio no se encuentran todas las Ana sin leerlo entero.

CÓMO DARLA (≈3 min):
- Al entrar: El índice idx_cita_estado_fecha: primero agrupado por estado y, dentro de cada estado, ordenado por fecha. Señala los corchetes de la derecha.
- Clic 1: Las dos consultas que empiezan por la columna líder: estado = 'PROGRAMADA' con un rango de fecha (resaltada la fila PROGRAMADA · 03-10) y estado = 'PROGRAMADA' a secas. Las dos sirven.
- Clic 2: La tercera filtra solo por fecha_hora: no hay búsqueda directa. Lee la nota: PostgreSQL 18 puede usar el índice «saltando» una vez por cada estado (skip scan), pero es un recurso del motor, no un diseño. Lee la regla.

EJEMPLO: Sin un índice que empiece por fecha_hora, una consulta solo por fecha usó idx_cita_estado_fecha con Index Searches: 7 en lugar de 1: siete búsquedas en el árbol, una por cada salto entre estados.

SI PREGUNTAN:
- «Un índice de tres columnas, ¿sirve para cualquier combinación?» → No: atiende sus prefijos (la primera; la primera y la segunda; las tres). Tres formas de consulta, no seis.
- «Entonces, ¿el skip scan hace innecesaria la regla?» → No. Solo sale barato cuando la columna líder tiene muy pocos valores, y existe desde PostgreSQL 18; en versiones anteriores ese filtro termina en Seq Scan.

CUIDADO: Decir que un índice compuesto sirve para cualquier combinación de sus columnas es el error más caro de la clase: el estudiante crea (estado, fecha_hora) y cree cubierta una consulta que solo filtra por fecha.

PASA A LA SIGUIENTE: A veces el índice basta para responder sin tocar la tabla.

### [Slide 9] Cuando el indice responde solo, sin tocar la tabla

QUÉ ES (dilo así): El acceso por índice normal tiene dos partes: buscar en el índice y luego ir a la tabla por cada fila encontrada. Si la consulta solo pide columnas que el índice ya tiene, la segunda parte sobra y el plan dice Index Only Scan. Es la forma más barata de leer.

CÓMO DARLA (≈3 min):
- Al entrar: SELECT estado, fecha_hora con filtro por estado y fecha: todo está en idx_cita_estado_fecha. El plan real: Index Only Scan using idx_cita_estado_fecha, Heap Fetches: 0, 13.187 filas.
- Clic 1: Se agrega id_mascota al SELECT: ya no está en el índice. El plan pasa a Bitmap Heap Scan: va a la tabla a buscar cada fila.
- Clic 2: La salida: CREATE INDEX idx_cita_cubridor ON cita (estado, fecha_hora) INCLUDE (id_mascota). El plan vuelve a Index Only Scan, ahora usando idx_cita_cubridor.

EJEMPLO: Con INCLUDE, las 13.187 filas salen con Heap Fetches: 0: ninguna lectura de la tabla. Oracle no tiene INCLUDE; ahí la columna se agrega al final de la clave.

SI PREGUNTAN:
- «Creé el índice y el plan dice Index Scan, no Index Only Scan. ¿Está mal?» → No necesariamente. En PostgreSQL el Index Only Scan necesita el mapa de visibilidad al día: justo después de una carga sale Index Scan hasta que corre VACUUM. En la prueba, antes del VACUUM salió Bitmap Heap Scan; después, Index Only Scan.

CUIDADO: Esto es un adelanto útil, no algo para exigir: si alguien ve Index Only Scan en su plan, que sepa qué significa.

PASA A LA SIGUIENTE: ¿Y si el índice existe y el plan no lo usa? Hay siete razones.

### [Slide 10] Las siete razones por las que un indice existente no se usa

QUÉ ES (dilo así): Que un índice exista no obliga al motor a usarlo: lo usa si le sale más barato. Hay siete razones típicas por las que no le sale, y conocerlas permite responder «¿por qué no usa mi índice?» sin decir que el motor es raro.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre la lista de arriba abajo. 1 tabla pequeña (dueno, 20 páginas); 2 función sobre la columna; 3 selectividad mala (activa = 'S' deja pasar el 94 % de mascota); 4 estadísticas viejas, resaltada porque es la más frecuente.
- Luego: 5 falta la columna líder; 6 un OR entre columnas de índices distintos; 7 el valor comparado no es del tipo de la columna.
- Abajo: El orden de revisión cuando algo no cambia: primero ANALYZE, después la columna líder, después si el predicado es sargable.

EJEMPLO: SELECT * FROM mascota WHERE activa = 'S'; sale con Seq Scan aunque hubiera índice sobre activa: devuelve 4.712 de 5.008 filas.

SI PREGUNTAN:
- «Con mis 20 filas de la Clase 1 el plan nunca usa el índice. ¿Lo hice mal?» → No: con 20 filas todo cabe en una página y leerla es lo más barato. El motor tiene razón. Por eso hoy se mide sobre 30.010 citas.

CUIDADO: No respondas «el motor es impredecible»: casi siempre es una de estas siete, y la primera que hay que revisar es el ANALYZE.

PASA A LA SIGUIENTE: Los cinco índices de hoy, cada uno con la consulta que lo justifica.

### [Slide 11] Los cinco indices, y la consulta que justifica cada uno

QUÉ ES (dilo así): Cada índice de la clase existe porque una consulta concreta lo necesita. Tres sirven para la medición del antes y el después; dos existen a propósito para demostrar que el orden de las columnas importa.

CÓMO DARLA (≈2 min):
- Al entrar: Los tres de la medición: idx_cita_fecha_hora (cualquier rango de fechas), idx_mascota_dueno (las mascotas de un dueño) e idx_cita_programada_fecha, parcial, para la agenda de recepción. A la derecha, su tamaño real.
- Abajo: Los dos del experimento: idx_cita_estado_fecha e idx_cita_fecha_estado, las mismas columnas al revés. Cierra con la línea final: PK sí trae índice, FK no.

EJEMPLO: SELECT id_mascota, nombre, especie FROM mascota WHERE id_dueno = 1234; devuelve 2 filas. Sin índice es Seq Scan sobre las 5.008 mascotas; con idx_mascota_dueno, Bitmap Index Scan on idx_mascota_dueno.

SI PREGUNTAN:
- «¿Por qué el índice sobre la FK ayuda también al borrar un dueño?» → Porque al borrar el dueño el motor tiene que verificar que ninguna mascota lo referencia; sin índice en mascota.id_dueno recorre la tabla entera.

CUIDADO: El nombre se escribe exacto: idx_cita_fecha_hora, no idx_cita_fecha. No lo dictes de memoria: cópialo de la lámina.

PASA A LA SIGUIENTE: Así se ve en código un índice justificado por su consulta.

### [Slide 12] Un indice se justifica con la consulta que lo usa

QUÉ ES (dilo así): Un índice se justifica escribiendo al lado la consulta frecuente que lo usa. Aquí, la agenda del día: siempre filtra por fecha y por estado PROGRAMADA.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-4: la consulta frecuente, la agenda del 2026-03-10 en estado PROGRAMADA: 91 filas.
- Líneas 6-8: Los dos índices que la atienden: el completo sobre fecha_hora y el parcial, que solo contiene las PROGRAMADA.
- Líneas 10-11: El mal candidato, comentado a propósito: activa solo toma 'S' o 'N' y deja pasar casi todas las filas; un índice ahí no ayuda.

EJEMPLO: Con los dos índices creados y ANALYZE, el plan de esa consulta es Bitmap Heap Scan on cita con Bitmap Index Scan on idx_cita_programada_fecha debajo: gana el parcial, y salen las 91 filas.

CUIDADO: Lee la leyenda de abajo: el nombre es el que aparece en el plan. En el navegador suele salir como «Bitmap Index Scan on <nombre>».

PASA A LA SIGUIENTE: Para demostrar que un índice sirve hay una secuencia que no se puede alterar.

### [Slide 13] La secuencia de medicion, y por que el ANALYZE del medio no es opcional

QUÉ ES (dilo así): Un índice se demuestra con un antes y un después de la misma consulta. Son cuatro pasos y en este orden: si se cambia el orden o la consulta, la comparación deja de valer.

CÓMO DARLA (≈3 min):
- Al entrar: Paso 1: EXPLAIN ANALYZE antes de crear nada. Tiene que salir Seq Scan on cita: ese es el punto de comparación.
- Clic 1: Paso 2: los CREATE INDEX, con el nombre exacto, porque ese nombre es el que imprimirá el plan.
- Clic 2: Paso 3, resaltado: ANALYZE cita; ANALYZE mascota;. Es el paso que se salta medio salón; con estadísticas viejas el planeador puede ignorar un índice perfectamente bueno.
- Clic 3: Paso 4: la misma consulta otra vez. Si se cambia una fecha o un id, ya no es la misma medición. Lee la frase final.

EJEMPLO: Agenda del 2026-03-10: antes, Seq Scan on cita con Rows Removed by Filter: 29919; después, Bitmap Heap Scan on cita con Bitmap Index Scan on idx_cita_programada_fecha debajo. Las 91 filas, iguales.

SI PREGUNTAN:
- «¿Cómo compruebo qué índices existen?» → SELECT indexname, tablename, indexdef FROM pg_indexes WHERE tablename IN ('cita','mascota') ORDER BY tablename, indexname; indexdef muestra el CREATE INDEX completo, con el WHERE del parcial.

CUIDADO: Cuando alguien diga «creé el índice y no sirvió», lo primero que se pregunta es si corrió el ANALYZE.

PASA A LA SIGUIENTE: La secuencia en código, con su salida real.

### [Slide 14] Crear el indice y probar que se usa

QUÉ ES (dilo así): La secuencia completa sobre la agenda de un día: crear los índices, actualizar estadísticas y volver a medir la misma consulta.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-4: los dos índices de una columna y los ANALYZE de las dos tablas.
- Líneas 6-9: La consulta: todas las citas del 2026-03-10 con rango semiabierto. Es la misma que se midió antes de crear nada.
- Líneas 11-13: La salida real. Antes: Seq Scan on cita, 150 filas y 29.860 descartadas. Después: Bitmap Heap Scan on cita con Bitmap Index Scan on idx_cita_fecha_hora. El nombre del índice aparece en el plan.

EJEMPLO: En una corrida en el navegador la misma consulta pasó de unos 22 ms a unos 8 ms. Lo que se afirma con seguridad es el cambio de nodo; los milisegundos varían.

SI PREGUNTAN:
- «¿Por qué Bitmap y no Index Scan?» → Es otra forma de usar el mismo índice: primero marca todas las filas que cumplen y luego visita la tabla en orden físico. El planeador la elige cuando salen decenas o cientos de filas.

CUIDADO: Si el plan no cambia, revisa en este orden: el ANALYZE, que la consulta sea exactamente la misma y que el filtro sea sargable.

PASA A LA SIGUIENTE: Con dos índices compuestos se demuestra la regla del prefijo.

### [Slide 15] El experimento del orden de columnas, paso a paso

QUÉ ES (dilo así): La regla del prefijo no se cree: se demuestra. Se crean dos índices con las mismas columnas en orden inverso y se miran tres consultas, cada una con un filtro distinto. El plan dice cuál índice le sirve a cuál.

CÓMO DARLA (≈3 min):
- Al entrar: Q1, estado por igualdad y fecha por rango: idx_cita_estado_fecha le sirve plenamente; idx_cita_fecha_estado, menos.
- Clic 1: Q2, solo rango de fecha: ahora es al revés, sirve el que empieza por fecha_hora.
- Clic 2: Q3, solo estado: idx_cita_estado_fecha sirve; el que empieza por fecha no le sirve, porque su columna líder no aparece en el filtro.
- Clic 3: La regla y el procedimiento: igualdad primero, rango al final; ANALYZE entre medición y medición, y DROP INDEX del que sobra al terminar.

EJEMPLO: En la demo, con los tres índices de la medición todavía creados, el motor del navegador eligió el parcial idx_cita_programada_fecha para Q1, idx_cita_fecha_hora para Q2 e idx_cita_estado_fecha para Q3. Con solo los dos compuestos, Q1 fue a idx_cita_estado_fecha y Q2 a idx_cita_fecha_estado.

SI PREGUNTAN:
- «¿Entonces creo los dos compuestos y listo?» → Hoy se crean los dos para medir; en producción rara vez se justifica tener ambos. Crear para medir y crear para dejar son cosas distintas.
- «Mi plan eligió otro índice. ¿Me equivoqué?» → No necesariamente: el planeador decide por costo entre índices que compiten de cerca. Se reporta lo que se vio y se explica.

CUIDADO: Si el plan del grupo no coincide con la lámina, no lo corrijas hacia la lámina: un plan distinto bien leído vale más que el esperado copiado.

PASA A LA SIGUIENTE: La misma regla sobre otro par de columnas, en código.

### [Slide 16] El orden de columnas en un indice compuesto

QUÉ ES (dilo así): La agenda de un veterinario usa igualdad en id_veterinario y rango u orden en fecha_hora. Por eso el índice va en ese orden: primero la igualdad, después el rango.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-3: el índice (id_veterinario, fecha_hora) y su ANALYZE.
- Líneas 5-9: Veterinario 5 el 2026-03-10: el Index Cond usa las DOS columnas y una sola búsqueda en el árbol (Index Searches: 1). Salen 50 citas.
- Líneas 11-13: El mismo veterinario ordenado por fecha con LIMIT 10: Index Scan using idx_cita_vet_fecha y ningún Sort, porque las hojas ya están en ese orden.
- Líneas 15-16: Sin la columna líder no hay búsqueda directa. En la prueba, sin otro índice disponible, PostgreSQL 18 lo usó saltando por cada veterinario: Index Searches: 13.

EJEMPLO: Veterinarios con citas el 2026-03-10 en la base sembrada: el 1, el 5 y el 9, con 50 citas cada uno.

SI PREGUNTAN:
- «¿Qué es Index Searches?» → Cuántas veces el motor bajó por el árbol. Una búsqueda directa da 1; un skip scan da una por cada valor de la columna líder que salta.

CUIDADO: El skip scan existe desde PostgreSQL 18; si el motor de alguien es más viejo, el filtro solo por fecha termina en Seq Scan. La regla de diseño es la misma en las dos versiones.

PASA A LA SIGUIENTE: Los nombres exactos, y dónde se leen.

### [Slide 17] Los cinco indices de hoy, con su nombre exacto

QUÉ ES (dilo así): El nombre de un índice no es decorativo: es lo que el plan imprime cuando lo usa y lo que se escribe en cualquier documento que lo justifique. Por eso se lee de la salida, no de la memoria.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba, el plan real de la agenda: Bitmap Heap Scan on cita (rows=91) y, debajo, Bitmap Index Scan on idx_cita_programada_fecha, resaltado. En un servidor también puede salir como «Index Scan using <nombre>»: es el mismo acceso por índice.
- En el medio: pg_indexes: su columna indexdef devuelve el CREATE INDEX completo. En el parcial termina en WHERE (estado = 'PROGRAMADA'::text): esa es la prueba de que se creó parcial.
- Abajo: El nombre que no es: idx_cita_fecha está tachado; el bueno es idx_cita_fecha_hora, con el sufijo de la columna.

EJEMPLO: La consulta a pg_indexes sobre cita y mascota devuelve 7 filas: los 5 índices de hoy más cita_pkey y mascota_pkey, que creó la clave primaria.

CUIDADO: Es el error que más cuesta y no es conceptual: un nombre mal copiado de la pizarra. Deja los cinco nombres proyectados mientras el grupo trabaja.

PASA A LA SIGUIENTE: Uno de los cinco es especial: el índice parcial.

### [Slide 18] El indice parcial: que indexa, cuanto ahorra y cuando gana

QUÉ ES (dilo así): Un índice parcial indexa solo una parte de la tabla: la que cumple el WHERE de su definición. Si la pantalla de recepción siempre busca citas PROGRAMADA, no tiene sentido indexar las atendidas ni las canceladas.

CÓMO DARLA (≈3 min):
- Al entrar: CREATE INDEX idx_cita_programada_fecha ON cita (fecha_hora) WHERE estado = 'PROGRAMADA'. Lee el recuadro: ese WHERE no filtra una consulta, decide qué filas entran al índice.
- Clic 1: Las barras: el índice completo indexa 30.010 entradas; el parcial, 18.187, el 61 %. Cuatro de cada diez entradas menos.
- Clic 2: El beneficio: menos disco, menos memoria y menos trabajo en las escrituras de citas que no están programadas. Y la condición para usarlo: que la consulta diga estado = 'PROGRAMADA'.

EJEMPLO: En bytes: el parcial mide 168 kB y el completo 256 kB.

SI PREGUNTAN:
- «Si la consulta pide estado IN ('PROGRAMADA', 'ATENDIDA'), ¿lo usa?» → No: el índice no tiene las atendidas, y el motor no puede arriesgarse a devolver un resultado incompleto.

CUIDADO: El error típico es leer el WHERE del CREATE INDEX como si fuera el filtro de una consulta.

PASA A LA SIGUIENTE: ¿Y cuál gana cuando el completo y el parcial compiten por la misma consulta?

### [Slide 19] El indice parcial: el mismo beneficio, una fraccion del tamano

QUÉ ES (dilo así): Con el índice completo y el parcial creados, la agenda del día tiene dos caminos. El completo encuentra todas las citas del día y luego debe descartar las que no están programadas; el parcial solo tiene programadas y va directo a las 91.

CÓMO DARLA (≈2 min):
- Al entrar: Izquierda, idx_cita_fecha_hora: 150 entradas encontradas y 59 descartadas después de ir a la tabla a leer el estado. Derecha, idx_cita_programada_fecha: 91 entradas, todas útiles, y un índice más chico.
- En el medio: El plan real: Bitmap Index Scan on idx_cita_programada_fecha (rows=91). Si en otra corrida gana el completo, se reporta lo que salió: con este volumen la diferencia de costo es pequeña.
- Abajo: La condición: la consulta tiene que traer el mismo filtro de estado.

EJEMPLO: SELECT id_cita, fecha_hora, estado FROM cita WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00' AND fecha_hora < TIMESTAMP '2026-03-11 00:00:00' AND estado = 'PROGRAMADA'; devuelve 91 filas usando el parcial.

SI PREGUNTAN:
- «¿Tener el completo y el parcial sobre la misma columna es redundante?» → No mientras haya consultas sin el filtro de estado: esas solo pueden usar el completo. Si todas filtraran por PROGRAMADA, el completo sobraría.

CUIDADO: No fuerces la respuesta «gana el parcial»: lo que se exige es leer el plan y escribir cuál salió.

PASA A LA SIGUIENTE: Cambiamos de herramienta: partir una tabla en pedazos.

### [Slide 20] Particionar: que es, y por que hoy si se implementa

QUÉ ES (dilo así): Particionar es partir una tabla en varias tablas físicas, llamadas particiones, según una clave como la fecha. Para quien consulta sigue siendo una sola tabla; el motor, al ver el filtro, descarta de entrada las particiones que no pueden tener lo buscado.

CÓMO DARLA (≈3 min):
- Al entrar: Una sola tabla lógica, cita_hist, partida en dos particiones por año: cita_hist_2025 y cita_hist_2026, cada una con su rango.
- Clic 1: Una consulta de 2026: el motor descarta cita_hist_2025 sin leerla (queda atenuada) y el plan solo nombra cita_hist_2026. Eso es la poda de particiones.
- Clic 2: La frase para recordar: el índice ordena, la partición separa.

EJEMPLO: SELECT COUNT(*) FROM cita_hist WHERE fecha_hora >= TIMESTAMP '2026-01-01'; produce un plan con Seq Scan on cita_hist_2026 y ninguna mención de cita_hist_2025.

SI PREGUNTAN:
- «¿Cuándo vale la pena particionar?» → Como convención de oficio, por encima de decenas de millones de filas o decenas de gigabytes. Por debajo, un índice sobre fecha_hora hace lo mismo con menos mantenimiento.

CUIDADO: No digas que hoy es solo teoría: hoy se implementa completo (DDL, migración, prueba de reparto y de poda). Lo que no se aprecia con este volumen es la ganancia de rendimiento.

PASA A LA SIGUIENTE: El DDL que la crea, con sus dos trampas.

### [Slide 21] El DDL de la particion, con sus dos trampas

QUÉ ES (dilo así): El DDL de una tabla particionada tiene dos trampas que dan error de una vez o, peor, más tarde. La primera es la clave primaria; la segunda, los límites de los rangos.

CÓMO DARLA (≈3 min):
- Al entrar: Las tres sentencias: CREATE TABLE cita_hist ( …, PRIMARY KEY (id_cita, fecha_hora)) PARTITION BY RANGE (fecha_hora) y las dos particiones.
- Clic 1: Trampa 1: la PK debe incluir fecha_hora. Con PRIMARY KEY (id_cita) a secas, el motor responde «unique constraint on partitioned table must include all partitioning columns».
- Clic 2: Trampa 2: FROM incluye y TO excluye. Si alguien escribe TO (TIMESTAMP '2025-12-31'), las citas del 31 de diciembre no tienen partición y el INSERT falla con «no partition of relation … found for row».

EJEMPLO: Prueba real: con la partición de 2025 cerrada en '2025-12-31', una cita del 2025-12-31 a las 10:00 fue rechazada: «no partition of relation "cita_hist" found for row».

SI PREGUNTAN:
- «¿Puedo agregar la partición de 2027 después?» → Sí: CREATE TABLE cita_hist_2027 PARTITION OF cita_hist FOR VALUES FROM (TIMESTAMP '2027-01-01') TO (TIMESTAMP '2028-01-01'); y desde ahí las citas de 2027 caen solas en ella.

CUIDADO: La trampa 2 no da error al crear la tabla, sino el día que llega una fila del hueco.

PASA A LA SIGUIENTE: El DDL completo, en código, listo para correr.

### [Slide 22] Particionar el historico por rango de fecha

QUÉ ES (dilo así): Tres sentencias: la tabla particionada, que no guarda filas, y una partición por año, que sí las guarda.

CÓMO DARLA (≈2 min):
- Al entrar: Líneas 1-8: la tabla cita_hist con PARTITION BY RANGE (fecha_hora). Subraya la línea 7: la clave primaria incluye fecha_hora, que es la clave de partición; sin eso el motor rechaza la tabla.
- Líneas 10-13: Las dos particiones con FOR VALUES FROM … TO …: 2025 y 2026.
- Línea 15: El rango: FROM incluye, TO excluye. El TO de 2025 es el FROM de 2026, así que no hay huecos ni solapes.

EJEMPLO: Después del DDL, INSERT INTO cita_hist SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado FROM cita; mueve las 30.010 citas. Como todas son de 2026, todas caen en cita_hist_2026.

SI PREGUNTAN:
- «¿Por qué la PK tiene que incluir la fecha?» → Porque PostgreSQL garantiza la unicidad dentro de cada partición; para garantizarla en toda la tabla, la clave tiene que contener la columna que decide la partición.

CUIDADO: Con PRIMARY KEY (id_cita) a secas el motor responde «unique constraint on partitioned table must include all partitioning columns»: tradúcelo en voz alta cuando aparezca.

PASA A LA SIGUIENTE: ¿Cómo se prueba que el reparto y la poda ocurrieron?

### [Slide 23] Particionar hoy de verdad: rango por ano, poda y archivado

QUÉ ES (dilo así): Particionar se demuestra con tres pruebas: dónde quedó cada fila, qué particiones lee una consulta y cuánto cuesta archivar un año. La tercera es la razón que no tiene alternativa.

CÓMO DARLA (≈2 min):
- Al entrar: Arriba, el reparto: SELECT tableoid::regclass AS particion, COUNT(*) FROM cita_hist GROUP BY 1; con la siembra de la demo devuelve una sola fila, cita_hist_2026 con 30.010, porque todas las citas son de 2026.
- En el medio: La poda: el plan de una consulta acotada a 2026 solo nombra cita_hist_2026.
- Abajo: El archivado: DROP TABLE cita_hist_2025 es una operación de metadatos y tarda un instante; DETACH PARTITION la separa sin borrarla. Sin particiones, el DELETE equivalente toca fila por fila, llena el registro de transacciones y sostiene bloqueos.

EJEMPLO: Sin filtro, SELECT COUNT(*) FROM cita_hist recorre las dos particiones (el plan muestra un Append con ambas); con el filtro de 2026, solo una.

SI PREGUNTAN:
- «Si cita_hist_2025 queda vacía, ¿se probó algo?» → Sí: que el motor envió cada fila a la partición que le corresponde. Con datos de dos años aparecerían las dos filas en el conteo.

CUIDADO: Sin la consulta de tableoid no hay evidencia del reparto: un INSERT que no dio error no prueba dónde quedaron las filas.

PASA A LA SIGUIENTE: Entonces, ¿la clínica debería particionar?

### [Slide 24] El veredicto de particionamiento

QUÉ ES (dilo así): Saber particionar no obliga a particionar. La decisión se toma con el volumen esperado al lado del umbral, y para una clínica de este tamaño el número dice que no.

CÓMO DARLA (≈2 min):
- Al entrar: La cuenta: 40 citas al día por 300 días son 12.000 al año; en cinco años, 60.000.
- En el medio: La escala va de mil a cien millones, y cada marca es diez veces la anterior. La base de hoy y la clínica a cinco años están juntas a la izquierda; el umbral, en decenas de millones, a la derecha: entre 10 millones y 60.000 hay más de 160 veces, y con 50 millones, más de 800.
- Abajo: El veredicto: no se particiona. Reconocer que con este volumen la ganancia no se aprecia es la respuesta correcta; inventar una mejora que el plan no muestra, no.

EJEMPLO: Con 60.000 citas, un índice sobre fecha_hora encuentra un día en dos o tres lecturas: no hay nada que la partición mejore en lectura.

SI PREGUNTAN:
- «Entonces, ¿para qué lo aprendimos?» → Porque el archivado no tiene alternativa en tablas grandes: un DROP de partición contra un DELETE de millones de filas. Y porque la poda se lee en el plan igual que un índice.

CUIDADO: No digas «sí conviene» para quedar bien: el número manda.

PASA A LA SIGUIENTE: Vamos a la demo, en el orden en que se proyecta.

### [Slide 25] La demo, en el orden en que se proyecta

QUÉ ES (dilo así): El script de la demo tiene cinco bloques y el orden importa: cada uno se apoya en el anterior.

CÓMO DARLA (≈1 min):
- Al entrar: Recorre los bloques de arriba abajo. El 0 recrea las tablas: se corre en una base vacía. Si el conteo de control no da 18.187, 9.095 y 2.728, se para ahí.
- Bloque 2: Es el corazón de la clase: proyecta las dos salidas, antes y después, una debajo de la otra, y lee en voz alta la línea del nodo.

EJEMPLO: En el bloque 4, como la siembra pone todas las citas en 2026, cita_hist_2025 queda vacía: igual demuestra el reparto.

CUIDADO: Si el tiempo aprieta, se recorta el bloque 3, nunca el 2.

PASA A LA SIGUIENTE: Qué se puede medir en el navegador y qué no.

### [Slide 26] Donde corre esto, y que no se puede medir aqui

QUÉ ES (dilo así): Todo lo de hoy corre en PostgreSQL dentro del navegador, con la base de 30.010 citas ya sembrada. Hay cosas que ahí no se pueden medir, y se declaran en vez de inventarlas.

CÓMO DARLA (≈1 min):
- Al entrar: Izquierda, lo que se mide y se ve en el plan; derecha, lo que no: tiempos con memoria vacía, índices sobre millones de filas, fragmentación tras meses de escrituras y dos sesiones a la vez (Clase 10). Cierra con la frase de abajo.

CUIDADO: No ofrezcas otra herramienta en línea: no tiene la base sembrada, así que ni el cambio de plan ni las 91 filas se pueden reproducir.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 27] Demo del dia

QUÉ ES (dilo así): La demo corre el script de la clase y muestra el antes y el después con planes reales: el mismo resultado, otro camino.

CÓMO DARLA (≈15 min):
- Al entrar: 1) Siembra y control. 2) Línea base: C1 (agenda del 2026-03-10, 91 filas) y C2 (mascotas del dueño 1234, 2 filas), las dos con Seq Scan. 3) Los tres CREATE INDEX, ANALYZE cita y ANALYZE mascota, y las mismas dos consultas.
- Después: 4) Lee los planes nuevos: C1 con Bitmap Index Scan on idx_cita_programada_fecha; C2 con Bitmap Index Scan on idx_mascota_dueno. 5) pg_indexes con el WHERE del parcial. 6) Si hay tiempo, el orden de columnas y la partición con su poda.

EJEMPLO: C1 antes: Seq Scan on cita, Rows Removed by Filter: 29919. C1 después: Bitmap Heap Scan on cita, Bitmap Index Scan on idx_cita_programada_fecha, 91 filas.

CUIDADO: Nunca hagas la demo sobre una base de 20 filas «porque es lo mismo»: el plan no cambia y el grupo concluye que indexar no sirve.

PASA A LA SIGUIENTE: Cierre de la clase.


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
21. El DDL de la particion, con sus dos trampas
22. Particionar el historico por rango de fecha
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
📸 El plan de C1 antes y despues: Seq Scan -> Bitmap Index Scan on idx_cita_programada_fecha [[captura: salida-indice-antes-despues.png]]
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
