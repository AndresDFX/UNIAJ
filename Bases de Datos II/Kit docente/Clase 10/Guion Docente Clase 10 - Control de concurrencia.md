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


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] La transaccion como unidad de todo o nada** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Una transaccion es un grupo de sentencias SQL que el motor trata como una sola unidad de todo o nada: o se aplican todas o no se aplica ninguna.
  - El motor no las ejecuta una despues de la otra: intercala sus operaciones para aprovechar disco y CPU, y ese intercalado es la fuente de todos los problemas de esta clase.
  - El resultado son dos mascotas citadas al mismo minuto con el mismo veterinario, y ninguna de las dos sentencias fallo ni produjo un error.
  - La base de datos no se corrompio ni tiene un defecto: cumplio dos ordenes contradictorias porque nadie le dijo que no debia.
  - Todo lo que sigue son las cuatro formas de decirselo.
  - Ejemplo la clínica: agendar la cita y descontar la vacuna son dos sentencias de un mismo hecho; si la segunda falla, la primera tampoco debe quedar.
  - NOTAS:
  - Se abre de forma explicita o implicita y se cierra con COMMIT, que hace permanentes los cambios, o con ROLLBACK, que los deshace.
  - Concurrencia significa que dos o mas transacciones estan abiertas al mismo tiempo sobre los mismos datos.
  - El escenario canonico de la clínica conviene tenerlo escrito en el tablero desde el minuto uno: dos recepcionistas, en dos computadores distintos, abren la agenda del veterinario Ruiz para el martes a las 10:00.
  - Ambas consultan si la franja esta libre.
  - Ambas reciben cero filas.
  - Ambas insertan una cita.

**[Slide 5] Serializar de verdad existe, y cuesta** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Si la clínica tiene ocho recepcionistas y cada agendamiento debe esperar a que termine el anterior, el sistema pasa de atender ocho operaciones simultaneas a una, y el tiempo que el usuario percibe frente a la pantalla se multiplica.
  - Aislamiento, en este contexto, es la propiedad que responde a una pregunta muy concreta: que puede ver mi transaccion de lo que estan haciendo las otras mientras esas otras todavia no terminan.
  - Es la I de ACID (atomicidad, consistencia, aislamiento y durabilidad) y es la unica de las cuatro propiedades que el desarrollador configura deliberadamente; las otras tres el motor las garantiza siempre.
  - Esto amarra directo con la Clase 8, donde se vieron transacciones, COMMIT y ROLLBACK: sin esa base, hablar de aislamiento no tiene donde apoyarse.
  - En PostgreSQL se pide con cuando el motor detecta que dos transacciones no pueden ordenarse, aborta una con un error de serializacion y la aplicacion debe reintentarla.
  - NOTAS:
  - La solucion obvia, que consiste en ejecutar las transacciones estrictamente una tras otra, existe y se llama serializacion, pero tiene un costo que hay que nombrar para que las demas opciones tengan sentido.
  - Por eso el estandar SQL no impone una sola forma de trabajar: ofrece una perilla llamada nivel de aislamiento, que permite negociar cuanta anomalia se tolera a cambio de cuanto rendimiento.
  - CÓDIGO CITADO (referencia):
  - SET TRANSACTION ISOLATION LEVEL SERIALIZABLE

**[Slide 6] Los tres fenomenos indeseables, en escenas de la clinica** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Lectura sucia, o dirty read: la transaccion T1 inserta la cita de las 10:00 y todavia no hace COMMIT
  - T2 consulta la agenda, ve esa cita y le dice al dueno que la franja esta ocupada; despues T1 hace ROLLBACK porque el pago no paso, y esa cita nunca existio.
  - T2 tomo una decision con un dato que jamas fue real.
  - Lectura no repetible, o non-repeatable read: dentro de una misma transaccion de facturacion, el procedimiento lee el stock del insumo 40 y obtiene 5 unidades
  - Hace unos calculos, vuelve a leer el mismo stock y ahora obtiene 2, porque otra transaccion vendio 3 unidades y confirmo en el intervalo.
  - Lectura fantasma, o phantom read: T1 cuenta las citas del veterinario Ruiz para el martes y obtiene 4, decide que puede agendar una quinta, y al volver a contar hay 5 porque T2 inserto una fila nueva que cumple el mismo criterio de busqueda.
  - NOTAS:
  - El estandar define tres fenomenos indeseables, y cada uno se entiende mejor con una escena de la clinica.
  - La misma consulta, en la misma transaccion, devolvio dos valores distintos.
  - La diferencia entre las dos ultimas es fina y conviene decirla de forma explicita, porque es la pregunta de examen mas fallada: en la lectura no repetible cambio una fila que ya existia; en la fantasma aparecio o desaparecio una fila del conjunto que cumple la condicion del WHERE.

**[Slide 7] Doble reserva sin control de concurrencia** — 6 vinetas.

**[Slide 8] Los cuatro niveles de aislamiento se definen por lo que permiten** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Los cuatro niveles de aislamiento del estandar SQL se definen exactamente por cuales de esos tres fenomenos permiten, y esa es la unica forma sensata de memorizarlos.
  - READ UNCOMMITTED permite los tres: puede leer datos no confirmados.
  - Es el mas rapido, practicamente no se usa en sistemas transaccionales, y Oracle ni siquiera lo implementa.
  - Es el nivel por omision de PostgreSQL, Oracle y SQL Server, y por lo tanto es el nivel en el que corre la enorme mayoria de los sistemas del mundo, incluido cualquier la clínica que el estudiante construya sin tocar nada.
  - REPEATABLE READ impide tambien la lectura no repetible: una fila leida dentro de la transaccion se ve igual hasta el final.
  - Segun el estandar todavia permite fantasmas, pero en la practica el motor InnoDB de MySQL, donde REPEATABLE READ es el nivel por omision, los bloquea usando gap locks; esa es una desviacion util del estandar y conviene aclararla
  - Porque si un estudiante prueba en DB Fiddle con MySQL no va a reproducir el fantasma y va a creer que el material esta mal.
  - La sentencia para cambiarlo es SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
  - Y la regla practica que el estudiante debe recordar es que subir de nivel nunca es gratis: se paga en esperas mas largas o en transacciones abortadas que la aplicacion tiene que reintentar.
  - NOTAS:
  - READ COMMITTED impide la lectura sucia, porque solo se ve lo que ya fue confirmado, pero permite lectura no repetible y fantasma.
  - SERIALIZABLE impide los tres y equivale logicamente a ejecutar las transacciones una tras otra.

**[Slide 9] Niveles de aislamiento: que anomalia tapa cada uno** — 13 vinetas.

**[Slide 10] Control pesimista: SELECT... FOR UPDATE** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La herramienta concreta es SELECT...
  - FOR UPDATE: al leer la fila con SELECT stock FROM insumo WHERE id_insumo = 40 FOR UPDATE, el motor coloca un bloqueo exclusivo sobre esa fila
  - Y cualquier otra transaccion que intente leerla con la misma clausula queda esperando hasta el COMMIT o el ROLLBACK de la primera.
  - Aplicado a la clínica resuelve limpiamente el doble descuento de stock: la segunda transaccion espera, y cuando por fin entra ya lee 2 y no 5, de modo que su validacion de stock suficiente funciona sobre el dato verdadero.
  - Su costo es la espera, y la espera mal manejada produce un sistema que para el usuario parece caido.
  - La regla de diseno asociada, y la mas importante de toda la clase, es mantener las transacciones cortas: entre el bloqueo y el COMMIT no debe haber una llamada a un servicio externo ni una pantalla esperando que el usuario confirme
  - Porque mientras el usuario piensa o se va a almorzar la fila sigue bloqueada y nadie mas puede facturar ese insumo.
  - NOTAS:
  - El control pesimista asume que el conflicto va a ocurrir, asi que bloquea el recurso antes de tocarlo.
  - Por eso existen variantes que el docente debe conocer: FOR UPDATE NOWAIT falla de inmediato en vez de esperar, y FOR UPDATE WAIT 5 espera cinco segundos y luego falla, lo cual permite devolver un mensaje honesto al usuario en vez de una pantalla congelada.

**[Slide 11] El bloqueo explicito y la actualizacion condicional** — 10 vinetas.

**[Slide 12] Control optimista: verificar unicamente al escribir** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El control optimista asume lo contrario: que los conflictos son raros, asi que no bloquea nada al leer y verifica unicamente al escribir.
  - Se implementa con una columna adicional, tipicamente llamada version, de tipo entero, o con un timestamp de ultima modificacion.
  - El flujo en la clínica es este: la transaccion lee la cita 812 y obtiene version 7; el usuario edita la hora; al guardar se ejecuta
  - Si otra transaccion ya paso por ahi, la version almacenada es 8 y la sentencia afecta cero filas.
  - El numero de filas afectadas es la senal de conflicto, y con esa senal la aplicacion decide si reintenta o le avisa al usuario que el dato cambio mientras editaba.
  - El criterio para elegir entre los dos enfoques es la frecuencia real del conflicto, no el gusto: si dos personas pelean por la misma fila muchas veces al dia, el optimista reintenta sin parar y conviene el pesimista
  - Si el choque es excepcional, el optimista da mejor rendimiento porque nadie espera nunca.
  - En la clínica, el stock de los insumos mas vendidos es un caso pesimista y la edicion de los datos de contacto de un dueno es un caso claramente optimista.
  - CÓDIGO CITADO (referencia):
  - UPDATE cita SET fecha_hora = ..., version = 8 WHERE id_cita = 812 AND version = 7

**[Slide 13] Deadlock: la escena de VetCare y como se evita** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La escena de la clínica es concreta: el procedimiento de facturacion bloquea primero la fila de Factura y luego la de Insumo, mientras el procedimiento de devolucion bloquea primero Insumo y luego Factura.
  - Los motores no dejan eso colgado: mantienen internamente un grafo de esperas y, al detectar un ciclo, eligen una victima y la abortan con un error explicito.
  - En Oracle es ORA-00060, en MySQL el error 1213, en PostgreSQL el codigo 40P01.
  - La consecuencia practica para el estudiante es que la aplicacion debe estar preparada para recibir ese error y reintentar la operacion, porque no es un defecto del sistema sino el mecanismo funcionando como debe.
  - Y la prevencion es sorprendentemente simple y barata: acceder siempre a las tablas en el mismo orden en todos los procedimientos.
  - Si todo el codigo de la clínica toca Factura antes que Insumo, el ciclo no puede formarse nunca.
  - Ese acuerdo de orden canonico se escribe una vez en el documento de diseno, se respeta, y elimina la clase entera de problemas sin costo de rendimiento.
  - PostgreSQL detecta el ciclo, aborta una de las dos transacciones con deadlock detected y deja seguir a la otra; la abortada debe reintentarse completa.
  - NOTAS:
  - Un deadlock, o interbloqueo, ocurre cuando dos transacciones se esperan mutuamente y ninguna puede avanzar.
  - Si los dos arrancan al mismo tiempo, cada uno tiene exactamente lo que el otro necesita, nadie cede y ninguna espera termina sola.
  - La transaccion sobreviviente termina normal.

**[Slide 14] Antes de los niveles: la restriccion que cuesta una linea** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Antes de complicarse con niveles de aislamiento hay una solucion declarativa que resuelve el caso estrella de la clínica y cuesta una sola linea:.
  - Esto conduce a la limitacion practica del dia y a la pregunta previsible: «como demuestro dos transacciones simultaneas si PostgreSQL en el navegador es una sola sesion?».
  - El informe de hoy se audita en el checkpoint de la Clase 11 y se convierte en clausula del contrato de operaciones de la Clase 12, donde cada procedimiento declara que errores puede lanzar, incluido el de horario ya tomado.
  - NOTAS:
  - Con esa restriccion, cuando las dos recepcionistas insertan, el motor deja pasar la primera y rechaza la segunda con una violacion de unicidad, sin que nadie haya razonado sobre aislamiento; el procedimiento captura esa excepcion y devuelve «ese horario acaba de ser tomado, elija otro».
  - La leccion general que el docente debe transmitir es que una regla que se puede expresar como restriccion declarativa, es decir UNIQUE, CHECK, FOREIGN KEY o NOT NULL, es mas confiable que la misma regla escrita en codigo, porque el motor la aplica siempre: venga la escritura de la aplicacion, de un script de carga masiva o de alguien conectado con un cliente SQL a corregir un dato a mano.
  - La respuesta honesta es que no se puede: los playgrounds gratuitos ejecutan un script en una unica sesion, normalmente con autocommit activo, y no permiten abrir dos conexiones para intercalarlas.
  - Lo que si se demuestra con evidencia ejecutable son tres cosas: la restriccion UNIQUE rechazando el segundo INSERT, el patron optimista completo con la columna version y el UPDATE que afecta cero filas, y la sintaxis de SELECT FOR UPDATE ejecutandose sin error.
  - Lo que no se demuestra se documenta en una tabla de linea de tiempo con columnas T1, T2 y estado de la fila, paso por paso; esa tabla es un artefacto profesional legitimo, no un premio de consolacion, y es exactamente como se comunican estos escenarios en un documento de diseno real.
  - CÓDIGO CITADO (referencia):
  - ALTER TABLE cita ADD CONSTRAINT uq_agenda UNIQUE (id_veterinario, fecha_hora)

**[Slide 15] La doble reserva, y la restriccion que la cierra de raiz** — 10 vinetas.

**[Slide 16] La restriccion que hace imposible la doble reserva** — 10 vinetas.


**Demo que usted debe poder repetir:** Narrativa paso a paso T1/T2 sobre tabla Cita.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 10 - Control de concurrencia/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 10 · Control de concurrencia · la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. La transaccion como unidad de todo o nada
5. Serializar de verdad existe, y cuesta
6. Los tres fenomenos indeseables, en escenas de la clinica
7. Doble reserva sin control de concurrencia
8. Los cuatro niveles de aislamiento se definen por lo que permiten
9. Niveles de aislamiento: que anomalia tapa cada uno
10. Control pesimista: SELECT... FOR UPDATE
11. El bloqueo explicito y la actualizacion condicional
12. Control optimista: verificar unicamente al escribir
13. Deadlock: la escena de la clínica y como se evita
14. Antes de los niveles: la restriccion que cuesta una linea
15. La doble reserva, y la restriccion que la cierra de raiz
16. La restriccion que hace imposible la doble reserva
17. Demo del dia
18. Cierre · Clase 10

> Privado, no se proyecta: `Kit docente/Clase 10/Solucion Taller Clase 10 - VetCare.docx`

## Plan minuto a minuto (120 min equivalentes — trabajo autonomo)

> El estudiante trabaja sin encuentro sincrono. Usted publica este guion resumido + taller en ExamLab.

### Bloque A (0-20) · Encuadre PI
**Decir/publicar:** «Hoy avanzamos el PI en: Escenarios de concurrencia del PI documentados. No es un taller suelto.»
Referencia slides: Encuadre + Mapa del bloque.

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
Carpeta Codigo/ — archivo 10_concurrencia_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 10/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
