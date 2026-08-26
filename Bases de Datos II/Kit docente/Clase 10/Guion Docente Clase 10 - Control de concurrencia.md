# Guion docente · Clase 10 · Control de concurrencia · VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** AUTONOMA (festivo, sin encuentro sincrono)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Escenarios de concurrencia del PI documentados
- **Entregable de hoy:** Informe corto: 2 escenarios (cita doble / stock) + mitigacion
- **Herramienta:** Google Docs + Live SQL
- **Slides:** Clases/Clase 10 - Control de concurrencia/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Concurrencia = varias transacciones ejecutandose al mismo tiempo sobre los mismos datos. El problema clasico de VetCare: dos recepcionistas, en dos computadores distintos, intentan agendar la MISMA franja horaria para el MISMO veterinario en el mismo instante; sin control, ambas lecturas ven la franja libre y ambas insertan — doble reserva.
- Control pesimista: asumir que el conflicto va a ocurrir, asi que se bloquea la fila (o el recurso) apenas se empieza a leer para modificar, y otras transacciones deben esperar a que termine (SELECT ... FOR UPDATE es el ejemplo tipico). Simple y seguro, pero puede generar esperas largas si hay muchas transacciones compitiendo.
- Control optimista: asumir que el conflicto es raro, dejar que todos lean libremente, y verificar SOLO al momento de escribir si alguien mas cambio el dato mientras tanto (comparando una version o timestamp); si hubo cambio, se rechaza y se reintenta. Mejor rendimiento cuando los conflictos son poco frecuentes.
- Deadlock (mencion breve): dos transacciones se bloquean mutuamente esperando un recurso que la otra tiene — T1 espera la fila que T2 bloqueo, y T2 espera la fila que T1 bloqueo. El motor detecta esto y aborta una de las dos automaticamente.
- Mitigaciones concretas y accesibles para el PI: una restriccion UNIQUE sobre (id_veterinario, fecha_hora) hace que el segundo INSERT falle automaticamente en vez de crear la doble reserva; transacciones cortas reducen la ventana de tiempo en la que puede ocurrir un conflicto; centralizar la logica en un procedimiento (Clase 3) evita que cada pantalla de la app implemente su propia validacion de forma inconsistente.
- Error de docente que no domina el tema: creer que 'poner una transaccion' ya resuelve la concurrencia — una transaccion garantiza atomicidad, pero sin un mecanismo de bloqueo o una restriccion UNIQUE, dos transacciones concurrentes pueden seguir generando la doble reserva porque ambas leen 'libre' antes de que la otra confirme.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Una transaccion es un grupo de sentencias SQL que el motor trata como una sola unidad de todo o nada: o se aplican todas o no se aplica ninguna. Se abre de forma explicita o implicita y se cierra con COMMIT, que hace permanentes los cambios, o con ROLLBACK, que los deshace. Concurrencia significa que dos o mas transacciones estan abiertas al mismo tiempo sobre los mismos datos. El motor no las ejecuta una despues de la otra: intercala sus operaciones para aprovechar disco y CPU, y ese intercalado es la fuente de todos los problemas de esta clase. El escenario canonico de VetCare conviene tenerlo escrito en el tablero desde el minuto uno: dos recepcionistas, en dos computadores distintos, abren la agenda del veterinario Ruiz para el martes a las 10:00. Ambas consultan si la franja esta libre. Ambas reciben cero filas. Ambas insertan una cita. El resultado son dos mascotas citadas al mismo minuto con el mismo veterinario, y ninguna de las dos sentencias fallo ni produjo un error. La base de datos no se corrompio ni tiene un defecto: cumplio dos ordenes contradictorias porque nadie le dijo que no debia. Todo lo que sigue son las cuatro formas de decirselo.

La solucion obvia, que consiste en ejecutar las transacciones estrictamente una tras otra, existe y se llama serializacion, pero tiene un costo que hay que nombrar para que las demas opciones tengan sentido. Si VetCare tiene ocho recepcionistas y cada agendamiento debe esperar a que termine el anterior, el sistema pasa de atender ocho operaciones simultaneas a una, y el tiempo que el usuario percibe frente a la pantalla se multiplica. Por eso el estandar SQL no impone una sola forma de trabajar: ofrece una perilla llamada nivel de aislamiento, que permite negociar cuanta anomalia se tolera a cambio de cuanto rendimiento. Aislamiento, en este contexto, es la propiedad que responde a una pregunta muy concreta: que puede ver mi transaccion de lo que estan haciendo las otras mientras esas otras todavia no terminan. Es la I de ACID (atomicidad, consistencia, aislamiento y durabilidad) y es la unica de las cuatro propiedades que el desarrollador configura deliberadamente; las otras tres el motor las garantiza siempre. Esto amarra directo con la Clase 8, donde se vieron transacciones, COMMIT y ROLLBACK: sin esa base, hablar de aislamiento no tiene donde apoyarse.

El estandar define tres fenomenos indeseables, y cada uno se entiende mejor con una escena de la clinica. Lectura sucia, o dirty read: la transaccion T1 inserta la cita de las 10:00 y todavia no hace COMMIT; T2 consulta la agenda, ve esa cita y le dice al dueno que la franja esta ocupada; despues T1 hace ROLLBACK porque el pago no paso, y esa cita nunca existio. T2 tomo una decision con un dato que jamas fue real. Lectura no repetible, o non-repeatable read: dentro de una misma transaccion de facturacion, el procedimiento lee el stock del insumo 40 y obtiene 5 unidades, hace unos calculos, vuelve a leer el mismo stock y ahora obtiene 2, porque otra transaccion vendio 3 unidades y confirmo en el intervalo. La misma consulta, en la misma transaccion, devolvio dos valores distintos. Lectura fantasma, o phantom read: T1 cuenta las citas del veterinario Ruiz para el martes y obtiene 4, decide que puede agendar una quinta, y al volver a contar hay 5 porque T2 inserto una fila nueva que cumple el mismo criterio de busqueda. La diferencia entre las dos ultimas es fina y conviene decirla de forma explicita, porque es la pregunta de examen mas fallada: en la lectura no repetible cambio una fila que ya existia; en la fantasma aparecio o desaparecio una fila del conjunto que cumple la condicion del WHERE.

Los cuatro niveles de aislamiento del estandar SQL se definen exactamente por cuales de esos tres fenomenos permiten, y esa es la unica forma sensata de memorizarlos. READ UNCOMMITTED permite los tres: puede leer datos no confirmados. Es el mas rapido, practicamente no se usa en sistemas transaccionales, y Oracle ni siquiera lo implementa. READ COMMITTED impide la lectura sucia, porque solo se ve lo que ya fue confirmado, pero permite lectura no repetible y fantasma. Es el nivel por omision de PostgreSQL, Oracle y SQL Server, y por lo tanto es el nivel en el que corre la enorme mayoria de los sistemas del mundo, incluido cualquier VetCare que el estudiante construya sin tocar nada. REPEATABLE READ impide tambien la lectura no repetible: una fila leida dentro de la transaccion se ve igual hasta el final. Segun el estandar todavia permite fantasmas, pero en la practica el motor InnoDB de MySQL, donde REPEATABLE READ es el nivel por omision, los bloquea usando gap locks; esa es una desviacion util del estandar y conviene aclararla, porque si un estudiante prueba en DB Fiddle con MySQL no va a reproducir el fantasma y va a creer que el material esta mal. SERIALIZABLE impide los tres y equivale logicamente a ejecutar las transacciones una tras otra. La sentencia para cambiarlo es SET TRANSACTION ISOLATION LEVEL SERIALIZABLE, y la regla practica que el estudiante debe recordar es que subir de nivel nunca es gratis: se paga en esperas mas largas o en transacciones abortadas que la aplicacion tiene que reintentar.

El control pesimista asume que el conflicto va a ocurrir, asi que bloquea el recurso antes de tocarlo. La herramienta concreta es SELECT ... FOR UPDATE: al leer la fila con SELECT stock FROM insumo WHERE id_insumo = 40 FOR UPDATE, el motor coloca un bloqueo exclusivo sobre esa fila, y cualquier otra transaccion que intente leerla con la misma clausula queda esperando hasta el COMMIT o el ROLLBACK de la primera. Aplicado a VetCare resuelve limpiamente el doble descuento de stock: la segunda transaccion espera, y cuando por fin entra ya lee 2 y no 5, de modo que su validacion de stock suficiente funciona sobre el dato verdadero. Su costo es la espera, y la espera mal manejada produce un sistema que para el usuario parece caido. Por eso existen variantes que el docente debe conocer: FOR UPDATE NOWAIT falla de inmediato en vez de esperar, y FOR UPDATE WAIT 5 espera cinco segundos y luego falla, lo cual permite devolver un mensaje honesto al usuario en vez de una pantalla congelada. La regla de diseno asociada, y la mas importante de toda la clase, es mantener las transacciones cortas: entre el bloqueo y el COMMIT no debe haber una llamada a un servicio externo ni una pantalla esperando que el usuario confirme, porque mientras el usuario piensa o se va a almorzar la fila sigue bloqueada y nadie mas puede facturar ese insumo.

El control optimista asume lo contrario: que los conflictos son raros, asi que no bloquea nada al leer y verifica unicamente al escribir. Se implementa con una columna adicional, tipicamente llamada version, de tipo entero, o con un timestamp de ultima modificacion. El flujo en VetCare es este: la transaccion lee la cita 812 y obtiene version 7; el usuario edita la hora; al guardar se ejecuta UPDATE cita SET fecha_hora = ..., version = 8 WHERE id_cita = 812 AND version = 7. Si otra transaccion ya paso por ahi, la version almacenada es 8 y la sentencia afecta cero filas. El numero de filas afectadas es la senal de conflicto, y con esa senal la aplicacion decide si reintenta o le avisa al usuario que el dato cambio mientras editaba. El criterio para elegir entre los dos enfoques es la frecuencia real del conflicto, no el gusto: si dos personas pelean por la misma fila muchas veces al dia, el optimista reintenta sin parar y conviene el pesimista; si el choque es excepcional, el optimista da mejor rendimiento porque nadie espera nunca. En VetCare, el stock de los insumos mas vendidos es un caso pesimista y la edicion de los datos de contacto de un dueno es un caso claramente optimista.

Un deadlock, o interbloqueo, ocurre cuando dos transacciones se esperan mutuamente y ninguna puede avanzar. La escena de VetCare es concreta: el procedimiento de facturacion bloquea primero la fila de Factura y luego la de Insumo, mientras el procedimiento de devolucion bloquea primero Insumo y luego Factura. Si los dos arrancan al mismo tiempo, cada uno tiene exactamente lo que el otro necesita, nadie cede y ninguna espera termina sola. Los motores no dejan eso colgado: mantienen internamente un grafo de esperas y, al detectar un ciclo, eligen una victima y la abortan con un error explicito. En Oracle es ORA-00060, en MySQL el error 1213, en PostgreSQL el codigo 40P01. La transaccion sobreviviente termina normal. La consecuencia practica para el estudiante es que la aplicacion debe estar preparada para recibir ese error y reintentar la operacion, porque no es un defecto del sistema sino el mecanismo funcionando como debe. Y la prevencion es sorprendentemente simple y barata: acceder siempre a las tablas en el mismo orden en todos los procedimientos. Si todo el codigo de VetCare toca Factura antes que Insumo, el ciclo no puede formarse nunca. Ese acuerdo de orden canonico se escribe una vez en el documento de diseno, se respeta, y elimina la clase entera de problemas sin costo de rendimiento.

Antes de complicarse con niveles de aislamiento hay una solucion declarativa que resuelve el caso estrella de VetCare y cuesta una sola linea: ALTER TABLE cita ADD CONSTRAINT uq_agenda UNIQUE (id_veterinario, fecha_hora). Con esa restriccion, cuando las dos recepcionistas insertan, el motor deja pasar la primera y rechaza la segunda con una violacion de unicidad, sin que nadie haya razonado sobre aislamiento; el procedimiento captura esa excepcion y devuelve «ese horario acaba de ser tomado, elija otro». La leccion general que el docente debe transmitir es que una regla que se puede expresar como restriccion declarativa, es decir UNIQUE, CHECK, FOREIGN KEY o NOT NULL, es mas confiable que la misma regla escrita en codigo, porque el motor la aplica siempre: venga la escritura de la aplicacion, de un script de carga masiva o de alguien conectado con un cliente SQL a corregir un dato a mano. Esto conduce a la limitacion practica del dia y a la pregunta previsible: «como demuestro dos transacciones simultaneas si DB Fiddle es una sola sesion?». La respuesta honesta es que no se puede: los playgrounds gratuitos ejecutan un script en una unica sesion, normalmente con autocommit activo, y no permiten abrir dos conexiones para intercalarlas. Lo que si se demuestra con evidencia ejecutable son tres cosas: la restriccion UNIQUE rechazando el segundo INSERT, el patron optimista completo con la columna version y el UPDATE que afecta cero filas, y la sintaxis de SELECT FOR UPDATE ejecutandose sin error. Lo que no se demuestra se documenta en una tabla de linea de tiempo con columnas T1, T2 y estado de la fila, paso por paso; esa tabla es un artefacto profesional legitimo, no un premio de consolacion, y es exactamente como se comunican estos escenarios en un documento de diseno real. El informe de hoy se audita en el checkpoint de la Clase 11 y se convierte en clausula del contrato de operaciones de la Clase 12, donde cada procedimiento declara que errores puede lanzar, incluido el de horario ya tomado.

Error tipico del docente que no domina el tema: el primero es afirmar que envolver las sentencias en una transaccion ya resuelve la concurrencia. No la resuelve. La transaccion garantiza atomicidad, es decir que las tres sentencias de la facturacion se apliquen juntas o ninguna, pero dos transacciones concurrentes en READ COMMITTED pueden seguir leyendo ambas «franja libre» y produciendo la doble reserva, porque ninguna ve lo que la otra todavia no confirmo. La consecuencia aguas abajo es un estudiante que en la Clase 12 escribe un procedimiento con COMMIT al final y jura que el problema esta cubierto, y que en la sustentacion de la Clase 15 no puede responder que pasa si las dos recepcionistas presionan Guardar en el mismo segundo. El segundo error es subir todo a SERIALIZABLE como respuesta universal sin nombrar el costo; la consecuencia es que el estudiante aprende que el aislamiento es gratis y no aprende a reconocer el sintoma opuesto, es decir esperas largas, timeouts y deadlocks mas frecuentes, que es justamente lo que se va a encontrar en un sistema real y lo que nadie le va a explicar en el momento. Un tercer tropiezo: presentar el deadlock como una falla catastrofica que hay que evitar a toda costa, cuando el comportamiento correcto es esperarlo, capturar el error del motor y reintentar la operacion.


**Demo que usted debe poder repetir:** Narrativa paso a paso T1/T2 sobre tabla Cita.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 10 - Control de concurrencia/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 10 · Control de concurrencia · VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Doble reserva sin control de concurrencia
6. La restriccion que hace imposible la doble reserva
7. Demo del dia
8. Herramientas de hoy
9. Actividad autonoma — contexto / por que importa
10. Actividad autonoma — objetivo y criterios
11. Actividad autonoma — escenario / datos de partida
12. Actividad autonoma — pasos guiados
13. Actividad autonoma — pistas (checklist vacio)
14. Criterios de exito / entregable
15. Para el PI esta semana
16. Cierre · Clase 10

> Privado, no se proyecta: `Kit docente/Clase 10/Solucion Taller Clase 10 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Escenarios de concurrencia del PI documentados. No es un taller suelto.»
Referencia slides: Agenda + Objetivo PI.

### Bloque B (20-45) · Teoria minima
Leer Teoria Core. Tomar notas en el informe del PI.

### Bloque C (45-100) · Practica = entregable PI
Seguir el taller estudiante. Herramienta: Google Docs + Live SQL.
Salida esperada de la practica (publiquela junto al enunciado para que el
estudiante autonomo sepa si le quedo bien):
📸 Evidencia del problema: dos citas en la misma franja (sin restriccion) [[captura: salida-doble-reserva.png]]
📸 El MISMO INSERT ya con UNIQUE: la BD lo rechaza sola [[captura: salida-unique-rechaza.png]]

### Bloque D (100-120) · Empaquetado y cierre
Subir entregable a ExamLab. Actualizar el checklist PI del proyecto.


## Codigo / scripts
Carpeta Codigo/ — archivo 10_concurrencia_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 10/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
