# Solucion del taller · Clase 13 · Analisis de un caso real aplicado a VetCare (clase autonoma)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** El analisis del caso GitLab 2017 con las seis secciones y la causa raiz separada de la aparente; la demostracion cuantificada de la inyeccion —la funcion vulnerable devuelve **las 8 mascotas** y, con una variante `UNION`, **los correos de los 6 duenos**— y su cierre con `EXECUTE ... USING`, incluida la trampa de ambiguedad que hace fallar la variante estatica; el control de borrados completo: respaldo con bitacora calculada, trigger `BEFORE DELETE` que archiva `OLD`, el `DELETE` sin `WHERE` que deja `cita` en 0 y `cita_borrada` en 10, la restauracion y la consulta de veredicto que devuelve `RESTAURACION OK`; la clave razonada de las cuatro opciones correctas; y el plan de tres mejoras con la unica pendiente que sigue siendo la misma desde la Clase 11: **el restore que nadie ha ensayado**.

> **Clase autonoma: Sesion 11, lunes 2026-11-02, sin docente en vivo.** Eso cambia como se usa este documento. No hay momento para aclarar dudas en el aula, asi que la retroalimentacion tiene que ser **escrita** y llegar rapido: el 2026-11-09 es el Parcial 3 —tampoco hay espacio ahi— y el 2026-11-16 es la sustentacion. En la practica, el ultimo momento util para devolver correcciones es la semana del 2026-11-02, y conviene publicar junto con el taller las tres advertencias de abajo, porque son las que sin docente presente bloquean a un estudiante media tarde. **El motor es PostgreSQL, no Oracle.**

**Advertencia etica, primero que todo y en el enunciado publicado.** La pregunta 2 pide ejecutar cadenas de ataque. Se ejecutan contra la base de practica del propio estudiante en ExamLab, que es suya y es desechable. Probar lo mismo contra un sistema ajeno y sin autorizacion escrita no es un ejercicio: es un delito. El objetivo de la pregunta es **cerrar** el agujero, y la evidencia que se califica es el 0 filas del final.

**Tres trampas tecnicas que hay que anunciar.** (1) La variante estatica que sugiere el enunciado —`buscar_mascota_directa` con `SELECT id_mascota, nombre ... WHERE nombre = p_nombre`— **falla** con «column reference “id_mascota” is ambiguous», porque los nombres del `RETURNS TABLE` son variables de PL/pgSQL y chocan con las columnas; se arregla con alias (`m.id_mascota`, `m.nombre`, …) y es instructivo que la version con `EXECUTE` no tenga ese problema. (2) En la pregunta 3, `RETURN NEW` en un trigger de `DELETE` devuelve `NULL` y **cancela el borrado en silencio**: el estudiante vera 10 filas en las dos tablas y creera que funciono. (3) `DROP FUNCTION buscar_mascota_insegura(TEXT);` es lo ultimo del script: si se ejecuta antes, los pasos 1 a 3 ya no corren.

**Y una incoherencia del banco que conviene resolver antes de publicar.** La pregunta 1 deja elegir entre tres casos, pero las preguntas 2 y 3 implementan mejoras del caso **C** (inyeccion) y del caso **A** (respaldo). Quien elija el **B** —rendimiento— se encuentra en la pregunta 5 con que las dos mejoras «ya implementadas» no derivan de su caso. Lo razonable es sugerir A o C; y si alguien elige B, se acepta que cite como mejora ya implementada el indice de la Clase 6 (`idx_cita_vet_fecha`, con sus dos `EXPLAIN`) y que la tabla mezcle los tres origenes, siempre que cada fila nombre un objeto real. Las preguntas 1 y 5 son sobre el caso y el PI de cada estudiante, asi que lo que sigue es un **modelo de referencia y no una clave**: se desarrolla el caso A y se dan las notas para calificar B y C.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 13 - Analisis de casos reales/Taller PI - Clase 13 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 13/Taller en ExamLab - Clase 13 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Informe de caso -> mejoras concretas al PI
- Entregable: Informe 1-2 pag.: caso + 3 mejoras aplicables a VetCare
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | El caso: que paso, por que y que aprendemos | `abierta` | 25 |
| 2 | Mejora implementada 1: cerrar la inyeccion de SQL en VetCare | `bd_sql` | 25 |
| 3 | Mejora implementada 2: ningun borrado sin traza ni sin vuelta atras | `bd_sql` | 25 |
| 4 | Que control habria evitado el incidente | `cerrada_multi` | 10 |
| 5 | Tres mejoras priorizadas para VetCare | `abierta` | 15 |

---

## Pregunta 1 · El caso: que paso, por que y que aprendemos · 25 pts

### Respuesta esperada

Se desarrolla el **caso A**, porque es el que conecta con el control que se implementa en la pregunta 3 y con el unico item que sigue en `NO` en el checklist de la Clase 11. Las notas para calificar B y C van al final.

### 1. Contexto

GitLab.com, plataforma de alojamiento de codigo fuente y gestion de proyectos de software, con millones de repositorios alojados y equipos de desarrollo de todo el mundo trabajando sobre ella. La base de datos principal es PostgreSQL, con una replica secundaria que deberia servir para conmutar en caso de fallo. Lo que estaba en juego no era solo el codigo —que casi todos los usuarios tienen tambien en sus maquinas— sino **todo lo que vive unicamente en la base de datos**: incidencias, solicitudes de fusion, comentarios, cuentas de usuario y proyectos recien creados. Es decir, la conversacion y el historial de decisiones de miles de equipos.

### 2. Que fallo, en orden

1. Un aumento anormal de carga —trafico de spam que generaba escrituras masivas— saturo la base de datos principal.
2. Por efecto de esa carga, la **replicacion hacia el servidor secundario se quedo atras** y termino rompiendose.
3. Para volver a sincronizar la replica hay que dejar su directorio de datos vacio y copiarlo de nuevo desde el principal. Un ingeniero, ya de noche y varias horas dentro del incidente, ejecuto ese borrado.
4. **Lo ejecuto en la terminal del servidor principal, no en la de la replica.** Se dio cuenta en segundos y lo interrumpio, pero para entonces ya se habia eliminado la mayor parte del directorio de datos de produccion.
5. Empezo la recuperacion, y ahi aparecio el verdadero problema: de los cinco mecanismos de respaldo que la organizacion creia tener, **ninguno estaba en condiciones de usarse**. Los volcados logicos periodicos fallaban en silencio —una diferencia de version entre las herramientas y el servidor los dejaba practicamente vacios— y las alertas de ese fallo no llegaban a ninguna bandeja. Las instantaneas de disco no estaban habilitadas en ese servidor. La replica ya estaba destruida por el paso 3.
6. La unica copia utilizable era una de un entorno de pruebas, tomada unas **seis horas antes**. Se restauro desde ahi, y todo lo ocurrido en esas seis horas se perdio de forma definitiva.

### 3. Causa raiz, separada de la causa aparente

**Causa aparente:** «un ingeniero se equivoco de terminal». Es cierto y es irrelevante para la prevencion, porque un equipo que trabaja a las once de la noche en un incidente **va** a equivocarse de terminal alguna vez; disenar para que eso no ocurra nunca es disenar para un ser humano que no existe.

**Causa raiz: no habia ningun control que detuviera ese error ni que garantizara la vuelta atras.** Y es doble.

- **La raiz proxima:** el mismo comando destructivo se podia ejecutar en produccion sin confirmacion, sin distincion visual del entorno y sin ninguna barrera. El error humano tenia acceso directo al dato.
- **La raiz de fondo, que es la importante:** **ninguno de los cinco respaldos se habia verificado nunca restaurandolo.** Existian como procedimiento y como archivo, no como capacidad comprobada. Y el fallo era silencioso por diseno accidental: el proceso avisaba por correo, y esos correos se rechazaban, asi que la senal de que el respaldo estaba roto se perdia todos los dias sin que nadie la viera. **Un respaldo que falla en silencio es indistinguible de uno que funciona, hasta el dia en que hace falta.**

Dicho de otra manera: el borrado accidental no causo la perdida de datos. El borrado accidental **reveló** que la capacidad de recuperacion no existia. La perdida llevaba meses siendo inevitable.

### 4. Impacto

- **Datos:** aproximadamente seis horas de escrituras perdidas de forma irrecuperable —incidencias, comentarios, solicitudes de fusion, usuarios y proyectos creados en esa ventana—. No se pudo reconstruir: no habia de donde.
- **Tiempo:** del orden de dieciocho horas de servicio interrumpido o degradado, mas dias de trabajo del equipo en la recuperacion y el analisis posterior.
- **Confianza:** es el costo mas caro y el menos medible. Miles de equipos descubrieron el mismo dia que su historial de decisiones dependia de una cadena de respaldos que no funcionaba.
- **Contrapeso honesto:** la organizacion publico el analisis completo del incidente, con los cinco mecanismos y por que fallo cada uno. Esa transparencia es la razon por la que hoy se puede estudiar en un curso, y es en si misma una practica que vale la pena copiar.

### 5. Leccion en una frase accionable

> **Un respaldo que no se ha restaurado no es un respaldo: es un archivo con un nombre tranquilizador. La copia no es el control; el control es la restauracion verificada.**

Y una segunda, que se deriva de la misma raiz: **si el fallo de un control puede pasar inadvertido, el control no existe.** Un respaldo que avisa cuando falla —y que se comprueba que avisa— vale mas que cinco que se ejecutan en silencio.

### 6. Traduccion a VetCare

El proceso vulnerable al **mismo** tipo de fallo es el borrado de `cita`, y el mecanismo es identico, no analogo:

- **Hoy `DELETE FROM cita;` sin `WHERE` se ejecuta y no deja nada.** No hay confirmacion, no hay archivo de lo borrado y no hay copia previa. Diez filas en el taller; en produccion, la agenda completa de la clinica.
- **La bitacora que si existe no cubre este caso.** `audit_cita`, de la Clase 4, se dispara con los `UPDATE` de estado. **Un `DELETE` no deja rastro en ella**, asi que el evento mas destructivo es justamente el unico que no se audita.
- **Y la copia esta en el mismo sitio que el original.** Cualquier `respaldo_cita` o `audit_cita` vive en la misma base de datos: protege contra un error logico y **no** protege contra perder la instancia, el disco o el servidor. Es exactamente el error de razonamiento del caso —confundir «tengo una copia» con «puedo recuperar»—.
- **El equivalente exacto del respaldo que falla en silencio, en mi proyecto,** es el item 12 del checklist de la Clase 11: plan de respaldo escrito, con RPO y RTO estimados, y **restauracion nunca ensayada**. Es el unico item en `NO` y es el unico irreversible.

La pregunta 3 implementa los dos controles que faltaban: el archivo de lo borrado, que convierte el accidente en recuperable, y la consulta de verificacion, que convierte la copia en capacidad comprobada.

---

### Notas para calificar los otros dos casos

**Caso B (rendimiento).** La causa raiz correcta **no** es «la consulta estaba mal escrita»: es que un proceso automatico podia consumir recursos sin limite y sin que nadie lo notara antes de la hora pico —sin limite de tiempo de ejecucion, sin tope de conexiones, sin revision del plan antes de publicar el panel—. El `SELECT *` y el indice ausente son el mecanismo; la raiz es la ausencia de control. La traduccion a VetCare esta hecha desde la Clase 6: la consulta de agenda por veterinario y rango de fechas hacia `Seq Scan` con `Rows Removed by Filter`, y el indice `idx_cita_vet_fecha` lo cerro. Quien elija B puede citar ese trabajo como mejora ya implementada en la pregunta 5.

**Caso C (inyeccion).** La causa raiz es que el texto de la sentencia se construia con datos del usuario, de modo que un dato podia convertirse en codigo; **no** es «no se validaba la entrada». La distincion importa porque lleva a soluciones distintas: validar es una lista de casos que siempre queda incompleta, y ligar parametros elimina el mecanismo. La traduccion a VetCare es `buscar_mascota_insegura`, y la pregunta 2 la ejecuta y la cierra. Se reconoce como sobresaliente notar que era una funcion de **solo lectura**, y que por eso nadie la reviso: no escribia nada, «no podia hacer dano», y entregaba la base completa.

### Como calificar

- **9 pts — las seis secciones presentes,** 1,5 cada una. Se califica la presencia y que cada una responda lo suyo: contexto (que organizacion y que estaba en juego), secuencia **en orden**, causa raiz, impacto, leccion y traduccion. Una seccion que existe pero repite otra —impacto que vuelve a contar los hechos— cuenta como media.
- **6 pts — la causa raiz distinguida explicitamente de la aparente y apuntando a un control ausente.** Es el punto de mas peso y el que decide la calidad del analisis. Requiere las dos mitades escritas: la aparente («alguien se equivoco», «la consulta estaba mal escrita», «no se validaba la entrada») y la raiz formulada como **ausencia de control** («no habia nada que detuviera ese error», «los respaldos nunca se restauraron»). Un texto que se queda en la culpa de una persona vale 2 de 6, aunque este bien escrito: es el analisis que no cambia nada.
- **4 pts — impacto concreto.** Se piden magnitudes en las cuatro dimensiones que nombra el enunciado —datos, dinero o tiempo, y confianza— con cifras u ordenes de magnitud, no adjetivos. «Fue muy grave» vale 0; «unas seis horas de escrituras perdidas sin posibilidad de reconstruirlas» vale completo. Se acepta «aproximadamente» y se agradece: es mas honesto que una cifra falsa.
- **3 pts — la leccion redactada como regla accionable,** en imperativo o como afirmacion verificable. «Hay que cuidar los respaldos» no es accionable; «un respaldo que no se ha restaurado no es un respaldo» si, porque se puede comprobar si se cumple o no.
- **3 pts — la traduccion a VetCare nombrando tablas, funciones o triggers reales y explicando el mecanismo.** 1,5 pts nombrar el objeto y 1,5 pts explicar **como** se reproduce el mismo fallo ahi. «VetCare tambien podria tener problemas de respaldo» vale 0. «`DELETE FROM cita;` se ejecuta hoy sin nada que lo detenga, y `audit_cita` solo registra `UPDATE`, asi que el evento mas destructivo es el unico sin auditoria» vale completo.
- **Si el caso es propio, la fuente es obligatoria** —enlace o publicacion— y su ausencia cuesta 3 pts: sin fuente no es un caso real, es un relato. Se reconoce como sobresaliente citar el analisis publico del incidente en lugar de una nota de prensa que lo resume.
- **Se reconoce como sobresaliente, sin puntos extra:** senalar que el fallo era **silencioso** —la alerta de que el respaldo no servia no llegaba a nadie— y sacar de ahi la segunda regla; o notar que la copia logica vive en la misma base que el original y por tanto no protege contra perder la instancia.

### Errores frecuentes y que hacer

- **Confundir la causa raiz con la culpa.** «El error fue del ingeniero que se equivoco de servidor» es la version que no sirve para nada, porque la conclusion practica seria «tener mas cuidado», y eso no es un control. La pregunta util es la contraria: ¿que tendria que haber existido para que ese error, que iba a ocurrir tarde o temprano, no terminara en perdida de datos?
- **Un resumen en vez de un analisis.** Media pagina contando los hechos, sin separar causa aparente de raiz y sin traduccion al proyecto. Es lo que sale cuando se copia el enunciado con otras palabras. La forma de detectarlo: si el texto no contiene ninguna afirmacion que no estuviera ya en el enunciado, no hay analisis.
- **Impacto con adjetivos:** «enorme», «gravisimo», «se perdio mucha informacion». No informa y no se puede comparar con nada. Cualquier magnitud aproximada —horas de datos, horas de servicio, numero de usuarios afectados— vale mas que tres superlativos.
- **Una leccion que no es accionable:** «hay que ser cuidadoso con la base de datos», «la seguridad es importante». No se puede comprobar si se cumple. Una regla accionable siempre se puede convertir en una pregunta de si o no: ¿se restauro el ultimo respaldo? ¿se comparo el conteo?
- **Una traduccion a VetCare por analogia y no por mecanismo:** «a VetCare tambien le podria pasar algo parecido». Hay que nombrar el objeto —`cita`, `audit_cita`, `buscar_mascota_insegura`, `api_facturar`— y describir la sentencia o el camino concreto por el que el fallo se reproduce.
- **Elegir el caso B y despues no poder conectarlo con las preguntas 2 y 3,** que implementan mejoras de C y de A. No es culpa del estudiante —el enunciado lo permite—, pero deja la pregunta 5 sin sustento. La salida correcta es citar el trabajo de indices de la Clase 6 como la mejora ya implementada del caso B.
- **Inventar cifras precisas.** «Se perdieron 4.312 registros y 2,3 millones de dolares» sin fuente resta credibilidad a todo el analisis. Si no se sabe, se escribe el orden de magnitud y se dice que es aproximado.

---

## Pregunta 2 · Mejora implementada 1: cerrar la inyeccion de SQL en VetCare · 25 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- ADVERTENCIA, y no es formalismo
-- Las cadenas de ataque de abajo se ejecutan contra TU base de practica en
-- ExamLab: es tuya, es desechable y se vuelve a sembrar en cada pregunta.
-- Probar esto mismo contra un sistema que no es propio y sin autorizacion
-- escrita no es un ejercicio, es un delito. Lo que se aprende aqui es a
-- CERRAR el agujero, y la evidencia que se entrega es el 0 filas del final.
-- ======================================================================

-- ----------------------------------------------------------------------
-- 1. Uso normal: la funcion vulnerable parece impecable
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura('Firulais');
-- 1 fila. Y ahi esta el problema de fondo de todo incidente de inyeccion:
-- en la prueba que hizo quien la escribio, funciono.

-- ----------------------------------------------------------------------
-- 2. El ataque: el usuario reescribe el WHERE
--
-- La cadena que se envia es    Firulais' OR '1'='1
-- y en SQL se escribe duplicando cada comilla simple. La funcion la
-- concatena y el texto que termina ejecutando el motor es:
--
--   SELECT id_mascota, nombre, especie, activa
--     FROM mascota WHERE nombre = 'Firulais' OR '1'='1'
--
-- El dato dejo de ser un dato y se convirtio en codigo. Nadie violo una
-- contrasena ni un permiso: la funcion hizo exactamente lo que le
-- pidieron.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura('Firulais'' OR ''1''=''1');
-- 8 filas: la tabla completa, incluidas Rocky y Kiara, que el buscador
-- del negocio nunca deberia mostrar.

-- ----------------------------------------------------------------------
-- 3. Cuantificar la fuga: la evidencia del incidente
--
-- Este par de consultas es lo que se pega en el informe. Una captura de
-- "salieron muchas filas" no prueba nada; dos numeros iguales, si.
-- ----------------------------------------------------------------------
SELECT COUNT(*) AS filas_devueltas_por_el_ataque
  FROM buscar_mascota_insegura('x'' OR ''1''=''1');
-- 8. Notese que ahora el nombre buscado es 'x', que NO existe: el
-- resultado no depende del dato, depende del OR que el atacante inyecto.

SELECT COUNT(*) AS filas_totales_en_la_tabla FROM mascota;
-- 8. Coinciden. Un buscador de una mascota entrego la tabla entera.

-- ----------------------------------------------------------------------
-- 3b. EXTRA: lo que de verdad se roba (opcional, y es el que convence)
--
-- El OR '1'='1' entrega una tabla. Un UNION entrega OTRA tabla, una que
-- la funcion no menciona en ninguna parte. La cadena enviada es:
--
--   x' UNION SELECT id_dueno, nombre, email, 'S'::CHAR(1) FROM dueno --
--
-- El -- del final comenta la comilla suelta que quedaba. Resultado: los
-- correos de los seis duenos, viajando por un buscador de mascotas. Esto
-- es la fuga de datos personales del caso C, reproducida en dos lineas.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_insegura(
  'x'' UNION SELECT id_dueno, nombre, email, ''S''::CHAR(1) FROM dueno --');
-- 6 filas con los datos de contacto de los duenos. El ::CHAR(1) esta
-- porque las columnas del UNION deben coincidir con el RETURNS TABLE; sin
-- el, el motor responde "structure of query does not match function result
-- type", que tambien es informativo: el atacante ajusta los tipos y sigue.

-- ----------------------------------------------------------------------
-- 4. La version segura: el dato viaja como parametro, no como texto
--
-- La diferencia esta en $1 y en USING. El texto de la sentencia es una
-- constante del programa; el valor va aparte y el motor NUNCA lo analiza
-- como codigo. No hay nada que escapar porque no hay nada que interpretar.
-- ----------------------------------------------------------------------
CREATE FUNCTION buscar_mascota_segura(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql
AS $fn$
BEGIN
  RETURN QUERY EXECUTE
    'SELECT id_mascota, nombre, especie, activa FROM mascota WHERE nombre = $1'
    USING p_nombre;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 4b. Mejor todavia: aqui no hacia falta SQL dinamico
--
-- El EXECUTE existe para armar sentencias cuyo TEXTO cambia -- otra tabla,
-- otra columna, otro ORDER BY --. Cuando lo unico que cambia es un valor,
-- la consulta estatica es mas simple, se planifica mejor y no da
-- oportunidad de equivocarse.
--
-- OJO A LA TRAMPA: los nombres del RETURNS TABLE son variables de
-- PL/pgSQL, asi que en una consulta estatica "id_mascota" es ambiguo
-- -- ¿la columna o la variable? --. Sin los alias m., esta funcion se crea
-- sin protestar y falla en la PRIMERA llamada con
--   ERROR: column reference "id_mascota" is ambiguous
-- La version con EXECUTE no tiene el problema porque su cadena se pasa al
-- motor sin sustitucion de variables. Es una diferencia real entre las dos
-- formas y conviene entenderla en vez de pelearse con el error.
-- ----------------------------------------------------------------------
CREATE FUNCTION buscar_mascota_directa(p_nombre TEXT)
RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))
LANGUAGE plpgsql
AS $fn$
BEGIN
  RETURN QUERY
    SELECT m.id_mascota, m.nombre, m.especie, m.activa
      FROM mascota m
     WHERE m.nombre = p_nombre;
END;
$fn$;

-- ----------------------------------------------------------------------
-- 5. Probar que el agujero quedo cerrado
--
-- Dos pruebas, no una: que el ataque falle Y que el uso legitimo siga
-- funcionando. Una funcion que devuelve 0 filas para todo tambien pasaria
-- la primera prueba.
-- ----------------------------------------------------------------------
SELECT * FROM buscar_mascota_segura('Firulais'' OR ''1''=''1');
-- 0 filas. La cadena completa -- con sus comillas y su OR -- se comparo
-- como un VALOR contra la columna nombre. Ninguna mascota se llama asi.

SELECT * FROM buscar_mascota_segura('Firulais');
-- 1 fila. El buscador sigue sirviendo para lo que existe.

SELECT * FROM buscar_mascota_directa('Firulais'' OR ''1''=''1');   -- 0 filas
SELECT * FROM buscar_mascota_directa('Firulais');                   -- 1 fila

-- El UNION tampoco pasa: ya no hay sentencia que reescribir.
SELECT COUNT(*) AS filas_del_ataque_contra_la_segura
  FROM buscar_mascota_segura(
    'x'' UNION SELECT id_dueno, nombre, email, ''S''::CHAR(1) FROM dueno --');
-- 0. El contraste 8 -> 0 es la evidencia del antes y despues.

-- ----------------------------------------------------------------------
-- 6. Eliminar la funcion vulnerable y dejar la regla escrita
--
-- Va de ultimo a proposito: si se hace el DROP antes, los pasos 1 a 3 ya
-- no se pueden ejecutar y se pierde la evidencia del incidente.
-- ----------------------------------------------------------------------
DROP FUNCTION buscar_mascota_insegura(TEXT);

-- Y la comprobacion de que ya no existe -- porque "la borre" tambien es
-- una afirmacion que se verifica:
SELECT COUNT(*) AS funciones_inseguras_restantes
  FROM information_schema.routines
 WHERE routine_name = 'buscar_mascota_insegura';
-- 0

-- ======================================================================
-- REGLA QUE ADOPTO PARA VETCARE (esto es lo que pide el punto 6)
--
-- -- 1. Ningun valor que provenga de un usuario se concatena en el texto
-- --    de una sentencia. Nunca, ni "solo por esta vez", ni en funciones
-- --    de solo lectura. Los valores viajan como parametros: $1 con USING
-- --    en PL/pgSQL, %s en psycopg2.
-- -- 2. El SQL dinamico se usa solo cuando cambia la ESTRUCTURA de la
-- --    sentencia (nombre de tabla, de columna, sentido del ORDER BY).
-- --    Si lo unico que cambia es un valor, la consulta va estatica.
-- -- 3. Cuando de verdad haya que construir un identificador, se hace con
-- --    format('... %I ...', v_columna), nunca con ||, porque los
-- --    parametros no pueden ligar identificadores: $1 sirve para valores.
-- -- 4. Una funcion de solo lectura tambien es una puerta.
-- --    buscar_mascota_insegura no escribia nada y entregaba la base
-- --    completa; precisamente por "solo consultar" nadie la reviso.
-- ======================================================================
```

### Salida esperada

```
1. Uso normal de la funcion vulnerable -- 1 fila

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S

2. El ataque OR '1'='1' -- 8 filas

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S
          2 | Luna     | Felino  | S
          3 | Rocky    | Canino  | N
          4 | Mishi    | Felino  | S
          5 | Bobby    | Canino  | S
          6 | Nube     | Felino  | S
          7 | Toby     | Canino  | S
          8 | Kiara    | Canino  | N

Ocho filas donde el negocio esperaba una. Y notese el detalle que suele pasar
inadvertido: aparecen Rocky y Kiara, que estan inactivas. El buscador de la
aplicacion filtraria las inactivas en la interfaz; el ataque se salta la
interfaz completa. La consulta no lleva ORDER BY, asi que el orden no esta
garantizado -- en una tabla recien sembrada sale el fisico, 1 a 8 -- y por eso la
evidencia que se entrega es el COUNT, no la captura.

3. La fuga, cuantificada -- 1 fila cada una

 filas_devueltas_por_el_ataque
-------------------------------
                             8

 filas_totales_en_la_tabla
---------------------------
                         8

Iguales. Ese par de numeros es el informe del incidente: un buscador de una
mascota devolvio el 100 % de la tabla. Y el nombre buscado era 'x', que no
existe -- el resultado ya no depende del dato.

3b. EXTRA, el UNION -- 6 filas

 id_mascota |     nombre     |         especie          | activa
------------+----------------+--------------------------+--------
          1 | Ana Gomez      | ana.gomez@mail.com       | S
          2 | Carlos Ruiz    | carlos.ruiz@mail.com     | S
          3 | Marcela Diaz   | marcela.diaz@mail.com    | S
          4 | Jorge Pineda   | jorge.pineda@mail.com    | S
          5 | Luisa Cardona  | luisa.cardona@mail.com   | S
          6 | Andres Vallejo | andres.vallejo@mail.com  | S

Detente aqui un momento, porque es el resultado que cambia la conversacion. La
columna que dice "especie" trae CORREOS ELECTRONICOS. La funcion nunca menciono
la tabla dueno y aun asi acaba de entregar los datos de contacto de los seis
clientes de la clinica. El OR '1'='1' era una fuga de una tabla; el UNION es una
fuga de cualquier tabla que el rol pueda leer. Un UNION no garantiza orden; da
igual, lo que importa son las 6 filas.

5. Contra la version segura -- 0 filas

 id_mascota | nombre | especie | activa
------------+--------+---------+--------
(0 filas)

Cero. La cadena Firulais' OR '1'='1 se comparo como un valor contra la columna
nombre, y ninguna mascota se llama asi. No hubo nada que escapar porque no hubo
nada que interpretar.

 id_mascota |  nombre  | especie | activa
------------+----------+---------+--------
          1 | Firulais | Canino  | S

Y el uso legitimo sigue funcionando, que es la mitad de la prueba que se olvida:
una funcion que devolviera 0 filas para todo tambien "resiste" el ataque.

 filas_del_ataque_contra_la_segura
-----------------------------------
                                 0

El contraste completo, que es lo que la rubrica exige: **8 antes, 0 despues.**

6. Despues del DROP -- 1 fila

 funciones_inseguras_restantes
-------------------------------
                             0

Si en algun momento aparece
  ERROR:  column reference "id_mascota" is ambiguous
  DETAIL:  It could refer to either a PL/pgSQL variable or a table column.
es buscar_mascota_directa sin los alias m.: los nombres del RETURNS TABLE son
variables de PL/pgSQL y chocan con las columnas de la tabla. Se arregla
calificando las columnas, no cambiando la consulta.
```

### Como calificar

- **4 pts — el uso normal y el ataque ejecutados y mostrados,** 2 pts cada uno. El ataque tiene que devolver las **8** filas; si devuelve 1, casi siempre es que las comillas no se duplicaron y la cadena llego literal. Se reconoce como sobresaliente escribir en un comentario el texto **final** que ejecuta el motor —`... WHERE nombre = 'Firulais' OR '1'='1'`—, porque es lo que hace visible que el dato se volvio codigo.
- **5 pts — el contraste cuantitativo con `COUNT`.** Es requisito literal de la rubrica —«se descuenta si no se muestra el contraste cuantitativo antes/despues»— y se califica de forma estricta: hacen falta los dos `COUNT` del antes (8 y 8, iguales) y el 0 del despues. Capturas de pantalla con «salieron muchas filas» valen 0 de 5: el informe de un incidente se sostiene en numeros comparables.
- **7 pts — `buscar_mascota_segura` con `EXECUTE ... USING` y la firma de retorno intacta.** 4 pts el `$1` con `USING` —no un `||` con comillas escapadas— y 3 pts que el `RETURNS TABLE (id_mascota INT, nombre TEXT, especie TEXT, activa CHAR(1))` sea identico al de la funcion que reemplaza, porque una funcion que cierra el agujero y cambia el contrato rompe la aplicacion que la llama.
- **4 pts — el ataque contra la version segura devolviendo 0 filas,** y se reconoce como sobresaliente probar **tambien** que el uso legitimo sigue devolviendo 1: una funcion que devolviera 0 filas para cualquier entrada tambien «resiste» el ataque y no sirve para nada. La pareja 0 filas / 1 fila es la prueba completa.
- **2 pts — la variante estatica `buscar_mascota_directa`,** que el enunciado sugiere como «mejor aun». Se otorgan si funciona; y **no se descuenta a quien no la incluya**, porque es opcional. Al calificar hay que anticipar el error de ambiguedad: sin los alias `m.` la funcion se crea sin protestar y falla en la primera llamada con «column reference “id_mascota” is ambiguous», porque los nombres del `RETURNS TABLE` son variables de PL/pgSQL.
- **3 pts — el `DROP FUNCTION buscar_mascota_insegura(TEXT);` y la regla propia en un comentario `--`.** 1 pt el `DROP` con la firma —`(TEXT)` es obligatorio— y 2 pts que la regla sea una regla: «usar parametros ligados siempre que sea posible» no lo es, «ningun valor de usuario se concatena en el texto de una sentencia» si. Se reconoce como sobresaliente distinguir que el SQL dinamico se justifica solo cuando cambia la **estructura** de la sentencia, y que para identificadores va `format('%I')` porque los parametros no ligan nombres de objetos.
- **Se reconoce como muy sobresaliente, sin puntos extra, la variante con `UNION`** que extrae los correos de los seis duenos a traves de un buscador de mascotas. Demuestra lo que el `OR '1'='1'` solo insinua: la fuga no se limita a la tabla consultada, alcanza cualquier tabla que el rol pueda leer. Es la lamina que hay que llevar a la sustentacion.

### Errores frecuentes y que hacer

- **El ataque devuelve 1 fila en vez de 8.** Casi siempre porque las comillas no se duplicaron: se escribio `buscar_mascota_insegura('Firulais' OR '1'='1')`, que ni siquiera es SQL valido, o se paso la cadena sin escapar. En SQL, para meter una comilla simple dentro de una cadena se duplica: `'Firulais'' OR ''1''=''1'`. Vale la pena mostrar el texto intermedio para que se vea que son dos niveles de comillas, no uno.
- **Escapar a mano en vez de ligar parametros:** `replace(p_nombre, '''', '''''')` y seguir concatenando. Cierra **este** ataque y no cierra el mecanismo: en un contexto numerico no hay comillas que escapar —`WHERE id_mascota = ' || p_id` con `p_id = '1 OR 1=1'` pasa limpio—, depende de la configuracion de escapes del servidor y hay que recordar aplicarlo en cada camino. Es exactamente la opcion falsa de la pregunta 4.
- **Cambiar la firma de retorno «para que quede mas limpia»,** por ejemplo devolviendo `SETOF mascota` o quitando `activa`. La funcion segura reemplaza a la insegura **en una aplicacion que ya la llama**; cambiar el contrato convierte una correccion de seguridad en una interrupcion del servicio, que es la razon por la que estas correcciones se posponen en la vida real.
- **`buscar_mascota_directa` sin alias de tabla.** Se crea sin errores y falla en la primera llamada con «column reference “id_mascota” is ambiguous». El estudiante suele concluir que «la consulta estatica no sirve» y volver al `EXECUTE`. La causa real es el sombreado de nombres del `RETURNS TABLE`, y la solucion son cuatro `m.`.
- **Hacer el `DROP` antes de demostrar el ataque.** El script queda en un orden que ya no se puede volver a ejecutar y la evidencia del incidente desaparece. La demostracion va primero; el `DROP` es la ultima linea.
- **`DROP FUNCTION buscar_mascota_insegura;` sin la firma.** Falla con «could not find a function named ...» o pide desambiguar. Es el mismo aprendizaje de la Clase 12 con los `GRANT`: las funciones se identifican por nombre **mas** tipos de argumentos.
- **Probar solo que el ataque falla.** Media prueba. Falta comprobar que la busqueda legitima sigue devolviendo su fila; sin eso no se sabe si se cerro el agujero o se rompio el buscador.

---

## Pregunta 3 · Mejora implementada 2: ningun borrado sin traza ni sin vuelta atras · 25 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- LO QUE SE CONSTRUYE AQUI, Y POR QUE SON TRES COSAS DISTINTAS
--
--   respaldo_cita + bitacora_respaldo  -> la copia, y la constancia de
--                                         cuantas filas tenia
--   cita_borrada + trg_archivar_cita   -> el archivo, que hace RECUPERABLE
--                                         un borrado accidental
--   la consulta de veredicto           -> la VERIFICACION, que es lo que
--                                         convierte una copia en una
--                                         capacidad comprobada
--
-- El caso analizado tenia lo primero -- cinco veces -- y no tenia lo
-- tercero. Por eso se perdieron datos con cinco respaldos disponibles.
-- ======================================================================

-- ----------------------------------------------------------------------
-- 1. Respaldo logico previo y su bitacora
--
-- CREATE TABLE ... AS SELECT copia estructura de columnas y datos, y NADA
-- mas: no trae la PK, ni los CHECK, ni las FK, ni la secuencia del SERIAL.
-- Para un respaldo eso esta bien -- lo que se quiere es el dato -- pero hay
-- que saberlo: respaldo_cita no es una tabla equivalente a cita.
-- ----------------------------------------------------------------------
CREATE TABLE respaldo_cita AS SELECT * FROM cita;

CREATE TABLE bitacora_respaldo (
  id_bitacora       SERIAL PRIMARY KEY,
  tabla             TEXT NOT NULL,
  filas_respaldadas INT  NOT NULL,
  hecho_en          TIMESTAMP NOT NULL DEFAULT now()
);

-- El conteo se CALCULA. Escribir "10" a mano es la version en miniatura
-- del error del caso: dejar constancia de lo que uno cree en vez de lo que
-- hay. Si el respaldo se hubiera hecho a medias, el 10 escrito a mano
-- mentiria y la verificacion del paso 5 diria OK sobre una base incompleta.
INSERT INTO bitacora_respaldo (tabla, filas_respaldadas)
SELECT 'cita', COUNT(*) FROM respaldo_cita;

SELECT * FROM bitacora_respaldo;          -- 1 fila: cita | 10

-- ----------------------------------------------------------------------
-- 2. Archivo de borrados + trigger
--
-- Mismas columnas que cita, mas quien borro y cuando. Y a proposito SIN
-- llaves foraneas: un archivo tiene que poder sobrevivir a lo que archiva.
-- Es el mismo argumento de audit_cita en la Clase 4, y aqui es mas fuerte,
-- porque si manana se borra una mascota, una FK impediria conservar la
-- traza de sus citas -- justo cuando mas se necesita.
-- ----------------------------------------------------------------------
CREATE TABLE cita_borrada (
  id_cita        INT,
  id_mascota     INT,
  id_veterinario INT,
  fecha_hora     TIMESTAMP,
  estado         TEXT,
  borrado_en     TIMESTAMP DEFAULT now(),
  usuario_bd     TEXT      DEFAULT current_user
);

-- Un trigger son SIEMPRE dos objetos: la funcion y la asociacion.
CREATE FUNCTION fn_trg_archivar_cita()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  INSERT INTO cita_borrada (id_cita, id_mascota, id_veterinario,
                            fecha_hora, estado)
  VALUES (OLD.id_cita, OLD.id_mascota, OLD.id_veterinario,
          OLD.fecha_hora, OLD.estado);
  -- RETURN OLD deja pasar el borrado. Si aqui se escribe RETURN NEW -- que
  -- en un DELETE vale NULL --, el borrado se CANCELA en silencio: la fila
  -- se archiva, cita conserva sus 10 filas y el DELETE informa 0. Parece
  -- que funciono y no funciono nada.
  RETURN OLD;
END;
$fn$;

CREATE TRIGGER trg_archivar_cita
  BEFORE DELETE ON cita
  FOR EACH ROW
  EXECUTE FUNCTION fn_trg_archivar_cita();

-- ----------------------------------------------------------------------
-- 3. Reproducir el incidente: el DELETE sin WHERE
--
-- Esta es la sentencia del caso, en miniatura y en una base desechable.
-- Diez filas aqui; la agenda completa de la clinica en produccion.
-- ----------------------------------------------------------------------
DELETE FROM cita;                          -- DELETE 10

SELECT COUNT(*) AS filas_en_cita          FROM cita;           -- 0
SELECT COUNT(*) AS filas_en_cita_borrada  FROM cita_borrada;   -- 10

-- Y el archivo, para verlo: trae quien y cuando, que es lo que el caso
-- real tuvo que reconstruir a mano.
SELECT id_cita, id_mascota, estado, usuario_bd
  FROM cita_borrada
 ORDER BY id_cita;

-- ----------------------------------------------------------------------
-- 4. Restaurar, con columnas explicitas
--
-- Columnas explicitas y no INSERT INTO cita SELECT * FROM cita_borrada,
-- que falla: cita_borrada tiene dos columnas mas. Ademas el SELECT *
-- depende del orden fisico de las columnas, y eso es exactamente el tipo
-- de suposicion que rompe un guion de recuperacion el dia que se usa.
-- ----------------------------------------------------------------------
INSERT INTO cita (id_cita, id_mascota, id_veterinario, fecha_hora, estado)
SELECT id_cita, id_mascota, id_veterinario, fecha_hora, estado
  FROM cita_borrada
 ORDER BY id_cita;                         -- INSERT 0 10

-- La secuencia del SERIAL NO se movio con estos INSERT, porque el id se
-- dio explicito. Aqui no hay choque -- la secuencia ya iba en 10 y las
-- secuencias no se devuelven, como se vio en la Clase 8 --, pero en una
-- restauracion sobre una tabla recien creada la secuencia estaria en 1 y
-- el primer INSERT normal reventaria contra la PK. Realinearla es parte
-- del guion de recuperacion, no un detalle:
SELECT last_value AS secuencia_antes FROM cita_id_cita_seq;      -- 10
SELECT setval(pg_get_serial_sequence('cita','id_cita'),
              (SELECT MAX(id_cita) FROM cita));                  -- 10

-- ----------------------------------------------------------------------
-- 5. Verificar la restauracion: la consulta que faltaba en el caso real
--
-- Una sola fila, con lo esperado, lo obtenido, los extremos del rango y un
-- veredicto calculado. No es adorno: es la diferencia entre "restaure" y
-- "comprobe que la restauracion quedo bien". El ORDER BY ... LIMIT 1 esta
-- porque si el script se vuelve a correr, la bitacora tendria dos filas y
-- la consulta dejaria de devolver una sola.
-- ----------------------------------------------------------------------
SELECT b.filas_respaldadas                        AS filas_esperadas,
       (SELECT COUNT(*) FROM cita)                AS filas_actuales,
       (SELECT MIN(fecha_hora) FROM cita)         AS primera_cita,
       (SELECT MAX(fecha_hora) FROM cita)         AS ultima_cita,
       CASE WHEN b.filas_respaldadas = (SELECT COUNT(*) FROM cita)
            THEN 'RESTAURACION OK'
            ELSE 'REVISAR'
       END                                        AS veredicto
  FROM bitacora_respaldo b
 WHERE b.tabla = 'cita'
 ORDER BY b.id_bitacora DESC
 LIMIT 1;

-- ----------------------------------------------------------------------
-- 5b. EXTRA: tapar el hueco del propio control (va mas alla del enunciado)
--
-- Un trigger FOR EACH ROW se dispara con DELETE y NO se dispara con
-- TRUNCATE, que borra sin recorrer filas. Es decir: el control que se
-- acaba de construir no cubre la sentencia mas destructiva de las dos.
-- Se cierra con un trigger de sentencia, y se puede COMPROBAR sin perder
-- nada, porque el TRUNCATE queda bloqueado.
-- ----------------------------------------------------------------------
CREATE FUNCTION fn_trg_bloquear_truncate()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $fn$
BEGIN
  RAISE EXCEPTION
    'TRUNCATE bloqueado en %: use DELETE para que el archivo funcione',
    TG_TABLE_NAME;
END;
$fn$;

CREATE TRIGGER trg_bloquear_truncate_cita
  BEFORE TRUNCATE ON cita
  FOR EACH STATEMENT
  EXECUTE FUNCTION fn_trg_bloquear_truncate();

TRUNCATE cita;
-- ERROR: TRUNCATE bloqueado en cita: use DELETE para que el archivo funcione
-- Las 10 filas siguen ahi. Un control probado es uno que se vio estorbar.

SELECT COUNT(*) AS filas_tras_intentar_truncate FROM cita;       -- 10

-- ======================================================================
-- POR QUE EL TRIGGER Y LA CONSULTA SON CONTROLES DISTINTOS
--
-- -- El trigger es un control de RECUPERACION: no evita nada. El DELETE
-- -- sin WHERE se ejecuta igual y cita queda en cero. Lo que hace es
-- -- convertir un dano irreversible en uno reversible, guardando el dato
-- -- y quien lo borro. Actua en el momento del incidente y de forma
-- -- automatica, sin depender de que nadie se acuerde.
-- --
-- -- La consulta de veredicto es un control de VERIFICACION: no protege
-- -- ningun dato, comprueba una afirmacion. Responde "¿la restauracion
-- -- quedo completa?" con un numero comparable, no con una impresion.
-- -- Actua DESPUES y solo si alguien la ejecuta.
-- --
-- -- Hacen falta los dos porque cada uno falla donde el otro no llega:
-- -- con archivo y sin verificacion se restaura a medias y se declara
-- -- resuelto -- que es literalmente el caso analizado, con cinco copias
-- -- y ninguna probada --; con verificacion y sin archivo se detecta la
-- -- perdida con precision y no hay nada que reponer. Y los dos juntos
-- -- siguen sin proteger contra perder la instancia: respaldo_cita y
-- -- cita_borrada viven en la MISMA base. Eso lo cubre un respaldo
-- -- fisico externo, que es la mejora pendiente de la pregunta 5.
-- ======================================================================
```

### Salida esperada

```
1. Bitacora del respaldo -- 1 fila

 id_bitacora | tabla | filas_respaldadas |          hecho_en
-------------+-------+-------------------+----------------------------
           1 | cita  |                10 | 2026-11-02 19:14:33.201

El 10 salio de un COUNT sobre respaldo_cita, no de los dedos. La marca de tiempo
varia en cada corrida y no se califica.

3. El incidente

DELETE 10

 filas_en_cita
---------------
             0

 filas_en_cita_borrada
-----------------------
                    10

Cero y diez: el borrado ocurrio de verdad -- el trigger no lo evita -- y el dato
esta a salvo. Esa es la definicion de "incidente recuperable".

El archivo -- 10 filas

 id_cita | id_mascota |   estado   | usuario_bd
---------+------------+------------+------------
       1 |          1 | PROGRAMADA | postgres
       2 |          2 | ATENDIDA   | postgres
       3 |          4 | PROGRAMADA | postgres
       4 |          5 | CANCELADA  | postgres
       5 |          6 | ATENDIDA   | postgres
       6 |          7 | PROGRAMADA | postgres
       7 |          1 | ATENDIDA   | postgres
       8 |          2 | PROGRAMADA | postgres
       9 |          4 | PROGRAMADA | postgres
      10 |          6 | ATENDIDA   | postgres

El usuario_bd sale de current_user y en ExamLab es el rol del entorno -- suele ser
postgres --; el nombre no es lo que se califica, que la columna exista y se
llene si. En produccion esa columna es la que responde "¿quien lo borro?" sin
tener que reconstruirlo de la memoria de nadie.

4. Restauracion

INSERT 0 10

 secuencia_antes
-----------------
              10

 setval
--------
     10

El setval no cambia nada aqui, y esta a proposito: la secuencia ya iba en 10
porque las secuencias no se devuelven. En una restauracion sobre una tabla recien
creada estaria en 1 y el primer INSERT normal chocaria contra la llave primaria.
Realinearla pertenece al guion de recuperacion.

5. El veredicto -- 1 fila

 filas_esperadas | filas_actuales |    primera_cita     |     ultima_cita     |    veredicto
-----------------+----------------+---------------------+---------------------+-----------------
              10 |             10 | 2026-09-01 08:00:00 | 2026-09-10 09:00:00 | RESTAURACION OK

Esta fila es el entregable de la pregunta. No dice "restaure la tabla": dice que
las filas esperadas y las presentes coinciden y que el rango de fechas es el que
tenia que ser -- del 1 al 10 de septiembre --. Los dos extremos importan: un
conteo correcto con un MIN o un MAX desplazado significa que se restauro otra
cosa, o solo una parte, y el conteo solo no lo delataria.

Si sale REVISAR, el veredicto esta haciendo su trabajo: hay que mirar el
INSERT ... SELECT antes de seguir. Y si la consulta devuelve DOS filas, es que el
script se corrio dos veces y la bitacora tiene dos entradas -- para eso esta el
ORDER BY ... LIMIT 1.

5b. EXTRA: el hueco del propio control

ERROR:  TRUNCATE bloqueado en cita: use DELETE para que el archivo funcione

 filas_tras_intentar_truncate
------------------------------
                           10

Y ahi esta lo incomodo: el trigger FOR EACH ROW que se acaba de construir **no
se dispara con TRUNCATE**, que es la sentencia mas destructiva de las dos. El
control tenia un agujero del tamano de una palabra. El trigger de sentencia lo
cierra, y se pudo comprobar sin perder nada porque el bloqueo funciona.
```

### Como calificar

- **4 pts — `respaldo_cita` y `bitacora_respaldo`,** 1,5 y 1,5 pts, mas **1 pt reservado a que el conteo se calcule con una subconsulta y no se escriba a mano.** Ese punto suelto es deliberado: es requisito literal de la rubrica y es la version en miniatura del error del caso —dejar constancia de lo que uno cree en vez de lo que hay—. Un `filas_respaldadas` con un `10` literal mentiria si el respaldo hubiera quedado a medias, y la verificacion del paso 5 diria `RESTAURACION OK` sobre una base incompleta.
- **7 pts — `cita_borrada` y el trigger.** 2 pts la tabla con las cinco columnas de `cita` mas `borrado_en` y `usuario_bd` con sus `DEFAULT`; 3 pts la funcion `fn_trg_archivar_cita()` insertando los valores de `OLD` **columna por columna** y terminando en `RETURN OLD`; 2 pts la asociacion `BEFORE DELETE ON cita FOR EACH ROW`. Se reconoce como sobresaliente justificar que `cita_borrada` **no** lleva llaves foraneas: un archivo tiene que sobrevivir a lo que archiva, y una FK a `mascota` impediria conservar la traza el dia que se borre una mascota.
- **4 pts — el `DELETE FROM cita;` y las dos consultas de comprobacion,** con `cita` en **0** y `cita_borrada` en **10**. Si las dos dan 10, el trigger devuelve `NULL` —tipicamente un `RETURN NEW`, que en un `DELETE` vale `NULL`— y **el borrado se cancelo en silencio**: hay que devolverlo, porque el estudiante suele leerlo como exito.
- **4 pts — la restauracion con columnas explicitas.** 3 pts el `INSERT INTO cita (...) SELECT ...` reponiendo las 10 filas y 1 pt que las columnas esten enumeradas: un `SELECT *` desde `cita_borrada` falla —tiene dos columnas mas— y ademas depende del orden fisico de las columnas, que es justo la suposicion que rompe un guion de recuperacion el dia que se usa.
- **5 pts — la consulta de validacion en una sola fila con las cinco columnas y el `veredicto` calculado con `CASE`.** 3 pts la estructura —esperadas, actuales, `MIN`, `MAX`, veredicto— y 2 pts que el veredicto sea **calculado** y no un literal `'RESTAURACION OK'` escrito porque ya se sabe el resultado. Una consulta que devuelva dos filas no cumple «una sola fila»: pasa cuando el script se corre dos veces y la bitacora acumula, y se resuelve con `ORDER BY id_bitacora DESC LIMIT 1`.
- **1 pt — el comentario final distinguiendo los dos controles.** El argumento correcto es que el trigger es **recuperacion** —no evita nada, hace reversible el dano, actua automaticamente en el momento— y la consulta es **verificacion** —no protege ningun dato, comprueba una afirmacion, actua despues y solo si alguien la ejecuta—; y que hacen falta los dos porque con archivo y sin verificacion se restaura a medias y se declara resuelto, que es literalmente el caso analizado.
- **Se reconoce como muy sobresaliente, sin puntos extra:** notar que un trigger `FOR EACH ROW` **no se dispara con `TRUNCATE`**, de modo que el control recien construido no cubre la sentencia mas destructiva, y cerrarlo con un trigger `BEFORE TRUNCATE ... FOR EACH STATEMENT`; o dejar escrito que `respaldo_cita` y `cita_borrada` viven en la **misma** base y por tanto no protegen contra perder la instancia, que es exactamente el error de razonamiento del caso.

### Errores frecuentes y que hacer

- **`RETURN NEW` en el trigger de `DELETE`.** Es el error mas enganoso de la pregunta: en un `DELETE`, `NEW` vale `NULL`, y un trigger `BEFORE` que devuelve `NULL` **cancela la operacion**. El resultado es que la fila se archiva, `cita` conserva sus 10 filas, el motor informa `DELETE 0` y el estudiante concluye que su control «evito el borrado». No evito nada: rompio el `DELETE`. La comprobacion que lo delata son las dos consultas del paso 3.
- **Escribir el conteo a mano** en `bitacora_respaldo`, casi siempre porque «son 10, ya lo vi». Es el error del caso reproducido: la bitacora deja de ser evidencia y pasa a ser una opinion, y si el respaldo hubiera quedado incompleto la verificacion del paso 5 daria `OK` de todas formas. La rubrica lo pide calculado con esas palabras.
- **`INSERT INTO cita SELECT * FROM cita_borrada;`.** Falla, porque `cita_borrada` tiene siete columnas y `cita` cinco. Al intentar arreglarlo aparece la segunda version del error —enumerar las columnas del `INSERT` pero dejar el `SELECT *`—, que tambien falla. Las dos listas van explicitas y en el mismo orden.
- **Un `veredicto` escrito a mano:** `'RESTAURACION OK' AS veredicto`. Ya se sabe que salio bien, asi que «para que el `CASE`». Porque el control no es para hoy: es la consulta que alguien va a correr dentro de seis meses, a las tres de la manana, sin saber el resultado esperado. Un veredicto literal siempre dice OK, tambien cuando no lo esta.
- **Olvidar el `RETURN OLD` por completo** —una funcion de trigger que termina sin `RETURN`—. En PL/pgSQL una funcion `RETURNS TRIGGER` que cae al final devuelve `NULL`, con el mismo efecto que el `RETURN NEW`: el borrado se cancela. El sintoma es identico y la causa tambien.
- **Creer que `CREATE TABLE respaldo_cita AS SELECT * FROM cita;` crea una tabla equivalente.** Copia columnas y datos, y nada mas: sin PK, sin `CHECK`, sin FK, sin secuencia. Sirve como respaldo de datos y no sirve para reemplazar la tabla. Conviene decirlo antes de que alguien planee la recuperacion apoyandose en eso.
- **Poner llaves foraneas en `cita_borrada`** «para que quede bien modelada». Invierte el proposito: el archivo tiene que sobrevivir a lo que archiva, y una FK a `mascota` haria fallar el borrado de una mascota justo cuando conservar la traza de sus citas es lo unico que queda. Es el mismo argumento de `audit_cita` en la Clase 4.
- **Concluir que con el trigger «ya no se puede perder una cita».** No cubre `TRUNCATE`, no cubre `DROP TABLE`, no cubre a quien haga `ALTER TABLE cita DISABLE TRIGGER`, y sobre todo el archivo vive en la misma base que el original. Protege contra un error logico; no contra perder la instancia.

---

## Pregunta 4 · Que control habria evitado el incidente · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | Un respaldo solo cuenta como valido cuando se ha restaurado en un entorno de prueba y una consulta de verificacion confirmo conteos y rangos de datos esperados. | **Correcta, y es la tesis del caso A.** Una copia es un archivo; el control es la restauracion verificada. El caso analizado tenia cinco copias y perdio datos porque ninguna se habia restaurado nunca. La palabra que hace verdadera la afirmacion es «confirmo conteos y rangos»: es lo que hace la consulta de veredicto de la pregunta 3, y por eso pide `MIN` y `MAX` ademas del conteo —un conteo correcto con un rango desplazado significa que se restauro otra cosa—. |
| no | Escapar manualmente las comillas de la entrada del usuario antes de concatenarla es equivalente a usar parametros ligados. | **Falsa, y es la opcion que mas se marca por error,** porque escapar *parece* resolver el problema. No es equivalente por tres razones acumulativas. Primera: en un contexto numerico no hay comillas que escapar, asi que `'... WHERE id_mascota = ' || p_id` con `p_id` igual a `1 OR 1=1` pasa intacto. Segunda: escapar correctamente depende de la configuracion de escapes del servidor y de la codificacion, y hay motores donde la funcion ingenua es insuficiente. Tercera y decisiva: es un control que hay que **acordarse** de aplicar en cada camino del codigo, y un solo camino olvidado es el agujero completo. Ligar parametros no mejora la defensa: **elimina el mecanismo**, porque el valor nunca llega al analizador de sentencias. |
| **SI** | Usar parametros ligados (EXECUTE ... USING, o %s desde la aplicacion) elimina la inyeccion porque la entrada viaja como valor y nunca se interpreta como codigo SQL. | **Correcta, y conviene fijarse en la razon que da la afirmacion,** que es la que hay que poder repetir: «la entrada viaja como valor y nunca se interpreta como codigo». No es que el motor limpie la cadena —no la limpia—, es que el texto de la sentencia se planifica **antes** y por separado, asi que el dato ya no tiene forma de convertirse en instruccion. Es lo que la pregunta 2 demuestra con el 8 → 0. |
| no | Tener cinco mecanismos de respaldo garantiza la recuperacion, aunque ninguno se haya probado. | **Falsa, y es la descripcion literal del incidente:** cinco mecanismos, ninguno probado, cero recuperacion. Peor todavia, la cantidad genero una falsa sensacion de seguridad —con cinco copias nadie sintio la necesidad de probar una—. La regla practica que se deriva: **un respaldo verificado vale mas que cinco sin verificar**, y un respaldo cuyo fallo pasa inadvertido no cuenta como respaldo. |
| **SI** | Un trigger que archiva las filas antes de borrarlas convierte un borrado accidental en un incidente recuperable, aunque no evita el error humano. | **Correcta, y hay que subrayar la segunda mitad de la frase:** «aunque no evita el error humano». Es exactamente lo que se comprueba en la pregunta 3: el `DELETE FROM cita;` se ejecuta, `cita` queda en 0 y el trigger no lo impide. Lo que hace es cambiar la naturaleza del incidente, de perdida definitiva a interrupcion recuperable. Es un control de recuperacion, no de prevencion, y confundirlos lleva a creerse protegido. |
| **SI** | Un indice adecuado mas la eliminacion de SELECT * en un reporte que corre cada minuto pueden ser la diferencia entre un panel util y una caida del servicio en hora pico. | **Correcta, y es el caso B.** El mecanismo es concreto: sin indice, la consulta recorre la tabla completa; con `SELECT *`, cada recorrido arrastra columnas que el reporte no usa y multiplica la memoria y el trafico; y cada minuto significa que una ejecucion todavia corriendo se solapa con la siguiente, hasta agotar las conexiones. Los tres factores se suman, y es el mismo diagnostico de las Clases 6 y 7: `Rows Removed by Filter` alto es trabajo que se paga y no se usa. |

### Como calificar

- **10 pts con las cuatro correctas —0, 2, 4 y 5— y ninguna incorrecta;** puntaje proporcional por acierto parcial, tal como declara la rubrica de la plataforma. Al revisar en grupo conviene senalar que las cuatro correctas son los cuatro controles del curso: verificar el respaldo, ligar parametros, archivar antes de borrar y medir el plan de una consulta.
- **La opcion 1 —escapar comillas a mano— es la que mas se marca por error** y merece explicacion aparte, no solo un «es falsa». Tres razones acumulativas: en contexto numerico no hay comillas que escapar; el escape correcto depende de la configuracion del servidor; y es un control que hay que recordar aplicar en cada camino del codigo. Ligar parametros **elimina el mecanismo** en vez de reforzar la defensa.
- **La opcion 3 es el caso A en una linea** y sirve para comprobar si el estudiante lo leyo: quien marque «tener cinco respaldos garantiza la recuperacion» no analizo el incidente, porque el incidente es precisamente eso saliendo mal. Conviene devolverlo con la cifra: cinco mecanismos, ninguno utilizable, seis horas perdidas.
- **En la opcion 4 lo que se califica es entender la segunda mitad de la frase:** «aunque no evita el error humano». Es la distincion prevencion/recuperacion que la pregunta 3 demuestra ejecutando el `DELETE` y viendo `cita` en 0. Un estudiante que la marque bien pero crea que el trigger impide el borrado tiene el punto y no la idea.
- **Errores frecuentes de seleccion:** marcar solo 0 y 2 —quedarse con los dos controles «de libro» y descartar el trigger por «no evitar nada», que es justamente lo que la opcion admite— o marcar las seis, que suele indicar que se respondio por intuicion sin leer las dos negativas.

### Errores frecuentes y que hacer

- **Marcar la opcion 1 creyendo que escapar y ligar son lo mismo.** Es el error conceptual central de la clase y no se cierra diciendo «es falsa»: hay que mostrar el contraejemplo numerico, donde no hay ni una comilla que escapar y la inyeccion pasa igual.
- **Marcar la opcion 3** porque «cinco es mejor que uno». Cinco copias sin probar son cinco archivos con nombre tranquilizador, y ademas producen la falsa sensacion de seguridad que impidio probar alguna. La opcion es el caso analizado, escrito en afirmativo.
- **Descartar la opcion 4** razonando «si no evita el error, no es un control». Confunde prevencion con recuperacion. La mayoria de los controles de un sistema real no evitan el fallo: acotan su consecuencia, y esa es toda la diferencia entre una interrupcion de dos horas y una perdida definitiva.
- **Descartar la opcion 5** por parecer exagerada. No lo es, y esta medida en el propio curso: en la Clase 6 la misma consulta pasa de recorrer la tabla completa a resolverse por indice, y en la Clase 7 se vio que el problema no es solo el tiempo sino el trabajo desperdiciado que `Rows Removed by Filter` delata.
- **Marcar las seis opciones.** Con una pregunta de seleccion multiple y puntaje proporcional, marcar todo no maximiza nada: las dos incorrectas restan. Y ademas revela que no se leyeron, porque 1 y 3 se contradicen directamente con las conclusiones de las preguntas 2 y 3 del mismo taller.

---

## Pregunta 5 · Tres mejoras priorizadas para VetCare · 15 pts

### Respuesta esperada

| # | Mejora concreta | Objeto de VetCare que cambia | Riesgo que mitiga | Esfuerzo | Impacto | Como se verifica | Estado |
|---|---|---|---|---|---|---|---|
| 1 | Reemplazar el buscador que concatena por uno con parametros ligados y eliminar el vulnerable | Funciones `buscar_mascota_segura` y `buscar_mascota_directa` creadas; `buscar_mascota_insegura` eliminada con `DROP FUNCTION` | Fuga de datos personales por inyeccion de SQL. El ataque no solo entregaba las 8 mascotas: con un `UNION` entregaba los correos de los 6 duenos | Bajo | Alto | Ya ejecutado: el ataque `'Firulais'' OR ''1''=''1'` devuelve **8 filas** contra la funcion vieja y **0 filas** contra `buscar_mascota_segura`, y `buscar_mascota_segura('Firulais')` sigue devolviendo su fila | **IMPLEMENTADA** |
| 2 | Archivar toda cita antes de borrarla y verificar cada restauracion con una consulta de veredicto | Tabla `cita_borrada`, funcion `fn_trg_archivar_cita()`, trigger `trg_archivar_cita` (`BEFORE DELETE ... FOR EACH ROW`) y tabla `bitacora_respaldo` | Perdida definitiva por un borrado accidental, y restauracion incompleta declarada como exitosa —los dos fallos del caso— | Medio | Alto | Ya ejecutado: `DELETE FROM cita;` dejo `cita` en **0** y `cita_borrada` en **10**; tras el `INSERT ... SELECT` la consulta de validacion devolvio `10 | 10 | 2026-09-01 08:00 | 2026-09-10 09:00 | RESTAURACION OK` | **IMPLEMENTADA** |
| 3 | Ensayar de punta a punta un respaldo **fisico externo**: `pg_dump` de la base completa, restauracion en una base vacia y ejecucion de la bateria de verificacion de la Clase 11 | Script nuevo `09_respaldo_y_restore.sql` mas la tabla `checklist_pi` de la Clase 11, que registra el resultado del ensayo | Perdida total por fallo de la instancia o del disco. Las mejoras 1 y 2 viven **dentro** de la misma base: no cubren este caso | Medio | Alto | `pg_restore --list` demuestra que el archivo es legible; la prueba real es que la bateria de la Clase 11 sobre la base restaurada devuelva el **mismo** resultado, incluido el `cumple = FALSE` de la prueba 5 | **PENDIENTE** · responsable: el estudiante que sustenta · fecha: **2026-11-06** |

### 1. Priorizacion: que haria primero con un solo dia

**La tercera, el ensayo de restauracion,** y no porque sea la mas atractiva sino porque es la unica que queda y es **la unica irreversible**. Las mejoras 1 y 2 estan hechas, asi que la comparacion real es entre cerrar el ensayo o dedicar el dia a pulir el informe. Con esfuerzo medio e impacto alto, el ensayo gana sin discusion: un error de redaccion se arregla el dia siguiente, y un respaldo que no restaura no se arregla **despues** del incidente. Ademas es el unico item en `NO` del checklist de la Clase 11 y la tercera pregunta que el jurado va a hacer.

**Y si ninguna estuviera hecha, el orden seria 1 → 2 → 3,** por dos criterios distintos que conviene separar. Por esfuerzo/impacto, la mejora 1 es la unica con esfuerzo **bajo** e impacto alto: dos funciones y un `DROP`, media hora. Y por urgencia, es la unica que cierra un agujero **activo**: `buscar_mascota_insegura` era explotable en ese momento, mientras que las mejoras 2 y 3 mitigan un incidente **futuro**. Cuando un riesgo ya se esta materializando y otro todavia no, el que se esta materializando va primero, aunque el otro tenga peor consecuencia.

### 2. Que dice esto de mi diseno

El caso puso en evidencia **tres supuestos** que estaban en el proyecto sin que nadie los hubiera escrito, y por lo tanto sin que nadie los hubiera discutido.

**El primero, y el que mas me sorprendio: supuse que la capa `api_*` de la Clase 12 cerraba la inyeccion.** No la cierra. La cierra para las tres operaciones de escritura, que son las que revise; `buscar_mascota_insegura` era una funcion de **solo lectura** y no la miro nadie, precisamente porque «solo consulta». Ahi estaba el agujero, y era el mas grave del proyecto: no modificaba un dato, entregaba la base. La leccion es incomoda y util: **el codigo que nadie audita es el que solo lee.**

**El segundo: supuse que tener una copia era poder recuperar.** El plan de respaldo del informe declara un RPO de 15 minutos y un RTO de 4 horas, y esos dos numeros nunca se midieron: son estimaciones presentadas como compromisos. El caso muestra el resultado de esa confusion con cinco copias en vez de una.

**El tercero: supuse que auditar los cambios era auditar todo.** `audit_cita`, de la Clase 4, registra los `UPDATE` de estado. **Un `DELETE` no dejaba rastro**, asi que el evento mas destructivo era el unico sin traza. Es el patron del caso otra vez: los controles cubrian lo que se esperaba que pasara.

### 3. Actualizacion del informe del PI

El analisis entra en la seccion de **seguridad y control de acceso**, como una subseccion nueva —«Analisis de un incidente real y mejoras derivadas»— con la tabla de tres filas como cierre, y se referencia desde la seccion de **respaldo y recuperacion**, donde la mejora 3 pasa a ser la prueba de aceptacion del plan en lugar de una intencion. Los dos scripts nuevos entran en el orden de ejecucion: el buscador seguro va con las funciones de la API —despues de `06_api.sql`— y el archivo de borrados con el resto de triggers.

**Las dos frases que agrego a lecciones aprendidas:**

> Un respaldo que no se ha restaurado no es un respaldo: es un archivo con un nombre tranquilizador. Lo unico que cuenta como control es la restauracion verificada con conteos y rangos.

> Una funcion de solo lectura tambien es una puerta. `buscar_mascota_insegura` no escribia nada, no aparecia en ninguna revision por eso mismo, y entregaba la base completa —incluidos los correos de los clientes— a quien escribiera una comilla en el buscador.

### Como calificar

- **6 pts — la tabla con exactamente tres filas y las ocho columnas,** 2 pts por fila. Dentro de cada fila: 0,5 que la mejora sea concreta, 0,5 que la columna de objeto nombre un **objeto real** de la base —tabla, funcion, trigger, indice, rol—, 0,5 el riesgo que mitiga, 0,5 esfuerzo e impacto. Una fila que diga «mejorar la seguridad» en objeto vale 0,5 de 2: la rubrica exige objetos, no intenciones. Mas o menos de tres filas incumple el enunciado.
- **4 pts — que dos filas esten en `IMPLEMENTADA` y citen la prueba real que se corrio** en las preguntas 2 y 3, 2 pts cada una. La cita tiene que ser verificable: «el ataque contra `buscar_mascota_segura` devuelve 0 filas frente a las 8 de la insegura», «la consulta de validacion devolvio 10 | 10 | `RESTAURACION OK`». «Lo probe y funciono» vale 0,5 de 2. Este es el punto que convierte la tabla en un informe de trabajo hecho y no en una lista de deseos.
- **2 pts — la tercera fila en `PENDIENTE` con responsable y fecha,** 1 pt cada uno. La fecha tiene que ser anterior al **2026-11-16**, que es la sustentacion, y conviene revisar que no caiga el 2026-11-09, que es el Parcial 3. Un «pendiente» sin fecha no es un plan.
- **2 pts — la priorizacion argumentada con esfuerzo/impacto,** no por gusto ni por orden de aparicion. Se acepta cualquier orden bien defendido. Se reconoce como sobresaliente separar los dos criterios que aqui apuntan distinto: por esfuerzo/impacto gana la mejora 1 —esfuerzo bajo, impacto alto—, y por urgencia tambien, porque es la unica que cierra un agujero **activo** frente a dos que mitigan un incidente futuro.
- **1 pt — el supuesto de diseno que el caso puso en evidencia,** formulado como supuesto y no como tarea. «Me falta probar el respaldo» es una tarea; «supuse que tener una copia era poder recuperar» es un supuesto, y es lo que se pide. Se reconoce como sobresaliente el que casi nadie ve: **la capa `api_*` de la Clase 12 no cerraba la inyeccion**, porque solo cubria las escrituras, y el agujero estaba en una funcion de solo lectura que nadie reviso justamente por «solo consultar».
- **La actualizacion del informe se califica dentro de los puntos anteriores** y lo que se busca es que nombre una seccion existente y una frase concreta para lecciones aprendidas, no un «lo agrego al informe». Y conviene contrastar: si la tabla declara el respaldo resuelto mientras el checklist de la Clase 11 lo tiene en `NO`, hay una contradiccion entre dos entregables del mismo estudiante, y es mejor senalarla al calificar que dejarla para el jurado.

### Errores frecuentes y que hacer

- **Filas con intenciones en vez de objetos:** «mejorar la seguridad de la base», «hacer respaldos». La rubrica pide un objeto real —`buscar_mascota_segura`, `trg_archivar_cita`, `idx_cita_vet_fecha`, `app_vetcare`— porque un plan de mejoras cuya unidad no es un objeto no se puede verificar ni asignar.
- **Marcar `IMPLEMENTADA` sin citar la prueba,** o citando una que no se corrio. Es lo mismo que declaro resuelto el respaldo en el caso analizado. La columna de verificacion pide el numero: 8 → 0, 0 y 10, `RESTAURACION OK`.
- **Una tercera fila con estado `PENDIENTE` y sin responsable ni fecha,** o con una fecha posterior al 2026-11-16. Un pendiente sin fecha se convierte en un pendiente permanente, que es como el item del respaldo llego hasta aqui.
- **Priorizar por gusto:** «haria primero la 1 porque es la que mas me interesa». El enunciado pide la relacion esfuerzo/impacto, y es una herramienta, no un formalismo: obliga a comparar el costo de hacer con el costo de no hacer.
- **Confundir el supuesto con la tarea.** «Me falta ensayar el restore» es lo que hay que hacer; el supuesto es el que llevo a no hacerlo: «supuse que tener el respaldo era suficiente». La pregunta apunta al segundo, porque es el que se repite en el proyecto siguiente.
- **Repetir una de las mejoras ya implementadas como la tercera fila** con otras palabras, para no tener que pensar una pendiente. Se detecta rapido: las tres filas deben nombrar objetos distintos.
- **Elegir el caso B en la pregunta 1 y despues no poder llenar las dos filas `IMPLEMENTADA`.** El enunciado permite B pero las preguntas 2 y 3 implementan mejoras de C y de A. La salida limpia es citar como implementada la mejora de rendimiento de la Clase 6 —`idx_cita_vet_fecha` con sus dos `EXPLAIN`— y decirlo asi en la tabla.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**Es una clase autonoma y no hay quien me responda en el momento. ¿Que hago si me trabo?**

Todo lo que necesitas esta en el enunciado —incluidas las cadenas de ataque y el cuerpo de la funcion segura— y las tres cosas que trancan a mas gente estan resueltas en estas preguntas frecuentes: el error de ambiguedad de `buscar_mascota_directa`, el `RETURN NEW` que cancela el borrado y el orden del `DROP`. La sesion es el **2026-11-02**; el **2026-11-09** es el Parcial 3 y el **2026-11-16** la sustentacion, asi que no cuentes con una clase posterior para aclarar dudas: si algo no sale, entrega lo que tengas con una nota de que fallo y por donde ibas. Un entregable con un problema documentado se califica; uno en blanco, no.

**¿Es legal ejecutar estos ataques? ¿Me puedo meter en problemas?**

Lo que haces aqui es ejecutarlos contra **tu propia** base de practica en ExamLab: es tuya, es desechable y se vuelve a sembrar en cada pregunta. Eso es igual que probar un candado en tu propia puerta. Lo que **no** puedes hacer —y esto no es una formalidad academica sino la ley— es probar la misma cadena contra un sistema que no es tuyo y sin autorizacion escrita, aunque «solo sea para ver si es vulnerable». El objetivo de la pregunta es el paso 5: demostrar que el agujero quedo cerrado. La evidencia que se califica es el **0 filas**, no el 8.

**Mi ataque devuelve 1 fila en vez de 8. ¿La funcion no es vulnerable?**

Lo es; lo que pasa es que la cadena no llego como querias. En SQL, para escribir una comilla simple dentro de una cadena hay que **duplicarla**, asi que el ataque se escribe `buscar_mascota_insegura('Firulais'' OR ''1''=''1')` —con dos comillas seguidas en cada sitio—. Si escribes una sola, o el motor se queja de sintaxis o la funcion recibe un nombre literal que no existe. Para verlo claro, sigue los dos niveles: la cadena **enviada** es `Firulais' OR '1'='1`, y el texto que la funcion acaba construyendo es `... WHERE nombre = 'Firulais' OR '1'='1'`.

**Escribi `buscar_mascota_directa` como dice el enunciado y me da «column reference “id_mascota” is ambiguous». ¿Esta mal el enunciado?**

El enunciado sugiere la idea correcta y le falta un detalle. Los nombres del `RETURNS TABLE (id_mascota INT, nombre TEXT, ...)` son **variables de PL/pgSQL**, asi que dentro de una consulta estatica `id_mascota` puede referirse a la columna o a la variable, y PostgreSQL no adivina: falla. Se arregla calificando las columnas con un alias de tabla —`SELECT m.id_mascota, m.nombre, m.especie, m.activa FROM mascota m WHERE m.nombre = p_nombre`—. Y fijate en algo interesante: la version con `EXECUTE` **no** tiene este problema, porque su cadena se entrega al motor sin sustitucion de variables. Es una diferencia real entre las dos formas y vale la pena entenderla en vez de volver al `EXECUTE` por miedo.

**Hice el `DELETE FROM cita;` y `cita` sigue con 10 filas, aunque `cita_borrada` tambien tiene 10. ¿Funciono?**

No, y este es el error mas enganoso del taller. Tu funcion de trigger termina en `RETURN NEW` —o no tiene `RETURN`—, y en un trigger de `DELETE` **`NEW` vale `NULL`**. Un trigger `BEFORE` que devuelve `NULL` **cancela la operacion**, asi que la fila se archivo y el borrado no ocurrio: mira el mensaje del motor, dice `DELETE 0`. Cambia la ultima linea por `RETURN OLD;`. Y aprovecha el susto, porque la leccion es de la clase: tu control no «evito el borrado», rompio el `DELETE`. Un control que impide la operacion legitima no es seguridad, es una averia.

**Si ya tengo el trigger que archiva, ¿para que la consulta de verificacion? Ya se que el dato esta ahi.**

Porque son controles de tipos distintos y ninguno hace el trabajo del otro. El trigger es **recuperacion**: no evita nada —el `DELETE` se ejecuta y `cita` queda en 0— y lo que consigue es que el dano sea reversible. La consulta es **verificacion**: no protege ningun dato, comprueba una afirmacion, y responde «¿la restauracion quedo completa?» con numeros comparables en vez de una impresion. El caso analizado tenia cinco copias y ninguna verificacion, y perdio datos igual. Fijate ademas en que la consulta pide `MIN` y `MAX` y no solo el conteo: un conteo correcto con un rango desplazado significa que restauraste otra cosa, y el conteo solo no te lo diria.

**¿El trigger me protege de cualquier perdida de citas?**

No, y conviene saber exactamente de que no protege. **No se dispara con `TRUNCATE cita;`**, porque un trigger `FOR EACH ROW` necesita recorrer filas y `TRUNCATE` no las recorre —eso se cierra con un trigger `BEFORE TRUNCATE ... FOR EACH STATEMENT`, y en la solucion esta—. No se dispara con `DROP TABLE`. No hace nada si alguien ejecuta `ALTER TABLE cita DISABLE TRIGGER trg_archivar_cita`. Y lo mas importante: `cita_borrada` y `respaldo_cita` viven en la **misma** base que `cita`, asi que si se pierde la instancia o el disco, se pierde todo junto. Protege contra un error logico, que es mucho, y no contra perder el servidor. Eso lo cubre un respaldo fisico externo, y es la mejora pendiente de la pregunta 5.

**¿Puedo elegir el caso B, el de rendimiento?**

Puedes, y conviene que sepas lo que te vas a encontrar: las preguntas 2 y 3 implementan mejoras del caso C —inyeccion— y del caso A —respaldo—, asi que en la pregunta 5, donde dos de las tres filas deben ser mejoras «ya implementadas», no tendras nada de tu propio caso. La salida limpia es citar el trabajo de la Clase 6 como tu mejora implementada de rendimiento: el `EXPLAIN` con `Seq Scan` y `Rows Removed by Filter`, el indice `idx_cita_vet_fecha` y el segundo `EXPLAIN` con `Index Cond`. Si prefieres que todo el taller cuente la misma historia, elige A o C.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: el **analisis del caso** con la causa raiz separada de la aparente y traducida a un objeto concreto de VetCare; el **contraste 8 → 0** con `buscar_mascota_segura` creada, probada en los dos sentidos y la funcion vulnerable eliminada; el **control de borrados completo** —bitacora con el conteo calculado, `cita_borrada`, `trg_archivar_cita`, el `DELETE` que deja 0 y 10, la restauracion con columnas explicitas y la fila `RESTAURACION OK`—; las **cuatro opciones correctas** de la pregunta 4; y la **tabla de tres mejoras** con dos `IMPLEMENTADA` que citan su prueba y una `PENDIENTE` con responsable y fecha anterior al 2026-11-16.
- Cuatro comprobaciones antes de entregar, todas de mirar un numero. Que el `COUNT` del ataque contra la funcion insegura sea **8** y contra la segura **0**, y que `buscar_mascota_segura('Firulais')` siga devolviendo **1** —si devuelve 0, cerraste el buscador, no el agujero—. Que despues del `DELETE` sea `cita` = **0** y `cita_borrada` = **10**; si las dos dan 10, tu trigger devuelve `NULL` y cancelo el borrado. Que la consulta de validacion devuelva **una sola fila** con el veredicto **calculado** por un `CASE` y no escrito a mano. Y que el `DROP FUNCTION` sea la ultima linea del script de la pregunta 2, porque si va antes ya no puedes demostrar el incidente.
- La clase deja dos ideas y las dos vienen del mismo sitio. La primera: **el control no es la copia, es la restauracion verificada.** Cinco respaldos que nadie probo no sumaron cinco oportunidades de recuperar; sumaron cinco razones para no probar ninguna, y la diferencia entre «tengo respaldo» y «puedo recuperar» costo seis horas de datos que no volvieron. La segunda es la que sale de la pregunta 2 y es mas incomoda, porque toca lo que ya creiamos resuelto: **una funcion de solo lectura tambien es una puerta.** La capa `api_*` de la Clase 12 blindo las escrituras, que son las que revisamos, y el agujero grave del proyecto estaba en una funcion que «solo consultaba» —y que entregaba la base completa, con los correos de los clientes, a quien escribiera una comilla en el buscador—. El **2026-11-09** es el Parcial 3 y el **2026-11-16** la sustentacion: de las tres mejoras de hoy, dos quedan cerradas y la unica pendiente es la misma que viene abierta desde la Clase 11. Ya no es un hallazgo: es una decision.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
