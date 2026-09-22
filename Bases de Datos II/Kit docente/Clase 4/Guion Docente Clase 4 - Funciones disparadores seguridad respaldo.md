# Guion docente · Clase 4 · Funciones · Triggers · Seguridad y respaldo

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 funcion + >=1 trigger + borrador plan de respaldo
- **Entregable de hoy:** fn_precio_consulta + 2 triggers corriendo en ExamLab + Plan_Backup_VetCare con sus 6 secciones (1 pag.)
- **Herramienta:** ExamLab (PostgreSQL) + Google Docs
- **Slides:** Clases/Clase 4 - Funciones disparadores seguridad respaldo/Presentacion.pptx
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

**[Slide 4] Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (1/3)** — 5 vinetas.
  - Una funcion y un procedimiento se parecen tanto en la escritura que conviene separarlos por su papel y no por su sintaxis.
  - RETURNS declara el tipo del valor devuelto, y dentro del cuerpo tiene que haber al menos un RETURN, porque una funcion de PL/pgSQL que termina sin retornar lanza un error en ejecucion.

**[Slide 5] Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (2/3)** — 5 vinetas.

**[Slide 6] Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (3/3)** — 3 vinetas.

**[Slide 7] Funcion y procedimiento: se distinguen por su... — sintaxis** — 6 vinetas.

**[Slide 8] Los tres detalles de fn_precio_consulta que valen puntos (1/2)** — 6 vinetas.
  - La aplicacion de Huellitas puede mandar 'Canino', 'canino' o 'CANINO', y comparar el texto tal como llega significa que dos de las tres formas caen al precio de otra especie.
  - Si la casilla de urgencia llega en nulo, que es lo que hace una interfaz donde el usuario no marco nada, entonces IF p_urgencia THEN no entra —nulo no es verdadero— pero cualquier aritmetica con nulo si contamina: v_base * p_urgencia daria nulo y la factura saldria vacia.

**[Slide 9] Los tres detalles de fn_precio_consulta que valen puntos (2/2)** — 4 vinetas.

**[Slide 10] El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos (1/2)** — 4 vinetas.
  - Despues la asociacion,;, que dice cuando dispararla y a quien llamar.
  - EXECUTE PROCEDURE todavia se acepta por compatibilidad, pero esta obsoleto y no conviene ensenarlo.
  - De ahi salen sus dos caras: si el trigger falla, la sentencia original tambien falla y se deshace, que es exactamente lo que se quiere para un invariante como que el stock nunca quede negativo; y si el trigger es lento, la sentencia original se vuelve lenta, y si bloquea, bloquea al usuario que hizo el UPDATE.
  - Conviene mencionar tambien las variables especiales que PL/pgSQL pone a disposicion dentro de una funcion de trigger, porque permiten escribir una sola funcion para varios eventos: TG_OP dice si fue INSERT, UPDATE o DELETE, TG_TABLE_NAME dice sobre que tabla, y TG_WHEN y TG_LEVEL dicen si es BEFORE o AFTER y de fila o de sentencia.
  - Hoy no hacen falta, pero saber que existen evita que el estudiante escriba tres funciones casi identicas.

**[Slide 11] El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos (2/2)** — 2 vinetas.

**[Slide 12] El trigger: el unico que nadie invoca, y en... — sintaxis** — 4 vinetas.

**[Slide 13] BEFORE o AFTER, y que significa el valor que se retorna (1/2)** — 4 vinetas.
  - Para un trigger de DELETE se retorna OLD, porque NEW no existe en ese evento; simetricamente, en un INSERT no existe OLD.
  - FOR EACH ROW indica que se ejecuta una vez por fila afectada y da acceso a OLD y NEW.
  - La regla operativa, que es la que se califica en la pregunta 4, se dice en una frase: el que VALIDA va BEFORE, porque tiene que abortar antes de que el dato quede escrito y porque solo ahi puede corregirlo; el que AUDITA va AFTER, porque registra un hecho ya consumado.

**[Slide 14] BEFORE o AFTER, y que significa el valor que se retorna (2/2)** — 6 vinetas.

**[Slide 15] La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado (1/2)** — 6 vinetas.
  - Vale leer la cabecera del trigger del proyecto palabra por palabra, porque cada pieza tiene razon.
  - AFTER UPDATE OF estado ON cita limita el disparo a los cambios de esa columna y no a cualquier actualizacion de la fila, de modo que corregir el telefono no escribe una fila de auditoria.
  - FOR EACH ROW da acceso a OLD y NEW.
  - Sin WHEN, la auditoria se llena de eventos donde no cambio nada y deja de servir para investigar.
  - Conviene detenerse en esos dos defaults porque tienen matices. current_user devuelve el rol EFECTIVO, es decir el que la Clase 2 cambiaba con SET ROLE, y no necesariamente quien inicio la sesion, que es session_user; para auditar interesa el efectivo.
  - Y now() devuelve el instante de inicio de la transaccion, no el del reloj, asi que si una transaccion escribe cinco filas de auditoria las cinco llevan la misma marca de tiempo; si eso importa, existe clock_timestamp().
  - Como referencia de dimensionamiento, si la clinica registra doscientos cambios auditables por dia, la tabla crece del orden de setenta y tres mil filas en doce meses, cifra que obliga a definir retencion en el mismo plan de respaldo.

**[Slide 16] La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado (2/2)** — 4 vinetas.

**[Slide 17] El trigger que impide: el hueco que el CHECK no tapa (1/2)** — 6 vinetas.
  - Lo que un CHECK no puede hacer es mirar OTRA fila, OTRA tabla, o el valor ANTERIOR de la fila que se esta cambiando; solo ve los valores finales de la fila que se inserta o actualiza.
  - Por eso el trigger de stock del taller no es un reemplazo del CHECK sino una demostracion de la capacidad extra: la funcion fn_trg_stock_no_negativo() puede escribir RAISE EXCEPTION 'ERROR: el stock de % no puede quedar negativo (resultado: %)', OLD.nombre, NEW.stock, es decir puede nombrar el insumo tomando el dato de OLD y el resultado de NEW en el mismo mensaje.

**[Slide 18] El trigger que impide: el hueco que el CHECK no tapa (2/2)** — 4 vinetas.

**[Slide 19] Las cuatro capas, y en cual vive cada regla (1/3)** — 5 vinetas.
  - La pregunta 4 vale quince puntos, no pide codigo y es la que mejor mide si el estudiante entendio el dia: hay que ubicar cada validacion en su capa y justificar por que ahi.
  - Conviene dictar las cuatro capas en orden de preferencia, porque el orden es la respuesta.
  - Las dos pasan la verificacion y las dos insertan.
  - La respuesta correcta es declarativa ——, es mas rapida, mas clara y a prueba de concurrencia, y el porque completo llega en la Clase 10.

**[Slide 20] Las cuatro capas, y en cual vive cada regla (2/3)** — 4 vinetas.

**[Slide 21] Las cuatro capas, y en cual vive cada regla (3/3)** — 3 vinetas.

**[Slide 22] Las cuatro capas, y en cual vive cada regla — sintaxis** — 1 vinetas.

**[Slide 23] Cuando NO se usa un trigger, y lo que un trigger no ve (1/3)** — 5 vinetas.
  - Hay tres riesgos que conviene exponer con ejemplos y no como advertencia generica.
  - PostgreSQL no la prohibe, la corta cuando se agota la pila, y eso ocurre en produccion y con datos reales, no durante la prueba.
  - TRUNCATE no dispara triggers de fila, asi que un TRUNCATE insumo pasa por encima de la validacion de stock sin que se escriba una sola linea de auditoria.

**[Slide 24] Cuando NO se usa un trigger, y lo que un trigger no ve (2/3)** — 4 vinetas.

**[Slide 25] Cuando NO se usa un trigger, y lo que un trigger no ve (3/3)** — 3 vinetas.

**[Slide 26] Seguridad y respaldo: dos preguntas complementarias (1/3)** — 5 vinetas.

**[Slide 27] Seguridad y respaldo: dos preguntas complementarias (2/3)** — 6 vinetas.

**[Slide 28] Seguridad y respaldo: dos preguntas complementarias (3/3)** — 2 vinetas.

**[Slide 29] RPO y RTO: dos siglas que solo sirven con un numero acordado (1/3)** — 4 vinetas.
  - RPO y RTO dejan de ser siglas cuando se les pone un numero acordado con el negocio, y la rubrica pide precisamente el numero con su justificacion.
  - Probar un restore de verdad tiene cuatro pasos y conviene dictarlos como procedimiento.
  - Cuatro, dejar bitacora con fecha, responsable, resultado y RTO medido; si no hay bitacora, la prueba no existe.

**[Slide 30] RPO y RTO: dos siglas que solo sirven con un numero acordado (2/3)** — 4 vinetas.

**[Slide 31] RPO y RTO: dos siglas que solo sirven con un numero acordado (3/3)** — 3 vinetas.

**[Slide 32] Lo que ExamLab si puede demostrar, y lo que se documenta en papel** — 6 vinetas.
  - Lo que NO se puede ejecutar es pg_dump, pg_dumpall, pg_basebackup ni pg_restore, y la razon hay que decirla con precision en vez de dejarla en «la herramienta no sirve»: son programas de linea de comandos que leen y escriben archivos, y ahi no hay sistema de archivos ni servidor al que conectarse.
  - Por eso la pregunta 5 es un documento y no una ejecucion: se califica que el plan nombre la herramienta correcta para cada cosa, no que el estudiante la haya corrido.
  - Esa distincion hay que decirla en clase, porque un estudiante que intente ejecutar pg_dump en la consola de ExamLab va a perder veinte minutos y va a creer que hizo algo mal.
  - Lo que si se puede ensayar de verdad, y conviene hacerlo, es el restore a escala de aula: borrar el esquema completo y volverlo a levantar pegando el propio guion del estudiante, con cronometro en mano.
  - Vale un minuto senalarlo para quien se encuentre Oracle en el trabajo, y no vale mas, porque la calificacion ocurre en PostgreSQL.

**[Slide 33] Como amarra con las clases vecinas y con la rubrica del PI (1/2)** — 4 vinetas.

**[Slide 34] Como amarra con las clases vecinas y con la rubrica del PI (2/2)** — 3 vinetas.

**[Slide 35] Preguntas frecuentes del grupo (1/3)** — 3 vinetas.

**[Slide 36] Preguntas frecuentes del grupo (2/3)** — 4 vinetas.

**[Slide 37] Preguntas frecuentes del grupo (3/3)** — 3 vinetas.

**[Slide 38] La funcion de tarifas, y por que IMMUTABLE importa** — 15 vinetas.

**[Slide 39] Un trigger son DOS objetos: la funcion y la asociacion** — 18 vinetas.

**[Slide 40] BEFORE o AFTER: uno puede impedir, el otro solo registrar** — 16 vinetas.

**[Slide 41] Las cuatro capas, y en cual vive cada regla** — 11 vinetas.


**Demo que usted debe poder repetir:** fn_precio_consulta + fn_trg_audit_cita con su CREATE TRIGGER ... EXECUTE FUNCTION, en ExamLab, y el esqueleto del plan de respaldo.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 4 - Funciones disparadores seguridad respaldo/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 4 · Funciones · Triggers · Seguridad y respaldo
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (1/3)
5. Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (2/3)
6. Funcion y procedimiento: se distinguen por su papel, no por su sintaxis (3/3)
7. Funcion y procedimiento: se distinguen por su... — sintaxis
8. Los tres detalles de fn_precio_consulta que valen puntos (1/2)
9. Los tres detalles de fn_precio_consulta que valen puntos (2/2)
10. El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos (1/2)
11. El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos (2/2)
12. El trigger: el unico que nadie invoca, y en... — sintaxis
13. BEFORE o AFTER, y que significa el valor que se retorna (1/2)
14. BEFORE o AFTER, y que significa el valor que se retorna (2/2)
15. La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado (1/2)
16. La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado (2/2)
17. El trigger que impide: el hueco que el CHECK no tapa (1/2)
18. El trigger que impide: el hueco que el CHECK no tapa (2/2)
19. Las cuatro capas, y en cual vive cada regla (1/3)
20. Las cuatro capas, y en cual vive cada regla (2/3)
21. Las cuatro capas, y en cual vive cada regla (3/3)
22. Las cuatro capas, y en cual vive cada regla — sintaxis
23. Cuando NO se usa un trigger, y lo que un trigger no ve (1/3)
24. Cuando NO se usa un trigger, y lo que un trigger no ve (2/3)
25. Cuando NO se usa un trigger, y lo que un trigger no ve (3/3)
26. Seguridad y respaldo: dos preguntas complementarias (1/3)
27. Seguridad y respaldo: dos preguntas complementarias (2/3)
28. Seguridad y respaldo: dos preguntas complementarias (3/3)
29. RPO y RTO: dos siglas que solo sirven con un numero acordado (1/3)
30. RPO y RTO: dos siglas que solo sirven con un numero acordado (2/3)
31. RPO y RTO: dos siglas que solo sirven con un numero acordado (3/3)
32. Lo que ExamLab si puede demostrar, y lo que se documenta en papel
33. Como amarra con las clases vecinas y con la rubrica del PI (1/2)
34. Como amarra con las clases vecinas y con la rubrica del PI (2/2)
35. Preguntas frecuentes del grupo (1/3)
36. Preguntas frecuentes del grupo (2/3)
37. Preguntas frecuentes del grupo (3/3)
38. La funcion de tarifas, y por que IMMUTABLE importa
39. Un trigger son DOS objetos: la funcion y la asociacion
40. BEFORE o AFTER: uno puede impedir, el otro solo registrar
41. Las cuatro capas, y en cual vive cada regla
42. Un trigger son DOS objetos: la funcion y la asociacion
43. La funcion de tarifas: RETURNS NUMERIC, CASE, COALESCE e IMMUTABLE
44. Donde vive cada validacion: CHECK, trigger o aplicacion
45. Plan de respaldo: 6 secciones y herramientas reales de PostgreSQL
46. Demo del dia
47. Herramientas de hoy
48. Taller PI VetCare — contexto / por que importa
49. Taller PI VetCare — objetivo y criterios
50. Taller PI VetCare — escenario / datos de partida
51. Taller PI VetCare — pasos guiados
52. Taller PI VetCare — pistas (checklist vacio)
53. Criterios de exito / entregable
54. Para el PI esta semana
55. Cierre · Clase 4

> Privado, no se proyecta: `Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=1 funcion + >=1 trigger + borrador plan de respaldo.
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
- Funcion (Clase 3 vio procedimiento): retorna un valor y se usa DENTRO de una expresion SQL, ej. SELECT fn_precio_consulta(especie, urgencia) FROM mascota. Su molde es CREATE FUNCTION nombre(params) RETURNS tipo LANGUAGE plpgsql AS $fn$ ... $fn$;. Si no toca datos se marca IMMUTABLE, que le dice al motor que puede memorizar el resultado. Nada de RETURN NUMBER IS: eso es Oracle.
- Trigger (disparador): bloque de codigo que el motor ejecuta AUTOMATICAMENTE cuando ocurre un evento (BEFORE/AFTER INSERT, UPDATE o DELETE) sobre una tabla, sin que nadie lo llame explicitamente. Dos usos tipicos aqui: auditoria (guardar quien/cuando cancelo una cita) y validacion de invariantes (que el stock nunca quede negativo tras un UPDATE).
- En PostgreSQL un trigger son SIEMPRE dos objetos, no uno: la funcion y la asociacion. Primero CREATE FUNCTION fn_trg_x() RETURNS TRIGGER, que termina en RETURN NEW (o RETURN OLD si el evento es DELETE); despues CREATE TRIGGER trg_x AFTER UPDATE OF estado ON cita FOR EACH ROW EXECUTE FUNCTION fn_trg_x();. Dentro de la funcion las filas se leen como NEW y OLD, SIN los dos puntos: NEW.estado, no :NEW.estado. Escribir el cuerpo dentro del CREATE TRIGGER es la herencia de Oracle que mas cuesta puntos, porque no compila.
- BEFORE o AFTER no es un detalle de estilo: un trigger que VALIDA va BEFORE, porque tiene que abortar antes de que el dato quede escrito; un trigger que AUDITA va AFTER, porque registra un hecho ya consumado. Y la clausula WHEN (OLD.estado IS DISTINCT FROM NEW.estado) evita registrar los UPDATE que no cambiaron nada: es la diferencia entre auditar 2 filas y auditar 3.
- Riesgo real de los triggers: son invisibles en el codigo de la app (un desarrollador que solo mira el INSERT no ve que ademas se dispara una auditoria), y pueden encadenarse (un trigger que dispara otro trigger) generando efectos dificiles de rastrear. Se usan para pocas reglas criticas, no para toda la logica de negocio: una regla sobre una sola columna es un CHECK, una regla que compara filas es un trigger, y una regla de interfaz es de la app.
- Seguridad y respaldo van juntos: seguridad evita que datos se corrompan o se filtren; respaldo (backup) asume que igual algo saldra mal y prepara la recuperacion. Full backup (copia completa), incremental (solo lo que cambio desde el ultimo backup) y diferencial (todo lo que cambio desde el ultimo FULL) son las tres estrategias base. En PostgreSQL las herramientas son pg_dump (una base), pg_dumpall --globals-only (los roles del cluster, que pg_dump NO respalda) y pg_basebackup con archivado de WAL.
- RPO (Recovery Point Objective) = cuantos datos se puede permitir perder, medido en tiempo ('maximo 1 hora de citas perdidas'). RTO (Recovery Time Objective) = cuanto tiempo puede estar caida la BD antes de restaurar. Un backup diario sin probar el restore no cumple ningun RPO/RTO real: un plan de respaldo sin prueba de restauracion es solo una promesa.
- Error de docente que no domina el tema: presentar el backup como 'copiar el archivo de vez en cuando' sin frecuencia, retencion (cuantas copias se guardan) ni prueba de restore — eso es lo que el taller de esta clase pide explicitamente que el estudiante defina. El segundo error es dictar el trigger como en Oracle, con el cuerpo dentro del CREATE TRIGGER y :NEW/:OLD: la rubrica lo penaliza expresamente, asi que el docente estaria proyectando el codigo por el que va a descontar.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 46]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: fn_precio_consulta + fn_trg_audit_cita con su CREATE TRIGGER ... EXECUTE FUNCTION, en ExamLab, y el esqueleto del plan de respaldo.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 trg_audit_cita: los 3 UPDATE dejan 2 filas de auditoria (el WHEN filtra el tercero) [[captura: cap01_demo.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 51]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Escribir fn_precio_consulta(especie, urgencia) RETURNS NUMERIC en PL/pgSQL y probarla con SELECT sobre las 3 especies.
2. Crear la tabla audit_cita y el trigger de auditoria en sus dos objetos: fn_trg_audit_cita() RETURNS TRIGGER + CREATE TRIGGER ... EXECUTE FUNCTION.
3. Crear el trigger de stock no negativo (BEFORE UPDATE), evidenciando primero que sin el el stock llega a -7.
4. Decidir donde vive cada validacion: CHECK, trigger o aplicacion (pregunta 4).
5. Redactar Plan_Backup_VetCare con sus 6 secciones (plantilla en este documento): que se respalda y con que, frecuencia, retencion, RPO/RTO, restore de prueba con quien firma, y que NO cubre el plan.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: fn_precio_consulta + 2 triggers corriendo en ExamLab + Plan_Backup_VetCare con sus 6 secciones (1 pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 4/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 53]
Repasar checklist del dia con [Slide 53] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 4 - VetCare.docx`. Clave para usted: `Quiz Clase 4 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 55]
**Decir:** «Queda avanzado: >=1 funcion + >=1 trigger + borrador plan de respaldo. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 55] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 04_func_trigger_backup.sql.

## Capturas
Carpeta `Kit docente/Clase 4/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
