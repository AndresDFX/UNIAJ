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

**[Slide 4] De donde viene la clase: los Seq Scan de la Clase 6 (1/2)** — 6 vinetas.
  - Los tres adjetivos de la definicion importan.

**[Slide 5] De donde viene la clase: los Seq Scan de la Clase 6 (2/2)** — 4 vinetas.

**[Slide 6] De donde viene la clase: los Seq Scan de la... — sintaxis** — 1 vinetas.

**[Slide 7] El B-Tree por dentro, en cinco minutos (1/2)** — 4 vinetas.
  - Balanceado significa que todas las hojas quedan a la misma profundidad, asi que cualquier busqueda cuesta lo mismo y no hay valores afortunados.
  - De ahi la afirmacion que el docente debe poder defender: tres o cuatro niveles alcanzan para tablas de millones de filas, y encontrar una fila cuesta tres o cuatro lecturas de pagina, sin importar si la tabla tiene cien mil filas o cincuenta millones.
  - Esa es exactamente la forma de la consulta C1 del taller, que pide un rango de un dia.

**[Slide 8] El B-Tree por dentro, en cinco minutos (2/2)** — 4 vinetas.

**[Slide 9] El precio se paga en cada escritura, y se cuantifica (1/3)** — 4 vinetas.

**[Slide 10] El precio se paga en cada escritura, y se cuantifica (2/3)** — 5 vinetas.

**[Slide 11] El precio se paga en cada escritura, y se cuantifica (3/3)** — 2 vinetas.

**[Slide 12] Indice compuesto: la regla del prefijo izquierdo** — 4 vinetas.
  - De ahi la regla del prefijo mas a la izquierda: un indice sobre (estado, fecha_hora) resuelve una busqueda por estado, y una por estado junto con fecha_hora, pero NO resuelve eficientemente una busqueda solo por fecha_hora, igual que en el directorio no se pueden encontrar todas las personas llamadas Ana sin leerlo entero.
  - El corolario de diseno cabe en una linea, y es la que hay que dejar escrita en la pizarra: las columnas comparadas por igualdad van primero y la comparada por rango va al final, porque despues del primer rango el orden interno del indice deja de ser aprovechable.

**[Slide 13] Cuando el indice responde solo, sin tocar la tabla (1/2)** — 4 vinetas.
  - Oracle no tiene INCLUDE y la columna se agrega al final de la clave.

**[Slide 14] Cuando el indice responde solo, sin tocar la tabla (2/2)** — 4 vinetas.

**[Slide 15] Cuando el indice responde solo, sin tocar la... — sintaxis** — 1 vinetas.

**[Slide 16] Las siete razones por las que un indice existente no se usa (1/2)** — 4 vinetas.
  - Cinco, se violo el prefijo mas a la izquierda.
  - Seis, la condicion combina columnas de indices distintos con OR, caso en el que el motor arma una combinacion de mapas de bits o simplemente escanea.
  - Siete, el tipo de dato o la ordenacion no coincide con lo que el predicado compara.

**[Slide 17] Las siete razones por las que un indice existente no se usa (2/2)** — 3 vinetas.

**[Slide 18] Los cinco nombres que se califican, y la consulta que justifica cada uno (1/3)** — 3 vinetas.
  - Aqui empieza la parte que se califica letra por letra, y conviene decirlo con esas palabras.
  - Dos hechos sobre claves evitan la mitad de los indices inutiles que se entregan en los proyectos.

**[Slide 19] Los cinco nombres que se califican, y la consulta que justifica cada uno (2/3)** — 3 vinetas.

**[Slide 20] Los cinco nombres que se califican, y la consulta que justifica cada uno (3/3)** — 2 vinetas.

**[Slide 21] La secuencia de medicion, y por que el ANALYZE del medio no es opcional (1/2)** — 4 vinetas.
  - Segundo, los CREATE INDEX.

**[Slide 22] La secuencia de medicion, y por que el ANALYZE del medio no es opcional (2/2)** — 5 vinetas.

**[Slide 23] La secuencia de medicion, y por que el... — sintaxis** — 7 vinetas.

**[Slide 24] El experimento del orden de columnas, paso a paso (1/2)** — 4 vinetas.
  - La pregunta 2 no pide creer la regla del prefijo izquierdo, pide demostrarla, y el docente tiene que poder anticipar los tres resultados.
  - Eso es la regla del prefijo izquierdo vista en vivo, y es la unica manera de que no quede como una frase que se memoriza.
  - Un plan distinto bien leido vale mas que el plan esperado copiado.

**[Slide 25] El experimento del orden de columnas, paso a paso (2/2)** — 3 vinetas.

**[Slide 26] El indice parcial: que indexa, cuanto ahorra y cuando gana (1/3)** — 4 vinetas.

**[Slide 27] El indice parcial: que indexa, cuanto ahorra y cuando gana (2/3)** — 4 vinetas.

**[Slide 28] El indice parcial: que indexa, cuanto ahorra y cuando gana (3/3)** — 3 vinetas.

**[Slide 29] El indice parcial: que indexa, cuanto ahorra... — sintaxis** — 1 vinetas.

**[Slide 30] Particionar: que es, y por que hoy si se implementa (1/2)** — 4 vinetas.
  - Ahora la advertencia importante para el docente, porque es la que ha costado puntos: eso NO significa que hoy el particionamiento sea una idea conceptual que solo se cuenta.
  - Lo que si es cierto, y hay que decirlo en la misma frase, es que con 5.010 filas la ganancia de RENDIMIENTO no es apreciable: lo que se demuestra hoy es que el motor descarta particiones enteras antes de leer, y que archivar un ano se vuelve trivial.

**[Slide 31] Particionar: que es, y por que hoy si se implementa (2/2)** — 3 vinetas.

**[Slide 32] El DDL de la particion, con sus dos trampas (1/2)** — 6 vinetas.
  - Sin esa consulta no hay evidencia del enrutamiento, solo un INSERT que no dio error, y la rubrica lo pide explicitamente.

**[Slide 33] El DDL de la particion, con sus dos trampas (2/2)** — 3 vinetas.

**[Slide 34] El DDL de la particion, con sus dos trampas — sintaxis** — 20 vinetas.

**[Slide 35] El veredicto de particionamiento que pide la pregunta 5 (1/3)** — 4 vinetas.

**[Slide 36] El veredicto de particionamiento que pide la pregunta 5 (2/3)** — 4 vinetas.

**[Slide 37] El veredicto de particionamiento que pide la pregunta 5 (3/3)** — 3 vinetas.

**[Slide 38] La demo, en el orden en que se proyecta (1/2)** — 5 vinetas.
  - El script trae cinco bloques y el orden importa.
  - Lo que no se puede hacer es medir en una base de 20 filas: el plan no va a cambiar y el grupo se va a llevar la conclusion contraria.

**[Slide 39] La demo, en el orden en que se proyecta (2/2)** — 4 vinetas.

**[Slide 40] Donde corre esto, y que no se puede medir aqui** — 4 vinetas.
  - Ahi corre la demo, ahi se resuelve el taller y ahi se califica, asi que no hay razon para trabajar en otro sitio.
  - Lo que si se puede medir aqui: el cambio de Seq Scan a Index Scan, la eleccion entre dos indices que compiten, el efecto del orden de columnas con su DROP INDEX, el particionamiento declarativo completo y la poda en el plan, y el tamano de cada indice con pg_relation_size.
  - Lo que NO se puede medir, y hay que declararlo en el informe en vez de inventarlo: los tiempos con la memoria intermedia vacia, porque vaciarla exige privilegios de administrador; el tiempo de creacion de un indice sobre decenas de millones de filas; la fragmentacion despues de meses de escrituras; la degradacion medible de un INSERT con diez indices, que necesita una carga sostenida; y cualquier cosa que exija dos sesiones simultaneas, porque PGlite corre una sola, que es el tema de la Clase 10.
  - Esa lista de limites es la seccion 5 de la pregunta 5 y vale puntos: se pierde por omitirla, no por tenerla.

**[Slide 41] El reparto de los 120 minutos y como acompanar el taller (1/2)** — 6 vinetas.
  - Tres avisos para el acompanamiento.
  - Vale la pena anunciar a mitad del taller que faltan 15 minutos y que la tabla de justificacion todavia no esta escrita.

**[Slide 42] El reparto de los 120 minutos y como acompanar el taller (2/2)** — 6 vinetas.

**[Slide 43] Preguntas frecuentes del grupo (1/3)** — 3 vinetas.

**[Slide 44] Preguntas frecuentes del grupo (2/3)** — 4 vinetas.

**[Slide 45] Preguntas frecuentes del grupo (3/3)** — 5 vinetas.


**Demo que usted debe poder repetir:** EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 7 · Indices y particionamiento · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. De donde viene la clase: los Seq Scan de la Clase 6 (1/2)
5. De donde viene la clase: los Seq Scan de la Clase 6 (2/2)
6. De donde viene la clase: los Seq Scan de la... — sintaxis
7. El B-Tree por dentro, en cinco minutos (1/2)
8. El B-Tree por dentro, en cinco minutos (2/2)
9. El precio se paga en cada escritura, y se cuantifica (1/3)
10. El precio se paga en cada escritura, y se cuantifica (2/3)
11. El precio se paga en cada escritura, y se cuantifica (3/3)
12. Indice compuesto: la regla del prefijo izquierdo
13. Cuando el indice responde solo, sin tocar la tabla (1/2)
14. Cuando el indice responde solo, sin tocar la tabla (2/2)
15. Cuando el indice responde solo, sin tocar la... — sintaxis
16. Las siete razones por las que un indice existente no se usa (1/2)
17. Las siete razones por las que un indice existente no se usa (2/2)
18. Los cinco nombres que se califican, y la consulta que justifica cada uno (1/3)
19. Los cinco nombres que se califican, y la consulta que justifica cada uno (2/3)
20. Los cinco nombres que se califican, y la consulta que justifica cada uno (3/3)
21. La secuencia de medicion, y por que el ANALYZE del medio no es opcional (1/2)
22. La secuencia de medicion, y por que el ANALYZE del medio no es opcional (2/2)
23. La secuencia de medicion, y por que el... — sintaxis
24. El experimento del orden de columnas, paso a paso (1/2)
25. El experimento del orden de columnas, paso a paso (2/2)
26. El indice parcial: que indexa, cuanto ahorra y cuando gana (1/3)
27. El indice parcial: que indexa, cuanto ahorra y cuando gana (2/3)
28. El indice parcial: que indexa, cuanto ahorra y cuando gana (3/3)
29. El indice parcial: que indexa, cuanto ahorra... — sintaxis
30. Particionar: que es, y por que hoy si se implementa (1/2)
31. Particionar: que es, y por que hoy si se implementa (2/2)
32. El DDL de la particion, con sus dos trampas (1/2)
33. El DDL de la particion, con sus dos trampas (2/2)
34. El DDL de la particion, con sus dos trampas — sintaxis
35. El veredicto de particionamiento que pide la pregunta 5 (1/3)
36. El veredicto de particionamiento que pide la pregunta 5 (2/3)
37. El veredicto de particionamiento que pide la pregunta 5 (3/3)
38. La demo, en el orden en que se proyecta (1/2)
39. La demo, en el orden en que se proyecta (2/2)
40. Donde corre esto, y que no se puede medir aqui
41. El reparto de los 120 minutos y como acompanar el taller (1/2)
42. El reparto de los 120 minutos y como acompanar el taller (2/2)
43. Preguntas frecuentes del grupo (1/3)
44. Preguntas frecuentes del grupo (2/3)
45. Preguntas frecuentes del grupo (3/3)
46. Un indice se justifica con la consulta que lo usa
47. Los cinco indices de hoy, con su nombre exacto
48. El indice parcial: el mismo beneficio, una fraccion del tamano
49. Particionar hoy de verdad: rango por ano, poda y archivado
50. Demo del dia
51. Herramientas de hoy
52. Taller PI VetCare — contexto / por que importa
53. Taller PI VetCare — objetivo y criterios
54. Taller PI VetCare — escenario / datos de partida
55. Taller PI VetCare — pasos guiados
56. Taller PI VetCare — pistas (checklist vacio)
57. Criterios de exito / entregable
58. Para el PI esta semana
59. Cierre · Clase 7

> Privado, no se proyecta: `Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: 3 indices justificados (uno parcial) + historico particionado por ano.
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
- Un indice es una estructura auxiliar (tipicamente un arbol B-Tree) que el motor mantiene ordenada por una o mas columnas, para encontrar filas sin recorrer toda la tabla — como el indice de un libro en vez de leer pagina por pagina.
- El costo no es gratis: cada INSERT/UPDATE/DELETE sobre una columna indexada obliga al motor a actualizar tambien el indice, asi que mas indices = lecturas mas rapidas pero escrituras mas lentas. Por eso 'indexar todo' es un error, no una optimizacion.
- Buen candidato a indice: columna usada muy frecuentemente en WHERE, JOIN u ORDER BY, con alta cardinalidad (muchos valores distintos, ej. id_dueno) — indexar una columna de baja cardinalidad (ej. un booleano activo S/N con solo 2 valores) rara vez ayuda porque el motor igual debe leer una fraccion enorme de la tabla.
- Candidatos reales en VetCare: cita(fecha_hora) para listar la agenda del dia, mascota(id_dueno) porque cada consulta de historial parte de un dueno, detalle_factura(id_factura) para armar el total de una factura sin escanear toda la tabla.
- Particionamiento (hoy SI se implementa, y es la pregunta 3 del taller): dividir una tabla logica en fragmentos fisicos por rango de fecha, de modo que la consulta de un ano no toque los datos del otro. PostgreSQL lo hace con PARTITION BY RANGE (fecha_hora) y una particion por ano. El indice ORDENA los datos; la particion los SEPARA.
- Con 5.010 filas la particion no acelera nada y hay que decirlo: lo que si se comprueba hoy es la poda de particiones en el plan (solo aparece cita_hist_2026) y el archivado, porque tirar un ano completo es un DROP TABLE de la particion en vez de un DELETE masivo.
- Error de docente que no domina el tema: crear un indice sobre CADA columna 'por si acaso' sin mirar que consultas realmente lo necesitan — el taller exige justificar cada indice con la consulta concreta que lo aprovecha.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 50]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 El plan de C1 antes y despues: Seq Scan -> Index Scan using idx_cita_programada_fecha [[captura: salida-indice-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 55]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Medir la linea base con EXPLAIN ANALYZE de las dos consultas frecuentes: hay que ver Seq Scan.
2. Crear los tres indices con el nombre exacto, incluido el parcial idx_cita_programada_fecha, y correr ANALYZE.
3. Repetir los EXPLAIN y decir cual indice eligio el planeador y por que.
4. Construir cita_hist particionada por ano, migrar las citas y demostrar el enrutamiento y la poda.
5. Llenar la tabla de justificacion consulta->indice (7 columnas) y el veredicto de particionamiento.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Script CREATE INDEX + cita_hist particionada + tabla justificacion consulta->indice
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 7/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 57]
Repasar checklist del dia con [Slide 57] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 7 - VetCare.docx`. Clave para usted: `Quiz Clase 7 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 59]
**Decir:** «Queda avanzado: 3 indices justificados (uno parcial) + historico particionado por ano. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 59] slide de cierre. Dudas finales.


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
