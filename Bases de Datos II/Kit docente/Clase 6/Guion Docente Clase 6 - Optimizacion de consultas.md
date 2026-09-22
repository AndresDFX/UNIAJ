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

**[Slide 4] SQL es declarativo: quien decide el como es el optimizador (1/2)** — 5 vinetas.

**[Slide 5] SQL es declarativo: quien decide el como es el optimizador (2/2)** — 3 vinetas.

**[Slide 6] Leer un plan: es un arbol y se lee de adentro hacia afuera (1/3)** — 5 vinetas.
  - Y hay dos trampas al senalar el nodo mas costoso, que el docente tiene que conocer antes de calificar: el tiempo que muestra un nodo INCLUYE el de sus hijos, de modo que la primera linea siempre parece la mas cara sin serlo, y actual time es POR VUELTA, asi que el costo real de un nodo es su tiempo multiplicado por loops.

**[Slide 7] Leer un plan: es un arbol y se lee de adentro hacia afuera (2/3)** — 6 vinetas.

**[Slide 8] Leer un plan: es un arbol y se lee de adentro hacia afuera (3/3)** — 2 vinetas.

**[Slide 9] Las estadisticas: metadatos que describen los datos sin leerlos (1/2)** — 5 vinetas.
  - De ahi que se comparen rows estimadas contra actual rows, que es literalmente una de las tres columnas que pide la pregunta 2: una divergencia de 2 veces es normal, una de 10 veces o mas es la senal clasica de estadisticas viejas o de predicados correlacionados, y esa es tambien la sexta afirmacion de la pregunta 4, que es correcta.
  - Conviene marcar la diferencia de palabras en voz alta, porque van a aparecer las dos hoy: predicados correlacionados es esto, un asunto de estimacion; subconsulta correlacionada, la de la pregunta 3, es otra cosa completamente distinta y es un asunto de numero de ejecuciones.

**[Slide 10] Las estadisticas: metadatos que describen los datos sin leerlos (2/2)** — 5 vinetas.

**[Slide 11] Cardinalidad y selectividad: por que el motor decide lo que decide (1/3)** — 4 vinetas.
  - Dos terminos explican por que el motor decide lo que decide.

**[Slide 12] Cardinalidad y selectividad: por que el motor decide lo que decide (2/3)** — 4 vinetas.

**[Slide 13] Cardinalidad y selectividad: por que el motor decide lo que decide (3/3)** — 2 vinetas.

**[Slide 14] Full table scan contra index scan, sin caricaturas (1/3)** — 4 vinetas.
  - Con eso se explica full table scan contra index scan sin caricaturas.
  - Por eso la Clase 7 tiene que MEDIRLO y no suponerlo.

**[Slide 15] Full table scan contra index scan, sin caricaturas (2/3)** — 5 vinetas.

**[Slide 16] Full table scan contra index scan, sin caricaturas (3/3)** — 4 vinetas.

**[Slide 17] Predicado sargable: el antipatron que conecta con la Clase 7 (1/3)** — 5 vinetas.

**[Slide 18] Predicado sargable: el antipatron que conecta con la Clase 7 (2/3)** — 5 vinetas.

**[Slide 19] Predicado sargable: el antipatron que conecta con la Clase 7 (3/3)** — 3 vinetas.

**[Slide 20] Predicado sargable: el antipatron que conecta... — sintaxis** — 1 vinetas.

**[Slide 21] La subconsulta correlacionada: 2.006 pasadas o una sola (1/4)** — 5 vinetas.
  - Dos detalles que valen puntos y que el docente tiene que poder justificar en el momento.
  - No esta colgada.

**[Slide 22] La subconsulta correlacionada: 2.006 pasadas o una sola (2/4)** — 5 vinetas.

**[Slide 23] La subconsulta correlacionada: 2.006 pasadas o una sola (3/4)** — 4 vinetas.

**[Slide 24] La subconsulta correlacionada: 2.006 pasadas o una sola (4/4)** — 2 vinetas.

**[Slide 25] Optimizar no cambia el resultado, y eso se demuestra (1/2)** — 4 vinetas.
  - Y se rompe sin avisar, porque ningun motor va a lanzar un error por eso.
  - Por eso el taller cobra la prueba dos veces, unos 6 de los 100 puntos, y hay dos formas segun lo que se compare.
  - Para conjuntos completos, donde el conteo puede coincidir con filas distintas, se usa EXCEPT en los DOS sentidos, y el docente tiene que saber por que son dos: A EXCEPT B devuelve lo que esta en A y no esta en B, asi que si sale vacio todavia puede haber filas de mas en B; se corren las dos direcciones unidas con UNION ALL y se exige cero filas en total.
  - Tres advertencias al calificar.

**[Slide 26] Optimizar no cambia el resultado, y eso se demuestra (2/2)** — 2 vinetas.

**[Slide 27] El antes y el despues del script de la clase (1/3)** — 4 vinetas.
  - La version ANTES es SELECT * FROM cita c, mascota m, dueno d, veterinario v con las cuatro condiciones de union en el WHERE, to_char sobre la fecha y UPPER sobre el estado, y el docente debe saber que esta mal en cada linea.
  - SELECT * arrastra todas las columnas de las cuatro tablas cuando la pantalla de agenda necesita seis, lo cual multiplica el ancho de la fila y con el la memoria de trabajo del ordenamiento.
  - Las dos funciones sobre columnas se explicaron en el parrafo del predicado sargable.
  - Hay que decir aqui, y no despues, lo que la quinta afirmacion de la pregunta 4 castiga: cambiar la coma por JOIN...
  - ON no acelera nada, porque PostgreSQL normaliza las dos formas al mismo plan interno; se gana legibilidad y se gana que un ON faltante salte a la vista, o sea seguridad, no milisegundos.
  - Si el docente lo presenta como una mejora de rendimiento, esta ensenando justo la opcion por la que va a descontar.
  - La version DESPUES proyecta las seis columnas, escribe los tres JOIN...

**[Slide 28] El antes y el despues del script de la clase (2/3)** — 4 vinetas.

**[Slide 29] El antes y el despues del script de la clase (3/3)** — 2 vinetas.

**[Slide 30] Donde se corre todo esto, y que no se puede medir aqui (1/2)** — 4 vinetas.
  - Lo que hay que documentar en papel, porque el entorno no lo permite y es literalmente la seccion 5 de la pregunta 5: los tiempos con la memoria intermedia vacia, ya que vaciarla exige privilegios de administrador; el comportamiento con varias sesiones compitiendo, que es la Clase 10; y cualquier comparacion por encima de unos cientos de miles de filas.

**[Slide 31] Donde se corre todo esto, y que no se puede medir aqui (2/2)** — 4 vinetas.

**[Slide 32] Preguntas frecuentes del grupo (1/3)** — 4 vinetas.
  - Cuatro preguntas aparecen siempre.

**[Slide 33] Preguntas frecuentes del grupo (2/3)** — 4 vinetas.

**[Slide 34] Preguntas frecuentes del grupo (3/3)** — 3 vinetas.


**Demo que usted debe poder repetir:** Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada, con EXPLAIN ANALYZE antes y despues, en ExamLab.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 6 - Optimizacion de consultas/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 6 · Optimizacion de consultas · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. SQL es declarativo: quien decide el como es el optimizador (1/2)
5. SQL es declarativo: quien decide el como es el optimizador (2/2)
6. Leer un plan: es un arbol y se lee de adentro hacia afuera (1/3)
7. Leer un plan: es un arbol y se lee de adentro hacia afuera (2/3)
8. Leer un plan: es un arbol y se lee de adentro hacia afuera (3/3)
9. Las estadisticas: metadatos que describen los datos sin leerlos (1/2)
10. Las estadisticas: metadatos que describen los datos sin leerlos (2/2)
11. Cardinalidad y selectividad: por que el motor decide lo que decide (1/3)
12. Cardinalidad y selectividad: por que el motor decide lo que decide (2/3)
13. Cardinalidad y selectividad: por que el motor decide lo que decide (3/3)
14. Full table scan contra index scan, sin caricaturas (1/3)
15. Full table scan contra index scan, sin caricaturas (2/3)
16. Full table scan contra index scan, sin caricaturas (3/3)
17. Predicado sargable: el antipatron que conecta con la Clase 7 (1/3)
18. Predicado sargable: el antipatron que conecta con la Clase 7 (2/3)
19. Predicado sargable: el antipatron que conecta con la Clase 7 (3/3)
20. Predicado sargable: el antipatron que conecta... — sintaxis
21. La subconsulta correlacionada: 2.006 pasadas o una sola (1/4)
22. La subconsulta correlacionada: 2.006 pasadas o una sola (2/4)
23. La subconsulta correlacionada: 2.006 pasadas o una sola (3/4)
24. La subconsulta correlacionada: 2.006 pasadas o una sola (4/4)
25. Optimizar no cambia el resultado, y eso se demuestra (1/2)
26. Optimizar no cambia el resultado, y eso se demuestra (2/2)
27. El antes y el despues del script de la clase (1/3)
28. El antes y el despues del script de la clase (2/3)
29. El antes y el despues del script de la clase (3/3)
30. Donde se corre todo esto, y que no se puede medir aqui (1/2)
31. Donde se corre todo esto, y que no se puede medir aqui (2/2)
32. Preguntas frecuentes del grupo (1/3)
33. Preguntas frecuentes del grupo (2/3)
34. Preguntas frecuentes del grupo (3/3)
35. Optimizar es un ANTES medible, no una opinion
36. Leer un plan: es un arbol y se lee de adentro hacia afuera
37. La subconsulta correlacionada: 2.006 pasadas o una sola
38. Optimizar no cambia el resultado: como se prueba
39. Demo del dia
40. Herramientas de hoy
41. Taller PI VetCare — contexto / por que importa
42. Taller PI VetCare — objetivo y criterios
43. Taller PI VetCare — escenario / datos de partida
44. Taller PI VetCare — pasos guiados
45. Taller PI VetCare — pistas (checklist vacio)
46. Criterios de exito / entregable
47. Para el PI esta semana
48. Cierre · Clase 6

> Privado, no se proyecta: `Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Primera pareja de consultas antes/despues del PI.
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
- Optimizar consultas parte de entender que el motor NO ejecuta el SQL tal cual se escribe: primero lo transforma en un plan de ejecucion (que tablas leer, en que orden, con o sin indice) y ese plan es lo que realmente determina el tiempo de respuesta.
- Tres cuellos de botella clasicos: (1) SELECT * trae columnas que nadie usa y aumenta el trafico/memoria; (2) JOIN sin filtro temprano obliga a cruzar tablas completas antes de descartar filas; (3) aplicar una funcion sobre la columna en el WHERE (ej. WHERE UPPER(nombre)='LUNA') impide que el motor use un indice normal sobre esa columna (esto se llama 'no-sargable').
- Reescritura tipica: proyectar solo columnas necesarias (SELECT nombre, fecha en vez de SELECT *), aplicar el filtro mas selectivo primero (WHERE fecha >= hoy antes del JOIN si reduce mucho el conjunto), y mover comparaciones a la forma que el motor pueda usar con indice.
- El cuarto cuello de botella, y el mas caro: una subconsulta correlacionada en la lista de columnas se evalua UNA VEZ POR FILA del exterior — el plan lo dice con loops=2006 —, y se elimina reescribiendola como LEFT JOIN + GROUP BY, que hace una sola pasada. Con LEFT JOIN hay que contar la columna, COUNT(c.id_cita), y no COUNT(*): el LEFT JOIN fabrica una fila de NULL por cada dueno sin citas, y COUNT(*) cuenta filas, asi que reportaria 1 donde la respuesta es 0.
- Optimizar NO puede cambiar el resultado, y eso se demuestra, no se afirma: un COUNT(*) de cada version que coincida, y para conjuntos completos un EXCEPT en los DOS sentidos que devuelva cero filas (EXCEPT no es simetrico: A EXCEPT B vacio no dice nada sobre filas de mas en B).
- EXPLAIN muestra el plan que el motor ESTIMA; EXPLAIN ANALYZE lo ejecuta de verdad y agrega actual rows, loops y Execution Time. En PostgreSQL el recorrido completo de tabla se llama Seq Scan (en Oracle, TABLE ACCESS FULL): verlo sobre una tabla grande donde se esperaba un indice es la senal de que el WHERE o el tipo de dato bloquea el indice.
- Conexion con Clase 7: optimizar consultas y crear indices son las dos caras de la misma moneda — una consulta mal escrita no aprovecha ni el mejor indice, y el mejor indice no compensa una consulta que fuerza un escaneo completo. Hoy NO se crea ningun indice: por eso la mejora que se mide es la de filas procesadas y pasadas sobre la tabla, no un cambio de Seq Scan a Index Scan.
- Error de docente que no domina el tema: pedir 'la consulta más rápida' sin definir contra que se compara (volumen de datos, indices existentes) — optimizar siempre es relativo a un antes medible, por eso el taller pide guardar la version antes Y despues, no solo la version final.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 39]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Consulta pesada citas+mascotas+duenos -> version filtrada y proyectada, con EXPLAIN ANALYZE antes y despues, en ExamLab.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 EXPLAIN ANALYZE ANTES vs DESPUES: el nodo no cambia, las pasadas si (loops 2006 -> 1) [[captura: salida-explain-antes-despues.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 44]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Reescribir la agenda del dia corrigiendo sus 4 antipatrones (SELECT *, joins con coma, to_char sobre la fecha, UPPER sobre el estado) y probar con COUNT(*) que las dos versiones devuelven las mismas 91 filas.
2. Medir con EXPLAIN (ANALYZE, BUFFERS) las dos versiones, y con EXPLAIN ANALYZE una tercera que le anada LIMIT 50, y anotar las tres en comentarios: nodo mas costoso, filas estimadas vs reales y tiempo.
3. Matar la subconsulta correlacionada del ranking de duenos: LEFT JOIN + GROUP BY + COUNT(c.id_cita), y demostrar la equivalencia con EXCEPT en los dos sentidos.
4. Responder la de seleccion multiple sobre antipatrones (6 afirmaciones, 4 correctas).
5. Escribir la justificacion tecnica de media pagina y guardar 06_opt_antes.sql / 06_opt_despues.sql en la carpeta del PI.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 consultas (antes/despues) + justificacion (media pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 6/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 46]
Repasar checklist del dia con [Slide 46] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 6 - VetCare.docx`. Clave para usted: `Quiz Clase 6 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 48]
**Decir:** «Queda avanzado: Primera pareja de consultas antes/despues del PI. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 48] slide de cierre. Dudas finales.


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
