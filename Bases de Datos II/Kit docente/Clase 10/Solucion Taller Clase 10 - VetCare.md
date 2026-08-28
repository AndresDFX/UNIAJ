# Solucion del taller · Clase 10 · Control de concurrencia en VetCare

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** La linea de tiempo de la doble reserva con el intervalo exacto en que **las dos** transacciones leyeron `COUNT(*) = 0`, y la razon de fondo de por que ninguna validacion podia detectarlo —**no se puede bloquear una fila que todavia no existe**—; la reproduccion en SQL con las dos citas aceptadas, la deteccion encontrando la franja duplicada, el **indice unico parcial** cerrandola y la prueba de que no es excesiva porque la `CANCELADA` si entra; los dos mecanismos de stock —`UPDATE` condicional dando `true/false` y `FOR UPDATE` / `NOWAIT` / `SKIP LOCKED`— con la explicacion de por que en una sola sesion los tres se ven iguales; y el informe con el contrato de errores para la aplicacion y el limite del entorno declarado sin adornos.

> **Esta es una clase autonoma: no hay docente en vivo,** asi que el enunciado tiene que sostenerse solo y esta solucion se usa sobre todo para calificar y para responder por escrito. Conviene publicar un aviso el mismo dia con las tres cosas que mas se atascan y que estan resueltas aqui: que el `CREATE UNIQUE INDEX` de la pregunta 2 **falla** si no se borro antes el duplicado —y ese fallo es informacion, no un error—; que la pregunta 3 pide **dos** mecanismos y no dos versiones del mismo; y que en la pregunta 5 el punto 4 se califica por reconocer el limite, no por disimularlo. **El motor es PostgreSQL, no Oracle:** aqui aparecen `GET DIAGNOSTICS ... ROW_COUNT`, `FOR UPDATE SKIP LOCKED` y `EXCEPTION WHEN unique_violation`, que no tienen equivalente literal en Oracle. Y el aviso central del dia: ExamLab corre PostgreSQL compilado a WebAssembly con **una unica conexion**, asi que **ningun** bloqueo real, ninguna espera y ningun interbloqueo se pueden observar. Toda la clase esta disenada alrededor de eso: se demuestra lo que **si** es demostrable con una sesion —que la base **acepta** el dato invalido sin restriccion y lo **rechaza** con ella— y se declara por escrito lo que no.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 10 - Control de concurrencia/Taller PI - Clase 10 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 10/Taller en ExamLab - Clase 10 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Escenarios de concurrencia del PI documentados
- Entregable: Informe corto: 2 escenarios (cita doble / stock) + mitigacion
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Escenario de doble reserva con linea de tiempo T1/T2 | `abierta` | 25 |
| 2 | Reproducir la doble reserva y cerrarla con una restriccion | `bd_sql` | 25 |
| 3 | Doble descuento de stock: bloqueo explicito y actualizacion condicional | `bd_sql` | 20 |
| 4 | Niveles de aislamiento y anomalias en PostgreSQL | `cerrada_multi` | 10 |
| 5 | Informe de concurrencia del PI y limites de la verificacion | `abierta` | 20 |

---

## Pregunta 1 · Escenario de doble reserva con linea de tiempo T1/T2 · 25 pts

### Respuesta esperada

| Momento | Transaccion T1 (Recepcion A) | Transaccion T2 (Recepcion B) | Estado de la tabla `cita` | Comentario |
|---|---|---|---|---|
| **t0** | `BEGIN` | — | 0 citas para (vet 1, 2026-10-12 09:00) | A contesta el telefono: el dueno de Firulais quiere el lunes a las 9 |
| **t1** | — | `BEGIN` | 0 citas para esa franja | B contesta otra linea: la duena de Luna quiere **la misma** franja. Ninguna de las dos sabe de la otra |
| **t2** | `SELECT COUNT(*) ... = 0` **-> 0** | — | 0 citas para esa franja | A valida y **cree** que la franja esta libre. Es verdad: en este instante lo esta. **El `SELECT` no toma ningun bloqueo** |
| **t3** | — | `SELECT COUNT(*) ... = 0` **-> 0** | 0 citas para esa franja | **AQUI ESTA LA FALLA.** B valida y tambien lee **0**, porque A no ha insertado nada todavia. **Las dos leyeron 0 antes de que cualquiera escribiera:** este es el instante que hay que senalar |
| **t4** | `INSERT` (Firulais, vet 1, 09:00) | — | 1 fila (no confirmada por A) | A inserta. La fila existe pero **nadie fuera de A la ve**: la transaccion sigue abierta |
| **t5** | — | `INSERT` (Luna, vet 1, 09:00) | 2 filas (una por transaccion, ninguna visible a la otra) | B inserta. **Su validacion ya paso hace dos pasos y nadie la va a repetir.** Sin restriccion en la tabla, no hay nada que se oponga |
| **t6** | `COMMIT` | — | 1 fila confirmada | A confirma. La franja ya esta ocupada de verdad |
| **t7** | — | `COMMIT` | **2 filas confirmadas en la misma franja** | B confirma. La base acepta el dato invalido **sin un solo error**: nadie le pidio que lo impidiera. Laura Restrepo tiene dos pacientes a las 9:00 |

El intervalo critico es **t2–t5**: entre la primera lectura y la ultima escritura, las dos transacciones sostienen una creencia —«la franja esta libre»— que era cierta cuando la formaron y falsa cuando actuaron sobre ella. Vale la pena decirlo asi porque describe **toda** la familia de problemas de concurrencia: no hay un dato mal leido en ninguna parte; hay una decision tomada sobre una foto que envejecio.

**1. Nombre de la anomalia y por que `READ COMMITTED` no la evita.** Es un **write skew sobre un predicado**, y en la forma concreta en que aparece aqui —dos transacciones que consultan un predicado y despues **insertan** filas que lo cambian— se le llama tambien **lectura fantasma** (*phantom*): la fila de la otra transaccion es un fantasma que no estaba cuando cada una miro. `READ COMMITTED` **no** lo evita, y no por descuido, sino porque hace exactamente lo que promete y nada mas:

- Garantiza que cada sentencia vea una foto de lo **confirmado** en el instante en que esa sentencia empieza. En t3 el `INSERT` de A todavia no existe (t4) y, aunque existiera, no estaria confirmado hasta t6. B lee **0** y esa lectura es **correcta**. No hay lectura sucia, no hay lectura mal hecha: hay una lectura veraz que caduco.
- **Y la razon de fondo, que es la que hay que entender: un `SELECT COUNT(*)` no bloquea nada, y no puede.** Un bloqueo se pone sobre **filas que existen**, y aqui el conflicto lo produce una fila que **todavia no existe** en ninguna de las dos transacciones. Ni siquiera un `SELECT ... FOR UPDATE` sobre el resultado del `COUNT(*)` ayudaria: no hay ninguna fila que bloquear. Por eso la unica salida es **desplazar el candado a otro objeto** —una fila que si exista, como la del veterinario; una estructura fisica, como el B-tree de un indice unico; o un bloqueo de predicado, que es lo que hace `SERIALIZABLE`—.

> La frase corta: **el problema no es que se lea mal, es que se decide sobre algo que no se puede bloquear porque no existe.**

**2. Que pasaria en el negocio.** No es un problema estetico:

- **Para la clinica:** dos duenos con confirmacion escrita de la misma hora, y quien lo descubre es la recepcionista del turno de la manana, delante de los dos. La respuesta invariable es dar por buena la primera y reagendar la segunda «por un error del sistema», que es la version publica de «nadie puso una restriccion».
- **Para la veterinaria:** una consulta de 30 minutos se convierte en dos de 15, o en 60 minutos que desbordan la agenda del resto del dia. Si la agenda estaba completa, el retraso se arrastra hasta la ultima cita.
- **Para los duenos:** uno espera con su mascota estresada en la sala, y el otro se lleva la impresion de que su reserva no vale nada. En una clinica chica esa impresion se paga en la siguiente vacunacion.
- **Y el dano invisible:** el reporte de ocupacion queda inflado. La franja de las 9:00 aparece con dos citas, y cualquier decision que se tome sobre ese dato —contratar, ampliar horario, medir productividad— parte de un numero falso.

**3. Tres mitigaciones, de la mas fuerte a la mas debil.** El orden no es de gusto: es por **quien queda a cargo de que la regla se cumpla**.

| # | Mitigacion | Que garantiza | Que cuesta | Que hace la aplicacion cuando la base rechaza |
|---|---|---|---|---|
| **(a)** | **Indice unico parcial** `CREATE UNIQUE INDEX uq_cita_vet_franja ON cita (id_veterinario, fecha_hora) WHERE estado <> 'CANCELADA';` | **La garantia mas fuerte que existe: no hay forma de que el dato invalido entre.** No depende del orden, ni de la velocidad, ni de que el procedimiento este bien escrito, ni de que manana alguien haga un `INSERT` a mano. Funciona **precisamente porque** las transacciones son simultaneas: la segunda que intenta escribir la misma clave **espera** en el B-tree del indice y, cuando la primera confirma, recibe el error | Un indice mas que mantener en cada `INSERT` y `UPDATE` de `cita` —costo real pero minimo—, y hay que decidir la condicion parcial con cuidado: sin el `WHERE estado <> 'CANCELADA'`, una franja liberada por una cancelacion no se podria volver a usar nunca | Captura `unique_violation` (SQLSTATE **23505**) y **no** la muestra en crudo. Traduce: «esa franja se acaba de ocupar», recarga la agenda del dia y ofrece las franjas libres mas cercanas. **No reintenta el mismo `INSERT`:** volveria a fallar |
| **(b)** | **`SELECT ... FOR UPDATE` sobre una fila que si exista** —la del veterinario— antes de validar: `SELECT 1 FROM veterinario WHERE id_veterinario = 1 FOR UPDATE;` y luego el `COUNT(*)` y el `INSERT` | Serializa a todas las transacciones que agenden con **ese** veterinario: la segunda espera y, cuando entra, su `COUNT(*)` ya ve la cita de la primera y se detiene sola. Es una garantia **fuerte pero condicionada**: solo protege a quien recuerde pedir el candado | **Es el que cuesta mas.** Reduce la concurrencia a una reserva a la vez por veterinario, y una transaccion lenta hace esperar a todas las demas. Y si dos operaciones bloquean varias filas en orden distinto, aparece el **interbloqueo**. Sobre todo: **es una convencion, no una garantia** —un `INSERT` que se olvide del `FOR UPDATE` pasa por encima— | Recibe una espera, no un error: la operacion simplemente tarda. Si el `COUNT(*)` posterior encuentra la franja ocupada, es la propia aplicacion la que decide y mensaje: «franja ocupada, elige otra». Con `NOWAIT` recibiria **55P03** y podria decir «intentalo de nuevo en un momento» |
| **(c)** | **`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE`** con reintento en la aplicacion | La garantia teorica mas limpia: PostgreSQL vigila los **predicados** leidos —no solo las filas— y, si el resultado final no equivale a haber ejecutado las transacciones una tras otra, **aborta una de las dos**. Es la unica de las tres que resuelve el fantasma *sin* que haya que anticipar la regla ni nombrar la columna | Costo de seguimiento en el servidor, y sobre todo **obliga a que toda la aplicacion sepa reintentar**. El error llega **al confirmar**, no al escribir, asi que hay que poder repetir la operacion completa. Un solo camino de codigo sin reintento convierte la garantia en errores intermitentes para el usuario | Captura `serialization_failure` (SQLSTATE **40001**) y **reintenta la transaccion entera** —de forma automatica, con un tope de 3 intentos y una espera creciente—. Solo si agota los intentos muestra un mensaje. Es el unico caso de los tres en que reintentar **es** la respuesta correcta |

**Recomendacion para VetCare: (a), y ademas.** La (a) es la que se implementa en la pregunta 2 porque es **estructural**: sigue funcionando cuando alguien reescriba `sp_agendar_cita`, cuando entre un `INSERT` desde un script de carga o cuando el proximo semestre llegue otro programador. La (b) y la (c) protegen **codigo**; la (a) protege **datos**. Las tres no son alternativas excluyentes: lo razonable es (a) como red de la que no se puede escapar, y la aplicacion traduciendo el `23505` a un mensaje util.

### Como calificar

- **10 pts — la linea de tiempo, con al menos 6 pasos y las cinco columnas pedidas.** 4 pts la estructura y que los pasos esten intercalados de verdad —T1 y T2 alternandose, no primero toda T1 y despues toda T2—; **6 pts que quede senalado con precision el intervalo en que las dos leyeron `COUNT(*) = 0` antes de que cualquiera insertara**. La rubrica lo dice explicitamente: **se descuenta si la narrativa no distingue el instante de la lectura del de la escritura.** Una tabla donde T1 lee, inserta y confirma antes de que T2 lea no describe el problema: describe el caso que funciona bien.
- **5 pts — el nombre de la anomalia y por que `READ COMMITTED` no la evita.** 2 pts el nombre: se acepta **lectura fantasma**, **phantom**, **write skew sobre un predicado** o cualquiera de las dos con la otra como sinonimo. 3 pts la explicacion, y aqui hay dos niveles: decir que «cada sentencia ve una foto nueva de lo confirmado» vale 2 de 3; **llegar a que un `SELECT COUNT(*)` no bloquea nada porque la fila del conflicto todavia no existe** vale los 3 y es la comprension real del problema.
- **3 pts — el impacto en el negocio,** repartido entre clinica, veterinaria y los dos duenos. Se piden efectos concretos y no adjetivos: «dos duenos a la misma hora y una agenda que se corre el resto del dia» vale; «afecta la calidad del servicio» no. Se reconoce como sobresaliente quien note el dano invisible —el reporte de ocupacion queda inflado y las decisiones que salgan de ahi parten de un numero falso—.
- **7 pts — las tres mitigaciones, aproximadamente 2,3 pts cada una,** y cada una vale por sus **tres** partes: que garantiza, que cuesta y que hace la aplicacion cuando la base rechaza. La tercera parte es la que casi siempre falta y es la que la rubrica nombra: sin ella, la mitigacion es un buen deseo sin contrato.
- **Se reconoce como sobresaliente, sin puntos extra:** notar que reintentar es la respuesta correcta **solo** con `SERIALIZABLE` —el `40001` es reintentable y el `23505` no lo es, porque el segundo `INSERT` volveria a fallar siempre—; o senalar que la (b) y la (c) protegen **codigo** mientras la (a) protege **datos**, y que por eso la (a) sobrevive a que alguien reescriba el procedimiento.
- **Extension:** la tabla mas una pagina. No se premia la longitud. Si la linea de tiempo esta bien y las tres mitigaciones traen sus tres partes, la pregunta esta completa en menos de lo que la mayoria escribe.

### Errores frecuentes y que hacer

- **La linea de tiempo secuencial en vez de intercalada:** T1 valida, inserta y confirma; despues T2 valida, ve 1 y se detiene. Es el error dominante y delata que no se entendio el problema, porque esa secuencia **funciona correctamente**: es lo que pasa cuando no hay concurrencia. El defecto solo existe si las dos lecturas caen **antes** de la primera escritura.
- **Decir que `READ COMMITTED` «lee datos sucios» o que «lee mal».** Es al contrario: PostgreSQL **nunca** permite lecturas sucias, en ningun nivel. Aqui las dos lecturas son veraces. Confundir esto lleva directo a marcar mal la opcion de `READ UNCOMMITTED` en la pregunta 4.
- **Proponer «poner el `SELECT` y el `INSERT` mas cerca» o «hacer la transaccion mas rapida» como mitigacion.** Reducir la ventana **no** es cerrarla: con dos recepcionistas y una ventana de 5 milisegundos, el problema pasa de diario a mensual, y un problema mensual de agenda es peor que uno diario porque nadie lo relaciona con el software.
- **Afirmar que un `SELECT ... FOR UPDATE` sobre `cita` resolveria el problema.** No hay nada que bloquear: la fila en conflicto **no existe** todavia. Si se elige la via (b), el candado tiene que ir sobre una fila que si exista —la del veterinario— y usarla como representante de la franja. Quien no vea esta distincion tampoco va a poder justificar por que la (a) funciona.
- **Presentar las tres mitigaciones sin decir que hace la aplicacion.** «Se crea un `UNIQUE` y listo» deja al usuario final viendo `duplicate key value violates unique constraint "uq_cita_vet_franja"` en pantalla. La restriccion es la mitad del trabajo; la otra mitad es traducirla a «esa franja se acaba de ocupar, aqui tienes las tres mas cercanas».
- **Ordenar las mitigaciones al azar** o justificar el orden por dificultad de implementacion. El enunciado pide **de la mas fuerte a la mas debil**, y fuerte significa **de quien no se puede escapar**: la restriccion no depende de nadie, el `FOR UPDATE` depende de que todo el mundo lo pida, y el `SERIALIZABLE` depende de que toda la aplicacion sepa reintentar.

---

## Pregunta 2 · Reproducir la doble reserva y cerrarla con una restriccion · 25 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- PASO 1. MOSTRAR EL PROBLEMA.
-- Las dos citas del escenario de la pregunta 1: mismo veterinario, misma
-- franja, dos mascotas distintas. La tabla NO tiene ninguna restriccion
-- de unicidad de franja, asi que las dos entran sin un solo error.
-- Esto no es un fallo del motor: es que nadie le pidio que lo impidiera.
-- ======================================================================
INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado) VALUES
  (1, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA'),   -- Firulais, Recepcion A
  (2, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');   -- Luna, Recepcion B

INSERT INTO evidencia (paso, resultado) VALUES
  ('sin restriccion',
   'PROBLEMA: las dos citas se insertaron sin error. La franja del veterinario 1 '
   'el 2026-10-12 09:00 quedo con 2 citas PROGRAMADA.');

-- ======================================================================
-- PASO 2. EVIDENCIAR EL DATO INVALIDO.
-- Esta consulta es la que hay que dejar escrita en el proyecto: es la que
-- responde "¿tengo el problema hoy?" sin depender de que alguien se
-- acuerde de revisar. Devuelve exactamente la franja duplicada.
-- ======================================================================
SELECT id_veterinario,
       fecha_hora,
       COUNT(*) AS citas_en_la_misma_franja
  FROM cita
 WHERE estado <> 'CANCELADA'
 GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- ======================================================================
-- PASO 3. LIMPIAR EL DUPLICADO.
-- Se borra la de mayor id_cita, es decir la que llego despues. Y se
-- escribe con una subconsulta en vez de un id fijo, porque el id
-- depende de cuantas veces se haya corrido el script.
--
-- OJO, y esto es lo que mas confunde en esta pregunta: si se salta este
-- paso, el CREATE UNIQUE INDEX del paso 4 FALLA con
--   ERROR: could not create unique index "uq_cita_vet_franja"
--   DETALLE: Key (id_veterinario, fecha_hora)=(1, 2026-10-12 09:00:00) is duplicated.
-- Eso no es un error del ejercicio: es la base diciendo "no puedo
-- prometerte una regla que tus datos actuales ya rompen". Una restriccion
-- se puede crear solo si lo que ya hay la cumple.
-- ======================================================================
DELETE FROM cita
 WHERE id_cita = (
   SELECT MAX(id_cita)
     FROM cita
    WHERE id_veterinario = 1
      AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
      AND estado <> 'CANCELADA');

-- ======================================================================
-- PASO 4. APLICAR LA MITIGACION.
-- Indice unico PARCIAL. El WHERE es lo importante: las citas CANCELADAS
-- SI pueden repetir franja, porque una cancelacion libera la hora y esa
-- hora tiene que poder volver a venderse. Un UNIQUE total sobre
-- (id_veterinario, fecha_hora) dejaria una franja quemada para siempre
-- cada vez que alguien cancelara.
--
-- Y aqui esta el mecanismo que responde a la pregunta 4 de este taller:
-- la restriccion no funciona "si las transacciones van una despues de
-- otra". Funciona PRECISAMENTE cuando son simultaneas, porque la segunda
-- que intenta escribir la misma clave se queda ESPERANDO en el B-tree del
-- indice hasta que la primera confirme, y entonces recibe el error. Es un
-- punto de serializacion fisico, no una convencion.
-- ======================================================================
CREATE UNIQUE INDEX uq_cita_vet_franja
    ON cita (id_veterinario, fecha_hora)
 WHERE estado <> 'CANCELADA';

-- ======================================================================
-- PASO 5. PROBAR QUE AHORA LA BASE RECHAZA EL CONFLICTO.
-- El DO con EXCEPTION captura el error para que el script no se detenga.
-- Se captura unique_violation y no OTHERS a proposito: si el INSERT
-- fallara por otra razon -- una FK, un CHECK -- queremos que el script
-- muera y nos lo diga, no anotar "OK rechazada" por el motivo equivocado.
-- ======================================================================
DO $$
BEGIN
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (4, 1, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');
  INSERT INTO evidencia (paso, resultado)
  VALUES ('con restriccion', 'FALLO: se permitio la doble reserva');
EXCEPTION WHEN unique_violation THEN
  INSERT INTO evidencia (paso, resultado)
  VALUES ('con restriccion', 'OK rechazada: ' || SQLERRM);
END $$;

-- ======================================================================
-- PASO 6. PROBAR QUE LA RESTRICCION NO ES EXCESIVA.
-- La misma franja, pero CANCELADA. TIENE que entrar: el indice parcial no
-- la vigila. Esta prueba es la que distingue una restriccion bien pensada
-- de una que simplemente prohibe cosas: sirve para demostrar que no se
-- rompio el caso legitimo.
-- ======================================================================
DO $$
BEGIN
  INSERT INTO cita (id_mascota, id_veterinario, fecha_hora, estado)
  VALUES (5, 1, TIMESTAMP '2026-10-12 09:00:00', 'CANCELADA');
  INSERT INTO evidencia (paso, resultado)
  VALUES ('cancelada en la misma franja',
          'OK aceptada: el indice parcial no aplica a CANCELADA, la franja liberada se puede reusar');
EXCEPTION WHEN unique_violation THEN
  INSERT INTO evidencia (paso, resultado)
  VALUES ('cancelada en la misma franja',
          'FALLO: la restriccion es excesiva, bloqueo una cita CANCELADA');
END $$;

-- ======================================================================
-- PASO 7. CIERRE.
-- ======================================================================
SELECT paso, resultado FROM evidencia ORDER BY id_evidencia;

-- La MISMA consulta de deteccion del paso 2, sin cambiarle una coma.
-- Ahora tiene que devolver CERO filas.
SELECT id_veterinario,
       fecha_hora,
       COUNT(*) AS citas_en_la_misma_franja
  FROM cita
 WHERE estado <> 'CANCELADA'
 GROUP BY id_veterinario, fecha_hora
HAVING COUNT(*) > 1;

-- Comprobacion de una linea, la que conviene pegar al calificar.
SELECT (SELECT COUNT(*) FROM cita
          WHERE id_veterinario = 1
            AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
            AND estado <> 'CANCELADA')                    AS programadas_debe_ser_1,
       (SELECT COUNT(*) FROM cita
          WHERE id_veterinario = 1
            AND fecha_hora = TIMESTAMP '2026-10-12 09:00:00'
            AND estado = 'CANCELADA')                     AS canceladas_debe_ser_1,
       (SELECT COUNT(*) FROM evidencia)                   AS pasos_registrados_debe_ser_3,
       (SELECT COUNT(*) FROM pg_indexes
          WHERE tablename = 'cita'
            AND indexname = 'uq_cita_vet_franja')         AS indice_creado_debe_ser_1;
```

### Salida esperada

```
PASO 2 -- la deteccion encuentra el problema: 1 fila

 id_veterinario |     fecha_hora      | citas_en_la_misma_franja
----------------+---------------------+--------------------------
              1 | 2026-10-12 09:00:00 |                        2

Una sola fila, y es la unica: las 10 citas sembradas no repiten ninguna franja, asi
que todo lo que aparece aqui lo produjo el paso 1.

PASO 3 -- DELETE 1

PASO 4 -- CREATE INDEX

Si aqui sale un error en vez de CREATE INDEX, falto el paso 3. El mensaje exacto es:

  ERROR:  could not create unique index "uq_cita_vet_franja"
  DETAIL:  Key (id_veterinario, fecha_hora)=(1, 2026-10-12 09:00:00) is duplicated.

Vale la pena provocarlo a proposito una vez: es la base explicando que una
restriccion solo se puede crear si los datos que ya existen la cumplen.

PASO 5 y PASO 6 -- los dos bloques terminan en DO, sin ERROR

PASO 7 -- evidencia: 3 filas

              paso              |                          resultado
--------------------------------+-------------------------------------------------------------
 sin restriccion                | PROBLEMA: las dos citas se insertaron sin error. La franja
                                | del veterinario 1 el 2026-10-12 09:00 quedo con 2 citas
                                | PROGRAMADA.
 con restriccion                | OK rechazada: duplicate key value violates unique constraint
                                | "uq_cita_vet_franja"
 cancelada en la misma franja    | OK aceptada: el indice parcial no aplica a CANCELADA, la
                                | franja liberada se puede reusar

El texto del paso 1 y del paso 3 lo escribe cada estudiante y no se califica palabra
por palabra. Lo que SI se califica es que el segundo diga "rechazada" y traiga el
SQLERRM, y que el tercero diga "aceptada". Si el tercero dice FALLO, el indice se
creo sin la condicion parcial.

Deteccion final -- 0 filas

(0 rows)

Comprobacion -- 1 fila

 programadas_debe_ser_1 | canceladas_debe_ser_1 | pasos_registrados_debe_ser_3 | indice_creado_debe_ser_1
------------------------+-----------------------+------------------------------+--------------------------
                      1 |                     1 |                            3 |                        1

Los cuatro numeros son 1, 1, 3 y 1, y resumen la pregunta completa: queda UNA cita
programada en la franja disputada -- no dos y no cero --, entro UNA cancelada en la
misma franja -- prueba de que la restriccion no es excesiva --, se registraron los
TRES pasos y el indice existe.

Estado final de la tabla cita: 12 filas. Las 10 sembradas, mas la cita 11
(PROGRAMADA, la que gano la franja) y la cita 14 (CANCELADA). Los ids 12 y 13 no
estan: el 12 lo consumio la cita duplicada que se borro en el paso 3, y el 13 lo
consumio el INSERT rechazado del paso 5. Las secuencias no vuelven atras ni con un
DELETE ni con un ROLLBACK, y por eso en cualquier base real hay huecos en los ids.
```

### Como calificar

- **6 pts — el problema demostrado primero.** 3 pts que los dos `INSERT` se ejecuten **sin error** y quede registrado en `evidencia`, y 3 pts que la consulta de deteccion devuelva **la franja duplicada con `COUNT(*) = 2`**. El orden importa y la rubrica lo dice: **se demuestra primero que sin restriccion la doble reserva entra**. Quien cree el indice antes de reproducir el problema pierde estos 6 pts aunque el resto quede perfecto, porque ya no puede demostrar que habia algo que arreglar.
- **7 pts — el indice unico PARCIAL, bien escrito.** 3 pts que sea `UNIQUE` sobre `(id_veterinario, fecha_hora)`, y **4 pts la condicion `WHERE estado <> 'CANCELADA'`**. Un `UNIQUE` total —sin `WHERE`— vale 3 de 7 y hay que explicar en la devolucion que rompe el caso legitimo: dejaria una franja quemada para siempre cada vez que alguien cancelara. Se acepta `ALTER TABLE ... ADD CONSTRAINT ... UNIQUE` **solo** si se argumenta el cambio, porque una `CONSTRAINT UNIQUE` **no** admite condicion parcial y por eso el enunciado pide un indice.
- **5 pts — el rechazo capturado.** 3 pts que el segundo `INSERT` sea rechazado y 2 pts que quede en `evidencia` como `unique_violation` con el `SQLERRM`. Se reconoce como mejor solucion capturar `WHEN unique_violation` en lugar de `WHEN OTHERS`: con `OTHERS`, un fallo por otra causa —una FK, un `CHECK`— se registraria como «OK rechazada» y la evidencia mentiria.
- **4 pts — la prueba de que la restriccion no es excesiva:** el `INSERT` con estado `'CANCELADA'` en la misma franja **si** entra, y queda registrado. Es el punto que distingue una restriccion pensada de una que solo prohibe cosas, y es la unica prueba de que el `WHERE` del indice hace lo que se dice que hace. Quien haya puesto un `UNIQUE` total va a ver esta insercion **fallar** y eso mismo le muestra el error.
- **3 pts — el cierre completo:** `SELECT` de `evidencia` con los **3** pasos y la consulta de deteccion devolviendo **cero filas**, con la misma consulta del paso 2 sin cambiar una coma. 1 pt adicional dentro de estos 3 si el script **no aborta** en ningun punto, que es requisito explicito de la rubrica.
- **Se reconoce como sobresaliente, sin puntos extra:** haber provocado a proposito el fallo del `CREATE UNIQUE INDEX` sin limpiar antes y haberlo dejado documentado en un comentario; explicar por que la restriccion funciona **precisamente** cuando las transacciones son simultaneas —la segunda espera en el B-tree del indice y recibe el error al confirmar la primera—; o notar los huecos en los ids y por que existen.

### Errores frecuentes y que hacer

- **Crear el indice antes de reproducir el problema.** Es el error de procedimiento mas costoso: los dos `INSERT` del paso 1 fallan, la consulta de deteccion no encuentra nada y la pregunta se queda sin su mitad demostrativa. El taller no pide implementar la restriccion: pide **demostrar que hacia falta** y despues que funciona.
- **El `UNIQUE` total, sin la condicion parcial.** Es el error conceptual central. Funciona para el caso de la doble reserva y rompe el caso legitimo: con un `UNIQUE` sobre `(id_veterinario, fecha_hora)` a secas, cada cita cancelada deja su franja **inutilizable para siempre**. El paso 6 esta puesto justo para que este error se vea, no para que se explique.
- **Olvidar el `DELETE` del paso 3** y quedarse trabado en el error del `CREATE UNIQUE INDEX`. Suele terminar en un mensaje de «no me deja crear el indice». No es un problema de la plataforma: **una restriccion solo se puede crear si los datos que ya existen la cumplen**, y esa es una de las cosas utiles que se aprenden en esta pregunta.
- **Capturar `WHEN OTHERS` y anotar «OK rechazada» sin mirar el error.** La evidencia queda diciendo que la restriccion funciono cuando en realidad pudo haber fallado la FK de `id_mascota` o el `CHECK` de `estado`. Capturar `unique_violation` no es purismo: es la diferencia entre una prueba y una suposicion.
- **Cambiar la consulta de deteccion en el paso 7** —quitarle el `WHERE estado <> 'CANCELADA'`, agrupar por otra cosa—. Entonces el «cero filas» no prueba nada, porque no es la misma pregunta que devolvio una fila en el paso 2. Y si se le quita el filtro de estado, **vuelve a devolver una fila** por la cita cancelada del paso 6, que es correcta.
- **Concluir que «la restriccion resuelve la concurrencia» y dejarlo ahi.** Resuelve la **integridad**: garantiza que el dato invalido no entre nunca. Lo que sigue faltando es el otro lado del contrato: que la aplicacion capture el `23505`, no lo muestre en crudo y ofrezca otra franja. Eso se pide en la pregunta 5 y conviene senalarlo aqui para que llegue advertido.

---

## Pregunta 3 · Doble descuento de stock: bloqueo explicito y actualizacion condicional · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- ======================================================================
-- PARTE A - ACTUALIZACION CONDICIONAL (sin bloqueo explicito)
-- ======================================================================
CREATE OR REPLACE FUNCTION fn_tomar_stock(p_id_insumo INT, p_cantidad INT)
RETURNS BOOLEAN
LANGUAGE plpgsql
AS $fn$
DECLARE
  v_filas INT;
BEGIN
  -- Comprobar y descontar en UNA sola sentencia. La condicion del stock
  -- va en el WHERE, no en un IF previo: asi no existe ningun instante
  -- entre el "hay stock" y el "lo descuento" en el que otra sesion pueda
  -- meterse. Si no alcanza, el UPDATE no encuentra fila que cumpla la
  -- condicion y afecta 0 filas -- no falla, simplemente no hace nada.
  UPDATE insumo
     SET stock = stock - p_cantidad
   WHERE id_insumo = p_id_insumo
     AND stock >= p_cantidad;

  GET DIAGNOSTICS v_filas = ROW_COUNT;
  RETURN v_filas = 1;
END;
$fn$;

-- Las dos auxiliares pidiendo lo mismo, una detras de la otra. La primera
-- se lleva las 3 unidades; la segunda se queda sin nada, pero el stock no
-- baja de 0 en ningun momento.
SELECT fn_tomar_stock(2, 3) AS primera,
       fn_tomar_stock(2, 3) AS segunda;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 5);

-- ======================================================================
-- PARTE B - BLOQUEO EXPLICITO DE FILA
--
-- Bloque 1: FOR UPDATE. El SELECT toma la fila del insumo 5 y no la
-- suelta hasta que termine la transaccion. Cualquier otra sesion que
-- quiera esa misma fila para escribirla ESPERA.
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE;                       -- <-- toma el candado de la fila

  IF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'FOR UPDATE: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'FOR UPDATE: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
END $$;

-- ======================================================================
-- Bloque 2: FOR UPDATE NOWAIT. Identico, salvo el candado: si la fila
-- estuviera tomada por otra sesion, en vez de esperar falla en el acto
-- con lock_not_available (SQLSTATE 55P03). Se captura para poder
-- distinguir en la evidencia "no habia stock" de "no pude ni mirar".
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE NOWAIT;                -- <-- o muerte

  IF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'NOWAIT: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'NOWAIT: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
EXCEPTION WHEN lock_not_available THEN
  RAISE NOTICE 'NOWAIT: la fila estaba tomada por otra sesion, no espero. %', SQLERRM;
END $$;

-- ======================================================================
-- Bloque 3 (opcional pero muy ilustrativo): FOR UPDATE SKIP LOCKED.
-- No espera y no falla: SALTA la fila bloqueada, asi que el SELECT
-- devuelve CERO filas y v_stock se queda en NULL. Hay que detectarlo con
-- IF NOT FOUND, porque "IF NULL >= 4" no es falso: es NULL, y el IF no
-- entra por ninguna rama. Es el error silencioso de este mecanismo.
-- ======================================================================
DO $$
DECLARE
  v_stock INT;
BEGIN
  SELECT stock INTO v_stock
    FROM insumo
   WHERE id_insumo = 5
     FOR UPDATE SKIP LOCKED;

  IF NOT FOUND THEN
    RAISE NOTICE 'SKIP LOCKED: la fila estaba tomada, la salte. No hice nada.';
  ELSIF v_stock >= 4 THEN
    UPDATE insumo SET stock = stock - 4 WHERE id_insumo = 5;
    RAISE NOTICE 'SKIP LOCKED: habia % gasas, descuento 4, quedan %', v_stock, v_stock - 4;
  ELSE
    RAISE NOTICE 'SKIP LOCKED: solo habia % gasas, no alcanza para 4', v_stock;
  END IF;
END $$;

SELECT id_insumo, nombre, stock FROM insumo WHERE id_insumo IN (2, 5);

-- ======================================================================
-- LAS TRES VARIANTES DEL CANDADO, EN UNA LINEA CADA UNA
--
--   FOR UPDATE             -> ESPERA a que la otra sesion suelte la fila.
--                             La operacion tarda mas, pero se hace.
--   FOR UPDATE NOWAIT      -> NO espera: falla en el acto con 55P03
--                             (lock_not_available). Sirve cuando es mejor
--                             decirle al usuario "intentalo otra vez" que
--                             dejarlo mirando un reloj de arena.
--   FOR UPDATE SKIP LOCKED -> NO espera y NO falla: devuelve las filas que
--                             puede y SALTA las tomadas. Es el mecanismo
--                             de las colas de trabajo: diez procesos leen
--                             la misma tabla y cada uno se lleva tareas
--                             distintas sin pisarse. Para descontar stock
--                             de un insumo concreto es peligroso, porque
--                             "no pude" se disfraza de "no hay".
--
-- POR QUE AQUI LOS TRES SE COMPORTAN IGUAL
-- Porque en esta sesion unica nadie mas tiene la fila tomada. El candado
-- se concede siempre de inmediato, asi que no hay nada que esperar, nada
-- que fallar y nada que saltar: los tres bloques descuentan igual. Los
-- tres NOTICE que se ven arriba no prueban que los tres mecanismos sean
-- equivalentes; prueban que el escenario que los diferencia NO SE PUEDE
-- MONTAR aqui.
--
-- QUE VERIAMOS EN UN SERVIDOR REAL, con dos sesiones de psql: la sesion A
-- abre BEGIN, hace SELECT ... FOR UPDATE del insumo 5 y NO confirma. Con
-- FOR UPDATE, la sesion B se queda colgada -- visible en pg_locks con
-- granted = false y en pg_stat_activity con wait_event_type = 'Lock' --
-- hasta que A haga COMMIT o ROLLBACK. Con NOWAIT, B falla al instante con
-- 55P03. Con SKIP LOCKED, B recibe 0 filas y sigue de largo.
--
-- CUAL ELIJO PARA VETCARE: el A, la actualizacion condicional, y no es
-- por comodidad. El A resuelve la comprobacion y la escritura en UNA sola
-- sentencia atomica, asi que no hay ventana ni convencion que recordar:
-- funciona aunque manana alguien escriba un procedimiento nuevo. El B
-- deja el candado tomado durante todo lo que la transaccion tarde en
-- pensar, y solo protege a quien se acuerde de pedirlo.
-- El B es NECESARIO -- y ahi si no hay alternativa -- cuando hay que
-- LEER, CALCULAR con datos de varias tablas y DESPUES escribir, porque el
-- calculo no cabe en el WHERE de un UPDATE. En VetCare ese caso existe:
-- el reporte de cierre de caja que suma detalle_factura, compara contra
-- el total de factura y ajusta. Ahi el A no sirve.
-- ======================================================================
```

### Salida esperada

```
PARTE A -- 1 fila

 primera | segunda
---------+---------
 t       | f

La primera auxiliar se lleva las 3 unidades; la segunda recibe false. Nadie queda
en negativo y nadie tuvo que coordinarse con nadie.

Un detalle honesto sobre esta prueba: el orden en que PostgreSQL evalua las dos
funciones de la lista de columnas NO esta garantizado por el estandar. En la
practica se evalua de izquierda a derecha y se ve t | f. Si alguna vez se viera
f | t, la conclusion seria exactamente la misma -- el par siempre es {true,
false} -- y lo que no se puede es construir una prueba que dependa de cual de las
dos columnas trae el true.

 id_insumo |        nombre        | stock
-----------+----------------------+-------
         2 | Vacuna triple felina |     0     <-- 3 - 3, exactamente en el limite
         5 | Gasa esteril         |     8     <-- todavia sin tocar

PARTE B -- los NOTICE de los tres bloques

NOTICE:  FOR UPDATE: habia 8 gasas, descuento 4, quedan 4
NOTICE:  NOWAIT: habia 4 gasas, descuento 4, quedan 0
NOTICE:  SKIP LOCKED: solo habia 0 gasas, no alcanza para 4

Los tres bloques obtuvieron el candado de inmediato, porque no habia nadie mas.
El insumo 5 baja 8 -> 4 -> 0, y el tercer bloque ya no alcanza: entra por la rama
del ELSE, que es exactamente la que hay que tener escrita. Si el tercer bloque se
escribio sin la validacion del IF, el UPDATE tampoco habria hecho dano -- el
CHECK (stock >= 0) lo habria abortado --, pero el mensaje habria sido un error en
vez de una explicacion.

Ninguno de los tres NOTICE dice nada sobre esperas ni sobre candados negados, y
eso es el resultado que hay que reportar: el escenario que diferencia a los tres
mecanismos NO se puede montar con una sola sesion.

 id_insumo |        nombre        | stock
-----------+----------------------+-------
         2 | Vacuna triple felina |     0
         5 | Gasa esteril         |     0

Estado final: los dos insumos en 0 y ninguno negativo. Los numeros de la pregunta
son true/false en la parte A, el insumo 2 en 0, y la secuencia 8 -> 4 -> 0 del
insumo 5 en la parte B.

Nota para calificar la parte B: el enunciado pide "otro bloque identico" con NOWAIT
o SKIP LOCKED, asi que dos bloques bastan y el tercero es voluntario. Si el
estudiante entrego solo dos, los NOTICE esperados son 8 -> 4 y 4 -> 0, y el insumo
5 termina igual en 0.
```

### Como calificar

- **6 pts — `fn_tomar_stock` con el `UPDATE` condicional y su prueba.** 3 pts la funcion: condicion del stock en el `WHERE`, `GET DIAGNOSTICS v_filas = ROW_COUNT` y `RETURN v_filas = 1`. 3 pts que la prueba arroje **`true` y luego `false`**, el insumo 2 quede en **0** y no haya negativos. Un `SELECT stock INTO` seguido de un `IF` vale 0 de los 3 primeros, aunque el resultado sea correcto: es el patron que toda la clase esta desmontando.
- **6 pts — los bloques `DO` con bloqueo explicito.** 3 pts el `SELECT stock INTO v_stock ... FOR UPDATE` seguido de la validacion y el `UPDATE`, con su `RAISE NOTICE`; 3 pts el segundo bloque con **`NOWAIT` o `SKIP LOCKED`**. El enunciado pide **uno** de los dos, asi que con dos bloques la pregunta esta completa; el tercero se reconoce y no se exige.
- **4 pts — la diferencia entre los tres comportamientos, explicada en comentarios `--`.** Aproximadamente 1,3 pts cada uno y se pide precision, no extension: `FOR UPDATE` **espera**, `NOWAIT` **falla de inmediato** con `lock_not_available` (**55P03**), `SKIP LOCKED` **salta la fila** y devuelve cero filas. Confundir `NOWAIT` con `SKIP LOCKED` —los dos «no esperan», pero uno grita y el otro calla— es el error mas frecuente y cuesta la mitad de estos puntos.
- **4 pts — el comentario de cierre, y aqui esta el nucleo de la clase.** 1,5 pts reconocer que **en una sola sesion los tres se comportan igual porque nadie tiene la fila tomada** —el candado se concede siempre de inmediato—; 1,5 pts describir que se veria con dos sesiones reales; 1 pt elegir un mecanismo con argumento tecnico. La rubrica exige las tres cosas. Un cierre que diga «los tres funcionan igual» **sin** explicar que eso es un limite del entorno y no una propiedad de los mecanismos vale 0 de los primeros 1,5: es justo la conclusion equivocada que el taller quiere evitar.
- **Sobre la eleccion (el 1 pt final):** se acepta **A** o **B** si esta argumentado, pero **A** es la respuesta esperada y la pista del enunciado lo dice. El argumento completo es que A resuelve comprobacion y escritura en una sola sentencia atomica —sin ventana y sin convencion que recordar—, y que B es **necesario** cuando hay que leer, calcular con datos de varias tablas y despues escribir, porque ese calculo no cabe en el `WHERE` de un `UPDATE`. Quien nombre un caso concreto de VetCare para B —el cierre de caja que suma `detalle_factura` y ajusta `factura`— tiene la mejor respuesta posible.
- **Se reconoce como sobresaliente, sin puntos extra:** notar que con `SKIP LOCKED` el `SELECT ... INTO` no devuelve fila y `v_stock` queda en `NULL`, de modo que `IF v_stock >= 4` **no entra por ninguna rama** —hay que usar `IF NOT FOUND`—; o senalar que en un descuento de stock `SKIP LOCKED` es **peligroso** porque disfraza «no pude» de «no hay», mientras que en una cola de trabajos es exactamente el mecanismo correcto.

### Errores frecuentes y que hacer

- **Concluir que los tres candados «son equivalentes» porque dieron el mismo resultado.** Es la trampa central de la pregunta y la conclusion opuesta a la que se pide. Dieron el mismo resultado porque **el escenario que los diferencia no se puede montar con una sola sesion**. Lo que hay que reportar es la imposibilidad de la prueba, no una equivalencia inexistente.
- **Confundir `NOWAIT` con `SKIP LOCKED`.** Los dos «no esperan» y ahi termina el parecido: `NOWAIT` **lanza un error** —`55P03`, que la aplicacion puede capturar y traducir— y `SKIP LOCKED` **devuelve cero filas en silencio**. En un descuento de stock esa diferencia es grave: con `SKIP LOCKED` y sin `IF NOT FOUND`, «no pude tomar la fila» se reporta al usuario como «no hay gasas».
- **Volver al patron inseguro dentro de `fn_tomar_stock`:** `SELECT stock INTO` y despues un `IF`. En ExamLab da exactamente el mismo `true / false`, asi que el estudiante no tiene forma de notarlo por si mismo —y por eso hay que senalarlo en la devolucion—. La condicion va en el `WHERE`.
- **Entregar dos versiones del mismo mecanismo** en vez de los dos que se piden: por ejemplo, dos `UPDATE` condicionales con distinto nombre, o dos bloques `DO` los dos con `FOR UPDATE`. La pregunta compara **A contra B**: una sentencia atomica frente a un candado explicito. Sin las dos, no hay nada que comparar y el cierre se queda sin sustento.
- **Poner el `FOR UPDATE` en el `UPDATE`** en vez de en el `SELECT`. Un `UPDATE` ya bloquea las filas que modifica —eso no hay que pedirlo— y `FOR UPDATE` es clausula de `SELECT`: la sintaxis ni compila. Lo que el mecanismo B aporta es bloquear la fila **antes** de leerla, para que el valor leido siga siendo valido cuando se escriba.
- **Un cierre de una linea que solo elige un mecanismo.** La rubrica pide tres cosas en ese comentario y la eleccion es la menos valiosa de las tres. Sin el reconocimiento del limite del entorno y sin la descripcion de lo que se veria con dos sesiones, la pregunta pierde 3 de sus 20 puntos.

---

## Pregunta 4 · Niveles de aislamiento y anomalias en PostgreSQL · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| **SI** | El nivel por defecto en PostgreSQL es READ COMMITTED: cada sentencia ve una foto nueva de los datos confirmados, asi que dos lecturas dentro de la misma transaccion pueden dar resultados distintos. | **Correcta.** `READ COMMITTED` es el nivel por omision y su promesa es exactamente esa: **cada sentencia** toma una foto nueva de lo confirmado en el instante en que empieza. Dos `SELECT` iguales dentro de la misma transaccion pueden dar resultados distintos si entre ellos alguien confirmo un cambio, y eso se llama **lectura no repetible**. No es un defecto: es el contrato. Quien necesite que las dos lecturas coincidan tiene que pedir `REPEATABLE READ`, donde la foto se toma una vez por **transaccion** y no por sentencia. |
| **SI** | READ COMMITTED evita las lecturas sucias (dirty reads), pero no las lecturas no repetibles ni los fantasmas sobre un predicado. | **Correcta, y conviene aprenderse los tres nombres por separado.** `READ COMMITTED` **si** evita las **lecturas sucias** —nunca se ve un dato no confirmado— pero **no** evita las **lecturas no repetibles** —el mismo `SELECT` dos veces con distinto resultado— ni los **fantasmas** —filas nuevas que aparecen y cambian el resultado de un predicado—. La doble reserva de las preguntas 1 y 2 es justamente un fantasma: la fila que rompe la validacion **no existia** cuando cada transaccion la hizo. |
| no | En PostgreSQL, READ UNCOMMITTED permite leer datos no confirmados de otras transacciones. | **Incorrecta, y es la que mas se marca porque en otros motores seria cierta.** PostgreSQL **acepta la sintaxis** `SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED` —para no romper aplicaciones portadas— pero **la trata como `READ COMMITTED`**. En PostgreSQL las lecturas sucias **no son posibles en ningun nivel**, y no por una decision de configuracion sino por como funciona MVCC: una version de fila no confirmada simplemente **no es visible** para las demas transacciones. No hay forma de pedirle que la muestre. |
| **SI** | Con SERIALIZABLE, PostgreSQL puede abortar una transaccion con un error de serializacion; la aplicacion debe estar preparada para reintentarla. | **Correcta, y es la parte que casi siempre se olvida al implementar.** Con `SERIALIZABLE`, PostgreSQL vigila los predicados leidos y, si el resultado conjunto no equivale a haber ejecutado las transacciones una tras otra, **aborta una** con `serialization_failure` (SQLSTATE **40001**) y el mensaje «could not serialize access due to read/write dependencies among transactions». El error llega normalmente **al confirmar**, no al escribir. La consecuencia practica es la que dice la opcion: si la aplicacion no sabe **reintentar la transaccion completa**, elegir `SERIALIZABLE` no da mas seguridad, da errores intermitentes. |
| no | Una restriccion UNIQUE resuelve el problema solo si las transacciones se ejecutan una despues de otra; si son simultaneas, la restriccion no aplica. | **Incorrecta, y es exactamente al reves: la restriccion funciona sobre todo cuando las transacciones son simultaneas.** El propio taller la refuta: en la pregunta 2, el `INSERT` posterior fue rechazado con `unique_violation` sin que hiciera falta coordinar nada. Y el mecanismo tiene nombre: la insercion en un indice unico es un **punto de serializacion fisico**. La segunda transaccion que intenta escribir la misma clave **se queda esperando** en el B-tree hasta que la primera resuelva, y entonces recibe el error —o entra, si la primera hizo `ROLLBACK`—. Esa es la razon por la que la restriccion es la mitigacion **mas fuerte** de las tres de la pregunta 1: es la unica que no depende de que nadie se acuerde de nada. |
| **SI** | Mantener las transacciones cortas reduce la ventana de conflicto: nunca hay que dejar una transaccion abierta esperando que el usuario llene un formulario. | **Correcta, y es la unica de las seis que no es sobre el motor sino sobre como se escribe la aplicacion.** Mientras una transaccion esta abierta sostiene sus candados, y cada milisegundo que los sostiene es ventana para un conflicto. Dejar una transaccion abierta esperando que alguien llene un formulario convierte segundos de espera humana en minutos de bloqueo para todos los demas: el usuario se fue por un cafe y la agenda de la clinica esta detenida. La regla practica es leer, calcular y decidir **fuera** de la transaccion, y abrirla solo para escribir. Y ojo: **transaccion corta no es lo mismo que consulta rapida** —una transaccion de 50 ms que espera una confirmacion en pantalla puede retener un candado diez minutos—. |

### Como calificar

- **10 pts con las cuatro correctas marcadas y ninguna incorrecta;** puntaje proporcional por acierto parcial, tal como dice la rubrica del banco. Las correctas son las cuatro que hablan de `READ COMMITTED` como nivel por omision, de que evita lecturas sucias pero no no-repetibles ni fantasmas, del reintento necesario con `SERIALIZABLE` y de mantener las transacciones cortas.
- **La opcion de `READ UNCOMMITTED` es la que decide la nota de esta pregunta,** porque es correcta en otros motores y por eso se marca por analogia. Vale la pena responderla siempre con el dato concreto: PostgreSQL **acepta la sintaxis** y **la trata como `READ COMMITTED`**; las lecturas sucias no son posibles en ningun nivel por como funciona MVCC.
- **La opcion del `UNIQUE` que «solo funciona en secuencial» se refuta con el propio taller,** no con teoria: en la pregunta 2 el `INSERT` fue rechazado y no hubo que coordinar nada. Si un estudiante la marco, conviene revisarle tambien la pregunta 1, porque probablemente ordeno mal las mitigaciones —y esa es la comprension que la pregunta 4 esta midiendo—.
- Al devolver la pregunta conviene insistir en el matiz de la opcion del reintento: el error de `SERIALIZABLE` llega **al confirmar**, no al escribir. Es lo que hace que «poner `SERIALIZABLE`» no sea una decision del motor sino de la arquitectura de la aplicacion, y es lo que separa una respuesta memorizada de una entendida.

### Errores frecuentes y que hacer

- **Marcar la de `READ UNCOMMITTED`.** Transferencia desde SQL Server o desde la teoria generica de los cuatro niveles del estandar. En PostgreSQL ese nivel existe **solo como sinonimo** de `READ COMMITTED`. Quien lo marque suele tambien creer que `READ COMMITTED` «lee mal», y eso arrastra un error en la pregunta 1.
- **Marcar la del `UNIQUE` en secuencial.** Es la que revela si se entendio el mecanismo o solo se copio la sentencia. Una restriccion unica **serializa fisicamente** las inserciones de la misma clave; su valor esta justamente en el caso concurrente.
- **Dejar sin marcar la del reintento con `SERIALIZABLE`,** por parecer «un detalle de programacion». Es la unica de las seis que dice que hacer cuando la base dice no, y es la que separa una mitigacion implementable de una teorica.
- **Marcar las seis, o marcar cuatro «por si acaso» sin poder justificarlas.** El puntaje es proporcional y penaliza las incorrectas, asi que marcar todo baja la nota. Al devolver conviene pedir la justificacion de una sola opcion al azar: es la forma rapida de distinguir el acierto del tanteo.

---

## Pregunta 5 · Informe de concurrencia del PI y limites de la verificacion · 20 pts

### Respuesta esperada

| Momento | T1 (Auxiliar A) | T2 (Auxiliar B) | `insumo`: stock del id 2 | Comentario |
|---|---|---|---|---|
| **t0** | `BEGIN` | — | **3** | Quedan 3 vacunas triple felina. A empieza a facturar la consulta de Mishi y necesita 3 |
| **t1** | — | `BEGIN` | **3** | B empieza a facturar la de Nube y **tambien** necesita 3. Hay para una sola de las dos |
| **t2** | `SELECT stock` **-> 3** | — | **3** | A lee y decide: «3 >= 3, alcanza». **El `SELECT` no toma ningun candado** |
| **t3** | — | `SELECT stock` **-> 3** | **3** | **AQUI ESTA LA FALLA.** B lee el **mismo 3** y toma la **misma** decision. Las dos leyeron antes de que cualquiera escribiera |
| **t4** | `UPDATE stock = 3 - 3` | — | **0** (visible solo a T1) | A descuenta. Correcto: habia 3 y se llevo 3 |
| **t5** | — | `UPDATE stock = 3 - 3` | espera / **-3** segun como se escribio | B descuenta **sobre el 3 que leyo hace dos pasos**. Con `stock = stock - 3` sin condicion, el resultado es **-3**: tres vacunas que no existen, ya facturadas |
| **t6** | `COMMIT` | — | **0** confirmado | A confirma su factura |
| **t7** | — | `COMMIT` | **-3** … o error del `CHECK` | B confirma. Si la tabla tiene `CHECK (stock >= 0)`, **aqui aborta** y el dano se queda en un error feo en lugar de un inventario falso. Si no lo tiene, la clinica cree tener -3 vacunas y **las dos facturas ya se cobraron** |

El instante que hay que senalar es **t2–t5**, igual que en la doble reserva: las dos lecturas caen antes de la primera escritura, y las dos decisiones se toman sobre una foto que ya envejecio. Los dos escenarios del PI son el mismo problema con distinto disfraz —uno sobre una fila que **no existe** todavia, otro sobre una fila que **si existe** y cambia de valor—, y por eso llevan mitigaciones distintas.

**2. Mitigacion elegida para cada escenario, con la sentencia exacta.**

*Escenario 1 — doble reserva de franja:* **indice unico parcial**.

```sql
CREATE UNIQUE INDEX uq_cita_vet_franja
    ON cita (id_veterinario, fecha_hora)
 WHERE estado <> 'CANCELADA';
```

Se elige porque es la unica **estructural**: no depende de que el procedimiento este bien escrito, ni de que el proximo programador se acuerde de nada, ni de un `INSERT` a mano en una migracion. La condicion parcial no es un adorno: sin ella, cada cita cancelada dejaria su franja inutilizable para siempre. **Descartadas:** `SELECT ... FOR UPDATE` sobre la fila del veterinario, porque protege **codigo** y no **datos** —una via de insercion que se olvide del candado pasa por encima— y porque serializa todas las reservas de ese veterinario; y `SERIALIZABLE`, porque obligaria a que **toda** la aplicacion sepa reintentar y en este proyecto no hay ese nivel de control sobre el codigo cliente. Ninguna de las dos es mala: son mas fragiles para este equipo.

*Escenario 2 — doble descuento de stock:* **`UPDATE` condicional**, con el `CHECK` como segunda red.

```sql
UPDATE insumo
   SET stock = stock - p_cantidad
 WHERE id_insumo = p_id_insumo
   AND stock >= p_cantidad;   -- la condicion va aqui, no en un IF previo
GET DIAGNOSTICS v_filas = ROW_COUNT;
-- v_filas = 0 significa: no habia suficiente. Es una respuesta, no un error.
```

Se elige porque comprobar y escribir quedan en **una sola sentencia atomica**: no hay ventana t2–t5 en la que meterse. **Descartado** `SELECT ... FOR UPDATE` **para este caso**, no por debilidad —es correcto— sino porque es mas caro y no hace falta: sostiene el candado de la fila durante toda la transaccion y solo protege a quien lo pida. **Pero se conserva** para el unico caso del PI donde el `UPDATE` condicional no alcanza: el **cierre de caja**, que lee `detalle_factura`, suma, compara contra el total de `factura` y despues ajusta. Ese calculo no cabe en un `WHERE`, asi que ahi el candado explicito es obligatorio. Y el `CHECK (stock >= 0)` se queda como red final: garantiza que un negativo no pueda existir **aunque** alguien escriba mañana un procedimiento equivocado.

> **La regla en una linea:** cuando la condicion cabe en el `WHERE`, va en el `WHERE`; cuando hay que calcular con varias tablas antes de escribir, hace falta el candado explicito; y la restriccion declarativa va **siempre**, porque es la unica que sigue ahi cuando el codigo cambie.

**3. Contrato con la aplicacion.** Una fila por caso. La restriccion es la mitad del trabajo; esta tabla es la otra mitad:

| Caso | Que recibe la aplicacion | Que debe hacer | Que **no** debe hacer |
|---|---|---|---|
| **Doble reserva** | `unique_violation`, SQLSTATE **23505**, sobre `uq_cita_vet_franja` | Traducir a **«esa franja se acaba de ocupar»**, recargar la agenda del dia y ofrecer las tres franjas libres mas cercanas del mismo veterinario | **No reintentar el mismo `INSERT`**: volveria a fallar siempre. Y no mostrar el mensaje del motor en crudo |
| **Stock insuficiente** | La funcion devuelve **`false`** (`ROW_COUNT = 0`). **No hay excepcion:** es una respuesta de negocio | Mostrar **«quedan N unidades de X»** con el stock real, y ofrecer sustituto, cantidad menor o dejar el item en pedido. La factura no se emite | No tratarlo como error tecnico ni escribirlo en el log de fallos: **es un caso normal** y va al log de negocio |
| **Error de serializacion** (si algun dia se usa `SERIALIZABLE`) | `serialization_failure`, SQLSTATE **40001**, normalmente **al confirmar** | **Reintentar la transaccion completa** de forma automatica: hasta 3 intentos con espera creciente. Es el unico de los tres casos en que reintentar es la respuesta correcta | No mostrarle nada al usuario en los primeros intentos: no hizo nada mal. Solo si se agotan, un «intentalo de nuevo» |
| **Candado no disponible** (`FOR UPDATE NOWAIT` en el cierre de caja) | `lock_not_available`, SQLSTATE **55P03** | «La caja la esta cerrando otra persona en este momento». Reintentable, pero con intervencion humana | No reintentar en bucle: se estaria compitiendo con quien ya tiene el candado |

**4. Limitacion del entorno, explicitamente.** **No fue posible reproducir ningun bloqueo ni ningun interbloqueo real.** ExamLab ejecuta PostgreSQL compilado a **WebAssembly dentro del navegador**, con **una unica conexion**. No es que sea lento o limitado: es que **no existen dos transacciones concurrentes que puedan esperarse**. De ahi salen tres consecuencias concretas, y conviene escribirlas sin suavizarlas:

- **Las lineas de tiempo T1/T2 de las secciones 1 y 4 son razonamiento, no medicion.** Estan construidas sobre como funciona `READ COMMITTED`, no sobre una ejecucion observada.
- **Los tres candados —`FOR UPDATE`, `NOWAIT`, `SKIP LOCKED`— se comportaron igual,** porque el candado siempre se concedio de inmediato. Eso **no** prueba que sean equivalentes: prueba que el escenario que los distingue no se puede montar aqui.
- **Y lo mas incomodo: en una sola sesion, el patron inseguro habria dado exactamente los mismos resultados que el seguro.** El `true/false` de la pregunta 3 sale igual con la condicion en el `WHERE` que con un `IF` previo. El entorno **no distingue** el codigo correcto del incorrecto; lo distingue el razonamiento.

*Lo que si quedo demostrado, y no es poco:* que **sin** restriccion la base acepta el dato invalido y **con** ella lo rechaza, sin importar el orden ni la velocidad de las transacciones. Esa es la mitigacion estructural, y es verificable con una sola sesion precisamente porque no depende de la concurrencia.

*Como se probaria en un servidor real, con la evidencia que se capturaria:*

| Herramienta | Que se haria | Evidencia concreta a capturar |
|---|---|---|
| **Dos sesiones de `psql`** | Sesion A: `BEGIN`, `SELECT ... FOR UPDATE` del insumo 2, **sin confirmar**. Sesion B: el mismo `SELECT ... FOR UPDATE` | Captura de la sesion B **colgada**, y despues del `COMMIT` de A, la marca de tiempo en que se desbloquea. Repetir con `NOWAIT` para capturar el **55P03** inmediato |
| **`pg_locks`** | `SELECT locktype, relation::regclass, mode, granted, pid FROM pg_locks WHERE NOT granted;` mientras B espera | La fila con **`granted = false`**: es la prueba fotografiable de que un bloqueo existe y de quien lo tiene |
| **`pg_stat_activity`** | `SELECT pid, state, wait_event_type, wait_event, query FROM pg_stat_activity WHERE wait_event_type = 'Lock';` | El **`wait_event_type = 'Lock'`** de la sesion B, con la consulta exacta que esta esperando |
| **`pgbench`** con script propio | 20 clientes intentando reservar **la misma** franja y descontar el mismo insumo, 1.000 transacciones | El conteo de `23505` frente al de exitos: tiene que haber **exactamente 1 exito** por franja. Y el `stock` final, que debe cuadrar con las unidades facturadas |
| **Interbloqueo provocado** | Dos transacciones que descuentan los insumos 2 y 5 en **orden inverso** | El mensaje `deadlock detected` en el log con el **grafo de espera** que PostgreSQL imprime, y la confirmacion de que el motor mata a una de las dos. De ahi sale la regla de descontar **siempre en orden de `id_insumo` ascendente** |

**5. Riesgo residual.** Dos, y el segundo es el que de verdad preocupa:

- **Interbloqueo en facturas con varios insumos, sin mitigar.** Dos facturas que toman los insumos 2 y 5 en orden inverso pueden quedarse esperandose. La mitigacion es barata —**descontar siempre ordenando por `id_insumo` ascendente**, un `ORDER BY` en el bucle de `sp_facturar`— pero **no esta implementada ni probada**, porque no se puede probar aqui. *Vigilancia:* activar `log_lock_waits = on` con `deadlock_timeout = 1s` y revisar el log semanalmente; cualquier `deadlock detected` es un incidente que se investiga, no una curiosidad.
- **La franja del veterinario esta protegida; la de la mascota no.** El indice unico impide dos citas del mismo **veterinario** a la misma hora, pero **nada** impide que la misma **mascota** tenga dos citas simultaneas con dos veterinarios distintos. Es un dato invalido igual de real —Firulais no puede estar en dos consultorios— y **no** se cerro, porque hay un caso legitimo que habria que decidir primero: una urgencia atendida por dos veterinarios a la vez. *Vigilancia:* la misma consulta de deteccion de la pregunta 2, agrupando por `(id_mascota, fecha_hora)` en lugar de por veterinario, ejecutada como reporte semanal. **Si en tres meses devuelve cero filas, se convierte en un segundo indice unico parcial;** si devuelve filas legitimas, ya se sabe que el caso existe y como tratarlo. Documentar el criterio de decision es la mitad del trabajo.

**Archivos del PI:** esta seccion en `/informe/10-concurrencia.md`, el indice en `/db/05_restricciones_concurrencia.sql`, `fn_tomar_stock` en `/db/02_procedimientos.sql`, y las salidas de `evidencia` en `/informe/10-evidencia.txt`.

### Como calificar

- **5 pts — el escenario 2 con linea de tiempo de al menos 5 pasos.** 2 pts la estructura intercalada y **3 pts que esten marcados los instantes del `SELECT stock` de cada una y los de los `UPDATE`**, que es lo que la rubrica exige literalmente. Una linea de tiempo donde A lee, descuenta y confirma antes de que B lea describe el caso que funciona bien y vale 1 de 5. Se reconoce como sobresaliente notar que con el `CHECK (stock >= 0)` la anomalia termina en un **error** en vez de en un inventario falso: el dano cambia de forma, no desaparece.
- **5 pts — las dos mitigaciones con su sentencia SQL exacta y el descarte razonado.** 2,5 pts cada escenario, repartidos en tres: la sentencia completa y pegable —no «un `UNIQUE`» sino el `CREATE UNIQUE INDEX ... WHERE ...` entero—, el argumento de por que esa, y **el descarte de las alternativas**. El descarte es lo que mas falta y es lo que la rubrica nombra: sin el, no hay decision, hay una unica opcion considerada.
- **4 pts — la tabla del contrato con la aplicacion, cubriendo los tres tipos de error.** Aproximadamente 1,3 pts cada uno: `unique_violation` / **23505**, la funcion que devuelve `false`, y `serialization_failure` / **40001**. Lo que se califica es **la accion**, no el nombre del error. **El punto que separa una respuesta buena de una excelente:** distinguir que el `40001` **si** se reintenta automaticamente y el `23505` **no** —porque volveria a fallar siempre—. Quien invierta esos dos casos no entendio ninguno de los dos.
- **4 pts — la limitacion del entorno, y es donde se juega la clase.** 2 pts reconocer con precision **por que** no se puede: PostgreSQL en WebAssembly con **una unica conexion**, asi que no existen dos transacciones que puedan esperarse. 2 pts nombrar herramientas reales —dos sesiones de `psql`, `pg_locks`, `pg_stat_activity`, `pgbench`— **con la evidencia concreta que se capturaria en cada una**. «Usaria `pg_locks`» vale la mitad; «capturaria la fila con `granted = false` mientras B espera» vale el punto entero. **Un informe que presente la concurrencia como verificada pierde los 4 pts completos**, por perfecto que este el resto.
- **2 pts — el riesgo residual con su forma de vigilancia.** 1 pt identificar al menos uno de verdad sin mitigar y 1 pt **como se vigila**: una consulta concreta, una frecuencia, un parametro del servidor. «Habria que revisarlo» vale 0 de ese punto. Los dos residuos mas defendibles son el **interbloqueo** en facturas de varios insumos y que **la franja de la mascota no esta protegida** —solo la del veterinario—; el segundo es el mejor porque sale de leer su propia solucion de la pregunta 2 con ojo critico.
- **Extension:** dos paginas con las tablas. Se califican las cinco secciones completas, no la longitud. **Se reconoce como sobresaliente, sin puntos extra:** admitir que en una sola sesion el patron **inseguro** habria dado los mismos resultados que el seguro, y que por lo tanto el taller no distingue el codigo correcto del incorrecto. Es la observacion mas madura posible sobre esta clase.

### Errores frecuentes y que hacer

- **Presentar la concurrencia como resuelta y verificada.** Aparece como «se probo que el `UPDATE` condicional evita el doble descuento». No se probo: hubo **una sola sesion**, y la anomalia nunca ocurrio porque no podia ocurrir. El patron es correcto y el razonamiento es correcto; la evidencia no existe. La seccion 4 esta puesta exactamente para medir esa distincion, y confundirla cuesta 4 de los 20 puntos.
- **La linea de tiempo del escenario 2 sin marcar las lecturas.** Es el mismo error de la pregunta 1 y se repite porque se copia la estructura sin entenderla. Sin los instantes de los dos `SELECT stock` **antes** del primer `UPDATE`, la tabla no describe una anomalia: describe una operacion normal.
- **Mitigaciones sin la sentencia SQL.** «Se usa un indice unico» y «se usa un `UPDATE` condicional» no son mitigaciones: son titulos. La rubrica pide la **sentencia exacta**, y la razon es practica: quien no la escriba completa casi siempre olvida el `WHERE estado <> 'CANCELADA'`, que es la parte que evita romper el caso legitimo.
- **Invertir el contrato del reintento:** reintentar el `INSERT` que fallo con `23505` —volveria a fallar siempre, y en bucle es un ataque contra la propia base— y **no** reintentar el `40001`, que es el unico de los tres que **si** se debe reintentar de forma automatica. Es el error mas costoso en produccion de toda la clase.
- **Tratar el stock insuficiente como un error tecnico.** La funcion devuelve `false`, no lanza excepcion, y eso es deliberado: «no hay suficiente» es un **caso normal de negocio**. Mandarlo al log de fallos lo esconde entre ruido; mostrarle al usuario «error del sistema» en vez de «quedan 2 unidades» convierte una decision de mostrador en una llamada a soporte.
- **Nombrar herramientas sin decir que se capturaria con ellas.** Una lista —`pg_locks`, `pgbench`, `pg_stat_activity`— sin la evidencia asociada es un indice, no un plan. Lo que hace verificable la seccion 4 es la columna de la derecha: la fila con `granted = false`, el `wait_event_type = 'Lock'`, el conteo de `23505` frente a los exitos.
- **Decir «no hay riesgo residual».** Siempre hay. En este proyecto hay dos identificables sin salir del propio taller, y uno de ellos —que la franja de la **mascota** no esta protegida, solo la del **veterinario**— se encuentra releyendo el indice que se acaba de crear. Un informe sin riesgo residual no es un informe seguro: es uno que no se reviso.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Por que `READ COMMITTED` no evita la doble reserva, si es el nivel «normal»?**

Porque hace exactamente lo que promete y nada mas: cada sentencia ve una foto de lo **confirmado** en el instante en que esa sentencia empieza. Cuando la Recepcion B hace su `SELECT COUNT(*)`, la cita de A **todavia no existe** —o existe sin confirmar, que para B es lo mismo—, asi que B lee **0** y esa lectura es **correcta**. No hay lectura sucia en ninguna parte. Y la razon de fondo es la que hay que recordar: **un `SELECT COUNT(*)` no bloquea nada, y no puede**, porque un bloqueo se pone sobre filas que existen y aqui el conflicto lo produce una fila que todavia no existe. Por eso la solucion pasa por mover el candado a otro objeto: una fila que si exista, el B-tree de un indice unico, o un bloqueo de predicado con `SERIALIZABLE`.

**¿Por que el indice tiene que ser **parcial**? ¿No basta un `UNIQUE` normal?**

No, y es el error mas caro de la pregunta 2. Con un `UNIQUE` sobre `(id_veterinario, fecha_hora)` a secas, la primera vez que alguien cancele una cita esa franja queda **inutilizable para siempre**: la fila cancelada sigue ahi ocupando la clave, y nadie podra volver a agendar el lunes a las 9 con Laura. Con `WHERE estado <> 'CANCELADA'` el indice solo vigila las citas vivas, que es la regla de negocio real: una franja liberada se puede volver a vender. El paso 6 del enunciado —insertar una `CANCELADA` en la misma franja y comprobar que **si** entra— esta puesto justo para que este error se vea en pantalla y no en un comentario.

**Me dice `could not create unique index ... is duplicated`. ¿Que hice mal?**

Nada raro: te saltaste el paso 3, el `DELETE` del duplicado. Y el mensaje es una de las cosas mas utiles que aprendes hoy: **una restriccion solo se puede crear si los datos que ya existen la cumplen.** La base no te va a prometer una regla que tu propia tabla ya rompe. En un proyecto real esto es el orden obligatorio de cualquier arreglo de integridad: primero encuentras los datos malos con una consulta de deteccion, despues los limpias o los decides caso por caso, y solo entonces creas la restriccion. Vale la pena provocar el error a proposito una vez y dejarlo documentado.

**Si ExamLab tiene una sola sesion, ¿de que sirve el taller?**

Sirve para lo que **si** es demostrable con una sesion, que resulta ser lo mas importante: que sin restriccion la base **acepta** el dato invalido y con ella lo **rechaza**, sin importar el orden ni la velocidad de las transacciones. Esa es la mitigacion estructural, y es verificable precisamente porque **no** depende de la concurrencia. Lo que no se puede montar aqui es el escenario de la espera: ver a una sesion colgada esperando a otra. Eso no se disimula, se **declara** —es el punto 4 de la pregunta 5 y vale 4 de los 20 puntos—, y se dice con que herramientas se probaria en un servidor real.

**¿Cual es la diferencia real entre `FOR UPDATE`, `NOWAIT` y `SKIP LOCKED`?**

Es lo que cada uno hace **cuando la fila ya esta tomada por otra sesion**, y por eso aqui los tres se ven iguales: nunca esta tomada. `FOR UPDATE` **espera** a que la suelten —la operacion tarda, pero se hace—. `FOR UPDATE NOWAIT` **falla en el acto** con `lock_not_available`, SQLSTATE **55P03**, que la aplicacion puede capturar y traducir a «lo esta haciendo otra persona, intentalo en un momento». `FOR UPDATE SKIP LOCKED` **salta** la fila y devuelve cero filas, en silencio: es el mecanismo de las colas de trabajo, donde diez procesos leen la misma tabla y cada uno se lleva tareas distintas sin pisarse. Para descontar stock de un insumo concreto `SKIP LOCKED` es **peligroso**, porque «no pude tomar la fila» se disfraza de «no hay existencias».

**Con `SKIP LOCKED`, ¿por que mi `IF v_stock >= 4` no entra por ninguna rama?**

Porque si la fila se salta, el `SELECT ... INTO` **no devuelve ninguna fila** y `v_stock` se queda en `NULL`. Y `NULL >= 4` no es falso: es `NULL`, asi que el `IF` no entra por el `THEN` **ni** por el `ELSE`. Es el error silencioso de este mecanismo y hay que detectarlo con `IF NOT FOUND THEN ...` justo despues del `SELECT`, que es lo unico que distingue «no pude leer la fila» de «la lei y no alcanza». La leccion general es la misma de siempre con `NULL`: no significa cero, significa que no se sabe.

**¿Y si simplemente pongo `SERIALIZABLE` y me olvido del problema?**

Es la opcion mas limpia en teoria y la mas fragil en la practica, y la razon esta en **cuando** llega el error. Con `SERIALIZABLE`, PostgreSQL vigila los predicados que cada transaccion leyo y, si el resultado conjunto no equivale a haberlas ejecutado una tras otra, **aborta una** con `serialization_failure` (SQLSTATE **40001**) — y normalmente lo hace **al confirmar**, no al escribir. Eso significa que **toda** la aplicacion tiene que poder repetir la operacion completa. Un solo camino de codigo sin reintento convierte la garantia en errores intermitentes para el usuario, que es peor que no tener la garantia, porque nadie sabe reproducirlos. Es el unico de los casos de esta clase en que **reintentar es la respuesta correcta**: el `23505` de una franja ocupada, en cambio, volveria a fallar siempre.

**¿Por que el `UNIQUE` funciona con transacciones simultaneas, si nadie lo coordina?**

Porque el propio indice es el punto de coordinacion. Insertar en un indice unico es un **punto de serializacion fisico**: cuando la segunda transaccion intenta escribir la misma clave, se encuentra la entrada de la primera —todavia sin confirmar— y **se queda esperando** ahi. Cuando la primera resuelve, la segunda recibe el `unique_violation` si aquella confirmo, o entra tranquilamente si hizo `ROLLBACK`. Nadie tuvo que pedir un candado ni acordar nada: la estructura de datos lo impone. Es la razon por la que la restriccion es la mitigacion **mas fuerte** de las tres — es la unica que no depende de que alguien se acuerde de usarla— y es por eso que la opcion «el `UNIQUE` solo sirve si las transacciones van una despues de otra» de la pregunta 4 es falsa.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: la linea de tiempo de la doble reserva con el intervalo **t2–t5** senalado y las tres mitigaciones con garantia, costo y accion de la aplicacion; el script de la pregunta 2 con la deteccion encontrando la franja duplicada, el **indice unico parcial** creado, el rechazo capturado como `unique_violation` y la `CANCELADA` aceptada —**1, 1, 3 y 1** en la comprobacion final—; `fn_tomar_stock` dando **`true / false`** con el insumo 2 en 0, y los bloques `DO` con `FOR UPDATE` y `NOWAIT` o `SKIP LOCKED` llevando el insumo 5 de **8 a 4 a 0**; las cuatro opciones correctas de la pregunta 4; y la seccion de concurrencia en `/informe/10-concurrencia.md` con el contrato de errores y el limite del entorno declarado.
- Antes de cerrar hay que verificar **tres cosas y una coherencia**, y todas se leen sin ejecutar nada. Que la deteccion final devuelva **cero filas** y que la de la franja disputada deje **una** cita `PROGRAMADA` y **una** `CANCELADA` —si la cancelada no entro, el indice se creo sin la condicion parcial—. Que la pregunta 3 traiga **dos mecanismos distintos** y no dos versiones del mismo. Que la pregunta 5 diga en alguna parte que la concurrencia **no se pudo verificar**. Y la coherencia: quien haya marcado en la pregunta 4 que «el `UNIQUE` solo funciona en secuencial» no puede haber puesto la restriccion como mitigacion **mas fuerte** en la pregunta 1 — las dos respuestas se contradicen y conviene senalarlo en la devolucion, porque es ahi donde se aprende.
- Y el mensaje del dia, que hay que dejar por escrito porque no hay clase en vivo para decirlo: **la conclusion honesta de esta clase es una imposibilidad, no un resultado**. Con una sola sesion, los tres candados se comportaron igual y el patron inseguro habria dado exactamente los mismos `true` y `false` que el seguro. El entorno **no distingue** el codigo correcto del incorrecto; lo distingue el razonamiento, y por eso el peso de la nota esta en las lineas de tiempo y en el informe, no en que el SQL corra. Lo que si quedo probado es lo que mas vale en produccion: que una **restriccion declarativa** cierra el problema sin depender de nadie, mientras que un candado o un nivel de aislamiento dependen de que todo el mundo se acuerde. La Clase 11 cambia de tema —vistas, procedimientos y la capa que la aplicacion consume—, pero se lleva esta regla intacta: **si la regla se puede declarar, se declara; el codigo explica, la restriccion garantiza**.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
