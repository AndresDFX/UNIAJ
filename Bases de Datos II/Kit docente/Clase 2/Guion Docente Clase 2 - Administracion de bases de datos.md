# Guion docente · Clase 2 · Administracion de BD · Roles VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Plan de roles/privilegios de VetCare
- **Entregable de hoy:** Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)
- **Herramienta:** Oracle Live SQL / DB Fiddle + Google Docs
- **Slides:** Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. RECEPCION), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto).
- Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.
- Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.
- GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol RECEPCION) y modificar en un solo lugar en vez de uno por uno.
- Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar DBA/ALL PRIVILEGES a todo el mundo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.
- En el playground (Live SQL / DB Fiddle) el motor puede restringir CREATE ROLE o GRANT reales: cuando eso pase, el estudiante redacta la matriz rol x objeto x privilegio como documento/plan, y ejecuta lo que el playground SI permita como evidencia parcial — no es escusa para omitir el analisis.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Administrar una base de datos es decidir y hacer cumplir quien puede hacer que sobre cada objeto, y dejar rastro de quien lo hizo. Antes de llegar a la sintaxis conviene fijar cuatro terminos que se usan sueltos y se confunden todo el tiempo. Un objeto de base de datos es cualquier cosa que el motor guarda y a la que se le puede poner nombre: una tabla como Mascota, una vista, un procedimiento, una secuencia. Un esquema es el conjunto de objetos que pertenecen a un mismo propietario; en Oracle, esquema y usuario son practicamente lo mismo, y por eso VETCARE.MASCOTA se lee como «la tabla Mascota del esquema VETCARE». Autenticacion es probar quien es usted, con usuario y clave o con un certificado. Autorizacion es decidir que puede hacer una vez que ya esta dentro. Son etapas distintas, se controlan con mecanismos distintos, y un usuario puede autenticarse perfectamente y no tener permiso para leer ni una sola fila. Esta clase se dicta en sesion virtual sincrona, en el bloque normal de 120 minutos: hay explicacion en vivo, taller acompanado y espacio para preguntar, asi que este texto es el material con el que el docente dicta y no una lectura que sustituya la clase. Conviene aprovechar precisamente eso, porque los permisos son el tema del curso donde el estudiante mas necesita que alguien le diga en el momento por que su GRANT no surtio efecto.

Un privilegio es un permiso atomico: la unidad mas pequena de autorizacion que el motor sabe otorgar o quitar. Se dividen en dos familias que los estudiantes mezclan constantemente. Los privilegios de sistema habilitan acciones sobre el motor en general: CREATE SESSION para poder conectarse, CREATE TABLE, CREATE PROCEDURE, CREATE ROLE. Los privilegios de objeto habilitan acciones sobre un objeto concreto: SELECT, INSERT, UPDATE y DELETE sobre una tabla, EXECUTE sobre un procedimiento o una funcion, y REFERENCES para poder crear una clave foranea que apunte a esa tabla. La distincion practica que hay que dejar clara es la que separa DDL de DML. DDL, Data Definition Language, son las sentencias que cambian la estructura: CREATE, ALTER, DROP, TRUNCATE. DML, Data Manipulation Language, son las que leen o cambian los datos sin tocar la estructura: SELECT, INSERT, UPDATE, DELETE. Un recepcionista de la clinica Huellitas necesita DML sobre unas pocas tablas y nunca necesita DDL. Si su cuenta puede ejecutar DROP TABLE cita, un error de copiar y pegar borra la agenda completa, y ningun respaldo de la noche anterior devuelve las citas que se agendaron hoy.

Un rol es un paquete de privilegios con nombre propio, que se otorga a un usuario en un solo paso. Existe por una razon aritmetica que conviene poner en el tablero. VetCare tiene siete objetos relevantes: Dueno, Mascota, Veterinario, Cita, Consulta, Insumo y Factura con su detalle. Sobre cada uno hay hasta cinco acciones posibles. Si la clinica tiene doce empleados y los permisos se otorgan cuenta por cuenta, el administrador escribe del orden de cientos de sentencias GRANT, pero el problema grave no es el volumen: es que cuando cambie una regla, por ejemplo que recepcion ya no pueda anular facturas, tendra que recordar tocar doce cuentas sin olvidar ninguna. Con roles se define una sola vez el conjunto de privilegios de RECEPCION y se ejecutan doce sentencias GRANT RECEPCION TO usuario. Al cambiar la regla se hace un REVOKE sobre el rol y los doce usuarios quedan corregidos en el mismo instante, sin excepciones y sin listas de verificacion. Ese es el argumento real que el docente debe transmitir: el rol no ahorra tipeo, ahorra olvidos, y los olvidos en materia de permisos son precisamente los que producen incidentes de seguridad.

El principio de minimo privilegio dice que cada rol recibe exactamente lo que necesita para cumplir su funcion y ni un privilegio mas. Aplicado a VetCare deja una matriz muy concreta y defendible. El rol RECEPCION necesita SELECT sobre Mascota, Dueno y Veterinario para poder buscar y agendar; INSERT y UPDATE sobre Dueno y Mascota para registrar un paciente nuevo; INSERT y UPDATE sobre Cita para agendar y reprogramar; y nada mas. No necesita leer Consulta, porque el historial clinico es informacion sensible del paciente que la recepcion no requiere para hacer su trabajo. El rol VETERINARIO necesita SELECT sobre Mascota, Dueno y Cita e INSERT sobre Consulta, pero no UPDATE ni DELETE sobre Consulta: una nota clinica ya registrada no se edita, se corrige con una nota nueva que deja rastro y fecha. El rol AUDITOR recibe unicamente SELECT, sobre todo, y jamas una escritura. El rol ADMIN_BD es el unico con privilegios DDL. Notese que DELETE casi no aparece en ninguna fila, y eso no es descuido: en un sistema clinico las cosas no se borran, se marcan. Una cita cancelada lleva estado igual a CANCELADA y una mascota que ya no se atiende lleva activa igual a 0. Eso se llama borrado logico, y hace que el privilegio DELETE sea innecesario para casi todos los usuarios, lo que a su vez elimina de raiz la posibilidad de una perdida accidental de informacion.

Separacion de funciones, o segregation of duties, es la practica de repartir un proceso sensible entre dos o mas personas para que ninguna pueda completarlo sola sin dejar rastro. En terminos de base de datos significa que quien disena y modifica el esquema no debe ser la misma cuenta que opera los datos del dia a dia, y que quien audita solo debe leer. El ejemplo de VetCare es facil de contar: si la misma cuenta que emite una factura puede tambien borrarla, entonces una persona puede cobrar en efectivo y hacer desaparecer el registro, y no queda evidencia de que la factura existio. Separando funciones, emitir una factura es un INSERT permitido a un rol, y anular una factura es un UPDATE de estado permitido a un rol distinto, y ese UPDATE deja fecha, usuario y motivo. Aqui aparece la primera pregunta previsible del estudiante: «no es mas facil darle todo al jefe y ya?». La respuesta que el docente debe dar es que el problema no es la confianza en la persona sino el dano posible por un error o por una sesion robada. Si alguien roba la sesion del recepcionista, con minimo privilegio el atacante ve agendas y datos de contacto; con privilegios de administrador, borra la base completa. El permiso no mide cuanto se quiere a un empleado, mide cuanto se puede perder.

GRANT otorga y REVOKE retira, y ambos operan igual sobre usuarios y sobre roles. La forma de las sentencias reales, que el estudiante debe poder escribir de memoria al terminar la lectura, es esta: CREATE ROLE recepcion; luego GRANT SELECT, INSERT, UPDATE ON cita TO recepcion; luego GRANT SELECT ON mascota TO recepcion; y finalmente GRANT recepcion TO ana_gomez. Para retirar un permiso: REVOKE UPDATE ON cita FROM recepcion. Hay dos detalles que el docente debe conocer porque los estudiantes tropiezan con ellos. Primero, la clausula WITH GRANT OPTION permite que quien recibio el privilegio lo vuelva a otorgar a otros; suena comodo y es una mala idea, porque el administrador pierde el control de la cadena de permisos y, al hacer REVOKE, en varios motores se produce una revocacion en cascada con efectos que nadie previo. Segundo, existe un rol especial llamado PUBLIC al que pertenecen todos los usuarios: un GRANT SELECT ON consulta TO PUBLIC entrega el historial clinico a cualquiera que pueda conectarse, incluido el proximo usuario que se cree manana. Buscar y quitar privilegios otorgados a PUBLIC es una tarea real de endurecimiento en bases de datos heredadas, y vale la pena nombrarla para que el estudiante entienda que estos conceptos no son escolares.

El entregable central de hoy no es el script sino la matriz rol por objeto por privilegio, y conviene explicar por que. El script es la traduccion mecanica de una decision; la matriz es la decision. Se construye con los roles en las filas, los objetos en las columnas, y en cada celda las acciones permitidas mas una justificacion de una linea. El minimo exigible para VetCare son cuatro roles (ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR) por los seis o siete objetos del modelo que quedo de la Clase 1, y la regla de calidad es que ninguna celda queda sin decir por que: «AUDITOR sobre Cita: solo SELECT, porque auditar es verificar, no corregir» es una celda completa; una X sin texto no lo es. Aqui aparece la segunda pregunta previsible: «en DB Fiddle no me deja hacer CREATE ROLE, entonces no puedo entregar?». La respuesta es que si se puede entregar. Los playgrounds gratuitos restringen privilegios administrativos porque todos los usuarios comparten el mismo entorno; asi que se entrega la matriz completa como documento, se ejecuta lo que el motor SI permita como evidencia parcial, y se anota que sentencias quedaron bloqueadas y en que motor funcionarian. Un permiso que no se pudo ejecutar sigue siendo una decision de diseno evaluable. Lo que no se acepta es no haber decidido.

La segunda pagina del entregable es la politica de altas y bajas, que documenta el ciclo de vida de una cuenta: quien autoriza que se cree, con que rol nace, que pasa cuando alguien cambia de funcion, y en cuanto tiempo se desactiva cuando se va de la clinica. El plazo que se compromete habitualmente en la industria es el mismo dia del retiro, y por convencion se revisan las cuentas activas cada tres o seis meses; ninguno de esos dos numeros es una regla dura del motor, son practicas de gobierno. El problema que resuelve la politica es la cuenta huerfana: la del pasante que se fue hace un ano y cuya clave sigue funcionando. Dos reglas la cierran. Una, nunca cuentas compartidas: si tres recepcionistas entran con la cuenta recepcion1, la tabla de auditoria dira que recepcion1 cancelo la cita y no habra forma de saber quien fue; la trazabilidad se pierde de manera irrecuperable y con ella cualquier investigacion posterior. Dos, los permisos no se acumulan: al cambiar de rol se revoca el anterior, porque quien pasa de recepcion a auditoria y conserva ambos roles termina pudiendo modificar justamente lo que audita. Esto amarra con las clases vecinas de forma directa. La Clase 1 dejo el modelo y las claves primarias que hoy se protegen. La Clase 3 introduce procedimientos almacenados y con ellos el patron mas fino de todos: no dar INSERT sobre Cita al rol RECEPCION, sino EXECUTE sobre sp_agendar_cita, de modo que el usuario solo pueda escribir a traves de la regla de negocio. La Clase 4 agrega disparadores de auditoria y el plan de respaldo, que son el otro componente de este mismo criterio de rubrica. Y la Clase 12 reutiliza estos roles para definir la cuenta de servicio con la que la aplicacion se conecta. En la rubrica del PI, seguridad y respaldo valen 15 de los 100 puntos.

Error tipico del docente que no domina el tema: el primero es crear un unico usuario admin que todos comparten «para que no falle nada». La consecuencia aguas abajo es doble. Rompe la trazabilidad, porque ninguna auditoria posterior puede atribuir un cambio a una persona y los disparadores de auditoria de la Clase 4 quedan registrando siempre el mismo nombre, es decir sirviendo para nada. Y deja al estudiante convencido de que los permisos son un tramite administrativo y no una decision de diseno. El segundo error es otorgar DBA o ALL PRIVILEGES a todos los roles para que ningun taller se bloquee en el playground. La consecuencia es que la matriz del entregable queda con todas las celdas en si, de modo que no hay ninguna decision que evaluar, y en la sustentacion de la Clase 15 el estudiante no puede responder por que RECEPCION no ve el historial clinico, que es exactamente la pregunta que se hace ahi. Un tercer tropiezo, pequeno pero delator: confundir rol con usuario al explicar, y decir «le doy el rol a la tabla» o «creo un privilegio». Los privilegios no se crean, vienen definidos por el motor; lo unico que se crea son usuarios y roles, y los privilegios solo se otorgan o se retiran.


**Demo que usted debe poder repetir:** Matriz rol x objeto x privilegio sobre tablas VetCare.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 2 - Administracion de bases de datos/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 2 · Administracion de BD · Roles VetCare
2. Encuadre de hoy · Objetivo PI
3. Mapa del bloque de hoy (120 min)
4. Teoria Core (breve)
5. Minimo privilegio, en concreto
6. Demo del dia
7. Herramientas de hoy
8. Taller PI VetCare — contexto / por que importa
9. Taller PI VetCare — objetivo y criterios
10. Taller PI VetCare — escenario / datos de partida
11. Taller PI VetCare — pasos guiados
12. Taller PI VetCare — pistas (checklist vacio)
13. Criterios de exito / entregable
14. Para el PI esta semana
15. Cierre · Clase 2

> Privado, no se proyecta: `Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Plan de roles/privilegios de VetCare.
La teoria sera corta; el peso esta en el taller del proyecto.»
Proyectar [Slide 2] «Encuadre de hoy · Objetivo PI» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · [Slide 4]
**Decir:** «Solo lo necesario para el entregable de hoy.»
Proyectar [Slide 4] «Teoria Core (breve)». El desarrollo completo de cada punto esta
arriba, en «Fundamento teorico», dividido por diapositiva.
Cubrir:
- Administracion de BD = gestionar QUIEN puede hacer QUE sobre CADA objeto. Tres piezas: usuario (identidad que se conecta), rol (paquete de privilegios con nombre, ej. RECEPCION), privilegio (permiso atomico: SELECT, INSERT, UPDATE, DELETE, EXECUTE sobre un objeto concreto).
- Principio de minimo privilegio: cada rol recibe solo lo que necesita para su funcion, ni un privilegio mas. No es paranoia, es reduccion de superficie de dano: si roban la sesion de un recepcionista, no debe poder borrar el historial clinico ni ver nomina.
- Separacion de funciones (segregation of duties): quien disena/modifica el esquema (DDL: CREATE/ALTER/DROP) no deberia ser la misma cuenta que opera datos del dia a dia (DML: INSERT/UPDATE/DELETE), y quien audita solo deberia leer (SELECT), nunca escribir.
- GRANT otorga un privilegio a un rol o usuario; REVOKE lo retira. Un rol se puede asignar a varios usuarios (todos los recepcionistas heredan el rol RECEPCION) y modificar en un solo lugar en vez de uno por uno.
- Error de docente que no domina el tema: crear un unico usuario 'admin' que todos comparten (rompe la trazabilidad de auditoria) o dar DBA/ALL PRIVILEGES a todo el mundo 'para que no falle nada' — exactamente lo opuesto a minimo privilegio.
- En el playground (Live SQL / DB Fiddle) el motor puede restringir CREATE ROLE o GRANT reales: cuando eso pase, el estudiante redacta la matriz rol x objeto x privilegio como documento/plan, y ejecuta lo que el playground SI permita como evidencia parcial — no es escusa para omitir el analisis.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 6]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Matriz rol x objeto x privilegio sobre tablas VetCare.
Herramienta: Oracle Live SQL / DB Fiddle + Google Docs
📸 Salida esperada de la demo de la Clase 2 [[captura: cap01_demo.png | receta: 1) Abra Oracle Live SQL / DB Fiddle + Google Docs y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 2/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI · [Slide 11]
**Decir:** «Abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Definir >=4 roles (ADMIN_BD, RECEPCION, VETERINARIO, AUDITOR).
2. Matriz SELECT/INSERT/UPDATE/DELETE/EXECUTE por objeto clave.
3. Justificar privilegio minimo (least privilege).
4. Redactar 1 pagina: politica de altas/bajas de usuarios.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Documento Roles_VetCare + script GRANT/REVOKE (o plan equivalente)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 2/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Criterios de exito + quiz corto · [Slide 13]
Repasar checklist del dia con [Slide 13] «Criterios de exito / entregable».
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 2 - VetCare.docx`. Clave para usted: `Quiz Clase 2 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 15]
**Decir:** «Queda avanzado: Plan de roles/privilegios de VetCare. Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Proyectar [Slide 15] slide de cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 02_roles_vetcare.sql.

## Capturas
Carpeta `Kit docente/Clase 2/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
