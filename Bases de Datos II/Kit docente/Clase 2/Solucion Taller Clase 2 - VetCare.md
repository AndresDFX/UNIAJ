# Solucion del taller · Clase 2 · Administracion de BD y roles de VetCare

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Los 4 roles de VetCare creados y verificados con SQL que corre, la superficie recortada con una vista y con privilegios por columna, la matriz de 10 objetos x 4 roles consistente con esos GRANT, y la politica de altas y bajas con el limite del entorno reconocido.

> **El motor es PostgreSQL, no Oracle.** Las preguntas 1 y 3 son SQL que corre en ExamLab: `CREATE ROLE`, `GRANT`, `REVOKE`, `CREATE VIEW`, privilegios por columna e `information_schema` funcionan todos. Lo unico que el entorno no permite es una segunda sesion, asi que no se puede conectar como `recepcion` para ver el *permission denied*: eso es lo que la pregunta 5 pide reconocer. No repita en clase que «el playground no deja crear roles»: es falso aqui y cuesta los 50 puntos de las preguntas 1 y 3.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 2 - Administracion de bases de datos/Taller PI - Clase 2 - VetCare.docx`
- Configuracion en la plataforma: `Kit docente/Clase 2/Taller en ExamLab - Clase 2 (configuracion).md`
- Caso de estudio: `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
- Hito del PI: Plan de roles/privilegios de VetCare
- Entregable: Documento Roles_VetCare + script GRANT/REVOKE ejecutado en ExamLab
- **Estas preguntas: 100 puntos** en 5 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Crear los roles de VetCare y otorgar privilegios | `bd_sql` | 30 |
| 2 | Privilegio minimo en la matriz de VetCare | `cerrada_multi` | 10 |
| 3 | Reducir la superficie: vista de agenda y privilegios por columna | `bd_sql` | 20 |
| 4 | Matriz rol x objeto x privilegio de VetCare | `abierta` | 25 |
| 5 | Politica de altas y bajas de usuarios (y limites del entorno) | `abierta` | 15 |

---

## Pregunta 1 · Crear los roles de VetCare y otorgar privilegios · 30 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- 1) Los cuatro roles. NOLOGIN porque son bolsas de privilegios, no
    --    identidades: la persona se crea aparte, con LOGIN, y recibe el rol.
    -- =====================================================================
    CREATE ROLE admin_bd        NOLOGIN;
    CREATE ROLE recepcion       NOLOGIN;
    CREATE ROLE veterinario_rol NOLOGIN;
    CREATE ROLE auditor         NOLOGIN;

    -- =====================================================================
    -- 2) Privilegios. Un rol recien creado no tiene NINGUNO sobre tablas
    --    ajenas, asi que lo que no se escriba aqui queda negado por omision.
    -- =====================================================================

    -- recepcion: agenda y reprograma citas; identifica al cliente y su mascota.
    -- Sin DELETE: cancelar es UPDATE de estado a 'CANCELADA'.
    GRANT SELECT, INSERT, UPDATE ON cita TO recepcion;
    GRANT SELECT ON dueno, mascota, veterinario TO recepcion;

    -- veterinario_rol: lee la agenda y el paciente; documenta la atencion.
    GRANT SELECT ON cita, mascota TO veterinario_rol;
    GRANT SELECT, INSERT, UPDATE ON consulta TO veterinario_rol;

    -- auditor: solo lectura, y nunca una escritura.
    GRANT SELECT ON dueno, mascota, cita, consulta, factura TO auditor;

    -- admin_bd: el unico rol con privilegios amplios, sobre las 8 tablas.
    GRANT ALL PRIVILEGES ON dueno, mascota, veterinario, cita,
                            consulta, insumo, factura, detalle_factura
      TO admin_bd;

    -- =====================================================================
    -- 3) REVOKE explicito y documentado. Es redundante -- recepcion nunca
    --    recibio DELETE -- y se escribe precisamente por eso: deja por
    --    escrito que la ausencia de DELETE es una decision, no un olvido.
    --    Quien audite el script manana no tiene que adivinarlo.
    -- =====================================================================
    REVOKE DELETE ON cita FROM recepcion;

    -- =====================================================================
    -- 4) Verificacion: la matriz sale del motor, no de un documento.
    -- =====================================================================
    SELECT grantee, table_name, privilege_type
      FROM information_schema.role_table_grants
     WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')
     ORDER BY grantee, table_name, privilege_type;
```

### Salida esperada

```
Filas por rol (el orden es grantee, table_name, privilege_type):

      auditor          -> 5 filas   : cita, consulta, dueno, factura, mascota (SELECT en cada una)
      recepcion        ->  6 filas   : cita x 3 (INSERT, SELECT, UPDATE) + dueno, mascota, veterinario (SELECT)
      veterinario_rol  ->  5 filas   : cita (SELECT), consulta x 3 (INSERT, SELECT, UPDATE), mascota (SELECT)
      admin_bd         -> 56 o 64 filas : las 8 tablas x los privilegios que ALL PRIVILEGES expande

    Las tres primeras cifras son exactas y son las que hay que contar. La de admin_bd
    depende de la version del motor: ALL PRIVILEGES sobre una tabla expande a INSERT,
    SELECT, UPDATE, DELETE, TRUNCATE, REFERENCES y TRIGGER (7 x 8 = 56), y desde
    PostgreSQL 17 se agrega MAINTAIN (8 x 8 = 64). No descuente por esa diferencia:
    lo que se califica es que aparezcan las 8 tablas.

    Para revisar rapido una entrega, sin leer 60 filas, esta variante agrupa la matriz
    en una fila por rol y objeto (no se pide en el enunciado, es para el docente):

      SELECT grantee, table_name,
             string_agg(privilege_type, ', ' ORDER BY privilege_type) AS privilegios
        FROM information_schema.role_table_grants
       WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor')
       GROUP BY grantee, table_name
       ORDER BY grantee, table_name;

      grantee          | table_name  | privilegios
      -----------------+-------------+-----------------------
      auditor          | cita        | SELECT
      auditor          | consulta    | SELECT
      auditor          | dueno       | SELECT
      auditor          | factura     | SELECT
      auditor          | mascota     | SELECT
      recepcion        | cita        | INSERT, SELECT, UPDATE
      recepcion        | dueno       | SELECT
      recepcion        | mascota     | SELECT
      recepcion        | veterinario | SELECT
      veterinario_rol  | cita        | SELECT
      veterinario_rol  | consulta    | INSERT, SELECT, UPDATE
      veterinario_rol  | mascota     | SELECT
```

### Como calificar

- **10 pts — los 4 roles.** Los cuatro `CREATE ROLE` corren sin error y con `NOLOGIN`. 2,5 por rol. Si usa `CREATE USER`, medio punto menos por rol: no es un error de sintaxis (es un alias de `CREATE ROLE ... LOGIN`) pero contradice la decision de que estos cuatro son bolsas de permisos.
- **14 pts — los GRANT reproducen la matriz exactamente.** Se cuenta por rol: 4 pts `recepcion`, 3 pts `veterinario_rol`, 3 pts `auditor`, 4 pts `admin_bd`. Se descuenta tanto por privilegio de mas como de menos, y la verificacion es la salida de arriba: si `recepcion` no da 6 filas o `auditor` no da 5, hay una diferencia y hay que localizarla.
- **3 pts — el REVOKE explicito** de `DELETE ON cita FROM recepcion` esta presente. Se dan los 3 puntos completos aunque el estudiante escriba al lado que es redundante; de hecho, decirlo demuestra que entendio el punto de partida en cero.
- **3 pts — la consulta de verificacion** sobre `information_schema.role_table_grants` con las tres columnas pedidas y el `ORDER BY grantee, table_name, privilege_type`, y devuelve filas de los 4 roles.
- **Piso de sintaxis.** Si el script no corre, no hay puntos de los 14 de la matriz: la pregunta es `bd_sql` y la evidencia es que el motor lo acepte. Si corre pero la matriz esta incompleta, se califica lo que si quedo.

### Errores frecuentes y que hacer

- **`GRANT CREATE SESSION TO recepcion`.** Es sintaxis de Oracle y en PostgreSQL no existe. El equivalente no es un privilegio sino un atributo del rol: `LOGIN`, que se escribe en el `CREATE ROLE`. Aparece en quien busco en internet sin filtrar por motor.
- **`CREATE USER recepcion IDENTIFIED BY '...'`.** Tambien Oracle. En PostgreSQL es `CREATE ROLE recepcion LOGIN PASSWORD '...'`, y hoy no hace falta ninguna clave porque no se conecta nadie.
- **Otorgar `DELETE` a `recepcion` «para que pueda cancelar».** Es justo lo que la pregunta 2 evalua. Cancelar es `UPDATE cita SET estado = 'CANCELADA'`: conserva la historia y basta el `UPDATE` que ya tiene.
- **Darle `ALL PRIVILEGES` a `admin_bd` sobre 5 tablas y no 8.** Deja al administrador sin acceso a `dueno`, `mascota` y `veterinario`, y entonces la matriz de la pregunta 4 queda con guiones en la columna del administrador, que es indefendible. Es el error mas facil de arrastrar porque no produce ningun mensaje de error.
- **Escribir el rol en mayusculas y creerlo distinto.** PostgreSQL pasa los identificadores sin comillas a minusculas, asi que `RECEPCION` y `recepcion` son el mismo rol. `"Recepcion"` entre comillas dobles si es otro, y ese si produce un error de rol inexistente que cuesta encontrar.
- **Entregar solo la matriz en un documento** porque «el playground no deja». Aqui si deja. Si alguien llega con eso, es probable que lo haya leido en una version anterior de la guia: corrijalo en voz alta al grupo entero.

---

## Pregunta 2 · Privilegio minimo en la matriz de VetCare · 10 pts

### Clave y por que

La clave se lee del banco de la plataforma, asi que esta es la que se califica. La columna de la derecha es lo que hay que poder responderle al estudiante cuando pregunte.

|  | Opcion | Por que |
|---|---|---|
| no | Darle DELETE sobre cita es aceptable porque cancelar una cita es basicamente borrarla. | **Incorrecta.** Confunde la accion del negocio con la sentencia SQL. Cancelar es un cambio de estado, no una desaparicion: la cita cancelada hay que poder contarla, cobrarla si aplica y explicarla. Con `DELETE` se pierde la evidencia de que existio, y ademas se abre la puerta a un `DELETE` sin `WHERE` que borre la agenda completa. |
| **SI** | Cancelar debe ser un UPDATE de estado a 'CANCELADA', no un DELETE: se conserva la historia y basta el privilegio UPDATE. | **Correcta.** Es el borrado logico de la Clase 1 aplicado a permisos: `UPDATE cita SET estado = 'CANCELADA' WHERE id_cita = ...`. Se conserva la historia y el rol no necesita ningun privilegio nuevo, porque `UPDATE` ya lo tiene para reprogramar. |
| no | Conviene darle ALL PRIVILEGES sobre cita para no tener que ajustar permisos cada vez que cambie el proceso. | **Incorrecta.** Es exactamente lo contrario de privilegio minimo: se otorga por comodidad futura y no por necesidad presente. `ALL PRIVILEGES` sobre `cita` incluye `DELETE` y `TRUNCATE`, asi que un error de copiar y pegar vacia la tabla. El argumento de «no tener que ajustar permisos» es justamente lo que resuelve el rol: se ajusta en un solo lugar. |
| **SI** | Sobre dueno y mascota le basta SELECT; no necesita INSERT ni UPDATE porque el alta de mascotas la hace otro rol. | **Correcta.** El alta de una mascota la hace otro rol, asi que recepcion no necesita escribir en `dueno` ni en `mascota`; le basta leer para identificar a quien llama. Cada privilegio que no se otorga es una superficie de dano que no existe. |
| **SI** | Si solo requiere telefono y nombre del dueno, es mejor exponerle una vista o privilegios por columna que la tabla dueno completa con email y direccion. | **Correcta.** Es el mecanismo de la pregunta 3. Si solo necesita nombre y telefono, darle la tabla `dueno` completa le entrega tambien el correo y la ciudad. La vista o el privilegio por columna entregan el dato sin el resto. |
| no | El rol auditor deberia tener UPDATE sobre la tabla de auditoria para poder corregir registros erroneos. | **Incorrecta.** Y es la mas importante de descartar. Quien puede corregir el registro de lo que hizo puede borrar la evidencia de lo que hizo: una tabla de auditoria con `UPDATE` para el auditor no prueba nada. Un registro erroneo se corrige con un registro nuevo que deja fecha y autor, no editando el anterior. |

### Como calificar

- 10 pts con las tres correctas (indices 1, 3 y 4) y ninguna incorrecta marcada.
- Parcial proporcional: 10/3 ≈ 3,33 por correcta marcada, menos 3,33 por cada incorrecta marcada, con piso en 0. Quien marque las 6 saca 0, y eso es deliberado: marcar todo no es responder.
- Si alguien marca 0 y 1 a la vez, senale la contradiccion en voz alta: son afirmaciones opuestas sobre la misma decision, y no se puede estar de acuerdo con las dos.

### Errores frecuentes y que hacer

- **Marcar la 5 «porque el auditor tiene que poder corregir errores».** Es la trampa de la pregunta y la que mas cae. La respuesta es que corregir un registro de auditoria destruye su valor como prueba.
- **Marcar la 2 «porque asi no toca volver a tocar permisos».** Confunde comodidad del administrador con necesidad del usuario. Es el argumento con el que en la practica se llega a que todo el mundo sea administrador.
- **Dudar entre 3 y 4 y marcar solo una.** No son alternativas: la 3 dice que sobre `dueno` basta `SELECT`, y la 4 dice que incluso ese `SELECT` puede recortarse a dos columnas. Son dos pasos del mismo razonamiento.

---

## Pregunta 3 · Reducir la superficie: vista de agenda y privilegios por columna · 20 pts

### Respuesta esperada (SQL que corre tal cual)

```sql
-- =====================================================================
    -- 1) La vista recorta las dos dimensiones a la vez:
    --    filas  -> WHERE c.estado <> 'CANCELADA'
    --    columnas -> el email del dueno simplemente no esta en el SELECT
    -- =====================================================================
    CREATE VIEW v_agenda_recepcion AS
    SELECT c.id_cita,
           c.fecha_hora,
           c.estado,
           m.nombre  AS mascota,
           d.nombre  AS dueno,
           d.telefono,
           v.nombre  AS veterinario
      FROM cita c
      JOIN mascota     m ON m.id_mascota     = c.id_mascota
      JOIN dueno       d ON d.id_dueno       = m.id_dueno
      JOIN veterinario v ON v.id_veterinario = c.id_veterinario
     WHERE c.estado <> 'CANCELADA';

    GRANT SELECT ON v_agenda_recepcion TO recepcion;

    -- Y se le cierra la puerta directa: a partir de aqui recepcion llega al
    -- telefono del dueno UNICAMENTE a traves de la vista. Funciona porque la
    -- vista se ejecuta con los privilegios de su propietario, no de quien la
    -- consulta.
    REVOKE SELECT ON dueno FROM recepcion;

    -- =====================================================================
    -- 2) Privilegio por columna: mismo objetivo, sin crear objeto nuevo.
    -- =====================================================================
    GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol;

    -- =====================================================================
    -- 3) Verificacion
    -- =====================================================================
    SELECT * FROM v_agenda_recepcion ORDER BY fecha_hora;

    SELECT grantee, table_name, column_name, privilege_type
      FROM information_schema.column_privileges
     WHERE grantee = 'veterinario_rol'
       AND table_name = 'dueno'
     ORDER BY column_name;
```

### Salida esperada

```
SELECT * FROM v_agenda_recepcion ORDER BY fecha_hora;  -- 9 filas

     id_cita |     fecha_hora      |   estado   | mascota  |     dueno      |  telefono  |  veterinario
    ---------+---------------------+------------+----------+----------------+------------+----------------
           1 | 2026-09-01 08:00:00 | PROGRAMADA | Firulais | Ana Gomez      | 3001112233 | Laura Restrepo
           2 | 2026-09-01 09:00:00 | ATENDIDA   | Luna     | Ana Gomez      | 3001112233 | Laura Restrepo
           3 | 2026-09-01 10:00:00 | PROGRAMADA | Mishi    | Marcela Diaz   | 3027778899 | Diego Moreno
           5 | 2026-09-02 11:00:00 | ATENDIDA   | Nube     | Jorge Pineda   | 3105551212 | Diego Moreno
           6 | 2026-09-03 07:45:00 | PROGRAMADA | Toby     | Luisa Cardona  | 3123334455 | Ivan Ortiz
           7 | 2026-09-05 15:00:00 | ATENDIDA   | Firulais | Ana Gomez      | 3001112233 | Laura Restrepo
           8 | 2026-09-08 16:00:00 | PROGRAMADA | Luna     | Ana Gomez      | 3001112233 | Paula Salazar
           9 | 2026-09-10 08:00:00 | PROGRAMADA | Mishi    | Marcela Diaz   | 3027778899 | Ivan Ortiz
          10 | 2026-09-10 09:00:00 | ATENDIDA   | Nube     | Jorge Pineda   | 3105551212 | Laura Restrepo

    Son 9 de las 10 citas sembradas: falta la id_cita 4, que esta CANCELADA. Ese
    "9 y no 10" es la comprobacion de un solo golpe de que el WHERE quedo puesto.
    Notese tambien que no hay columna de email: la vista no lo expone.


    SELECT ... FROM information_schema.column_privileges ...  -- exactamente 2 filas

        grantee      | table_name | column_name | privilege_type
    -----------------+------------+-------------+----------------
     veterinario_rol | dueno      | id_dueno    | SELECT
     veterinario_rol | dueno      | nombre      | SELECT

    Si aparecen 4 o 6 filas, con telefono, email o ciudad, es que se otorgo la
    tabla completa y el recorte por columna no se hizo.
```

### Como calificar

- **8 pts — la vista.** 4 pts por las 7 columnas con los alias pedidos (`mascota`, `dueno`, `telefono`, `veterinario`), 2 pts por excluir el email y 2 pts por el `WHERE` que deja fuera las canceladas. El `SELECT` sobre la vista devuelve 9 filas: si devuelve 10, falta el filtro; si devuelve mas de 10, hay un JOIN mal cerrado y se multiplicaron filas.
- **4 pts — el traslado del acceso.** 2 pts por `GRANT SELECT ON v_agenda_recepcion TO recepcion` y 2 pts por el `REVOKE SELECT ON dueno FROM recepcion`. Los dos: dar la vista sin cerrar la tabla no reduce nada, porque el rol sigue pudiendo leer el email por la puerta de al lado.
- **5 pts — el privilegio por columna.** La forma exacta `GRANT SELECT (id_dueno, nombre) ON dueno TO veterinario_rol`. Se descuenta todo si otorgo la tabla completa, aunque despues escriba que «idealmente serian dos columnas»: la pregunta es de implementacion.
- **3 pts — las dos consultas de verificacion**, y que la segunda devuelva exactamente las dos filas de arriba.
- **Bono conceptual, sin puntos.** Si el estudiante escribe en un comentario por que la vista funciona despues del `REVOKE` (se ejecuta con los privilegios del propietario), tomelo como senal de que entendio el mecanismo y no solo copio la sintaxis. Es el concepto central de la pregunta.

### Errores frecuentes y que hacer

- **`WHERE c.estado != 'cancelada'` en minusculas.** No falla ni avisa: devuelve las 10 filas porque ninguna coincide con el literal en minusculas, y el estudiante cree que su filtro funciona. El `CHECK` de la tabla guarda `'CANCELADA'` en mayusculas.
- **`SELECT *` dentro de la vista.** Trae el email y la ciudad, que es exactamente lo que la pregunta pide dejar fuera. Ademas la vista queda amarrada a la forma de las tablas: si manana se agrega una columna sensible a `dueno`, la vista la expone sola.
- **Dar la vista y olvidar el `REVOKE`.** Es el error mas comun y el mas invisible: todo corre, la vista se ve bien, y la superficie no se redujo ni un poco.
- **`GRANT SELECT ON dueno(id_dueno, nombre) TO veterinario_rol`.** Las columnas van despues del privilegio, no despues de la tabla: `GRANT SELECT (id_dueno, nombre) ON dueno`. Es un error de sintaxis, asi que al menos avisa.
- **Esperar que `veterinario_rol` pueda hacer `SELECT * FROM dueno`.** No puede, y esa es la consecuencia correcta del privilegio por columna: el asterisco pide todas las columnas y dos de ellas le estan negadas. Tiene que nombrarlas. Vale advertirlo antes de que alguien lo reporte como fallo.
- **Crear la vista sin `veterinario` en el JOIN** y poner el `id_veterinario` en bruto. La pregunta pide el nombre del veterinario: quien lee la agenda es una persona en el mostrador, no un programa.

---

## Pregunta 4 · Matriz rol x objeto x privilegio de VetCare · 25 pts

### Respuesta esperada

| Objeto | admin_bd | recepcion | veterinario_rol | auditor |
|---|---|---|---|---|
| `dueno` | S I U D | - (vista) | S (2 col.) | S |
| `mascota` | S I U D | S | S | S |
| `veterinario` | S I U D | S | - | - |
| `cita` | S I U D | S I U | S | S |
| `consulta` | S I U D | - | S I U | S |
| `insumo` | S I U D | - | - | - |
| `factura` | S I U D | - | - | S |
| `detalle_factura` | S I U D | - | - | - |
| `sp_agendar_cita` | E | E | - | - |
| `sp_facturar` | E | - | - | - |

La celda de `dueno` x `recepcion` es la unica que necesita nota al pie, y es la que separa una matriz copiada de una razonada: **no es `-` a secas ni `S` a secas**. Despues de la pregunta 3, `recepcion` no tiene `SELECT` sobre la tabla `dueno` — se le revoco — pero si tiene `SELECT` sobre `v_agenda_recepcion`, y por ahi llega al nombre y al telefono. Se acepta escribirlo como `-` con la nota «solo via `v_agenda_recepcion`», o agregar la vista como fila 11 de la matriz. Lo que no se acepta es `S`, porque contradice el `REVOKE` que el propio estudiante ejecuto.

Las tres justificaciones que la pregunta pide (4 a 6 lineas en total):

1. **Ningun rol operativo tiene `D`.** En VetCare nada se borra: una cita cancelada lleva `estado = 'CANCELADA'` y una mascota que ya no se atiende lleva `activa = 'N'`. Como el borrado es logico, `DELETE` no le hace falta a nadie que opere el dia a dia, y no otorgarlo elimina de raiz la perdida accidental de informacion. Solo `admin_bd` lo conserva, y para tareas de mantenimiento, no de operacion.
2. **`auditor` es de solo lectura, incluida la tabla de auditoria** que llegara en la Clase 4. Quien puede corregir el registro de lo que hizo puede borrar la evidencia de lo que hizo; un registro equivocado se corrige con uno nuevo que deja fecha y autor.
3. **La aplicacion llegara por `E` y no por `I`.** `recepcion` tiene `E` sobre `sp_agendar_cita` porque agendar no es «insertar una fila en `cita`»: es insertarla *si* la mascota esta activa y *si* el veterinario tiene la franja libre. Con `EXECUTE`, la regla vive una sola vez dentro de la base y ninguna pantalla puede saltarsela. Ese es el patron que construye la Clase 3 y que consume la Clase 12.

### Como calificar

- **14 pts — la matriz completa.** Los 10 objetos x 4 roles, sin celdas vacias, a razon de 1,4 pts por fila. El `-` cuenta como respuesta; la celda en blanco, no.
- **5 pts — consistencia con la pregunta 1.** Es el criterio duro y se revisa comparando contra el script del estudiante, no contra esta tabla: si su script no otorgo `DELETE` a nadie, en su matriz no puede haber una `D`; si le dio `ALL PRIVILEGES` a `admin_bd` sobre 8 tablas, las 8 filas de esa columna tienen que estar servidas. Una matriz internamente coherente con un script distinto del de arriba se califica completa.
- **3 pts — los procedimientos con `E`.** `sp_agendar_cita` y `sp_facturar` aparecen con `E` y nunca con `S`, `I`, `U` o `D`. Es el error conceptual que esta pregunta busca: un procedimiento no se consulta, se ejecuta.
- **3 pts — la justificacion.** Tres decisiones concretas, cada una nombrando privilegio minimo y el dano que evita. 1 pt por decision. No se dan puntos por repetir la definicion del principio sin aplicarla a una celda de la matriz.
- **Descuentos.** −2 por cada rol con `ALL PRIVILEGES` sin justificar (aparte de `admin_bd`, que si esta justificado). −1,4 por objeto omitido.

### Errores frecuentes y que hacer

- **`admin_bd` con guiones en `dueno`, `mascota` y `veterinario`.** Es el arrastre del error de la pregunta 1 y produce una matriz donde el administrador de la base no puede leer a los clientes. Si aparece, la correccion es en la pregunta 1 y la matriz se recalifica coherente.
- **Poner `S` en `dueno` x `recepcion`.** Contradice el `REVOKE` de la pregunta 3. Es la celda que revela si el estudiante armo la matriz mirando su propio script o copiandola de la teoria.
- **`sp_agendar_cita` con `I` «porque inserta una cita».** Confunde lo que el procedimiento hace por dentro con el privilegio que necesita quien lo llama. El rol solo necesita `EXECUTE`; el `INSERT` lo hace el procedimiento con los privilegios de su propietario, que es precisamente la gracia.
- **Dar `S` sobre `insumo` y `detalle_factura` a `auditor` «porque audita todo».** Aqui hay que ser justo: es una decision defendible y no un error, siempre que su script de la pregunta 1 lo haya otorgado. Si la matriz dice `S` y el script no lo otorgo, el problema es la inconsistencia, no la decision.
- **Justificar con la definicion en vez de con el caso.** «Aplicamos privilegio minimo porque cada rol debe tener solo lo necesario» no dice nada sobre VetCare. Se pide nombrar la celda y el dano que evita.

---

## Pregunta 5 · Politica de altas y bajas de usuarios (y limites del entorno) · 15 pts

### Respuesta esperada

Version de referencia, en una pagina. Lo que se califica no es la redaccion sino que **haya responsables y plazos concretos**: «el administrador» y «lo antes posible» no son respuestas.

**1. Alta.** La solicita el jefe del area donde entra la persona (recepcion, clinica o administracion) por correo a la coordinacion. La aprueba la administradora de la clinica, que es la unica que decide quien entra a la base. La ejecuta el `admin_bd` creando un rol con `LOGIN` y otorgandole **exactamente uno** de los cuatro roles del negocio segun el cargo; por omision, `recepcion` para el personal de mostrador. La credencial inicial se entrega en persona o por un canal distinto del correo con el que se pidio, es temporal, y el sistema exige cambiarla en el primer ingreso. Caduca a las 72 horas si no se usa, y en ese caso hay que volver a solicitarla.

**2. Cambio de rol.** Una recepcionista que pasa a auxiliar veterinaria recibe `GRANT veterinario_rol TO ana_gomez` y — esto es lo que se califica — **pierde el anterior** con `REVOKE recepcion FROM ana_gomez`, el mismo dia y en la misma solicitud. Los permisos no se acumulan: quien conserva los dos roles termina pudiendo hacer las dos mitades de un proceso que se separo a proposito. La solicitud la firma el jefe que la recibe y la nota el jefe que la entrega, para que ninguno de los dos asuma que el otro pidio la revocacion.

**3. Baja.** El mismo dia de la desvinculacion, y antes de que la persona salga del edificio: (a) `REVOKE` de todos los roles del negocio; (b) `ALTER ROLE ana_gomez NOLOGIN` para cerrar el acceso sin destruir nada; (c) los objetos que la persona era dueno se reasignan con `REASSIGN OWNED BY ana_gomez TO admin_bd`, porque PostgreSQL no permite `DROP ROLE` de un rol que todavia posee objetos, y porque una vista o un procedimiento que desaparece con su autor rompe la aplicacion; (d) el rol se conserva deshabilitado, **no se borra**, durante los cinco anos de retencion de la traza clinica, para que los registros de auditoria sigan apuntando a un nombre y no a un identificador huerfano.

**4. Revision periodica.** Cada tres meses, el primer lunes del trimestre. La evidencia es la salida de `SELECT grantee, table_name, privilege_type FROM information_schema.role_table_grants WHERE grantee IN ('admin_bd','recepcion','veterinario_rol','auditor') ORDER BY 1,2,3`, mas `information_schema.column_privileges` para los recortes por columna, y se compara contra la matriz aprobada. Firma la administradora de la clinica; el `admin_bd` prepara la evidencia pero no se autoaprueba, porque eso rompe la separacion de funciones que la matriz defiende. Toda diferencia se corrige o se documenta como excepcion con fecha de vencimiento.

**5. Limite del entorno de practica.** En ExamLab la base es PostgreSQL corriendo en el navegador, con **una sola sesion y un solo usuario**. Eso alcanza para todo lo que es DDL de permisos — crear los cuatro roles, otorgar, revocar, crear la vista, recortar por columna — y para verificarlo con `information_schema`, porque esas consultas describen el estado del catalogo y no requieren cambiar de identidad. Lo que **no** se puede hacer es la prueba negativa: conectarse como `recepcion` e intentar un `DELETE FROM cita` para ver el rechazo. En un servidor real se hace sin cambiar de conexion, con `SET ROLE recepcion;` seguido de `DELETE FROM cita WHERE id_cita = 1;`, y el resultado esperado es el error `permission denied for table cita`; despues se vuelve con `RESET ROLE`. La ausencia de esa prueba es una brecha de verificacion concreta en esta entrega: se comprobo que el permiso **esta escrito** como se decidio, no que el motor **lo hace cumplir**. Son dos afirmaciones distintas y solo una quedo demostrada.

### Como calificar

- **8 pts — las cinco secciones, con responsable y plazo.** 1,6 por seccion. Se descuenta la mitad de la seccion cuando dice que hay que hacer algo pero no dice quien ni cuando: una politica sin responsable no es ejecutable.
- **2 pts — el cambio de rol incluye la revocacion del anterior.** Es el punto que separa una politica pensada de una lista de buenas intenciones. Si solo dice que se otorga el nuevo, no se dan.
- **2 pts — la baja resuelve el destino de los objetos** (`REASSIGN OWNED` o equivalente razonado) y dice cuanto se conserva la traza.
- **3 pts — la seccion 5.** 1 pt por identificar bien la limitacion (una sola sesion, no «no se pueden crear roles»), 1 pt por proponer `SET ROLE` u otra conexion como prueba negativa, y 1 pt por nombrar la consecuencia: que sin esa prueba lo verificado es la configuracion y no el cumplimiento.
- **Extension.** Una pagina es el techo, no la meta. Tres parrafos que resuelven las cinco secciones valen mas que dos paginas de generalidades, y no se descuenta por brevedad si esta todo.

### Errores frecuentes y que hacer

- **«El administrador revisa los permisos periodicamente».** No tiene responsable con nombre de cargo, no tiene periodo y no tiene evidencia. Es la forma mas comun de entregar esta pregunta y no vale los puntos de la seccion 4.
- **Decir que en la baja se hace `DROP ROLE` y listo.** Falla en el motor si el rol posee objetos, y destruye la trazabilidad de la auditoria. La respuesta correcta es deshabilitar, reasignar y conservar.
- **Escribir en la seccion 5 que «en ExamLab no se pueden crear roles ni otorgar privilegios».** Es la limitacion equivocada, y ademas contradice las preguntas 1 y 3, que el propio estudiante acaba de ejecutar. Casi siempre viene de leer material de otro motor.
- **Proponer como prueba negativa «abrir otra pestana y entrar como recepcion».** No sirve: no hay segundo usuario ni segunda sesion. Lo que se pide es el comando concreto de PostgreSQL, y es `SET ROLE`.
- **Permitir cuentas compartidas** («la cuenta recepcion1 la usan las tres recepcionistas»). Rompe toda la auditoria de la Clase 4 antes de escribirla: el disparador registrara siempre el mismo nombre y ninguna investigacion posterior podra atribuir un cambio a una persona.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**Ejecute el GRANT y no surtio efecto. ¿Por que?**

Casi siempre es una de cuatro cosas, en este orden de frecuencia: (1) se otorgo el privilegio al rol pero no se otorgo el rol a la persona, y falta el `GRANT recepcion TO ana_gomez`; (2) se esta «comprobando» en la misma sesion del propietario, que pasa por encima de todos los permisos y por lo tanto nunca vera un error; (3) el rol no tiene `USAGE` sobre el esquema — en `public` viene por omision, asi que hoy no estorba, pero en un servidor real es la causa numero uno; (4) el nombre se escribio entre comillas dobles, y `"Recepcion"` no es `recepcion`.

**¿ExamLab me va a dejar hacer CREATE ROLE?**

Si. Es PostgreSQL real en el navegador y el DDL de permisos funciona completo. Lo unico que no hay es una segunda sesion. Si un estudiante llega diciendo que no puede, revise el mensaje de error real antes de aceptar la premisa: normalmente es un rol que ya existia de un intento anterior, y se resuelve con `DROP ROLE` o volviendo a cargar el ejercicio.

**Si le doy SELECT solo a la vista, ¿no necesita tambien SELECT sobre dueno?**

No, y es el concepto central de la clase: la consulta de la vista se ejecuta con los privilegios de su **propietario**, no con los de quien la consulta. Por eso se puede dar la vista y revocar la tabla en el mismo script, y el rol sigue viendo el telefono pero ya no el correo.

**¿Puedo demostrar que a recepcion le rebota el DELETE?**

No en ExamLab, porque hay una sola sesion. En un servidor real, sin abrir otra conexion: `SET ROLE recepcion;` y luego `DELETE FROM cita WHERE id_cita = 1;`, que debe responder `permission denied for table cita`; se vuelve con `RESET ROLE`. Esa es la respuesta que vale puntos en la pregunta 5.

**¿Rol y usuario son lo mismo?**

En PostgreSQL si: un usuario es un rol con el atributo `LOGIN`, y `CREATE USER` es literalmente un alias de `CREATE ROLE ... LOGIN`. Por eso los cuatro roles del taller se crean con `NOLOGIN`: son paquetes de permisos, no identidades con las que alguien se conecte.

**¿Por que el rol se llama veterinario_rol y no veterinario?**

Por legibilidad, no por obligacion del motor. En PostgreSQL los roles son globales al cluster y las tablas viven en un esquema, asi que un rol `veterinario` y una tabla `veterinario` pueden coexistir sin problema. Pero en la linea `GRANT SELECT ON cita TO veterinario` nadie puede saber a simple vista si eso es un rol o un error, y el sufijo lo resuelve. Conviene dar esta respuesta completa: un estudiante despierto va a preguntar y merece la razon verdadera.

**¿El REVOKE de DELETE no es inutil si nunca se otorgo?**

Tecnicamente si es redundante, y decirlo esta bien. Se escribe porque es la evidencia documental de la decision: quien lea el script en seis meses tiene que poder distinguir «aqui se decidio que recepcion no borra» de «aqui se olvidaron de darle DELETE». Vale los 3 puntos igual.

**¿La matriz va en el mismo ExamLab o en un documento aparte?**

En ExamLab, en la respuesta de la pregunta 4, como tabla markdown. El documento `Roles_VetCare` de la carpeta del PI es la misma matriz mas la politica, y sirve para que el estudiante conserve su trabajo; lo que se califica es lo que esta en la plataforma.

---

## Cierre de la clase

- Al terminar, cada estudiante debe tener: el script de los 4 roles corriendo con su consulta de verificacion, la vista `v_agenda_recepcion` con el `REVOKE` que la hace necesaria, el privilegio por columna evidenciado en `column_privileges`, la matriz de 10 objetos x 4 roles consistente con su propio script, y la politica de una pagina.
- Lo que hay que verificar antes de cerrar la sesion es la **consistencia entre la pregunta 1 y la pregunta 4**: son la misma decision escrita dos veces, en SQL y en tabla, y la mitad de las entregas flojas se detecta comparandolas. Proyecte una entrega voluntaria y haga esa comparacion en vivo.
- Dejar dicho en voz alta lo que sigue: en la Clase 3 el rol `recepcion` va a perder el `INSERT` directo sobre `cita` y va a recibir `EXECUTE` sobre `sp_agendar_cita`. La matriz de hoy no es definitiva, es la primera version de un documento que el PI va a revisar dos veces mas.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. El motor de la plataforma es PostgreSQL (PGlite en el navegador), no Oracle.
