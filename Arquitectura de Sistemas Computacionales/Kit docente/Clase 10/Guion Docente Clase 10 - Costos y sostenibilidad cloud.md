# Guion docente — Clase 10: Costos y sostenibilidad cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Actividad autónoma (festivo, sin encuentro síncrono)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Identificar drivers de costo (cómputo, datos, transferencia, idle).
- Proponer 3 apalancamientos de ahorro sin romper el diseño.
- Redactar sostenibilidad (apagado de labs, imágenes ligeras, sobredimensionamiento).

## Hoy avanzamos el PI en…
**Estimación cualitativa de costos + notas de sostenibilidad**

**Entregable concreto:** Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)

**Herramienta:** Google Docs

## Fundamento teórico para el docente
Esta clase es autonoma por festivo: no hay encuentro sincronico y este fundamento se publica tal cual como material de lectura, asi que debe sostener por si solo la comprension del tema. Conviene empezar por la economia, porque sin ella el tema suena a contabilidad. En un centro de datos propio el gasto es de capital: se compra un servidor, se paga por adelantado, se amortiza en tres o cinco anos, y desde ese momento dejarlo encendido una hora mas no aparece en ninguna factura visible. En la nube el gasto es operativo y medido: se paga por segundo de computo, por gigabyte almacenado al mes, por gigabyte que sale hacia internet y por peticion atendida. El cambio no es contable sino arquitectonico. Cuando cada recurso tiene precio unitario, casi cualquier decision de diseno se convierte en una cifra mensual y el arquitecto pasa a ser corresponsable del gasto. Esa es la razon por la que este tema vive en un curso de arquitectura y no en uno de administracion.

CloudLite App no tiene facturacion real y no la va a tener: el curso prohibe cuentas cloud de pago y tarjetas de credito, y todo se trabaja con draw.io, Excalidraw, LabEx Docker Playground y el free tier de GitHub Actions. Eso no impide el analisis de costo, solo cambia la escala de medida. En vez de pesos se usa una escala ordinal de tres niveles, Bajo, Medio y Alto, asignada componente por componente. Una escala ordinal ordena pero no mide distancias: decir que la base de datos es Alto y el frontend estatico es Bajo afirma que uno cuesta mas que el otro, no cuantas veces mas. Alcanza de sobra para el objetivo real, que es identificar el driver de costo de cada componente. Un driver de costo es la variable concreta que, si crece, hace crecer la factura de ese componente; no es "el uso" en abstracto sino algo contable: instancias encendidas, horas encendidas, gigabytes almacenados, gigabytes de trafico de salida, numero de peticiones, gigabytes de logs ingeridos. Un componente al que el estudiante no le sabe poner driver es un componente que todavia no entiende.

El docente debe poder citar ordenes de magnitud, y conviene decir en voz alta que son convenciones aproximadas de precios de lista y no reglas duras: las cifras cambian por proveedor, region y ano, pero las proporciones se mantienen estables. Una instancia pequena de 2 vCPU y 4 GB encendida todo el mes cuesta del orden de 25 a 40 dolares. El almacenamiento de objetos cuesta del orden de 0.02 a 0.03 dolares por gigabyte al mes, es decir casi nada. El trafico de salida hacia internet, llamado egress, cuesta del orden de 0.08 a 0.12 dolares por gigabyte: unas cuatro veces mas caro por gigabyte que guardarlo un mes entero. Una base de datos gestionada cuesta entre dos y tres veces la maquina desnuda equivalente, porque incluye respaldos, parches y conmutacion por falla. Un balanceador de carga cobra una tarifa fija de 18 a 25 dolares al mes incluso con cero trafico. Una funcion serverless suele traer free tier de alrededor de un millon de invocaciones mensuales, asi que un componente poco usado cuesta cero de verdad. La leccion durable son tres proporciones: guardar es barato, mover datos hacia afuera es caro, y estar prendido sin hacer nada tambien cuesta.

El primer ejemplo anclado en CloudLite es la tabla del entregable, y el docente deberia recorrerla componente por componente. El contenedor de la API queda en Medio, con driver instancias por horas encendidas. La base de datos queda en Alto con un argumento preciso: paga computo las 24 horas de los 30 dias aunque nadie consulte, mas almacenamiento que nunca baja, mas respaldos. El frontend estatico queda en Bajo porque es almacenamiento mas trafico y no tiene computo propio. Las notificaciones quedan en Bajo si se modelan como funcion serverless de volumen pequeno, y pasan a Medio si se implementan como un worker encendido de forma permanente: el mismo requisito con dos disenos y dos costos, que es exactamente el razonamiento que se evalua. Y hay un componente que sorprende, el monitoreo de la Clase 8: un sistema que registra cada peticion con detalle puede generar mas gigabytes de logs que de datos de negocio, y la ingesta de logs se cobra por gigabyte; existen casos reales de equipos cuya observabilidad costaba mas que la aplicacion observada.

El segundo ejemplo muestra por que el driver importa mas que el nivel. Suponga que CloudLite permite subir comprobantes en PDF o imagenes y que en un semestre acumula 5000 archivos de 2 MB, o sea 10 GB. Guardarlos cuesta unos 0.25 dolares al mes, despreciable. Pero si cada archivo se descarga en promedio 20 veces, el sistema mueve 200 GB de egress al mes, que a 0.09 dolares por gigabyte son unos 18 dolares: setenta veces mas que el almacenamiento. La conclusion es contraintuitiva y por eso vale en clase: el driver del componente "almacenamiento de archivos" no es el almacenamiento, es el trafico, y la mitigacion no es contable sino arquitectonica, poner una cache o una red de distribucion de contenido delante para que el mismo archivo no salga del origen veinte veces. Esto tambien desarma la intuicion mas comun del estudiante, que si nadie usa el sistema el sistema no cuesta. Hay dos familias de recursos: los que cobran por uso y los que cobran por existir. La base de datos gestionada, el balanceador, las IP reservadas, los volumenes huerfanos y las instantaneas viejas son de la segunda y facturan aunque el ultimo usuario se haya ido hace meses.

De ahi sale el segundo bloque del entregable: tres acciones de right-sizing. Right-sizing es ajustar la capacidad aprovisionada a la demanda observada, y la palabra clave es observada: sin medicion es adivinanza, y la medicion viene de las senales doradas de la Clase 8, en particular la saturacion. La metrica que lo gobierna es la utilizacion, el porcentaje de la capacidad pagada que efectivamente se usa; una maquina al 5 por ciento de CPU durante un mes desperdicia el 95 por ciento de lo pagado. La convencion de industria, que es convencion y no regla, apunta a una utilizacion sostenida entre el 40 y el 70 por ciento: por debajo hay sobreaprovisionamiento y por encima no queda holgura para picos. La primera accion tipica es reducir tamano o numero de replicas hasta acercarse a ese rango. La segunda es apagar por horario lo que no es produccion: un ambiente encendido las 24 horas los siete dias consume 168 horas semanales, y encendido solo de 8 a 6 en dias habiles consume 50, un ahorro cercano al 70 por ciento sin tocar codigo. La tercera es adelgazar el artefacto, que amarra con la Clase 3: una imagen basada en python:3.12 pesa del orden de 1 GB, la variante slim unos 150 MB y una construida sobre alpine puede bajar a decenas de megabytes; eso es menos registro, menos transferencia en cada despliegue y menos tiempo de arranque, dato que reaparece en la Clase 13. Igual de validos son fijar retencion de logs a 30 dias en vez de para siempre y borrar volumenes e instantaneas sin dueno.

La sostenibilidad en este curso es tecnica antes que ambiental, y conviene decirlo asi para no caer en discurso vacio. La energia que consume un servidor depende sobre todo de la capacidad encendida, no de la usada: una maquina al 5 por ciento no consume el 5 por ciento de la energia, consume mucho mas, porque el consumo en reposo de un servidor moderno ronda la mitad del consumo a plena carga. Por eso las mismas tres acciones sirven a la vez para la factura y para la huella. Hay ademas una decision de arquitectura con efecto directo: la intensidad de carbono de la electricidad varia fuerte entre regiones, asi que elegir region no es solo latencia y cumplimiento normativo. Y hay una tercera cara que el estudiante ignora: el costo humano de mantener el diseno. Una arquitectura de ocho servicios que un equipo de tres personas no puede operar es insostenible aunque la infraestructura sea gratis.

Tres preguntas aparecen siempre. La primera es si tiene sentido estimar costos cuando nadie va a pagar nada; la respuesta es que la estimacion no cambia la factura, cambia el diseno, y que en un trabajo real la segunda pregunta despues de "funciona" es "cuanto cuesta al mes". Ademas el costo es un atributo de calidad como la latencia, de los enumerados en la Clase 1, y compite con los demas: el objetivo de p95 que se definira en la Clase 12 casi siempre se compra con dinero. La segunda es si entonces lo mas barato es siempre lo mejor, y la respuesta es no, porque lo mas barato suele mover el costo hacia la operacion humana; el concepto a nombrar es costo total de propiedad, que suma infraestructura mas operacion mas incidentes mas migraciones, y bajo esa lente una base de datos autoadministrada en una maquina desnuda es mas barata al mes y mas cara al ano cuando alguien debe parcharla, respaldarla y atender su caida a las tres de la manana. La tercera es como asignar los niveles sin factura: se asignan comparando componentes entre si con el driver como argumento y escribiendo el supuesto; "Alto porque es computo 24/7 mas almacenamiento acumulativo mas respaldos" es defendible, "Alto porque suena caro" no. Conviene advertir que en la Clase 11 la auditoria exigira que los componentes de esta tabla se llamen igual que los contenedores del C4 de la Clase 4 y las piezas del despliegue de la Clase 7, y que en la Clase 13 el limite maximo del autoescalado sera el techo de costo que se decide hoy.

Error tipico del docente que no domina el tema: tratar el costo como asunto "de negocio, no tecnico" y despacharlo en cinco minutos. Las decisiones que mas mueven la factura son decisiones de arquitectura, tomadas por quien dibuja el diagrama: gestionado o autoadministrado, con cache o sin cache, sincronico o con cola, replicas fijas o autoescalado. Si esta clase se salta, la consecuencia aparece dos clases despues: en la Clase 13 los estudiantes escriben politicas de autoescalado sin limite superior, en la Clase 15 defienden arquitecturas que nadie podria pagar y en el Parcial 3 responden la pregunta de drivers con generalidades sobre "optimizar recursos". El segundo error es el opuesto e igual de danino: exigir cifras exactas en dolares. Con eso la clase se vuelve una caceria de calculadoras de precios, el estudiante copia numeros que no entiende y las acciones de right-sizing quedan cosmeticas. El criterio de aprobacion no es la precision del numero sino que cada componente tenga driver nombrado y que cada accion sea verificable: "reducir a una replica el worker de notificaciones y usar imagen slim" se puede revisar, "optimizar el codigo" no.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 10 - Costos y sostenibilidad cloud/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 10 · Costos y sostenibilidad cloud
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. Costos sin factura real
6. Sostenibilidad
7. Herramientas de hoy
8. Del boceto a ExamLab (diagrama)
9. Taller PI (paso a paso)
10. Para continuar (PI)
11. Clase 10 · PI en movimiento

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
4. Mensaje sugerido: «Clase 10 autónoma (festivo). Hoy avanzamos el PI en: Estimación cualitativa de costos + notas de sostenibilidad.
   Entregable: Sección Costos/Sostenibilidad del informe (bajo/medio + drivers). Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a ExamLab.

### La demo, en versión asíncrona
**Demo que usted debe poder repetir:** Tabla de costo cualitativo en 5 minutos

1. Dibuje 3 columnas: Componente | Costo (Bajo/Medio/Alto) | Driver del costo.
2. Llene 3 filas de CloudLite: base de datos gestionada (Alto, computo+almacenamiento constante 24/7), API en contenedor (Medio, numero de instancias), object storage de imagenes (Bajo, volumen de datos).
3. Pregunte cual bajaria primero si el presupuesto se corta a la mitad, y exija que justifiquen con el driver, no con intuicion.

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
1. Paso 1: liste los 6 elementos de costo de su diseno tomandolos del C4Deployment de la Clase 7 (edge, API, worker, base de datos, almacen de objetos y minutos de integracion continua), verificando que no aparezca ningun componente que no exista en su diagrama y que ninguno quede sin fila, porque al ser clase autonoma nadie va a completar la tabla por usted.
2. Paso 2: complete la tabla de 5 columnas asignando a cada elemento su driver de costo, el nivel bajo, medio o alto, un apalancamiento y el riesgo de aplicarlo, verificando que ningun driver se repita entre filas y que la palabra caro no aparezca sola como explicacion.
3. Paso 3: escriba en ExamLab el mindmap Mermaid con las 5 ramas de drivers (computo, datos, transferencia, ocioso e integracion continua) y 2 hojas concretas por rama, verificando al renderizar que las 10 hojas mencionen elementos reales de su despliegue y no categorias abstractas.
4. Paso 4: desarrolle 3 apalancamientos de ahorro con su estado antes y despues y 3 acciones de sostenibilidad verificables, verificando que cada accion tenga una evidencia que un tercero pueda revisar (tamano de la imagen en megabytes, hora de apagado del lab, numero de replicas en la noche) y que ninguna rompa un requisito del PI.
5. Paso 5: integre la tabla, el mindmap y las acciones en la seccion Costos y sostenibilidad del informe (1 pagina) y suba las 5 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, verificando que no haya inventado ninguna factura en dolares de un proveedor de pago.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Pedir precios exactos de un proveedor. No es el objetivo: el analisis es cualitativo y por driver.
- Marcar todo como costo «Medio» para no pensar. Fuerce al menos un Alto y un Bajo con justificacion.
- Olvidar el trafico de red saliente, que es el driver que mas sorprende en facturas reales.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Cual es el componente mas caro de su CloudLite y cual es su driver?
1. Que es right-sizing en una frase?
1. Como se conecta el autoescalado con el costo?

## Solución del taller (privada)
`Kit docente/Clase 10/Solucion Taller Clase 10 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 10/Quiz Clase 10 - Costos y sostenibilidad cloud.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 10/Quiz Clase 10 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase10.png | receta: 1) Abre Google Docs y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 10/Capturas/demo-clase10.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase10.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 10/Capturas/evidencia-clase10.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
