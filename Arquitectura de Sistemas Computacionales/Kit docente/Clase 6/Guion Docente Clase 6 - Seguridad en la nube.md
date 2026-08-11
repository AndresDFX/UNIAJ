# Guion docente — Clase 6: Seguridad en la nube

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Aplicar un modelo de amenazas simple al dominio CloudLite.
- Mapear controles (authn/z, secretos, superficie de red) sin cloud de pago.
- Dejar la sección Seguridad del informe lista en borrador.

## Hoy avanzamos el PI en…
**Modelo de amenazas mínimo + controles para CloudLite**

**Entregable concreto:** Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI

**Herramienta:** Excalidraw · Google Docs

## Fundamento teórico para el docente
Seguridad no es un componente que se agrega al final ni una casilla que se marca poniendo un firewall: es una propiedad del diseno que se gana o se pierde en cada decision arquitectonica. Asegurar un sistema es preservar tres propiedades, la triada CIA: confidencialidad (solo quien debe ver un dato lo ve), integridad (nadie lo modifica sin autorizacion) y disponibilidad (el sistema responde cuando se lo necesita). La justificacion es economica: un control disenado antes de escribir codigo cuesta una reunion; agregado despues de una fuga cuesta reescritura, notificacion a los usuarios y perdida de confianza. La primera pregunta del estudiante sera «no es el proveedor de nube el que ya se encarga de la seguridad?», y la respuesta sale del modelo de responsabilidad compartida de la Clase 2: el proveedor asegura la nube (hardware, hipervisor, red fisica) y el equipo asegura lo que pone DENTRO de ella (identidades, permisos, configuracion, codigo y datos). Casi todos los incidentes reales ocurren del lado del cliente.

Modelar amenazas es responder en orden cuatro preguntas: que estamos construyendo, que puede salir mal, que hacemos al respecto y si lo hicimos bien. Hace falta vocabulario preciso, porque el estudiante usa estas palabras como sinonimos. Un activo es algo que vale la pena proteger: los datos personales de los usuarios de CloudLite, el token de administrador, la disponibilidad de la API. Una amenaza es el evento indeseado: que un tercero lea la tabla de usuarios. Una vulnerabilidad es la debilidad que lo hace posible: la base de datos acepta conexiones desde internet. Un control reduce probabilidad o impacto: mover esa base a una zona privada. Y la superficie de ataque son los puntos por donde alguien externo puede interactuar con el sistema: cada endpoint publico, cada puerto publicado del contenedor, cada formulario, cada dependencia de terceros. Reducir superficie es el control mas barato que existe: lo que no esta expuesto no se puede atacar.

STRIDE es una lista de verificacion de seis categorias, y deja de ser memoria pura cuando se ve que cada una niega una propiedad deseable. Spoofing es hacerse pasar por otro y niega la autenticacion. Tampering modifica datos sin autorizacion y niega la integridad. Repudiation es negar una accion cuando no hay evidencia que lo contradiga, y niega el no repudio, que se consigue con registros de auditoria. Information disclosure expone datos a quien no debe verlos y niega la confidencialidad. Denial of service agota un recurso hasta que el sistema deja de responder y niega la disponibilidad. Elevation of privilege obtiene mas permisos de los asignados y niega la autorizacion. De ahi sale la distincion que mas se confunde: autenticacion es demostrar quien eres, autorizacion es determinar que puedes hacer una vez identificado. Un sistema puede autenticar impecablemente y seguir siendo inseguro si despues no verifica permisos.

Primer ejemplo concreto. En CloudLite el usuario final se autentica contra la API y recibe un token, una cadena firmada que acompana cada peticion posterior para no volver a pedir la contrasena. Amenaza de spoofing: alguien copia ese token de un archivo de registro y actua como ese usuario. Controles: HTTPS en todo el trayecto, el token en el encabezado de autorizacion y nunca en la URL, y vida corta. La convencion de industria es un token de acceso de 15 a 60 minutos con un refresco de dias; no es regla dura, es un balance entre comodidad y ventana de dano. Evidencia: la caja Auth del C4 Containers de la Clase 4 y la flecha etiquetada HTTPS. Segunda fila, tampering: un usuario ya autenticado invoca el endpoint que cambia el estado de un registro que no le pertenece. El control no es autenticacion, que ya paso, sino autorizacion a nivel de objeto: antes de escribir, el servidor verifica que el registro pertenezca a quien lo pide.

Segundo ejemplo concreto. CloudLite guarda datos personales, lo que se llama PII: informacion que identifica a una persona (nombre, correo, telefono, documento). Tres amenazas de information disclosure aparecen casi siempre. La respuesta que devuelve mas de lo necesario: el endpoint de perfil serializa la fila completa e incluye el hash de la contrasena o el correo de otros usuarios; el control es declarar que campos salen. El mensaje de error que revela informacion: «ese correo no existe» permite enumerar cuentas validas, mientras «credenciales invalidas» no dice nada. Y el dato en reposo sin proteger: las contrasenas no se guardan, se guarda su hash con una funcion lenta a proposito, como bcrypt o Argon2, para que probar millones de combinaciones sea costoso. Hay que separar cifrado en transito (TLS, protege el dato mientras viaja) de cifrado en reposo (protege el archivo si alguien obtiene una copia): el informe debe decir cual aplica donde.

La gestion de secretos es el error que mas se repite y el mas facil de verificar. Un secreto es cualquier valor que otorga acceso: contrasena de base de datos, llave de API, token de despliegue. Regla sin excepciones: no va en el codigo, ni en el Dockerfile, ni en el repositorio. Dos razones tecnicas hay que saber explicar. Una imagen de contenedor esta hecha de capas y cualquiera que la tenga puede extraer los archivos de cada capa: borrar el archivo en un paso posterior no lo elimina, solo lo oculta. Y Git guarda historia: si la llave se subio en un commit y se borro en el siguiente, sigue en el repositorio y en cada clon, y un buscador automatizado la encuentra en minutos. Un secreto filtrado no se arregla borrandolo: se rota, es decir se genera uno nuevo y se invalida el anterior. Con herramientas gratis, el valor real vive en los secretos del repositorio y se inyecta como variable de entorno en ejecucion, versionando solo un archivo de ejemplo con los nombres de las variables. Esto se materializa en la Clase 8.

Los controles que el equipo puede citar sin pagar nada se ordenan en tres familias. Identidad: autenticacion con token y autorizacion por rol con minimo privilegio, que es dar solo los permisos necesarios; el ejemplo es que la API de CloudLite use un usuario de base de datos que lee y escribe en sus tablas pero no borra tablas ni crea usuarios. Red: publicar solo el punto de entrada y dejar la base de datos sin acceso desde internet, que es el diagrama de la Clase 7. Aplicacion: validar toda entrada en el servidor y limitar la tasa de peticiones. Aparece la segunda pregunta previsible: «si ya valido en el formulario, para que validar otra vez en la API?». El cliente esta bajo control del atacante: cualquiera llama la API con curl y se salta el formulario, asi que la validacion del navegador es experiencia de usuario y la del servidor es seguridad. El limite de tasa, del orden de decenas o cientos de peticiones por minuto por identidad o por IP, mitiga la denegacion de servicio y los intentos de adivinar contrasenas; el numero exacto es decision de diseno, no estandar.

El entregable exige cuatro columnas por fila: amenaza especifica del dominio, activo afectado, control y evidencia. La palabra que hay que defender es evidencia: un control es verificable cuando otra persona puede senalar un artefacto y decir si esta o no esta, sin discutir. «Usamos buenas practicas» no es evidencia; «la flecha cliente-balanceador esta etiquetada HTTPS» o «el workflow lee la clave desde los secretos del repositorio» si lo son. Tercera pregunta previsible: «cuantas amenazas hay que poner?». Cinco bien desarrolladas valen mas que veinte genericas copiadas de internet: se califica especificidad, no cantidad. La Clase 5 cerro con el Parcial 1 el bloque de arquitectura y esta clase abre el de operacion. Las fronteras de confianza que hoy se nombran en texto se dibujan como zonas publica, privada y de datos en la Clase 7; la politica de secretos se ejecuta en el pipeline de la Clase 8, donde la denegacion de servicio se vuelve una senal medible; y todo el bloque se evalua en el Parcial 2 de la Clase 9.

Error tipico del docente que no domina el tema: convertir la clase en una diapositiva generica de buenas practicas («usen contrasenas fuertes, actualicen sus sistemas») en lugar de recorrer amenaza, activo, control y evidencia sobre el dominio real de cada equipo. La consecuencia aguas abajo es inmediata: la seccion de seguridad queda como relleno intercambiable entre proyectos y, en la sustentacion de la Clase 15, el estudiante no puede senalar en su propio diagrama donde vive un solo control porque nunca los ubico. El segundo tropiezo es aceptar controles no verificables, del tipo «ciframos todo» o «tenemos un firewall», sin preguntar que dato, en que momento y donde se ve. Si eso pasa hoy, el diagrama de la Clase 7 nace sin distinguir zona publica de privada, el pipeline de la Clase 8 termina con la contrasena de la base de datos escrita en el YAML, y el equipo llega al Parcial 2 repitiendo definiciones de memoria sin poder aplicarlas a un caso.

Referencia de slides: `Clases/Clase 6 - Seguridad en la nube/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Modelo de amenazas mínimo + controles para CloudLite**.
Entregable concreto: Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿en qué quedó su CloudLite la clase pasada?» — sirve para detectar equipos rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller)
Cubre estos conceptos, en este orden, ~10 min cada uno (son los títulos de las diapositivas de teoría):
- Amenazas que sí importan al PI
- Controles prácticos (gratis)
- Ejercicio guiado

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un equipo voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo
Herramienta del día: **Excalidraw · Google Docs**.
**Demo que usted debe poder repetir:** De amenaza STRIDE a control verificable, en vivo

1. Escriba en el tablero: «Tampering: alguien cambia el precio de un item via la API sin permiso».
2. Pregunte al grupo cual seria el control; guie hasta «autenticacion + validacion de rol antes de aceptar el cambio».
3. Agregue la columna Evidencia: «en que archivo o diagrama se ve ese control» — sin evidencia, el control no cuenta.
4. Demo de 1 minuto del anti-patron: muestre un Dockerfile con una API key escrita en texto plano y explique que queda en el historial de la imagen para siempre.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 6/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto) [[captura: salida-secreto-en-imagen.png]]


### 55–100 · Taller guiado PI (equipos)
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 equipos en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre
Di: «Queda avanzado: Modelo de amenazas mínimo + controles para CloudLite.
Criterio de éxito: cualquier integrante explica el artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: liste 5 amenazas concretas de su dominio, una por cada categoria de STRIDE-lite (suplantacion, manipulacion, divulgacion de informacion, denegacion de servicio y elevacion de privilegios), verificando que cada amenaza nombre el activo afectado de su propio C4 (por ejemplo la Base de datos Citas o el token del estudiante) y que ninguna sea copiada como frase generica de internet.
2. Paso 2: asigne a cada amenaza un control tecnico y la flecha o zona exacta del diagrama donde se ve ese control, verificando que los 5 controles sean distintos entre si y que al menos uno sea preventivo, uno detectivo y uno de contencion; la tabla completa queda en la seccion Seguridad del informe del PI.
3. Paso 3: escriban en ExamLab el diagrama Mermaid de fronteras de confianza con 3 zonas (publica, privada y de datos), los 5 contenedores de la Clase 4 ubicados en su zona, las aristas rotuladas con protocolo y puerto, y una arista punteada de trafico bloqueado, verificando al renderizar que la base de datos y la cola quedan en la zona de datos y que el usuario no tiene ninguna arista solida hacia ellas.
4. Paso 4: redacten la politica de secretos con los 6 puntos obligatorios (inventario de 4 secretos, donde vive cada uno, quien accede, rotacion, plan si se filtra, prohibiciones), verificando que ningun secreto quede en el Dockerfile, en el repositorio ni en el YAML en claro y que el plan de filtracion incluya rotar e invalidar la credencial anterior.
5. Paso 5: integren la tabla STRIDE, el diagrama y la politica de secretos en la seccion Seguridad del informe (1 a 1.5 paginas) y suban las 5 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que cada amenaza de la tabla se pueda senalar con el dedo en el diagrama renderizado.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Entregar una lista generica de buenas practicas en vez de amenaza -> control -> evidencia. Devuelva la tabla si no tiene las 3 columnas.
- Escribir credenciales en el Dockerfile o en el repositorio. Es el error mas costoso y hay que cortarlo el mismo dia.
- Cubrir las 6 categorias STRIDE de forma superficial en vez de 3 bien argumentadas para su dominio.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que significa la T de STRIDE y una amenaza concreta de su CloudLite?
1. Donde guardan una API key y por que NO dentro de la imagen?
1. Que evidencia demuestra que su control existe de verdad?

## Solución del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los equipos. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 6/Quiz Clase 6 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase06.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (https://examlab.lovable.app/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
