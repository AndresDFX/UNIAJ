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


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Tema y objetivo

QUÉ ES (dilo así): Hoy la base deja de ser solo un lugar donde se guardan datos y empieza a defenderse sola: funciones que calculan, triggers que reaccionan sin que nadie los llame, y un plan para el día en que algo salga mal.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema en voz alta y haz la pregunta de arranque: «si mañana alguien conecta un programa nuevo a la base y se salta la aplicación, ¿qué reglas siguen protegiendo los datos?». Deja que respondan 1-2 personas.
- Clic 1: Cierra: «al final de hoy van a poder responder eso con nombres concretos: CHECK, trigger, función, y qué hacer si de todos modos se pierde algo».

PASA A LA SIGUIENTE: Empezamos por la diferencia que más confunde: función y procedimiento.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido de las dos horas: teoría con una lámina por concepto, demo sobre la base de la clínica y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] Funcion y procedimiento: se distinguen por su papel, no por su sintaxis

QUÉ ES (dilo así): Función y procedimiento se parecen mucho al escribirlos, así que no se distinguen por la sintaxis sino por para qué se usan. La función devuelve un valor y vive dentro de una consulta; el procedimiento ejecuta acciones (insertar, validar, actualizar) y se invoca con CALL.

CÓMO DARLA (≈4 min):
- Al entrar: Columna izquierda completa: «el SELECT llama a fn_precio_consulta, la función calcula 40000 y ese valor vuelve a la consulta como una columna más del resultado». Subraya que la función no cambió ningún dato.
- Clic 1: Columna derecha: «el CALL ejecuta sp_agendar_cita, que valida y escribe: aparece una fila nueva en cita». Aquí el resultado no es un valor, es un cambio en la tabla.
- Clic 2: Lee la conclusión y pregunta: «¿calcular el precio de una consulta es función o procedimiento? ¿Y registrar una cita?».

EJEMPLO: SELECT nombre, fn_precio_consulta(especie, FALSE) AS tarifa FROM mascota; devuelve una tarifa por cada mascota, como si fuera una columna calculada.

SI PREGUNTAN:
- «¿Una función puede hacer INSERT?» → En PostgreSQL técnicamente sí, pero no conviene: dentro de un SELECT el motor decide cuántas veces la ejecuta. Si hay que modificar datos, es un procedimiento.
- «¿Puedo hacer SELECT de un procedimiento?» → No: el motor responde que es un procedimiento y que se llama con CALL.

CUIDADO: No digas «la función es la que devuelve algo y el procedimiento no devuelve nada» como regla absoluta: el criterio es el uso (valor dentro de una consulta vs. acción).

PASA A LA SIGUIENTE: Veamos una función real de la clínica y la palabra que más se olvida: IMMUTABLE.

### [Slide 5] La funcion de tarifas, y por que IMMUTABLE importa

QUÉ ES (dilo así): Una función completa que calcula un recargo de fin de semana. Sirve para ver el molde entero y entender IMMUTABLE.

CÓMO DARLA (≈3 min):
- Al entrar: Recorre de arriba abajo: nombre y parámetros (línea 1), RETURNS DECIMAL (qué tipo devuelve), LANGUAGE plpgsql, IMMUTABLE, y el cuerpo entre $$.
- Clic 1: En el cuerpo: si el día es sábado o domingo (DOW 6 o 0) devuelve la base por 1,25; si no, la base. Cada camino termina en un RETURN.
- Clic 2: Lee el comentario final: IMMUTABLE significa «mismos argumentos, mismo resultado, siempre», y por eso el motor puede guardar el resultado o usar la función en un índice.

EJEMPLO: fn_recargo_festivo(100000, DATE '2026-10-04') — 4 de octubre de 2026 es domingo — devuelve 125000.00.

SI PREGUNTAN:
- «¿Por qué no puede ser IMMUTABLE si usa NOW()?» → Porque con los mismos argumentos el resultado cambia según el momento. Una función que lee la hora o una tabla es STABLE o VOLATILE.
- «¿Qué pasa si declaro IMMUTABLE algo que no lo es?» → El motor confía en la promesa y puede devolver resultados viejos o incorrectos, sobre todo si la función se usa en un índice.

CUIDADO: No confundir con Oracle: aquí es RETURNS (no RETURN ... IS) y el cuerpo va entre $$.

PASA A LA SIGUIENTE: Ahora la función de tarifas de la clínica y sus tres detalles finos.

### [Slide 6] Los tres detalles de fn_precio_consulta

QUÉ ES (dilo así): La función de tarifas tiene tres decisiones pequeñas que evitan errores reales: comparar el texto sin importar mayúsculas, no dejar ninguna especie sin precio y no dejar que un NULL contamine la cuenta.

CÓMO DARLA (≈4 min):
- Al entrar: UPPER: tres formas de escribir la especie llegan a UPPER() y salen iguales. Pregunta: «sin UPPER, ¿cuánto cobraría 'canino' en minúscula?» (respuesta: 35000, porque caería en el ELSE).
- Clic 1: CASE: la especie normalizada elige su fila: CANINO 45000, FELINO 40000, cualquier otra 35000. Subraya que el ELSE es una decisión de negocio.
- Clic 2: COALESCE: si la casilla de urgencia llega vacía (NULL), COALESCE la vuelve FALSE y no hay recargo. Sin él, base * NULL da NULL y la factura sale vacía.
- Clic 3: Conclusión: la función nunca devuelve NULL; toda entrada tiene tarifa.

EJEMPLO: fn_precio_consulta('canino', NULL) → 45000. fn_precio_consulta('FELINO', TRUE) → 54000 (40000 × 1,35).

SI PREGUNTAN:
- «¿Un IF con NULL no se trata ya como falso?» → Sí, el IF no entra; el problema aparece cuando el NULL entra en una cuenta: ahí todo el resultado se vuelve NULL.

CUIDADO: El recargo de urgencia es 1,35 (35 %); revisa que el número que digas coincida con el de la lámina siguiente.

PASA A LA SIGUIENTE: Juntemos todo en la firma completa de la función.

### [Slide 7] La funcion de tarifas: RETURNS NUMERIC, CASE, COALESCE e IMMUTABLE

QUÉ ES (dilo así): Esta lámina reúne la función completa y los tres errores que más aparecen al escribirla: copiar RETURNS TRIGGER del trigger, olvidar UPPER() y declarar IMMUTABLE una función que consulta tablas.

CÓMO DARLA (≈3 min):
- Al entrar: Recorre la ilustración de arriba abajo: CREATE FUNCTION + nombre, parámetros con su tipo, RETURNS NUMERIC y la volatilidad IMMUTABLE. Abajo, por qué RETURNS TRIGGER está tachado y qué promete IMMUTABLE.

EJEMPLO: SELECT nombre, especie, fn_precio_consulta(especie, FALSE) AS normal, fn_precio_consulta(especie, TRUE) AS urgencia FROM mascota;

SI PREGUNTAN:
- «¿Dónde filtro las mascotas inactivas?» → En el WHERE de la consulta que llama a la función. Si la función leyera la tabla mascota dejaría de ser IMMUTABLE (sería STABLE).

CUIDADO: RETURNS TRIGGER solo existe para la función que ejecuta un trigger; si aparece aquí, la función no se puede usar en un SELECT.

PASA A LA SIGUIENTE: Pasamos al objeto que nadie invoca: el trigger.

### [Slide 8] El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos

QUÉ ES (dilo así): Todo lo anterior se ejecuta porque alguien lo llama. El trigger no: se declara una vez y el motor lo ejecuta cada vez que ocurre el evento. En PostgreSQL se escribe en dos piezas separadas.

CÓMO DARLA (≈4 min):
- Al entrar: Las dos piezas: arriba la función fn_trg_audit_cita() RETURNS TRIGGER y la asociación CREATE TRIGGER … AFTER UPDATE OF estado ON cita, que apunta a la función. Abajo, la tabla cita y la tabla audit_cita, todavía vacía.
- Clic 1: Llega un UPDATE que cambia el estado de la cita 7 de 'confirmada' a 'atendida'. Nadie ha llamado al trigger.
- Clic 2: El cambio es el evento: el motor dispara la asociación, que ejecuta la función, y aparece la fila en audit_cita con el antes y el después.
- Clic 3: Lee la frase: «nadie lo llama: lo dispara el evento». Ese es todo el concepto.

EJEMPLO: Cada vez que recepción cambia el estado de una cita, queda registrado quién y cuándo, sin que la aplicación tenga que acordarse.

SI PREGUNTAN:
- «Creé la función y no pasa nada.» → Falta la segunda pieza, el CREATE TRIGGER. Sin asociación la función nunca se ejecuta.

CUIDADO: No dictes la forma de Oracle (cuerpo dentro del CREATE TRIGGER y :NEW con dos puntos): en PostgreSQL no compila.

PASA A LA SIGUIENTE: ¿En qué momento corre el trigger, antes o después de escribir la fila? Eso cambia lo que puede hacer.

### [Slide 9] BEFORE o AFTER, y que significa el valor que se retorna

QUÉ ES (dilo así): La diferencia entre BEFORE y AFTER es el momento, y el momento decide qué se puede hacer. En BEFORE lo que la función retorna es lo que se guarda; en AFTER la fila ya está guardada.

CÓMO DARLA (≈4 min):
- Al entrar: La fila NEW viaja por la vía y llega a BEFORE, todavía sin escribir.
- Clic 1: Lo que BEFORE puede retornar: NEW (se guarda tal cual), NEW cambiado (se guarda la versión cambiada) o NULL (la operación se cancela sin aviso).
- Clic 2: La fila se escribe y llega a AFTER: ya está en la tabla, así que el retorno se ignora (se escribe RETURN NEW por convención).
- Clic 3: La regla práctica: para rechazar, RAISE EXCEPTION, nunca RETURN NULL.

EJEMPLO: BEFORE: poner el estado en mayúsculas o rechazar un stock negativo. AFTER: escribir la fila de auditoría.

SI PREGUNTAN:
- «¿Por qué no usar RETURN NULL para rechazar?» → Porque no da error: la aplicación cree que guardó y el dato nunca llegó. RAISE EXCEPTION aborta y avisa con un mensaje.

CUIDADO: Poner AFTER en el trigger que debe impedir algo es el error más común: cuando corre, el dato ya está escrito.

PASA A LA SIGUIENTE: Veamos el trigger BEFORE que impide un stock negativo, en código.

### [Slide 10] BEFORE o AFTER: uno puede impedir, el otro solo registrar

QUÉ ES (dilo así): Un trigger BEFORE completo que impide que el stock de un insumo quede negativo. Son las dos piezas: la función y la asociación.

CÓMO DARLA (≈3 min):
- Al entrar: La función: si NEW.stock < 0, RAISE EXCEPTION con el id y el valor; si no, RETURN NEW para que la fila se guarde.
- Clic 1: La asociación: BEFORE UPDATE OF stock ON insumo, FOR EACH ROW, EXECUTE FUNCTION. Solo se dispara cuando cambia la columna stock.
- Clic 2: Lee el comentario: en BEFORE, devolver NULL cancelaría sin aviso; por eso se usa RAISE EXCEPTION.

EJEMPLO: Con 3 unidades, UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 → ERROR: Stock negativo en el insumo 2 (-7). El stock sigue en 3.

SI PREGUNTAN:
- «¿El error deshace solo esa fila?» → Deshace toda la sentencia (y la transacción en curso, si no se maneja): nada del UPDATE queda escrito.

PASA A LA SIGUIENTE: El uso donde los triggers brillan de verdad: la auditoría.

### [Slide 11] La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado

QUÉ ES (dilo así): Un trigger de auditoría guarda el antes y el después de cada cambio. Es el mejor uso de un trigger porque nadie puede saltárselo. La cláusula WHEN decide qué cambios valen la pena registrar.

CÓMO DARLA (≈4 min):
- Al entrar: UPDATE 1: pendiente → confirmada. Cambió el estado, el WHEN lo deja pasar y aparece la primera fila en audit_cita.
- Clic 1: UPDATE 2: confirmada → atendida. Otra vez cambió: segunda fila.
- Clic 2: UPDATE 3: atendida → atendida. No cambió nada: el WHEN lo detiene y no se escribe nada.
- Clic 3: Resultado: tres UPDATE, dos filas. Sin el WHEN serían tres, y la auditoría se llenaría de ruido.

SI PREGUNTAN:
- «¿Por qué IS DISTINCT FROM y no <>?» → Porque si uno de los dos es NULL, <> devuelve NULL y el cambio no se registra. IS DISTINCT FROM trata NULL como un valor comparable.

CUIDADO: En la demo ejecuta los tres UPDATE y muestra la tabla audit_cita; si no se ve el resultado, el grupo concluye que el trigger no hizo nada.

PASA A LA SIGUIENTE: El código completo de este trigger.

### [Slide 12] La auditoria de cita: funcion, trigger y WHEN

QUÉ ES (dilo así): El trigger de auditoría completo, con sus dos piezas rotuladas.

CÓMO DARLA (≈3 min):
- Al entrar: Pieza 1, la función: inserta en audit_cita el id, la acción y el estado anterior y nuevo. Usuario y fecha los pone la tabla por DEFAULT. Termina en RETURN NEW.
- Clic 1: Pieza 2, la asociación: AFTER UPDATE OF estado ON cita, FOR EACH ROW, con el WHEN que descarta los no-cambios, y EXECUTE FUNCTION.
- Clic 2: Señala que NEW y OLD van sin dos puntos (en Oracle llevan dos puntos).

EJEMPLO: Después de los tres UPDATE: SELECT accion, valor_anterior, valor_nuevo FROM audit_cita; → 2 filas.

CUIDADO: El trigger es invisible para quien solo lee el código de la aplicación: documéntalo junto al esquema.

PASA A LA SIGUIENTE: Ahora el trigger que no registra sino que impide.

### [Slide 13] El trigger que impide: el hueco que el CHECK no tapa

QUÉ ES (dilo así): La demo retira a propósito el CHECK (stock >= 0) para mostrar qué pasa sin defensa, y luego la defensa con un trigger. La lección no es «trigger mejor que CHECK»: es saber cuándo cada uno.

CÓMO DARLA (≈4 min):
- Al entrar: Sin defensa: el UPDATE resta 10 a un insumo con 3 unidades y la base guarda −7. Pregunta: «¿qué significa tener −7 vacunas?».
- Clic 1: Con el trigger BEFORE: el mismo UPDATE choca con RAISE EXCEPTION, se rechaza y el stock sigue en 3.
- Clic 2: La regla: si cabe en un CHECK, va en un CHECK; el trigger es para lo que necesita mirar otra fila u otra tabla.

SI PREGUNTAN:
- «Entonces, ¿para qué el trigger si el CHECK ya lo hacía?» → Para esta regla, no hace falta. El trigger se justifica cuando la regla consulta otra tabla, por ejemplo que la mascota esté activa al agendar.

CUIDADO: Si no retiras el CHECK antes de la demo, el UPDATE falla por la restricción y nadie ve el trigger actuar.

PASA A LA SIGUIENTE: Ordenemos dónde va cada regla: las cuatro capas.

### [Slide 14] Las cuatro capas, y en cual vive cada regla

QUÉ ES (dilo así): Cada regla tiene una capa natural, y el orden de las capas es el orden de preferencia: lo más simple y difícil de saltarse primero.

CÓMO DARLA (≈4 min):
- Al entrar: Las cuatro capas, de la más preferida a la menos. Léelas en orden.
- Clic 1: Dos reglas caen en su capa: «stock >= 0» en CHECK; «un veterinario, una franja» en UNIQUE (id_veterinario, fecha_hora).
- Clic 2: Otras dos: «auditar el cambio de estado» en trigger; «el formato del correo» en la aplicación.
- Clic 3: Cierre: lo que solo vive en la aplicación se salta conectándose por otra vía (como hicimos con SET ROLE en la Clase 2).

SI PREGUNTAN:
- «¿La doble reserva no es para un trigger que cuente citas?» → No: un UNIQUE la impide siempre, incluso con dos usuarios a la vez. El trigger que cuenta puede fallar con concurrencia (se ve en la Clase 10).

PASA A LA SIGUIENTE: Una guía rápida para decidirlo con preguntas.

### [Slide 15] Donde vive cada validacion: CHECK, trigger o aplicacion

QUÉ ES (dilo así): Las mismas cuatro capas convertidas en preguntas: la primera respuesta «sí» decide dónde va la regla.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre el árbol con dos reglas del grupo: pide una regla de la clínica y bájenla pregunta por pregunta hasta su capa.

EJEMPLO: «Una cita no puede ser en domingo» → mira solo su fila → CHECK. «No agendar a una mascota inactiva» → mira otra tabla → trigger o procedimiento.

PASA A LA SIGUIENTE: ¿Y cuándo un trigger es mala idea?

### [Slide 16] Cuando NO se usa un trigger, y lo que un trigger no ve

QUÉ ES (dilo así): Los triggers son poderosos pero invisibles. Estos cuatro casos son señales de que la regla debe vivir en otro lado.

CÓMO DARLA (≈3 min):
- Al entrar: Caso 1: si una restricción declarativa lo resuelve, no se escribe trigger.
- Clic 1: Caso 2: un descuento que el administrador puede autorizar: el trigger no distingue el caso autorizado.
- Clic 2: Caso 3: enviar un correo dentro del trigger alarga la transacción y la deja esperando a un servicio externo.
- Clic 3: Caso 4: lógica con varios pasos va en un procedimiento, que se llama a propósito y se prueba solo.

CUIDADO: Un trigger también se ejecuta en cargas masivas: un UPDATE de 10.000 filas dispara 10.000 veces un trigger FOR EACH ROW.

PASA A LA SIGUIENTE: Cambiamos de tema: proteger y recuperar los datos.

### [Slide 17] Seguridad y respaldo: dos preguntas complementarias

QUÉ ES (dilo así): Seguridad y respaldo responden preguntas distintas. La seguridad reduce la probabilidad de daño; el respaldo reduce cuánto duele cuando el daño ocurre.

CÓMO DARLA (≈3 min):
- Al entrar: Los dos lados: el escudo (roles y permisos de la Clase 2) y la base que se copia.
- Clic 1: pg_dump -Fc -d clinica -f clinica_AAAAMMDD.dump: copia una base, tablas y datos, en formato que permite restaurar selectivamente.
- Clic 2: pg_dumpall --globals-only: copia los roles, que pg_dump no incluye porque son del servidor, no de la base.

SI PREGUNTAN:
- «Si restauro el dump, ¿vuelven los permisos?» → Los GRANT sobre las tablas sí, pero si los roles no existen en el servidor nuevo, nadie puede entrar. Por eso se respaldan aparte.

PASA A LA SIGUIENTE: Un plan de respaldo de verdad tiene seis partes.

### [Slide 18] Plan de respaldo: 6 secciones y herramientas reales de PostgreSQL

QUÉ ES (dilo así): Un plan de respaldo no es una lista de comandos: dice cuánto se puede perder, en cuánto se vuelve y cómo se comprueba que la vuelta funciona.

CÓMO DARLA (≈3 min):
- Al entrar: Recorre las seis tarjetas en orden. Detente en la 2 (la hora se justifica con el negocio: dump a las 20:30 porque la facturación cierra a las 20:00) y en la 5: un respaldo que nunca se restauró es solo un archivo.

EJEMPLO: Retención 7 diarias, 4 semanales y 12 mensuales, con una copia fuera del servidor.

PASA A LA SIGUIENTE: Las dos siglas del plan que más se confunden: RPO y RTO.

### [Slide 19] RPO y RTO: dos siglas que solo sirven con un numero acordado

QUÉ ES (dilo así): RPO mira hacia atrás (cuánto de lo último se pierde); RTO mira hacia adelante (cuánto tarda en volver). Los dos se fijan con el negocio, no con el administrador de la base.

CÓMO DARLA (≈4 min):
- Al entrar: La línea de tiempo: el último respaldo y el momento en que la base se cae.
- Clic 1: Lo que hay entre el respaldo y la caída se pierde: eso es el RPO. Lo que tarda en volver: el RTO.
- Clic 2: Con números de la clínica: 4 horas de RPO son 15 a 20 citas sin registro; 8 horas de RTO un sábado es cerrar el día.
- Clic 3: Quién decide: el dueño del negocio, porque es quien paga la pérdida.

SI PREGUNTAN:
- «¿Con un dump diario cuál es el RPO?» → Hasta 24 horas. Si es demasiado, hace falta archivado continuo del WAL.

PASA A LA SIGUIENTE: ¿Qué de todo esto podemos ejecutar en el navegador?

### [Slide 20] Lo que PostgreSQL en el navegador si puede demostrar, y lo que se documenta en papel

QUÉ ES (dilo así): La herramienta del curso es PostgreSQL ejecutándose dentro del navegador. Todo el código SQL de hoy funciona ahí; las herramientas de respaldo no, porque necesitan archivos y un servidor.

CÓMO DARLA (≈2 min):
- Al entrar: Columna izquierda: lo que se ejecuta y se ve. Columna derecha: lo que se escribe en el plan con su comando exacto.

CUIDADO: No digas «la herramienta no sirve para respaldos»: la razón precisa es que esos programas leen y escriben archivos del servidor.

PASA A LA SIGUIENTE: Cómo se conecta lo de hoy con lo que ya vimos.

### [Slide 21] Como amarra con las clases vecinas

QUÉ ES (dilo así): Nada de hoy es nuevo del todo: cada pieza se apoya en una clase anterior, y lo de hoy se usa en las siguientes.

CÓMO DARLA (≈2 min):
- Al entrar: Recorre la cadena de izquierda a derecha y cierra con lo que viene: la Clase 8 retoma la transacción dentro de la que corre todo trigger, y la Clase 10 explica por qué un trigger que cuenta no evita la doble reserva.

PASA A LA SIGUIENTE: Vamos a la demo.

### [Slide 22] Demo del dia

QUÉ ES (dilo así): La demo muestra en vivo lo que se explicó: una función que se usa en una consulta, un trigger que audita y un trigger que impide.

CÓMO DARLA (≈15 min):
- Al entrar: 1) CREATE de fn_precio_consulta y SELECT con la tarifa por mascota. 2) Las dos piezas del trigger de auditoría; tres UPDATE de estado (el tercero sin cambio) y SELECT de audit_cita: 2 filas. 3) Quitar el CHECK, UPDATE a −7, crear el trigger BEFORE, repetir: error y stock en 3.

CUIDADO: Muestra siempre el SELECT del resultado: el trigger es invisible si no se mira la tabla.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** fn_precio_consulta + fn_trg_audit_cita con su CREATE TRIGGER ... EXECUTE FUNCTION, en ExamLab, y el esqueleto del plan de respaldo.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 4 - Funciones disparadores seguridad respaldo/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 4 · Funciones · Triggers · Seguridad y respaldo
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Funcion y procedimiento: se distinguen por su papel, no por su sintaxis
5. La funcion de tarifas, y por que IMMUTABLE importa
6. Los tres detalles de fn_precio_consulta
7. La funcion de tarifas: RETURNS NUMERIC, CASE, COALESCE e IMMUTABLE
8. El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos
9. BEFORE o AFTER, y que significa el valor que se retorna
10. BEFORE o AFTER: uno puede impedir, el otro solo registrar
11. La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado
12. La auditoria de cita: funcion, trigger y WHEN
13. El trigger que impide: el hueco que el CHECK no tapa
14. Las cuatro capas, y en cual vive cada regla
15. Donde vive cada validacion: CHECK, trigger o aplicacion
16. Cuando NO se usa un trigger, y lo que un trigger no ve
17. Seguridad y respaldo: dos preguntas complementarias
18. Plan de respaldo: 6 secciones y herramientas reales de PostgreSQL
19. RPO y RTO: dos siglas que solo sirven con un numero acordado
20. Lo que PostgreSQL en el navegador si puede demostrar, y lo que se documenta en papel
21. Como amarra con las clases vecinas
22. Demo del dia
23. Cierre · Clase 4

> Privado, no se proyecta: `Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Funciones · Triggers · Seguridad y respaldo.»
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
- Funcion (Clase 3 vio procedimiento): retorna un valor y se usa DENTRO de una expresion SQL, ej. SELECT fn_precio_consulta(especie, urgencia) FROM mascota. Su molde es CREATE FUNCTION nombre(params) RETURNS tipo LANGUAGE plpgsql AS $fn$ ... $fn$;. Si no toca datos se marca IMMUTABLE, que le dice al motor que puede memorizar el resultado. Nada de RETURN NUMBER IS: eso es Oracle.
- Trigger (disparador): bloque de codigo que el motor ejecuta AUTOMATICAMENTE cuando ocurre un evento (BEFORE/AFTER INSERT, UPDATE o DELETE) sobre una tabla, sin que nadie lo llame explicitamente. Dos usos tipicos aqui: auditoria (guardar quien/cuando cancelo una cita) y validacion de invariantes (que el stock nunca quede negativo tras un UPDATE).
- En PostgreSQL un trigger son SIEMPRE dos objetos, no uno: la funcion y la asociacion. Primero CREATE FUNCTION fn_trg_x() RETURNS TRIGGER, que termina en RETURN NEW (o RETURN OLD si el evento es DELETE); despues CREATE TRIGGER trg_x AFTER UPDATE OF estado ON cita FOR EACH ROW EXECUTE FUNCTION fn_trg_x();. Dentro de la funcion las filas se leen como NEW y OLD, SIN los dos puntos: NEW.estado, no :NEW.estado. Escribir el cuerpo dentro del CREATE TRIGGER es la herencia de Oracle que mas cuesta puntos, porque no compila.
- BEFORE o AFTER no es un detalle de estilo: un trigger que VALIDA va BEFORE, porque tiene que abortar antes de que el dato quede escrito; un trigger que AUDITA va AFTER, porque registra un hecho ya consumado. Y la clausula WHEN (OLD.estado IS DISTINCT FROM NEW.estado) evita registrar los UPDATE que no cambiaron nada: es la diferencia entre auditar 2 filas y auditar 3.
- Riesgo real de los triggers: son invisibles en el codigo de la app (un desarrollador que solo mira el INSERT no ve que ademas se dispara una auditoria), y pueden encadenarse (un trigger que dispara otro trigger) generando efectos dificiles de rastrear. Se usan para pocas reglas criticas, no para toda la logica de negocio: una regla sobre una sola columna es un CHECK, una regla que compara filas es un trigger, y una regla de interfaz es de la app.
- Seguridad y respaldo van juntos: seguridad evita que datos se corrompan o se filtren; respaldo (backup) asume que igual algo saldra mal y prepara la recuperacion. Full backup (copia completa), incremental (solo lo que cambio desde el ultimo backup) y diferencial (todo lo que cambio desde el ultimo FULL) son las tres estrategias base. En PostgreSQL las herramientas son pg_dump (una base), pg_dumpall --globals-only (los roles del cluster, que pg_dump NO respalda) y pg_basebackup con archivado de WAL.
- RPO (Recovery Point Objective) = cuantos datos se puede permitir perder, medido en tiempo ('maximo 1 hora de citas perdidas'). RTO (Recovery Time Objective) = cuanto tiempo puede estar caida la BD antes de restaurar. Un backup diario sin probar el restore no cumple ningun RPO/RTO real: un plan de respaldo sin prueba de restauracion es solo una promesa.
- Error de docente que no domina el tema: presentar el backup como 'copiar el archivo de vez en cuando' sin frecuencia, retencion (cuantas copias se guardan) ni prueba de restore — eso es lo que el taller de esta clase pide explicitamente que el estudiante defina. El segundo error es dictar el trigger como en Oracle, con el cuerpo dentro del CREATE TRIGGER y :NEW/:OLD: la rubrica lo penaliza expresamente, asi que el docente estaria proyectando el codigo por el que va a descontar.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 22]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: fn_precio_consulta + fn_trg_audit_cita con su CREATE TRIGGER ... EXECUTE FUNCTION, en ExamLab, y el esqueleto del plan de respaldo.
Herramienta: ExamLab (PostgreSQL) + Google Docs
📸 trg_audit_cita: los 3 UPDATE dejan 2 filas de auditoria (el WHEN filtra el tercero) [[captura: cap01_demo.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 4 - Funciones disparadores seguridad respaldo/Taller PI - Clase 4 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: >=1 funcion + >=1 trigger + borrador plan de respaldo
Actividades:
1. Escribir fn_precio_consulta(especie, urgencia) RETURNS NUMERIC en PL/pgSQL y probarla con SELECT sobre las 3 especies.
2. Crear la tabla audit_cita y el trigger de auditoria en sus dos objetos: fn_trg_audit_cita() RETURNS TRIGGER + CREATE TRIGGER ... EXECUTE FUNCTION.
3. Crear el trigger de stock no negativo (BEFORE UPDATE), evidenciando primero que sin el el stock llega a -7.
4. Decidir donde vive cada validacion: CHECK, trigger o aplicacion (pregunta 4).
5. Redactar Plan_Backup_VetCare con sus 6 secciones (plantilla en este documento): que se respalda y con que, frecuencia, retencion, RPO/RTO, restore de prueba con quien firma, y que NO cubre el plan.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: fn_precio_consulta + 2 triggers corriendo en ExamLab + Plan_Backup_VetCare con sus 6 secciones (1 pag.)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 4/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 4 - VetCare.docx`. Clave para usted: `Quiz Clase 4 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 23]
**Decir:** «Queda visto: Funciones · Triggers · Seguridad y respaldo. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 23] slide de cierre. Dudas finales.


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
