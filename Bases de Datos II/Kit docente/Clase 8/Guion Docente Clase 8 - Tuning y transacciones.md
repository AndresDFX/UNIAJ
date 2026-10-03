# Guion docente · Clase 8 · Tuning · Transacciones · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Transaccion de negocio (factura + stock) + notas de tuning
- **Entregable de hoy:** sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
- **Herramienta:** ExamLab (PostgreSQL/PGlite)
- **Slides:** Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx
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

**[Slide 4] Que es una transaccion, y las dos amenazas de las que protege (1/2)** — 5 vinetas.
  - La condicion stock >= 2 no es decoracion, es la que impide que el descuento se aplique cuando no hay existencias y hace que el motor informe cero filas afectadas en lugar de dejar un numero negativo.
  - Fuera de la lamina (habla de la practica): En PL/pgSQL, cuantas filas afecto la sentencia anterior se pregunta con GET DIAGNOSTICS v_filas = ROW_COUNT; no existe SQL%ROWCOUNT, que es de Oracle, y esa sola diferencia decide si el codigo del entregable compila o no.

**[Slide 5] Que es una transaccion, y las dos amenazas de las que protege (2/2)** — 5 vinetas.

**[Slide 6] Que es una transaccion, y las dos amenazas de... — sintaxis** — 3 vinetas.

**[Slide 7] Atomicidad: el fallo concreto en VetCare** — 4 vinetas.
  - Sin atomicidad queda una factura cobrando dos productos con una sola linea registrada, y un insumo descontado que nadie entrego.
  - Nadie recibe un error, la clinica cobro, y el dano aparece semanas despues, cuando el inventario fisico no cuadra y ya no hay forma de saber que factura lo desajusto.
  - Fuera de la lamina (habla de la practica): Esa es la razon por la que el entregable no pide tres sentencias sueltas sino un procedimiento que las agrupa, y por la que la pregunta 2 de la clase vale 25 puntos por demostrar con datos —foto inicial y foto final— que el descuento que SI habia alcanzado se deshizo.

**[Slide 8] Atomicidad: el fallo concreto en VetCare — sintaxis** — 1 vinetas.

**[Slide 9] Consistencia: valido es lo que las restricciones declaran (1/2)** — 6 vinetas.
  - Si nadie declaro la restriccion, la transaccion puede ser perfectamente atomica y dejar la base en un estado absurdo.
  - Con eso el mismo UPDATE falla con un error del motor y la transaccion se puede deshacer entera.
  - Conviene notar como se combinan las dos defensas del dia: el CHECK es la red de seguridad declarativa, y el AND stock >= p_cantidad del WHERE es el guardia que evita llegar al error y permite dar un mensaje de negocio en lugar de un error de restriccion.

**[Slide 10] Consistencia: valido es lo que las restricciones declaran (2/2)** — 4 vinetas.

**[Slide 11] Consistencia: valido es lo que las... — sintaxis** — 1 vinetas.

**[Slide 12] Aislamiento: el fallo mas facil de reproducir (1/2)** — 5 vinetas.
  - Aislamiento significa que dos transacciones concurrentes producen un resultado equivalente al que darian ejecutadas una despues de la otra.
  - Eso se llama actualizacion perdida o lost update, y la primera defensa es de diseno, no de configuracion: no leer y luego escribir con el valor leido, sino dejar que el motor haga la resta en la misma sentencia, UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3, porque esa sentencia es atomica y toma un bloqueo sobre la fila mientras se ejecuta.
  - Oracle implementa solo dos, READ COMMITTED por omision y SERIALIZABLE
  - MySQL con InnoDB usa REPEATABLE READ por omision, valor distinto que explica diferencias reales al portar un script.
  - Fuera de la lamina (habla de la practica): Esa es exactamente la decision que la pregunta 5 pide documentar en una frase defendible.

**[Slide 13] Aislamiento: el fallo mas facil de reproducir (2/2)** — 3 vinetas.

**[Slide 14] Durabilidad: el registro de transacciones (1/2)** — 4 vinetas.
  - Durabilidad significa que despues de confirmar, el dato sobrevive incluso si el servidor se apaga un segundo mas tarde.
  - Fuera de la lamina (habla de la practica): Es tambien el ultimo item del checklist de la pregunta 5, el del restore probado.

**[Slide 15] Durabilidad: el registro de transacciones (2/2)** — 3 vinetas.

**[Slide 16] La firma de sp_facturar, y por que recibe dos arreglos (1/2)** — 3 vinetas.
  - Tres observaciones.
  - Segunda, y es la que sorprende, recibe DOS ARREGLOS PARALELOS y no un insumo suelto, porque una factura real tiene varias lineas; se invoca, que significa una unidad del insumo 1, dos del 6 y tres del 5.
  - Tercera, el cuerpo va entre delimitadores de dolar, y conviene usar una etiqueta como $proc$ en lugar de $$ pelado para que no choque con otro bloque anidado.
  - El cuerpo tiene cuatro partes y vale recorrerlas en orden.
  - INTO evita ir a buscar con otro SELECT el identificador que se acaba de generar.
  - Fuera de la lamina (habla de la practica): Aqui empieza lo que se califica, y la primera cosa que hay que proyectar es la firma exacta, porque no es la que uno escribiria de memoria: CREATE PROCEDURE sp_facturar(p_id_consulta INT, p_insumos INT[], p_cantidades INT[]) LANGUAGE plpgsql AS $proc$ ... $proc$.

**[Slide 17] La firma de sp_facturar, y por que recibe dos arreglos (2/2)** — 5 vinetas.

**[Slide 18] La firma de sp_facturar, y por que recibe dos... — sintaxis** — 10 vinetas.

**[Slide 19] El guardia del stock, sentencia por sentencia (1/3)** — 4 vinetas.

**[Slide 20] El guardia del stock, sentencia por sentencia (2/3)** — 5 vinetas.

**[Slide 21] El guardia del stock, sentencia por sentencia (3/3)** — 3 vinetas.

**[Slide 22] El guardia del stock, sentencia por sentencia — sintaxis** — 7 vinetas.

**[Slide 23] Error del motor y error de negocio: se atienden distinto (1/2)** — 5 vinetas.
  - Hay que separar dos tipos de fallo a mitad de transaccion porque se atienden distinto, y esta distincion es la que ordena todo el procedimiento.
  - De ahi que el procedimiento tenga que convertir el cero filas en una excepcion, con el RAISE EXCEPTION de la seccion anterior, y de ahi tambien que el mensaje deba nombrar el insumo concreto: quien lea el error en la sustentacion tiene que poder decir cual linea fallo.
  - Hoy NO se usa.
  - Fuera de la lamina (habla de la practica): Dos exigencias del entregable salen de aqui.
  - Fuera de la lamina (habla de la practica): Hoy NO se usa, porque la regla del negocio que la actividad implementa es todo o nada, pero conviene nombrarlo para que nadie crea que la unica opcion es abortar la factura completa.

**[Slide 24] Error del motor y error de negocio: se atienden distinto (2/2)** — 3 vinetas.

**[Slide 25] Donde empieza y termina la transaccion de un CALL (1/2)** — 4 vinetas.
  - Si la excepcion se propaga hasta afuera del procedimiento, el motor deshace TODO lo que ese CALL habia hecho —la cabecera de la factura, las lineas ya insertadas y los descuentos de stock ya aplicados— y nadie escribio ROLLBACK.

**[Slide 26] Donde empieza y termina la transaccion de un CALL (2/2)** — 3 vinetas.

**[Slide 27] Donde empieza y termina la transaccion de un... — sintaxis** — 1 vinetas.

**[Slide 28] El savepoint implicito del bloque EXCEPTION (1/2)** — 6 vinetas.
  - EXCEPTION WHEN...
  - END en PL/pgSQL crea un savepoint implicito al entrar.
  - Por eso, cuando el codigo captura el error, se revierte solo lo hecho DENTRO de ese bloque y el resto de la transaccion sigue vivo.
  - El savepoint implicito de ese DO deshace todo lo que el CALL habia hecho, el mensaje se imprime, y la foto final demuestra que la base quedo igual.

**[Slide 29] El savepoint implicito del bloque EXCEPTION (2/2)** — 3 vinetas.

**[Slide 30] El savepoint implicito del bloque EXCEPTION — sintaxis** — 1 vinetas.

**[Slide 31] El contraste con Oracle, que es la pregunta 4 (1/3)** — 4 vinetas.
  - Por eso el mismo procedimiento no se traduce linea por linea entre motores: cambia quien es responsable de confirmar, y con eso cambia donde se escribe el manejo del error.
  - Fuera de la lamina (habla de la practica): La pregunta 4 vale 10 puntos y es de seleccion unica, asi que conviene que el docente sepa exactamente que se pregunta y por que las otras opciones son falsas.

**[Slide 32] El contraste con Oracle, que es la pregunta 4 (2/3)** — 4 vinetas.

**[Slide 33] El contraste con Oracle, que es la pregunta 4 (3/3)** — 3 vinetas.

**[Slide 34] Abortar o informar: fn_descontar_stock (1/2)** — 6 vinetas.
  - El procedimiento ABORTA la factura completa cuando no hay stock; la funcion INFORMA y deja que el llamador decida.
  - Lo que hay que enfatizar es la linea que separa un caso del otro: una cantidad negativa o cero no es «no hay stock», es una llamada mal hecha, y eso SI es una excepcion; el resultado negativo legitimo se devuelve como dato.
  - Eso aqui no se puede demostrar, porque el motor corre una sola sesion.
  - Fuera de la lamina (habla de la practica): Eso aqui no se puede demostrar, porque el motor corre una sola sesion, y ese es el gap que la pregunta 5 pide declarar.

**[Slide 35] Abortar o informar: fn_descontar_stock (2/2)** — 6 vinetas.

**[Slide 36] Abortar o informar: fn_descontar_stock — sintaxis** — 3 vinetas.

**[Slide 37] Tuning: habitos de escritura, no parametros del servidor (1/2)** — 5 vinetas.
  - Esos cuatro habitos, mas el de no usar SELECT asterisco en los reportes, mas los predicados sargables, mas el respaldo con restore probado.
  - Fuera de la lamina (habla de la practica): Esos cuatro habitos, mas el de no usar SELECT asterisco en los reportes, mas los predicados sargables, mas el respaldo con restore probado, son literalmente los siete items del checklist que la pregunta 5 pide llenar, y cada item exige estado Y evidencia concreta —un nombre de indice, un archivo, una consulta— porque siete casillas marcadas sin evidencia no demuestran nada.

**[Slide 38] Tuning: habitos de escritura, no parametros del servidor (2/2)** — 4 vinetas.

**[Slide 39] La demo, en el orden en que se proyecta (1/2)** — 6 vinetas.
  - Fuera de la lamina (habla de la practica): Si el tiempo aprieta, lo que se recorta es el bloque 4, que el estudiante rehace en la pregunta 3 de la clase; lo que NO se recorta es la pareja de fotos del bloque 3.

**[Slide 40] La demo, en el orden en que se proyecta (2/2)** — 5 vinetas.

**[Slide 41] La demo, en el orden en que se proyecta — sintaxis** — 3 vinetas.

**[Slide 42] Donde corre esto, y por que el autocommit ya no es el enemigo** — 5 vinetas.
  - Nada de eso corre en Oracle Live SQL.
  - Sobre el autocommit, que en versiones anteriores de este material era la advertencia central.
  - Se menciona como diferencia entre motores, no como precaucion de la clase.
  - Lo que si hay que declarar es el limite real: PGlite corre UNA SOLA sesion, asi que la espera por bloqueo, el interbloqueo, la lectura sucia y la actualizacion perdida no se pueden reproducir y se documentan en papel como una linea de tiempo de T1 y T2 con lo que ve cada una en cada paso, formato que usara la Clase 10.
  - Tampoco se demuestra la durabilidad real, porque nadie puede apagar el servidor.
  - Fuera de la lamina (habla de la practica): Las tres preguntas de SQL del dia suman 75 de los 100 puntos y son PL/pgSQL: CALL, GET DIAGNOSTICS ...
  - Fuera de la lamina (habla de la practica): Nada de eso corre en Oracle Live SQL, asi que Live SQL se queda solamente como el contraste de sintaxis de la pregunta 4.
  - Fuera de la lamina (habla de la practica): Sobre el autocommit, que en versiones anteriores de este material era la advertencia central: con la forma del entregable de hoy deja de ser un problema, y conviene explicar por que en lugar de repetir la advertencia.

**[Slide 43] Preguntas frecuentes del grupo (1/3)** — 6 vinetas.
  - Fuera de la lamina (habla de la practica): Es la pregunta 4 de la clase, y la respuesta hay que poder darla sin leer.

**[Slide 44] Preguntas frecuentes del grupo (2/3)** — 5 vinetas.

**[Slide 45] Preguntas frecuentes del grupo (3/3)** — 4 vinetas.

**[Slide 46] Todo o nada: la transaccion explicita** — 11 vinetas.

**[Slide 47] SAVEPOINT: deshacer una parte sin perder el resto** — 12 vinetas.

**[Slide 48] El bloque EXCEPTION y la trampa que cuesta puntos** — 12 vinetas.


**Demo que usted debe poder repetir:** CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 8 · Tuning · Transacciones · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es una transaccion, y las dos amenazas de las que protege (1/2)
5. Que es una transaccion, y las dos amenazas de las que protege (2/2)
6. Que es una transaccion, y las dos amenazas de... — sintaxis
7. Atomicidad: el fallo concreto en la clínica
8. Atomicidad: el fallo concreto en la clínica — sintaxis
9. Consistencia: valido es lo que las restricciones declaran (1/2)
10. Consistencia: valido es lo que las restricciones declaran (2/2)
11. Consistencia: valido es lo que las... — sintaxis
12. Aislamiento: el fallo mas facil de reproducir (1/2)
13. Aislamiento: el fallo mas facil de reproducir (2/2)
14. Durabilidad: el registro de transacciones (1/2)
15. Durabilidad: el registro de transacciones (2/2)
16. La firma de sp_facturar, y por que recibe dos arreglos (1/2)
17. La firma de sp_facturar, y por que recibe dos arreglos (2/2)
18. La firma de sp_facturar, y por que recibe dos... — sintaxis
19. El guardia del stock, sentencia por sentencia (1/3)
20. El guardia del stock, sentencia por sentencia (2/3)
21. El guardia del stock, sentencia por sentencia (3/3)
22. El guardia del stock, sentencia por sentencia — sintaxis
23. Error del motor y error de negocio: se atienden distinto (1/2)
24. Error del motor y error de negocio: se atienden distinto (2/2)
25. Donde empieza y termina la transaccion de un CALL (1/2)
26. Donde empieza y termina la transaccion de un CALL (2/2)
27. Donde empieza y termina la transaccion de un... — sintaxis
28. El savepoint implicito del bloque EXCEPTION (1/2)
29. El savepoint implicito del bloque EXCEPTION (2/2)
30. El savepoint implicito del bloque EXCEPTION — sintaxis
31. El contraste con Oracle (1/3)
32. El contraste con Oracle (2/3)
33. El contraste con Oracle (3/3)
34. Abortar o informar: fn_descontar_stock (1/2)
35. Abortar o informar: fn_descontar_stock (2/2)
36. Abortar o informar: fn_descontar_stock — sintaxis
37. Tuning: habitos de escritura, no parametros del servidor (1/2)
38. Tuning: habitos de escritura, no parametros del servidor (2/2)
39. La demo, en el orden en que se proyecta (1/2)
40. La demo, en el orden en que se proyecta (2/2)
41. La demo, en el orden en que se proyecta — sintaxis
42. Donde corre esto, y por que el autocommit ya no es el enemigo
43. Preguntas frecuentes del grupo (1/3)
44. Preguntas frecuentes del grupo (2/3)
45. Preguntas frecuentes del grupo (3/3)
46. Todo o nada: la transaccion explicita
47. SAVEPOINT: deshacer una parte sin perder el resto
48. El bloque EXCEPTION
49. Todo o nada: la transaccion de facturacion
50. sp_facturar en PL/pgSQL
51. Por que el procedimiento no lleva COMMIT ni ROLLBACK
52. fn_descontar_stock: cuando «no hay stock» es una respuesta, no un error
53. Demo del dia
54. Cierre · Clase 8

> Privado, no se proyecta: `Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Tuning · Transacciones · VetCare.»
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
- Una transaccion agrupa varias sentencias SQL en una sola unidad de todo-o-nada: si facturar implica INSERT en factura, INSERT en detalle_factura Y UPDATE de stock en insumo, las tres deben aplicarse juntas o ninguna — nunca queda una factura sin descontar stock, ni stock descontado sin factura.
- Propiedades ACID en una frase cada una: Atomicidad (todo o nada, ya explicado), Consistencia (la BD pasa de un estado valido a otro, respetando reglas como stock>=0), Aislamiento (transacciones concurrentes no se pisan entre si — se profundiza en Clase 10), Durabilidad (una vez hecho COMMIT, el dato sobrevive aunque el sistema se caiga un segundo despues).
- COMMIT confirma la transaccion de forma permanente; ROLLBACK deshace todo lo hecho desde que se abrio. En PostgreSQL no hace falta escribir ROLLBACK dentro del procedimiento: el CALL de nivel superior es su propia transaccion, y si la excepcion se propaga hasta afuera, el motor deshace todo lo que el procedimiento habia hecho. En Oracle si hay que escribirlo, y ese contraste es la pregunta 4 del taller.
- Lo que si hay que escribir es el guardia: UPDATE insumo SET stock = stock - p_cantidades[i] WHERE id_insumo = p_insumos[i] AND stock >= p_cantidades[i], y despues GET DIAGNOSTICS v_filas = ROW_COUNT. Si v_filas es 0 no hubo stock, y ahi se decide: RAISE EXCEPTION si el fallo debe abortar la factura, o devolver FALSE si el 'no hay stock' es una respuesta y no un error.
- Dirty read (lectura sucia): una transaccion lee un dato que otra transaccion modifico pero AUN NO ha confirmado con COMMIT; si esa segunda transaccion hace ROLLBACK despues, la primera trabajo con un dato que nunca existio de verdad. Es uno de los problemas que el nivel de aislamiento intenta evitar.
- Tuning en este contexto no es magia, son habitos concretos: mantener estadisticas del optimizador actualizadas (para que EXPLAIN elija bien), apoyarse en los indices ya justificados en Clase 7, y mantener las transacciones lo mas CORTAS posible — una transaccion larga retiene bloqueos (locks) sobre filas y puede frenar a otras transacciones que esperan esas mismas filas.
- Error de docente que no domina el tema: envolver TODA la sesion de trabajo en una sola transaccion gigante 'para no perder nada' — eso maximiza el tiempo que otros usuarios quedan bloqueados esperando esas filas, exactamente el problema que Clase 10 (concurrencia) va a diagnosticar.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 53]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 CALL sp_facturar que falla a mitad: foto inicial y foto final identicas, sin ROLLBACK escrito [[captura: salida-rollback-stock.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 8 - Tuning y transacciones/Taller PI - Clase 8 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Transaccion de negocio (factura + stock) + notas de tuning
Actividades:
1. Escribir sp_facturar(p_id_consulta, p_insumos INT[], p_cantidades INT[]) en PL/pgSQL: cabecera con total 0, bucle por linea con el guardia stock >= cantidad, y UPDATE del total al final.
2. Probar el fallo a mitad con ARRAY[3,2] / ARRAY[2,10] y demostrar con foto inicial y final que el stock del insumo 3 volvio a 40.
3. Encapsular el descuento en fn_descontar_stock, que devuelve BOOLEAN y no lanza excepcion.
4. Llenar la seccion Transacciones y tuning del informe: inventario de 3 transacciones y checklist de 7 items.
5. Declarar el gap de concurrencia: PGlite corre una sola sesion, y eso es la Clase 10.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 8/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 8 - VetCare.docx`. Clave para usted: `Quiz Clase 8 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 54]
**Decir:** «Queda visto: Tuning · Transacciones · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 54] slide de cierre. Dudas finales.


## Reparto del bloque y logistica (no se proyecta)

### El reparto de los 120 minutos y como acompanar el taller

El bloque de 120 minutos se reparte asi. Del minuto 0 al 10, encuadre y el amarre con la Clase 7: ayer se hizo que las consultas leyeran menos, hoy se hace que las escrituras no queden a medias. Del 10 al 30, ACID con sus cuatro fallos concretos, uno por letra, cada uno nombrando la tabla de VetCare donde ocurre; conviene no dedicar mas de cinco minutos por letra y no entrar en niveles de aislamiento mas alla de nombrarlos. Del 30 al 50, la firma del procedimiento y el guardia, sentencia por sentencia, con el codigo en pantalla. Del 50 al 60, por que no lleva COMMIT ni ROLLBACK, con el savepoint implicito y el contraste con Oracle: son los 10 puntos de la pregunta 4 y se resuelven en esta diapositiva. Del 60 al 70, la funcion y la distincion entre abortar e informar. Del 70 al 80, tuning y el checklist. Del 80 al 115, el taller. Del 115 al 120, cierre y el gancho de la Clase 10. Cuatro avisos para el acompanamiento. Uno, la pregunta 1 es la mas larga del taller y vale 35 puntos: conviene resolver en voz alta con el grupo la validacion de los arreglos y la cabecera con RETURNING, y dejar el bucle para el trabajo individual. Dos, el error de sintaxis mas frecuente es el delimitador de dolar mal cerrado; si alguien reporta un error incomprensible, lo primero que se revisa es que el $proc$ del final este igual al del principio. Tres, quien escriba COMMIT dentro del procedimiento tiene que entender por que sobra, no solo borrarlo, porque es la pregunta 4. Cuatro, la pregunta 5 son 15 puntos de prosa estructurada y se queda sin tiempo si nadie la anuncia: a los 100 minutos hay que decir en voz alta que faltan 15 y que el checklist necesita evidencias, no casillas.

## Codigo / scripts
Carpeta Codigo/ — archivo 08_transacciones_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 8/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
