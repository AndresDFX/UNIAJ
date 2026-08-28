# Guion docente — Clase 3: Virtualización y contenedores

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Diferenciar VM vs contenedor y el rol de la imagen.
- Ejecutar un contenedor en lab de navegador (sin Docker Desktop obligatorio).
- Dejar evidencia PI: Dockerfile del stub CloudLite + captura.

## Hoy avanzamos el PI en…
**Contenerizar un stub del servicio principal de CloudLite**

**Entregable concreto:** Dockerfile (+ compose opcional) + captura/enlace lab navegador

**Herramienta:** Killercoda · alterna si no carga: LabEx Docker Playground

## Fundamento teórico para el docente
### De donde viene la clase y que se entrega hoy - diapositiva 4
Las dos clases anteriores decidieron QUE se va a construir (dominio, capacidades, actores, diagrama de contexto) y BAJO QUE modelo de servicio se va a operar, con su registro de decision. Hoy se abre la caja de la maquinaria que hace posible todo eso: la virtualizacion y su descendiente directo, los contenedores. Es la primera clase francamente tecnica del curso y la primera en la que el estudiante escribe algo que una maquina ejecuta. El entregable es un Dockerfile y una captura del contenedor corriendo, obtenida en Killercoda, un laboratorio gratuito que funciona en el navegador. Conviene decir desde el minuto uno por que esto importa para la arquitectura y no solo para la operacion: el contenedor es la unidad de despliegue con la que se razona en todos los diagramas siguientes, y sin entender que es exactamente, el nivel de contenedores del modelo C4 que se dibuja en la Clase 4 queda en pura metafora.
### Antes de la virtualizacion: un servidor por aplicacion - diapositiva 5
Antes de la virtualizacion, cada aplicacion importante vivia en su propio servidor fisico, por una razon sencilla: si dos aplicaciones compartian maquina, una podia tumbar a la otra. El resultado era un desperdicio enorme, con servidores trabajando tipicamente entre el 5 % y el 15 % de su capacidad la mayor parte del tiempo. La virtualizacion resolvio eso con una pieza de software llamada hipervisor, que se interpone entre el hardware y los sistemas operativos y presenta a cada uno la ilusion de tener una maquina completa para si. Cada una de esas maquinas se llama maquina virtual y contiene un sistema operativo entero, kernel incluido, donde kernel es el nucleo del sistema operativo, la parte que administra memoria, procesos y acceso al hardware. Los ordenes de magnitud que el docente debe poder citar: una maquina virtual ocupa varios gigabytes en disco y tarda entre 30 segundos y unos minutos en arrancar, porque debe iniciar un sistema operativo completo. En contraparte, su aislamiento es fuerte, ya que dos maquinas virtuales no comparten kernel y un problema en el nucleo de una no alcanza a la otra.
### El contenedor: aislamiento sin otro sistema operativo - diapositiva 9
Un contenedor parte de una observacion distinta: casi nunca se necesita otro sistema operativo, solo un espacio aislado dentro del que ya existe. Todos los contenedores de una maquina comparten el kernel del anfitrion, y el aislamiento se consigue con dos mecanismos del propio Linux. Los namespaces le dan a cada contenedor su propia vista de procesos, red, usuarios y sistema de archivos, de modo que dentro del contenedor su proceso principal se ve con el numero 1 y no ve los procesos vecinos. Los cgroups, o grupos de control, limitan cuanta CPU y cuanta memoria puede consumir. Sin sistema operativo propio, los numeros cambian de escala: una imagen basada en Alpine Linux pesa del orden de 5 a 10 MB, una imagen slim de un runtime como Node ronda los 150 a 250 MB frente a cerca de 1 GB de la version completa, y el arranque es de decimas de segundo. Aqui esta la respuesta a la frase que hay que evitar: un contenedor no es «una maquina virtual ligera». La diferencia no es el peso sino el aislamiento; como el kernel es compartido, una vulnerabilidad del kernel puede afectar a todos los contenedores de esa maquina, y por eso los proveedores de nube siguen usando maquinas virtuales para separar clientes distintos y ejecutan los contenedores DENTRO de ellas. Contenedores y maquinas virtuales no compiten: se apilan.
### Dockerfile, imagen, contenedor y registro: los cuatro terminos - diapositiva 7
Cuatro terminos se confunden de forma sistematica y conviene fijarlos con una sola analogia. El Dockerfile es la receta: un archivo de texto con instrucciones. La imagen es el resultado de ejecutar esa receta, un paquete inmutable y de solo lectura con el codigo, las dependencias y la configuracion. El contenedor es una instancia en ejecucion de esa imagen, y de una misma imagen se pueden lanzar diez contenedores identicos, igual que de una clase se instancian muchos objetos; esa comparacion funciona bien con estudiantes que ya vieron programacion orientada a objetos. Y el registro, o registry, es el repositorio donde las imagenes se publican y se descargan. Un detalle que explica el comportamiento diario: la imagen se construye por capas, una por instruccion, y esas capas quedan en cache; si una instruccion no cambio, la reconstruccion la reutiliza en lugar de volver a ejecutarla. De ahi la unica optimizacion que hay que ensenar hoy: copiar primero el archivo de dependencias e instalarlas, y solo despues copiar el codigo fuente, porque el codigo cambia en cada commit y las dependencias casi nunca. Hacerlo al reves obliga a reinstalar todo en cada construccion y convierte una build de 10 segundos en una de varios minutos.
### Primer ejemplo: el stub de la API de CloudLite - diapositiva 10
Primer ejemplo concreto en CloudLite. En CloudLite Turnos el estudiante contenerizara un stub de su API, es decir una version minima que responde algo verificable, por ejemplo un endpoint llamado /salud que devuelve el texto ok. Su Dockerfile tiene seis instrucciones y el docente debe poder explicar cada una. FROM node:20-alpine elige la imagen base, o sea el punto de partida ya construido por otros, en este caso un Linux minimo con Node instalado. WORKDIR /app fija el directorio dentro del contenedor donde ocurrira todo lo demas. COPY package.json ./ trae solo la lista de dependencias. RUN npm install las instala dentro de la imagen y no en la maquina del estudiante, lo cual es el punto entero del ejercicio, porque la dependencia viaja con el artefacto. COPY . . trae el resto del codigo. EXPOSE 3000 documenta en que puerto escucha el proceso. Y CMD indica que comando ejecutar cuando el contenedor arranque. Un detalle que hay que subrayar porque genera confusion: EXPOSE no abre nada, solo documenta. Lo que realmente publica el puerto es la opcion -p al ejecutar, por ejemplo -p 8080:3000, que se lee de derecha a izquierda, ya que el puerto 3000 de dentro del contenedor queda accesible como 8080 desde fuera.
### Segundo ejemplo: leer las siete columnas de docker ps - diapositiva 6
Segundo ejemplo concreto. Tras ejecutar el contenedor, el comando docker ps lista lo que esta corriendo con siete columnas, y leerlas es parte del entregable: identificador del contenedor, imagen de la que proviene, comando en ejecucion, tiempo desde su creacion, estado, puertos publicados y nombre asignado. La columna de estado es la que hay que mirar: si dice Up seguido de un tiempo, el contenedor vive; si dice Exited con un codigo entre parentesis, murio, y ese codigo es la primera pista del problema. Un estudiante mas adelantado puede levantar dos contenedores, la API y un stub de notificaciones, y comprobar algo que sera central en la Clase 4: desde el contenedor de la API, la direccion localhost NO es la maquina anfitriona ni el otro contenedor, es el propio contenedor, y para que dos contenedores se hablen hay que ponerlos en una misma red y llamarse por nombre. Todo esto ocurre en Killercoda (killercoda.com, cuenta gratuita y sin tarjeta, escenario Ubuntu), que entrega una terminal Linux real con Docker ya instalado dentro del navegador, sin instalar Docker Desktop, que en equipos institucionales suele estar bloqueado y tiene condiciones de licencia para organizaciones grandes. Hay dos limites que conviene anunciar ANTES de empezar y no despues, porque cambian como se planifica la hora de taller. El primero: la sesion caduca a una hora y al cerrarse se pierde lo que exista solo alli. De ahi sale la regla operativa del dia, y hay que decirla como consecuencia del limite y no como consejo suelto: el Dockerfile se escribe en la carpeta del proyecto y se PEGA en el laboratorio, nunca al contrario, y las capturas se guardan antes de cerrar. El segundo: en el plan gratuito solo se trabaja un escenario a la vez, asi que no sirve dejar dos labs abiertos. La alterna, si Killercoda no carga, es LabEx Docker Playground, que cumple la misma funcion tambien gratis y en el navegador, pero con una restriccion mas dura que conviene mencionar: su plan gratuito da solo tres sesiones al dia, de modo que quien la use para depurar puede quedarse sin intentos justo el dia de la entrega. Por eso la alterna es alterna y no la primera opcion.
### Preguntas frecuentes y cierre conceptual (de la diapositiva 5 a la diapositiva 8)
Tres preguntas se repiten en esta clase. Por que mi contenedor arranca y se muere de inmediato: porque un contenedor vive exactamente lo que vive su proceso principal, y si el comando termina, el contenedor termina. No es un error, es el diseno; un contenedor no es una maquina encendida esperando ordenes, es un proceso envuelto en aislamiento, y la solucion es que el comando quede corriendo en primer plano. Segunda: donde quedan mis datos si borro el contenedor. Se pierden, porque el sistema de archivos del contenedor es efimero; para persistir hay que montar un volumen, es decir un almacenamiento cuyo ciclo de vida es independiente del contenedor, y esa es la razon por la cual una base de datos no se trata igual que una API, tema que reaparece en la Clase 7 con almacenamiento y en la Clase 13 al discutir que piezas se pueden replicar. Tercera: entonces la base de datos tambien va en un contenedor. Para desarrollo y para este curso si, y es la practica normal; en produccion la respuesta honesta es que muchas organizaciones prefieren un servicio de datos gestionado, que es precisamente la decision registrada en el ADR de la Clase 2.

Antes de cerrar hay que desactivar una colision de vocabulario que arruina la Clase 4 si no se advierte hoy. En el modelo C4, la palabra contenedor significa cualquier cosa que se ejecuta o almacena de forma independiente, como una aplicacion web, una API o una base de datos, y es un concepto de diagrama anterior a Docker. El contenedor de Docker, en cambio, es un mecanismo concreto de empaquetado y ejecucion. Se parecen y a menudo coinciden uno a uno, pero no son sinonimos: una base de datos gestionada que nadie contenerizo sigue siendo un contenedor en el sentido de C4. Decirlo hoy, mientras el estudiante tiene un docker ps en la pantalla, cuesta dos minutos; no decirlo cuesta media clase de confusion la semana siguiente, cuando se dibuje el C4 Containers de CloudLite y alguien pregunte si debe dockerizar cada caja del diagrama. La respuesta, dicha desde ya, es no.

Error tipico del docente que no domina el tema: repetir que un contenedor es una maquina virtual liviana y dejarlo ahi. El estudiante que aprende eso concluye que puede correr cualquier cosa en cualquier parte con aislamiento total, y en la Clase 6 no entendera por que el kernel compartido es un asunto de seguridad, ni por que existe la recomendacion de no ejecutar el proceso como usuario root dentro del contenedor. El segundo error es convertir la clase en un recetario de comandos: dictar docker build, docker run y docker ps al tablero para que todos copien, sin explicar la distincion entre imagen y contenedor ni el modelo de capas. Un grupo que solo copio comandos consigue la captura del entregable, pero en la Clase 8, cuando el pipeline de integracion continua deba construir una imagen automaticamente, no sabra que esta construyendo ni por que su build tarda cinco minutos, y en la sustentacion de la Clase 15 describira su arquitectura diciendo que lo metieron en Docker, que no es una decision arquitectonica sino una herramienta sin justificar.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 3 - Virtualizacion y contenedores/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 3 · Virtualización y contenedores
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. VM vs contenedor
6. Lab en navegador (pasos demo)
7. Dockerfile mínimo para el stub
8. Máquinas virtuales vs. contenedores
9. Maquina virtual vs contenedor — que cambia de verdad
10. Dockerfile minimo del stub CloudLite
11. Herramientas de hoy
12. Taller PI (paso a paso)
13. Para continuar (PI)
14. Clase 3 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 4]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Contenerizar un stub del servicio principal de CloudLite**.
Entregable concreto: Dockerfile (+ compose opcional) + captura/enlace lab navegador.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~10 min cada uno (son los títulos de las diapositivas de teoría):
- VM vs contenedor
- Lab en navegador (pasos demo)
- Dockerfile mínimo para el stub

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · 
Herramienta del día: **Killercoda · alterna si no carga: LabEx Docker Playground**.
**Demo que usted debe poder repetir:** Construir y correr el stub en Killercoda

1. Abra killercoda.com, inicie sesion con la cuenta gratuita y lance un escenario Ubuntu (advierta en voz alta: la sesion caduca a 1 h, guarden capturas antes de cerrarla).
2. Escriba un Dockerfile minimo en vivo: FROM nginx:alpine y COPY de un index.html de una linea.
3. Ejecute docker build -t cloudlite-stub . y luego docker run -d -p 80:80 cloudlite-stub.
4. Ejecute docker ps y senale las columnas IMAGE, STATUS y PORTS: «esta es la evidencia que entregan».
5. Si Killercoda no carga, la alterna es LabEx Docker Playground (ojo: solo 3 sesiones al dia en el plan gratuito); si falla la red, proyecte las capturas de `Kit docente/Clase 3/Capturas/`.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 3/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Build y run del stub en el lab del navegador (lo que debe verse en pantalla) [[captura: salida-docker-build-run.png]]
📸 Evidencia del entregable: el contenedor corriendo (`docker ps`) [[captura: salida-docker-ps.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 12]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - Virtualizacion y contenedores.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 14]
Di: «Queda avanzado: Contenerizar un stub del servicio principal de CloudLite.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: elija en la pregunta 8 cual servicio de su C4 Context va a contenedorizar y justifiquelo en 2 o 3 frases; escriba a continuacion el Dockerfile completo con la imagen base ligera y con etiqueta fija, el COPY de dependencias antes del COPY del codigo, el EXPOSE y el CMD, verificando que no copie el .env ni ninguna clave.
2. Paso 2: explique en la pregunta 9, sobre su propio Dockerfile, la diferencia entre imagen y contenedor, que instrucciones de SU archivo crean capa, por que el orden aprovecha el cache y en que se diferencia su contenedor de una maquina virtual; verifique que no escribio que un contenedor es una VM ligera.
3. Paso 3: describa en la pregunta 10 el ciclo completo con los comandos exactos de build y de run, explicando que lado del mapeo de puertos es el anfitrion y que lado el contenedor, y cierre con el contrato del endpoint de salud (ruta, codigo de estado y cuerpo); verifique que el puerto sea el mismo que puso en el EXPOSE.
4. Paso 4: ejecute de verdad el ciclo en Killercoda y reporte en la pregunta 11 la tabla de 5 filas con la salida real pegada textualmente, la descripcion de la captura con prompt, docker ps y hora del sistema, y una fila de incidente; recuerde que la sesion caduca a 1 hora, asi que capture la evidencia ANTES de cerrarla.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Decir que el contenedor «es una VM ligera». Insista en la diferencia real: kernel propio vs kernel compartido.
- Confundir imagen con contenedor al hablar. Corrija en el momento: la imagen es el molde, el contenedor la instancia corriendo.
- Perder el trabajo porque la sesion del lab caduco a la hora. Es el error mas comun del dia: recuerdeles que el Dockerfile se escribe en la carpeta del PI y se PEGA en el lab, nunca al contrario.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que comparten los contenedores de una misma maquina que las VM no comparten?
1. Cual es la diferencia entre imagen y contenedor?
1. Que pasa con su trabajo cuando caduca la sesion del lab, y donde deberia vivir el Dockerfile?

## Solución del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 3/Quiz Clase 3 - Virtualizacion y contenedores.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 3/Quiz Clase 3 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase03.png | receta: 1) Abre Killercoda · alterna si no carga: LabEx Docker Playground y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 3/Capturas/demo-clase03.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase03.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 3/Capturas/evidencia-clase03.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
