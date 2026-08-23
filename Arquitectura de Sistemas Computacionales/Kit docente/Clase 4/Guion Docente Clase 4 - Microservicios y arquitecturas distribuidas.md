# Guion docente — Clase 4: Microservicios · Arquitecturas distribuidas

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Contrastar monolito vs microservicios con criterios de equipo y acoplamiento.
- Modelar CloudLite en C4 Container/Componentes sin exceso de servicios.
- Definir 3 contratos/API entre partes del sistema.

## Hoy avanzamos el PI en…
**Diagramar componentes/servicios de CloudLite y sus contratos**

**Entregable concreto:** Diagrama C4 Container/Componentes v0.9 + lista de APIs entre servicios

**Herramienta:** draw.io / diagrams.net

## Fundamento teórico para el docente
La Clase 3 dejo al estudiante con una unidad de despliegue concreta en las manos: una imagen que se ejecuta como contenedor. La Clase 1 le dejo una caja negra llamada CloudLite App con actores y sistemas externos alrededor. Hoy se juntan las dos cosas: se abre la caja negra y se decide de cuantas piezas esta hecha por dentro y por que. Ese es el nivel 2 del modelo C4, el de contenedores, y el entregable es ese diagrama mas una tabla de riesgos de distribucion. La pregunta que organiza la clase no es que son los microservicios, sino una mas incomoda y mas util: cada vez que un sistema se parte en dos, se gana algo y se paga algo, y hoy hay que decir explicitamente que se gana y que se paga. Un estudiante que solo aprende la primera mitad de esa frase sale convencido de que mas servicios es mejor arquitectura, que es exactamente el error que esta clase debe prevenir.

Empecemos por el termino que el estudiante trae con mala fama. Un monolito es un sistema que se despliega como una sola unidad: todo su codigo se construye junto y sale al aire junto. No es un insulto ni un error, es la arquitectura correcta por defecto para la mayoria de los sistemas pequenos, y varios proyectos de este curso deberian ser monolitos bien organizados. Un microservicio, en cambio, es una unidad de despliegue independiente con una frontera de responsabilidad de negocio propia. La palabra decisiva es independiente, y admite una prueba de una linea que el docente debe usar como criterio de correccion: si para poner en produccion el servicio A hay que desplegar tambien el servicio B, entonces A y B no son dos microservicios, son un solo sistema partido en dos repositorios, con todos los costos de la distribucion y ninguno de sus beneficios. Tres senales de una frontera real: el servicio es dueno de sus propios datos, puede liberarse a su propio ritmo y corresponde a una capacidad de negocio que se puede nombrar sin usar palabras tecnicas. En cuanto a la notacion, el nivel de contenedores del modelo C4 pide dibujar, dentro del sistema, cada cosa que se ejecuta o almacena de forma independiente, con tres datos obligatorios por caja (nombre, tecnologia y responsabilidad en una frase) y cada flecha etiquetada con protocolo y proposito, nunca una linea muda. Aqui hay que repetir la advertencia de la clase pasada, porque es la fuente numero uno de confusion: contenedor en C4 no significa contenedor de Docker. Una aplicacion web de una sola pagina que corre en el navegador, una API, una base de datos gestionada, una cola de mensajes y un proceso trabajador en segundo plano son cinco contenedores C4, aunque solo dos de ellos esten dockerizados. Confundirlo lleva al estudiante a creer que debe empaquetar cada caja con Docker para que el diagrama sea valido, lo cual no es cierto y desvia el trabajo de la semana hacia una tarea que nadie pidio.

Primer ejemplo concreto, y conviene construirlo en el tablero en vivo. CloudLite Turnos, el sistema de agendamiento de la barberia, empieza con tres contenedores: una aplicacion web que corre en el navegador del cliente, una API que atiende peticiones HTTP con cuerpo en formato JSON, y una base de datos relacional donde viven turnos, clientes y horarios. La flecha entre la web y la API dice «HTTPS/JSON, consulta disponibilidad y crea reservas»; la flecha entre la API y la base de datos dice «TCP, lee y escribe turnos». Con eso ya existe un diagrama valido y defendible. Ahora viene la parte interesante: la cuarta caja aparece solo si hay una razon. El envio del correo de confirmacion tarda, con proveedores reales de correo, entre 300 y 2000 milisegundos, y puede fallar por causas ajenas al sistema. Si la API espera ese envio antes de responder, la reserva de un turno hereda esa latencia y ese riesgo. Esa es una razon legitima para separar: se agrega una cola de mensajes y un trabajador de notificaciones, la API escribe el turno, publica un mensaje y responde en decenas de milisegundos, y el trabajador envia el correo despues, con reintentos si falla. Cuatro contenedores con una justificacion medible es mejor arquitectura que ocho por moda.

El segundo bloque de contenido es el mas importante del dia: que se paga al distribuir. Una llamada a una funcion dentro del mismo proceso cuesta del orden de nanosegundos y no puede fallar por causas de red. La misma llamada convertida en peticion HTTP entre dos contenedores de la misma maquina o del mismo centro de datos cuesta tipicamente entre 1 y 5 milisegundos, y entre regiones geograficas distintas puede subir a 50 o 200 milisegundos. Es decir, convertir una llamada local en remota empeora el costo en varios ordenes de magnitud, y a eso se suma que ahora la llamada puede perderse, llegar duplicada o tardar indefinidamente. Hay una aritmetica que conviene mostrar porque impresiona con razon: si una peticion del usuario atraviesa en cadena cinco servicios y cada uno esta disponible el 99,9 % del tiempo, la disponibilidad del recorrido completo es 0,999 elevado a la quinta potencia, alrededor del 99,5 %, lo que pasa de unos 43 minutos de indisponibilidad al mes a mas de tres horas. Ese calculo es exacto y no una convencion, y es el argumento mas contundente contra multiplicar servicios sin necesidad.

De ahi salen cuatro mecanismos que el diagrama y la tabla deben poder mencionar. Un timeout es el tiempo maximo que un servicio espera respuesta antes de darse por vencido; sin timeout explicito, un servicio lento no falla sino que deja colgado a quien lo llamo, y el bloqueo se propaga hacia arriba hasta tumbar el sistema completo. Los valores tipicos para llamadas internas estan entre 2 y 5 segundos, y son convencion, no ley. Un reintento es volver a intentar la llamada fallida, y trae una trampa: si todos los clientes reintentan de inmediato contra un servicio ya saturado, lo hunden mas, por lo que se limita a dos o tres reintentos con espera creciente entre uno y otro. Los reintentos exigen idempotencia, que significa que ejecutar la misma operacion dos veces produzca el mismo resultado que ejecutarla una vez. En CloudLite eso es literal: si el reintento de crear turno no es idempotente, el cliente termina con dos reservas para el mismo horario, y la solucion habitual es que la peticion lleve un identificador unico que el servidor reconozca como repetido. El cuarto mecanismo es el interruptor de circuito, o circuit breaker, que tras varias fallas consecutivas deja de intentar por un rato y responde de inmediato con un error controlado, para no gastar recursos golpeando algo que esta caido.

El punto donde los proyectos academicos se rompen es el de los datos. La regla ortodoxa de los microservicios dice que cada servicio es dueno exclusivo de su base de datos y que nadie mas la consulta directamente; si dos servicios comparten tablas, estan acoplados y no pueden desplegarse por separado, lo que contradice la definicion. Pero cumplir esa regla tiene un precio real: una consulta que antes era un join deja de existir y hay que resolverla llamando a otro servicio, y una operacion que abarca dos servicios ya no puede ser una transaccion unica sino una secuencia de pasos con compensaciones. Eso introduce consistencia eventual, es decir un lapso durante el cual dos partes del sistema tienen versiones distintas de la verdad, con consecuencias visibles para el usuario. La postura honesta para este curso, y hay que enunciarla en voz alta, es que un CloudLite con una base de datos compartida y propiedad de tablas claramente documentada resulta aceptable, siempre que el estudiante lo registre como un trade-off consciente en su informe y no lo presente como microservicios puros. Fingir ortodoxia es peor que documentar una concesion.

El segundo entregable, la tabla de riesgos de distribucion, es lo que impide que la clase quede en pura teoria. Debe tener cinco columnas y entre cuatro y seis filas, no mas: riesgo enunciado como frase de falla, componente afectado, impacto en el usuario, mitigacion concreta y donde queda la evidencia. Filas esperables en CloudLite Turnos: «el proveedor de correo no responde» afecta al trabajador de notificaciones, el usuario reserva pero no recibe confirmacion, y se mitiga con cola mas reintentos con espera creciente y un aviso en pantalla de que el correo puede tardar; «la base de datos alcanza su limite de conexiones» afecta a la API, todos los usuarios ven errores, y se mitiga con un pool de conexiones acotado; «el reintento duplica la reserva» se mitiga con un identificador de operacion idempotente. Si un estudiante dice que no encuentra riesgos, casi siempre es porque su diagrama tiene flechas sin protocolo: no sabe por donde puede romperse porque nunca definio como se comunican las piezas.

Las preguntas de esta clase son predecibles y conviene responderlas con firmeza. Cuantos microservicios son los correctos: no hay numero correcto, hay justificacion por frontera, y el rango de dos a cinco contenedores que exige el curso es una restriccion pedagogica pensada para proyectos de una a tres personas en doce semanas, no un hallazgo de la ingenieria. Si las empresas grandes tienen cientos de servicios, por que nosotros solo tres: porque el numero de servicios que una organizacion puede sostener es funcion del numero de equipos autonomos y de la madurez de su automatizacion de despliegue y observabilidad, condiciones que un equipo de tres no tiene, y copiar la forma sin las condiciones produce lo que aqui se llama microservicios teatro. Y la tercera, que hay que responder sin ambiguedad: esta mal hacer un monolito. No; esta mal hacerlo sin saber que se eligio, y un monolito modular bien argumentado recibe mejor calificacion que cinco servicios sin razon. Conviene cerrar ubicando el curso: este diagrama es el ultimo insumo del Parcial 1 de la Clase 5; en la Clase 6 cada flecha se convertira en una superficie de ataque que hay que proteger; en la Clase 7 estas mismas cajas se reubicaran en un diagrama de despliegue con zonas publicas y privadas, conservando exactamente los mismos nombres; en la Clase 8 cada contenedor implicara su propio pipeline de integracion continua; y en las Clases 12 y 13 se preguntara cual de estas piezas es el cuello de botella y cual se puede replicar.

Error tipico del docente que no domina el tema: aplaudir un diagrama con ocho microservicios sin preguntar por que existe cada uno. El numero de servicios no mide calidad arquitectonica; la justificacion de cada frontera si. La consecuencia aguas abajo es que ese estudiante llega a la Clase 7 con ocho cajas que no puede ubicar en zonas de red, a la Clase 8 con ocho pipelines que nunca construira y a la Clase 12 sin poder identificar un cuello de botella, porque no entiende el flujo de su propio sistema. El segundo error es tratar la latencia y los fallos parciales como un detalle de implementacion que se vera despues: si hoy no se dice que una flecha en el diagrama es una llamada de red que puede fallar, el estudiante disenara como si distribuir fuera gratis, no incluira timeouts ni idempotencia en su tabla de riesgos, y en la Clase 13 pedira autoescalado como solucion magica a un problema de diseno originado precisamente en esta clase.

Referencia de slides: `Clases/Clase 4 - Microservicios y arquitecturas distribuidas/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Diagramar componentes/servicios de CloudLite y sus contratos**.
Entregable concreto: Diagrama C4 Container/Componentes v0.9 + lista de APIs entre servicios.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller)
Cubre estos conceptos, en este orden, ~10 min cada uno (son los títulos de las diapositivas de teoría):
- Monolito vs microservicios (para el PI)
- C4-lite en draw.io
- Distribuido implica fallos

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo
Herramienta del día: **draw.io / diagrams.net**.
**Demo que usted debe poder repetir:** Convertir el Context de la Clase 1 en Containers

1. Abra el diagrama C4 Context de la demo de Clase 1 y haga zoom a la caja «CloudLite App».
2. Reemplace esa caja por 3 cajas internas: «API (REST)», «Base de datos» y «Worker de notificaciones».
3. Rotule CADA flecha con protocolo y formato: «HTTPS/JSON», «TCP/SQL». Sin flechas sin etiqueta.
4. Pregunte al grupo por que el worker esta separado; si nadie da una razon de negocio, borrelo en vivo: «eso es microservicios teatro».

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 4/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste)
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 4/Quiz Clase 4 - Microservicios y arquitecturas distribuidas.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre
Di: «Queda avanzado: Diagramar componentes/servicios de CloudLite y sus contratos.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: abran el C4 Context de la Clase 1 y escriban la lista canonica de nombres de CloudLite: exactamente 5 contenedores con nombre, responsabilidad en una frase y tecnologia tentativa (por ejemplo SPA Web, API CloudLite, Worker Notificaciones, Base de datos Citas, Cola Notificaciones), verificando que ninguno de los 5 sea un modulo interno de otro y que ningun nombre se repita; esa lista se congela y la reutilizan las clases 7, 11 y 15.
2. Paso 2: escriban en ExamLab el diagrama C4Container en Mermaid con los 5 contenedores dentro de un Container_Boundary, los 2 Person y los 2 System_Ext de la Clase 1, y 8 relaciones etiquetadas con protocolo y puerto, verificando al renderizar que la base de datos usa ContainerDb, la cola usa ContainerQueue y que ningun actor habla directamente con la base de datos.
3. Paso 3: definan los 3 contratos entre partes en una tabla de 6 columnas (ID, consumidor a proveedor, verbo y ruta, request, respuesta 2xx, error de negocio), verificando que al menos un contrato sea asincrono por evento y que cada fila declare un codigo de error de negocio real como 409 CUPO_OCUPADO o 401 TOKEN_INVALIDO, no solo 500.
4. Paso 4: escriban el sequenceDiagram del contrato principal con 5 participantes y un bloque alt que cubra el camino feliz y el camino de error 409, verificando que los nombres de los participantes sean identicos a los 5 contenedores del paso 1 y que el mensaje de error muestre el mismo codigo declarado en la tabla de contratos.
5. Paso 5: redacten los 3 riesgos de distribucion con su mitigacion, actualicen la seccion Arquitectura logica del informe con el diagrama y la tabla de contratos, y suban las 5 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que la lista canonica de 5 nombres aparezca identica en el diagrama, en los contratos y en el informe.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Inventar 6 u 8 servicios para verse sofisticados. Pregunte por cada uno: que responsabilidad de negocio propia tiene y quien lo despliega por separado.
- Flechas sin etiqueta entre servicios. Toda flecha lleva protocolo y formato de datos.
- Olvidar que distribuir agrega fallos parciales: exija al menos 2 riesgos de red en la tabla.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que justifica que dos funciones vivan en servicios separados?
1. Que cambia cuando una llamada de funcion se vuelve una llamada de red?
1. Como se llama en su C4 Containers el servicio que expone la API?

## Solución del taller (privada)
`Kit docente/Clase 4/Solucion Taller Clase 4 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 4/Quiz Clase 4 - Microservicios y arquitecturas distribuidas.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 4/Quiz Clase 4 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase04.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
