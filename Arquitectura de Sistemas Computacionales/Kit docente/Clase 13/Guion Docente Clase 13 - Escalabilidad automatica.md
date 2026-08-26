# Guion docente — Clase 13: Escalabilidad automática

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma (festivo, sin encuentro síncrono)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Distinguir escala vertical vs horizontal y cuándo aplicarlas.
- Definir triggers cualitativos (CPU, cola, RPS) sin cloud de pago.
- Actualizar el informe PI con la política de escala.

## Hoy avanzamos el PI en…
**Documentar política de autoescalado conceptual de CloudLite**

**Entregable concreto:** Sección Escalabilidad: triggers, límites, qué escala y qué no

**Herramienta:** Google Docs · draw.io (opcional nota en Deployment)

## Fundamento teórico para el docente
Esta clase es autonoma por festivo: el estudiante trabaja solo y este fundamento se publica como material de lectura, asi que esta escrito para explicar el tema completo sin apoyo de un encuentro sincronico. La escalabilidad es la capacidad de un sistema de sostener mas carga agregando recursos, y la primera precision importante es que no es lo mismo que rendimiento. El rendimiento, tema de la Clase 12, pregunta cuanto tarda una peticion con la carga actual. La escalabilidad pregunta que pasa cuando la carga se multiplica: si al duplicar los recursos el sistema atiende cerca del doble de trabajo, escala bien; si atiende un 20 por ciento mas, escala mal, y ninguna cantidad de dinero lo va a arreglar. Un sistema puede ser rapido y no escalar, y puede escalar y ser lento. Por eso el orden del temario no es casual: primero se mide y se identifica el cuello de botella, y solo despues se decide como agregar capacidad.

Hay dos formas de agregar capacidad y el estudiante debe poder definirlas sin dudar. Escalar verticalmente, o hacia arriba, es darle mas recursos a la MISMA maquina: mas CPU, mas memoria, disco mas rapido. Es la opcion simple porque no exige cambiar el codigo, y tiene tres limites reales: existe un techo fisico, porque la instancia mas grande disponible se acaba en algun punto; el precio crece peor que linealmente, ya que las instancias grandes cuestan mas por unidad de capacidad; y el cambio suele requerir reiniciar el servicio, lo que implica una ventana de indisponibilidad del orden de 30 segundos a 2 minutos. Ademas una sola maquina grande sigue siendo un unico punto de falla. Escalar horizontalmente, o hacia afuera, es agregar MAS instancias iguales trabajando en paralelo, con el balanceador de carga de la Clase 7 repartiendo peticiones entre ellas. No tiene techo cercano, mejora la disponibilidad porque si una instancia muere las otras siguen atendiendo, y permite crecer en pasos pequenos y baratos. Su precio es un requisito de diseno no negociable: la aplicacion tiene que poder correr en varias copias sin pisarse.

Ese requisito se llama ausencia de estado, o statelessness, y es donde mas estudiantes fallan. Un servicio sin estado no guarda en la memoria de su propio proceso ninguna informacion que necesite en la siguiente peticion; todo lo que deba persistir vive en un almacen compartido, sea la base de datos, una cache comun o el token que trae el cliente. El sintoma en CloudLite es facil de narrar: si la API guarda la sesion en un diccionario en memoria de la instancia que atendio el login, y el balanceador manda la siguiente peticion del mismo usuario a la segunda instancia, esa instancia no lo conoce y lo expulsa; el usuario percibe que la aplicacion lo saca al azar. La solucion parcial que casi todos proponen es la sesion pegajosa, que amarra al usuario a una instancia, y hay que decir por que es un parche: si esa instancia se cae la sesion se pierde igual, y el balanceo se vuelve desigual. La solucion arquitectonica es sacar el estado del proceso: guardar la sesion en un almacen compartido o usar un token firmado que el cliente presenta en cada peticion. Lo mismo aplica a los archivos subidos de CloudLite: si se escriben en el disco local del contenedor, la mitad de las descargas fallara porque el archivo esta en la otra instancia, y por eso van a almacenamiento de objetos, que fue la decision de la Clase 7.

El autoescalado es la automatizacion del escalado horizontal y consta de cinco piezas que el entregable debe nombrar: una metrica que se observa, un umbral que dispara la accion, un periodo de evaluacion durante el cual el umbral debe sostenerse, un enfriamiento o cooldown que impide actuar de nuevo de inmediato, y un rango con minimo y maximo de instancias. Una politica completa para CloudLite se lee asi: metrica CPU promedio del grupo de instancias de la API, umbral 70 por ciento sostenido durante 5 minutos, accion agregar una instancia, cooldown de 5 minutos, minimo 2 y maximo 6. Cada numero se justifica. El 70 por ciento deja holgura para el pico que llega mientras la instancia nueva arranca. Los 5 minutos evitan reaccionar a un ruido de 20 segundos. El minimo es 2 y no 1 porque con una sola instancia no hay tolerancia a fallas ni despliegue sin caida. Y el maximo es la pieza mas olvidada y la mas importante: es el techo de costo decidido en la Clase 10, y sin el, un error de programacion o un ataque puede escalar la factura sin limite; hay casos documentados de facturas de miles de dolares generadas en horas por autoescalado sin tope. Falta una simetria que casi nadie escribe: la politica de reduccion. Si se escala hacia afuera al 70 por ciento no se puede escalar hacia adentro tambien al 70, porque el sistema oscilaria agregando y quitando instancias sin parar, fenomeno llamado flapping. La convencion es usar umbrales asimetricos, por ejemplo salir al 70 y entrar al 30, y hacer la reduccion mas lenta que la expansion, porque equivocarse agregando cuesta dinero y equivocarse quitando cuesta una caida.

Hay un limite fisico del autoescalado que desarma la idea de que es magia: la instancia nueva no aparece al instante. Un contenedor liviano tarda del orden de 10 a 60 segundos entre que se decide crearlo y que recibe trafico util, contando descarga de imagen, arranque del proceso, conexion a la base de datos y aprobacion del chequeo de salud; una maquina virtual completa puede tardar de 2 a 5 minutos. Sume el periodo de evaluacion y el sistema reacciona entre 5 y 10 minutos despues de que empezo el problema, asi que un pico subito del tipo que la prueba de spike de la Clase 12 simula ocurre y termina antes de que llegue la ayuda. Las respuestas correctas son tres y ninguna es "poner mas autoescalado": mantener holgura permanente por encima de la demanda habitual, poner una cola delante para absorber la rafaga y procesarla al ritmo que el sistema aguante, o degradar con gracia devolviendo una version reducida de la respuesta. Aqui reaparece la Clase 3: una imagen slim arranca mas rapido que una de un gigabyte, asi que adelgazar la imagen no es solo ahorro de costo, es tiempo de reaccion.

Elegir bien la metrica es la decision mas fina del tema, y el ejemplo de CloudLite es contundente. La CPU es la metrica por defecto y es la equivocada para la mayoria de las APIs, porque una API que sobre todo espera respuestas de la base de datos esta limitada por entrada y salida, no por procesador: cuando la latencia se dispara a 3 segundos porque el pool de conexiones esta agotado, la CPU puede seguir marcando un tranquilo 20 por ciento, el umbral del 70 nunca se cruza y el autoescalado no hace nada mientras los usuarios sufren. Metricas mejores para ese caso son las peticiones por segundo por instancia, que se deriva del calculo hecho en la Clase 12, la latencia p95 del propio servicio, o la longitud de la cola pendiente. Para el componente de notificaciones de CloudLite la metrica natural es el numero de mensajes esperando en la cola, no la CPU del worker: si hay 500 mensajes acumulados hay que agregar workers, y da igual cuanta CPU usen. Regla de bolsillo: la metrica correcta es la que mide el recurso que se agota primero, es decir el cuello de botella identificado en la clase anterior. De ahi que el entregable de hoy no se pueda hacer bien si el de la Clase 12 quedo vacio.

Lo que NO escala es la mitad del entregable y separa una sustentacion seria de una lista de deseos. La capa de datos es el caso central: agregar instancias de API es casi gratis conceptualmente, pero una base de datos relacional que debe mantener consistencia tiene un unico escritor, y ese escritor no se multiplica sin cambiar el modelo. Se pueden agregar replicas de lectura, y ahi entra un concepto a definir: el retraso de replicacion, esos milisegundos o segundos en que la replica todavia no tiene el ultimo cambio, que produce el sintoma de que el usuario guarda un dato, la pagina lo relee de una replica y el dato no aparece. Las alternativas mas agresivas, particionar los datos por clave o cambiar a un modelo sin esquema fijo, son decisiones de arquitectura mayores y estan fuera del alcance de CloudLite v1; decirlo explicitamente en el informe es una respuesta correcta, no una debilidad. Hay un detalle aritmetico que es la mejor leccion del dia: si cada instancia de la API abre un pool de 20 conexiones y el autoescalado sube a 6 instancias, el sistema pide 120 conexiones, mientras que una base de datos gestionada pequena suele admitir del orden de 100; el resultado es que escalar la API tumba la base de datos. Multiplicar la capa sin verificar el limite del recurso compartido no mejora el sistema, lo rompe. Tambien conviene enumerar otras piezas que no escalan por replicacion: los limites de terceros, como un proveedor de correo que acepta 100 envios por minuto y rechaza el exceso, de modo que diez workers no envian diez veces mas rapido sino que generan diez veces mas errores; los sistemas de archivos compartidos; y las tareas programadas de tipo singleton, que si corren en seis instancias hacen el mismo trabajo seis veces y pueden duplicar cobros o correos.

Tres preguntas aparecen sin falta en una clase autonoma como esta y conviene responderlas por escrito en el foro. La primera es por que documentar limites si el autoescalado es automatico; la respuesta es que automatico significa que ejecuta la politica que alguien escribio, no que decide bien: sin maximo escala el costo, sin minimo pierde disponibilidad, con la metrica equivocada no reacciona y con umbrales simetricos oscila; el automatismo amplifica la calidad de la decision humana en ambos sentidos. La segunda es si no seria mejor serverless, que "escala infinito"; la respuesta reconoce la ventaja real, que escala por peticion y no cobra en reposo, y nombra los tres costos: el arranque en frio, esa demora extra de cientos de milisegundos a segundos cuando una funcion se invoca despues de estar inactiva; el agotamiento de conexiones, porque mil funciones concurrentes matan a la base de datos igual que mil contenedores; y el costo por invocacion, que a volumen alto puede superar el de instancias fijas. La tercera es cuantas instancias poner, y la respuesta sale de la aritmetica de la Clase 12 y no del gusto: si el pico estimado es de 5 RPS y una instancia sostiene con holgura unos 3 RPS dentro del objetivo de p95, se necesitan 2 con una de margen, y el maximo se fija donde el costo mensual deja de ser defendible o donde choca con el limite de conexiones, el que llegue primero. Para verificar el diseno sin gastar un peso alcanza LabEx Docker Playground con docker compose para levantar dos o tres replicas del stub detras de un balanceador y comprobar que la sesion no se rompe; el entregable formal es una nota sobre el diagrama de despliegue y la seccion escrita con estrategia, trigger, limite y lo que no escala, que la Clase 14 evaluara y la Clase 15 exigira sustentar.

Error tipico del docente que no domina el tema: presentar el autoescalado como solucion general a los problemas de rendimiento. Si no se identifico primero el cuello de botella, escalar la pieza equivocada no mejora nada y sube el costo; el caso mas ilustrativo es la API limitada por la base de datos, donde agregar instancias empeora la situacion porque suma presion sobre el recurso ya saturado. La consecuencia pedagogica es que el estudiante sale creyendo que la escalabilidad se compra con configuracion, y en el Parcial 3 responde con la definicion de vertical y horizontal sin poder decidir cual aplica a un caso. El segundo error es celebrar el escalado horizontal como si fuera gratis: presentarlo solo como "agregar instancias" sin exigir la revision del estado en memoria, ni el limite de conexiones, ni la capa de datos. Si eso se deja pasar, el entregable llega con la seccion de "que no escala" vacia o rellenada con una frase generica, y en la Clase 15 el estudiante afirma que su sistema soporta cualquier crecimiento mientras el diagrama muestra una unica base de datos con la sesion guardada en memoria, que es la contradiccion mas facil de detectar y la mas costosa de explicar en ese momento.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 13 - Escalabilidad automatica/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 13 · Escalabilidad automática
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. Escala para CloudLite
6. Límites y costos
7. Politica de autoescalado (tabla, no prosa)
8. Herramientas de hoy
9. Del boceto a ExamLab (diagrama)
10. Taller PI (paso a paso)
11. Para continuar (PI)
12. Clase 13 · PI en movimiento

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
4. Mensaje sugerido: «Clase 13 autónoma (festivo). Hoy avanzamos el PI en: Documentar política de autoescalado conceptual de CloudLite.
   Entregable: Sección Escalabilidad: triggers, límites, qué escala y qué no. Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a ExamLab.

### La demo, en versión asíncrona
**Demo que usted debe poder repetir:** Vertical vs horizontal, y lo que NO escala

1. Dibuje una caja «API» y agrandela: eso es vertical (mas CPU/RAM a la misma maquina, con techo fisico).
2. Borre y dibuje 3 cajas «API» iguales con un balanceador arriba: eso es horizontal.
3. Agregue la base de datos abajo, conectada a las 3, y encierrela en rojo: «esta no se multiplica igual; aqui esta el limite real».
4. Escriba el trigger y el limite: «CPU > 70% por 5 min -> +1 instancia, maximo 4» y amarre con el costo de la Clase 10.

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
1. Paso 1: tome los 5 componentes de su C4Deployment de la Clase 7 y clasifique cada uno como escala horizontal, escala vertical o no escala, verificando que al menos uno quede en no escala con justificacion tecnica, porque una politica donde todo escala no es una politica; el resultado abre la seccion Escalabilidad del informe.
2. Paso 2: complete la tabla de politica de escalado con 6 columnas y 5 filas (componente, tipo de escala, disparador de subida, disparador de bajada, minimo y maximo, tiempo de enfriamiento), verificando que cada disparador tenga metrica, umbral numerico y ventana de tiempo, y que ningun maximo quede en infinito o sin definir.
3. Paso 3: escriba en ExamLab el diagrama Mermaid de la maquina de decision del autoescalado con el nodo de observacion, los dos rombos de decision, las acciones de subida y bajada, el enfriamiento y el nodo de lo que no escala, verificando al renderizar que el ciclo se cierre sobre el nodo de observacion y que los umbrales del diagrama sean los mismos numeros de la tabla.
4. Paso 4: escriba los 3 componentes que NO escalan con su justificacion tecnica y su plan alterno, y la tabla de impacto en costos que enlaza con la Clase 10, verificando que cada plan alterno sea ejecutable sin cloud de pago y que el impacto de costo use los mismos niveles bajo, medio o alto de la seccion de costos.
5. Paso 5: integre la politica en la seccion Escalabilidad del informe, anote la marca de replicas en el diagrama de despliegue si aplica y suba las 5 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que la politica no prometa nada que la arquitectura dibujada no pueda cumplir.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Prometer autoescalado infinito sin limite maximo ni control de costo (Clase 10).
- Escalar horizontalmente un servicio que guarda la sesion en memoria local: al repartir la carga, el usuario pierde su sesion.
- No documentar QUE NO escala. La base de datos relacional es casi siempre la respuesta y hay que decirlo.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Vertical u horizontal: cual eligieron y por que?
1. Cual es su trigger y cual su limite maximo?
1. Que pieza de su sistema NO escala, y que harian al respecto?

## Solución del taller (privada)
`Kit docente/Clase 13/Solucion Taller Clase 13 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 13/Quiz Clase 13 - Escalabilidad automatica.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 13/Quiz Clase 13 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase13.png | receta: 1) Abre Google Docs · draw.io (opcional nota en Deployment) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 13/Capturas/demo-clase13.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase13.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 13/Capturas/evidencia-clase13.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
