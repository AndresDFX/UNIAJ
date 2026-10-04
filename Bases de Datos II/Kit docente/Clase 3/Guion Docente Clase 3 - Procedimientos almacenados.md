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


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): Hasta hoy la base guardaba datos y decidía quién los toca. Hoy empieza a contener comportamiento: un procedimiento almacenado que agenda una cita solo si la regla de negocio se cumple, y una forma ordenada de probar que la regla de verdad se cumple.

CÓMO DARLA (≈4 min):
- Al entrar: Recuerda el cierre de la Clase 1: la FK acepta una cita para una mascota inactiva. Pregunta: «¿dónde ponemos esa regla para que ninguna pantalla se la salte?».
- Cierre del encuadre: «Hoy la escribimos dentro de la base, la hacemos abortar cuando no se cumple y demostramos con pruebas que funciona».

CUIDADO: Todo el código de hoy es PL/pgSQL de PostgreSQL. Si alguien escribe IS, VARCHAR2 o la barra final de Oracle, el error es de sintaxis, no de lógica.

PASA A LA SIGUIENTE: El recorrido de las dos horas.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): Las dos horas en cinco tramos: encuadre, teoría con una lámina por concepto, demo en vivo, práctica opcional y cierre.

CÓMO DARLA (≈1 min):
- Al entrar: Señala los tramos sin detenerte. La práctica tiene su guía en la carpeta de la clase y es opcional.

PASA A LA SIGUIENTE: Qué es un procedimiento almacenado, en dos palabras.

### [Slide 4] Que es un procedimiento almacenado, y las dos palabras que importan

QUÉ ES (dilo así): Un procedimiento almacenado es un bloque de código con nombre que vive en la base. Dos palabras lo explican: guardado, porque su fuente queda en el motor aunque su autor se vaya, e invocado, porque una sola línea dispara varias sentencias. Lo importante no es el ahorro: es que la regla queda escrita una vez y ninguna pantalla se la puede saltar.

CÓMO DARLA (≈3 min):
- Al entrar: GUARDADO: el motor tiene un catálogo (pg_proc) con sp_agendar_cita y sp_registrar_consulta. «Si cierran la pestaña, el procedimiento sigue ahí».
- Clic 1: INVOCADO: CALL sp_agendar_cita(…) dispara adentro un SELECT (¿mascota activa?), un IF con RAISE EXCEPTION y el INSERT. Una línea, varias sentencias, una sola respuesta.
- Clic 2: La frase de abajo: la regla queda escrita una vez y todos pasan por ella.

EJEMPLO: SELECT pg_get_functiondef('sp_agendar_cita'::regproc); devuelve la definición completa, empezando por «CREATE OR REPLACE PROCEDURE public.sp_agendar_cita(IN p_id_mascota integer, …», lista para volver a ejecutar.

SI PREGUNTAN:
- «Ejecuté el CREATE y no dio error: ¿ya funciona?» → No necesariamente. PostgreSQL revisa la sintaxis al crearlo, pero los nombres de tablas y columnas solo al ejecutarlo: un INSERT INTO citas (con s) se crea sin queja y falla en el CALL con relation "citas" does not exist. La evidencia es el CALL corriendo.

CUIDADO: Si vienes de Oracle: aquí no existe el objeto «creado pero inválido». Si el CREATE no protestó, el objeto existe; eso no quiere decir que funcione.

PASA A LA SIGUIENTE: ¿Por qué ponerlo en la base y no repetir el SQL en cada pantalla?

### [Slide 5] Por que un procedimiento y no SQL en cada pantalla

QUÉ ES (dilo así): Antes y después de poner la regla en un procedimiento: sin él, cada pantalla la reescribe a su manera; con él, vive una vez en la base y vale igual para la aplicación, un script de carga o soporte.

CÓMO DARLA (≈2 min):
- Al entrar: Lee las dos columnas emparejadas, fila por fila: reescribir la regla en cada pantalla contra escribirla una vez; alguien la olvida contra todos la respetan; SQL armado con texto (inyección) contra parámetros tipados; cambiarla en N lugares contra cambiarla en uno.

EJEMPLO: La regla «una mascota inactiva no agenda» escrita en la pantalla de agenda no protege una carga masiva desde un archivo; escrita en sp_agendar_cita, sí, si la carga usa el procedimiento.

CUIDADO: La tercera fila (inyección) se explica completa dentro de unas láminas; aquí solo nómbrala.

PASA A LA SIGUIENTE: Veamos cómo se escribe uno: el molde de PL/pgSQL.

### [Slide 6] El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar

QUÉ ES (dilo así): El molde de un procedimiento es siempre el mismo, y se dicta entero antes de escribir una sola validación, porque es donde más se pierde tiempo sin haber entendido nada mal. Lo raro es el cuerpo entre signos de dólar: para el motor el cuerpo es un texto, y así no hay que duplicar comillas.

CÓMO DARLA (≈3 min):
- Al entrar: El molde completo y la primera trampa: después de LANGUAGE plpgsql va AS. En Oracle es IS; aquí IS da error de sintaxis.
- Clic 1: Se resalta el cuerpo, de DECLARE a END;: es una cadena. Entre $proc$ caben punto y coma y comillas sin duplicarlas. $$ funciona igual; la etiqueta con nombre sirve para bloques anidados.
- Clic 2: El cierre: $proc$; con punto y coma obligatorio. La barra sola en una línea, que en Oracle cierra el bloque, aquí es error.

EJEMPLO: CREATE PROCEDURE sp_y(p INT) LANGUAGE plpgsql IS $proc$ ... responde «syntax error at or near "IS"».

SI PREGUNTAN:
- «¿Por qué LANGUAGE plpgsql si es obvio?» → Porque PostgreSQL admite varios lenguajes (sql, plpgsql y otros) y no adivina cuál se usa.
- «¿Qué tipos uso?» → INT, NUMERIC, TEXT, VARCHAR(n), TIMESTAMP, BOOLEAN, DATE. VARCHAR2 y NUMBER son de Oracle y aquí no existen.

CUIDADO: sp_agendar_cita recibe tres parámetros, no cuatro: id_cita es SERIAL y lo genera el motor. Pasarlo desde afuera no es error de sintaxis: es error de diseño.

PASA A LA SIGUIENTE: El molde completo, en un procedimiento que corre.

### [Slide 7] El molde de un procedimiento en PL/pgSQL

QUÉ ES (dilo así): Un procedimiento completo y pequeño: da de baja un insumo poniendo su stock en cero, después de comprobar que existe. Tiene todas las piezas del molde.

CÓMO DARLA (≈2 min):
- Líneas 1-4: La firma: nombre y dos parámetros con su tipo (INT y VARCHAR). Los dos son IN, el modo por omisión.
- Líneas 5-6: LANGUAGE plpgsql y AS $proc$: aquí empieza el cuerpo.
- Líneas 7-8: DECLARE: la variable local v_stock.
- Líneas 10-13: SELECT ... INTO v_stock y, si no encontró fila, RAISE EXCEPTION con el id. Primero se valida.
- Líneas 14-16: Después se escribe: UPDATE del stock a cero y un RAISE NOTICE que informa sin abortar.
- Líneas 17-18: END; y $proc$; con su punto y coma.

EJEMPLO: CALL sp_dar_de_baja_insumo(1, 'vencido'); imprime «Insumo 1 dado de baja (12 unidades): vencido». CALL sp_dar_de_baja_insumo(9999, 'inexistente'); responde «El insumo 9999 no existe».

SI PREGUNTAN:
- «¿Qué diferencia hay entre RAISE NOTICE y RAISE EXCEPTION?» → NOTICE solo imprime un mensaje y el procedimiento sigue; EXCEPTION aborta y deshace lo que se había escrito.

CUIDADO: La leyenda menciona $proc$: el código usa la misma etiqueta para que no parezcan dos sintaxis distintas.

PASA A LA SIGUIENTE: Los parámetros tienen dirección, y eso decide cómo se devuelve un error.

### [Slide 8] Los modos de parametro, y por que hoy no se usa OUT

QUÉ ES (dilo así): Cada parámetro tiene un modo, que es la dirección en que viaja el dato. IN entra y es el de omisión; OUT sale; INOUT entra y sale. Hoy no se usa OUT para devolver errores, y la razón es de diseño: un código que nadie revisa deja la cita creada.

CÓMO DARLA (≈2 min):
- Al entrar: p_id_mascota INT entra al procedimiento: es IN, y no hace falta escribirlo.
- Clic 1: La alternativa mala: el procedimiento inserta y además pone p_resultado := -1 en un OUT. La aplicación no lo mira, nada falla, y la regla no se cumplió.
- Clic 2: La buena: RAISE EXCEPTION. El motor devuelve un fallo que la aplicación no puede ignorar, y nada quedó escrito. Lee la frase final: el encabezado es un contrato de nombre, orden y tipos.

EJEMPLO: En PostgreSQL el OUT de un procedimiento también se pasa al llamarlo: con sp_out(p_id INT, OUT p_res INT), CALL sp_out(4) falla (no existe ese procedimiento con un argumento) y CALL sp_out(4, NULL) devuelve p_res = 8.

SI PREGUNTAN:
- «¿Cómo evito confundir el orden de dos parámetros del mismo tipo?» → Con notación nombrada: CALL sp_agendar_cita(p_id_mascota => 1, p_id_veterinario => 2, p_fecha_hora => TIMESTAMP '2026-09-15 10:00:00').

CUIDADO: Si alguien intercambia dos parámetros INT en la firma, el procedimiento se crea igual y agenda la cita para la mascota equivocada sin ningún error.

PASA A LA SIGUIENTE: Ese RAISE EXCEPTION es la pieza que convierte el código en regla.

### [Slide 9] RAISE EXCEPTION: la validacion que aborta y deshace

QUÉ ES (dilo así): RAISE EXCEPTION lanza un error con un mensaje y aborta. No sale del procedimiento con un aviso: el error llega hasta quien llamó y todo lo que el procedimiento había escrito se deshace. Por eso es imposible que quede una cita a medias, y no porque el código lo cuide: lo garantiza el motor.

CÓMO DARLA (≈3 min):
- Al entrar: La línea RAISE EXCEPTION 'ERROR: la mascota % no existe', p_id: el % se reemplaza por p_id (99) y el mensaje queda «ERROR: la mascota 99 no existe». Para un porcentaje literal se escribe %%.
- Clic 1: Dentro del CALL: se hizo un INSERT, luego una validación falla y se lanza la excepción. La fila 3 que se había insertado desaparece: se deshizo.
- Clic 2: La conclusión y la segunda idea: el mensaje es parte de la interfaz; se escribe para la recepcionista, no para el programador.

EJEMPLO: Si hay más % que valores, el motor responde «too few parameters specified for RAISE». Y todo RAISE EXCEPTION sin más lleva el código SQLSTATE P0001.

SI PREGUNTAN:
- «¿Para qué sirve el SQLSTATE?» → Para que la aplicación distinga un error de negocio de un fallo de la base sin leer el texto. Se puede fijar uno propio con USING ERRCODE; hoy basta el mensaje.

CUIDADO: El orden natural es validar primero y escribir después; aun así, si algo falla tarde, el motor deshace lo escrito.

PASA A LA SIGUIENTE: Veámoslo con la regla que la FK no podía defender.

### [Slide 10] RAISE EXCEPTION en accion: la mascota inactiva

QUÉ ES (dilo así): La regla que quedó pendiente en la Clase 1: una mascota inactiva no agenda. Un bloque DO la prueba con la mascota 3, Rocky, que existe pero está inactiva.

CÓMO DARLA (≈2 min):
- Líneas 2-4: Un bloque DO, que se ejecuta una vez y no se guarda, con p_id_mascota = 3.
- Líneas 5-8: IF NOT EXISTS (mascota con ese id Y activa = 'S'): consulta OTRA tabla, que es justo lo que un CHECK no puede hacer. Si no existe tal fila, RAISE EXCEPTION.
- Línea 10: La salida real: ERROR: La mascota 3 no existe o esta inactiva.
- Líneas 12-14: Los comentarios: RAISE EXCEPTION no solo avisa, deshace; por eso se valida primero y se escribe después.

EJEMPLO: Con p_id_mascota = 1 (Firulais, activa) el bloque termina sin mensaje: la condición del IF es falsa.

SI PREGUNTAN:
- «¿Por qué un solo mensaje para «no existe» y «está inactiva»?» → Aquí se juntan para mostrar el mecanismo. En el procedimiento de la siguiente lámina se separan, porque la aplicación necesita distinguirlos.

PASA A LA SIGUIENTE: El mismo mecanismo dentro del procedimiento real de la clínica.

### [Slide 11] El molde de PL/pgSQL y la validacion que aborta

QUÉ ES (dilo así): El procedimiento central de la clase, con su molde completo y sus tres validaciones: la mascota debe existir, debe estar activa y la franja del veterinario debe estar libre. Si alguna falla, el CALL aborta y no inserta nada.

CÓMO DARLA (≈3 min):
- Líneas 1-2: Tres parámetros: mascota, veterinario y fecha_hora. id_cita no se pasa porque es SERIAL.
- Línea 3: LANGUAGE plpgsql AS $proc$: ni IS, ni VARCHAR2, ni barra final.
- Líneas 6-9: SELECT activa INTO v_activa y, enseguida, IF NOT FOUND: la mascota no existe.
- Líneas 10-12: IF v_activa <> 'S': la mascota está inactiva.
- Líneas 13-16: IF EXISTS una cita no cancelada del mismo veterinario a esa hora: la franja está ocupada. Una cita CANCELADA no cuenta, porque libera la franja.
- Líneas 17-19: Solo si las tres pasan, el INSERT con estado 'PROGRAMADA'.

EJEMPLO: CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-15 10:00:00') inserta; con la mascota 3 responde «ERROR: la mascota 3 esta inactiva», con la 99 «ERROR: la mascota 99 no existe», y CALL sp_agendar_cita(2, 1, TIMESTAMP '2026-09-01 08:00:00') «ERROR: el veterinario 1 ya tiene cita en 2026-09-01 08:00:00». Ninguno de los tres deja filas nuevas. El cliente muestra «ERROR:  ERROR: …» porque el mensaje ya trae la palabra ERROR.

SI PREGUNTAN:
- «¿Por qué IF NOT FOUND va antes que el IF de activa?» → Porque un SELECT INTO sin filas no lanza error en PL/pgSQL: deja v_activa en NULL, y NULL <> 'S' no entra al IF. Sin NOT FOUND, el INSERT llega a la FK y sale un error técnico de clave foránea en vez del mensaje del contrato.
- «Si ya está el IF EXISTS, ¿para qué la restricción de unicidad?» → Porque el IF EXISTS es código: dos sesiones a la vez pueden pasar las dos la comprobación. La restricción la garantiza el motor; el IF EXISTS da el mensaje claro. El porqué completo es de la Clase 10.

CUIDADO: La leyenda lo dice: con el mensaje en un parámetro OUT, el INSERT seguiría corriendo. El error se lanza, no se devuelve.

PASA A LA SIGUIENTE: ¿Toda la lógica debe ir en la base? La respuesta honesta.

### [Slide 12] Donde debe vivir la logica de negocio: la respuesta honesta

QUÉ ES (dilo así): La pregunta de fondo no tiene respuesta dogmática. A favor de la base: la regla se cumple aunque alguien entre por fuera de la aplicación, se ahorran viajes de red y se pueden dar permisos más finos. En contra: se versiona peor, se prueba con más esfuerzo y ata el sistema al motor. El criterio: en la base van las reglas que nunca pueden violarse.

CÓMO DARLA (≈3 min):
- Al entrar: Tres entradas, aplicación, migración y consola, pasan por sp_agendar_cita antes de llegar a cita. «La regla se cumple entre por donde se entre».
- Clic 1: Los permisos: GRANT EXECUTE sobre el procedimiento sí, GRANT INSERT sobre cita no. Lee el aviso: eso solo funciona si el procedimiento es SECURITY DEFINER (corre con los permisos de su dueño); sin esa cláusula corre con los de quien llama y el INSERT se niega.
- Clic 2: A favor y en contra. Cierra con el criterio de oficio: invariantes en la base; orquestación, interfaz y reglas que cambian seguido, en la aplicación.

EJEMPLO: Invariantes de la clínica: el stock nunca negativo y la mascota inactiva que no agenda. Regla volátil: el descuento de temporada, que cambia cada mes.

SI PREGUNTAN:
- «¿Un procedimiento es más rápido?» → Ahorra viajes de red y análisis repetido, pero no arregla una consulta mal escrita; eso se ve en las Clases 6 y 7. En el navegador la mejora de red no se puede medir.

CUIDADO: SECURITY DEFINER se nombra hoy y se usa en la Clase 12; no prometas que dar EXECUTE basta.

PASA A LA SIGUIENTE: Uno de los argumentos a favor merece su lámina: la inyección de SQL.

### [Slide 13] La inyeccion de SQL, explicada y no solo mencionada

QUÉ ES (dilo así): La inyección ocurre cuando la aplicación arma la consulta pegando texto que escribió el usuario, y ese texto termina interpretado como código. Un parámetro lo evita por un motivo preciso: el motor analiza la sentencia antes de conocer el valor, así que el valor nunca vuelve a pasar por el analizador.

CÓMO DARLA (≈3 min):
- Al entrar: El usuario escribe Luna, la aplicación arma … WHERE nombre = 'Luna' y devuelve a Luna. Todo bien.
- Clic 1: Escribe Luna' OR '1'='1: la sentencia queda WHERE nombre = 'Luna' OR '1'='1', que es siempre verdadera, y la pantalla lista todas las mascotas.
- Clic 2: Con parámetro: 1) el motor analiza la sentencia, 2) después llega el valor, 3) se compara como dato. Ninguna mascota se llama Luna' OR '1'='1. Lee el aviso final sobre EXECUTE.

EJEMPLO: Si escribe '; DELETE FROM cita; -- el motor recibe dos sentencias y la segunda borra la agenda.

SI PREGUNTAN:
- «¿Entonces un procedimiento es inmune?» → No. Si dentro alguien escribe EXECUTE 'SELECT ... WHERE nombre = ' || p_nombre, el agujero se reabre. Lo correcto es EXECUTE '... WHERE nombre = $1' USING p_nombre, o format con %L para valores y %I para nombres.

CUIDADO: Regla dura del curso: ningún dato del usuario se concatena dentro de una sentencia, ni en la aplicación ni en el procedimiento.

PASA A LA SIGUIENTE: Ya sabemos escribir el procedimiento. ¿Cómo demostramos que funciona?

### [Slide 14] La bateria de pruebas: por que un bloque DO por caso

QUÉ ES (dilo así): Un procedimiento sin pruebas no está terminado. El problema práctico: si se escriben los cuatro CALL seguidos y se ejecutan de un tiro, el primero que falla aborta el resto. La solución es un bloque DO por caso, cuya cláusula EXCEPTION atrapa el error y deja correr el siguiente.

CÓMO DARLA (≈2 min):
- Al entrar: Cuatro CALL de un tiro: el positivo pasa, el de la mascota inactiva falla y los otros dos quedan en gris: nunca corrieron.
- Clic 1: Un bloque DO por caso: DO $$ BEGIN CALL … EXCEPTION … END $$;. «Se ejecuta una vez y no se guarda en ningún catálogo».
- Clic 2: La tabla resultado_prueba con una fila por caso: caso, esperado, obtenido y paso.

EJEMPLO: Los cuatro casos con los datos de práctica: mascota 1 (activa, debe agendar), mascota 3 (Rocky, inactiva), mascota 99 (no existe) y la franja del veterinario 1 el 2026-09-01 a las 08:00 (ocupada).

SI PREGUNTAN:
- «¿Y si el procedimiento hace COMMIT?» → Llamado desde un bloque con EXCEPTION falla con «invalid transaction termination»: ese bloque abre un punto de retorno interno y no se puede confirmar con él activo. Por eso el procedimiento de hoy no lleva COMMIT.

CUIDADO: La captura tiene costo: no se envuelve todo en EXCEPTION «por si acaso». Es para las pruebas y para los casos que se quieren manejar.

PASA A LA SIGUIENTE: Así se escribe un caso de error completo.

### [Slide 15] La bateria de pruebas: un bloque DO por caso

QUÉ ES (dilo así): Un caso de error completo sobre el procedimiento del insumo: debe fallar, y debe fallar por la razón esperada. El resultado queda en la tabla, no en la pantalla.

CÓMO DARLA (≈2 min):
- Líneas 2-4: El bloque DO llama con el insumo 9999, que no existe.
- Líneas 5-6: Si el CALL termina sin error, la prueba falló: se registra «no lanzo error» con paso FALSE.
- Líneas 7-11: Si cae en EXCEPTION, se registra SQLERRM (el texto del error) y paso es la comparación SQLERRM ILIKE '%no existe%': falló Y por lo esperado.
- Líneas 13-14: El SELECT final y su salida real: insumo 9999 | El insumo 9999 no existe | t.

EJEMPLO: El caso OK se escribe al revés: si el CALL termina, se registra OK con paso TRUE; si cae en EXCEPTION, se registra SQLERRM con paso FALSE.

SI PREGUNTAN:
- «¿Dónde está la tabla resultado_prueba?» → Se crea antes: resultado_prueba(id_prueba SERIAL, caso TEXT, esperado TEXT, obtenido TEXT, paso BOOLEAN).

CUIDADO: Sin el ILIKE, un procedimiento roto (una columna mal escrita) también caería en EXCEPTION y la prueba saldría aprobada.

PASA A LA SIGUIENTE: El molde general de un caso de error, y la prueba que nadie piensa.

### [Slide 16] El molde de un caso de error y la prueba del conteo

QUÉ ES (dilo así): El molde de un caso de error invierte la lógica habitual: llegar al final sin excepción es el fallo. Y la batería se cierra con una prueba que nadie piensa: contar las citas antes y después.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre la imagen: el bloque DO con sus dos salidas (sin error, se registra «FALLO: no lanzó error»; con error, se registra SQLERRM), los cuatro casos y, abajo, el conteo de cita: 10 antes, 11 después.

EJEMPLO: Si el conteo diera 14, los tres casos de error habrían dejado filas: el procedimiento se queja pero escribe igual.

SI PREGUNTAN:
- «¿Por qué el conteo si ya tengo resultado_prueba?» → Porque la tabla prueba que el procedimiento se queja; el conteo prueba que el caso válido escribió y que los tres errores no dejaron basura.

CUIDADO: El conteo depende de los datos: con los de práctica son 10 citas al empezar. Si la base ya tenía pruebas anteriores, se recrea antes de medir.

PASA A LA SIGUIENTE: Falta la trampa más cara: qué significa la columna paso.

### [Slide 17] Que significa la columna paso, y la trampa del WHEN OTHERS

QUÉ ES (dilo así): Capturar WHEN OTHERS y marcar la prueba como superada porque hubo excepción no prueba nada: un procedimiento roto también lanza excepciones. Lo que se verifica es el texto del error, con SQLERRM. Así se afirma que falló y que falló por lo esperado.

CÓMO DARLA (≈3 min):
- Al entrar: Caso negativo, mascota inactiva, contra un procedimiento roto: una columna mal escrita da «column "activ" does not exist». También es una excepción.
- Clic 1: WHEN OTHERS THEN paso := TRUE: la prueba sale aprobada. Falso positivo.
- Clic 2: paso := SQLERRM ILIKE '%inactiva%': el texto no dice «inactiva», paso queda en f y el error queda a la vista.
- Clic 3: Las dos frases finales: se afirma que falló Y por qué; y una sola lectura de paso para las cuatro filas, declarada.

EJEMPLO: ILIKE compara sin importar mayúsculas: 'ERROR: la mascota 3 esta inactiva' ILIKE '%inactiva%' es verdadero.

SI PREGUNTAN:
- «¿Puedo usar SQLSTATE en vez del texto?» → Sí, si el procedimiento fija un código propio con USING ERRCODE. Con RAISE EXCEPTION simple todos los errores de negocio son P0001, así que hoy se compara el texto.

CUIDADO: Al revisar una batería, no te quedes con las cuatro filas en t: mira cómo se calculó paso.

PASA A LA SIGUIENTE: Las dos lecturas posibles de paso, lado a lado.

### [Slide 18] La columna paso y la trampa de WHEN OTHERS

QUÉ ES (dilo así): La columna paso admite dos lecturas legítimas. Si significa «coincidió con lo esperado», con el procedimiento correcto las cuatro filas quedan en t. Si significa «la operación se completó», los tres casos de error quedan en f aunque el procedimiento esté perfecto. Las dos valen; lo que no vale es no decir cuál.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre la imagen: arriba, paso := TRUE (mal) contra SQLERRM ILIKE (bien); en el medio, la misma tabla con la lectura A (t, t, t, t) y la B (t, f, f, f); abajo, la regla: una lectura para las cuatro filas, declarada.

EJEMPLO: Salida de una batería sana con la lectura A: 4 filas, el caso válido con paso t y los tres inválidos con paso t y su SQLERRM literal.

SI PREGUNTAN:
- «¿Qué hago si un caso de error sale con paso f en la lectura A?» → Es un hallazgo: el procedimiento dejó pasar algo que debía rechazar. Se corrige el procedimiento, no la prueba.

PASA A LA SIGUIENTE: Probado el procedimiento, falta documentarlo para quien lo va a llamar.

### [Slide 19] El contrato del procedimiento: los 6 bloques que consume la app

QUÉ ES (dilo así): El contrato no es código: es lo que necesita quien va a llamar al procedimiento sin abrirlo, por ejemplo quien construya la aplicación. Sirve si permite escribir la llamada y manejar los errores sin leer el cuerpo. Son seis bloques y cada uno responde una pregunta.

CÓMO DARLA (≈2 min):
- Al entrar: Bloques 1 y 2: firma exacta (¿cómo se declara?) y ejemplo de llamada (¿cómo se invoca?).
- Clic 1: Bloques 3 y 4: precondiciones (¿qué debe ser verdad antes?) y postcondiciones (¿qué queda?, y si falla, nada).
- Clic 2: Bloques 5 y 6: tabla de errores con el mensaje literal, y la decisión de diseño (¿por qué aborta?). La frase final: errores del contrato y de la batería, palabra por palabra.

EJEMPLO: Sin la postcondición del caso malo («si falla, no queda nada»), quien llama no sabe si tiene que limpiar algo después de un error.

CUIDADO: El contrato no es un resumen del código: si para escribir la llamada hay que leer el cuerpo, el contrato no sirve.

PASA A LA SIGUIENTE: Los seis bloques, llenos para sp_agendar_cita.

### [Slide 20] Los 6 bloques del contrato, uno por uno

QUÉ ES (dilo así): El contrato de sp_agendar_cita, lleno. Lo que lo vuelve útil es que se puede copiar la llamada y programar la respuesta a cada error sin abrir el procedimiento.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre la tarjeta de arriba abajo: la firma con tipos; el CALL de ejemplo con la mascota 1, el veterinario 2 y el 15 de septiembre a las 10:00; las precondiciones; la postcondición con su «NADA cambia»; la tabla de errores (mensaje literal y qué hace la aplicación); y la decisión de diseño.

EJEMPLO: Fila de la tabla de errores: «ERROR: la mascota 3 esta inactiva» → la aplicación avisa que hay que reactivar la mascota antes de agendar.

SI PREGUNTAN:
- «¿El mensaje del tercer error tiene que ser ese?» → No: es el que cada uno escriba en su RAISE EXCEPTION. Lo que se exige es que el contrato y la batería usen exactamente el mismo texto.

CUIDADO: Una paráfrasis en la tabla de errores rompe el contrato: la aplicación compara contra el texto exacto.

PASA A LA SIGUIENTE: Una distinción que se dice hoy y no en la Clase 4: procedimiento y función.

### [Slide 21] Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4

QUÉ ES (dilo así): Un procedimiento se invoca para que haga algo, con CALL; una función se invoca para que devuelva un valor, dentro de una expresión. No son dos sabores del mismo objeto: solo el procedimiento puede confirmar o deshacer la transacción, y el motor no deja usar uno donde va el otro.

CÓMO DARLA (≈2 min):
- Al entrar: PROCEDIMIENTO · hace: CALL sp_agendar_cita(…) cambia los datos y puede hacer COMMIT o ROLLBACK.
- Clic 1: FUNCIÓN · devuelve: SELECT fn_x(…) entrega un valor a la consulta y no puede hacer COMMIT ni ROLLBACK. «No son dos sabores del mismo objeto».
- Clic 2: La prueba: SELECT sp_agendar_cita(…) responde «is a procedure» con la pista «To call a procedure, use CALL». El motor no deja confundirlos.

EJEMPLO: Al revés también falla: CALL de una función responde «is not a procedure» y sugiere usar SELECT.

SI PREGUNTAN:
- «¿Por qué el objeto de hoy es procedimiento?» → Porque agendar es una acción que cambia datos. La tarifa de una consulta, que es un valor, será una función en la Clase 4.

PASA A LA SIGUIENTE: Una función real, y el error al revés, en código.

### [Slide 22] PROCEDURE o FUNCTION: la diferencia es donde se puede usar

QUÉ ES (dilo así): Una función de una línea que cuenta las citas de un día y se usa dentro de un SELECT, y el error que da intentar lo mismo con un procedimiento.

CÓMO DARLA (≈2 min):
- Líneas 2-8: CREATE FUNCTION con RETURNS INT y LANGUAGE sql: el cuerpo es una sola consulta. p_dia + 1 es el día siguiente, así que el rango es medio abierto: desde las 00:00 hasta antes de la medianoche.
- Línea 10: SELECT fn_citas_del_dia(DATE '2026-09-01'): con los datos de práctica devuelve 3.
- Líneas 12-14: SELECT de un procedimiento: «sp_dar_de_baja_insumo(integer, unknown) is a procedure».

EJEMPLO: La función se puede usar en una lista de columnas: SELECT d::date, fn_citas_del_dia(d::date) FROM generate_series(DATE '2026-09-01', DATE '2026-09-03', INTERVAL '1 day') d;

SI PREGUNTAN:
- «¿Una función tiene que ser LANGUAGE sql?» → No: puede ser plpgsql igual que un procedimiento. Esta es sql porque su cuerpo es una sola consulta.

CUIDADO: «unknown» en el mensaje es el tipo del literal 'x' sin conversión: no es un error aparte.

PASA A LA SIGUIENTE: La regla para decidir, en una sola pregunta.

### [Slide 23] PROCEDURE o FUNCTION: cual se puede usar dentro de un SELECT

QUÉ ES (dilo así): La decisión se toma con una sola pregunta: ¿el resultado tiene que entrar en una consulta? Si sí, es función. Si lo que se necesita es ejecutar pasos o manejar la transacción, es procedimiento.

CÓMO DARLA (≈1 min):
- Al entrar: Recorre el árbol: la pregunta arriba, FUNCTION a la izquierda (RETURNS, SELECT nombre, fn_precio(especie) FROM mascota) y PROCEDURE a la derecha (CALL; el SELECT se rechaza). Abajo, los tres mitos tachados.

EJEMPLO: Calcular el precio sugerido de una consulta según la especie, para mostrarlo en un listado: función que devuelve NUMERIC.

SI PREGUNTAN:
- «¿Un OUT no hace que el procedimiento «devuelva» un valor?» → Devuelve valores a quien hace el CALL, pero sigue sin poder ir dentro de un SELECT. Devolver por OUT no es lo mismo que ser invocable en una consulta.

PASA A LA SIGUIENTE: Cuando algo no funciona: depurar sin depurador.

### [Slide 24] Depurar sin depurador: los cuatro movimientos, en PostgreSQL

QUÉ ES (dilo así): Sin depurador también se depura, con cuatro movimientos: saber qué error se está leyendo, dejar trazas, aislar la consulta sospechosa y probar con casos hechos a propósito.

CÓMO DARLA (≈2 min):
- Al entrar: ¿Qué error leo? El del CREATE PROCEDURE es de sintaxis y señala línea y posición. El del CALL es de ejecución: ahí salen las tablas y columnas mal escritas.
- Clic 1: Trazas: RAISE NOTICE 'paso 2, v_activa = %', v_activa; imprime sin abortar. RAISE tiene niveles (NOTICE, WARNING, EXCEPTION) y solo el último aborta.
- Clic 2: Aislar: SELECT activa FROM mascota WHERE id_mascota = 3, suelto, con el valor que falló. Así se sabe si falla la consulta o la lógica que la rodea.
- Clic 3: Casos deliberados: uno correcto y tres de error, cada uno en su bloque DO.

EJEMPLO: Un procedimiento con INSERT INTO citas (con s) se crea sin error; el CALL responde «relation "citas" does not exist». Es un error de ejecución, no de creación.

CUIDADO: A diferencia de Oracle, no hay vista de errores que consultar ni objetos inválidos: si el CREATE no protestó, el objeto existe.

PASA A LA SIGUIENTE: El motor de hoy y lo que no hay que copiar de Oracle.

### [Slide 25] El motor de hoy es PostgreSQL, y eso decide que se puede demostrar

QUÉ ES (dilo así): Todo lo de hoy corre en PostgreSQL dentro del navegador: CREATE PROCEDURE, el dólar, RAISE EXCEPTION, los bloques DO y SQLERRM. Oracle queda como contraste para quien lo encuentre en el trabajo, con cuatro diferencias que vale la pena nombrar y no más.

CÓMO DARLA (≈1 min):
- Al entrar: Las cuatro parejas: IS → AS; VARCHAR2 y NUMBER → TEXT e INT; RAISE_APPLICATION_ERROR → RAISE EXCEPTION; la barra final → error de sintaxis.
- Clic 1: La regla operativa: la fuente de verdad es el archivo .sql de la carpeta. Quien reconstruye procedimiento, pruebas y datos pegando su archivo, va bien.

CUIDADO: No dediques más de un minuto a Oracle: cada minuto en la sintaxis del otro motor es un minuto que no se dedica al tema.

PASA A LA SIGUIENTE: Un segundo procedimiento, donde se practica otra decisión.

### [Slide 26] El segundo procedimiento: sp_registrar_consulta y el EXISTS

QUÉ ES (dilo así): El segundo procedimiento registra la consulta de una cita. La tabla ya tiene UNIQUE en id_cita, así que el motor impide dos consultas para la misma cita. Entonces, ¿para qué validar? Por el mensaje, y porque hay reglas que la restricción no ve.

CÓMO DARLA (≈3 min):
- Al entrar: Solo con UNIQUE, la segunda consulta para la cita 7 falla con «duplicate key value violates unique constraint "consulta_id_cita_key"»: técnico, nombra el índice.
- Clic 1: Con IF EXISTS (SELECT 1 FROM consulta WHERE id_cita = p_id_cita) THEN RAISE: «ERROR: la cita 7 ya tiene consulta registrada». Lo entiende la recepcionista.
- Clic 2: Lo que el UNIQUE no ve: si la cita existe y si no está CANCELADA. La frase: la restricción es la última línea de defensa; el procedimiento, la primera.

EJEMPLO: Con los datos de práctica: la cita 1 está PROGRAMADA y no tiene consulta (debe funcionar), la cita 4 está CANCELADA (debe fallar) y la cita 2 ya tiene consulta (debe fallar).

SI PREGUNTAN:
- «Si ya está el procedimiento, ¿quito el UNIQUE?» → No. El procedimiento mejora el mensaje; la restricción sigue protegiendo cuando alguien entra por fuera. Primero lo declarativo, encima el procedimiento.

CUIDADO: El orden importa: el IF EXISTS va antes del INSERT; si se deja chocar contra el UNIQUE, la aplicación recibe un error que no sabe traducir.

PASA A LA SIGUIENTE: Cómo se conecta todo esto con las clases vecinas.

### [Slide 27] Como amarra con las clases vecinas

QUÉ ES (dilo así): Lo de hoy usa lo que dejaron las clases anteriores y lo retoman las siguientes.

CÓMO DARLA (≈1 min):
- Al entrar: Antes: la Clase 1 dejó el esquema y la baja lógica; la Clase 2, los roles y la idea de EXECUTE en vez de INSERT; hoy, los procedimientos.
- Clic 1: Después: la Clase 4 decide para cada regla si va en CHECK, trigger o aplicación; la 8 retoma quién confirma la transacción; la 12 consume estos procedimientos desde la aplicación.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 28] Demo del dia

QUÉ ES (dilo así): La demo junta lo de hoy: el procedimiento con sus validaciones, los CALL que abortan con su mensaje literal, la batería de pruebas en resultado_prueba y el conteo que demuestra que los errores no dejaron nada.

CÓMO DARLA (≈15 min):
- Al entrar: 1) CREATE de sp_agendar_cita con las tres validaciones (4 min). 2) CALL con la mascota 1: cita creada; con la 3 y con la 99: lee cada mensaje en voz alta (3 min). 3) La batería: cuatro bloques DO y SELECT * FROM resultado_prueba ORDER BY id_prueba (5 min). 4) SELECT COUNT(*) FROM cita: de 10 a 11; y pg_get_functiondef para mostrar que quedó guardado (3 min).

CUIDADO: Recrea los datos antes de la demo si ya hiciste pruebas: el conteo de 10 a 11 solo vale sobre la base recién sembrada.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 3 - Procedimientos almacenados/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 3 · Procedimientos almacenados · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es un procedimiento almacenado, y las dos palabras que importan
5. Por que un procedimiento y no SQL en cada pantalla
6. El molde de PL/pgSQL, y por que el cuerpo va entre signos de dolar
7. El molde de un procedimiento en PL/pgSQL
8. Los modos de parametro, y por que hoy no se usa OUT
9. RAISE EXCEPTION: la validacion que aborta y deshace
10. RAISE EXCEPTION en accion: la mascota inactiva
11. El molde de PL/pgSQL y la validacion que aborta
12. Donde debe vivir la logica de negocio: la respuesta honesta
13. La inyeccion de SQL, explicada y no solo mencionada
14. La bateria de pruebas: por que un bloque DO por caso
15. La bateria de pruebas: un bloque DO por caso
16. El molde de un caso de error y la prueba del conteo
17. Que significa la columna paso, y la trampa del WHEN OTHERS
18. La columna paso y la trampa de WHEN OTHERS
19. El contrato del procedimiento: los 6 bloques que consume la app
20. Los 6 bloques del contrato, uno por uno
21. Procedimiento y funcion: la diferencia se dice hoy, no en la Clase 4
22. PROCEDURE o FUNCTION: la diferencia es donde se puede usar
23. PROCEDURE o FUNCTION: cual se puede usar dentro de un SELECT
24. Depurar sin depurador: los cuatro movimientos, en PostgreSQL
25. El motor de hoy es PostgreSQL, y eso decide que se puede demostrar
26. El segundo procedimiento: sp_registrar_consulta y el EXISTS
27. Como amarra con las clases vecinas
28. Demo del dia
29. Cierre · Clase 3

> Privado, no se proyecta: `Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Procedimientos almacenados · VetCare.»
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
- Un procedimiento almacenado es logica de negocio guardada DENTRO de la base, y se llama con CALL. No es una consulta con nombre: recibe parametros tipados y ejecuta varias sentencias como una sola unidad logica, de modo que la regla vive UNA vez y toda la app la respeta.
- El molde de PL/pgSQL es fijo: CREATE PROCEDURE nombre(params) LANGUAGE plpgsql AS $proc$ ... $proc$;. Dentro van DECLARE (variables), BEGIN y END. Los delimitadores $proc$ (dollar-quoting) existen porque el cuerpo lleva punto y coma y el motor necesita saber donde termina. Nada de IS en vez de AS, ni VARCHAR2, ni NUMBER, ni RAISE_APPLICATION_ERROR, ni la barra / final: eso es Oracle y aqui no compila.
- Parametros: IN es el defecto y no se escribe; OUT e INOUT existen pero hoy no se usan para reportar errores. Los tipos son los de PostgreSQL: INT, NUMERIC, TEXT, TIMESTAMP, BOOLEAN.
- La validacion no devuelve un mensaje: aborta con RAISE EXCEPTION 'ERROR: ... %', variable;. El % se sustituye en orden por las variables que siguen a la coma. Al abortar, todo lo que el procedimiento hubiera hecho se deshace, asi que es imposible que quede una cita a medias. Con un mensaje en un parametro OUT el INSERT seguiria corriendo: la regla no se cumpliria.
- Un procedimiento sin prueba no esta terminado: la bateria son bloques DO que capturan el error. Cada caso va en su propio bloque DO $$ BEGIN ... EXCEPTION WHEN OTHERS THEN ... SQLERRM ... END $$;, y el resultado se escribe en una tabla resultado_prueba (caso, esperado, obtenido, paso). Un caso OK y tres casos error, mas el COUNT(*) que demuestra que la tabla cita paso de 10 a 11 filas.
- Procedimiento y funcion se diferencian hoy, no en la Clase 4: CALL sp_x(...) frente a SELECT fn_x(...). El procedimiento se ejecuta como una accion y puede manejar transacciones; la funcion retorna un valor y se invoca dentro de una expresion SQL. En PostgreSQL una funcion no puede hacer COMMIT ni ROLLBACK, y eso es lo que decide cual de los dos se usa.
- El contrato del proc es lo que consume la futura app: firma, precondiciones, postcondiciones y errores. Son 6 bloques: la firma exacta con tipos, un ejemplo de CALL, las precondiciones, las postcondiciones, la tabla de errores con su mensaje literal, y la decision de diseno que explica por que se aborta en vez de devolver un codigo.
- Error de docente que no domina el tema: escribir el proc sin validar nada (solo el INSERT) y llamarlo 'logica de negocio' — un proc sin reglas de validacion es solo una consulta con nombre. El segundo error es dictar el molde de Oracle porque es el que uno recuerda: en ExamLab ese codigo no compila, y el estudiante pierde los 35 puntos de la pregunta 1 por sintaxis, no por no entender el tema.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 28]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: sp_agendar_cita en PL/pgSQL dentro de ExamLab: las 3 validaciones con RAISE EXCEPTION y la bateria de bloques DO que las prueba.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 Bateria de pruebas de sp_agendar_cita: P1 OK y P2 rechazado por mascota inactiva [[captura: salida-proc-ok-y-error.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 3 - Procedimientos almacenados/Taller PI - Clase 3 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: >=1 procedimiento de negocio (agendar cita / registrar consulta)
Actividades:
1. Escribir sp_agendar_cita en PL/pgSQL y ejecutarlo en ExamLab (LANGUAGE plpgsql, dollar-quoting, sin sintaxis de Oracle).
2. Incluir las 3 validaciones de negocio del PI, cada una con su RAISE EXCEPTION y su mensaje literal.
3. Correr la bateria de pruebas con bloques DO: 1 caso OK + 3 casos error, escritos en resultado_prueba, mas el COUNT(*) de cita antes y despues.
4. Escribir sp_registrar_consulta, comprobando con EXISTS antes de chocar contra la restriccion UNIQUE.
5. Redactar el contrato del proc en sus 6 bloques (plantilla en este documento) y pegarlo en la pregunta 5.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: 2 procedimientos en PL/pgSQL corriendo en ExamLab + bateria de pruebas con su tabla resultado_prueba + contrato del proc (6 bloques)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 3/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 3 - VetCare.docx`. Clave para usted: `Quiz Clase 3 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 29]
**Decir:** «Queda visto: Procedimientos almacenados · VetCare. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 29] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 03_procs_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 3/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
