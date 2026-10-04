# Guion docente · Clase 11 · Avance PI · VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Demo parcial + checklist de avance (hito formal PI)
- **Entregable de hoy:** Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
- **Herramienta:** ExamLab (PostgreSQL/PGlite) + draw.io / Mermaid
- **Slides:** Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx
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

QUÉ ES (dilo así): Hoy no hay SQL nuevo: hoy se revisa lo construido. Una revisión técnica bien hecha encuentra los defectos mientras todavía hay tiempo de corregirlos, y deja una lista escrita de qué arreglar.

CÓMO DARLA (≈4 min):
- Al entrar: Lee el tema y pregunta: «si hoy alguien abriera su base sin conocerlos, ¿qué sería lo primero que no coincide con lo que dice su diagrama?». Toma dos respuestas.
- Después: Cierra: «al final cada uno sale con su acta de hallazgos; cada hallazgo, demostrado con una ejecución».

CUIDADO: Esta sesión es doble: la Clase 11 y la 12 van el mismo día. Cuida el tiempo de la revisión para que la integración no quede comprimida.

PASA A LA SIGUIENTE: Primero, qué es una revisión técnica y con qué producto se sale.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El recorrido del bloque: teoría con una lámina por concepto, demo de una revisión real y práctica opcional.

CÓMO DARLA (≈1 min):
- Al entrar: Señala solo los tramos; no te detengas. La práctica está en la carpeta de la clase y es opcional.

### [Slide 4] Que es una revision tecnica, y con que producto se sale

QUÉ ES (dilo así): Una revisión técnica es una reunión con un solo propósito: encontrar defectos en un producto de trabajo mientras todavía es barato corregirlos, y salir con una lista escrita. No es una reunión de avance, ni una calificación, ni una demostración para lucirse.

CÓMO DARLA (≈5 min):
- Al entrar: El objetivo arriba y el artefacto al centro: puede ser el ER, el script DDL, la matriz de roles o un procedimiento. Todo gira alrededor del producto, no de quien lo hizo.
- Clic 1: Los cuatro roles: el autor presenta y responde, los revisores buscan defectos, el moderador cuida tiempo y tono, el escriba anota cada hallazgo. Entre dos personas, una hace de autor y la otra de revisor y escriba.
- Clic 2: El producto es el acta de hallazgos. Si de la reunión no sale nada escrito, no hubo revisión: hubo conversación.
- Clic 3: Las dos reglas, dichas antes de empezar: se revisa el artefacto y no la persona, y el problema no se arregla dentro de la revisión. Quien se pone a corregir el DDL en vivo consume el tiempo de todos.

EJEMPLO: El estándar IEEE 1028 distingue la inspección (formal, con lista de verificación y métricas), el walkthrough (el autor guía) y la revisión técnica (los pares evalúan si el artefacto sirve). Hoy se hace una revisión técnica con lista de verificación, de unos diez minutos por persona.

SI PREGUNTAN:
- «¿Esto tiene nota?» → La revisión no califica el producto: es la última oportunidad de mover puntos antes de la entrega. Conviene llegar con lo más flojo, no con lo mejor.
- «¿Si el revisor encuentra fallas me bajan la nota?» → No: el revisor par no califica. Encontrar fallas es el objetivo de la sesión.

CUIDADO: El error típico del docente es convertir la revisión en «va bien, faltan detalles»: amable, global y sin nada escrito. Sin acta, los defectos llegan intactos a la entrega final.

PASA A LA SIGUIENTE: ¿Qué se revisa en una base de datos? No cada pieza: la coherencia entre ellas.

### [Slide 5] Lo que se audita es la coherencia entre piezas

QUÉ ES (dilo así): En una base de datos no se audita cada pieza por separado sino la coherencia entre piezas: que todas describan el mismo sistema. Un ER bien dibujado y un DDL que ejecuta sin errores pueden describir dos bases distintas, y ninguna de las dos piezas «falla» por sí sola.

CÓMO DARLA (≈5 min):
- Al entrar: Las cinco piezas del proyecto, cada una con su visto: el ER, el DDL, la matriz de roles, los procedimientos y el informe de optimización. Revisadas solas, todas pasan.
- Clic 1: El enlace entre el ER y el DDL se rompe: el diagrama se dibujó en la Clase 1 y el DDL se parchó en las Clases 3 a 8 (una tabla de auditoría, una columna nueva) sin volver al diagrama. Es el hallazgo más común y el más fácil de encontrar si se sabe dónde mirar.
- Clic 2: Las cuatro verificaciones cruzadas, cada una entre dos piezas: el ER contra el DDL, la matriz de roles contra los GRANT, los procedimientos contra una llamada real y el informe contra el EXPLAIN de antes y después. Cada una toma dos o tres minutos.
- Clic 3: La frase de la lámina: se audita la coherencia entre piezas, no cada pieza.

EJEMPLO: La tabla audit_cita apareció en la Clase 4 con su trigger. Si el ER no la tiene, el DDL describe una base con una tabla más que el diagrama: hallazgo de coherencia, aunque las dos piezas estén bien hechas.

SI PREGUNTAN:
- «¿Y si el DDL es el correcto y el ER el viejo?» → Entonces se actualiza el ER: la fuente de verdad es lo que corre. El hallazgo es que no coinciden, no cuál de los dos tiene la culpa.

CUIDADO: No aceptes como evidencia lo que el autor dice («sí, está actualizado»): pide abrir las dos piezas lado a lado.

PASA A LA SIGUIENTE: Las dos primeras verificaciones, en detalle.

### [Slide 6] Verificaciones uno y dos: el ER contra el DDL

QUÉ ES (dilo así): La verificación uno compara el diagrama con el script en los dos sentidos y después mira las relaciones. La verificación dos compara la matriz de roles de la Clase 2 con los GRANT que de verdad se ejecutaron.

CÓMO DARLA (≈6 min):
- Al entrar: De ida: se recorre el ER entidad por entidad buscando su CREATE TABLE. Dueño, mascota y cita lo tienen; insumo no: entidad sin tabla.
- Clic 1: De vuelta: el script tiene CREATE TABLE proveedor y el ER no tiene esa entidad. El modelo creció sin registrarse, y es el sentido que nadie revisa.
- Clic 2: Las relaciones: si el ER dice que una cita pertenece a exactamente una mascota, el DDL debe tener id_mascota INT NOT NULL y REFERENCES mascota(id_mascota). Si dice que un dueño tiene varias mascotas, la clave foránea vive en mascota, no en dueño. Una cardinalidad sin restricción es decoración.
- Clic 3: Verificación dos: la matriz dice que el auditor solo lee cita, pero el script le dio GRANT SELECT, INSERT, UPDATE ON cita TO auditor. Pasa cuando se copia el bloque de recepción y solo se cambia el nombre del rol.

EJEMPLO: La consulta del catálogo que lista las claves foráneas devuelve 7 filas en la base completa del curso: una por cada relación del ER (cita con mascota y con veterinario, mascota con dueño, consulta con cita, factura con consulta y detalle_factura con factura y con insumo).

SI PREGUNTAN:
- «¿Cómo veo los privilegios reales de un rol?» → Con el catálogo: SELECT grantee, table_name, privilege_type FROM information_schema.role_table_grants WHERE grantee = 'auditor'; con el GRANT del ejemplo devuelve tres filas: INSERT, SELECT y UPDATE sobre cita.
- «¿Una FK sin NOT NULL está mal?» → Depende de la cardinalidad: sin NOT NULL la relación es opcional. Si el ER dice «exactamente una», falta el NOT NULL.

CUIDADO: Revisar solo de ida deja pasar las tablas que crecieron sin diagrama, que son justo las que la sustentación pregunta.

PASA A LA SIGUIENTE: La verificación tres separa a quien va bien de quien no: que compile no es que sirva.

### [Slide 7] Verificacion tres: que compile no es que sirva

QUÉ ES (dilo así): Las verificaciones tres y cuatro piden ejecuciones, no afirmaciones. Un procedimiento se prueba con dos llamadas: una que debe pasar y una que debe ser rechazada. Una optimización se prueba con el plan de ejecución de antes y de después.

CÓMO DARLA (≈5 min):
- Al entrar: CREATE PROCEDURE sp_agendar_cita(…) compiló. Eso solo dice que la sintaxis es correcta; todavía no se sabe si la regla funciona.
- Clic 1: Caso válido: CALL sp_agendar_cita(1, 2, …) con una mascota activa (Firulais) y una franja libre: inserta la cita.
- Clic 2: Caso inválido declarado: CALL sp_agendar_cita(3, 2, …) con Rocky, que está inactiva: el procedimiento aborta con «ERROR: la mascota 3 esta inactiva; no se agenda cita» y no inserta nada. Si el autor no puede mostrar esta segunda ejecución, el procedimiento no tiene manejo de errores.
- Clic 3: Verificación cuatro: se pide la consulta, el plan de antes (Seq Scan on cita), el cambio aplicado y el plan de después (Index Scan using idx_cita_fecha_hora on cita). Sin medición, el informe es una opinión; y un índice que ninguna consulta aprovecha se anota como hallazgo.

EJEMPLO: Un sp_agendar_cita que compila pero no valida la mascota inactiva pasa la primera llamada y también la segunda: inserta la cita de Rocky, que debía rechazarse. Solo la segunda ejecución lo delata.

SI PREGUNTAN:
- «¿Cómo confirmo que el caso inválido no dejó nada?» → Con SELECT COUNT(*) FROM cita; antes y después: el número no cambia.
- «¿El plan de después siempre muestra Index Scan?» → No necesariamente: con pocas filas el planificador puede preferir Seq Scan aunque el índice exista. Lo que se exige es la medición y que el informe explique lo que muestra.

CUIDADO: No marques en verde un procedimiento porque el autor dice que funciona: pide la ejecución del caso inválido en pantalla.

PASA A LA SIGUIENTE: Las verificaciones en SQL: el catálogo responde qué existe de verdad.

### [Slide 8] La bateria de verificacion del avance

QUÉ ES (dilo así): El catálogo de la base, information_schema, responde con datos qué tablas existen y cuáles tienen clave primaria. Así se verifica el DDL sin leerlo línea por línea.

CÓMO DARLA (≈4 min):
- Líneas 1-3: Lista las tablas del esquema public en orden alfabético. En una base con el modelo completo y la auditoría aparecen 9: audit_cita, cita, consulta, detalle_factura, dueno, factura, insumo, mascota y veterinario. Cualquier otra es una tabla sin entidad que revisar.
- Líneas 5-10: Une cada tabla con sus restricciones PRIMARY KEY mediante LEFT JOIN y se queda con las que no encontraron ninguna (c.constraint_name IS NULL).
- Línea 11: Cero filas significa que todas las tablas tienen clave primaria. Cada fila que aparezca es un hallazgo.

EJEMPLO: En la base completa del curso la segunda consulta devuelve 0 filas: todas las tablas, incluida audit_cita, tienen su clave primaria.

SI PREGUNTAN:
- «¿Por qué LEFT JOIN y no JOIN?» → Porque se buscan las tablas que NO tienen PK: un JOIN las descartaría; el LEFT JOIN las conserva con NULL en las columnas de la restricción, y el WHERE … IS NULL las deja solas.
- «¿information_schema es de PostgreSQL?» → Es del estándar SQL: también existe en MySQL y SQL Server. PostgreSQL tiene además su catálogo propio, pg_catalog.

CUIDADO: Corre las consultas sobre la base que el autor va a entregar, no sobre una copia de prueba: el catálogo describe la base en la que se ejecuta.

PASA A LA SIGUIENTE: Una revisión también encuentra lo contrario de lo que falta: lo que sobra.

### [Slide 9] Scope creep: el crecimiento no controlado del alcance

QUÉ ES (dilo así): Scope creep es el crecimiento no controlado del alcance: se agregan cosas sin decidirlo y sin quitar nada. En un proyecto de base de datos tiene un síntoma que se cuenta: el número de entidades.

CÓMO DARLA (≈4 min):
- Al entrar: El mínimo son seis entidades (dueño, mascota, veterinario, cita, insumo y factura con su detalle) y el rango sano llega a nueve con una o dos ampliaciones justificadas, como consulta o un historial clínico. El modelo del curso tiene 8 tablas: dentro del rango.
- Clic 1: Se agregan proveedores, inventario multialmacén, portal de dueños, notificaciones… y se llega a 15. Nadie decidió agregarlas y nada se quitó a cambio.
- Clic 2: Mismo esfuerzo, el doble de superficie: se termina con quince tablas vacías en vez de ocho con procedimientos probados. La acción va al acta: las sobrantes pasan a una sección de alcance futuro, con su porqué.

EJEMPLO: Un hallazgo bien escrito: «Artefacto: ER. Observación: 15 entidades, 7 sin procedimientos ni datos. Acción: mover proveedor, almacén, portal y notificación a alcance futuro.»

SI PREGUNTAN:
- «¿Mover entidades a alcance futuro no se ve mal?» → Al contrario: declarar el límite con su razón es señal de madurez y se valora al sustentar.

CUIDADO: Existe el problema inverso: quien recortó tanto que ya no tiene material para procedimientos, funciones y triggers. También se escribe como hallazgo.

PASA A LA SIGUIENTE: ¿Cómo se escribe un hallazgo para que sirva? Tiene una anatomía fija.

### [Slide 10] La anatomia fija de la retroalimentacion util

QUÉ ES (dilo así): La retroalimentación útil se escribe siempre con la misma forma, para que el acta sea una lista de tareas y no un desahogo. Cada hallazgo dice qué pieza, qué se observó, por qué importa, qué hacer y quién lo hace para cuándo.

CÓMO DARLA (≈5 min):
- Al entrar: La versión inútil: «el modelo está flojo, mejórenlo». No dice qué mirar ni cómo saber cuándo está resuelto.
- Clic 1: La versión accionable, parte por parte: artefacto, el script DDL; observación, detalle_factura no tiene FOREIGN KEY hacia insumo aunque el ER dibuja la relación; impacto, se pueden insertar detalles con insumos que no existen; acción, agregar la restricción y re-ejecutar el script completo desde cero; responsable y fecha, el autor, antes de la próxima sesión.
- Clic 2: La diferencia no es cortesía, es verificabilidad. Y la dosis: de tres a cinco hallazgos por persona; más de cinco desmoraliza y nadie los cierra, menos de tres suele ser una revisión superficial.

EJEMPLO: La observación se prueba con SQL: INSERT INTO detalle_factura (id_factura, id_insumo, cantidad, precio_unit) VALUES (1, 999, 1, 1000); si entra, falta la FK; si responde «violates foreign key constraint», el hallazgo está cerrado.

SI PREGUNTAN:
- «¿Por qué re-ejecutar todo el script desde cero?» → Porque un ALTER aplicado a mano en la base de uno no queda en el script: la prueba de que quedó es que el script completo corra limpio en una base vacía.

CUIDADO: La observación tiene que ser verificable: «la FK no existe» se comprueba; «el modelo está raro», no.

PASA A LA SIGUIENTE: ¿Y si la revisión no encuentra nada? Entonces se desperdició.

### [Slide 11] Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado

QUÉ ES (dilo así): Un punto de control intermedio solo vale si de él sale una lista de cosas por corregir mientras aún hay clases para hacerlo. Un «todo bien» no ahorra trabajo: lo aplaza al momento en que ya no se puede arreglar.

CÓMO DARLA (≈4 min):
- Al entrar: La línea del tiempo: checkpoint y entrega. Entre los dos, la franja verde es el tiempo que queda para corregir.
- Clic 1: Con hallazgos concretos: el defecto aparece en el checkpoint, se anota y se corrige dentro de esa franja.
- Clic 2: Con «todo bien, sigan así»: el estudiante entiende, con razón, que su trabajo está aprobado; deja de revisarlo y el defecto llega intacto a la entrega, cuando ya no hay tiempo. Es un costo diferido, no un ahorro.

EJEMPLO: La revisión entre pares tiene un beneficio propio: quien revisa casi siempre vuelve a su carpeta y arregla en silencio el mismo problema que acaba de señalar.

SI PREGUNTAN:
- «¿Llego con lo mejor o con lo peor?» → Con lo peor: es lo que la revisión puede arreglar. Esconder la parte floja es perder justo la ayuda que se vino a buscar.

CUIDADO: Convertir el checkpoint en una clase de repaso porque incomoda no tener tema nuevo: el tiempo se va explicando y nadie sale con su acta, que era el producto del día.

PASA A LA SIGUIENTE: Para que los hallazgos salgan de datos y no de opiniones: más consultas al catálogo.

### [Slide 12] Integridad y objetos de negocio, contados

QUÉ ES (dilo así): Dos verificaciones más con el catálogo: qué claves foráneas existen y qué procedimientos, funciones y triggers hay de verdad en la base, no en el informe.

CÓMO DARLA (≈4 min):
- Líneas 1-9: Une las restricciones FOREIGN KEY con la columna que las lleva (key_column_usage) y con la tabla a la que apuntan (constraint_column_usage). En la base completa devuelve 7 filas: cita→veterinario, cita→mascota, consulta→cita, detalle_factura→factura, detalle_factura→insumo, factura→consulta y mascota→dueno.
- Líneas 11-13: information_schema.routines lista lo que existe con su tipo: con el avance completo aparecen fn_trg_audit_cita (FUNCTION), sp_agendar_cita y sp_facturar (PROCEDURE).
- Línea 14: information_schema.triggers devuelve trg_audit_cita sobre cita. Un trigger aparece una vez por cada evento que lo dispara; este solo escucha UPDATE.

EJEMPLO: Si el informe dice «tres procedimientos» y routines devuelve dos, el tercero está en un archivo y no en la base: hallazgo.

SI PREGUNTAN:
- «¿Por qué la función del trigger aparece como FUNCTION?» → Porque en PostgreSQL el trigger son dos objetos: la función RETURNS TRIGGER, que es una rutina más, y la asociación CREATE TRIGGER, que está en information_schema.triggers.

CUIDADO: La consulta de claves foráneas une solo por nombre de restricción: una FK de dos columnas aparecería repetida. En el modelo del curso todas son de una columna.

PASA A LA SIGUIENTE: Ahora todo esto en la demo.

### [Slide 13] Demo del dia

QUÉ ES (dilo así): La demo es una revisión real de diez minutos sobre una base completa: el docente hace de revisor, ejecuta las verificaciones y escribe los hallazgos en vivo con sus cinco partes.

CÓMO DARLA (≈15 min):
- 1 · Catálogo: Ejecuta las consultas de las dos láminas de código: tablas, tablas sin PK (0 filas), claves foráneas (7) y rutinas y triggers. Compara cada resultado con el ER.
- 2 · Procedimiento: CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-11-05 10:00:00') inserta; CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-11-05 09:00:00') responde «ERROR: la mascota 3 esta inactiva; no se agenda cita». Muestra SELECT COUNT(*) FROM cita antes y después de la segunda.
- 3 · Hallazgo: Escribe un hallazgo completo en el acta, en voz alta, parte por parte. Si la base no tiene ninguno real, usa el de detalle_factura sin FK y pruébalo con el INSERT del insumo 999.
- 4 · Cierre: Muestra el acta terminada: de 3 a 5 hallazgos, cada uno con responsable y fecha.

EJEMPLO: Tiempos sugeridos: catálogo 5 min, procedimiento 4 min, hallazgo 4 min, cierre 2 min.

SI PREGUNTAN:
- «¿Y si la base del estudiante no corre?» → Ese es el primer hallazgo, y el más grave: sin un script que corra de principio a fin en una base vacía no hay sobre qué montar lo demás.

CUIDADO: No corrijas en vivo lo que encuentres: anótalo. Corregir dentro de la revisión es la regla que más se rompe.

PASA A LA SIGUIENTE: Para el ER del avance: del boceto al código Mermaid.

### [Slide 14] Del boceto al código Mermaid

QUÉ ES (dilo así): El diagrama se entrega como texto Mermaid, no como imagen: la imagen sale del código. Se piensa dibujando, se traduce a texto, se comprueba que dibuje y se guardan las dos cosas.

CÓMO DARLA (≈3 min):
- Paso 1: Diseña visual: en Excalidraw o draw.io arrastrar cajas es más rápido, y ahí se piensa el modelo.
- Paso 2: Traduce con IA: pide el código erDiagram a partir del boceto. Revisa el resultado: la IA acierta la sintaxis, no el modelo; los nombres tienen que ser los del DDL.
- Paso 3: Renderiza y corrige en un visor Mermaid (mermaid.live): si no dibuja, no comunica.
- Paso 4: Guarda el texto Mermaid, que es la fuente, y exporta el PNG.

EJEMPLO: Una relación en erDiagram: dueno ||--o{ mascota : tiene (un dueño, cero o muchas mascotas). Cada entidad lleva sus atributos con tipo y PK o FK: int id_mascota PK.

SI PREGUNTAN:
- «¿Por qué no basta una imagen del diagrama?» → Porque el texto se puede revisar, comparar con el DDL y versionar; una imagen no se corrige sin volver a dibujarla.

CUIDADO: Revisa que los nombres del erDiagram sean exactamente los del DDL (dueno, no Dueño): un diagrama que no coincide con el script es justo el hallazgo de coherencia de hoy.

PASA A LA SIGUIENTE: Cierre de la clase.


**Demo que usted debe poder repetir:** Recorrido de checklist + ejemplo demo de 3 min.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 11 · Avance proyecto · la base de la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es una revision tecnica, y con que producto se sale
5. Lo que se audita es la coherencia entre piezas
6. Verificaciones uno y dos: el ER contra el DDL
7. Verificacion tres: que compile no es que sirva
8. La bateria de verificacion del avance
9. Scope creep: el crecimiento no controlado del alcance
10. La anatomia fija de la retroalimentacion util
11. Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado
12. Integridad y objetos de negocio, contados
13. Demo del dia
14. Del boceto al código Mermaid
15. Cierre · Clase 11

> Privado, no se proyecta: `Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Avance PI · VetCare DB.»
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
- Hoy no hay tema nuevo: se cierran huecos del PI con rubrica.
- Evidencias: ER, DDL, roles, >=2 procs, >=1 fn, >=2 triggers, 1 opt.
- Revision cruzada entre estudiantes: 10 min por persona.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 13][Slide 14]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Recorrido de checklist + ejemplo demo de 3 min.
Herramienta: ExamLab (PostgreSQL/PGlite) + draw.io / Mermaid

**Cierre la demo dentro de ExamLab** [Slide 14] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `erDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 11 [[captura: cap01_demo.png | receta: 1) Abra ExamLab (PostgreSQL/PGlite) + draw.io / Mermaid y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 11/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 11 - Avance del proyecto final/Taller PI - Clase 11 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Demo parcial + checklist de avance (hito formal PI)
Actividades:
1. Completar checklist de avance (si/no/parcial).
2. Demo 3-5 min: ER + 1 proc + 1 trigger.
3. Lista de gaps con responsable.
4. Subir avance intermedio a ExamLab (Talleres) si se pide.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 11/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 11 - VetCare.docx`. Clave para usted: `Quiz Clase 11 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 15]
**Decir:** «Queda visto: Avance PI · VetCare DB. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 15] slide de cierre. Dudas finales.


## Reparto del bloque y logistica (no se proyecta)

### La aritmetica del calendario, dicha en voz alta

Para decidir si un estudiante va a tiempo hay que hacer la aritmetica del calendario en voz alta, porque los estudiantes casi siempre creen que tienen mas tiempo del que tienen, y este semestre la cuenta es mas dura de lo que parece. Quedan cuatro Clases de material pero solo tres bloques mas de clase, y ninguno de los tres es de trabajo acompanado. La razon: este checkpoint cae en una sesion doble que continua el mismo dia con la Clase 12, la de integracion aplicacion-base de datos; despues viene la Clase 13, de casos reales, que es autonoma por festivo y el estudiante hace solo; luego el Parcial 3, que es solo evaluacion; y finalmente la sesion de cierre, que es la sustentacion en vivo del proyecto. Dicho de frente al grupo: hoy es la ultima vez que el docente revisa el proyecto con ellos delante, y lo que salga mal de aqui en adelante se corrige por cuenta propia, con retroalimentacion escrita entre sesiones. Con ese dato, el umbral razonable a esta altura es tener cerrados los 20 puntos de modelo mas DDL y los 15 de seguridad y respaldo, o sea 35 de los 100, y tener al menos la mitad de los 25 de objetos programables: dos procedimientos, uno de ellos probado con su caso invalido. Con ese criterio el semaforo es objetivo y se puede decir a la cara sin que suene arbitrario. Verde: modelo cerrado, roles definidos, dos procedimientos que ejecutan y una consulta optimizada con medicion. Amarillo: modelo cerrado pero procedimientos que compilan sin pruebas, o roles que solo existen en papel. Rojo: ER que aun cambia semana a semana, o DDL que no ejecuta de principio a fin en un entorno limpio. A un estudiante en rojo no se le pide que avance; se le pide que congele el alcance hoy mismo y dedique la semana a cerrar el DDL, porque sin una base ejecutable no hay nada sobre lo que montar procedimientos, disparadores ni optimizacion.

## Codigo / scripts
Carpeta Codigo/ — archivo 11_checklist_seed.sql.

## Capturas
Carpeta `Kit docente/Clase 11/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
