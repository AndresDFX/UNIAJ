# Guion docente · Clase 4 · Funciones · Triggers · Seguridad y respaldo

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** >=1 funcion + >=1 trigger + borrador plan de respaldo
- **Entregable de hoy:** Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)
- **Herramienta:** Oracle Live SQL + Google Docs
- **Slides:** Clases/Clase 4 - Funciones disparadores seguridad respaldo/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Funcion (Clase 3 vio procedimiento): retorna un valor y se usa DENTRO de una expresion SQL, ej. SELECT fn_precio_base(especie) FROM mascota. Debe ser determinista y sin efectos secundarios pesados; si necesita modificar datos y ejecutarse como accion independiente, es un procedimiento, no una funcion.
- Trigger (disparador): bloque de codigo que el motor ejecuta AUTOMATICAMENTE cuando ocurre un evento (BEFORE/AFTER INSERT, UPDATE o DELETE) sobre una tabla, sin que nadie lo llame explicitamente. Dos usos tipicos aqui: auditoria (guardar quien/cuando cancelo una cita) y validacion de invariantes (que el stock nunca quede negativo tras un UPDATE).
- Riesgo real de los triggers: son invisibles en el codigo de la app (un desarrollador que solo mira el INSERT no ve que ademas se dispara una auditoria), y pueden encadenarse (un trigger que dispara otro trigger) generando efectos dificiles de rastrear. Se usan para pocas reglas criticas, no para toda la logica de negocio.
- Seguridad y respaldo van juntos: seguridad evita que datos se corrompan o se filtren; respaldo (backup) asume que igual algo saldra mal y prepara la recuperacion. Full backup (copia completa), incremental (solo lo que cambio desde el ultimo backup) y diferencial (todo lo que cambio desde el ultimo FULL) son las tres estrategias base.
- RPO (Recovery Point Objective) = cuantos datos se puede permitir perder, medido en tiempo ('maximo 1 hora de citas perdidas'). RTO (Recovery Time Objective) = cuanto tiempo puede estar caida la BD antes de restaurar. Un backup diario sin probar el restore no cumple ningun RPO/RTO real: un plan de respaldo sin prueba de restauracion es solo una promesa.
- Error de docente que no domina el tema: presentar el backup como 'copiar el archivo de vez en cuando' sin frecuencia, retencion (cuantas copias se guardan) ni prueba de restore — eso es lo que el taller de esta clase pide explicitamente que el equipo defina.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Una funcion y un procedimiento se parecen tanto en la escritura que conviene separarlos por su papel y no por su sintaxis. Un procedimiento se invoca para que haga algo; una funcion se invoca para que devuelva un valor, y ese valor se usa dentro de una expresion SQL, como en SELECT m.nombre, fn_precio_base(m.especie) AS tarifa FROM mascota m WHERE m.activa = 'S'. La palabra determinista, que aparece en todo manual, tiene aqui un significado operativo simple: la funcion es determinista si con la misma entrada devuelve siempre la misma salida, hoy y en tres meses. fn_precio_base cumple, porque solo depende de p_especie. Un contraejemplo util: una funcion fn_edad_mascota que calcule la edad usando SYSDATE por dentro no es determinista, porque manana devuelve otro numero para la misma mascota, y por eso no puede sustentar un indice basado en funcion de los que se veran en la Clase 7; la correccion es de una linea, pasar la fecha de referencia como parametro. Hay un segundo efecto que hay que dimensionar con numeros: una funcion invocada dentro de un SELECT se ejecuta una vez por fila evaluada. Si fn_saldo_factura(p_id_factura) hace un SUM sobre detalle_factura y la consulta recorre diez mil facturas, el motor ejecuta diez mil consultas internas; el resultado es correcto y el tiempo es inaceptable. La alternativa es una consulta con GROUP BY, y esa comparacion es material directo de la Clase 6.

Un disparador se distingue de todo lo anterior en que nadie lo llama: se declara una vez y el motor lo ejecuta cuando ocurre el evento declarado, un INSERT, un UPDATE o un DELETE sobre una tabla. El detalle que cambia todo el analisis, y que rara vez se dice, es que el disparador corre dentro de la misma transaccion de la sentencia que lo activo. De ahi salen sus dos caras: si el disparador falla, la sentencia original tambien falla y se deshace, que es exactamente lo que se quiere para un invariante como que el stock nunca quede negativo; y si el disparador es lento, la sentencia original se vuelve lenta, y si bloquea, bloquea al usuario que hizo el UPDATE. BEFORE y AFTER no son estilos alternativos, tienen capacidades distintas: en un BEFORE la fila aun no esta escrita, asi que se pueden modificar los valores que se van a guardar mediante :NEW, por ejemplo :NEW.estado := UPPER(:NEW.estado), o rechazar la operacion; en un AFTER la fila ya esta escrita y :NEW es de solo lectura, lo que lo hace el lugar correcto para auditar o propagar efectos. FOR EACH ROW indica que se ejecuta una vez por fila afectada y da acceso a :OLD y :NEW; sin esa clausula el disparador es de sentencia y corre una sola vez, sin acceso a los valores de cada fila. El numero hace palpable la diferencia: un UPDATE que toca quinientas citas ejecuta un disparador de fila quinientas veces y uno de sentencia una sola vez.

La auditoria es el uso donde los disparadores brillan, porque es el unico mecanismo que no se puede evitar olvidandose de llamarlo. El del proyecto queda asi: CREATE OR REPLACE TRIGGER trg_audit_cancelacion AFTER UPDATE OF estado ON cita FOR EACH ROW WHEN (NEW.estado = 'CANCELADA' AND OLD.estado <> 'CANCELADA'), y en el cuerpo un INSERT INTO audit_cita. Vale leer esa cabecera palabra por palabra, porque cada pieza tiene razon: AFTER UPDATE OF estado limita el disparo a los cambios de esa columna y no a cualquier actualizacion de la fila, y la clausula WHEN evita registrar una cancelacion que ya estaba cancelada. Sobre el diseno de la tabla de auditoria hay un criterio exigible: una fila debe responder quien, cuando, que y de que a que. Registrar solo que la cita cambio no sirve para investigar nada; hacen falta columnas para el usuario, obtenido con USER o SYS_CONTEXT, la marca de tiempo con SYSTIMESTAMP, y el valor anterior y el nuevo tomados de :OLD.estado y :NEW.estado. Conviene senalar en voz alta una debilidad del guion de demostracion, porque ensena mas que el guion mismo: calcular el identificador con MAX(id_audit) mas uno funciona con un usuario y falla con dos, ya que dos sesiones simultaneas leen el mismo maximo y una pierde; la solucion es una secuencia o una columna de identidad, y el porque completo se estudia en la Clase 10. Como referencia de dimensionamiento, si la clinica registra doscientos cambios auditables por dia, la tabla crece del orden de setenta y tres mil filas en doce meses, cifra que obliga a definir retencion en el mismo entregable.

Los disparadores son peligrosos por tres razones que hay que exponer con ejemplos y no como advertencia generica. La primera es la invisibilidad: quien lee la aplicacion ve un UPDATE cita SET estado = 'CANCELADA' y no ve que ademas se escribio en audit_cita y se recalculo un total; el comportamiento del sistema deja de estar en el codigo que se lee. La segunda es el encadenamiento: si el disparador de cita inserta en audit_cita y audit_cita tiene su propio disparador, se forma una cadena, y si alguno acaba modificando la tabla que lo activo, hay recursion. Los motores la cortan con un error de niveles excedidos, del orden de unas decenas de niveles en Oracle segun version, pero eso ocurre en produccion y con datos reales, no durante la prueba. La tercera es un error especifico que conviene anticipar: un disparador de fila sobre cita no puede consultar la propia tabla cita, porque esta en mutacion, y Oracle lo rechaza con el clasico error de tabla mutante. Tiene consecuencia inmediata, porque la primera idea de todo el mundo para impedir la doble reserva es un disparador que haga SELECT COUNT(*) FROM cita WHERE id_veterinario = :NEW.id_veterinario AND fecha_hora = :NEW.fecha_hora, y ese disparador simplemente no funciona. La respuesta correcta es declarativa, ALTER TABLE cita ADD CONSTRAINT uq_vet_franja UNIQUE (id_veterinario, fecha_hora), y es mas rapida, mas clara y a prueba de concurrencia. Depurar un disparador, por ultimo, es mas incomodo que depurar el procedimiento de la Clase 3: no hay depurador, la salida por pantalla depende del cliente, y una tabla de bitacora pierde sus filas si la transaccion se deshace, salvo transaccion autonoma.

De lo anterior se deduce cuando no usar un disparador, y esta es probablemente la parte mas util de la clase. No se usa cuando una restriccion declarativa resuelve el problema, porque NOT NULL, CHECK, UNIQUE y las claves foraneas de la Clase 1 son mas rapidas, imposibles de olvidar y no se pueden desactivar sin que se note. No se usa cuando la regla pertenece al flujo de la aplicacion y debe admitir excepciones, como un descuento autorizado por el administrador: un disparador no distingue casos autorizados y termina obligando a trucos para desactivarlo. No se usa cuando el efecto es pesado o depende de algo externo, como enviar un correo o llamar un servicio, porque eso corre dentro de la transaccion, alarga los bloqueos y convierte una demora ajena en demora de la base de datos, tema que se retoma en las Clases 8 y 10. Y no se usa cuando la logica tiene varios pasos y decisiones, porque para eso existe el procedimiento de la Clase 3, que se invoca a proposito y se puede probar solo. La convencion que conviene fijar para VetCare, como criterio y no como norma del motor, es a lo sumo uno o dos disparadores por tabla y solo para dos usos: auditoria de cambios sensibles e invariantes que no se puedan declarar. El entregable pide un disparador, no cinco, y esa cifra es deliberada.

Seguridad y respaldo van en la misma sesion porque responden a preguntas complementarias: la seguridad intenta que nada malo pase, el respaldo asume que igual pasara. Hay que separar dos familias de copia que se confunden todo el tiempo. Un respaldo logico exporta objetos y datos como sentencias o en un formato propio del motor, con pg_dump en PostgreSQL o Data Pump en Oracle, y en su version mas modesta es el propio archivo con CREATE TABLE mas los INSERT. Es portable entre versiones y maquinas, permite restaurar una sola tabla y se lee con un editor de texto; en cambio es lento de restaurar en volumenes grandes y no captura un instante exacto de la base entera. Un respaldo fisico copia los archivos del motor, los datafiles y los registros de transacciones, con RMAN o pg_basebackup, y es lo que se usa en produccion porque permite recuperar a un punto en el tiempo aplicando los registros; exige acceso al sistema de archivos y, en general, la misma version y plataforma. La consecuencia para este curso hay que decirla sin rodeos: en un playground gratuito no existe respaldo fisico, porque no hay instancia ni sistema de archivos al que llegar. Por eso el respaldo real del proyecto es logico, el archivo sql versionado mas una exportacion de datos, y todo lo fisico se documenta en papel como el plan que se aplicaria en la clinica real. Con esa base se ordenan las tres estrategias con numeros: un completo semanal mas incrementales diarios deja una perdida potencial de veinticuatro horas, y agregar archivado de registros cada quince minutos la baja a quince minutos; son ejemplos de convencion, no valores obligatorios.

RPO y RTO dejan de ser siglas cuando se les pone un numero acordado con el negocio. El RPO es cuanta informacion se acepta perder, medida en tiempo. Si Huellitas atiende del orden de cuarenta citas por dia, perder cuatro horas de datos son entre quince y veinte citas con sus consultas clinicas y sus facturas, y quien decide si eso es tolerable es el dueno de la clinica, no el administrador de la base; esa asignacion de responsabilidad es regla, no matiz. El RTO es cuanto tiempo puede estar caida la base antes de restaurar: si el sistema se cae un sabado a las diez de la manana con la sala llena, un RTO de ocho horas equivale a cerrar el dia y devolver pacientes. Probar un restore de verdad tiene cuatro pasos y conviene dictarlos como procedimiento. Uno, restaurar en un entorno distinto del original, nunca encima del que funciona, porque una prueba que destruye el dato bueno es un incidente y no una prueba. Dos, cronometrar desde que se decide restaurar hasta que una consulta de la aplicacion devuelve datos correctos, porque ese intervalo, y no el tiempo de copiar un archivo, es el RTO medido. Tres, verificar con comprobaciones de negocio: SELECT COUNT(*) FROM cita, SELECT COUNT(*) FROM consulta y SELECT SUM(total) FROM factura, comparados contra los valores del origen al momento del corte. Cuatro, dejar bitacora con fecha, responsable, resultado y RTO medido; si no hay bitacora, la prueba no existe. Y esta prueba si se puede hacer de verdad en el playground, borrando el esquema completo y volviendolo a levantar pegando el guion del equipo, con cronometro en mano; el numero que salga, por ejemplo tres minutos, es un RTO honesto a escala de aula y es lo que la rubrica espera ver escrito.

Tres preguntas se repiten en esta clase y conviene responderlas sin evasivas. Primera: si ya tengo el disparador de auditoria, para que quiero respaldo. Porque cumplen funciones distintas: la auditoria cuenta que paso y quien lo hizo, el respaldo devuelve los datos; y si el incidente afecta el esquema completo, audit_cita se pierde junto con todo lo demas y no reconstruye ni una cita. Segunda: puedo poner toda la validacion en disparadores y no escribir procedimientos. Se puede, y el sistema se vuelve imposible de razonar, porque cada INSERT tendra efectos que nadie ve al leer el codigo; el orden de preferencia que conviene memorizar es declarativo primero, procedimiento despues, disparador al final y solo para lo que los dos anteriores no pueden. Tercera, mas tecnica y muy reveladora: puede una funcion modificar datos. No debe, y en Oracle directamente no puede cuando se la invoca desde una consulta, que rechaza el intento de hacer una operacion de modificacion dentro de un SELECT. La razon de fondo importa mas que la regla: el optimizador decide cuantas veces evalua una funcion, de modo que un INSERT escondido en ella podria ejecutarse una vez, ninguna o diez mil. Si hace falta modificar datos, es un procedimiento; si debe ocurrir automaticamente, es un disparador.

Error tipico del docente que no domina el tema: crear el disparador de auditoria, ejecutar el UPDATE y no mostrar nunca el contenido de audit_cita. La consecuencia aguas abajo es que el estudiante concluye que el disparador no hizo nada, entrega el guion sin evidencia y no llega a entender la diferencia entre :OLD y :NEW, que es justo lo que pregunta el Parcial 1; ademas, en la Clase 13, cuando se analicen casos reales, no reconocera por que la ausencia de auditoria vuelve imposible investigar un incidente. El segundo tropiezo es dejar RPO y RTO como definiciones de diccionario sin exigir que el equipo escriba dos numeros acordados con el negocio y una prueba de restauracion cronometrada. La consecuencia es un Plan_Backup_VetCare lleno de frases generales que la rubrica penaliza, y un equipo que en la Clase 12 y en la sustentacion final no puede responder cuanto tarda la clinica en volver a operar ni cuanta informacion perderia, que es la primera pregunta de cualquier evaluador y la que separa un plan real de una promesa.


**Demo que usted debe poder repetir:** fn_precio_consulta + trg_audit_cancelacion_cita + outline backup.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: >=1 funcion + >=1 trigger + borrador plan de respaldo.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Funcion (Clase 3 vio procedimiento): retorna un valor y se usa DENTRO de una expresion SQL, ej. SELECT fn_precio_base(especie) FROM mascota. Debe ser determinista y sin efectos secundarios pesados; si necesita modificar datos y ejecutarse como accion independiente, es un procedimiento, no una funcion.
- Trigger (disparador): bloque de codigo que el motor ejecuta AUTOMATICAMENTE cuando ocurre un evento (BEFORE/AFTER INSERT, UPDATE o DELETE) sobre una tabla, sin que nadie lo llame explicitamente. Dos usos tipicos aqui: auditoria (guardar quien/cuando cancelo una cita) y validacion de invariantes (que el stock nunca quede negativo tras un UPDATE).
- Riesgo real de los triggers: son invisibles en el codigo de la app (un desarrollador que solo mira el INSERT no ve que ademas se dispara una auditoria), y pueden encadenarse (un trigger que dispara otro trigger) generando efectos dificiles de rastrear. Se usan para pocas reglas criticas, no para toda la logica de negocio.
- Seguridad y respaldo van juntos: seguridad evita que datos se corrompan o se filtren; respaldo (backup) asume que igual algo saldra mal y prepara la recuperacion. Full backup (copia completa), incremental (solo lo que cambio desde el ultimo backup) y diferencial (todo lo que cambio desde el ultimo FULL) son las tres estrategias base.
- RPO (Recovery Point Objective) = cuantos datos se puede permitir perder, medido en tiempo ('maximo 1 hora de citas perdidas'). RTO (Recovery Time Objective) = cuanto tiempo puede estar caida la BD antes de restaurar. Un backup diario sin probar el restore no cumple ningun RPO/RTO real: un plan de respaldo sin prueba de restauracion es solo una promesa.
- Error de docente que no domina el tema: presentar el backup como 'copiar el archivo de vez en cuando' sin frecuencia, retencion (cuantas copias se guardan) ni prueba de restore — eso es lo que el taller de esta clase pide explicitamente que el equipo defina.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: fn_precio_consulta + trg_audit_cancelacion_cita + outline backup.
Herramienta: Oracle Live SQL + Google Docs
📸 Pantallazo: [CAP: demo VetCare Clase 4]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Crear >=1 funcion util al PI.
2. Crear >=1 trigger (auditoria o stock no negativo).
3. Redactar plan de respaldo: frecuencia, retencion, restore de prueba.
4. Actualizar checklist PI: seguridad/respaldo en progreso.
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Scripts funcion/trigger + Plan_Backup_VetCare (1 pag.)
📸 Pantallazo: [CAP: avance equipo / playground Clase 4]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 4 - VetCare.docx`. Clave para usted: `Quiz Clase 4 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: >=1 funcion + >=1 trigger + borrador plan de respaldo. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 04_func_trigger_backup.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
