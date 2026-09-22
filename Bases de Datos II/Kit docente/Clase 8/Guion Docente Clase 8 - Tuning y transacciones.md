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

**[Slide 4] Que es una transaccion, y las dos amenazas de las que protege (1/2)** — 6 vinetas.

**[Slide 5] Que es una transaccion, y las dos amenazas de las que protege (2/2)** — 5 vinetas.

**[Slide 6] Atomicidad: el fallo concreto en VetCare (1/2)** — 5 vinetas.

**[Slide 7] Atomicidad: el fallo concreto en VetCare (2/2)** — 3 vinetas.

**[Slide 8] Consistencia: valido es lo que las restricciones declaran (1/2)** — 6 vinetas.
  - Conviene notar como se combinan las dos defensas del dia: el CHECK es la red de seguridad declarativa, y el AND stock >= p_cantidad del WHERE es el guardia que evita llegar al error y permite dar un mensaje de negocio en lugar de un error de restriccion.

**[Slide 9] Consistencia: valido es lo que las restricciones declaran (2/2)** — 5 vinetas.

**[Slide 10] Aislamiento: el fallo mas facil de reproducir (1/2)** — 7 vinetas.

**[Slide 11] Aislamiento: el fallo mas facil de reproducir (2/2)** — 7 vinetas.

**[Slide 12] Durabilidad: el registro de transacciones (1/2)** — 5 vinetas.

**[Slide 13] Durabilidad: el registro de transacciones (2/2)** — 4 vinetas.

**[Slide 14] La firma de sp_facturar, y por que recibe dos arreglos (1/2)** — 8 vinetas.

**[Slide 15] La firma de sp_facturar, y por que recibe dos arreglos (2/2)** — 8 vinetas.

**[Slide 16] El guardia del stock, sentencia por sentencia (1/2)** — 7 vinetas.

**[Slide 17] El guardia del stock, sentencia por sentencia (2/2)** — 7 vinetas.

**[Slide 18] Error del motor y error de negocio: se atienden distinto (1/2)** — 8 vinetas.

**[Slide 19] Error del motor y error de negocio: se atienden distinto (2/2)** — 5 vinetas.

**[Slide 20] Donde empieza y termina la transaccion de un CALL (1/2)** — 5 vinetas.

**[Slide 21] Donde empieza y termina la transaccion de un CALL (2/2)** — 4 vinetas.

**[Slide 22] El savepoint implicito del bloque EXCEPTION (1/2)** — 8 vinetas.

**[Slide 23] El savepoint implicito del bloque EXCEPTION (2/2)** — 4 vinetas.

**[Slide 24] El contraste con Oracle, que es la pregunta 4 (1/2)** — 6 vinetas.

**[Slide 25] El contraste con Oracle, que es la pregunta 4 (2/2)** — 5 vinetas.

**[Slide 26] Abortar o informar: fn_descontar_stock (1/2)** — 8 vinetas.

**[Slide 27] Abortar o informar: fn_descontar_stock (2/2)** — 7 vinetas.

**[Slide 28] Tuning: habitos de escritura, no parametros del servidor (1/2)** — 6 vinetas.

**[Slide 29] Tuning: habitos de escritura, no parametros del servidor (2/2)** — 5 vinetas.

**[Slide 30] La demo, en el orden en que se proyecta (1/2)** — 7 vinetas.

**[Slide 31] La demo, en el orden en que se proyecta (2/2)** — 4 vinetas.

**[Slide 32] Donde corre esto, y por que el autocommit ya no es el enemigo (1/2)** — 7 vinetas.

**[Slide 33] Donde corre esto, y por que el autocommit ya no es el enemigo (2/2)** — 5 vinetas.

**[Slide 34] El reparto de los 120 minutos y como acompanar el taller (1/2)** — 8 vinetas.

**[Slide 35] El reparto de los 120 minutos y como acompanar el taller (2/2)** — 6 vinetas.

**[Slide 36] Preguntas frecuentes del grupo (1/2)** — 8 vinetas.

**[Slide 37] Preguntas frecuentes del grupo (2/2)** — 8 vinetas.


**Demo que usted debe poder repetir:** CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 8 - Tuning y transacciones/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 8 · Tuning · Transacciones · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Que es una transaccion, y las dos amenazas de las que protege (1/2)
5. Que es una transaccion, y las dos amenazas de las que protege (2/2)
6. Atomicidad: el fallo concreto en VetCare (1/2)
7. Atomicidad: el fallo concreto en VetCare (2/2)
8. Consistencia: valido es lo que las restricciones declaran (1/2)
9. Consistencia: valido es lo que las restricciones declaran (2/2)
10. Aislamiento: el fallo mas facil de reproducir (1/2)
11. Aislamiento: el fallo mas facil de reproducir (2/2)
12. Durabilidad: el registro de transacciones (1/2)
13. Durabilidad: el registro de transacciones (2/2)
14. La firma de sp_facturar, y por que recibe dos arreglos (1/2)
15. La firma de sp_facturar, y por que recibe dos arreglos (2/2)
16. El guardia del stock, sentencia por sentencia (1/2)
17. El guardia del stock, sentencia por sentencia (2/2)
18. Error del motor y error de negocio: se atienden distinto (1/2)
19. Error del motor y error de negocio: se atienden distinto (2/2)
20. Donde empieza y termina la transaccion de un CALL (1/2)
21. Donde empieza y termina la transaccion de un CALL (2/2)
22. El savepoint implicito del bloque EXCEPTION (1/2)
23. El savepoint implicito del bloque EXCEPTION (2/2)
24. El contraste con Oracle, que es la pregunta 4 (1/2)
25. El contraste con Oracle, que es la pregunta 4 (2/2)
26. Abortar o informar: fn_descontar_stock (1/2)
27. Abortar o informar: fn_descontar_stock (2/2)
28. Tuning: habitos de escritura, no parametros del servidor (1/2)
29. Tuning: habitos de escritura, no parametros del servidor (2/2)
30. La demo, en el orden en que se proyecta (1/2)
31. La demo, en el orden en que se proyecta (2/2)
32. Donde corre esto, y por que el autocommit ya no es el enemigo (1/2)
33. Donde corre esto, y por que el autocommit ya no es el enemigo (2/2)
34. El reparto de los 120 minutos y como acompanar el taller (1/2)
35. El reparto de los 120 minutos y como acompanar el taller (2/2)
36. Preguntas frecuentes del grupo (1/2)
37. Preguntas frecuentes del grupo (2/2)
38. Todo o nada: la transaccion de facturacion
39. sp_facturar en PL/pgSQL: el molde que se califica
40. Por que el procedimiento no lleva COMMIT ni ROLLBACK
41. fn_descontar_stock: cuando «no hay stock» es una respuesta, no un error
42. Demo del dia
43. Herramientas de hoy
44. Taller PI VetCare — contexto / por que importa
45. Taller PI VetCare — objetivo y criterios
46. Taller PI VetCare — escenario / datos de partida
47. Taller PI VetCare — pasos guiados
48. Taller PI VetCare — pistas (checklist vacio)
49. Criterios de exito / entregable
50. Para el PI esta semana
51. Cierre · Clase 8

> Privado, no se proyecta: `Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Transaccion de negocio (factura + stock) + notas de tuning.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde 
**Decir:** «Solo lo necesario para el entregable de hoy.»
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

### 35-55 · Demo paso a paso · [Slide 42]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: CALL sp_facturar(4, ARRAY[1,6,5], ARRAY[1,2,3]) que factura 27.400, y CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]) que falla en la segunda linea: el stock del insumo 3 vuelve a 40 sin ROLLBACK escrito.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 CALL sp_facturar que falla a mitad: foto inicial y foto final identicas, sin ROLLBACK escrito [[captura: salida-rollback-stock.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 47]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Escribir sp_facturar(p_id_consulta, p_insumos INT[], p_cantidades INT[]) en PL/pgSQL: cabecera con total 0, bucle por linea con el guardia stock >= cantidad, y UPDATE del total al final.
2. Probar el fallo a mitad con ARRAY[3,2] / ARRAY[2,10] y demostrar con foto inicial y final que el stock del insumo 3 volvio a 40.
3. Encapsular el descuento en fn_descontar_stock, que devuelve BOOLEAN y no lanza excepcion.
4. Llenar la seccion Transacciones y tuning del informe: inventario de 3 transacciones y checklist de 7 items.
5. Declarar el gap de concurrencia: PGlite corre una sola sesion, y eso es la Clase 10.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: sp_facturar + fn_descontar_stock + seccion Transacciones y tuning del informe (1 pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 8/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 49]
Repasar checklist del dia con [Slide 49] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 8 - VetCare.docx`. Clave para usted: `Quiz Clase 8 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 51]
**Decir:** «Queda avanzado: Transaccion de negocio (factura + stock) + notas de tuning. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 51] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 08_transacciones_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 8/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
