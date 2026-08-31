# Guion docente · Clase 12 · Integracion app <-> BD · Prep. presentacion

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Contrato integracion + preparacion de entrega/sustentacion
- **Entregable de hoy:** Contrato app<->BD + outline de slides de sustentacion (5-8 min)
- **Herramienta:** Google Docs + Live SQL + Excalidraw
- **Slides:** Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Integrar app<->BD significa que la aplicacion NUNCA arma SQL dinamico contra las tablas directamente; llama procedimientos y funciones ya construidos (Clases 3-4). Esto evita SQL injection (nadie concatena texto de usuario dentro de una consulta), centraliza la regla de negocio en un solo lugar, y permite cambiar el esquema interno sin romper la app mientras el contrato del proc se mantenga igual.
- Un contrato de integracion documenta, por cada operacion: nombre del proc, parametros de entrada con su tipo, que retorna (valor OUT o codigo de resultado), y que errores puede lanzar y con que significado (ej. 'ERROR: mascota inactiva' vs una excepcion no controlada del motor). Sin este contrato, cualquier desarrollador que use la BD debe adivinar el comportamiento leyendo el codigo SQL directamente.
- Manejo de errores en la frontera app-BD: la app no deberia mostrar al usuario final un error crudo de base de datos (ej. 'ORA-00001: unique constraint violated'); el proc devuelve un mensaje o codigo de negocio legible, y la app lo traduce a un mensaje humano ('Ya existe una cita en ese horario').
- Autenticacion/autorizacion en este punto es conceptual, no de implementacion: la app se conecta con una cuenta de servicio que respeta los roles definidos en Clase 2 (principio de minimo privilegio) — la app de recepcion no deberia poder ejecutar procs reservados a auditoria o administracion.
- Preparar la sustentacion no es 'hacer diapositivas bonitas': es organizar la evidencia tecnica en una narrativa logica -> problema real que resuelve VetCare, modelo de datos (ER + normalizacion), seguridad (roles), automatizacion (procs/triggers), rendimiento (indices/optimizacion), y una demo en vivo que conecte todo eso con una operacion real (agendar una cita, facturar).
- Error de docente que no domina el tema: dejar que la 'integracion' quede como una idea abstracta sin contrato escrito — el entregable de hoy exige documentar minimo 3 operaciones con su firma completa, no solo mencionarlas de palabra.

### Desarrollo del tema (para dictar sin consultar otra fuente)

### Integrar no es conectarse: cual es la unica puerta de entrada - diapositiva 4
Integrar la aplicacion con la base de datos no es conectarse: conectarse son dos lineas de configuracion. Integrar es decidir cual es la unica puerta por la que la aplicacion puede tocar los datos, y dejar esa puerta escrita en un documento que las dos partes respetan. Esa puerta es la interfaz app-BD y el documento que la describe es el contrato. Hay exactamente dos formas de construirla. En la primera, la aplicacion arma texto SQL contra las tablas: SELECT, INSERT y UPDATE escritos dentro del codigo Java o Python, apuntando directo a Mascota, Cita o Insumo. En la segunda, la aplicacion no conoce las tablas y solo puede invocar procedimientos y funciones ya construidos dentro de la base, los mismos que este curso escribio en las Clases 3 y 4. La eleccion no es de gusto. La primera abre la puerta a la inyeccion SQL, reparte la regla de negocio en tantos lugares como pantallas tenga el sistema y amarra el esquema fisico al codigo. La segunda concentra cada regla en un unico punto, permite reorganizar las tablas por dentro sin tocar la aplicacion mientras el contrato se mantenga igual, y habilita algo que la primera hace imposible: quitarle al usuario de la aplicacion todo permiso de leer o escribir tablas y dejarle solo EXECUTE sobre los procedimientos, que es el privilegio minimo trabajado en la Clase 2. Todo lo demas de esta clase se deriva de esa decision.
### Inyeccion SQL: cuando el dato se interpreta como codigo - diapositiva 4
La inyeccion SQL es lo que ocurre cuando un dato que escribio un usuario termina siendo interpretado como codigo por el motor. El motor no puede distinguir que parte del texto la escribio el programador y que parte el usuario: recibe una cadena, la analiza completa y ejecuta lo que esa cadena diga. Concretemoslo en VetCare. El buscador de mascotas de la recepcion arma la consulta pegando la entrada del usuario, de modo que el motor recibe SELECT id_mascota, nombre FROM Mascota WHERE nombre = 'ENTRADA'. Si la recepcionista escribe Luna, el motor recibe WHERE nombre = 'Luna', devuelve una fila, todo parece correcto y la aplicacion pasa a produccion. Si alguien escribe la secuencia comilla, espacio, OR 1=1, espacio, doble guion, el motor recibe WHERE nombre = '' OR 1=1 -- ' y devuelve la tabla Mascota completa, porque 1=1 es verdadero para toda fila y el doble guion comenta el resto de la linea, incluida la comilla que quedo sobrando. El mismo truco en el formulario de acceso permite entrar sin conocer ninguna clave: si la validacion es SELECT COUNT(*) FROM Usuario WHERE usuario = 'U' AND clave = 'C', una clave que cierre la comilla y agregue OR 1=1 hace verdadera la condicion para todas las filas. Conviene una precision honesta, porque la hara un estudiante: en Oracle no se apilan dos sentencias en una misma llamada, asi que el clasico punto y coma seguido de DROP TABLE Cita no se comporta como en otros motores; lo que si funciona, y basta para un incidente reportable, es leer datos ajenos, saltarse un acceso o modificar informacion cuando la aplicacion ejecuta PL/SQL dinamico. La inyeccion aparece en todas las ediciones del OWASP Top Ten: fue la categoria numero uno en 2010, 2013 y 2017, y en 2021 quedo tercera ya fusionada con otras inyecciones.
### Por que el parametro lo evita por construccion - diapositiva 6
El parametro evita esto por construccion, y hay que explicar el mecanismo y no solo la receta. Cuando la aplicacion envia la sentencia con marcadores de posicion (en Oracle :1 o :p_nombre, en JDBC el signo de interrogacion) el motor analiza primero la sentencia sin los valores, construye el plan de ejecucion, y solo despues recibe cada valor como un dato tipado que se acomoda en una casilla ya reservada. Ese valor nunca vuelve al analizador sintactico: si el usuario escribio comilla OR 1=1 doble guion, el motor busca literalmente una mascota cuyo nombre sea esa cadena, no la encuentra y devuelve cero filas. La inyeccion queda imposible, no improbable, y esa diferencia entre imposible e improbable es la que hay que instalar. Llamar un procedimiento con parametros hereda esa proteccion y agrega dos cosas: el usuario de la aplicacion puede tener EXECUTE sobre sp_agendar_cita y ninguna posibilidad de SELECT ni UPDATE sobre las tablas, de modo que aunque alguien controle la entrada no tiene sobre que ejercerla; y el motor reutiliza el plan porque la sentencia es siempre la misma cadena, lo que enlaza con el analisis de planes de las Clases 6 y 8. Aqui llega la primera pregunta previsible: si uso un ORM como JPA, ya estoy protegido. La respuesta honesta es que si mientras use los metodos del ORM o consultas con parametros nombrados, y que no en el momento en que arme una consulta nativa concatenando texto, porque el ORM no revisa lo que usted le entrega. La vulnerabilidad no la produce la tecnologia sino la concatenacion.
### El contrato y sus seis partes, que se exigen en el entregable - diapositiva 5
Contrato, dicho en serio, es mucho mas que el nombre del procedimiento, y tiene seis partes que hay que exigir en el entregable de hoy. La firma: nombre y lista ordenada de parametros con su tipo y su direccion, donde IN significa que el dato entra, OUT que el procedimiento lo devuelve e IN OUT que entra y sale modificado. Las precondiciones: lo que debe ser verdadero antes de llamar. El efecto o postcondicion: que quedo distinto en la base despues de la llamada. La lista de errores posibles con codigo y significado. Si la operacion es idempotente. Y la version. En VetCare el contrato de agendamiento se escribe asi: sp_agendar_cita(p_id_mascota IN NUMBER, p_id_veterinario IN NUMBER, p_fecha_hora IN TIMESTAMP, p_motivo IN VARCHAR2, p_id_cita OUT NUMBER); precondicion, la mascota existe y esta activa; efecto, inserta una fila en Cita en estado PROGRAMADA y devuelve su identificador; errores, -20010 mascota inexistente, -20011 mascota inactiva, -20012 franja ocupada; idempotente, no. Idempotente significa que ejecutar la operacion dos veces con los mismos datos deja el sistema igual que ejecutarla una sola vez. Agendar no lo es, y eso tiene consecuencia inmediata: si la recepcionista da doble clic, o si la red corta la respuesta y la aplicacion reintenta, quedan dos citas identicas. La solucion no es pedirle al usuario que no haga doble clic: es una restriccion UNIQUE sobre (id_veterinario, fecha_hora) que hace fallar el segundo intento en la base y no en la interfaz, o una clave de idempotencia que la aplicacion genera y la base guarda como unica. Esto conecta con la Clase 10, donde dos recepcionistas simultaneas producian el mismo dano sin que ninguna sentencia fallara.
### El manejo de errores entre capas: las tres reglas - diapositiva 5
El manejo de errores entre capas se resuelve con tres reglas. Primera: el procedimiento nunca informa un fallo devolviendo cero o menos uno en un parametro de salida, porque quien llama puede ignorarlo y seguir; lanza el error con RAISE_APPLICATION_ERROR, y el rango disponible en Oracle para errores propios va de -20000 a -20999, es decir mil codigos. Ese rango es regla dura del motor; repartirlo por modulo, por ejemplo -20010 a -20019 para mascotas y -20020 a -20029 para inventario, es convencion propia del proyecto. Segunda: la aplicacion captura el codigo, lo traduce a un mensaje en lenguaje de recepcion y jamas muestra el texto crudo del motor, porque un ORA-00942 tabla o vista no existe le regala al atacante el nombre de los objetos y al recepcionista no le dice nada; el error tecnico completo se registra en el log del servidor con un identificador de correlacion que permita encontrar despues ese evento exacto. Tercera, la mas discutida: quien decide COMMIT. La operacion de negocio completa, con todas sus validaciones y sus insercciones, vive dentro de un solo procedimiento, y ese procedimiento hace COMMIT si todo salio bien o ROLLBACK si algo fallo; la aplicacion no confirma a la mitad. En el bloque de excepciones se escribe ROLLBACK y luego RAISE para que el error suba, y nunca WHEN OTHERS THEN NULL, que es la forma mas eficaz que existe de perder datos sin enterarse.
### El pool de conexiones: que es y por que se agota - diapositiva 4
Un pool de conexiones es un conjunto de conexiones ya abiertas y autenticadas que la aplicacion mantiene vivas, presta a cada peticion mientras dura y recupera al terminar. Existe por una asimetria que conviene dar con numeros: abrir una conexion es caro y ejecutar una consulta es barato. Abrir una conexion implica saludo TCP, autenticacion del usuario, creacion de la sesion y reserva de memoria privada; en un motor como Oracle sobre una red de oficina eso cuesta del orden de decenas de milisegundos, digamos entre 20 y 100 segun red y configuracion. Tomar una conexion prestada del pool cuesta una fraccion de milisegundo. Un SELECT bien indexado sobre Cita se resuelve en 2 o 3 milisegundos. Si por cada consulta se abre y se cierra la conexion, la aplicacion gasta cincuenta milisegundos en el tramite y tres en el trabajo: mas del noventa por ciento del tiempo de respuesta es protocolo. Los valores exactos dependen del entorno y hay que medirlos; lo que si es regla dura es la direccion de la desigualdad. De ahi salen dos consecuencias. El tamano del pool no se maximiza, porque cada sesion consume memoria del servidor y mas conexiones simultaneas que nucleos de CPU no aumentan el trabajo hecho, solo la cola: la convencion difundida, no ley, es partir de unas diez conexiones para una aplicacion de este tamano y subir solo con mediciones. Y la fuga de conexiones es el fallo tipico: si una ruta del codigo no devuelve la conexion porque falto el finally o el try con recursos, el pool se agota y la aplicacion se congela esperando; el sintoma es un sistema que funciona media hora y despues no responde. Segunda pregunta previsible: no es mas lento llamar un procedimiento que consultar directo. Normalmente es mas rapido, porque una llamada resuelve en el servidor lo que la aplicacion haria en tres o cuatro viajes de red; en todo caso la respuesta profesional es medir, con las herramientas de la Clase 8.
### Logica en la base o en la aplicacion: honestidad y no propaganda - diapositiva 4
El trade-off de poner logica en la base o en la aplicacion merece honestidad y no propaganda, porque el estudiante encontrara equipos reales que defienden lo contrario de lo que oye hoy. A favor de la base: la regla queda escrita una sola vez y la cumplen todos los clientes, incluida la consola del administrador, el reporte de Excel y el script que alguien correra a las once de la noche; queda dentro de la misma transaccion que los datos, sin ventana entre validar y escribir; y ahorra viajes de red. En contra: PL/SQL es mas dificil de probar de forma automatizada, sus cambios no se versionan tan naturalmente en un repositorio como el codigo de la aplicacion, hay menos programadores que lo dominen, ata el proyecto al motor elegido, y la CPU de la base suele ser el recurso mas escaso y mas caro de escalar, porque se agrega servidor de aplicacion con facilidad y no se agrega servidor de base de datos con la misma facilidad. El criterio de decision que conviene entregar es este: las invariantes que protegen la integridad de los datos van en la base, porque son las que no pueden depender de que todos los clientes se porten bien, y en VetCare son exactamente las tres reglas del proyecto, que una mascota inactiva no agende cita, que el stock de Insumo nunca quede negativo y que los cambios sensibles queden auditados. La orquestacion, la presentacion, los formatos de fecha y el envio de correos van en la aplicacion. Cuando pregunten cual es mejor, la respuesta es que depende de donde caiga el costo del error, y para datos que no se pueden reconstruir ese costo cae siempre del lado de la base.
### Cambiar el esquema sin romper la aplicacion que ya corre - diapositiva 4
Queda el problema mas subestimado: cambiar el esquema sin romper la aplicacion que ya esta corriendo. La regla es que nunca se cambia una cosa en su lugar, se expande, se migra y despues se contrae. Suponga que VetCare necesita registrar la fecha en que una mascota fue inactivada, dato que hoy no existe. Uno, expandir: ALTER TABLE Mascota ADD (fecha_inactivacion DATE NULL), sin tocar ningun procedimiento; la aplicacion vieja ignora la columna y sigue igual porque admite nulos. Dos, escribir en ambos lados: sp_inactivar_mascota se actualiza para llenar tambien la columna nueva. Tres, rellenar el historico con UPDATE por lotes y no en una sentencia gigante sobre la tabla completa, para no bloquear a nadie por minutos, lo que enlaza con la Clase 10. Cuatro, mover lecturas y reportes a la columna nueva. Cinco, contraer: eliminar lo viejo solo cuando ninguna version desplegada lo use. Cada paso deja funcionando al mismo tiempo la version vieja y la nueva. Con los procedimientos aplica la misma logica: agregar un parametro al final con valor DEFAULT es compatible, porque las llamadas existentes siguen valiendo; cambiar el orden de los parametros, su tipo o el significado de un codigo de error rompe, y ahi se publica sp_agendar_cita_v2 y se conserva la anterior como envoltura hasta que la aplicacion migre. Los scripts de migracion se numeran, se guardan en el repositorio y jamas se editan despues de aplicados: si algo quedo mal, se escribe el siguiente numero. Eso mismo entra en el informe y en el pitch de hoy, porque el estudiante no muestra pantallas: muestra su contrato, un caso de exito, un caso de error visto por el usuario y su plan de cambio de esquema, que es lo que la Clase 13 mirara desde el lado de los fallos reales y lo que la Clase 15 va a evaluar.
### Errores tipicos del docente que no domina el tema
Error tipico del docente que no domina el tema: el primero es reducir la inyeccion SQL a la consigna de usar parametros, sin mostrar en el tablero la cadena concatenada rompiendose. El estudiante que no vio el mecanismo aplica el parametro donde le resulta comodo y concatena donde le estorba, sobre todo al armar un ORDER BY dinamico o la lista de valores de un IN, y en el Parcial 3 y en su vida laboral escribira exactamente la vulnerabilidad que creia haber aprendido a evitar. El segundo es tratar el contrato como un formato administrativo que se llena para el entregable, aceptando una tabla con el nombre de los procedimientos y una descripcion vaga. Cuando el contrato no especifica tipos, codigos de error e idempotencia, el estudiante llega a la integracion sin saber que hacer si el procedimiento falla, y aparece la solucion que arruina el proyecto: capturar toda excepcion, no mostrar nada y continuar, con lo cual las citas se pierden en silencio y el estudiante pasa la Clase 15 explicando por que el informe no coincide con la base de datos.


**Demo que usted debe poder repetir:** Plantilla contrato sp_agendar_cita + storyboard 6 slides.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 12 - Integracion y preparacion final/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 12 · Integracion app <-> BD · Prep. presentacion
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. El contrato que la app consume (no SQL suelto)
6. Demo del dia
7. Herramientas de hoy
8. Del boceto a ExamLab (diagrama)
9. Taller PI VetCare — contexto / por que importa
10. Taller PI VetCare — objetivo y criterios
11. Taller PI VetCare — escenario / datos de partida
12. Taller PI VetCare — pasos guiados
13. Taller PI VetCare — pistas (checklist vacio)
14. Criterios de exito / entregable
15. Para el PI esta semana
16. Cierre · Clase 12

> Privado, no se proyecta: `Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Contrato integracion + preparacion de entrega/sustentacion.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde [Slide 4]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyecte estas diapositivas, en este orden, ~12 min cada una. Son la teoria
completa del dia: **ninguna se salta**, porque el taller cobra puntos por lo que se
proyecta en todas ellas.
1. **[Slide 4] Teoria Core (breve)**
2. **[Slide 5] El contrato que la app consume (no SQL suelto)**

El desarrollo completo de cada una esta arriba, en «Fundamento teorico», dividido por
diapositiva: esa seccion esta escrita para dictarla sin consultar otra fuente.
Ideas que tienen que quedar dichas:
- Integrar app<->BD significa que la aplicacion NUNCA arma SQL dinamico contra las tablas directamente; llama procedimientos y funciones ya construidos (Clases 3-4). Esto evita SQL injection (nadie concatena texto de usuario dentro de una consulta), centraliza la regla de negocio en un solo lugar, y permite cambiar el esquema interno sin romper la app mientras el contrato del proc se mantenga igual.
- Un contrato de integracion documenta, por cada operacion: nombre del proc, parametros de entrada con su tipo, que retorna (valor OUT o codigo de resultado), y que errores puede lanzar y con que significado (ej. 'ERROR: mascota inactiva' vs una excepcion no controlada del motor). Sin este contrato, cualquier desarrollador que use la BD debe adivinar el comportamiento leyendo el codigo SQL directamente.
- Manejo de errores en la frontera app-BD: la app no deberia mostrar al usuario final un error crudo de base de datos (ej. 'ORA-00001: unique constraint violated'); el proc devuelve un mensaje o codigo de negocio legible, y la app lo traduce a un mensaje humano ('Ya existe una cita en ese horario').
- Autenticacion/autorizacion en este punto es conceptual, no de implementacion: la app se conecta con una cuenta de servicio que respeta los roles definidos en Clase 2 (principio de minimo privilegio) — la app de recepcion no deberia poder ejecutar procs reservados a auditoria o administracion.
- Preparar la sustentacion no es 'hacer diapositivas bonitas': es organizar la evidencia tecnica en una narrativa logica -> problema real que resuelve VetCare, modelo de datos (ER + normalizacion), seguridad (roles), automatizacion (procs/triggers), rendimiento (indices/optimizacion), y una demo en vivo que conecte todo eso con una operacion real (agendar una cita, facturar).
- Error de docente que no domina el tema: dejar que la 'integracion' quede como una idea abstracta sin contrato escrito — el entregable de hoy exige documentar minimo 3 operaciones con su firma completa, no solo mencionarlas de palabra.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 6][Slide 8]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Plantilla contrato sp_agendar_cita + storyboard 6 slides.
Herramienta: Google Docs + Live SQL + Excalidraw

**Cierre la demo dentro de ExamLab** [Slide 8] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `sequenceDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 12 [[captura: cap01_demo.png | receta: 1) Abra Google Docs + Live SQL + Excalidraw y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 12/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 12]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Redactar contrato de >=3 operaciones.
2. Diagrama flujo app->BD (Excalidraw) opcional.
3. Outline presentacion 5-8 min + quien habla que.
4. Empaquetar borrador entrega final.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Contrato app<->BD + outline de slides de sustentacion (5-8 min)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 12/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 14]
Repasar checklist del dia con [Slide 14] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 12 - VetCare.docx`. Clave para usted: `Quiz Clase 12 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 16]
**Decir:** «Queda avanzado: Contrato integracion + preparacion de entrega/sustentacion. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 16] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 12_contrato_ops.sql.

## Capturas
Carpeta `Kit docente/Clase 12/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
