# Guion docente · Clase 1 · Revision BD I · Arranque VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Arranque PI: dominio, alcance y borrador ER de VetCare DB
- **Entregable de hoy:** Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion
- **Herramienta:** draw.io + DB Fiddle
- **Slides:** Clases/Clase 1 - Revision BD I y arranque VetCare/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Nivel conceptual = entidades y relaciones; nivel fisico = tablas con tipos y longitudes. El ER de hoy es el conceptual (Dueno posee Mascota); el CREATE TABLE de la demo es el mismo modelo en fisico (dueno.telefono VARCHAR(30)). Una tabla = conjunto de entidades del mismo tipo; cada fila es una instancia, cada columna un atributo. La clave primaria (PK) identifica sin ambiguedad cada fila: nunca se repite, nunca es nula.
- Clave foranea (FK): columna que apunta a la PK de otra tabla y materializa una relacion (1-N o N-N via tabla intermedia). Garantiza integridad referencial: la BD rechaza una Cita con id_mascota que no existe.
- Normalizacion 1FN-3FN en una frase cada una: 1FN = nada de listas dentro de una celda (una fila = una mascota, no varias); 2FN = ningun atributo depende solo de una parte de una PK compuesta; 3FN = ningun atributo depende de otro atributo que no sea la PK. Sub-normalizar genera anomalias de insercion/actualizacion/borrado (ej.: cambiar el telefono de un dueno en 5 filas distintas); sobre-normalizar multiplica JOINs sin necesidad real.
- Error de docente que no domina el tema: confundir PK con 'el primer campo de la tabla', o asumir que normalizar siempre mejora el rendimiento (en lectura intensiva a veces se denormaliza a proposito, y eso se vera en Clase 6-7).
- Dominio VetCare y sus relaciones: Dueno 1-N Mascota, Mascota 1-N Cita, Veterinario 1-N Cita, Consulta 1-1 Cita (una consulta documenta una cita atendida), Factura 1-N DetalleFactura N-1 Insumo.
- Reglas de negocio del PI que ya anticipan clases futuras: mascota inactiva no puede tener cita nueva (se validara con un procedimiento en Clase 3), stock de insumo nunca queda negativo (transacciones, Clase 8), cambios sensibles quedan auditados (triggers, Clase 4).

### Desarrollo del tema (para dictar sin consultar otra fuente)

### El cliente: la clinica Huellitas - diapositiva 4
Antes de dibujar una sola tabla hay que decir para quien se dibuja, porque el taller de hoy y los enunciados de las quince clases en ExamLab estan escritos sobre un cliente concreto y con nombre. La Clinica Veterinaria Huellitas atiende un alto volumen de pacientes y lleva toda su gestion en carpetas de papel. La administracion reporta tres problemas y conviene enunciarlos tal cual, porque cada uno se traduce despues en una decision de esquema: se extravian fichas de pacientes, y esa es la razon de que el expediente tenga que vivir en una fila con clave primaria y no en un papel; buscar un historial en el archivo fisico genera filas en la sala de espera, que es el motivo por el que en la Clase 7 se habla de indices y no como un tema abstracto de rendimiento; y no hay metricas, no saben cuantas especies atienden al mes, que es exactamente la consulta agregada que aparece en el taller de la Clase 6. Un curso de bases de datos que no nombra al cliente convierte cada taller en un ejercicio suelto; nombrarlo hace que el estudiante pueda decidir por si mismo si un dato sobra.

Hay que fijar la nomenclatura en voz alta porque el material la usa con precision y el estudiante la mezcla: Huellitas es la CLINICA, es decir el cliente que tiene el problema; VetCare es el SISTEMA que se le construye, y VetCare DB es concretamente la base de datos de ese sistema, que es lo que se hace en esta asignatura. Programacion II construye la aplicacion para el mismo cliente y Seminario disena sus planos, asi que un estudiante que curse dos de las tres materias trabaja el mismo caso desde dos angulos. La frontera de hoy conviene decirla de forma explicita para cortar la ansiedad: aqui no se pide la aplicacion ni la interfaz, se pide la capa de datos, y por eso el entregable del semestre es un esquema con integridad, roles, procedimientos y un plan de ejecucion, no una pantalla.

Los tres interesados son la herramienta de decision mas util que se le puede dar hoy al estudiante, y estan en la diapositiva por eso. El dueno de la clinica quiere metricas del negocio. La recepcionista quiere agendar rapido y con pocos clics. El veterinario quiere el historial del paciente a la mano durante la consulta. Lo importante, y hay que subrayarlo, es que esos intereses ENTRAN EN CONFLICTO: pedir mas datos en el formulario de la cita da mejores metricas al dueno y le hace mas lento el trabajo a la recepcionista. Ahi esta la diferencia entre un modelo copiado y uno decidido. Cuando en un taller un estudiante pregunte si una columna sobra, la respuesta del docente no deberia ser si o no sino otra pregunta: cual de los tres la necesita, y que pierde otro si la agregamos.

### Por que esto no es Bases de Datos I, y el vocabulario minimo - diapositiva 5
Esta clase parece repetir Bases de Datos I y no lo hace. Alla el objetivo era escribir consultas que devolvieran el resultado correcto; aqui es disenar un esquema que siga siendo correcto cuando lo usen tres personas distintas, cuando tenga cien mil filas y cuando alguien meta datos malos, a veces por error y a veces a proposito. Conviene fijar el vocabulario operativo antes de dibujar nada. Una tabla, o relacion, es un conjunto de entidades del mismo tipo: mascota guarda mascotas y nada mas. Una fila es una instancia concreta e irrepetible: la perra Luna de la duena Ana Perez. Una columna es un atributo, y todo atributo tiene un dominio, el conjunto de valores que el motor considera legales: especie no acepta cualquier texto, acepta Canino, Felino, Ave u Otro. Conviene desactivar una trampa de vocabulario: la palabra dominio se usara hoy con dos sentidos, el de un atributo y el del proyecto, que es la clinica Huellitas. Sobre estas tres nociones se monta el semestre: los roles de la Clase 2 se otorgan sobre tablas, los procedimientos de la Clase 3 validan columnas y los indices de la Clase 7 se crean sobre columnas concretas.

### Nivel conceptual y nivel fisico: dos vistas del mismo modelo - diapositiva 5
Antes de cualquier otra cosa hay que separar dos niveles que el estudiante mezcla y que hoy se recorren los dos. El nivel conceptual nombra entidades y relaciones con vocabulario de negocio y sin comprometerse con ningun motor: Dueno posee Mascota, Veterinario atiende Cita. El nivel fisico convierte esas entidades en tablas con columnas tipadas, longitudes, restricciones y claves: dueno.telefono VARCHAR(30) NOT NULL. Son dos vistas del MISMO modelo, no dos modelos distintos, y esa es la razon de que la clase produzca dos artefactos: el diagrama ER de la diapositiva 6 es la vista conceptual, y el guion CREATE TABLE de la diapositiva 7 es la misma informacion en fisico. El criterio operativo para saber si el conceptual esta completo es exactamente ese: si otra persona puede escribir el fisico mirandolo, sin preguntar nada, esta completo. Conviene decirlo en voz alta porque explica por que se exige tipo y longitud en el diagrama: no es decoracion, es lo que hace traducible el dibujo.

### Clave primaria: natural o sustituta - diapositiva 5
La clave primaria es la columna, o el conjunto de columnas, que identifica una fila sin ambiguedad: no se repite y no admite nulos. Eso no es estilo, es una restriccion que el motor verifica en cada INSERT y UPDATE y que rechaza con error. La pregunta de diseno real no es si poner clave primaria, sino cual. Una clave natural es un atributo del mundo real que ya identifica la entidad: la cedula del dueno, el microchip de la mascota. Una clave sustituta, o surrogate, es un numero sin significado de negocio que la base genera: id_dueno 1, 2, 3. La natural ahorra un JOIN cuando se busca por ella; la sustituta gana cuando el dato natural cambia, se repite o todavia no existe. En VetCare pasan las tres cosas: el dueno llega sin cedula a la mano, un microchip se digita mal y hay que corregirlo, y una mascota rescatada no tiene microchip. Por eso el esquema usa identificadores sustitutos y guarda el dato natural aparte con unicidad: CREATE TABLE dueno (id_dueno INT PRIMARY KEY, cedula VARCHAR(20) UNIQUE, nombre VARCHAR(80) NOT NULL, telefono VARCHAR(30), email VARCHAR(120)). UNIQUE impide dos duenos con la misma cedula, permite dejarla nula un rato y permite corregirla sin tocar las filas de mascota que apuntan al dueno. Regla citable, y es convencion de oficio, no regla dura: si el valor lo controla un tercero, el Estado o un fabricante, no lo use como clave primaria.

### Normalizacion 1FN-3FN: primero la enfermedad - diapositiva 5
La normalizacion se dicta mejor al reves de como se suele dictar: primero la enfermedad. Supongamos que el estudiante guarda el telefono del dueno dentro de cada fila de cita. Aparecen tres anomalias. De actualizacion: cuando Ana Perez cambia de telefono hay que actualizar todas sus citas, y si una queda sin actualizar la base contiene dos verdades contradictorias. De insercion: no se puede registrar un dueno nuevo hasta que tenga una cita, porque el dato solo vive en cita. De borrado: al eliminar la ultima cita desaparece el telefono. Leidas asi, las tres formas normales son tres vacunas. Primera: nada de listas en una celda; guardar 3001112233 y 3159998877 juntos obliga a buscar con SUBSTR, no se puede indexar y no se sabe cual esta vigente, luego se crea telefono_dueno. Segunda: en detalle_factura, con clave compuesta (id_factura, id_insumo), un atributo como nombre_insumo depende solo de id_insumo y sale hacia insumo; en cambio precio_unitario se queda, y este matiz separa a quien entendio de quien memorizo, porque no es redundancia sino el precio historico del momento de la venta: si el total se recalcula con el precio actual, reimprimir una factura de hace seis meses da otra cifra. Tercera: si cita guardara especialidad_veterinario, ese atributo depende de id_veterinario y no de id_cita, luego sale hacia veterinario. La tercera forma normal es el punto de parada practico en casi todo sistema transaccional, y eso es convencion; se rompe a proposito cuando conviene, por ejemplo guardando el total ya calculado en factura, decision que se sostiene con un disparador de la Clase 4 y se justifica con planes de ejecucion en las Clases 6 y 7.

### Clave foranea, borrado y por que la FK no basta - diapositiva 6
La clave foranea apunta a la clave primaria de otra tabla y su efecto practico es que el motor se niega a guardar una referencia inventada. Si se intenta INSERT INTO cita (id_cita, id_mascota, fecha_hora, estado) VALUES (101, 999, TIMESTAMP '2026-09-01 09:00:00', 'PROGRAMADA') y la mascota 999 no existe, la sentencia falla y nombra la restriccion violada: eso es integridad referencial. Lo que casi nunca se explica es la otra mitad: que pasa al borrar el padre. Al declarar la clave foranea se elige el comportamiento; RESTRICT o NO ACTION impide borrar el dueno mientras tenga mascotas, CASCADE borra las filas hijas en cadena y SET NULL deja la referencia nula. Si no se especifica nada, Oracle y PostgreSQL asumen el comportamiento restrictivo, y esa es regla dura del estandar, no convencion. En VetCare se decide entidad por entidad: mascota hacia dueno restrictivo, porque borrar un dueno no debe evaporar el historial clinico; consulta hacia cita restrictivo, porque la consulta es el registro medico; detalle_factura hacia factura en cascada, porque una linea de detalle no significa nada sin su factura; detalle_factura hacia insumo restrictivo, porque no se puede borrar un insumo ya facturado. La conclusion honesta es que en produccion casi nada se borra: se marca inactivo con activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N')). Esa baja logica es la que obliga a validar en la Clase 3 que una mascota inactiva no agende, porque la clave foranea la sigue aceptando: el identificador existe, el negocio no lo quiere.

### Baja logica: activa CHAR(1) en vez de DELETE - diapositiva 6
Conviene detenerse en la baja logica porque es la decision que sostiene medio semestre y casi nunca se explica. En un sistema real no se borran clientes ni pacientes: no se hace DELETE FROM mascota. Primero por integridad, porque la fila esta referenciada por citas, consultas y facturas y el motor lo va a impedir; segundo por trazabilidad, porque el historial clinico y la facturacion de esa mascota tienen que seguir existiendo aunque la mascota ya no venga; y tercero porque un borrado es irreversible y una equivocacion de digitacion no deberia serlo. Lo que se hace es marcar la fila como inactiva: activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N')), y las consultas del dia a dia filtran WHERE activa = 'S'. La consecuencia que hay que subrayar, porque es la que abre la Clase 3, es que la clave foranea NO defiende esa regla: para el motor, la mascota inactiva existe y su identificador es valido, asi que aceptara sin chistar una cita nueva sobre ella. La regla vive en otra capa: un CHECK si solo mira columnas de la misma fila, un procedimiento almacenado si necesita consultar otra tabla (Clase 3), o un disparador si debe aplicarse aunque nadie llame al procedimiento (Clase 4). Si el estudiante sale hoy con DELETE en la cabeza, en la Clase 3 no va a entender por que hace falta sp_agendar_cita.

### Que separa un diagrama ER de un dibujo - diapositiva 6
Hace falta distinguir un diagrama entidad-relacion de un dibujo, porque el entregable de hoy es un PNG y es facil entregar lo segundo creyendo que es lo primero. Un dibujo son cajas con nombres unidas por lineas. Un diagrama bien hecho cumple cinco condiciones verificables: entidades en singular con su clave primaria marcada; cada atributo con tipo y longitud, no solo nombre; cada clave foranea senalada indicando a que entidad apunta; cada relacion con cardinalidad en los dos extremos, con maximo y minimo; y cada relacion con nombre verbal legible, Dueno posee Mascota, Veterinario atiende Cita. El criterio de aceptacion que conviene entregar es operativo: el diagrama esta bien si otra persona puede escribir el CREATE TABLE completo mirandolo, sin preguntar nada. La opcionalidad es la parte que siempre se omite y la que mas cuesta despues. En VetCare, Consulta y Cita estan en relacion uno a uno pero no simetrica: una cita programada aun no tiene consulta, y una consulta no existe sin su cita. Eso se materializa como consulta.id_cita NOT NULL UNIQUE, no como una clave foranea simple, y decidirlo hoy evita la pregunta que aparece en la Clase 3 cuando alguien intenta registrar la consulta antes de la cita. Como referencia de tamano, el modelo tiene ocho entidades y siete relaciones y debe caber legible en una hoja; si no cabe, se divide en vistas por subsistema, y eso es convencion, no norma.

### Tipos de datos: donde se pagan las facturas mas caras - diapositiva 7
Elegir tipos parece trivial y es donde se pagan las facturas mas caras del semestre. Un telefono no es un numero: como NUMBER se pierden los ceros iniciales, no cabe el prefijo internacional ni una extension, asi que va VARCHAR(30). Una fecha no es texto: si fecha_hora fuera VARCHAR(20), el ORDER BY seria alfabetico y no cronologico, no se podrian sumar treinta minutos para calcular el fin de la cita y el indice de la Clase 7 serviria de poco; va TIMESTAMP. El dinero no es flotante: FLOAT representa decimales en binario y arrastra errores que, sumados en cientos de lineas de detalle_factura, hacen que el total no cuadre con sus partes; va NUMBER(12,2) en Oracle o DECIMAL(12,2) en PostgreSQL. La tentacion contraria, declarar todo VARCHAR(4000) por comodidad, renuncia a que la base valide algo y traslada la validacion entera a quien programe cada pantalla. Numeros de referencia como convencion del curso: nombre VARCHAR(80), email VARCHAR(120) porque el estandar de correo admite hasta 254 caracteres, telefono VARCHAR(30), especie VARCHAR(40). El costo de equivocarse no es reescribir una linea: la tabla ya tiene datos, el ALTER TABLE debe convertir cada valor, puede fallar por una sola fila invalida, bloquea la tabla mientras dura, y los procedimientos de las Clases 3 y 4 ya asumen el tipo antiguo.

### Convenciones de nombres para que el DDL corra a la primera - diapositiva 7
Convenciones de nombres del curso, y hay que exigirlas desde hoy porque el taller se corrige ejecutando el guion en el PostgreSQL que ExamLab trae en el navegador. Todo en minusculas: PostgreSQL pliega a minuscula cualquier identificador sin comillas, asi que escribir CREATE TABLE Mascota y despues consultarlo entrecomillado produce un error de tabla inexistente que cuesta veinte minutos de clase encontrar; la regla practica es no usar nunca comillas dobles en identificadores. Nombres de tabla en singular y sin tildes ni enes: dueno, mascota, cita, veterinario, consulta, insumo, factura, detalle_factura. Una tabla es un conjunto de entidades del mismo tipo, pero se nombra por lo que guarda cada fila, y el singular hace que la clave foranea se lea sola: cita.id_mascota apunta a mascota.id_mascota. Identificadores sustitutos uniformes con el patron id_<entidad>, el mismo nombre en la tabla propia y en la que la referencia, para que el JOIN se escriba sin buscar como se llamo la columna alla. Palabras compuestas con guion bajo (detalle_factura, fecha_hora), nunca camelCase. Y la convencion que mas tiempo ahorra en el semestre: el mismo nombre en el diagrama, en el DDL y en el codigo Mermaid que se entrega; cuando los tres coinciden, revisar el taller de un estudiante es leer una sola vez.

### Herramientas del dia y que se puede demostrar con cada una - diapositiva 9
Sobre lo que se puede demostrar con herramientas gratuitas conviene ser preciso, porque de eso depende que el taller no se atore. En DB Fiddle, sin cuenta y en menos de un minuto, se ejecuta el guion completo de CREATE TABLE con claves primarias, foraneas y CHECK, se insertan Ana Perez, Luna y su cita, se corre el JOIN de las tres tablas y, sobre todo, se provoca el error de integridad en vivo insertando una cita con id_mascota inexistente para que el grupo lea el mensaje real del motor. Tambien se demuestra el borrado en cascada: DELETE FROM factura WHERE id_factura = 1 y verificar con SELECT COUNT(*) FROM detalle_factura que las lineas hijas desaparecieron. Lo que DB Fiddle no da es persistencia: cada ejecucion recrea el esquema desde cero y no hay usuarios ni roles reales, razon por la cual la Clase 2 trabaja con matriz documentada. Oracle Live SQL exige cuenta gratuita pero conserva esquema y guiones entre sesiones y admite bloques PL/SQL, que es lo que se necesitara desde la Clase 3; conviene que el estudiante la cree hoy y no el dia que la necesite. draw.io corre en el navegador, no pide cuenta y exporta PNG, el formato que pide ExamLab. De ahi sale la regla operativa del curso: la fuente de verdad es el archivo sql en la carpeta del proyecto, nunca la pestana del navegador, y el estudiante va bien si reconstruye el esquema completo en menos de cinco minutos pegando su propio guion.

### Del ER dibujado al codigo Mermaid que se entrega - diapositiva 10
Ultimo tramo, y es el que decide si el taller se entrega o no: como pasa el estudiante del dibujo a lo que la plataforma califica. El taller de hoy pide el modelo ER en la pregunta de tipo diagrama de ExamLab, y esa pregunta NO recibe imagenes: recibe texto en sintaxis Mermaid (erDiagram) que la plataforma renderiza al instante. Eso no significa que haya que dibujar escribiendo codigo, y conviene decirlo asi para que nadie se bloquee: el camino corto es disenar visual en draw.io o Excalidraw, que es donde se piensa el modelo, y despues pedirle a una IA que traduzca ese boceto a Mermaid. La IA acierta la sintaxis; el modelo sigue siendo del estudiante, y por eso hay que revisar lo que devuelve: entidades completas, cardinalidades en el sentido correcto, PK y FK marcadas. El paso que nadie se puede saltar es pegar el codigo en la pregunta y mirarlo renderizado dentro de ExamLab antes de enviar, porque un diagrama que no renderiza no se puede calificar. El PNG exportado se conserva en la carpeta del PI para el informe, pero no reemplaza la respuesta en la plataforma. La demo de la diapositiva 8 debe terminar exactamente ahi, y la diapositiva 10 deja los cuatro pasos proyectados mientras el grupo trabaja.

### Preguntas frecuentes del grupo - diapositiva 5
Tres preguntas aparecen casi siempre y conviene tener la respuesta lista. Primera: si la pantalla muestra todo junto, por que no una sola tabla con todo. La respuesta no es doctrinal sino de costo: ahi el telefono de un dueno con veinte citas vive veinte veces y basta una actualizacion parcial para que el sistema mienta; ademas ese diseno impide registrar un dueno sin cita o un insumo sin venta. Segunda: la clave primaria tiene que ser el primer campo y autoincremental. No: el orden fisico de las columnas es irrelevante para el motor, la clave primaria es una restriccion y no una posicion, y el autoincremento es solo una forma comoda de generar valores sustitutos. Tercera, la mas valiosa porque abre las clases siguientes: si pongo la clave foranea, ya no necesito validar en la aplicacion. La clave foranea garantiza que el identificador exista, no que la regla de negocio se cumpla; la mascota inactiva tiene un identificador valido y la clave foranea la acepta sin chistar. Esa regla necesita otra herramienta: un CHECK cuando mira solo columnas de la misma fila, un procedimiento almacenado cuando debe consultar otra tabla, que es el hito de la Clase 3, o un disparador cuando debe aplicarse aunque nadie llame al procedimiento, que es el hito de la Clase 4.

### Errores tipicos del docente que no domina el tema
Error tipico del docente que no domina el tema: dictar las tres formas normales como una escalera de niveles sin mostrar una sola anomalia concreta sobre las tablas de VetCare. La consecuencia aguas abajo es que el estudiante normaliza por ritual, parte insumo en tres tablas que nunca se consultan por separado y llega a la Clase 6 sin poder explicar por que su consulta de agenda hace seis JOIN ni cual sobra, de modo que el mismo vacio le cuesta puntos en el Parcial 1 y otra vez en el Parcial 2. El segundo tropiezo es aceptar como valido un diagrama sin cardinalidades y sin tipos de datos, solo porque el PNG se ve ordenado. La consecuencia es que en la Clase 3 el estudiante descubre que nunca decidio si un veterinario puede tener dos citas en la misma franja, escribe sp_agendar_cita sin esa validacion, y en la Clase 10 la demostracion de doble reserva no tiene contra que compararse; a esa altura rehacer el modelo implica tocar tablas con datos, procedimientos y disparadores escritos encima, y el estudiante pierde una sesion completa del proyecto.


**Demo que usted debe poder repetir:** Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 1 - Revision BD I y arranque VetCare/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 1 · Revision BD I · Arranque VetCare DB
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. El cliente · Clínica Veterinaria «Huellitas»
5. Teoria Core (breve)
6. ER minimo VetCare (con cardinalidad)
7. El DDL minimo que sostiene el ER
8. Demo del dia
9. Herramientas de hoy
10. Del boceto a ExamLab (diagrama)
11. Taller PI VetCare — contexto / por que importa
12. Taller PI VetCare — objetivo y criterios
13. Taller PI VetCare — escenario / datos de partida
14. Taller PI VetCare — pasos guiados
15. Taller PI VetCare — pistas (checklist vacio)
16. Criterios de exito / entregable
17. Para el PI esta semana
18. Cierre · Clase 1

> Privado, no se proyecta: `Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Arranque PI: dominio, alcance y borrador ER de VetCare DB.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde [Slide 5]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyecte estas diapositivas, en este orden, ~8 min cada una. Son la teoria
completa del dia: **ninguna se salta**, porque el taller cobra puntos por lo que se
proyecta en todas ellas.
1. **[Slide 5] Teoria Core (breve)**
2. **[Slide 6] ER minimo VetCare (con cardinalidad)**
3. **[Slide 7] El DDL minimo que sostiene el ER**

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

### 35-55 · Demo paso a paso · [Slide 8][Slide 10]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.
Herramienta: draw.io + DB Fiddle

**Cierre la demo dentro de ExamLab** [Slide 10] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `erDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Resultado del JOIN de verificacion del ER (lo que debe salir tras los INSERT) [[captura: salida-join-vetcare.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 14]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Registrar el proyecto con el nombre exacto VetCare - [Apellido] (trabajo individual por defecto; equipo de 2-3 solo si el docente lo autoriza).
2. Llenar la plantilla de la ficha del PI: alcance SI / alcance NO y 3 reglas de negocio propias en formato Condicion -> Accion.
3. Dibujar el ER borrador en Excalidraw o draw.io, pasarlo a Mermaid (erDiagram) con ayuda de una IA y pegarlo renderizado en ExamLab.
4. Exportar tambien el PNG del ER a la carpeta del PI y verificar que los nombres coincidan con el DDL (minusculas, singular, id_<entidad>).
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Ficha del PI (plantilla) + ER en Mermaid renderizado en ExamLab (PNG para tu carpeta) + 3 reglas Condicion -> Accion
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 1/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 16]
Repasar checklist del dia con [Slide 16] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 1 - VetCare.docx`. Clave para usted: `Quiz Clase 1 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 18]
**Decir:** «Queda avanzado: Arranque PI: dominio, alcance y borrador ER de VetCare DB. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 18] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 01_arranque_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 1/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
