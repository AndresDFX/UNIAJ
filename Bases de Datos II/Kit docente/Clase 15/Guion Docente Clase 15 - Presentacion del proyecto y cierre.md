# Guion docente · Clase 15 · Presentacion PI · Cierre VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** SUSTENTACION DEL PI **EN VIVO** (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy cerramos el PI:** Sustentacion en vivo y entrega final del PI (20% Corte 3)
- **Entregable de hoy:** ZIP/PDF final subido antes del turno + sustentacion en vivo 5-8 min + Q&A
- **Herramienta:** ExamLab (Proyectos) + slides propias
- **Slides:** Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Cierre: evidencias completas segun rubrica (100 pts -> 20%).
- Sustentacion breve alineada a criterios del enunciado.
- Autoevaluacion del propio proceso de trabajo.

### Desarrollo del tema (para dictar sin consultar otra fuente)

### Sustentar no es describir: el eje de toda la clase - diapositiva 4
Sustentar una base de datos no es recorrer el diagrama entidad-relacion nombrando tablas. Describir es decir que hay: «tenemos Dueno, Mascota, Cita, Veterinario, Insumo y Factura». Sustentar es responder por que quedo asi y que alternativa se descarto. La razon por la que esto importa mas en bases de datos que en casi cualquier otra parte del software es el costo de revertir: cambiar el texto de un boton cuesta minutos, mientras que partir en dos una tabla que ya tiene cien mil filas y seis procedimientos apuntando a ella cuesta una migracion, una ventana de mantenimiento y el riesgo real de perder datos. Una decision de modelado es, por definicion, una decision costosa de deshacer. Eso convierte cada eleccion del ER en algo que se debe poder defender, y es exactamente lo que un evaluador (o un lider tecnico en una entrevista) va a probar con dos o tres preguntas bien elegidas. La clase de hoy no trae tema nuevo: trae la teoria de como se comunica y se empaqueta un trabajo tecnico para que un tercero pueda evaluarlo, reproducirlo y usarlo sin hablar con quien lo hizo.
### Las cuatro preguntas de por que que se hacen casi siempre - diapositiva 4
Hay cuatro preguntas de por que que se hacen casi siempre, y el estudiante debe llegar con las cuatro respondidas. Por que esa normalizacion: la respuesta esperada es que el modelo esta en tercera forma normal, es decir que cada atributo depende de la clave completa y de nada mas, y por eso el telefono del dueno vive en la tabla Dueno y no repetido en cada fila de Mascota. Y a continuacion se declara la desnormalizacion deliberada si existe: «guardamos el total en Factura aunque se pueda calcular sumando el detalle, porque el total es un valor historico que no debe cambiar si manana sube el precio del insumo». Esa segunda mitad es la que distingue al estudiante que entendio, porque normalizar no es un dogma sino un punto de partida del que se sale con razones escritas. Por que ese indice: la respuesta debe nombrar la consulta concreta que lo aprovecha, por ejemplo un indice sobre (id_veterinario, fecha_hora) porque la busqueda de agenda filtra por veterinario y ordena por hora, y debe venir con la medicion de antes y despues. Por que ese tipo de dato: por que la fecha de la cita es DATE o TIMESTAMP y no VARCHAR, y por que el telefono es VARCHAR y no numerico, porque con telefonos no se hace aritmetica y porque un tipo numerico pierde los ceros iniciales.
### La cuarta pregunta, la que mas se falla - diapositiva 4
La cuarta pregunta merece parrafo propio porque es la que mas se falla: por que esa regla esta en un disparador y no en la aplicacion. Un disparador, o trigger, es un bloque de codigo que el motor ejecuta automaticamente cuando ocurre un evento sobre una tabla, sin que nadie lo invoque. El argumento a favor, y el unico que vale en una sustentacion, es la cobertura: el disparador se ejecuta no importa quien escriba. Si la regla «el stock de un insumo nunca queda negativo» vive en el disparador, se cumple cuando escribe la aplicacion, cuando escribe un script de carga masiva y cuando alguien se conecta con un cliente SQL a corregir un dato a mano. Si vive en la aplicacion, los dos ultimos caminos la evaden sin esfuerzo. Lo mismo aplica al disparador de auditoria de precios: si se quiere saber quien cambio el precio de una vacuna, ese registro tiene que escribirse dentro de la base, porque quien edita a mano no lo va a escribir por cortesia. Y hay que dar tambien el contra-argumento, porque un evaluador atento lo va a pedir: los disparadores son logica invisible, no aparecen en el codigo de la aplicacion, sorprenden a quien depura, y se disparan en cascada si uno modifica una tabla que a su vez tiene otro disparador. Por eso la convencion sana, que el estudiante puede citar como criterio propio, es reservarlos para invariantes de integridad y auditoria, y dejar el flujo de negocio en procedimientos que se invocan explicitamente.
### Reproducible: un tercero llega a la misma base sin hablar con el autor - diapositiva 12
Un entregable de base de datos es reproducible si un tercero, con solo el archivo comprimido y sin hablar con el autor, obtiene la misma base funcionando. Esa es la definicion operativa y es la unica prueba que importa; el docente puede aplicarla literalmente abriendo el ZIP en un playground limpio y ejecutando. La estructura que la garantiza es una carpeta con archivos numerados en el orden exacto de ejecucion: 00_LEEME.txt, 01_ddl.sql, 02_datos_prueba.sql, 03_roles.sql, 04_procedimientos.sql, 05_funciones.sql, 06_triggers.sql, 07_optimizacion.sql y 08_pruebas.sql. El orden no es estetico, es una dependencia real: una tabla con clave foranea no se puede crear antes que la tabla a la que apunta, y un disparador no compila si su tabla todavia no existe. Los datos de prueba tampoco son triviales, porque con dos filas por tabla no se demuestra nada: el minimo razonable para VetCare es tres duenos, cinco mascotas, dos veterinarios, diez citas repartidas en varios dias, cinco insumos con stock y tres facturas con su detalle, incluyendo deliberadamente los casos borde que los procedimientos deben rechazar, es decir una mascota marcada como inactiva y un insumo con stock en uno, porque sin esas dos filas el estudiante no puede demostrar su manejo de errores. Sobre esa base, cuatro detalles rompen la reproducibilidad y son los que el docente debe buscar primero al abrir el paquete. Uno, no declarar motor y version: el SQL no es un solo idioma, porque una columna autoincremental se escribe SERIAL en PostgreSQL, AUTO_INCREMENT en MySQL e IDENTITY o una secuencia en Oracle y SQL Server, el texto variable es VARCHAR en unos y VARCHAR2 en Oracle, y la fecha actual es NOW() en unos y SYSDATE en Oracle; un script sin la linea «probado en PostgreSQL 15 en DB Fiddle» o «probado en Oracle 19c en Oracle Live SQL» obliga al evaluador a adivinar, y si adivina mal falla en la primera sentencia. Dos, scripts que asumen un estado previo: quien ejecuta debe poder empezar desde una base vacia. Tres, falta de idempotencia: si el script no se puede correr dos veces porque falla al encontrar que la tabla ya existe, se pierde tiempo en cada intento, y anteponer DROP TABLE IF EXISTS en orden inverso al de creacion lo resuelve. Cuatro, el LEEME ausente o inutil; uno que sirve tiene cuatro cosas y cabe en media pagina: motor y version exactos, el orden de ejecucion de los archivos, como verificar que quedo bien (una consulta cuyo resultado se conoce, por ejemplo SELECT COUNT(*) FROM cita devolviendo 10) y las limitaciones conocidas.
### El reparto de los 5 a 8 minutos - diapositiva 5
La sustentacion dura de 5 a 8 minutos y ese limite obliga a decidir que se deja fuera. El reparto que funciona, y que es convencion y no regla dura, es: 45 segundos para el problema de la clinica Huellitas en lenguaje de negocio, sin una sola tabla en pantalla; 90 segundos para el modelo, mostrando el ER y justificando dos decisiones y no las quince; 60 segundos para seguridad, con la matriz de roles y una frase sobre por que recepcion no ve el historial clinico; 90 segundos para la automatizacion, ejecutando un procedimiento con su caso valido y su caso invalido; 60 segundos para la optimizacion, con el plan de ejecucion antes y despues; 45 segundos para la integracion y el punto debil declarado; y 30 de cierre. Y conviene ser explicito sobre el formato, porque de eso depende como se prepara el estudiante: la Clase 15 se dicta el 16 de noviembre en la ultima sesion del semestre, dedicada por completo a sustentaciones EN VIVO, con turnos consecutivos y preguntas del docente al cierre de cada uno. No es clase autonoma y la defensa no se reemplaza por un video grabado, porque el Q&A dirigido al azar es lo unico que permite verificar que el modelo y los procedimientos son de quien los presenta. Lo que si hay que exigir dentro del turno es la ejecucion real: que el estudiante corra el procedimiento en el playground, con su caso valido y su caso invalido, en vez de proyectar capturas fijas, porque una consulta ejecutandose delante del evaluador es la evidencia mas dificil de fingir y la mas rapida de calificar. El paquete, en cambio, se sube al modulo de Proyectos de ExamLab ANTES del turno: quien llega a subir archivos consume su propio tiempo de sustentacion. Y el criterio de dominio es el mismo trabajando solo o en equipo autorizado: quien sustenta debe poder explicar cualquier parte en 60 segundos, y si hubo equipo, cualquier integrante debe poder hacerlo con cualquier parte, no solo con la suya, porque el Q&A se dirige al azar y porque si solo una persona entiende el modelo el evaluador no tiene forma de atribuir el trabajo a los demas.
### El Q&A de modelado, con las respuestas listas - diapositiva 5
El Q&A sobre modelado tiene preguntas que se repiten, y conviene que el docente tenga las respuestas listas para poder calificarlas y para poder formularlas. «Por que nombre y apellido separados y no un solo campo nombre_completo?»: porque se necesita ordenar y buscar por apellido, y separar despues un campo unido es un trabajo sucio y lleno de errores con nombres compuestos. «Que pasa si un dueno tiene dos mascotas llamadas Pelusa?»: nada, porque la identidad la da id_mascota y no el nombre; y si se quisiera prohibirlo habria que declarar UNIQUE (id_dueno, nombre), decision que el estudiante debe poder defender en cualquiera de los dos sentidos. «Por que no borran las citas canceladas?»: porque el historial de cancelaciones es informacion de negocio, ya que permite ver que dueno cancela siempre, y porque borrar filas referenciadas por facturas rompe la integridad referencial; se usa borrado logico con un campo de estado. Y la pregunta que desarma a quien no midio: «cuanto mejoro esa consulta?». Aqui vale la regla general del Q&A tecnico, que el docente debe anunciar antes de empezar: decir «no lo medimos» no penaliza si viene acompanado de como se mediria, por ejemplo «no medimos con volumen real porque el playground se reinicia, pero el plan de ejecucion pasa de recorrido completo a busqueda por indice, y la prueba seria cargar cincuenta mil citas y comparar los tiempos». Inventar un numero, en cambio, se cae con la siguiente pregunta y cuesta mucho mas que admitir el limite.
### Evaluar con rubrica: puntos a evidencia observable - diapositiva 12
Evaluar con rubrica es asignar puntos a evidencia observable y no a impresion general. Los 100 puntos del PI VetCare DB se reparten en 20 por modelo y DDL coherente, 15 por seguridad y respaldo, 25 por procedimientos, funciones y disparadores con casos de prueba, 15 por optimizacion con antes y despues, 10 por la integracion aplicacion-base de datos documentada como contrato, y 15 por informe y sustentacion. Leer ese reparto en voz alta al abrir la sesion, antes del primer turno, evita el reclamo mas comun: los 15 puntos de sustentacion son solo la sexta parte del total, pero la sustentacion es el instrumento con el que el evaluador verifica que los otros 85 son de su autor, y un modelo excelente que nadie sabe defender abre una duda de autoria que ningun documento cierra. Y va el recordatorio de pesos: estos 100 puntos valen 20% del Corte 3, el Parcial 3 de la Clase 14 (virtual sincrono por Meet y escrito, el 9 de noviembre) vale 15%, y la asistencia 5%. El proyecto no reemplaza ni compensa el parcial: son dos evaluaciones distintas del mismo corte, y confundirlas produce reclamos que se evitan diciendolo una sola vez, hoy, con los numeros a la vista.
### El cierre del curso: conectar lo hecho con el trabajo real - diapositiva 13
El cierre del curso debe conectar lo hecho con el trabajo real, porque de eso depende que el estudiante conserve los scripts en vez de borrarlos al terminar el semestre. Lo que el estudiante produjo (un ER justificado, un DDL con restricciones declarativas, una matriz de privilegios, procedimientos con manejo de errores, disparadores de auditoria, un analisis de plan de ejecucion y un contrato de operaciones) es literalmente el contenido de las tareas de un desarrollador de base de datos o de un administrador junior en su primer ano de trabajo. Leer un plan de ejecucion y decidir si un indice sobra es una habilidad que se paga. Conviene tambien cerrar la duda sobre las herramientas, porque alguien la trae: Oracle Live SQL, DB Fiddle y draw.io se usaron por equidad y porque funcionan en cualquier navegador, no porque sean juguetes. El SQL que se escribio ahi es el mismo que corre en un servidor de produccion; lo que cambia en un entorno profesional es el volumen de datos y las consecuencias de un error, no la sintaxis. Y la autoevaluacion del taller conviene pedirla con una consigna concreta en vez de una reflexion vaga: nombren la decision de modelado que mas les costo revertir y en que clase se dieron cuenta de que estaba mal. Esa respuesta es la que mejor predice si aprendieron, y ademas le da al docente material real para ajustar el curso el proximo semestre.
### Errores tipicos del docente que no domina el tema
Error tipico del docente que no domina el tema: el primero es evaluar el paquete leyendo los scripts sin ejecutarlos. Un script que se ve correcto puede fallar en la tercera sentencia por una clave foranea que apunta a una tabla creada mas abajo, y si el docente no lo ejecuta en un playground limpio, el estudiante recibe puntos por algo que no funciona y aprende que la reproducibilidad es un discurso; el efecto aguas abajo es que ese estudiante entrega en su primer empleo un script que nadie mas puede correr, y descubre el costo cuando ya hay un cliente esperando. El segundo error es aceptar la descripcion del modelo como sustentacion: dejar que el estudiante recorra el ER nombrando tablas durante seis minutos y calificar bien porque «explicaron todo». La consecuencia es que nunca se prueba la unica cosa que la sustentacion puede probar, que es si el estudiante entiende sus propias decisiones, y se pierden las preguntas de por que esa normalizacion o por que ese disparador, que son precisamente las que separan a quien modelo de quien copio. Un tercer tropiezo: no fijar por escrito, la semana anterior, el formato de entrega (un solo archivo comprimido, con LEEME, motor declarado y archivos numerados) ni el orden de los turnos, con lo cual llegan quince entregas en quince formatos distintos, la sesion arranca con gente subiendo archivos en vez de sustentando, y el docente termina calificando con mas rigor al primero que abrio que al ultimo.


**Demo que usted debe poder repetir:** Checklist final de empaquetado del ZIP.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 15 · Presentacion PI · Cierre VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Como se ordena la sesion de hoy
6. Herramientas de hoy
7. Sustentacion del PI — contexto / por que importa
8. Sustentacion del PI — objetivo y criterios
9. Sustentacion del PI — escenario / datos de partida
10. Sustentacion del PI — pasos guiados
11. Sustentacion del PI — pistas (checklist vacio)
12. Criterios de exito / entregable
13. Cierre del PI
14. Cierre · Clase 15

> Privado, no se proyecta: `Kit docente/Clase 15/Solucion Taller Clase 15 - VetCare.docx`

## Plan minuto a minuto (120 min) — sesion de SUSTENTACIONES EN VIVO

> Este bloque es sincrono y se dedica completo a las sustentaciones del PI VetCare DB.
> **No es clase autonoma y no es parcial.** No autorice reemplazar la defensa por un video
> grabado: el Q&A dirigido al azar es el unico instrumento con el que verifica que el modelo,
> los procedimientos y la optimizacion son de quien los presenta. El dia cae en festivo de
> calendario, pero la sesion esta destinada por decision docente a sustentar: anunciela por
> escrito la semana anterior para que nadie asuma que no hay clase.

### Antes de la sesion (semana previa)
1. Publique el orden y la duracion del turno: **5-8 min de pitch + 2-4 min de Q&A**. Con 12
   sustentaciones son ~110 min; si el grupo es mas grande, baje a 5 + 2 y avisele antes.
2. Exija el paquete subido a ExamLab (modulo Proyectos) **antes** del bloque, y abra usted
   mismo dos o tres ZIP en un playground limpio: quien llega a subir archivos consume su turno.
3. Tenga la rubrica impresa por estudiante y las preguntas de Q&A ya escogidas por tipo
   (verificacion, profundizacion, hipotetica), para no preguntar lo mismo a todos.

### 0-10 · Encuadre y orden de turnos
**Decir:** «Hoy sustentamos. De 5 a 8 minutos de pitch y hasta 4 de preguntas. Corto a los 8
minutos: si no llegaron a optimizacion, esa parte no se califica. El orden lo sorteo ahora.»
Sortee el orden delante del grupo, proyecte el cronometro y pida que el resto escuche.

### 10-110 · Sustentaciones (turnos consecutivos)
Por cada turno:
1. **5-8 min de pitch.** No interrumpa ni para corregir: anote y pregunte despues. Exija que se
   vea al menos **una ejecucion real** (procedimiento con caso valido e invalido, o el plan de
   ejecucion antes/despues), no solo capturas fijas.
2. **2-4 min de Q&A.** Una pregunta de verificacion («muestreme el DDL de esa tabla»), una de
   profundizacion («por que esa regla esta en un disparador y no en la aplicacion») y, si hay
   tiempo, una hipotetica («si manana entran cien mil citas, que consulta se cae primero»). Si
   autorizo equipo, dirija cada pregunta a un integrante distinto.
3. **Cierre el turno con la nota puesta**, no al final del dia.

### 110-120 · Cierre del curso
**Decir:** «Lo que entregaron —ER justificado, DDL con restricciones, matriz de privilegios,
procedimientos con manejo de errores, disparadores y analisis de plan— es el contenido real de
las tareas de un desarrollador de base de datos junior. Conserven el repositorio.»
Recuerde los pesos sin abrir discusion de notas: el PI vale **20% del Corte 3** y el Parcial 3
ya se aplico en su propia sesion; el proyecto no lo reemplaza ni lo compensa.

### Si alguien no se presenta o falla la conexion
Deje constancia escrita en el momento (hora, motivo) y reprograme dentro de la misma semana por
Meet, sustentando igualmente en vivo. Aceptar un video «por esta vez» elimina el Q&A, que es la
mitad de lo que se evalua, y vuelve regla la excepcion el semestre siguiente.


## Codigo / scripts
Carpeta Codigo/ — archivo N/A.

## Capturas
Carpeta `Kit docente/Clase 15/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
