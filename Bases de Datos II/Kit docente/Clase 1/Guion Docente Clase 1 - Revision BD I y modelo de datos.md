# Guion docente · Clase 1 · Revision BD I · Arranque de la base de datos

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Arranque PI: dominio, alcance y borrador ER de VetCare DB
- **Entregable de hoy:** Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion
- **Herramienta:** draw.io + DB Fiddle
- **Slides:** Clases/Clase 1 - Revision BD I y modelo de datos/Presentacion.pptx
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

QUÉ ES (dilo así): Hoy no se repite Bases de Datos I: se arranca la base de datos de una clínica veterinaria que hoy trabaja en papel. Vamos a decidir qué tablas tiene, cómo se identifica cada fila y qué reglas defiende el motor por sí solo, y a dejar el modelo en dos formas que deben coincidir: el diagrama y el CREATE TABLE.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema y la herramienta. Pregunta de arranque: «¿qué pasa en una clínica cuando se pierde la ficha de un paciente?». Deja que respondan 1-2 personas.
- Cierre del encuadre: «Al final de hoy van a poder decir por qué una cita no puede apuntar a una mascota que no existe, y por qué eso todavía no basta».

CUIDADO: Las herramientas son gratuitas y corren en el navegador: nadie tiene que instalar nada hoy. Si alguien no tiene cuenta en ningún lado, DB Fiddle funciona sin registrarse.

PASA A LA SIGUIENTE: Este es el recorrido de las dos horas.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): Las dos horas en cinco tramos: encuadre, teoría con una lámina por concepto, demo en vivo, práctica opcional y cierre.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica tiene su guía en la carpeta de la clase y es opcional.

PASA A LA SIGUIENTE: Antes de dibujar una tabla, conozcamos para quién la dibujamos.

### [Slide 4] El cliente: una clínica veterinaria en papel

QUÉ ES (dilo así): Toda base de datos se diseña para alguien. Nuestro cliente es una clínica veterinaria de Cali con unas 150 citas diarias, 16 veterinarios y cerca de 5.000 mascotas de 2.000 dueños, y todo vive en carpetas. El semestre entero construye la capa de datos de esa clínica: no la aplicación ni las pantallas, sino el esquema, sus reglas, sus permisos y su rendimiento.

CÓMO DARLA (≈4 min):
- Al entrar: Arriba, los tres dolores, y conecta cada uno con una decisión del curso: la ficha perdida se resuelve con una fila que tiene clave primaria (hoy); las filas en la sala de espera, con índices (Clase 7); la falta de métricas, con consultas agregadas (Clase 6). Abajo, las tres personas y lo que quiere cada una, y el recuadro del conflicto: «un campo más en el formulario de la cita le da métricas al dueño y le suma clics a la recepcionista».

EJEMPLO: ¿Guardamos la raza de la mascota? Al dueño le sirve para saber qué razas atiende más; a la recepcionista le cuesta un campo más por cita; al veterinario le sirve en la consulta. Se guarda en mascota, una sola vez, y no en cada cita.

SI PREGUNTAN:
- «¿Esta columna sobra?» → Responde con otra pregunta: ¿cuál de las tres personas la necesita, y qué pierde otra si la agregamos? Así se decide un modelo, no se copia.
- «¿Tenemos que hacer la aplicación?» → No. En esta materia se construye la base de datos: tablas, reglas, roles, procedimientos y rendimiento. La aplicación es de otra materia.

CUIDADO: El modelo tiene 8 entidades (dueño, mascota, veterinario, cita, consulta, insumo, factura, detalle de factura) y 3 reglas que vuelven todo el semestre: una mascota inactiva no agenda, el stock nunca queda negativo y todo cambio de estado de una cita queda registrado. Nómbralas hoy aunque se resuelvan después.

PASA A LA SIGUIENTE: ¿Por qué esto no es repetir Bases de Datos I? Por el vocabulario con que vamos a decidir.

### [Slide 5] Por que esto no es Bases de Datos I, y el vocabulario minimo

QUÉ ES (dilo así): En Bases de Datos I el objetivo era escribir la consulta que devuelve el resultado correcto. Aquí el objetivo es diseñar un esquema que siga siendo correcto cuando lo usen tres personas distintas, cuando tenga cien mil filas y cuando alguien meta datos malos. Para decidir eso hacen falta tres palabras precisas: tabla, fila y columna con su dominio.

CÓMO DARLA (≈3 min):
- Al entrar: La tabla mascota con tres filas: «una tabla guarda cosas de un solo tipo; aquí no hay dueños ni citas, solo mascotas».
- Clic 1: Se marca la fila de Luna: «una fila es UNA mascota concreta; si la misma mascota apareciera en dos filas, ya no sabríamos cuál es la verdadera».
- Clic 2: Se marca la columna especie y aparece su dominio: «una columna no acepta cualquier cosa; especie solo admite cuatro valores, y eso lo puede vigilar el motor».

EJEMPLO: Si alguien escribe especie = 'Perro' en vez de 'Canino', el dato parece correcto pero rompe el conteo de especies del mes. El dominio cerrado es lo que evita eso.

SI PREGUNTAN:
- «¿Dominio no era el tema del proyecto?» → La palabra tiene dos usos: el dominio de un atributo (sus valores legales) y el dominio del problema (la clínica). Hoy se usan los dos; aclara cuál.

CUIDADO: Sobre estas tres nociones se monta el semestre: los permisos de la Clase 2 se dan sobre tablas, las validaciones de la Clase 3 miran columnas y los índices de la Clase 7 se crean sobre columnas concretas.

PASA A LA SIGUIENTE: El mismo modelo se puede mirar de dos maneras: como negocio y como tablas.

### [Slide 6] Nivel conceptual y nivel fisico: dos vistas del mismo modelo

QUÉ ES (dilo así): Hay dos niveles que se mezclan. El conceptual nombra entidades y relaciones con palabras del negocio, sin decir nada del motor. El físico convierte eso en tablas con columnas tipadas, restricciones y claves. No son dos modelos: es el mismo modelo visto de dos formas, y por eso hoy se producen dos artefactos que deben coincidir.

CÓMO DARLA (≈3 min):
- Al entrar: Arriba, el nivel conceptual: dos cajas, dueño y mascota, y el verbo «posee». «Esto lo entiende la administradora de la clínica; no hay un solo tipo de dato».
- Clic 1: Abajo aparecen las tablas dueno y mascota con sus columnas: id_dueno SERIAL PK, telefono VARCHAR(30) NOT NULL, id_dueno INT FK → dueno. «Esto ya lo entiende el motor».
- Clic 2: Las flechas punteadas unen cada caja con su tabla: «dos vistas del MISMO modelo; el diagrama ER es la vista conceptual y el CREATE TABLE la física».

EJEMPLO: «Dueño posee mascota» en el diagrama se convierte en la columna mascota.id_dueno con REFERENCES dueno(id_dueno) en el DDL.

SI PREGUNTAN:
- «¿Por qué el diagrama debe llevar tipos y longitudes si es conceptual?» → Porque el criterio de completitud es que alguien pueda escribir el CREATE TABLE mirándolo sin preguntar. Sin tipos, el diagrama no se puede traducir.

CUIDADO: No presentes el diagrama y el DDL como dos tareas separadas: si un nombre cambia entre los dos, ya no son el mismo modelo.

PASA A LA SIGUIENTE: Veamos el modelo mínimo de la clínica en su vista conceptual.

### [Slide 7] ER minimo de la clinica (con cardinalidad)

QUÉ ES (dilo así): Este es el corazón del modelo: dueño, mascota, cita y veterinario, unidos por tres relaciones uno a muchos. La regla que se lee aquí es que la clave foránea vive siempre en la tabla del lado «muchos».

CÓMO DARLA (≈2 min):
- Al entrar: Lee las relaciones en voz alta: un dueño tiene N mascotas, una mascota tiene N citas, un veterinario atiende N citas. Señala dónde quedó cada FK: mascota lleva id_dueno y cita lleva id_mascota (y también id_veterinario, que el diagrama abrevia).
- Después: Lee la nota de abajo: la PK identifica cada fila y la FK materializa la relación; el motor rechaza una cita con id_mascota 999 si esa mascota no existe.

EJEMPLO: Luna (id_mascota 10) pertenece a Ana Pérez (id_dueno 1): la fila de Luna guarda id_dueno = 1. Ana no guarda nada de Luna.

SI PREGUNTAN:
- «¿Por qué la FK no va en dueño, con la lista de sus mascotas?» → Porque una celda no guarda listas (primera forma normal) y porque un dueño puede tener cualquier número de mascotas. El lado N es el que tiene una sola referencia por fila.

PASA A LA SIGUIENTE: Ese diagrama, escrito como DDL: la tabla que depende de cita.

### [Slide 8] El DDL minimo que sostiene el ER

QUÉ ES (dilo así): La misma información del diagrama, ahora en físico, sobre la tabla consulta. Muestra las tres piezas que toda tabla del curso tiene: clave primaria, clave foránea y una regla de negocio con CHECK.

CÓMO DARLA (≈3 min):
- Línea 2: id_consulta SERIAL PRIMARY KEY: la base genera el número y ninguna consulta se repite.
- Líneas 3-4: id_cita INT NOT NULL UNIQUE REFERENCES cita: NOT NULL porque no hay consulta sin cita, REFERENCES porque la cita debe existir, y UNIQUE porque una cita tiene a lo sumo una consulta. Eso convierte la relación en 1:1.
- Líneas 5-7: diagnostico obligatorio y precio NUMERIC(12,2) con CHECK (precio >= 0): la primera regla de negocio que defiende el motor.

EJEMPLO: Una segunda consulta para la cita 2 falla con «duplicate key value violates unique constraint "consulta_id_cita_key"», y un precio de −5 con «violates check constraint "consulta_precio_check"».

SI PREGUNTAN:
- «¿Por qué no pongo id_consulta dentro de cita?» → Porque una cita programada todavía no tiene consulta: la columna quedaría vacía en la mayoría de filas. La FK va en la tabla que depende.

CUIDADO: La relación cita-consulta es 1:1 pero no simétrica: la cita existe sin consulta; la consulta no existe sin cita.

PASA A LA SIGUIENTE: El mismo patrón, completo, sobre la tabla de veterinarios.

### [Slide 9] El patron de tabla: PK, obligatorios y dominio cerrado

QUÉ ES (dilo así): Este es el molde de cualquier tabla del curso, aplicado a veterinario: clave sustituta, dato natural con UNIQUE, columnas obligatorias, un dominio cerrado con CHECK y la baja lógica con DEFAULT.

CÓMO DARLA (≈2 min):
- Líneas 3-4: id_veterinario SERIAL es la clave sustituta; tarjeta_prof es la natural: UNIQUE para que no se repita, pero puede faltar.
- Líneas 5-7: nombre y especialidad son NOT NULL; especialidad solo acepta 'GENERAL', 'CIRUGIA' o 'DERMATOLOGIA'.
- Líneas 8-9: activo CHAR(1) DEFAULT 'S' con CHECK: si no se dice nada, el veterinario nace activo, y nunca se borra: se marca 'N'.

EJEMPLO: INSERT INTO veterinario (nombre, especialidad) VALUES ('Laura Restrepo', 'GENERAL'); crea el id 1, con activo = 'S' y tarjeta_prof nula.

SI PREGUNTAN:
- «¿UNIQUE deja tener varios veterinarios sin tarjeta?» → Sí: en PostgreSQL dos NULL no se consideran iguales, así que UNIQUE admite varios nulos. Lo que no admite es la misma tarjeta dos veces.

CUIDADO: El CHECK distingue mayúsculas: 'Cirugia' no es 'CIRUGIA' y se rechaza con «violates check constraint "veterinario_especialidad_check"». Decide el formato del dominio y úsalo igual en todos los INSERT.

PASA A LA SIGUIENTE: Con las tablas unidas por FK, la consulta típica las recorre con JOIN.

### [Slide 10] El JOIN de tres tablas

QUÉ ES (dilo así): La consulta más común del sistema: la agenda con el nombre de la mascota y de su dueño. Cada JOIN sigue una clave foránea del diagrama: cita llega a mascota por id_mascota, y mascota llega a dueño por id_dueno.

CÓMO DARLA (≈3 min):
- Líneas 1-4: Las columnas que se muestran, con alias: m.nombre AS mascota y d.nombre AS dueno, porque las dos tablas tienen una columna nombre.
- Líneas 5-7: FROM cita y dos JOIN, cada uno con su ON sobre la FK.
- Líneas 8-10: El WHERE filtra después de unir: citas desde el 1 de septiembre y solo mascotas activas; ORDER BY por fecha y hora.

EJEMPLO: Con los datos de práctica (10 citas, ninguna de Rocky ni de Kiara, que están inactivas) devuelve 10 filas; la primera es Firulais, de Ana Gomez, el 1 de septiembre a las 08:00.

SI PREGUNTAN:
- «¿Da lo mismo poner m.activa = 'S' en el WHERE o en el ON?» → Con JOIN interno, sí. Con LEFT JOIN no: en el ON conserva la cita con la mascota en nulo; en el WHERE la elimina.

CUIDADO: Lee bien la leyenda: el producto cartesiano sale con la coma (FROM cita c, mascota m sin la condición da 10 × 8 = 80 filas) o con CROSS JOIN; con JOIN sin ON, PostgreSQL responde error de sintaxis. El riesgo real es un ON equivocado, que no da error y devuelve filas que no corresponden.

PASA A LA SIGUIENTE: Cada JOIN se apoya en una clave primaria. ¿Cuál columna debe serlo?

### [Slide 11] Clave primaria: natural o sustituta

QUÉ ES (dilo así): Toda tabla necesita una clave primaria: la columna que identifica una fila sin ambigüedad. Eso no se discute; lo que se decide es cuál. La natural es un dato del mundo real; la sustituta es un número sin significado que genera la base. En la clínica gana la sustituta, y el dato natural se guarda aparte con UNIQUE.

CÓMO DARLA (≈3 min):
- Al entrar: Arriba, la definición: no se repite y no admite nulos. «No es estilo: el motor lo revisa en cada INSERT y UPDATE». Pregunta: «¿cuál columna de dueño usarían?».
- Clic 1: La natural, cédula o microchip, y sus tres fallas en la clínica: el dueño llega sin la cédula a la mano, el microchip se digita mal y hay que corregirlo, y la mascota rescatada no tiene microchip.
- Clic 2: La sustituta: la genera la base, no significa nada y nunca se corrige. Lee la regla de abajo y aclara que es convención de oficio, no regla del motor.

EJEMPLO: dueno(id_dueno SERIAL PRIMARY KEY, cedula VARCHAR(20) UNIQUE, ...): la cédula no se repite, puede quedar nula un rato y se corrige sin tocar las mascotas, que apuntan a id_dueno.

SI PREGUNTAN:
- «¿La clave primaria tiene que ser la primera columna y autoincremental?» → No. El orden de las columnas no le importa al motor, y el autoincremento es solo una forma cómoda de generar valores sustitutos.
- «¿La natural no ahorra un JOIN?» → Sí, cuando se busca por ella. Pero si cambia, hay que corregirla en todas las tablas que la referencian; la sustituta nunca cambia.

CUIDADO: No digas que la natural «está mal»: es válida cuando el dato es estable y lo controla la propia organización. La regla es sobre quién controla el valor.

PASA A LA SIGUIENTE: Elegida la clave, el siguiente error clásico es repetir datos. Primero la enfermedad.

### [Slide 12] Normalizacion 1FN-3FN: primero la enfermedad

QUÉ ES (dilo así): Normalizar se entiende mejor empezando por el problema. Si un dato se guarda repetido, la base puede contradecirse, no puede registrar cosas que existen y pierde datos al borrar otros. Las tres formas normales son la cura: cada dato vive una sola vez, en la tabla de la que depende.

CÓMO DARLA (≈5 min):
- Al entrar: La tabla mal diseñada: cada cita guarda el nombre y el teléfono del dueño. «Ana Pérez aparece dos veces, con su teléfono dos veces».
- Clic 1: Actualización: Ana cambia de teléfono y solo se corrige una cita. «¿Cuál es su teléfono? La base guarda dos verdades».
- Clic 2: Inserción: un dueño nuevo que todavía no pide cita no se puede registrar, porque su teléfono solo vive en cita.
- Clic 3: Borrado: se borra la única cita de Luis Mora y su teléfono desaparece con ella.
- Clic 4: La cura: dueno(id_dueno, nombre, telefono) y cita con la referencia al dueño. El teléfono vive una vez.

EJEMPLO: Las tres formas, con la clínica: 1FN, nada de listas en una celda (dos teléfonos juntos van a otra tabla); 2FN, en detalle_factura el nombre del insumo depende solo de id_insumo y sale a insumo, pero el precio unitario se queda porque es el precio del día de la venta; 3FN, la especialidad del veterinario no se guarda en cita: depende de id_veterinario.

SI PREGUNTAN:
- «Si la pantalla muestra todo junto, ¿por qué no una sola tabla?» → Por costo: el teléfono de un dueño con veinte citas viviría veinte veces y bastaría una actualización parcial para que el sistema mienta.
- «¿El precio_unit de detalle_factura no es redundante?» → No: es el precio histórico. Si se recalculara con el precio actual, reimprimir una factura de hace seis meses daría otra cifra.

CUIDADO: No dictes 1FN-2FN-3FN como una escalera de definiciones sin mostrar una anomalía concreta: el grupo termina normalizando por ritual y partiendo tablas que nunca se consultan por separado.

PASA A LA SIGUIENTE: Al separar tablas, alguien tiene que garantizar que las referencias apunten a algo real: la clave foránea.

### [Slide 13] Clave foranea, borrado y por que la FK no basta

QUÉ ES (dilo así): La clave foránea hace que el motor se niegue a guardar una referencia inventada. Esa es la mitad que todos conocen. La otra mitad es qué pasa cuando se intenta borrar la fila a la que otros apuntan: eso se decide al declarar la FK, y si no se decide, el estándar impide el borrado.

CÓMO DARLA (≈3 min):
- Al entrar: Dos tablas: las citas apuntan a mascotas que existen (1 y 2). «La flecha es la FK: cita.id_mascota debe existir en mascota».
- Clic 1: El INSERT con id_mascota 999: el motor lo rechaza y nombra la restricción violada, cita_id_mascota_fkey. Nada se insertó.
- Clic 2: El DELETE de la mascota 1, que tiene citas: rechazado. «Sin cláusula ON DELETE el comportamiento es restrictivo; eso es regla del estándar SQL, no una costumbre».

EJEMPLO: Decisión por relación: mascota → dueño, restrictiva (borrar un dueño no puede evaporar el historial); consulta → cita, restrictiva; detalle_factura → factura, CASCADE (una línea no significa nada sin su factura); detalle_factura → insumo, restrictiva (no se borra un insumo ya facturado).

SI PREGUNTAN:
- «¿Qué diferencia hay entre RESTRICT y NO ACTION?» → Las dos impiden borrar el padre con hijos. NO ACTION, la opción por omisión, revisa al final de la sentencia y puede diferirse; RESTRICT revisa de inmediato. Para este curso se comportan igual.

CUIDADO: CASCADE en mascota → dueño parece cómodo y es peligroso: un DELETE de un dueño se llevaría sus mascotas y, en cadena, sus citas y su historia clínica.

PASA A LA SIGUIENTE: Veamos cómo se declara la FK con su comportamiento al borrar.

### [Slide 14] La clave foranea y que pasa al borrar el padre

QUÉ ES (dilo así): Dos cosas en un mismo código: la tabla insumo con sus reglas, y una FK agregada después con ALTER TABLE, donde se declara explícitamente qué pasa al borrar el insumo referenciado.

CÓMO DARLA (≈2 min):
- Líneas 1-6: insumo: stock entero, por defecto 0 y nunca negativo (CHECK stock >= 0); precio_unit mayor que cero.
- Líneas 8-9: El comentario: si no se declara, PostgreSQL asume NO ACTION y se niega a borrar.
- Líneas 10-13: ALTER TABLE detalle_factura ADD CONSTRAINT fk_detalle_insumo ... ON DELETE RESTRICT: el nombre de la restricción lo elegimos nosotros y es el que aparecerá en el mensaje de error.

EJEMPLO: Con un insumo ya facturado, DELETE FROM insumo WHERE id_insumo = 1 responde: «update or delete on table "insumo" violates RESTRICT setting of foreign key constraint "fk_detalle_insumo" on table "detalle_factura"».

SI PREGUNTAN:
- «¿Por qué ponerle nombre a la restricción?» → Porque el nombre sale en el error: fk_detalle_insumo dice qué se violó; un nombre automático obliga a buscarlo en el catálogo.

CUIDADO: El CHECK (stock >= 0) de esta tabla es el que la Clase 4 retira a propósito en su demo; aquí queda como la primera defensa del stock.

PASA A LA SIGUIENTE: Y así se ve, palabra por palabra, el error que devuelve el motor.

### [Slide 15] Integridad referencial: el error que devuelve el motor

QUÉ ES (dilo así): Integridad referencial en vivo: el mismo INSERT funciona con una mascota que existe y falla con una que no. Lo importante es aprender a leer el mensaje del motor.

CÓMO DARLA (≈2 min):
- Líneas 2-4: Cita para la mascota 1, que existe: INSERT 0 1, una fila insertada.
- Líneas 6-10: Cita para la mascota 999: el error dice la tabla (cita), la restricción (cita_id_mascota_fkey) y, en DETAIL, la clave que falta: (id_mascota)=(999) no está en mascota.

EJEMPLO: Después del error, SELECT COUNT(*) FROM cita muestra el mismo número que antes del segundo INSERT: la sentencia que falla no deja nada.

SI PREGUNTAN:
- «¿De dónde sale el nombre cita_id_mascota_fkey?» → PostgreSQL lo arma solo cuando la FK no tiene nombre: tabla, columna y el sufijo fkey.

PASA A LA SIGUIENTE: Ahora, por qué en un sistema real casi nunca se borra una mascota.

### [Slide 16] Baja logica: activa CHAR(1) en vez de DELETE

QUÉ ES (dilo así): Una mascota que ya no viene no se borra: se marca como inactiva. Borrar falla por integridad, destruye el historial y es irreversible; marcar conserva todo y se puede deshacer. La consecuencia importante es que la regla «una mascota inactiva no agenda» ya no la defiende la FK.

CÓMO DARLA (≈3 min):
- Al entrar: Izquierda, el borrado físico: Luna tiene citas, consultas y facturas colgando. Tres problemas: la integridad lo impide, se pierde la historia y es irreversible.
- Clic 1: Derecha, la baja lógica: UPDATE mascota SET activa = 'N'. Las referencias siguen válidas, el historial queda intacto y se revierte con activa = 'S'.
- Clic 2: Abajo, cómo se declara (activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N'))), que las consultas del día filtran WHERE activa = 'S', y el aviso: para la FK la mascota inactiva sigue existiendo.

EJEMPLO: UPDATE mascota SET activa = 0 WHERE id_mascota = 2; falla con «violates check constraint "mascota_activa_check"»: los valores son 'S' y 'N', no 0 y 1.

SI PREGUNTAN:
- «Entonces, ¿quién impide agendar a una mascota inactiva?» → Un CHECK no puede (mira solo su propia fila, y activa vive en otra tabla). Lo resuelve un procedimiento almacenado (Clase 3) o un trigger (Clase 4).

CUIDADO: Si el grupo sale de hoy pensando en DELETE, en la Clase 3 no va a entender para qué se valida «mascota activa» antes de agendar.

PASA A LA SIGUIENTE: Comprobémoslo con código: la FK acepta la cita de una mascota inactiva.

### [Slide 17] Lo que el DDL NO puede defender solo

QUÉ ES (dilo así): El código demuestra el límite del DDL: después de dar de baja a la mascota 1, el motor acepta una cita nueva para ella. La FK garantiza que el identificador existe, no que el negocio lo quiera.

CÓMO DARLA (≈3 min):
- Línea 2: UPDATE mascota SET activa = 'N' WHERE id_mascota = 1: la baja lógica.
- Líneas 4-6: El INSERT de una cita para la mascota 1: INSERT 0 1. El motor la acepta porque la mascota 1 existe.
- Líneas 8-10: Un CHECK tampoco sirve: solo mira columnas de su propia fila, y activa está en mascota, no en cita. Hace falta un procedimiento (Clase 3) o un trigger (Clase 4).

EJEMPLO: Con los datos de práctica, el riesgo se mide con una consulta: citas no canceladas cuya mascota tiene activa = 'N'. Hoy da 0 filas; mañana puede no darlo.

SI PREGUNTAN:
- «¿Y si pongo la columna activa también en cita?» → Sería un dato repetido: se desincroniza en cuanto cambie la mascota (la anomalía de actualización de hace un rato).

CUIDADO: Las tres reglas del modelo se reparten así: «stock nunca negativo» sí cabe en un CHECK; «mascota inactiva no agenda» y «todo cambio de estado queda registrado» necesitan lógica programada.

PASA A LA SIGUIENTE: Volvamos al diagrama: ¿qué lo hace un diagrama y no un dibujo?

### [Slide 18] Que separa un diagrama ER de un dibujo

QUÉ ES (dilo así): Es fácil dibujar cajas y creer que eso es un modelo. Un diagrama entidad-relación bien hecho cumple cinco condiciones que se pueden revisar una por una, y tiene una prueba de aceptación muy simple: alguien más debe poder escribir el CREATE TABLE con solo mirarlo.

CÓMO DARLA (≈3 min):
- Al entrar: El dibujo: «Dueños» y «Mascotas» unidos por una línea. «¿Qué tipo tiene el teléfono? ¿Cuántas mascotas puede tener un dueño? El dibujo no lo dice».
- Clic 1: El mismo modelo como diagrama: dueno y mascota en singular, PK y FK marcadas, atributos con tipo, cardinalidad 1..1 y 0..N y el verbo «posee».
- Clic 2: Las cinco condiciones, una por una; detente en la 4: el mínimo dice si la relación es obligatoria (0..N: un dueño puede no tener mascotas aún).
- Clic 3: La prueba de aceptación: otra persona escribe el CREATE TABLE mirándolo, sin preguntar.

EJEMPLO: Cita y consulta son 1 a 1 pero no simétricas: una cita programada aún no tiene consulta, y una consulta no existe sin su cita. Eso se materializa como consulta.id_cita NOT NULL UNIQUE.

SI PREGUNTAN:
- «¿Cuánto debe ocupar el diagrama?» → El modelo completo tiene 8 entidades y 7 relaciones y cabe legible en una hoja. Si no cabe, se divide por subsistemas (convención, no norma).

CUIDADO: No aceptes un diagrama sin cardinalidades ni tipos «porque se ve ordenado»: la decisión que falta (¿un veterinario puede tener dos citas en la misma franja?) reaparece cuando ya hay datos y procedimientos escritos encima.

PASA A LA SIGUIENTE: La condición 2 pide tipos: elegirlos mal es donde se pagan las facturas más caras.

### [Slide 19] Tipos de datos: donde se pagan las facturas mas caras

QUÉ ES (dilo así): Elegir el tipo parece trivial y es donde se pagan los errores más caros, porque cambiarlo después obliga a convertir datos que ya existen. Hay tres casos clásicos: teléfono, fecha y dinero, y una tentación contraria, declarar todo como texto largo.

CÓMO DARLA (≈3 min):
- Al entrar: Teléfono: como NUMERIC se pierden el 0 inicial, el + del prefijo y la extensión. Va VARCHAR(30).
- Clic 1: Fecha: como VARCHAR(20), ORDER BY ordena como palabras y no se pueden sumar 30 minutos para calcular el fin de la cita. Va TIMESTAMP.
- Clic 2: Dinero: FLOAT guarda decimales en binario; 0.1 + 0.2 no da exactamente 0.3 y el total deja de cuadrar con sus líneas. Va DECIMAL(12,2), que en PostgreSQL es lo mismo que NUMERIC(12,2).
- Clic 3: La tentación contraria: todo VARCHAR(4000). La base ya no valida nada y cada pantalla tiene que hacerlo por su cuenta.

EJEMPLO: En PostgreSQL, SELECT 0.1::float8 + 0.2::float8 = 0.3::float8 devuelve false; con NUMERIC devuelve true. Y ordenar como texto las fechas '2026-10-02' y '2026-9-15' pone la de septiembre después de la de octubre.

SI PREGUNTAN:
- «¿Por qué email VARCHAR(120) y no 50?» → Porque el estándar de correo admite direcciones de hasta 254 caracteres; 120 cubre los casos reales. Son números de convención del curso: nombre 80, teléfono 30, especie 40.

CUIDADO: Si vienes de Oracle: allí el dinero es NUMBER(12,2); en PostgreSQL NUMBER no existe, se escribe NUMERIC o DECIMAL.

PASA A LA SIGUIENTE: Además del tipo, el nombre: una mayúscula puede costar veinte minutos.

### [Slide 20] Convenciones de nombres para que el DDL corra a la primera

QUÉ ES (dilo así): PostgreSQL convierte a minúsculas cualquier nombre escrito sin comillas. Por eso la regla del curso es simple: todo en minúsculas, singular, sin tildes y sin comillas dobles, y el mismo nombre en el diagrama, en el DDL y en el código Mermaid.

CÓMO DARLA (≈3 min):
- Al entrar: CREATE TABLE Mascota crea una tabla llamada mascota: el motor pliega el nombre a minúscula.
- Clic 1: SELECT * FROM "Mascota" falla: con comillas el nombre se toma letra a letra y esa tabla no existe. Error real: relation "Mascota" does not exist.
- Clic 2: Las cuatro reglas con su ejemplo: mascota, dueno, detalle_factura, y la FK que se lee sola: cita.id_mascota apunta a mascota.id_mascota.

EJEMPLO: El error al revés también existe: CREATE TABLE "Mascota" con comillas y luego SELECT * FROM mascota responde relation "mascota" does not exist.

SI PREGUNTAN:
- «¿Por qué singular si la tabla guarda muchas mascotas?» → Porque se nombra por lo que guarda cada fila, y así la FK se lee sola: cita.id_mascota.
- «¿Por qué sin eñe?» → Funciona en PostgreSQL, pero complica escribirla en otros teclados, herramientas y motores. dueno se escribe igual en cualquier parte.

CUIDADO: El patrón de identificadores es id_<entidad>, con el mismo nombre en la tabla propia y en la que la referencia: así el JOIN se escribe sin buscar cómo se llamó la columna.

PASA A LA SIGUIENTE: Con qué herramientas se hace todo esto hoy, y qué demuestra cada una.

### [Slide 21] Herramientas del dia y que se puede demostrar con cada una

QUÉ ES (dilo así): Tres herramientas gratuitas, cada una responde una pregunta: ¿cómo es el modelo? (draw.io o Excalidraw), ¿el DDL corre? (DB Fiddle, que es PostgreSQL real en el navegador) y ¿el diagrama se dibuja? (un visor Mermaid).

CÓMO DARLA (≈2 min):
- Al entrar: Recorre las tres cajas de arriba abajo; en la del medio señala el ejemplo: la cita con la mascota 999 y el error de FK que se lee en vivo. Cierra con el recuadro: DB Fiddle recrea el esquema en cada ejecución, así que lo que vale es el archivo .sql guardado en la carpeta del proyecto.

EJEMPLO: La prueba de que el .sql está completo: abrir DB Fiddle vacío, pegar el archivo y reconstruir el esquema con sus datos en menos de cinco minutos.

SI PREGUNTAN:
- «¿Y Oracle Live SQL?» → Solo como contraste de sintaxis para quien encuentre Oracle en el trabajo. El motor del curso es PostgreSQL.

CUIDADO: DB Fiddle no tiene usuarios ni roles reales; los permisos de la Clase 2 se practican en PostgreSQL en el navegador con SET ROLE.

PASA A LA SIGUIENTE: La tercera herramienta merece su lámina: del ER dibujado al código Mermaid.

### [Slide 22] Del ER dibujado al codigo Mermaid

QUÉ ES (dilo así): El diagrama del curso se guarda como texto Mermaid, no como imagen. No hace falta dibujar escribiendo código: se piensa en un boceto, una IA traduce la sintaxis y uno revisa que el modelo sea el suyo. Al final se comprueba en un visor que se dibuje.

CÓMO DARLA (≈3 min):
- Al entrar: El camino: boceto en draw.io o Excalidraw, la IA traduce, sale texto erDiagram.
- Clic 1: El texto: dueno ||--o{ mascota : posee se lee «un dueño posee cero o muchas mascotas»; dentro de dueno { } van los atributos con su tipo y PK.
- Clic 2: La revisión: entidades completas, cardinalidad en el sentido correcto, PK y FK marcadas. «La IA acierta la sintaxis, no tu modelo».
- Clic 3: El visor dibuja el diagrama. Si no renderiza, se corrige ahí mismo.

EJEMPLO: En ||--o{ cada lado es un extremo: || es «exactamente uno» del lado de dueno y o{ es «cero o muchos» del lado de mascota.

SI PREGUNTAN:
- «¿Puedo entregar el PNG en vez del texto?» → El PNG sirve para un informe, pero la fuente es el texto: es lo que se corrige, se versiona y se compara con el DDL.

CUIDADO: Los nombres del erDiagram deben ser los del DDL: dueno y mascota en minúscula, no DUENO ni Dueños. Si difieren, ya no es el mismo modelo.

PASA A LA SIGUIENTE: Vamos a la demo: todo esto en vivo.

### [Slide 23] Demo del dia

QUÉ ES (dilo así): La demo junta lo de hoy: un boceto, el DDL que corre en PostgreSQL, el error de integridad leído en vivo y el mismo modelo pasado a Mermaid.

CÓMO DARLA (≈15 min):
- Al entrar: 1) Boceto en draw.io: dueño, mascota y cita con sus claves (3 min). 2) En DB Fiddle, el DDL de las tres tablas con PK, FK y CHECK, y los INSERT de Ana Pérez, la perra Luna y su cita; corre el JOIN (5 min). 3) Inserta una cita con la mascota 999 y lee el error en voz alta: tabla, restricción y DETAIL (2 min). 4) Pide a una IA el erDiagram del boceto, pégalo en el visor y compara nombres con el DDL (5 min).

CUIDADO: Lleva el script de la demo en un archivo .sql y pégalo: escribirlo en vivo consume el tiempo de la parte que importa, que es leer el error. Y si la IA devuelve DUENO en mayúsculas, corrígelo frente al grupo: es justo el punto de la lámina de convenciones.

PASA A LA SIGUIENTE: Los cuatro pasos del boceto al código quedan proyectados para la práctica.

### [Slide 24] Del boceto al código Mermaid

QUÉ ES (dilo así): Los cuatro pasos para pasar de un diagrama dibujado a uno en texto Mermaid. Quedan proyectados mientras el grupo trabaja.

CÓMO DARLA (≈2 min):
- Al entrar: Léelos en orden y subraya dos: en el 2, la IA acierta la sintaxis pero el modelo lo revisa cada uno; en el 4, lo que se guarda es el texto Mermaid (la fuente), y el PNG es solo para el informe.

CUIDADO: Si alguien pega el código y el visor marca error, casi siempre es un nombre con espacio o tilde, o un atributo sin tipo.

PASA A LA SIGUIENTE: Cerramos.


**Demo que usted debe poder repetir:** Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 1 - Revision BD I y modelo de datos/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 1 · Revision BD I · Arranque de la base de datos
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. El cliente: una clínica veterinaria en papel
5. Por que esto no es Bases de Datos I, y el vocabulario minimo
6. Nivel conceptual y nivel fisico: dos vistas del mismo modelo
7. ER minimo de la clinica (con cardinalidad)
8. El DDL minimo que sostiene el ER
9. El patron de tabla: PK, obligatorios y dominio cerrado
10. El JOIN de tres tablas
11. Clave primaria: natural o sustituta
12. Normalizacion 1FN-3FN: primero la enfermedad
13. Clave foranea, borrado y por que la FK no basta
14. La clave foranea y que pasa al borrar el padre
15. Integridad referencial: el error que devuelve el motor
16. Baja logica: activa CHAR(1) en vez de DELETE
17. Lo que el DDL NO puede defender solo
18. Que separa un diagrama ER de un dibujo
19. Tipos de datos: donde se pagan las facturas mas caras
20. Convenciones de nombres para que el DDL corra a la primera
21. Herramientas del dia y que se puede demostrar con cada una
22. Del ER dibujado al codigo Mermaid
23. Demo del dia
24. Del boceto al código Mermaid
25. Cierre · Clase 1

> Privado, no se proyecta: `Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Revision BD I · Arranque de la base de datos.»
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
- Nivel conceptual = entidades y relaciones; nivel fisico = tablas con tipos y longitudes. El ER de hoy es el conceptual (Dueno posee Mascota); el CREATE TABLE de la demo es el mismo modelo en fisico (dueno.telefono VARCHAR(30)). Una tabla = conjunto de entidades del mismo tipo; cada fila es una instancia, cada columna un atributo. La clave primaria (PK) identifica sin ambiguedad cada fila: nunca se repite, nunca es nula.
- Clave foranea (FK): columna que apunta a la PK de otra tabla y materializa una relacion (1-N o N-N via tabla intermedia). Garantiza integridad referencial: la BD rechaza una Cita con id_mascota que no existe.
- Normalizacion 1FN-3FN en una frase cada una: 1FN = nada de listas dentro de una celda (una fila = una mascota, no varias); 2FN = ningun atributo depende solo de una parte de una PK compuesta; 3FN = ningun atributo depende de otro atributo que no sea la PK. Sub-normalizar genera anomalias de insercion/actualizacion/borrado (ej.: cambiar el telefono de un dueno en 5 filas distintas); sobre-normalizar multiplica JOINs sin necesidad real.
- Error de docente que no domina el tema: confundir PK con 'el primer campo de la tabla', o asumir que normalizar siempre mejora el rendimiento (en lectura intensiva a veces se denormaliza a proposito, y eso se vera en Clase 6-7).
- Dominio VetCare y sus relaciones: Dueno 1-N Mascota, Mascota 1-N Cita, Veterinario 1-N Cita, Consulta 1-1 Cita (una consulta documenta una cita atendida), Factura 1-N DetalleFactura N-1 Insumo.
- Reglas de negocio del PI que ya anticipan clases futuras: mascota inactiva no puede tener cita nueva (se validara con un procedimiento en Clase 3), stock de insumo nunca queda negativo (transacciones, Clase 8), cambios sensibles quedan auditados (triggers, Clase 4).
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 23][Slide 24]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.
Herramienta: draw.io + DB Fiddle

**Cierre la demo dentro de ExamLab** [Slide 24] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `erDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Resultado del JOIN de verificacion del ER (lo que debe salir tras los INSERT) [[captura: salida-join-clinica.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 1 - Revision BD I y modelo de datos/Taller PI - Clase 1 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Arranque PI: dominio, alcance y borrador ER de VetCare DB
Actividades:
1. Registrar el proyecto con el nombre exacto VetCare - [Apellido] (trabajo individual por defecto; equipo de 2-3 solo si el docente lo autoriza).
2. Llenar la plantilla de la ficha del PI: alcance SI / alcance NO y 3 reglas de negocio propias en formato Condicion -> Accion.
3. Dibujar el ER borrador en Excalidraw o draw.io, pasarlo a Mermaid (erDiagram) con ayuda de una IA y pegarlo renderizado en ExamLab.
4. Exportar tambien el PNG del ER a la carpeta del PI y verificar que los nombres coincidan con el DDL (minusculas, singular, id_<entidad>).
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 1/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 1 - VetCare.docx`. Clave para usted: `Quiz Clase 1 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 25]
**Decir:** «Queda visto: Revision BD I · Arranque de la base de datos. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 25] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 01_arranque_clinica.sql.

## Capturas
Carpeta `Kit docente/Clase 1/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
