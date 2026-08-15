# Guion docente · Clase 1 · Revision BD I · Arranque VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Arranque PI: dominio, alcance y borrador ER de VetCare DB
- **Entregable de hoy:** Ficha del proyecto + ER borrador (PNG) + lista de entidades/reglas
- **Herramienta:** draw.io + DB Fiddle
- **Slides:** Clases/Clase 1 - Revision BD I y arranque VetCare/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Modelo entidad-relacion: una tabla = conjunto de entidades del mismo tipo; cada fila es una instancia, cada columna un atributo. La clave primaria (PK) identifica sin ambiguedad cada fila: nunca se repite, nunca es nula.
- Clave foranea (FK): columna que apunta a la PK de otra tabla y materializa una relacion (1-N o N-N via tabla intermedia). Garantiza integridad referencial: la BD rechaza una Cita con id_mascota que no existe.
- Normalizacion 1FN-3FN en una frase cada una: 1FN = nada de listas dentro de una celda (una fila = una mascota, no varias); 2FN = ningun atributo depende solo de una parte de una PK compuesta; 3FN = ningun atributo depende de otro atributo que no sea la PK. Sub-normalizar genera anomalias de insercion/actualizacion/borrado (ej.: cambiar el telefono de un dueno en 5 filas distintas); sobre-normalizar multiplica JOINs sin necesidad real.
- Error de docente que no domina el tema: confundir PK con 'el primer campo de la tabla', o asumir que normalizar siempre mejora el rendimiento (en lectura intensiva a veces se denormaliza a proposito, y eso se vera en Clase 6-7).
- Dominio VetCare y sus relaciones: Dueno 1-N Mascota, Mascota 1-N Cita, Veterinario 1-N Cita, Consulta 1-1 Cita (una consulta documenta una cita atendida), Factura 1-N DetalleFactura N-1 Insumo.
- Reglas de negocio del PI que ya anticipan clases futuras: mascota inactiva no puede tener cita nueva (se validara con un procedimiento en Clase 3), stock de insumo nunca queda negativo (transacciones, Clase 8), cambios sensibles quedan auditados (triggers, Clase 4).

### Desarrollo del tema (para dictar sin consultar otra fuente)

Esta clase parece repetir Bases de Datos I y no lo hace. Alla el objetivo era escribir consultas que devolvieran el resultado correcto; aqui es disenar un esquema que siga siendo correcto cuando lo usen tres personas distintas, cuando tenga cien mil filas y cuando alguien meta datos malos, a veces por error y a veces a proposito. Conviene fijar el vocabulario operativo antes de dibujar nada. Una tabla, o relacion, es un conjunto de entidades del mismo tipo: mascota guarda mascotas y nada mas. Una fila es una instancia concreta e irrepetible: la perra Luna de la duena Ana Perez. Una columna es un atributo, y todo atributo tiene un dominio, el conjunto de valores que el motor considera legales: especie no acepta cualquier texto, acepta Canino, Felino, Ave u Otro. Conviene desactivar una trampa de vocabulario: la palabra dominio se usara hoy con dos sentidos, el de un atributo y el del proyecto, que es la clinica Huellitas. Sobre estas tres nociones se monta el semestre: los roles de la Clase 2 se otorgan sobre tablas, los procedimientos de la Clase 3 validan columnas y los indices de la Clase 7 se crean sobre columnas concretas.

La clave primaria es la columna, o el conjunto de columnas, que identifica una fila sin ambiguedad: no se repite y no admite nulos. Eso no es estilo, es una restriccion que el motor verifica en cada INSERT y UPDATE y que rechaza con error. La pregunta de diseno real no es si poner clave primaria, sino cual. Una clave natural es un atributo del mundo real que ya identifica la entidad: la cedula del dueno, el microchip de la mascota. Una clave sustituta, o surrogate, es un numero sin significado de negocio que la base genera: id_dueno 1, 2, 3. La natural ahorra un JOIN cuando se busca por ella; la sustituta gana cuando el dato natural cambia, se repite o todavia no existe. En VetCare pasan las tres cosas: el dueno llega sin cedula a la mano, un microchip se digita mal y hay que corregirlo, y una mascota rescatada no tiene microchip. Por eso el esquema usa identificadores sustitutos y guarda el dato natural aparte con unicidad: CREATE TABLE dueno (id_dueno INT PRIMARY KEY, cedula VARCHAR(20) UNIQUE, nombre VARCHAR(80) NOT NULL, telefono VARCHAR(30), email VARCHAR(120)). UNIQUE impide dos duenos con la misma cedula, permite dejarla nula un rato y permite corregirla sin tocar las filas de mascota que apuntan al dueno. Regla citable, y es convencion de oficio, no regla dura: si el valor lo controla un tercero, el Estado o un fabricante, no lo use como clave primaria.

La clave foranea apunta a la clave primaria de otra tabla y su efecto practico es que el motor se niega a guardar una referencia inventada. Si se intenta INSERT INTO cita (id_cita, id_mascota, fecha_hora, estado) VALUES (101, 999, TIMESTAMP '2026-09-01 09:00:00', 'PROGRAMADA') y la mascota 999 no existe, la sentencia falla y nombra la restriccion violada: eso es integridad referencial. Lo que casi nunca se explica es la otra mitad: que pasa al borrar el padre. Al declarar la clave foranea se elige el comportamiento; RESTRICT o NO ACTION impide borrar el dueno mientras tenga mascotas, CASCADE borra las filas hijas en cadena y SET NULL deja la referencia nula. Si no se especifica nada, Oracle y PostgreSQL asumen el comportamiento restrictivo, y esa es regla dura del estandar, no convencion. En VetCare se decide entidad por entidad: mascota hacia dueno restrictivo, porque borrar un dueno no debe evaporar el historial clinico; consulta hacia cita restrictivo, porque la consulta es el registro medico; detalle_factura hacia factura en cascada, porque una linea de detalle no significa nada sin su factura; detalle_factura hacia insumo restrictivo, porque no se puede borrar un insumo ya facturado. La conclusion honesta es que en produccion casi nada se borra: se marca inactivo con activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N')). Esa baja logica es la que obliga a validar en la Clase 3 que una mascota inactiva no agende, porque la clave foranea la sigue aceptando: el identificador existe, el negocio no lo quiere.

Elegir tipos parece trivial y es donde se pagan las facturas mas caras del semestre. Un telefono no es un numero: como NUMBER se pierden los ceros iniciales, no cabe el prefijo internacional ni una extension, asi que va VARCHAR(30). Una fecha no es texto: si fecha_hora fuera VARCHAR(20), el ORDER BY seria alfabetico y no cronologico, no se podrian sumar treinta minutos para calcular el fin de la cita y el indice de la Clase 7 serviria de poco; va TIMESTAMP. El dinero no es flotante: FLOAT representa decimales en binario y arrastra errores que, sumados en cientos de lineas de detalle_factura, hacen que el total no cuadre con sus partes; va NUMBER(12,2) en Oracle o DECIMAL(12,2) en PostgreSQL. La tentacion contraria, declarar todo VARCHAR(4000) por comodidad, renuncia a que la base valide algo y traslada la validacion entera a quien programe cada pantalla. Numeros de referencia como convencion del curso: nombre VARCHAR(80), email VARCHAR(120) porque el estandar de correo admite hasta 254 caracteres, telefono VARCHAR(30), especie VARCHAR(40). El costo de equivocarse no es reescribir una linea: la tabla ya tiene datos, el ALTER TABLE debe convertir cada valor, puede fallar por una sola fila invalida, bloquea la tabla mientras dura, y los procedimientos de las Clases 3 y 4 ya asumen el tipo antiguo.

La normalizacion se dicta mejor al reves de como se suele dictar: primero la enfermedad. Supongamos que el estudiante guarda el telefono del dueno dentro de cada fila de cita. Aparecen tres anomalias. De actualizacion: cuando Ana Perez cambia de telefono hay que actualizar todas sus citas, y si una queda sin actualizar la base contiene dos verdades contradictorias. De insercion: no se puede registrar un dueno nuevo hasta que tenga una cita, porque el dato solo vive en cita. De borrado: al eliminar la ultima cita desaparece el telefono. Leidas asi, las tres formas normales son tres vacunas. Primera: nada de listas en una celda; guardar 3001112233 y 3159998877 juntos obliga a buscar con SUBSTR, no se puede indexar y no se sabe cual esta vigente, luego se crea telefono_dueno. Segunda: en detalle_factura, con clave compuesta (id_factura, id_insumo), un atributo como nombre_insumo depende solo de id_insumo y sale hacia insumo; en cambio precio_unitario se queda, y este matiz separa a quien entendio de quien memorizo, porque no es redundancia sino el precio historico del momento de la venta: si el total se recalcula con el precio actual, reimprimir una factura de hace seis meses da otra cifra. Tercera: si cita guardara especialidad_veterinario, ese atributo depende de id_veterinario y no de id_cita, luego sale hacia veterinario. La tercera forma normal es el punto de parada practico en casi todo sistema transaccional, y eso es convencion; se rompe a proposito cuando conviene, por ejemplo guardando el total ya calculado en factura, decision que se sostiene con un disparador de la Clase 4 y se justifica con planes de ejecucion en las Clases 6 y 7.

Hace falta distinguir un diagrama entidad-relacion de un dibujo, porque el entregable de hoy es un PNG y es facil entregar lo segundo creyendo que es lo primero. Un dibujo son cajas con nombres unidas por lineas. Un diagrama bien hecho cumple cinco condiciones verificables: entidades en singular con su clave primaria marcada; cada atributo con tipo y longitud, no solo nombre; cada clave foranea senalada indicando a que entidad apunta; cada relacion con cardinalidad en los dos extremos, con maximo y minimo; y cada relacion con nombre verbal legible, Dueno posee Mascota, Veterinario atiende Cita. El criterio de aceptacion que conviene entregar es operativo: el diagrama esta bien si otra persona puede escribir el CREATE TABLE completo mirandolo, sin preguntar nada. La opcionalidad es la parte que siempre se omite y la que mas cuesta despues. En VetCare, Consulta y Cita estan en relacion uno a uno pero no simetrica: una cita programada aun no tiene consulta, y una consulta no existe sin su cita. Eso se materializa como consulta.id_cita NOT NULL UNIQUE, no como una clave foranea simple, y decidirlo hoy evita la pregunta que aparece en la Clase 3 cuando alguien intenta registrar la consulta antes de la cita. Como referencia de tamano, el modelo tiene ocho entidades y siete relaciones y debe caber legible en una hoja; si no cabe, se divide en vistas por subsistema, y eso es convencion, no norma.

Tres preguntas aparecen casi siempre y conviene tener la respuesta lista. Primera: si la pantalla muestra todo junto, por que no una sola tabla con todo. La respuesta no es doctrinal sino de costo: ahi el telefono de un dueno con veinte citas vive veinte veces y basta una actualizacion parcial para que el sistema mienta; ademas ese diseno impide registrar un dueno sin cita o un insumo sin venta. Segunda: la clave primaria tiene que ser el primer campo y autoincremental. No: el orden fisico de las columnas es irrelevante para el motor, la clave primaria es una restriccion y no una posicion, y el autoincremento es solo una forma comoda de generar valores sustitutos. Tercera, la mas valiosa porque abre las clases siguientes: si pongo la clave foranea, ya no necesito validar en la aplicacion. La clave foranea garantiza que el identificador exista, no que la regla de negocio se cumpla; la mascota inactiva tiene un identificador valido y la clave foranea la acepta sin chistar. Esa regla necesita otra herramienta: un CHECK cuando mira solo columnas de la misma fila, un procedimiento almacenado cuando debe consultar otra tabla, que es el hito de la Clase 3, o un disparador cuando debe aplicarse aunque nadie llame al procedimiento, que es el hito de la Clase 4.

Sobre lo que se puede demostrar con herramientas gratuitas conviene ser preciso, porque de eso depende que el taller no se atore. En DB Fiddle, sin cuenta y en menos de un minuto, se ejecuta el guion completo de CREATE TABLE con claves primarias, foraneas y CHECK, se insertan Ana Perez, Luna y su cita, se corre el JOIN de las tres tablas y, sobre todo, se provoca el error de integridad en vivo insertando una cita con id_mascota inexistente para que el grupo lea el mensaje real del motor. Tambien se demuestra el borrado en cascada: DELETE FROM factura WHERE id_factura = 1 y verificar con SELECT COUNT(*) FROM detalle_factura que las lineas hijas desaparecieron. Lo que DB Fiddle no da es persistencia: cada ejecucion recrea el esquema desde cero y no hay usuarios ni roles reales, razon por la cual la Clase 2 trabaja con matriz documentada. Oracle Live SQL exige cuenta gratuita pero conserva esquema y guiones entre sesiones y admite bloques PL/SQL, que es lo que se necesitara desde la Clase 3; conviene que el estudiante la cree hoy y no el dia que la necesite. draw.io corre en el navegador, no pide cuenta y exporta PNG, el formato que pide ExamLab. De ahi sale la regla operativa del curso: la fuente de verdad es el archivo sql en la carpeta del proyecto, nunca la pestana del navegador, y el estudiante va bien si reconstruye el esquema completo en menos de cinco minutos pegando su propio guion.

Error tipico del docente que no domina el tema: dictar las tres formas normales como una escalera de niveles sin mostrar una sola anomalia concreta sobre las tablas de VetCare. La consecuencia aguas abajo es que el estudiante normaliza por ritual, parte insumo en tres tablas que nunca se consultan por separado y llega a la Clase 6 sin poder explicar por que su consulta de agenda hace seis JOIN ni cual sobra, de modo que el mismo vacio le cuesta puntos en el Parcial 1 y otra vez en el Parcial 2. El segundo tropiezo es aceptar como valido un diagrama sin cardinalidades y sin tipos de datos, solo porque el PNG se ve ordenado. La consecuencia es que en la Clase 3 el estudiante descubre que nunca decidio si un veterinario puede tener dos citas en la misma franja, escribe sp_agendar_cita sin esa validacion, y en la Clase 10 la demostracion de doble reserva no tiene contra que compararse; a esa altura rehacer el modelo implica tocar tablas con datos, procedimientos y disparadores escritos encima, y el estudiante pierde una sesion completa del proyecto.


**Demo que usted debe poder repetir:** Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle.

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
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Arranque PI: dominio, alcance y borrador ER de VetCare DB.
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Modelo entidad-relacion: una tabla = conjunto de entidades del mismo tipo; cada fila es una instancia, cada columna un atributo. La clave primaria (PK) identifica sin ambiguedad cada fila: nunca se repite, nunca es nula.
- Clave foranea (FK): columna que apunta a la PK de otra tabla y materializa una relacion (1-N o N-N via tabla intermedia). Garantiza integridad referencial: la BD rechaza una Cita con id_mascota que no existe.
- Normalizacion 1FN-3FN en una frase cada una: 1FN = nada de listas dentro de una celda (una fila = una mascota, no varias); 2FN = ningun atributo depende solo de una parte de una PK compuesta; 3FN = ningun atributo depende de otro atributo que no sea la PK. Sub-normalizar genera anomalias de insercion/actualizacion/borrado (ej.: cambiar el telefono de un dueno en 5 filas distintas); sobre-normalizar multiplica JOINs sin necesidad real.
- Error de docente que no domina el tema: confundir PK con 'el primer campo de la tabla', o asumir que normalizar siempre mejora el rendimiento (en lectura intensiva a veces se denormaliza a proposito, y eso se vera en Clase 6-7).
- Dominio VetCare y sus relaciones: Dueno 1-N Mascota, Mascota 1-N Cita, Veterinario 1-N Cita, Consulta 1-1 Cita (una consulta documenta una cita atendida), Factura 1-N DetalleFactura N-1 Insumo.
- Reglas de negocio del PI que ya anticipan clases futuras: mascota inactiva no puede tener cita nueva (se validara con un procedimiento en Clase 3), stock de insumo nunca queda negativo (transacciones, Clase 8), cambios sensibles quedan auditados (triggers, Clase 4).
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle.
Herramienta: draw.io + DB Fiddle
📸 Resultado del JOIN de verificacion del ER (lo que debe salir tras los INSERT) [[captura: salida-join-vetcare.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Nombrar y registrar su proyecto VetCare DB (trabajo individual por defecto; equipo de 2-3 solo si el docente lo autoriza).
2. Listar entidades minimas + 3 reglas de negocio propias.
3. Dibujar ER borrador en draw.io/Excalidraw y exportar PNG.
4. Escribir 5-8 lineas de alcance (que SI / que NO hara el PI).
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Ficha del proyecto + ER borrador (PNG) + lista de entidades/reglas
📸 Pantallazo: [CAP: avance del estudiante / playground Clase 1]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 1 - VetCare.docx`. Clave para usted: `Quiz Clase 1 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: Arranque PI: dominio, alcance y borrador ER de VetCare DB. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 01_arranque_vetcare.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
