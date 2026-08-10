# Guion docente — Clase 2: Modelos de servicio: IaaS, PaaS, SaaS

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Comparar IaaS, PaaS y SaaS con criterios de control, operación y velocidad.
- Elegir el modelo dominante de CloudLite con justificación.
- Documentar la decisión como ADR reutilizable en el informe PI.

## Hoy avanzamos el PI en…
**Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**

**Entregable concreto:** ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio

**Herramienta:** Google Docs · draw.io (opcional)

## Fundamento teórico para el docente
Esta clase es autonoma: no hay encuentro sincronico y el estudiante trabaja solo con este material, por lo que el texto debe bastar por si mismo y conviene publicarlo tal cual como lectura guiada, junto con la instruccion del entregable. El punto de partida es lo definido en la Clase 1: cada equipo ya tiene un dominio para CloudLite App, tres a cinco capacidades, sus actores y un diagrama de contexto. La pregunta de hoy es la siguiente en orden logico: si ese sistema va a vivir en la nube, quien administra cada capa de la maquinaria que lo sostiene. No hay una sola respuesta, hay tres respuestas estandar que la industria llama IaaS, PaaS y SaaS, y elegir entre ellas es una decision de arquitectura con consecuencias medibles en costo, velocidad de entrega, seguridad y libertad futura.

Para entender los tres modelos hay que ver primero la pila completa de responsabilidades que existe debajo de cualquier aplicacion, de abajo hacia arriba: el edificio y la energia electrica, el hardware fisico (servidores, discos, cableado de red), la capa de virtualizacion que parte ese hardware en maquinas logicas, el sistema operativo de cada maquina, el runtime o entorno de ejecucion (por ejemplo Node.js, Python o la maquina virtual de Java) junto con servicios de apoyo como la base de datos, y finalmente el codigo de la aplicacion, sus datos y la administracion de usuarios y permisos. Son ocho o nueve capas segun como se cuente. En el modelo tradicional, llamado on-premise porque los equipos son propios y estan en las instalaciones de la organizacion, todas son responsabilidad del cliente. Los tres modelos de servicio se distinguen exactamente por donde se traza la linea que separa lo que administra el proveedor de lo que administra el cliente. Nada mas y nada menos: si el estudiante entiende esa frase, entendio la clase.

IaaS, infraestructura como servicio, corta la linea justo encima de la virtualizacion: el proveedor entrega maquinas virtuales, redes y discos, y el cliente recibe una maquina practicamente vacia con un sistema operativo que debe actualizar, endurecer, monitorear y respaldar el mismo. Lo que gana es control total, porque puede instalar cualquier version de cualquier cosa, abrir los puertos que quiera y afinar el sistema. Lo que paga es trabajo operativo permanente, que en la practica se mide en horas de persona por semana dedicadas a aplicar parches de seguridad, rotar certificados y vigilar el espacio en disco. Para CloudLite Turnos, el ejemplo de la barberia con agendamiento de citas, elegir IaaS significaria que el equipo se compromete a administrar el sistema operativo donde corren la API y la base de datos; en un curso de doce semanas con dos o tres integrantes, eso consume justamente el tiempo que deberia dedicarse a disenar la arquitectura y a sustentarla.

PaaS, plataforma como servicio, sube la linea dos escalones: el proveedor administra tambien el sistema operativo y el runtime, y el cliente entrega su codigo mas un archivo de configuracion; la plataforma lo construye, lo empaqueta y lo pone a correr. El cliente pierde el acceso a la maquina, porque ya no hay un servidor donde entrar por consola, y gana velocidad: un despliegue que en IaaS implica preparar una imagen, configurar el servicio y probar la red, en PaaS se reduce a subir el codigo al repositorio. Los niveles gratuitos tipicos de este modelo ofrecen del orden de 512 MB de memoria por instancia, una cantidad limitada de horas de ejecucion al mes y suspension automatica del servicio tras unos 15 minutos sin trafico, lo que produce el efecto conocido como arranque en frio: la primera peticion despues de la inactividad puede tardar varios segundos en lugar de milisegundos. Esos numeros son ordenes de magnitud tipicos que varian entre proveedores, no constantes; lo estructural es el patron, porque gratis siempre implica limites de memoria, de horas y de latencia en frio, y el estudiante debe anticiparlo en su diseno en vez de descubrirlo la noche antes de la sustentacion.

SaaS, software como servicio, lleva la linea hasta arriba: el proveedor administra la aplicacion completa y el cliente solo la configura y la usa, sin desplegar nada. El correo corporativo, un servicio de envio de mensajes transaccionales, un proveedor de identidad que resuelve el inicio de sesion o un servicio de almacenamiento y transformacion de imagenes son SaaS desde la perspectiva de quien construye CloudLite. Y aqui esta el punto que casi siempre se pierde: los tres modelos no son excluyentes y un sistema real los combina. La arquitectura probable de CloudLite Turnos es hibrida: la API desplegada como PaaS, la base de datos como servicio gestionado (que es PaaS en su variante de datos), el envio de recordatorios delegado a un SaaS de correo y el almacenamiento de fotos de perfil a un SaaS de archivos. El entregable de hoy no pide elegir un modelo unico para todo el sistema; pide elegir por componente y justificar cada eleccion, que es exactamente como se decide en la industria.

El concepto que unifica todo esto se llama modelo de responsabilidad compartida y se resume en una frase que conviene memorizar: el proveedor es responsable de la seguridad DE la nube y el cliente de la seguridad EN la nube. El proveedor garantiza que el centro de datos no se incendie, que la capa de virtualizacion este parcheada y que los discos esten cifrados en reposo; el cliente sigue siendo responsable de sus contrasenas, sus permisos, sus datos y su configuracion. Importa porque la causa dominante de los incidentes de seguridad en la nube no son fallas del proveedor sino configuraciones erradas del cliente: un almacenamiento de archivos dejado publico, una credencial subida al repositorio en texto plano, un puerto de base de datos expuesto a internet. Subir de IaaS a PaaS reduce la superficie de responsabilidad del cliente, pero nunca la elimina, y esa idea es el punto de partida literal de la Clase 6. De ahi sale el trade-off central, que se escribe como regla practica: a mas abstraccion, menos control y menos trabajo operativo. Pero hay un tercer eje que el estudiante no ve solo, el amarre al proveedor o vendor lock-in, que es el costo de mudarse a otro proveedor mas adelante: bajo en IaaS, porque una maquina virtual con Linux se parece a cualquier otra; medio en PaaS, porque el archivo de configuracion y algunos servicios son propietarios; potencialmente alto en SaaS, porque los datos y parte de la logica viven dentro de un producto ajeno. Para CloudLite la mitigacion no es evitar SaaS sino acotarlo: si el envio de correos se encapsula detras de una interfaz propia, por ejemplo un modulo Notificador con un solo metodo enviar, cambiar de proveedor toca un archivo y no cuarenta.

El entregable concreto es el ADR-001. Un ADR (Architecture Decision Record, registro de decision arquitectonica) es un documento corto, de media pagina a una pagina, que registra UNA sola decision con cinco secciones fijas: titulo con numero consecutivo, contexto (que problema y que restricciones existen), opciones consideradas, decision tomada y consecuencias. La regla de una decision por documento no es burocracia: es lo que permite que meses despues alguien lea por que se eligio algo sin depender de la memoria de nadie. Un ADR-001 aceptable para CloudLite Turnos diria en contexto: equipo de tres personas, doce semanas, sin presupuesto ni tarjeta de credito, y se requiere que el sistema este disponible el dia de la sustentacion. En opciones: IaaS con maquina virtual propia, descartada porque el equipo asumiria parches y respaldos del sistema operativo sin tiempo para ello; y SaaS de agendamiento ya existente, descartada porque el proyecto perderia su objeto, ya que no habria arquitectura que disenar sino solo configuracion. En decision: PaaS para la API, base de datos gestionada y SaaS para el correo. Y en consecuencias, que es la seccion que los estudiantes dejan vacia, deben aparecer tambien las malas: se acepta un arranque en frio de varios segundos tras inactividad, se acepta no poder afinar el sistema operativo y se acepta un amarre medio al proveedor, mitigado con contenedores.

Tres preguntas llegan por escrito en toda clase autonoma y conviene responderlas por anticipado en el mismo material. Cual de los tres modelos es el mejor: ninguno; la pregunta correcta es cual conviene para este componente, con este equipo y en este plazo, y responder que PaaS es mejor sin decir para que es la senal de que el ADR sera de relleno. Donde encaja serverless o las funciones como servicio: es una variante extrema de PaaS en la que no se administra ninguna instancia siempre encendida, se paga por invocacion y el codigo debe tolerar arrancar en frio; para efectos del curso se clasifica como PaaS anotando la diferencia. Y la mas comun: si elegimos PaaS, para que aprendemos Docker en la Clase 3 si la plataforma se encarga de todo. Respuesta: porque la plataforma construye internamente una imagen de contenedor con el codigo entregado, de modo que entender contenedores es entender que hace la plataforma por debajo, y porque el contenedor es precisamente el artefacto que vuelve reversible la decision de hoy. La Clase 4 usara este mismo ADR para justificar cuantas piezas tendra el sistema, y el Parcial 1 de la Clase 5 evalua la capacidad de ubicar la linea de responsabilidad en cada modelo.

Error tipico del docente que no domina el tema: presentar IaaS, PaaS y SaaS como catalogos de marcas y no como un modelo conceptual de responsabilidad, con lo cual el estudiante memoriza nombres de productos que cambiaran en dos periodos y no aprende a preguntar quien administra que capa; aguas abajo, en la Clase 6 sera incapaz de decir de que es responsable su equipo en materia de seguridad, y en la Clase 10 no podra explicar por que su factura hipotetica sube o baja. El segundo error, especifico de una clase autonoma sin encuentro sincronico, es recibir ADR sin consecuencias negativas y darlos por buenos: un ADR que solo lista beneficios no es una decision, es una justificacion escrita despues de los hechos, y el equipo que lo entrega asi llegara a la Clase 11 sin poder explicar ningun trade-off de su arquitectura, que es justamente lo que se le exigira sustentar en la Clase 15.

Referencia de slides: `Clases/Clase 2 - Modelos de servicio IaaS PaaS SaaS/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### Modalidad autónoma (festivo)
Esta clase cae en festivo: no hay encuentro síncrono obligatorio. El estudiante trabaja solo,
con `Presentacion.pptx` + el taller de la carpeta `Clases/`. Por eso el material publicado
tiene que ser **autosuficiente**: lo que no quede escrito, nadie lo va a explicar en vivo.

### Qué publicar (antes del día de la clase)
1. En ExamLab: las diapositivas, el taller y el recordatorio del hito del PI.
2. La sección «Fundamento teórico para el docente» de este guion, adaptada como **lectura guía**
   del estudiante — es el reemplazo de la explicación en vivo, no un anexo opcional.
3. La **salida esperada** del ejercicio (ver la demo de abajo), para que el estudiante autónomo
   pueda comparar y saber si le quedó bien sin preguntarte.
4. Mensaje sugerido: «Clase 2 autónoma (festivo). Hoy avanzamos el PI en: Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve.
   Entregable: ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio. Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a ExamLab.

### La demo, en versión asíncrona
**Demo que usted debe poder repetir:** Llenar un ADR-001 delante del grupo, en 6 lineas

1. Abra un Google Doc y escriba los 4 encabezados del ADR: Contexto, Opciones, Decision, Consecuencias.
2. Contexto: «CloudLite necesita correr una API y una base de datos; el equipo tiene 3 personas y cero presupuesto».
3. Opciones: IaaS (control total, mas trabajo operativo) · PaaS (menos control, menos operacion) · SaaS (no aplica, no compramos software hecho).
4. Decision: PaaS conceptual + contenedores. Consecuencias: se acepta menos control del sistema operativo a cambio de no administrar servidores.
5. Diga: «un ADR de media pagina que se entiende vale mas que 5 paginas que nadie lee».

Publica esto como pasos escritos o como un video corto (3–5 min) grabado con estos mismos pasos.
Sin uno de los dos, el estudiante autónomo no tiene con qué comparar su resultado.


### Seguimiento (lo que sí es tu trabajo esa semana)
1. Revisa las entregas del domingo 23:59 con la lista de errores frecuentes de abajo:
   en modalidad autónoma esos errores aparecen más, porque nadie los corrigió en el momento.
2. Deja feedback breve orientado a la rúbrica del PI, nombrando el error y la corrección.
3. En la siguiente clase regular, dedica los primeros 10 min a los 2 errores más repetidos.
   Es el sustituto de la retroalimentación en vivo que esta clase no tuvo.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos concretos de diagrama/ADR/lab. Usa las preguntas de comprobación de abajo
para detectar quién entendió y quién solo copió la plantilla. No adelantes contenido de Parcial.


## Actividad / taller (detalle)
1. Lea las diapositivas y el enunciado del PI (Clases/Proyecto Integrador).
2. Complete una matriz IaaS/PaaS/SaaS vs su dominio (control, costo cualitativo, operación, time-to-demo).
3. Redacte ADR-001 (decisión dominante + 2 alternativas descartadas).
4. Actualice el informe PI (sección «Modelo de servicio»).
5. Entrega domingo 23:59 en **ExamLab** (Talleres) — mismo doc del PI o anexo.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Elegir el modelo de servicio por moda y no por trade-off. Pida la frase «aceptamos perder X para ganar Y» escrita en el ADR.
- ADR sin alternativas descartadas: un ADR con una sola opcion no documenta una decision, documenta un hecho.
- Nombrar productos de marca en vez del modelo conceptual; el modelo aplica a cualquier proveedor.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Quien administra el sistema operativo en IaaS, en PaaS y en SaaS?
1. Que perdieron y que ganaron con el modelo que eligieron?
1. Por que un ADR necesita las alternativas que descartaron?

## Solución del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los equipos. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 2/Quiz Clase 2 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase02.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (https://examlab.lovable.app/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
