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


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 5] El cliente: la clinica Huellitas (1/2)** — 3 vinetas.
  - Antes de dibujar una sola tabla hay que decir para quien se dibuja, porque el taller de hoy y los enunciados de las quince clases en ExamLab estan escritos sobre un cliente concreto y con nombre.
  - La Clinica Veterinaria Huellitas atiende un alto volumen de pacientes y lleva toda su gestion en carpetas de papel.
  - Un curso de bases de datos que no nombra al cliente convierte cada taller en un ejercicio suelto; nombrarlo hace que el estudiante pueda decidir por si mismo si un dato sobra.
  - Hay que fijar la nomenclatura en voz alta porque el material la usa con precision y el estudiante la mezcla: Huellitas es la CLINICA, es decir el cliente que tiene el problema
  - Programacion II construye la aplicacion para el mismo cliente y Seminario disena sus planos, asi que un estudiante que curse dos de las tres materias trabaja el mismo caso desde dos angulos.
  - Los tres interesados son la herramienta de decision mas util que se le puede dar hoy al estudiante, y estan en la diapositiva por eso.
  - El dueno de la clinica quiere metricas del negocio.
  - La recepcionista quiere agendar rapido y con pocos clics.
  - El veterinario quiere el historial del paciente a la mano durante la consulta.
  - Lo importante, y hay que subrayarlo, es que esos intereses ENTRAN EN CONFLICTO: pedir mas datos en el formulario de la cita da mejores metricas al dueno y le hace mas lento el trabajo a la recepcionista.
  - Ahi esta la diferencia entre un modelo copiado y uno decidido.
  - Cuando en un taller un estudiante pregunte si una columna sobra, la respuesta del docente no deberia ser si o no sino otra pregunta: cual de los tres la necesita, y que pierde otro si la agregamos.

**[Slide 6] El cliente: la clinica Huellitas (2/2)** — 3 vinetas.

**[Slide 7] Por que esto no es Bases de Datos I, y el vocabulario minimo (1/2)** — 4 vinetas.
  - Esta clase parece repetir Bases de Datos I y no lo hace.
  - Conviene fijar el vocabulario operativo antes de dibujar nada.
  - Conviene desactivar una trampa de vocabulario: la palabra dominio se usara hoy con dos sentidos, el de un atributo y el del proyecto, que es la clinica Huellitas.

**[Slide 8] Por que esto no es Bases de Datos I, y el vocabulario minimo (2/2)** — 2 vinetas.

**[Slide 9] Nivel conceptual y nivel fisico: dos vistas del mismo modelo** — 4 vinetas.
  - Antes de cualquier otra cosa hay que separar dos niveles que el estudiante mezcla y que hoy se recorren los dos.
  - Conviene decirlo en voz alta porque explica por que se exige tipo y longitud en el diagrama: no es decoracion, es lo que hace traducible el dibujo.

**[Slide 10] Clave primaria: natural o sustituta** — 6 vinetas.
  - Eso no es estilo, es una restriccion que el motor verifica en cada INSERT y UPDATE y que rechaza con error.
  - La natural ahorra un JOIN cuando se busca por ella; la sustituta gana cuando el dato natural cambia, se repite o todavia no existe.
  - Por eso el esquema usa identificadores sustitutos y guarda el dato natural aparte con unicidad:.
  - UNIQUE impide dos duenos con la misma cedula, permite dejarla nula un rato y permite corregirla sin tocar las filas de mascota que apuntan al dueno.

**[Slide 11] Clave primaria: natural o sustituta — sintaxis** — 7 vinetas.

**[Slide 12] Normalizacion 1FN-3FN: primero la enfermedad (1/2)** — 6 vinetas.
  - Supongamos que el estudiante guarda el telefono del dueno dentro de cada fila de cita.
  - Aparecen tres anomalias.
  - Leidas asi, las tres formas normales son tres vacunas.

**[Slide 13] Normalizacion 1FN-3FN: primero la enfermedad (2/2)** — 4 vinetas.

**[Slide 14] Clave foranea, borrado y por que la FK no basta (1/2)** — 4 vinetas.
  - Lo que casi nunca se explica es la otra mitad: que pasa al borrar el padre.
  - Al declarar la clave foranea se elige el comportamiento
  - RESTRICT o NO ACTION impide borrar el dueno mientras tenga mascotas, CASCADE borra las filas hijas en cadena y SET NULL deja la referencia nula.
  - Esa baja logica es la que obliga a validar en la Clase 3 que una mascota inactiva no agende, porque la clave foranea la sigue aceptando: el identificador existe, el negocio no lo quiere.

**[Slide 15] Clave foranea, borrado y por que la FK no basta (2/2)** — 2 vinetas.

**[Slide 16] Clave foranea, borrado y por que la FK no... — sintaxis** — 2 vinetas.

**[Slide 17] Baja logica: activa CHAR(1) en vez de DELETE** — 4 vinetas.
  - Conviene detenerse en la baja logica porque es la decision que sostiene medio semestre y casi nunca se explica.
  - Lo que se hace es marcar la fila como inactiva: activa CHAR(1) DEFAULT 'S' CHECK (activa IN ('S','N')), y las consultas del dia a dia filtran WHERE activa = 'S'.
  - La consecuencia que hay que subrayar, porque es la que abre la Clase 3, es que la clave foranea NO defiende esa regla: para el motor, la mascota inactiva existe y su identificador es valido, asi que aceptara sin chistar una cita nueva sobre ella.
  - Si el estudiante sale hoy con DELETE en la cabeza, en la Clase 3 no va a entender por que hace falta sp_agendar_cita.

**[Slide 18] Que separa un diagrama ER de un dibujo (1/2)** — 4 vinetas.
  - Eso se materializa como consulta.id_cita NOT NULL UNIQUE, no como una clave foranea simple, y decidirlo hoy evita la pregunta que aparece en la Clase 3 cuando alguien intenta registrar la consulta antes de la cita.

**[Slide 19] Que separa un diagrama ER de un dibujo (2/2)** — 4 vinetas.

**[Slide 20] Tipos de datos: donde se pagan las facturas mas caras (1/2)** — 4 vinetas.

**[Slide 21] Tipos de datos: donde se pagan las facturas mas caras (2/2)** — 3 vinetas.

**[Slide 22] Convenciones de nombres para que el DDL corra a la primera (1/2)** — 4 vinetas.
  - Convenciones de nombres del curso, y hay que exigirlas desde hoy porque el taller se corrige ejecutando el guion en el PostgreSQL que ExamLab trae en el navegador.
  - Identificadores sustitutos uniformes con el patron id_<entidad>, el mismo nombre en la tabla propia y en la que la referencia, para que el JOIN se escriba sin buscar como se llamo la columna alla.

**[Slide 23] Convenciones de nombres para que el DDL corra a la primera (2/2)** — 2 vinetas.

**[Slide 24] Herramientas del dia y que se puede demostrar con cada una** — 2 vinetas.
  - En DB Fiddle, sin cuenta y en menos de un minuto, se ejecuta el guion completo de CREATE TABLE con claves primarias, foraneas y CHECK, se insertan Ana Perez, Luna y su cita, se corre el JOIN de las tres tablas y, sobre todo, se provoca el error de integridad en vivo insertando una cita con id_mascota inexistente para que el grupo lea el mensaje real del motor.
  - Lo que DB Fiddle no da es persistencia: cada ejecucion recrea el esquema desde cero y no hay usuarios ni roles reales, razon por la cual la Clase 2 trabaja con matriz documentada.
  - Oracle Live SQL exige cuenta gratuita pero conserva esquema y guiones entre sesiones y admite bloques PL/SQL, que es lo que se necesitara desde la Clase 3; conviene que el estudiante la cree hoy y no el dia que la necesite. draw.io corre en el navegador, no pide cuenta y exporta PNG, el formato que pide ExamLab.
  - De ahi sale la regla operativa del curso: la fuente de verdad es el archivo sql en la carpeta del proyecto, nunca la pestana del navegador, y el estudiante va bien si reconstruye el esquema completo en menos de cinco minutos pegando su propio guion.

**[Slide 25] Del ER dibujado al codigo Mermaid que se entrega** — 3 vinetas.
  - Ultimo tramo, y es el que decide si el taller se entrega o no: como pasa el estudiante del dibujo a lo que la plataforma califica.
  - Eso no significa que haya que dibujar escribiendo codigo, y conviene decirlo asi para que nadie se bloquee: el camino corto es disenar visual en draw.io o Excalidraw, que es donde se piensa el modelo, y despues pedirle a una IA que traduzca ese boceto a Mermaid.
  - El PNG exportado se conserva en la carpeta del PI para el informe, pero no reemplaza la respuesta en la plataforma.
  - La demo debe terminar exactamente ahi, y deja los cuatro pasos proyectados mientras el grupo trabaja.

**[Slide 26] Preguntas frecuentes del grupo** — 5 vinetas.
  - Tres preguntas aparecen casi siempre y conviene tener la respuesta lista.
  - La respuesta no es doctrinal sino de costo: ahi el telefono de un dueno con veinte citas vive veinte veces y basta una actualizacion parcial para que el sistema mienta; ademas ese diseno impide registrar un dueno sin cita o un insumo sin venta.
  - Esa regla necesita otra herramienta: un CHECK cuando mira solo columnas de la misma fila, un procedimiento almacenado cuando debe consultar otra tabla, que es el hito de la Clase 3, o un disparador cuando debe aplicarse aunque nadie llame al procedimiento, que es el hito de la Clase 4.

**[Slide 27] El patron de tabla: PK, obligatorios y dominio cerrado** — 10 vinetas.

**[Slide 28] La clave foranea y que pasa al borrar el padre** — 13 vinetas.

**[Slide 29] Integridad referencial: el error que devuelve el motor** — 10 vinetas.

**[Slide 30] El JOIN de tres tablas** — 10 vinetas.

**[Slide 31] Lo que el DDL NO puede defender solo** — 10 vinetas.


**Demo que usted debe poder repetir:** Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 1 - Revision BD I y arranque VetCare/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 1 · Revision BD I · Arranque VetCare DB
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. El cliente · Clínica Veterinaria «Huellitas»
5. El cliente: la clinica Huellitas (1/2)
6. El cliente: la clinica Huellitas (2/2)
7. Por que esto no es Bases de Datos I, y el vocabulario minimo (1/2)
8. Por que esto no es Bases de Datos I, y el vocabulario minimo (2/2)
9. Nivel conceptual y nivel fisico: dos vistas del mismo modelo
10. Clave primaria: natural o sustituta
11. Clave primaria: natural o sustituta — sintaxis
12. Normalizacion 1FN-3FN: primero la enfermedad (1/2)
13. Normalizacion 1FN-3FN: primero la enfermedad (2/2)
14. Clave foranea, borrado y por que la FK no basta (1/2)
15. Clave foranea, borrado y por que la FK no basta (2/2)
16. Clave foranea, borrado y por que la FK no... — sintaxis
17. Baja logica: activa CHAR(1) en vez de DELETE
18. Que separa un diagrama ER de un dibujo (1/2)
19. Que separa un diagrama ER de un dibujo (2/2)
20. Tipos de datos: donde se pagan las facturas mas caras (1/2)
21. Tipos de datos: donde se pagan las facturas mas caras (2/2)
22. Convenciones de nombres para que el DDL corra a la primera (1/2)
23. Convenciones de nombres para que el DDL corra a la primera (2/2)
24. Herramientas del dia y que se puede demostrar con cada una
25. Del ER dibujado al codigo Mermaid que se entrega
26. Preguntas frecuentes del grupo
27. El patron de tabla: PK, obligatorios y dominio cerrado
28. La clave foranea y que pasa al borrar el padre
29. Integridad referencial: el error que devuelve el motor
30. El JOIN de tres tablas
31. Lo que el DDL NO puede defender solo
32. ER minimo VetCare (con cardinalidad)
33. El DDL minimo que sostiene el ER
34. Demo del dia
35. Herramientas de hoy
36. Del boceto a ExamLab (diagrama)
37. Taller PI VetCare — contexto / por que importa
38. Taller PI VetCare — objetivo y criterios
39. Taller PI VetCare — escenario / datos de partida
40. Taller PI VetCare — pasos guiados
41. Taller PI VetCare — pistas (checklist vacio)
42. Criterios de exito / entregable
43. Para el PI esta semana
44. Cierre · Clase 1

> Privado, no se proyecta: `Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Arranque PI: dominio, alcance y borrador ER de VetCare DB.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde 
**Decir:** «Solo lo necesario para el entregable de hoy.»
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

### 35-55 · Demo paso a paso · [Slide 34][Slide 36]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Boceto ER en draw.io (Dueno-Mascota-Cita) + CREATE TABLE minimo en DB Fiddle, y cierre pasando el boceto a Mermaid con IA para pegarlo renderizado en ExamLab.
Herramienta: draw.io + DB Fiddle

**Cierre la demo dentro de ExamLab** [Slide 36] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `erDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Resultado del JOIN de verificacion del ER (lo que debe salir tras los INSERT) [[captura: salida-join-vetcare.png]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 40]
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

### 105-115 · Criterios de exito + quiz corto · [Slide 42]
Repasar checklist del dia con [Slide 42] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 1 - VetCare.docx`. Clave para usted: `Quiz Clase 1 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 44]
**Decir:** «Queda avanzado: Arranque PI: dominio, alcance y borrador ER de VetCare DB. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 44] slide de cierre. Dudas finales.


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
