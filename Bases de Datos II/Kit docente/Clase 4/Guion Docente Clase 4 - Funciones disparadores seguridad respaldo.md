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

**[Slide 4] Funcion y procedimiento: se distinguen por su papel, no por su sintaxis** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un procedimiento se invoca para que HAGA algo y se llama con CALL; una funcion se invoca para que DEVUELVA un valor, y ese valor se usa dentro de una expresion SQL, como en AS tarifa
  - El molde es el mismo de la Clase 3 con una linea mas: RETURNS NUMERIC LANGUAGE plpgsql IMMUTABLE AS $fn$... $fn$;.
  - Nada de RETURN NUMBER IS: eso es Oracle y aqui no compila.
  - La palabra que hay que desempacar es IMMUTABLE, porque es una de las tres categorias de volatilidad que PostgreSQL define y el estudiante no las conoce.
  - IMMUTABLE promete que con los mismos argumentos la funcion devuelve siempre lo mismo y que no lee ni escribe la base; el motor puede entonces evaluarla una sola vez y reutilizar el resultado, e incluso resolverla al planificar.
  - STABLE promete que el resultado no cambia DENTRO de una misma sentencia, y es lo que corresponde a una funcion que consulta tablas.
  - VOLATILE es el valor por omision y significa que puede devolver cualquier cosa cada vez. fn_precio_consulta es IMMUTABLE porque solo depende de sus dos parametros.
  - El contraejemplo util es fn_edad_mascota calculando la edad con now() por dentro: no es inmutable, porque manana devuelve otro numero para la misma mascota
  - Y por eso no puede sostener un indice sobre expresion de los que se veran en la Clase 7; la correccion es de una linea, pasar la fecha de referencia como parametro.
  - Vale advertir que declarar IMMUTABLE una funcion que si lee tablas no produce un error, produce algo peor: resultados obsoletos que el motor considera correctos.
  - Hay un segundo efecto que hay que dimensionar con numeros porque conecta con la Clase 6: una funcion invocada dentro de un SELECT se ejecuta una vez por fila evaluada.
  - Si fn_saldo_factura(p_id_factura) hace un SUM sobre detalle_factura y la consulta recorre diez mil facturas, el motor ejecuta diez mil consultas internas; el resultado es correcto y el tiempo es inaceptable.
  - La alternativa es una consulta con GROUP BY, y esa comparacion es material directo de la Clase 6.
  - NOTAS:
  - Una funcion y un procedimiento se parecen tanto en la escritura que conviene separarlos por su papel y no por su sintaxis.
  - RETURNS declara el tipo del valor devuelto, y dentro del cuerpo tiene que haber al menos un RETURN, porque una funcion de PL/pgSQL que termina sin retornar lanza un error en ejecucion.
  - CÓDIGO CITADO (referencia):
  - SELECT m.nombre, fn_precio_consulta(m.especie, FALSE)
  - FROM mascota m WHERE m.activa = 'S'
  - CREATE OR REPLACE FUNCTION fn_precio_consulta(p_especie TEXT, p_urgencia BOOLEAN)

**[Slide 5] La funcion de tarifas, y por que IMMUTABLE importa** — 15 vinetas.

**[Slide 6] Los tres detalles de fn_precio_consulta que valen puntos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La funcion de la clase tiene tres decisiones pequenas, y ninguna es evidente.
  - La primera es UPPER sobre la especie.
  - Se escribe CASE UPPER(p_especie) WHEN 'CANINO' THEN 45000 WHEN 'FELINO' THEN 40000 ELSE 35000 END
  - Y el ELSE no es pereza: es la definicion de negocio de que cualquier otra especie tarifa 35000, de modo que la funcion nunca devuelve nulo por una especie que nadie previo.
  - La segunda es COALESCE sobre la urgencia.
  - Se escribe IF COALESCE(p_urgencia, FALSE) THEN, que traduce ausencia de dato a no urgente.
  - La tercera es el recargo como multiplicacion y no como suma escrita a mano: v_base:= v_base * 1.35 en lugar de sumar un valor calculado aparte.
  - Con 45000 el resultado es 60750 exactos, y conviene proyectar ese numero porque es el que el estudiante va a comparar contra su propia salida.
  - El tipo de retorno es NUMERIC y no FLOAT por la razon de la Clase 1: el dinero no se representa en binario.
  - NOTAS:
  - La aplicacion de la clínica puede mandar 'Canino', 'canino' o 'CANINO', y comparar el texto tal como llega significa que dos de las tres formas caen al precio de otra especie.
  - Si la casilla de urgencia llega en nulo, que es lo que hace una interfaz donde el usuario no marco nada, entonces IF p_urgencia THEN no entra —nulo no es verdadero— pero cualquier aritmetica con nulo si contamina: v_base * p_urgencia daria nulo y la factura saldria vacia.
  - Vale decir en voz alta el criterio general, porque reaparece todo el semestre: en SQL, nulo no significa falso, significa desconocido, y toda comparacion con nulo devuelve nulo.

**[Slide 7] El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un trigger se distingue de todo lo anterior en que nadie lo llama: se declara una vez y el motor lo ejecuta cuando ocurre el evento declarado, un INSERT, un UPDATE o un DELETE sobre una tabla.
  - Y aqui esta la pieza de sintaxis central del dia: en PostgreSQL un trigger son SIEMPRE dos objetos separados, no uno.
  - Primero la funcion, RETURNS TRIGGER LANGUAGE plpgsql AS $fn$... $fn$;, que no recibe parametros declarados y cuyo tipo de retorno es literalmente TRIGGER.
  - Dos notas de sintaxis que ahorran tiempo: dentro de la funcion las filas se leen como NEW y OLD SIN los dos puntos —NEW.estado, no:NEW.estado, que aqui es un error de sintaxis—, y en la asociacion se escribe EXECUTE FUNCTION
  - El detalle que cambia todo el analisis, y que rara vez se dice, es que el trigger corre dentro de la misma transaccion de la sentencia que lo activo.
  - El orden de creacion es fijo: primero la funcion RETURNS TRIGGER y despues el CREATE TRIGGER que la asocia a la tabla.
  - Mientras el trigger exista, la funcion no se puede borrar con un DROP FUNCTION simple: hace falta CASCADE, que elimina tambien el trigger.
  - NOTAS:
  - Despues la asociacion,;, que dice cuando dispararla y a quien llamar.
  - No existe la forma de Oracle con el cuerpo dentro del CREATE TRIGGER.
  - EXECUTE PROCEDURE todavia se acepta por compatibilidad, pero esta obsoleto y no conviene ensenarlo.
  - De ahi salen sus dos caras: si el trigger falla, la sentencia original tambien falla y se deshace, que es exactamente lo que se quiere para un invariante como que el stock nunca quede negativo; y si el trigger es lento, la sentencia original se vuelve lenta, y si bloquea, bloquea al usuario que hizo el UPDATE.
  - Conviene mencionar tambien las variables especiales que PL/pgSQL pone a disposicion dentro de una funcion de trigger, porque permiten escribir una sola funcion para varios eventos: TG_OP dice si fue INSERT, UPDATE o DELETE, TG_TABLE_NAME dice sobre que tabla, y TG_WHEN y TG_LEVEL dicen si es BEFORE o AFTER y de fila o de sentencia.
  - Hoy no hacen falta, pero saber que existen evita que el estudiante escriba tres funciones casi identicas.
  - CÓDIGO CITADO (referencia):
  - CREATE OR REPLACE FUNCTION fn_trg_audit_cita()
  - CREATE TRIGGER trg_audit_cita AFTER UPDATE OF estado ON cita FOR EACH ROW EXECUTE FUNCTION fn_trg_audit_cita()
  - Fuera de la lamina (habla de la practica): No existe la forma de Oracle con el cuerpo dentro del CREATE TRIGGER, y hay que decirlo tal cual porque es el error que la rubrica penaliza expresamente.

**[Slide 8] Un trigger son DOS objetos: la funcion y la asociacion** — 18 vinetas.

**[Slide 9] BEFORE o AFTER, y que significa el valor que se retorna** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - En un trigger BEFORE de fila, la fila aun no esta escrita y lo que la funcion retorna es lo que se va a guardar: si retorna NEW, se guarda tal cual
  - Si retorna una version modificada de NEW, por ejemplo tras hacer NEW.estado:= UPPER(NEW.estado), se guarda la version modificada; y si retorna NULL, la operacion se cancela en silencio, sin error y sin mensaje.
  - En un trigger AFTER de fila la fila ya esta escrita y el valor de retorno se ignora; se escribe RETURN NEW por convencion.
  - Sin esa clausula el trigger es de sentencia, corre una sola vez y no tiene OLD ni NEW.
  - El numero hace palpable la diferencia: un UPDATE que toca quinientas citas ejecuta un trigger de fila quinientas veces y uno de sentencia una sola vez.
  - Es la clase de matiz que separa saber la regla de entenderla.
  - NOTAS:
  - BEFORE y AFTER no son estilos alternativos, tienen capacidades distintas, y en PostgreSQL la diferencia se expresa a traves del valor de retorno de la funcion, que es la parte que el estudiante no adivina.
  - Ese ultimo caso hay que nombrarlo como trampa: cancelar retornando NULL parece elegante y deja a la aplicacion creyendo que guardo, asi que para RECHAZAR se usa RAISE EXCEPTION y no un RETURN NULL.
  - Para un trigger de DELETE se retorna OLD, porque NEW no existe en ese evento; simetricamente, en un INSERT no existe OLD.
  - FOR EACH ROW indica que se ejecuta una vez por fila afectada y da acceso a OLD y NEW.
  - La regla operativa.
  - Poner AFTER en el trigger de stock es el error mas comun del dia, y conviene explicar por que es un error y no solo un descuento: un AFTER que lanza excepcion tambien deshace la transaccion, asi que el dato malo no queda, pero el motor ya hizo el trabajo de escribirlo y, sobre todo, con AFTER no se puede corregir el valor, solo abortar.
  - Fuera de la lamina (habla de la practica): La regla operativa, que es la que se califica en la pregunta 4, se dice en una frase: el que VALIDA va BEFORE, porque tiene que abortar antes de que el dato quede escrito y porque solo ahi puede corregirlo; el que AUDITA va AFTER, porque registra un hecho ya consumado.

**[Slide 10] BEFORE o AFTER: uno puede impedir, el otro solo registrar** — 16 vinetas.

**[Slide 11] La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La auditoria es el uso donde los triggers brillan, porque es el unico mecanismo que no se puede evitar olvidandose de llamarlo.
  - Y WHEN (OLD.estado IS DISTINCT FROM NEW.estado) es la pieza que decide el resultado de la prueba: hace que tres UPDATE dejen DOS filas de auditoria y no tres, porque el tercero asigna a la cita el estado que ya tenia.
  - IS DISTINCT FROM trata el nulo como un valor mas y devuelve verdadero o falso siempre.
  - Sobre el diseno de la tabla de auditoria hay un criterio exigible: una fila debe responder quien, cuando, que, y de que a que.
  - Registrar solo que la cita cambio no sirve para investigar nada.
  - Las columnas de audit_cita son id_cita, accion con el texto 'CAMBIO_ESTADO', valor_anterior y valor_nuevo tomados de OLD.estado y NEW.estado, y dos que se llenan solas con DEFAULT: usuario_bd con current_user y fecha_evento con now().
  - Ninguna de las dos columnas se pasa desde el trigger: se dejan al DEFAULT, porque un dato de auditoria que el codigo puede escribir es un dato que el codigo puede falsear.
  - Por ultimo, el identificador va SERIAL y no calculado con el maximo mas uno: dos sesiones simultaneas leen el mismo maximo y una pierde, y el porque completo se estudia en la Clase 10.
  - NOTAS:
  - Vale leer la cabecera del trigger del proyecto palabra por palabra, porque cada pieza tiene razon.
  - AFTER UPDATE OF estado ON cita limita el disparo a los cambios de esa columna y no a cualquier actualizacion de la fila, de modo que corregir el telefono no escribe una fila de auditoria.
  - FOR EACH ROW da acceso a OLD y NEW.
  - Sin WHEN, la auditoria se llena de eventos donde no cambio nada y deja de servir para investigar.
  - Hay que explicar tambien por que se escribe IS DISTINCT FROM y no el operador de desigualdad: si uno de los dos lados es nulo, la desigualdad devuelve nulo, y un WHEN que evalua a nulo NO dispara; una cita que pasa de estado nulo a 'PROGRAMADA' se quedaria sin auditar.
  - Conviene detenerse en esos dos defaults porque tienen matices. current_user devuelve el rol EFECTIVO, es decir el que la Clase 2 cambiaba con SET ROLE, y no necesariamente quien inicio la sesion, que es session_user; para auditar interesa el efectivo.
  - Y now() devuelve el instante de inicio de la transaccion, no el del reloj, asi que si una transaccion escribe cinco filas de auditoria las cinco llevan la misma marca de tiempo; si eso importa, existe clock_timestamp().
  - Como referencia de dimensionamiento, si la clinica registra doscientos cambios auditables por dia, la tabla crece del orden de setenta y tres mil filas en doce meses, cifra que obliga a definir retencion en el mismo plan de respaldo.

**[Slide 12] El trigger que impide: el hueco que el CHECK no tapa** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La segunda mitad del tema es el trigger que rechaza, y la demostracion se monta sobre un hueco real.
  - El esquema de la Clase 1 trae CHECK (stock >= 0) sobre insumo, asi que la primera reaccion sensata del grupo es que el trigger no hace falta.
  - La demo retira la restriccion a proposito con ALTER TABLE insumo DROP CONSTRAINT, ejecuta UPDATE insumo SET stock = stock - 10 WHERE id_insumo = 2 sobre un insumo que tiene tres unidades, y muestra el stock en menos siete.
  - Ese numero es el argumento entero de la clase: sin defensa, la base guarda un imposible fisico.
  - Un CHECK es mas barato, no se puede olvidar, lo aplica el motor sin una linea de codigo y se documenta solo al leer el DDL: si la regla cabe en un CHECK, no se hace trigger.
  - Un CHECK solo puede fallar; no puede explicar.
  - La prueba tambien tiene dos mitades y las dos importan: el descuento invalido rechazado, y el descuento legitimo que sigue funcionando.
  - No se bloqueo la operacion, se bloqueo el resultado invalido, y sin la segunda mitad nadie puede saber que el trigger no rompio nada mas.
  - NOTAS:
  - Hay que ser preciso al comparar los dos mecanismos, porque decir que el trigger es mejor seria falso.
  - Lo que un CHECK no puede hacer es mirar OTRA fila, OTRA tabla, o el valor ANTERIOR de la fila que se esta cambiando; solo ve los valores finales de la fila que se inserta o actualiza.
  - Por eso el trigger de stock de la clase no es un reemplazo del CHECK sino una demostracion de la capacidad extra: la funcion fn_trg_stock_no_negativo() puede escribir RAISE EXCEPTION 'ERROR: el stock de % no puede quedar negativo (resultado: %)', OLD.nombre, NEW.stock, es decir puede nombrar el insumo tomando el dato de OLD y el resultado de NEW en el mismo mensaje.
  - La asociacion va BEFORE
  - CÓDIGO CITADO (referencia):
  - UPDATE OF stock ON insumo FOR EACH ROW
  - Fuera de la lamina (habla de la practica): La asociacion va BEFORE UPDATE OF stock ON insumo FOR EACH ROW, y el mensaje es parte del entregable, igual que en la Clase 3: es lo que la aplicacion va a mostrar y lo que la prueba va a verificar.

**[Slide 13] Las cuatro capas, y en cual vive cada regla** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Primero lo declarativo de una fila: NOT NULL, CHECK y DEFAULT resuelven todo lo que se puede decidir mirando los valores finales de una sola fila —stock no negativo
  - Precio positivo, estado dentro de una lista—, y son lo mas barato y lo mas dificil de saltarse.
  - Segundo lo declarativo entre filas y entre tablas: UNIQUE y las claves foraneas.
  - Tercero el trigger, cuando la regla necesita comparar OLD con NEW, mirar otra tabla o escribir en una segunda tabla; la auditoria entra aqui por definicion, porque escribir en audit_cita no cabe en ninguna restriccion.
  - Cuarto la aplicacion, y solo para lo que la base no puede saber: el formato del correo, el permiso de la pantalla, el idioma del mensaje.
  - La primera idea de todo el mundo para impedir la doble reserva es un trigger que haga SELECT COUNT(*) FROM cita WHERE id_veterinario = NEW.id_veterinario AND fecha_hora = NEW.fecha_hora.
  - En Oracle ese trigger simplemente no funciona, porque un trigger de fila no puede consultar la tabla en mutacion.
  - En PostgreSQL SI corre, y ahi esta el peligro: parece funcionar en la demo y no protege de nada cuando hay concurrencia, porque cada transaccion ve su propia foto de la tabla y ninguna ve la cita que la otra acaba de insertar sin confirmar.
  - Decir esto hoy es lo que evita que en la Clase 10 el estudiante defienda un trigger que ya escribio.
  - NOTAS:
  - Conviene dictar las cuatro capas en orden de preferencia, porque el orden es la respuesta.
  - Aqui hay un ejemplo que hay que dar porque es el que el estudiante resuelve mal: la regla de que un veterinario no puede tener dos citas en la misma franja es UNIQUE (id_veterinario, fecha_hora) y no un trigger.
  - El criterio para decidir si algo pertenece a la aplicacion se dice en una frase y conviene escribirla en el tablero: una validacion que solo vive en la app se salta conectandose por otra via, como hizo la Clase 2 con SET ROLE.
  - Merece un parrafo la trampa que el estudiante intentara, porque la respuesta correcta es contraintuitiva y depende del motor.
  - Las dos pasan la verificacion y las dos insertan.
  - La respuesta correcta es declarativa ——, es mas rapida, mas clara y a prueba de concurrencia, y el porque completo llega en la Clase 10.
  - CÓDIGO CITADO (referencia):
  - ALTER TABLE cita ADD CONSTRAINT uq_vet_franja UNIQUE (id_veterinario, fecha_hora)
  - Fuera de la lamina (habla de la practica): La pregunta 4 vale quince puntos, no pide codigo y es la que mejor mide si el estudiante entendio el dia: hay que ubicar cada validacion en su capa y justificar por que ahi.

**[Slide 14] Las cuatro capas, y en cual vive cada regla** — 11 vinetas.

**[Slide 15] Cuando NO se usa un trigger, y lo que un trigger no ve** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - De lo anterior se deduce cuando no usar un trigger, y esta es probablemente la parte mas util de la clase.
  - No se usa cuando una restriccion declarativa resuelve el problema.
  - No se usa cuando la regla pertenece al flujo de la aplicacion y debe admitir excepciones, como un descuento autorizado por el administrador: un trigger no distingue casos autorizados y termina obligando a trucos para desactivarlo.
  - No se usa cuando el efecto es pesado o depende de algo externo, como enviar un correo o llamar un servicio
  - Porque eso corre dentro de la transaccion, alarga los bloqueos y convierte una demora ajena en demora de la base de datos, tema que se retoma en las Clases 8 y 10.
  - Y no se usa cuando la logica tiene varios pasos y decisiones, porque para eso existe el procedimiento de la Clase 3, que se invoca a proposito y se puede probar solo.
  - El primero es la invisibilidad: quien lee la aplicacion ve un UPDATE cita SET estado = 'CANCELADA' y no ve que ademas se escribio en audit_cita; el comportamiento del sistema deja de estar en el codigo que se lee.
  - Y no hay ninguna senal en el SQL, asi que la unica defensa es documentarlo.
  - El segundo es el encadenamiento: si el trigger de cita inserta en audit_cita y audit_cita tiene su propio trigger, se forma una cadena, y si alguno acaba modificando la tabla que lo activo hay recursion
  - La convencion que conviene fijar para la clínica, como criterio y no como norma del motor, es a lo sumo uno o dos triggers por tabla y solo para dos usos: auditoria de cambios sensibles e invariantes que no se puedan declarar.
  - Dos triggers, no cinco, y esa cifra es deliberada.
  - NOTAS:
  - Hay tres riesgos que conviene exponer con ejemplos y no como advertencia generica.
  - PostgreSQL no la prohibe, la corta cuando se agota la pila, y eso ocurre en produccion y con datos reales, no durante la prueba.
  - El tercero es un limite que hay que nombrar porque es exactamente lo que la seccion 6 del plan de respaldo pide: hay operaciones que un trigger de fila no ve.
  - TRUNCATE no dispara triggers de fila, asi que un TRUNCATE insumo pasa por encima de la validacion de stock sin que se escriba una sola linea de auditoria.
  - Fuera de la lamina (habla de la practica): Y no hay ninguna senal en el SQL, asi que la unica defensa es documentarlo, que es parte del entregable.

**[Slide 16] Seguridad y respaldo: dos preguntas complementarias** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Seguridad y respaldo van en la misma sesion porque responden a preguntas complementarias: la seguridad intenta que nada malo pase, el respaldo asume que igual pasara.
  - Hay que separar dos familias de copia que se confunden todo el tiempo.
  - Un respaldo logico exporta objetos y datos, como sentencias o en un formato propio del motor; en PostgreSQL la herramienta es pg_dump
  - Y el comando concreto que el plan tiene que nombrar es pg_dump -Fc -d clinica -f clinica_AAAAMMDD.dump, donde -Fc pide el formato comprimido propio, que es el que permite restaurar selectivamente con pg_restore.
  - Es portable entre versiones y maquinas, permite restaurar una sola tabla y se puede inspeccionar; en cambio es lento de restaurar en volumenes grandes y no captura un instante exacto de la base entera.
  - Aqui hay un hueco que casi nadie ve: pg_dump respalda UNA base de datos y NO respalda los roles, porque los roles son objetos del cluster y no de la base.
  - Los cuatro roles de la Clase 2 se van con pg_dumpall --globals-only.
  - Si ese comando falta en el plan, se restaura la base y ningun rol tiene permisos: el sistema esta ahi y nadie puede entrar.
  - Vale decirlo asi, porque es el tipo de detalle por el que un plan de respaldo real falla.
  - Un respaldo fisico copia los archivos del motor y los registros de transaccion, con pg_basebackup
  - Y es lo que se usa en produccion porque permite recuperar a un punto exacto en el tiempo aplicando el registro de escritura anticipada, el WAL; exige acceso al sistema de archivos y, en general, la misma version y plataforma.
  - Con esa base se ordenan las estrategias con numeros: un dump diario deja una perdida potencial de veinticuatro horas, y agregar archivado de WAL la baja al orden de minutos; son ejemplos, no valores obligatorios.
  - En la clínica las dos se cruzan en un punto: un rol con DELETE de mas puede borrar la agenda, y solo un respaldo probado la recupera.
  - Sin privilegio minimo el respaldo se usa mas; sin respaldo, un error de privilegios es irreversible.
  - NOTAS:
  - La consecuencia para este curso hay que decirla sin rodeos y esta en la seccion siguiente: nada de esto se puede EJECUTAR.

**[Slide 17] RPO y RTO: dos siglas que solo sirven con un numero acordado** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El RPO es cuanta informacion se acepta perder, medida en tiempo.
  - Si la clínica atiende del orden de cuarenta citas por dia en un horario de lunes a sabado de 7:00 a 19:00, perder cuatro horas de datos son entre quince y veinte citas con sus consultas clinicas y sus facturas
  - Y quien decide si eso es tolerable es el dueno de la clinica, no el administrador de la base; esa asignacion de responsabilidad es regla, no matiz.
  - El RTO es cuanto tiempo puede estar caida la base antes de restaurar: si el sistema se cae un sabado a las diez de la manana con la sala llena, un RTO de ocho horas equivale a cerrar el dia y devolver pacientes.
  - Y la ventana del respaldo se justifica con el mismo horario: un dump a las 20:30 se defiende porque la facturacion cierra a las 20:00, mientras que «diario» a secas no se defiende.
  - Uno, restaurar en un entorno distinto del original, nunca encima del que funciona, porque una prueba que destruye el dato bueno es un incidente y no una prueba.
  - Dos, cronometrar desde que se decide restaurar hasta que una consulta de la aplicacion devuelve datos correctos, porque ese intervalo, y no el tiempo de copiar un archivo, es el RTO medido.
  - Tres, verificar con comprobaciones de negocio, y esto es lo que convierte «restaure» en «restaure bien»: los conteos de cita, consulta y factura, y el maximo de fecha_hora en cita, comparados contra los valores del origen al momento del corte.
  - Y hay una sexta seccion que casi siempre se omite: que NO cubre el plan, y cual es el riesgo residual que se asume.
  - Un dump diario no protege del borrado por error que se descubre tres dias despues si la retencion es de dos copias; un respaldo logico no protege de la corrupcion del propio archivo si nunca se restaura.
  - Nombrar el limite es lo que separa un plan de una lista de comandos, y es lo que un evaluador pregunta primero.
  - NOTAS:
  - RPO y RTO dejan de ser siglas cuando se les pone un numero acordado con el negocio.
  - Probar un restore de verdad tiene cuatro pasos y conviene dictarlos como procedimiento.
  - Cuatro, dejar bitacora con fecha, responsable, resultado y RTO medido; si no hay bitacora, la prueba no existe.
  - Fuera de la lamina (habla de la practica): RPO y RTO dejan de ser siglas cuando se les pone un numero acordado con el negocio, y la rubrica pide precisamente el numero con su justificacion.

**[Slide 18] Lo que ExamLab si puede demostrar, y lo que se documenta en papel** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El motor de la clase es PostgreSQL, que corre dentro del navegador, y ahi funciona todo el codigo del dia: CREATE FUNCTION con IMMUTABLE
  - Las dos partes del trigger, RAISE EXCEPTION y RAISE NOTICE, los bloques DO de la Clase 3, current_user, now() e IS DISTINCT FROM.
  - La evidencia de las cuatro primeras preguntas es la salida del motor.
  - El numero que salga, por ejemplo tres minutos, es un RTO honesto y medido, y la consulta de validacion posterior es exactamente la que el plan tiene que traer escrita.
  - Oracle sigue en el kit solo como contraste: alla las herramientas se llaman Data Pump y RMAN, y el trigger se escribe con el cuerpo adentro y con:NEW y:OLD.
  - NOTAS:
  - Hay que ser preciso aqui porque es la parte de la clase que se puede entregar mal por una expectativa equivocada.
  - Lo que NO se puede ejecutar es pg_dump, pg_dumpall, pg_basebackup ni pg_restore, y la razon hay que decirla con precision en vez de dejarla en «la herramienta no sirve»: son programas de linea de comandos que leen y escriben archivos, y ahi no hay sistema de archivos ni servidor al que conectarse.
  - Esa distincion hay que decirla en clase, porque un estudiante que intente ejecutar pg_dump va a perder veinte minutos y va a creer que hizo algo mal.
  - Lo que si se puede ensayar de verdad, y conviene hacerlo, es el restore a escala de aula: borrar el esquema completo y volverlo a levantar pegando el propio guion del estudiante, con cronometro en mano.
  - Vale un minuto senalarlo para quien se encuentre Oracle en el trabajo, y no vale mas, porque la calificacion ocurre en PostgreSQL.
  - Fuera de la lamina (habla de la practica): Por eso la pregunta 5 es un documento y no una ejecucion: se califica que el plan nombre la herramienta correcta para cada cosa, no que el estudiante la haya corrido.

**[Slide 19] Como amarra con las clases vecinas y con la rubrica del PI** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La Clase 1 dejo el esquema, el CHECK de stock que hoy se retira a proposito para mostrar el hueco, y la restriccion de unicidad que hoy se defiende como la respuesta correcta a la doble reserva.
  - La Clase 2 dejo los roles, y hoy reaparecen en dos puntos: current_user es lo que la columna de auditoria guarda, y pg_dumpall --globals-only es lo que los respalda.
  - La Clase 3 dejo el procedimiento y la bateria de bloques DO, que es la tecnica con la que hoy se prueban los dos triggers.
  - Hacia adelante, el Parcial 1 de la Clase 5 evalua justamente procedimientos, seguridad y este contenido; la Clase 8 retoma la transaccion
  - Que es el marco dentro del cual corre todo trigger; la Clase 10 explica por que el trigger de conteo no protege de la doble reserva; y la Clase 12 conecta la aplicacion, que es cuando la invisibilidad del trigger deja de ser un concepto.
  - En el proyecto esto es la seccion de seguridad y respaldo: roles, matriz, auditoria y plan de restauracion se presentan como una sola pieza.
  - Y en la Clase 12 la cuenta de servicio de la aplicacion es un rol mas de esta matriz, con EXECUTE sobre los procedimientos y sin acceso directo a las tablas.
  - NOTAS:
  - Lo de hoy cierra el Corte 1 y conviene decir como.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - «Cree el trigger y no pasa nada»: la causa mas frecuente es que la funcion existe pero la asociacion no, porque el estudiante escribio solo el CREATE FUNCTION; la segunda es que la asociacion dice UPDATE OF otra columna, o que el WHEN nunca se cumple.
  - «Puede una funcion modificar datos»: en PostgreSQL si puede, y es una diferencia importante con Oracle, que lo prohibe cuando la funcion se invoca desde una consulta.
  - Que pueda no significa que deba: el planificador decide cuantas veces evalua una funcion, de modo que un INSERT escondido en ella podria ejecutarse una vez, ninguna o diez mil, y ademas obliga a declararla VOLATILE.
  - Si hace falta modificar datos, es un procedimiento; si debe ocurrir automaticamente, es un trigger.
  - «Puedo poner toda la validacion en triggers y no escribir procedimientos»: se puede
  - Y el sistema se vuelve imposible de razonar; el orden de preferencia que conviene memorizar es declarativo primero, procedimiento despues, trigger al final y solo para lo que los dos anteriores no pueden.
  - «Si ya tengo el trigger de auditoria, para que quiero respaldo»: porque cumplen funciones distintas; la auditoria cuenta que paso y quien lo hizo, el respaldo devuelve los datos
  - Y si el incidente afecta el esquema completo, audit_cita se pierde junto con todo lo demas y no reconstruye ni una cita.
  - «Por que la auditoria registro dos filas y no tres»: por la clausula WHEN, porque el tercer UPDATE asigno el estado que la cita ya tenia; si registra tres, falta el WHEN.
  - «Por que el trigger de stock deja pasar un TRUNCATE»: porque TRUNCATE no dispara triggers de fila, y eso va escrito en la seccion de lo que el plan no cubre.
  - Fuera de la lamina (habla de la practica): En la rubrica del proyecto, seguridad y respaldo valen 15 de los 100 puntos del proyecto.


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
7. El trigger: el unico que nadie invoca, y en PostgreSQL son DOS objetos
8. Un trigger son DOS objetos: la funcion y la asociacion
9. BEFORE o AFTER, y que significa el valor que se retorna
10. BEFORE o AFTER: uno puede impedir, el otro solo registrar
11. La auditoria: donde el trigger brilla, y el WHEN que cambia el resultado
12. El trigger que impide: el hueco que el CHECK no tapa
13. Las cuatro capas, y en cual vive cada regla
14. Las cuatro capas, y en cual vive cada regla
15. Cuando NO se usa un trigger, y lo que un trigger no ve
16. Seguridad y respaldo: dos preguntas complementarias
17. RPO y RTO: dos siglas que solo sirven con un numero acordado
18. Lo que PostgreSQL en el navegador si puede demostrar, y lo que se documenta en papel
19. Como amarra con las clases vecinas
20. Un trigger son DOS objetos: la funcion y la asociacion
21. La funcion de tarifas: RETURNS NUMERIC, CASE, COALESCE e IMMUTABLE
22. Donde vive cada validacion: CHECK, trigger o aplicacion
23. Plan de respaldo: 6 secciones y herramientas reales de PostgreSQL
24. Demo del dia
25. Cierre · Clase 4

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

### 35-55 · Demo paso a paso · [Slide 24]
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

### 115-120 · Cierre · [Slide 25]
**Decir:** «Queda visto: Funciones · Triggers · Seguridad y respaldo. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 25] slide de cierre. Dudas finales.


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
