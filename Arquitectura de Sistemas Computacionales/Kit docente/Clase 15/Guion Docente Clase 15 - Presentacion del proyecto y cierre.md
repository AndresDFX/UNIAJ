# Guion docente — Clase 15: Presentación del proyecto + cierre

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Sustentación del Proyecto Integrador · **en vivo** (síncrona)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Sustentar en vivo CloudLite App con evidencias completas.
- Responder en vivo preguntas de arquitectura (ADRs, amenazas, escala).
- Cerrar el curso con reflexión de aprendizaje.

## Hoy avanzamos el PI en…
**Sustentar en vivo el PI CloudLite App y entregar el paquete final**

**Entregable concreto:** Paquete final en ExamLab (módulo Proyectos) + pitch de 5–8 min sustentado hoy en clase + Q&A

**Herramienta:** Google Docs/Slides · diagramas · capturas lab

## Fundamento teórico para el docente
Sustentar no es describir, y esa distincion es el eje de toda la clase. Describir un artefacto es decir que contiene: «este es el diagrama de despliegue de CloudLite App, aqui esta el contenedor de la API, aqui la base de datos». Sustentar es responder por que quedo asi y no de otra forma, y que se acepto perder al elegirlo. Conviene fijar el termino con precision: una decision de arquitectura es una eleccion que afecta la estructura del sistema, es costosa de revertir una vez implementada, y tiene al menos una alternativa razonable que se descarto. Si una eleccion no cumple esas tres condiciones no es arquitectura sino detalle de implementacion: elegir el nombre de una variable no es arquitectura, elegir si el frontend y la API viven en el mismo contenedor si lo es. Un trade-off es lo que se sacrifica al tomar esa decision. No existe decision de arquitectura sin trade-off, y cuando un estudiante afirma que su opcion es mejor en todo, lo que ocurre en realidad es que todavia no encontro que perdio. Toda la sustentacion de hoy se apoya en esta distincion, porque la rubrica no premia describir bien: premia justificar bien.

Existe una prueba practica de tres capas que el docente puede aplicar en voz alta a cualquier afirmacion del estudiante, y conviene ensenarla antes de que empiecen las presentaciones. Primera capa, el QUE: «CloudLite corre con un contenedor por servicio». Segunda capa, el POR QUE: «porque el proyecto lo sostiene una sola persona sin presupuesto de nube, y un contenedor se levanta igual en el portatil de cualquiera y en LabEx Docker Playground, sin instalar un hipervisor ni pedir tarjeta de credito». Tercera capa, A CAMBIO DE QUE: «a cambio de perder el aislamiento fuerte que da una maquina virtual completa, y de asumir que si el host cae, caen todos los servicios a la vez porque comparten el mismo kernel». Quien solo llega a la primera capa esta leyendo el diagrama en voz alta y no deberia obtener los puntos de sustentacion. Quien llega a la segunda esta justificando. Quien llega a la tercera esta sustentando como un arquitecto, porque demuestra que conocia el costo de su decision antes de tomarla y aun asi la tomo. La instruccion operativa para el docente es simple: ante cada afirmacion, preguntar «a cambio de que», y no aceptar la respuesta «de nada».

El artefacto que sostiene esa tercera capa es el ADR, o Architecture Decision Record: un documento corto, de una pagina como maximo, que registra UNA sola decision con cuatro secciones fijas. Contexto, es decir que problema se estaba resolviendo y con que restricciones. Decision, en una frase afirmativa y en presente. Alternativas descartadas, al menos dos, cada una con la razon concreta del descarte. Y consecuencias, donde se escribe lo bueno, lo malo y lo neutro que se acepta. Los estudiantes ya produjeron el ADR-001 en la Clase 2, cuando decidieron el modelo de servicio dominante entre IaaS, PaaS y SaaS; a lo largo del curso debieron acumular tres o cuatro mas: contenedores frente a maquinas virtuales (Clase 3), donde poner la frontera entre servicios (Clase 4), y que se escala y que no (Clase 13). En la sustentacion el ADR no se lee en voz alta: se cita. La forma profesional es «esta decision esta registrada en el ADR-002, y el trade-off que aceptamos fue perder portabilidad entre proveedores», con el numero del ADR visible en la diapositiva. Citar un ADR por numero le dice al evaluador que existe una traza escrita y verificable, no una improvisacion del momento; es la diferencia entre quien decidio y quien recuerda.

Un pitch tecnico de 5 a 8 minutos no se improvisa ni se llena de diapositivas. El reparto que funciona, y que es convencion de industria y no regla dura, es el siguiente: 45 a 60 segundos para el problema y el dominio, es decir que hace CloudLite y para quien, sin nombrar una sola tecnologia todavia; 90 segundos para la arquitectura, apoyandose en el diagrama de contexto y el de contenedores; 90 segundos para la decision principal con su trade-off, citando el ADR; 60 a 90 segundos para la evidencia ejecutable, o sea la captura de la sesion de LabEx Docker Playground con el contenedor corriendo y el workflow de GitHub Actions en verde; 45 segundos para el punto debil declarado, lo que no escala o lo que no se midio; y 30 segundos de cierre. La suma queda entre 6 y 7 minutos, con margen para tropiezos. La regla practica de diapositivas es una idea por diapositiva y un maximo de ocho diapositivas para ocho minutos. La razon es concreta y el docente debe decirla: si el estudiante trae veinte diapositivas, no termina, corre las ultimas, y las ultimas suelen ser justamente las de seguridad, costos y escalabilidad, donde estan los puntos de la rubrica que menos se defienden solos.

El criterio de calidad que se anuncio desde el checkpoint de la Clase 11 es la regla de los 60 segundos: quien sustenta debe poder explicar CUALQUIER parte del sistema en 60 segundos, sin buscar en el informe. El trabajo es individual por defecto, asi que en la mayoria de los casos ese "quien" es el propio autor y la regla se comprueba sola; cuando el docente autorizo un equipo de dos o tres, la regla se vuelve exigente y se lee asi: CUALQUIER integrante debe poder explicar CUALQUIER parte. Esto casi siempre genera la primera pregunta real del estudiante: «podemos repartirnos los temas y que cada uno prepare solo el suyo?». La respuesta del docente debe ser: en equipo se puede repartir quien HABLA de cada tema, pero no quien ENTIENDE cada tema, porque el Q&A se dirige al azar; y en modo individual no hay reparto posible, de modo que la pregunta pierde sentido y lo que queda es preparar el sistema completo. La razon no es castigar. En un equipo profesional, cuando el sistema falla a las once de la noche, contesta quien esta disponible, no el autor del diagrama; un sistema que solo una persona entiende es un riesgo operativo con nombre propio. El segundo motivo es de evaluacion: si el estudiante no puede explicar su propio diagrama de despliegue, el evaluador no tiene forma de saber si el artefacto es suyo o copiado, y ese es exactamente el vacio que la sustentacion existe para cerrar. En los equipos autorizados el mismo riesgo se multiplica: si solo un integrante puede explicar el despliegue, no hay evidencia de que los demas participaran, y por eso la rubrica exige que todos hablen y descuenta cuando presenta uno solo. La practica concreta que se recomienda antes de presentar es un ensayo cruzado con otro estudiante: cada uno explica en 60 segundos una parte del sistema del otro y devuelve los huecos que encontro (en equipo, cada integrante explica una parte que NO le toco preparar). Ese ejercicio suele revelar en cinco minutos lo que la nota habria revelado demasiado tarde.

El Q&A tecnico tiene tres tipos de pregunta y conviene que el docente los reconozca para dosificarlos. La pregunta de verificacion comprueba que el estudiante hizo lo que dice: «muestreme el archivo .yml del workflow» o «en que linea del Dockerfile esta la imagen base y por que eligieron una variante alpine». La pregunta de profundizacion empuja un nivel mas alla de lo presentado: «por que la base de datos no esta en el mismo contenedor que la API». La pregunta hipotetica, o what-if, evalua si el diseno se entiende como sistema y no como dibujo: «si el trafico se multiplica por diez el lunes, que pieza de CloudLite se rompe primero y como se darian cuenta». Aqui aparece la segunda pregunta previsible del estudiante: «y si no sabemos la respuesta?». La respuesta correcta es que decir «no lo medimos» no penaliza si va acompanado de como se mediria: «no medimos el p95 porque no hay trafico real, pero el plan es simular 50 peticiones por segundo y observar la latencia de la API, que es el cuello de botella que sospechamos por lo que vimos en la Clase 12». Improvisar un dato falso, en cambio, se detecta con una sola pregunta de seguimiento y cuesta mucho mas que admitir el limite. Y conviene ser explicito sobre el formato de la sesion, porque es lo que decide como se prepara el estudiante: la Clase 15 se dicta en la ultima sesion del semestre (16 de noviembre) como sustentacion EN VIVO, sincrona, con turnos de unos 6 minutos de pitch y 2 a 4 de preguntas. No es clase autonoma y la defensa no se reemplaza por un video grabado, porque el Q&A dirigido al azar es justamente el instrumento que verifica autoria y no tiene sustituto asincronico. El Q&A escrito que pide el taller (tres preguntas duras que el propio estudiante se haria, con su respuesta) no reemplaza nada: es la preparacion del Q&A en vivo, y en la practica el estudiante que lo escribio en serio responde mucho mejor cuando la pregunta llega de verdad.

Evaluar con rubrica significa asignar puntos a evidencia observable y no a impresion general, y por eso conviene leer el reparto en voz alta al abrir la clase. Los 100 puntos del PI CloudLite App se distribuyen asi: 15 puntos por dominio y decision IaaS/PaaS/SaaS justificada, 25 por los diagramas de arquitectura (componentes y despliegue), 20 por el lab de contenedores con Dockerfile o compose mas la captura de la sesion, 15 por el CI/CD conceptual con el workflow .yml explicado, 10 por las secciones de seguridad, costos y escalabilidad del informe, y 15 por informe y sustentacion. Ese reparto responde la tercera pregunta previsible: «si el diagrama esta perfecto pero presentamos mal, cuanto pierdo?». Directamente, hasta 15 puntos. Indirectamente mucho mas, porque la sustentacion es el mecanismo con el que el evaluador verifica que los otros 85 puntos son de quien sustenta: un diagrama excelente que nadie puede explicar levanta una duda de autoria que ninguna diapositiva resuelve. Y va el recordatorio de pesos que evita reclamos posteriores: estos 100 puntos valen 20% del Corte 3, el Parcial 3 de la Clase 14 (9 de noviembre, presencial y escrito) vale 15%, y la asistencia 5%. El proyecto no reemplaza ni compensa el parcial; son evaluaciones distintas del mismo corte, y decirlo una vez hoy ahorra tres correos la semana siguiente.

El cierre del curso debe conectar lo hecho con la practica profesional, porque de eso depende que el estudiante conserve el material en vez de borrarlo al terminar el semestre. En la industria, esta sustentacion tiene nombre propio: design review, o architecture review. Un equipo presenta una propuesta a pares y a arquitectos mas experimentados cuyo trabajo explicito es buscarle el punto debil antes de que ese punto debil cueste dinero; y lo que se pregunta ahi es exactamente lo mismo que hoy, es decir que decidieron, que descartaron, que aceptaron perder, y como sabran si se equivocaron. El ADR es un formato real, usado en equipos reales, no un invento academico del curso. Conviene tambien cerrar la duda sobre las herramientas, porque algun estudiante la trae: el curso prohibio la nube de pago por razones pedagogicas y de equidad, no porque draw.io, LabEx Docker Playground y GitHub Actions sean juguetes. El diagrama de contenedores, el Dockerfile y el pipeline que el estudiante escribio son los mismos artefactos que se producen con una cuenta corporativa; lo que no se aprende en un free tier es justamente lo que si se aprendio aqui, que es razonar el trade-off. La frase de cierre util es que arquitectura no es una lista de logos de proveedores, sino un conjunto de decisiones documentadas con sus consecuencias. Y el pedido final debe ser concreto y verificable: conserven el repositorio con el informe, los diagramas y el workflow como portafolio, porque eso es lo que se muestra en una primera entrevista tecnica cuando piden un ejemplo de trabajo propio.

Error tipico del docente que no domina el tema: el primero es dar por sustentado un paquete sin haber hecho una sola pregunta al azar, y en los equipos autorizados permitir que un solo integrante presente todo mientras los demas observan en silencio, normalmente porque es el que habla mejor y la presentacion sale mas fluida. La consecuencia aguas abajo es la misma en los dos casos: el docente pierde el unico instrumento que tenia para verificar autoria individual, y cuando llegue el reclamo de nota no tendra con que sostener la calificacion de quien no hablo. El segundo es aceptar como sustentacion la lectura descriptiva del diagrama, del tipo «aqui esta la API, aqui la base de datos, aqui el balanceador», sin exigir nunca la tercera capa del trade-off. La consecuencia es que el estudiante cierra el curso creyendo que arquitectura es dibujar cajas, y en la siguiente asignatura o en su primer empleo no sabra defender una decision frente a un lider tecnico que le pregunte por el costo de mantenerla. Un tercer tropiezo menor pero muy frecuente: dejar el Q&A para el ultimo minuto y quedarse sin tiempo, con lo cual los 15 puntos de informe y sustentacion se califican sobre la presentacion sola y se pierde precisamente la parte que mas informacion da sobre lo que el estudiante realmente entendio.

Referencia de slides: `Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### Modalidad de la sesión: sustentaciones EN VIVO
Este bloque de 120 min se dedica íntegramente a las sustentaciones del Proyecto Integrador,
con encuentro síncrono. **No es clase autónoma y no es parcial.** No autorices reemplazar la
defensa por un video grabado: la sustentación es el único instrumento con el que verificas
autoría de los otros puntos del PI, y el Q&A en vivo no se puede sustituir por un documento.
El día cae en festivo de calendario, pero la sesión está destinada por decisión docente a
sustentar: anúncialo por escrito una semana antes para que nadie asuma que no hay clase.

### Antes de la sesión (semana previa)
1. Publica el orden y la duración exacta del turno: **6 min de pitch + 2–4 min de Q&A**.
   Con 12 sustentaciones eso es ~110 min; si el grupo es más grande, baja a 5 + 2 y avísalo
   antes, nunca el mismo día.
2. Exige el paquete subido a ExamLab (módulo Proyectos) **antes** del bloque: quien llega a
   subir archivos consume el tiempo de otro. Verifica tú mismo que los enlaces abren.
3. Ten a mano la rúbrica impresa por estudiante y la lista de preguntas de comprobación de
   abajo, para no improvisar el Q&A ni preguntar lo mismo a todos.
4. Si en la clase anterior no alcanzaron a ensayar, modela tú el formato antes de abrir turnos
   (no dentro de este bloque: no hay tiempo para eso y una sustentación menos):

**Demo que usted debe poder repetir:** Modelar una sustentacion de 6 minutos y un Q&A

1. Presente usted mismo un CloudLite de ejemplo en 6 minutos cronometrados, con la estructura: problema, decision clave, evidencia, limite conocido.
2. Hagase una pregunta dificil en voz alta y respondala: «por que no uso microservicios? Porque el proyecto lo sostiene una sola persona y la frontera no se justificaba».
3. Muestre la rubrica proyectada y senale donde habria perdido puntos su propia demo.
4. Recuerde la regla de los 60 segundos: quien sustenta debe poder explicar cualquier parte del paquete, y si hubo equipo autorizado, cualquier integrante.


### 0–10 · Encuadre y orden de turnos
Di casi literal:
> "Hoy sustentamos. 6 minutos de pitch y hasta 4 de preguntas. Yo corto a los 6 minutos: si no
> llegaron a seguridad, costos y escala, esa parte no se califica. El orden lo sorteo ahora."

**[Nota docente]:** sortea el orden delante del grupo (evita el reclamo de «me tocó primero»),
proyecta el cronómetro y pide que el resto escuche: cerramos el curso entre todos.

### 10–110 · Sustentaciones (turnos consecutivos)
Por cada turno, en este orden:
1. **6 min de pitch.** No interrumpas ni siquiera para corregir un error: se anota y se pregunta
   después. Corta seco a los 6 min.
2. **2–4 min de Q&A.** Haz siempre una pregunta de verificación («muéstrame el .yml del
   workflow»), una de profundización («¿por qué la base de datos no está en el mismo contenedor
   que la API?») y, si queda tiempo, una hipotética («si el tráfico se multiplica por diez el
   lunes, ¿qué pieza se rompe primero?»). En equipo autorizado, dirige cada pregunta a un
   integrante distinto y **no** dejes que responda siempre el mismo.
3. **Cierra el turno con la nota puesta**, no al final del día: la rúbrica se llena en caliente
   mientras recuerdas la respuesta exacta.

**[Nota docente]:** frase de rescate cuando el estudiante se bloquea, para no perder el turno:
> "Déjame la respuesta pendiente y sigue con el siguiente bloque; vuelvo a preguntar al final."

### 110–120 · Cierre del curso
Di casi literal:
> "Lo que entregaron —diagramas, Dockerfile, workflow, informe— es un portafolio real: no lo
> borren al terminar el semestre. Arquitectura no es una lista de logos de proveedores, es un
> conjunto de decisiones documentadas con sus consecuencias."

Recuerda los pesos sin abrir discusión de notas: el PI vale **20% del Corte 3** y el Parcial 3
ya se aplicó en su propia sesión; el proyecto no reemplaza ni compensa el parcial.

### Si un estudiante no se presenta o falla la conexión
Deja constancia escrita en el momento (hora, motivo) y reprograma dentro de la misma semana con
Meet, sustentando igualmente en vivo. Aceptar un video grabado «por esta vez» convierte la
excepción en la regla del semestre siguiente y elimina el Q&A, que es la mitad de lo que evalúas.


## Actividad / taller (detalle)
1. Paso 1: armen el paquete final y llenen el indice de 8 filas con entregable, nombre de archivo, ruta dentro del paquete y estado, verificando que los 8 archivos abran desde una maquina distinta a la del autor y que ningun nombre de archivo tenga espacios ni tildes que rompan la descarga.
2. Paso 2: escriban en ExamLab la lamina unica de arquitectura en Mermaid con las 3 zonas, los 5 contenedores, el edge, la cadena de entrega y los sistemas externos, verificando al renderizar que sea legible en una sola pantalla sin desplazamiento y que use los mismos nombres canonicos del paquete, porque esta es la lamina que van a proyectar en la sustentacion.
3. Paso 3: redacten el Q and A escrito con 3 preguntas duras que el jurado podria hacer, una de decision de arquitectura, una de seguridad y una de escala o rendimiento, cada una con respuesta de maximo 4 lineas que cite la evidencia del paquete, verificando que ninguna respuesta sea no lo alcanzamos a hacer sin nombrar la decision consciente que tomaron.
4. Paso 4: ensayen el pitch con cronometro ANTES de la sesion y registren la tabla de tiempos reales por seccion con quien hablo en cada una, verificando que el tiempo total quede entre 5 y 8 minutos; la sustentacion se hace EN VIVO en la sesion de clase, con preguntas del docente al cierre, no con un video grabado.
5. Paso 5: escriban la reflexion de media pagina sobre el trade-off mas difícil y suban el paquete final completo mas las 5 preguntas a ExamLab (modulo Proyectos) ANTES de su turno de sustentacion, verificando que el informe, los diagramas, la evidencia del lab, el ci.yml y la presentacion esten los cinco dentro del mismo paquete.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Describir el diagrama en vez de justificar la decision. Reoriente con «por que asi y no de la otra forma».
- En equipos autorizados, que un integrante presente y el resto observe. Distribuya el Q&A a proposito entre todos.
- Presentar sin mencionar ningun limite del diseno. Quien no reconoce limites no entendio el trade-off.

## Preguntas de comprobación oral (no son del quiz)
Úsalas como Q&A al cerrar cada turno de sustentación, variándolas entre estudiantes.
1. Justifiquen su decision de arquitectura mas importante en 60 segundos.
1. Cual es el limite conocido de su diseno actual?
1. Si tuvieran un mes mas, que cambiarian primero y por que?

## Solución del taller (privada)
`Kit docente/Clase 15/Solucion Taller Clase 15 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 15/Quiz Clase 15 - Presentacion del proyecto y cierre.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 15/Quiz Clase 15 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase15.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (https://examlab.lovable.app/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
