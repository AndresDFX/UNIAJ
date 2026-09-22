# Guion docente · Clase 3 · Procedimientos almacenados · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 procedimiento de negocio (agendar cita / registrar consulta)
- **Entregable de hoy:** 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx
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

**[Slide 4] Que es un procedimiento almacenado, y las dos palabras que importan (1/2)** — 6 vinetas.
  - Conviene senalar de entrada una diferencia con Oracle que importa hoy, porque cambia como se depura.

**[Slide 5] Que es un procedimiento almacenado, y las dos palabras que importan (2/2)** — 6 vinetas.

**[Slide 6] El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar (1/2)** — 8 vinetas.

**[Slide 7] El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar (2/2)** — 8 vinetas.

**[Slide 8] Los modos de parametro, y por que hoy no se usa OUT (1/2)** — 8 vinetas.

**[Slide 9] Los modos de parametro, y por que hoy no se usa OUT (2/2)** — 7 vinetas.

**[Slide 10] RAISE EXCEPTION: la validacion que aborta y deshace (1/3)** — 7 vinetas.

**[Slide 11] RAISE EXCEPTION: la validacion que aborta y deshace (2/3)** — 7 vinetas.

**[Slide 12] RAISE EXCEPTION: la validacion que aborta y deshace (3/3)** — 5 vinetas.

**[Slide 13] Donde debe vivir la logica de negocio: la respuesta honesta (1/2)** — 7 vinetas.

**[Slide 14] Donde debe vivir la logica de negocio: la respuesta honesta (2/2)** — 8 vinetas.

**[Slide 15] La inyeccion de SQL, explicada y no solo mencionada (1/2)** — 7 vinetas.

**[Slide 16] La inyeccion de SQL, explicada y no solo mencionada (2/2)** — 7 vinetas.

**[Slide 17] La bateria de pruebas: por que un bloque DO por caso (1/3)** — 8 vinetas.

**[Slide 18] La bateria de pruebas: por que un bloque DO por caso (2/3)** — 6 vinetas.

**[Slide 19] La bateria de pruebas: por que un bloque DO por caso (3/3)** — 6 vinetas.

**[Slide 20] Que significa la columna paso, y la trampa del WHEN OTHERS (1/2)** — 5 vinetas.
  - Conviene decir en voz alta la consecuencia, porque es la que evita reclamos: no se descuenta por elegir una u otra, se descuenta por las cuatro filas en verdadero sin haber verificado el texto.

**[Slide 21] Que significa la columna paso, y la trampa del WHEN OTHERS (2/2)** — 5 vinetas.

**[Slide 22] El contrato del procedimiento: los 6 bloques que consume la app (1/2)** — 6 vinetas.

**[Slide 23] El contrato del procedimiento: los 6 bloques que consume la app (2/2)** — 6 vinetas.

**[Slide 24] Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4** — 5 vinetas.
  - Conviene cerrar la teoria con esta distincion, y decirla HOY, porque el estudiante la va a necesitar en el taller de hoy y no la semana entrante.

**[Slide 25] Depurar sin depurador: los cuatro movimientos, en PostgreSQL (1/2)** — 5 vinetas.
  - Conviene mencionar que RAISE tiene niveles —NOTICE, WARNING, EXCEPTION— y que solo el ultimo aborta.

**[Slide 26] Depurar sin depurador: los cuatro movimientos, en PostgreSQL (2/2)** — 3 vinetas.

**[Slide 27] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (1/2)** — 4 vinetas.

**[Slide 28] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (2/2)** — 3 vinetas.

**[Slide 29] El segundo procedimiento: sp_registrar_consulta y el EXISTS (1/2)** — 6 vinetas.
  - Conviene decir tambien lo que NO hay que hacer: quitar la restriccion porque ya esta el procedimiento.

**[Slide 30] El segundo procedimiento: sp_registrar_consulta y el EXISTS (2/2)** — 4 vinetas.

**[Slide 31] Como amarra con las clases vecinas y con la rubrica del PI** — 6 vinetas.

**[Slide 32] Preguntas frecuentes del grupo (1/2)** — 7 vinetas.

**[Slide 33] Preguntas frecuentes del grupo (2/2)** — 6 vinetas.


**Demo que usted debe poder repetir:** sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 3 · Procedimientos almacenados · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Que es un procedimiento almacenado, y las dos palabras que importan (1/2)
5. Que es un procedimiento almacenado, y las dos palabras que importan (2/2)
6. El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar (1/2)
7. El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar (2/2)
8. Los modos de parametro, y por que hoy no se usa OUT (1/2)
9. Los modos de parametro, y por que hoy no se usa OUT (2/2)
10. RAISE EXCEPTION: la validacion que aborta y deshace (1/3)
11. RAISE EXCEPTION: la validacion que aborta y deshace (2/3)
12. RAISE EXCEPTION: la validacion que aborta y deshace (3/3)
13. Donde debe vivir la logica de negocio: la respuesta honesta (1/2)
14. Donde debe vivir la logica de negocio: la respuesta honesta (2/2)
15. La inyeccion de SQL, explicada y no solo mencionada (1/2)
16. La inyeccion de SQL, explicada y no solo mencionada (2/2)
17. La bateria de pruebas: por que un bloque DO por caso (1/3)
18. La bateria de pruebas: por que un bloque DO por caso (2/3)
19. La bateria de pruebas: por que un bloque DO por caso (3/3)
20. Que significa la columna paso, y la trampa del WHEN OTHERS (1/2)
21. Que significa la columna paso, y la trampa del WHEN OTHERS (2/2)
22. El contrato del procedimiento: los 6 bloques que consume la app (1/2)
23. El contrato del procedimiento: los 6 bloques que consume la app (2/2)
24. Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4
25. Depurar sin depurador: los cuatro movimientos, en PostgreSQL (1/2)
26. Depurar sin depurador: los cuatro movimientos, en PostgreSQL (2/2)
27. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (1/2)
28. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar (2/2)
29. El segundo procedimiento: sp_registrar_consulta y el EXISTS (1/2)
30. El segundo procedimiento: sp_registrar_consulta y el EXISTS (2/2)
31. Como amarra con las clases vecinas y con la rubrica del PI
32. Preguntas frecuentes del grupo (1/2)
33. Preguntas frecuentes del grupo (2/2)
34. Por que un procedimiento y no SQL en cada pantalla
35. El molde de PL/pgSQL y la validacion que aborta
36. La bateria de pruebas: un bloque DO por caso
37. La columna paso y la trampa de WHEN OTHERS
38. El contrato del procedimiento: los 6 bloques que consume la app
39. PROCEDURE o FUNCTION: cual se puede usar dentro de un SELECT
40. Demo del dia
41. Herramientas de hoy
42. Taller PI VetCare — contexto / por que importa
43. Taller PI VetCare — objetivo y criterios
44. Taller PI VetCare — escenario / datos de partida
45. Taller PI VetCare — pasos guiados
46. Taller PI VetCare — pistas (checklist vacio)
47. Criterios de exito / entregable
48. Para el PI esta semana
49. Cierre · Clase 3

> Privado, no se proyecta: `Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=1 procedimiento de negocio (agendar cita / registrar consulta).
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
- Un procedimiento almacenado es logica de negocio guardada DENTRO de la base, y se llama con CALL. No es una consulta con nombre: recibe parametros tipados y ejecuta varias sentencias como una sola unidad logica, de modo que la regla vive UNA vez y toda la app la respeta.
- El molde de PL/pgSQL es fijo: CREATE PROCEDURE nombre(params) LANGUAGE plpgsql AS $proc$ ... $proc$;. Dentro van DECLARE (variables), BEGIN y END. Los delimitadores $proc$ (dollar-quoting) existen porque el cuerpo lleva punto y coma y el motor necesita saber donde termina. Nada de IS en vez de AS, ni VARCHAR2, ni NUMBER, ni RAISE_APPLICATION_ERROR, ni la barra / final: eso es Oracle y aqui no compila.
- Parametros: IN es el defecto y no se escribe; OUT e INOUT existen pero hoy no se usan para reportar errores. Los tipos son los de PostgreSQL: INT, NUMERIC, TEXT, TIMESTAMP, BOOLEAN.
- La validacion no devuelve un mensaje: aborta con RAISE EXCEPTION 'ERROR: ... %', variable;. El % se sustituye en orden por las variables que siguen a la coma. Al abortar, todo lo que el procedimiento hubiera hecho se deshace, asi que es imposible que quede una cita a medias. Con un mensaje en un parametro OUT el INSERT seguiria corriendo: la regla no se cumpliria.
- Un procedimiento sin prueba no esta terminado: la bateria son bloques DO que capturan el error. Cada caso va en su propio bloque DO $$ BEGIN ... EXCEPTION WHEN OTHERS THEN ... SQLERRM ... END $$;, y el resultado se escribe en una tabla resultado_prueba (caso, esperado, obtenido, paso). Un caso OK y tres casos error, mas el COUNT(*) que demuestra que la tabla cita paso de 10 a 11 filas.
- Procedimiento y funcion se diferencian hoy, no en la Clase 4: CALL sp_x(...) frente a SELECT fn_x(...). El procedimiento se ejecuta como una accion y puede manejar transacciones; la funcion retorna un valor y se invoca dentro de una expresion SQL. En PostgreSQL una funcion no puede hacer COMMIT ni ROLLBACK, y eso es lo que decide cual de los dos se usa.
- El contrato del proc es lo que consume la futura app: firma, precondiciones, postcondiciones y errores. Son 6 bloques: la firma exacta con tipos, un ejemplo de CALL, las precondiciones, las postcondiciones, la tabla de errores con su mensaje literal, y la decision de diseno que explica por que se aborta en vez de devolver un codigo.
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre. El segundo error es dictar el molde de Oracle porque es el que uno recuerda: en ExamLab ese codigo no compila, y el estudiante pierde los 35 puntos de la pregunta 1 por sintaxis, no por no entender el tema.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 40]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 Bateria de pruebas de sp_agendar_cita: P1 OK y P2 rechazado por mascota inactiva [[captura: salida-proc-ok-y-error.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 45]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Escribir sp_agendar_cita en PL/pgSQL y ejecutarlo en ExamLab (LANGUAGE plpgsql, dollar-quoting, sin sintaxis de Oracle).
2. Incluir las 3 validaciones de negocio del PI, cada una con su RAISE EXCEPTION y su mensaje literal.
3. Correr la bateria de pruebas con bloques DO: 1 caso OK + 3 casos error, escritos en resultado_prueba, mas el COUNT(*) de cita antes y despues.
4. Escribir sp_registrar_consulta, comprobando con EXISTS antes de chocar contra la restriccion UNIQUE.
5. Redactar el contrato del proc en sus 6 bloques (plantilla en este documento) y pegarlo en la pregunta 5.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 3/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 47]
Repasar checklist del dia con [Slide 47] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 3 - VetCare.docx`. Clave para usted: `Quiz Clase 3 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 49]
**Decir:** «Queda avanzado: >=1 procedimiento de negocio (agendar cita / registrar consulta). Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 49] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 03_procs_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 3/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
