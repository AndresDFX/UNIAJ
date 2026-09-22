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

**[Slide 4] De donde viene la clase: los Seq Scan de la Clase 6 (1/2)** — 7 vinetas.

**[Slide 5] De donde viene la clase: los Seq Scan de la Clase 6 (2/2)** — 4 vinetas.

**[Slide 6] El B-Tree por dentro, en cinco minutos (1/2)** — 5 vinetas.
  - De ahi la afirmacion que el docente debe poder defender: tres o cuatro niveles alcanzan para tablas de millones de filas, y encontrar una fila cuesta tres o cuatro lecturas de pagina, sin importar si la tabla tiene cien mil filas o cincuenta millones.

**[Slide 7] El B-Tree por dentro, en cinco minutos (2/2)** — 5 vinetas.

**[Slide 8] El precio se paga en cada escritura, y se cuantifica (1/2)** — 6 vinetas.

**[Slide 9] El precio se paga en cada escritura, y se cuantifica (2/2)** — 5 vinetas.

**[Slide 10] Indice compuesto: la regla del prefijo izquierdo (1/2)** — 5 vinetas.

**[Slide 11] Indice compuesto: la regla del prefijo izquierdo (2/2)** — 3 vinetas.

**[Slide 12] Cuando el indice responde solo, sin tocar la tabla (1/2)** — 4 vinetas.

**[Slide 13] Cuando el indice responde solo, sin tocar la tabla (2/2)** — 5 vinetas.

**[Slide 14] Las siete razones por las que un indice existente no se usa (1/2)** — 5 vinetas.

**[Slide 15] Las siete razones por las que un indice existente no se usa (2/2)** — 5 vinetas.

**[Slide 16] Los cinco nombres que se califican, y la consulta que justifica cada uno (1/2)** — 5 vinetas.

**[Slide 17] Los cinco nombres que se califican, y la consulta que justifica cada uno (2/2)** — 5 vinetas.

**[Slide 18] La secuencia de medicion, y por que el ANALYZE del medio no es opcional (1/2)** — 6 vinetas.

**[Slide 19] La secuencia de medicion, y por que el ANALYZE del medio no es opcional (2/2)** — 5 vinetas.

**[Slide 20] El experimento del orden de columnas, paso a paso (1/2)** — 5 vinetas.
  - La pregunta 2 no pide creer la regla del prefijo izquierdo, pide demostrarla, y el docente tiene que poder anticipar los tres resultados.

**[Slide 21] El experimento del orden de columnas, paso a paso (2/2)** — 4 vinetas.

**[Slide 22] El indice parcial: que indexa, cuanto ahorra y cuando gana (1/2)** — 6 vinetas.

**[Slide 23] El indice parcial: que indexa, cuanto ahorra y cuando gana (2/2)** — 5 vinetas.

**[Slide 24] Particionar: que es, y por que hoy si se implementa (1/2)** — 5 vinetas.

**[Slide 25] Particionar: que es, y por que hoy si se implementa (2/2)** — 4 vinetas.

**[Slide 26] El DDL de la particion, con sus dos trampas (1/2)** — 6 vinetas.

**[Slide 27] El DDL de la particion, con sus dos trampas (2/2)** — 6 vinetas.

**[Slide 28] El veredicto de particionamiento que pide la pregunta 5 (1/2)** — 6 vinetas.

**[Slide 29] El veredicto de particionamiento que pide la pregunta 5 (2/2)** — 5 vinetas.

**[Slide 30] La demo, en el orden en que se proyecta (1/2)** — 6 vinetas.

**[Slide 31] La demo, en el orden en que se proyecta (2/2)** — 5 vinetas.

**[Slide 32] Donde corre esto, y que no se puede medir aqui (1/2)** — 6 vinetas.

**[Slide 33] Donde corre esto, y que no se puede medir aqui (2/2)** — 5 vinetas.

**[Slide 34] El reparto de los 120 minutos y como acompanar el taller (1/2)** — 8 vinetas.

**[Slide 35] El reparto de los 120 minutos y como acompanar el taller (2/2)** — 6 vinetas.

**[Slide 36] Preguntas frecuentes del grupo (1/2)** — 5 vinetas.

**[Slide 37] Preguntas frecuentes del grupo (2/2)** — 7 vinetas.


**Demo que usted debe poder repetir:** EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 7 - Indices y particionamiento/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 7 · Indices y particionamiento · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. De donde viene la clase: los Seq Scan de la Clase 6 (1/2)
5. De donde viene la clase: los Seq Scan de la Clase 6 (2/2)
6. El B-Tree por dentro, en cinco minutos (1/2)
7. El B-Tree por dentro, en cinco minutos (2/2)
8. El precio se paga en cada escritura, y se cuantifica (1/2)
9. El precio se paga en cada escritura, y se cuantifica (2/2)
10. Indice compuesto: la regla del prefijo izquierdo (1/2)
11. Indice compuesto: la regla del prefijo izquierdo (2/2)
12. Cuando el indice responde solo, sin tocar la tabla (1/2)
13. Cuando el indice responde solo, sin tocar la tabla (2/2)
14. Las siete razones por las que un indice existente no se usa (1/2)
15. Las siete razones por las que un indice existente no se usa (2/2)
16. Los cinco nombres que se califican, y la consulta que justifica cada uno (1/2)
17. Los cinco nombres que se califican, y la consulta que justifica cada uno (2/2)
18. La secuencia de medicion, y por que el ANALYZE del medio no es opcional (1/2)
19. La secuencia de medicion, y por que el ANALYZE del medio no es opcional (2/2)
20. El experimento del orden de columnas, paso a paso (1/2)
21. El experimento del orden de columnas, paso a paso (2/2)
22. El indice parcial: que indexa, cuanto ahorra y cuando gana (1/2)
23. El indice parcial: que indexa, cuanto ahorra y cuando gana (2/2)
24. Particionar: que es, y por que hoy si se implementa (1/2)
25. Particionar: que es, y por que hoy si se implementa (2/2)
26. El DDL de la particion, con sus dos trampas (1/2)
27. El DDL de la particion, con sus dos trampas (2/2)
28. El veredicto de particionamiento que pide la pregunta 5 (1/2)
29. El veredicto de particionamiento que pide la pregunta 5 (2/2)
30. La demo, en el orden en que se proyecta (1/2)
31. La demo, en el orden en que se proyecta (2/2)
32. Donde corre esto, y que no se puede medir aqui (1/2)
33. Donde corre esto, y que no se puede medir aqui (2/2)
34. El reparto de los 120 minutos y como acompanar el taller (1/2)
35. El reparto de los 120 minutos y como acompanar el taller (2/2)
36. Preguntas frecuentes del grupo (1/2)
37. Preguntas frecuentes del grupo (2/2)
38. Un indice se justifica con la consulta que lo usa
39. Los cinco indices de hoy, con su nombre exacto
40. El indice parcial: el mismo beneficio, una fraccion del tamano
41. Particionar hoy de verdad: rango por ano, poda y archivado
42. Demo del dia
43. Herramientas de hoy
44. Taller PI VetCare — contexto / por que importa
45. Taller PI VetCare — objetivo y criterios
46. Taller PI VetCare — escenario / datos de partida
47. Taller PI VetCare — pasos guiados
48. Taller PI VetCare — pistas (checklist vacio)
49. Criterios de exito / entregable
50. Para el PI esta semana
51. Cierre · Clase 7

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

### 35-55 · Demo paso a paso · [Slide 42]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: EXPLAIN ANALYZE con Seq Scan, CREATE INDEX idx_cita_fecha_hora, ANALYZE, y el mismo EXPLAIN mostrando Index Scan.
Herramienta: ExamLab (PostgreSQL/PGlite)
📸 El plan de C1 antes y despues: Seq Scan -> Index Scan using idx_cita_programada_fecha [[captura: salida-indice-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 47]
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

### 105-115 · Criterios de exito + quiz corto · [Slide 49]
Repasar checklist del dia con [Slide 49] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 7 - VetCare.docx`. Clave para usted: `Quiz Clase 7 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 51]
**Decir:** «Queda avanzado: 3 indices justificados (uno parcial) + historico particionado por ano. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 51] slide de cierre. Dudas finales.


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
