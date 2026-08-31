# Guion docente — Clase 6: Seguridad en la nube

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Aplicar un modelo de amenazas simple al dominio CloudLite.
- Mapear controles (authn/z, secretos, superficie de red) sin cloud de pago.
- Dejar la sección Seguridad del informe lista en borrador.

## Hoy avanzamos el PI en…
**Modelo de amenazas mínimo + controles para CloudLite**

**Entregable concreto:** Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI

**Herramienta:** Google Docs para la tabla y la política · ExamLab para entregar

## Fundamento teórico para el docente
### Seguridad como propiedad del diseno: la triada CIA - diapositiva 4
Seguridad no es un componente que se agrega al final ni una casilla que se marca poniendo un firewall: es una propiedad del diseno que se gana o se pierde en cada decision arquitectonica. Asegurar un sistema es preservar tres propiedades, la triada CIA: confidencialidad (solo quien debe ver un dato lo ve), integridad (nadie lo modifica sin autorizacion) y disponibilidad (el sistema responde cuando se lo necesita). La justificacion es economica: un control disenado antes de escribir codigo cuesta una reunion; agregado despues de una fuga cuesta reescritura, notificacion a los usuarios y perdida de confianza. La primera pregunta del estudiante sera «no es el proveedor de nube el que ya se encarga de la seguridad?», y la respuesta sale del modelo de responsabilidad compartida de la Clase 2: el proveedor asegura la nube (hardware, hipervisor, red fisica) y quien construye CloudLite asegura lo que pone DENTRO de ella (identidades, permisos, configuracion, codigo y datos). Casi todos los incidentes reales ocurren del lado del cliente.
### Modelar amenazas: las cuatro preguntas y el vocabulario - diapositiva 5
Modelar amenazas es responder en orden cuatro preguntas: que estamos construyendo, que puede salir mal, que hacemos al respecto y si lo hicimos bien. Hace falta vocabulario preciso, porque el estudiante usa estas palabras como sinonimos. Un activo es algo que vale la pena proteger: los datos personales de los usuarios de CloudLite, el token de administrador, la disponibilidad de la API. Una amenaza es el evento indeseado: que un tercero lea la tabla de usuarios. Una vulnerabilidad es la debilidad que lo hace posible: la base de datos acepta conexiones desde internet. Un control reduce probabilidad o impacto: mover esa base a una zona privada. Y la superficie de ataque son los puntos por donde alguien externo puede interactuar con el sistema: cada endpoint publico, cada puerto publicado del contenedor, cada formulario, cada dependencia de terceros. Reducir superficie es el control mas barato que existe: lo que no esta expuesto no se puede atacar.
### STRIDE: seis categorias, cada una niega una propiedad - diapositiva 5
STRIDE es una lista de verificacion de seis categorias, y deja de ser memoria pura cuando se ve que cada una niega una propiedad deseable. Spoofing es hacerse pasar por otro y niega la autenticacion. Tampering modifica datos sin autorizacion y niega la integridad. Repudiation es negar una accion cuando no hay evidencia que lo contradiga, y niega el no repudio, que se consigue con registros de auditoria. Information disclosure expone datos a quien no debe verlos y niega la confidencialidad. Denial of service agota un recurso hasta que el sistema deja de responder y niega la disponibilidad. Elevation of privilege obtiene mas permisos de los asignados y niega la autorizacion. De ahi sale la distincion que mas se confunde: autenticacion es demostrar quien eres, autorizacion es determinar que puedes hacer una vez identificado. Un sistema puede autenticar impecablemente y seguir siendo inseguro si despues no verifica permisos.
### Los controles gratuitos, en tres familias - diapositiva 6
Los controles que el estudiante puede citar sin pagar nada se ordenan en tres familias. Identidad: autenticacion con token y autorizacion por rol con minimo privilegio, que se abre aparte en la diapositiva 7 porque la rubrica lo califica por separado. Red: publicar solo el punto de entrada y dejar la base de datos sin acceso desde internet, que es el diagrama de la Clase 7. Aplicacion: validar toda entrada en el servidor y limitar la tasa de peticiones. Aparece la segunda pregunta previsible: «si ya valido en el formulario, para que validar otra vez en la API?». El cliente esta bajo control del atacante: cualquiera llama la API con curl y se salta el formulario, asi que la validacion del navegador es experiencia de usuario y la del servidor es seguridad. El limite de tasa, del orden de decenas o cientos de peticiones por minuto por identidad o por IP, mitiga la denegacion de servicio y los intentos de adivinar contrasenas; el numero exacto es decision de diseno, no estandar.
### Menor privilegio: la resta que hay que poder nombrar - diapositiva 7
El menor privilegio vale 1.25 puntos de la pregunta 2 y se pierde casi siempre por la misma razon: el estudiante lo define bien y no lo aplica. La rubrica pide las dos mitades y las pesa igual, asi que hay que instalar la idea de que menor privilegio no es una definicion sino una RESTA: se nombra un componente concreto y se dice que deja de poder hacer al aplicarlo. Si la respuesta no tiene un verbo en negativo, no esta aplicado. El ejemplo que conviene proyectar es el de la diapositiva 7, resuelto sobre el diagrama de turnos que ya se uso en la Clase 4: la API de turnos no se conecta a la base como duena de la base, sino con un rol propio al que se le conceden exactamente las operaciones de lectura, insercion y actualizacion sobre sus tablas. Ese rol no puede borrar filas, no puede alterar la estructura y no puede leer ningun otro esquema de la misma instancia. La razon por la que esto importa, y es la frase que hay que decir en voz alta, es que el privilegio se hereda: si manana aparece una inyeccion de SQL en la API, el atacante trabaja con los permisos de ese rol y no con los del duenio de la base, de modo que puede hacer dano pero no puede borrar el rastro de haberlo hecho ni tumbar el esquema completo. Menor privilegio no evita el ataque, acota el dano; decirlo asi evita la objecion de «entonces igual me atacan». Conviene ademas dar la version de la que casi nadie se acuerda: el principio aplica a personas igual que a servicios, y en un proyecto de un semestre el caso mas cercano es que no todo integrante del equipo necesita permiso de administracion en el repositorio.
### Gestion de secretos: el error mas repetido y el mas facil de verificar - diapositiva 8
La gestion de secretos es el error que mas se repite y el mas facil de verificar. Un secreto es cualquier valor que otorga acceso: contrasena de base de datos, llave de API, token de despliegue. Regla sin excepciones: no va en el codigo, ni en el Dockerfile, ni en el repositorio. Dos razones tecnicas hay que saber explicar. Una imagen de contenedor esta hecha de capas y cualquiera que la tenga puede extraer los archivos de cada capa: borrar el archivo en un paso posterior no lo elimina, solo lo oculta. Es exactamente lo que se proyecta en la diapositiva 11: el historial de la imagen lista la capa que fijo la llave, y el borrado posterior aparece como UNA CAPA MAS, no como una eliminacion. Y Git guarda historia: si la llave se subio en un commit y se borro en el siguiente, sigue en el repositorio y en cada clon, y un buscador automatizado la encuentra en minutos. Un secreto filtrado no se arregla borrandolo: se rota, es decir se genera uno nuevo y se invalida el anterior. Con herramientas gratis, el valor real vive en los secretos del repositorio y se inyecta como variable de entorno en ejecucion, versionando solo un archivo de ejemplo con los nombres de las variables. Esto se materializa en la Clase 8.
### La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion - diapositiva 8
La politica de secretos vale 7.5 puntos repartidos en cuatro respuestas de 1.5 mas el procedimiento ante filtracion, tambien de 1.5. Conviene recorrer la diapositiva 8 renglon por renglon, porque el estudiante que solo escucho «no los pongas en el Dockerfile» responde una de las cinco y pierde las otras cuatro. Donde viven: en los secretos del repositorio y en las variables de entorno del servicio en ejecucion; en local, en un archivo de entorno que esta en el .gitignore Y en el .dockerignore, del que se versiona solo una copia de ejemplo con los NOMBRES de las variables y ningun valor. Esa distincion entre el nombre de un secreto, que es publico, y su valor, que no lo es, es la senal de que el estudiante entendio el tema. Quien los rota: un responsable con rol, escrito en el README. «Se rotan automaticamente» no responde la pregunta, porque alguien tiene que responder por que la rotacion ocurra aunque la ejecucion sea automatica; si el proyecto es individual el responsable es el mismo estudiante como duenio del repositorio, y eso es una respuesta correcta. Con que frecuencia: un numero o un evento del calendario. En un proyecto de un semestre lo defendible es rotar al cierre de cada corte y en la entrega final, mas una rotacion inmediata si el secreto aparece donde no debia. «Periodicamente» no es una frecuencia. Que esta prohibido: el Dockerfile, el README, el YAML en claro, y tambien imprimir el secreto en el registro del pipeline «para verificar que llego», que es la forma mas comun de filtrar una clave y se hace con buena intencion; la alternativa es verificar la longitud del valor, no el valor. Y el cierre, que es el criterio que mas se falla: ante una filtracion el primer paso es ROTAR la credencial, no borrar el commit. El orden hay que justificarlo y no solo enunciarlo: el historial ya salio del equipo y esta en cada clon, asi que limpiar el repositorio no invalida la llave; lo unico que la invalida es generar una nueva. Limpiar el historial es el segundo paso, y sirve para que la llave vieja no quede a la vista, no para desactivarla.
### Primer ejemplo: autenticacion con token en CloudLite - diapositiva 9
Primer ejemplo concreto. En CloudLite el usuario final se autentica contra la API y recibe un token, una cadena firmada que acompana cada peticion posterior para no volver a pedir la contrasena. Amenaza de spoofing: alguien copia ese token de un archivo de registro y actua como ese usuario. Controles: HTTPS en todo el trayecto, el token en el encabezado de autorizacion y nunca en la URL, y vida corta. La convencion de industria es un token de acceso de 15 a 60 minutos con un refresco de dias; no es regla dura, es un balance entre comodidad y ventana de dano. Evidencia: la caja Auth del C4 Containers de la Clase 4 y la flecha etiquetada HTTPS. Segunda fila, tampering: un usuario ya autenticado invoca el endpoint que cambia el estado de un registro que no le pertenece. El control no es autenticacion, que ya paso, sino autorizacion a nivel de objeto: antes de escribir, el servidor verifica que el registro pertenezca a quien lo pide.
### Segundo ejemplo: PII y las tres amenazas de identidad - diapositiva 10
Segundo ejemplo concreto. CloudLite guarda datos personales, lo que se llama PII: informacion que identifica a una persona (nombre, correo, telefono, documento). Tres amenazas de information disclosure aparecen casi siempre. La respuesta que devuelve mas de lo necesario: el endpoint de perfil serializa la fila completa e incluye el hash de la contrasena o el correo de otros usuarios; el control es declarar que campos salen. El mensaje de error que revela informacion: «ese correo no existe» permite enumerar cuentas validas, mientras «credenciales invalidas» no dice nada. Y el dato en reposo sin proteger: las contrasenas no se guardan, se guarda su hash con una funcion lenta a proposito, como bcrypt o Argon2, para que probar millones de combinaciones sea costoso. Hay que separar cifrado en transito (TLS, protege el dato mientras viaja) de cifrado en reposo (protege el archivo si alguien obtiene una copia): el informe debe decir cual aplica donde.
### El entregable: tres columnas, y la tercera es una caja o una flecha - diapositiva 10
El entregable de la pregunta 2 exige TRES columnas por fila, y los nombres son los de la diapositiva 10: amenaza, control y «donde se ve (caja o flecha)». Conviene decirlo con esos nombres porque la tercera reparte 2.5 de los 8.75 puntos y es la que se responde mal: solo admite el nombre de una CAJA o de una FLECHA del C4 Containers o del Despliegue, escrito igual que en el diagrama. Un nombre de archivo no cuenta, aunque el archivo exista y aunque sea el archivo correcto: «.dockerignore» o «el contrato del endpoint» no son piezas del diagrama, y por eso no cierran la fila. La idea de fondo es que un control es verificable cuando otra persona puede senalar la pieza y decir si el control esta o no esta, sin discutir: «usamos buenas practicas» no se puede senalar; «la flecha App web -> API de turnos lleva HTTPS y el identificador se toma del token» si. Tercera pregunta previsible: «cuantas amenazas hay que poner?». Cinco bien desarrolladas valen mas que veinte genericas copiadas de internet: se califica especificidad, no cantidad. La Clase 5 cerro con el Parcial 1 el bloque de arquitectura y esta clase abre el de operacion. Las fronteras de confianza que hoy se nombran en texto se dibujan como zonas publica, privada y de datos en la Clase 7; la politica de secretos se ejecuta en el pipeline de la Clase 8, donde la denegacion de servicio se vuelve una senal medible; y todo el bloque se evalua en el Parcial 2 de la Clase 9.
### Preguntas frecuentes del grupo - diapositiva 5
Estas aparecen todos los semestres, y las cuatro se responden con material que ya esta proyectado. «Si trabajo solo, quien rota los secretos?» El mismo estudiante, y es una respuesta valida: lo que se califica es que exista un responsable escrito, no que sea otra persona. La forma correcta es nombrar el rol, el duenio del repositorio, y dejarlo en el README para que la politica siga en pie cuando el proyecto pase a dos manos. «Cada cuanto es cada cuanto?» Hace falta un numero o un evento del calendario; en un semestre lo realista es atarlo al cierre de cada corte, mas una rotacion inmediata si el secreto aparece en un registro, en una captura de pantalla o en el chat del grupo. «Y si mi sistema no tiene base de datos propia, sobre que aplico menor privilegio?» Sobre cualquier componente que reciba permisos: la llave del servicio de correo que solo puede enviar y no leer la bandeja, el token de despliegue que alcanza un solo repositorio, o el permiso de administracion del repositorio que no necesita todo el equipo. «Puedo repetir una letra de STRIDE?» Si, y suele pasar con la fuga de informacion: dos amenazas de la misma letra son dos amenazas distintas si el camino y el control son distintos. Lo que se descuenta es la misma amenaza escrita dos veces con otras palabras.
### Errores tipicos del docente que no domina el tema
Error tipico del docente que no domina el tema: convertir la clase en una diapositiva generica de buenas practicas («usen contrasenas fuertes, actualicen sus sistemas») en lugar de recorrer amenaza, control y donde se ve sobre el dominio real de cada estudiante. La consecuencia aguas abajo es inmediata: la seccion de seguridad queda como relleno intercambiable entre proyectos y, en la sustentacion de la Clase 15, el estudiante no puede senalar en su propio diagrama donde vive un solo control porque nunca los ubico. El segundo tropiezo es aceptar controles no verificables, del tipo «ciframos todo» o «tenemos un firewall», sin preguntar que dato, en que momento y donde se ve. Si eso pasa hoy, el diagrama de la Clase 7 nace sin distinguir zona publica de privada, el pipeline de la Clase 8 termina con la contrasena de la base de datos escrita en el YAML, y el estudiante llega al Parcial 2 repitiendo definiciones de memoria sin poder aplicarlas a un caso. El tercero es mas silencioso y cuesta 4.5 puntos: dar la politica de secretos por explicada cuando solo se dijo donde viven. La pregunta 3 califica cuatro respuestas y un procedimiento, asi que hay que proyectar la diapositiva 8 completa y decir en voz alta quien rota, cada cuanto, que esta prohibido y cual es el primer paso ante una filtracion. Si el docente no dice «primero se rota, despues se limpia», la mitad del grupo entrega «borro el commit» y pierde ese punto y medio.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 6 - Seguridad en la nube/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 6 · Seguridad en la nube
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. Amenazas que sí importan al PI
6. Controles prácticos (gratis)
7. Menor privilegio: qué deja de poder hacer
8. Política de secretos: las cuatro preguntas
9. Ejercicio guiado
10. La tabla que se califica: una fila por amenaza
11. El secreto en la imagen: por qué borrarlo no sirve
12. Herramientas de hoy
13. Taller PI (paso a paso)
14. Para continuar (PI)
15. Clase 6 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 4]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Modelo de amenazas mínimo + controles para CloudLite**.
Entregable concreto: Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~5 min cada uno, con su diapositiva:
- **Amenazas que sí importan al PI** · [Slide 5]
- **Controles prácticos (gratis)** · [Slide 6]
- **Menor privilegio: qué deja de poder hacer** · [Slide 7]
- **Política de secretos: las cuatro preguntas** · [Slide 8]
- **Ejercicio guiado** · [Slide 9]
- **La tabla que se califica: una fila por amenaza** · [Slide 10]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 11]
Herramienta del día: **Google Docs para la tabla y la política · ExamLab para entregar**.
**Demo que usted debe poder repetir:** De amenaza STRIDE a control verificable, en vivo

1. Escriba en el tablero, con las dos partes que exige la rubrica: «Tampering: un cliente mueve la franja de un turno ajeno porque la API no revisa de quien es el turno».
2. Pregunte al grupo cual seria el control; guie hasta «validar el rol y la propiedad del turno antes de aceptar el cambio».
3. Agregue la tercera columna preguntando «sobre que CAJA o sobre que FLECHA del C4 Containers cae ese control». Aqui la respuesta es la caja «API de turnos». Un nombre de archivo no vale: si no se puede senalar en el diagrama, el control todavia es una intencion.
4. Repita con una segunda fila cuyo control caiga en una FLECHA, para que se vea que las dos formas cuentan: «un cliente reserva a nombre de otro» -> «el id se toma del token» -> flecha «App web -> API de turnos».
5. Demo de 1 minuto del anti-patron, con la diapositiva del historial de capas proyectada: un Dockerfile con la llave en texto plano, el `docker history` que la lee, y el `rm` posterior que no la borra sino que la tapa.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 6/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto) [[captura: salida-secreto-en-imagen.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 13]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 15]
Di: «Queda avanzado: Modelo de amenazas mínimo + controles para CloudLite.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: liste en la pregunta 1 cinco amenazas de SU dominio, cada una nombrando el actor o el dato concreto que pone en riesgo y el camino por el que ocurre; use STRIDE como guia de categorias y verifique que ninguna sea una frase de manual que sirva igual para cualquier sistema.
2. Paso 2: complete en la pregunta 2 la tabla amenaza-control-donde, senalando para cada control la caja o la flecha concreta del C4 Containers o del Despliegue donde se ve; incluya el principio de menor privilegio aplicado a un componente, diciendo que deja de poder hacer.
3. Paso 3: escriba en la pregunta 3 la politica de secretos respondiendo donde viven, quien los rota, cada cuanto y que esta prohibido, y cierre con el procedimiento ante una filtracion; verifique que su politica no admita secretos en el Dockerfile, el README ni el YAML en claro.
4. Paso 4: guarde y continue. Esta actividad es una sola para las Clases 6, 7, 8 y 10 y se entrega completa al cierre del Corte 2: hoy resuelve las preguntas 1 a 3 y las 4 a 12 se resuelven en las clases siguientes.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Entregar una lista generica de buenas practicas en vez de amenaza -> control -> donde se ve. Devuelva la tabla si no tiene las 3 columnas con esos nombres.
- Escribir credenciales en el Dockerfile o en el repositorio. Es el error mas costoso y hay que cortarlo el mismo dia.
- Cubrir las 6 categorias STRIDE de forma superficial en vez de las CINCO amenazas bien argumentadas que pide el enunciado. Dos amenazas de la misma letra son validas si el camino y el control son distintos.
- Amenazas sin sujeto ni camino: «podrian hackear la base de datos». Valen la mitad. La prueba rapida es preguntar si esa frase se podria copiar en el trabajo de otro estudiante sin cambiar nada.
- Poner un nombre de archivo en la tercera columna («.dockerignore», «el contrato del endpoint»). No suma: son 2.5 pts que se reparten por senalar una caja o una flecha del diagrama.
- Menor privilegio recitado y no aplicado. Pida las dos frases: sobre que componente, y que deja de poder hacer al aplicarlo.
- Politica de secretos sin responsable ni frecuencia («deberian rotarse periodicamente»). Son 3 de los 7.5 pts de la pregunta 3, y se pierden por escribir en tercera persona.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que significa la T de STRIDE y una amenaza concreta de su CloudLite?
1. Donde guardan una API key y por que NO dentro de la imagen?
1. Sobre que caja o sobre que flecha de SU diagrama cae uno de sus controles? Digalo con el nombre que tiene alli.
1. Quien rota los secretos de su repositorio y cada cuanto? Un rol y un evento del calendario, no «periodicamente».
1. Si manana se filtra su cadena de conexion, cual es el PRIMER paso y por que no es borrar el commit?
1. Sobre que componente aplican menor privilegio, y que deja de poder hacer ese componente al aplicarlo?

## Solución del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 6/Quiz Clase 6 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase06.png | receta: 1) Abre Google Docs para la tabla y la política · ExamLab para entregar y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 6/Capturas/demo-clase06.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase06.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 6/Capturas/evidencia-clase06.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
