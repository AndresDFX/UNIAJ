# Guion docente — Clase 8: Monitoreo y optimización · CI/CD

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Explicar pipeline CI vs CD y qué es realista sin cloud de pago.
- Crear un workflow Actions que construya/pruebe un stub.
- Definir 4–6 señales de monitoreo para CloudLite.

## Hoy avanzamos el PI en…
**Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**

**Entregable concreto:** .github/workflows/ci.yml + sección Monitoreo/CI del informe

**Herramienta:** GitHub Actions · Google Docs

## Fundamento teórico para el docente
### Integracion continua: el problema que resuelve, en definicion operativa - diapositiva 4
Esta clase junta dos temas que parecen distintos y son el mismo asunto en dos momentos: automatizar la verificacion antes de que un cambio llegue a los usuarios, y observar el sistema despues de que llego. El problema que resuelve la integracion continua tiene nombre historico, infierno de integracion: varios desarrolladores trabajan semanas por separado y al juntar el codigo aparecen conflictos y fallas que nadie sabe de donde vienen. Su version cotidiana en un equipo de estudiantes es la frase «en mi maquina funciona». Integracion continua, definida operativamente, es esto: cada vez que alguien sube un cambio al repositorio, un servidor automatico toma el codigo en un entorno limpio, lo construye, le corre las pruebas y avisa en minutos si algo se rompio. El valor no esta en la automatizacion sino en el intervalo de retroalimentacion: encontrar el error tres minutos despues de escribirlo, cuando el autor recuerda que hizo, cuesta una fraccion de hallarlo tres semanas despues en el computador de otra persona.
### Entrega continua y despliegue continuo: la sigla CD es ambigua - diapositiva 5
La sigla CD es ambigua y ahi esta la confusion que hay que desarmar en el primer minuto. Entrega continua significa que cada cambio que pasa la validacion queda listo para desplegarse, empaquetado y probado, pero un humano decide cuando se aprieta el boton. Despliegue continuo significa que ese ultimo paso tambien es automatico y el cambio llega a produccion sin intervencion. Las dos comparten la sigla CD, no son lo mismo, y ninguna es sinonimo de integracion continua: CI valida, CD entrega o despliega. Se puede tener CI sin nada de CD, y es lo que se construye hoy porque el curso no usa infraestructura de pago ni pide tarjeta de credito. El pipeline llega hasta «listo para desplegar» y la etapa final imprime un mensaje y publica un artefacto en lugar de subir a un servidor real. Hay que decirlo explicito: lo simulado es el ultimo paso, no el pipeline; todo lo anterior es real y ejecutable.
### GitHub Actions en cinco palabras - diapositiva 6
GitHub Actions es la herramienta del dia porque es gratis, corre en el navegador y produce evidencia verificable. Su vocabulario tiene cinco palabras. Un workflow es un archivo YAML en la carpeta .github/workflows; el nombre es libre y ci.yml es la convencion. El evento o disparador declara cuando corre: on push para cada subida, on pull_request para cada propuesta de cambio, workflow_dispatch para un boton manual, schedule para una hora fija. Un job es un conjunto de pasos que corre en un runner, una maquina virtual limpia que se crea para esa ejecucion y se destruye al terminar. Un step es un comando o el uso de una action, unidad reutilizable publicada por otros. Que el runner sea limpio y efimero es el punto pedagogico central: demuestra que la construccion no depende de nada instalado a mano en el portatil de nadie. Advertencias: el YAML se indenta con espacios y nunca con tabulaciones, causa numero uno de un pipeline que no arranca; y en el nivel gratuito los repositorios publicos tienen minutos ilimitados mientras los privados tienen una cuota del orden de 2000 minutos al mes, cifra que conviene confirmar en la pagina de facturacion porque el proveedor la cambia.
### Primer ejemplo: el pipeline del stub de CloudLite - diapositiva 8
Primer ejemplo concreto: el pipeline del stub de CloudLite, que ya existe desde la Clase 3 como Dockerfile y contenedor. El workflow se dispara en push a la rama principal y en pull_request. Un job llamado validar hace cinco pasos: descargar el codigo, instalar el runtime del lenguaje, instalar dependencias, correr las pruebas y construir la imagen con docker build para comprobar que el Dockerfile sigue siendo valido. Un sexto paso simula el despliegue: imprime la etiqueta de version y publica un artefacto, un archivo que queda guardado junto a la corrida. Aparece la primera pregunta previsible: «para que escribir pruebas de un stub que casi no hace nada?». Incluso una sola prueba que verifique que el endpoint /health responde 200 detecta la clase de error mas costosa en operacion: que la aplicacion ya no arranca. La evidencia es doble: el archivo ci.yml en el repositorio y la captura de una corrida en verde; si Actions falla por cuota o red se acepta el YAML con la explicacion paso por paso, pero eso es plan B.
### Donde se ejecuta de verdad la politica de secretos de la Clase 6 - diapositiva 8
El pipeline es tambien donde se ejecuta de verdad la politica de secretos escrita en la Clase 6. Los valores sensibles se guardan en el repositorio bajo Settings, Secrets and variables, Actions; el workflow los referencia por nombre y la plataforma los inyecta como variables de entorno solo durante la corrida. Dos detalles evitan sustos. La plataforma enmascara los secretos en el registro de salida, pero enmascarar no es impedir la fuga: si un paso imprime el valor transformado, por ejemplo codificado, sale en claro; la regla es no imprimir secretos nunca. Y por diseno los secretos no se entregan a las corridas disparadas por un pull_request que viene de un fork, para que un extrano no pueda proponer un cambio que los imprima. La consecuencia practica es que la validacion de un cambio externo no puede depender de credenciales, y por eso las pruebas del stub deben correr sin acceso a servicios reales, con valores ficticios o un doble simulado.
### Monitorear y observar: la segunda mitad cambia de lado - diapositiva 7
La segunda mitad de la clase cambia de lado: ya no se trata de validar antes, sino de saber que pasa despues. Monitorear es vigilar indicadores decididos de antemano; observabilidad es la capacidad de responder preguntas nuevas sobre el sistema a partir de lo que el sistema emite, sin agregar codigo por cada duda. Se apoya en tres tipos de senal. Las metricas son numeros medidos en el tiempo, baratas porque se agregan, y detectan que algo cambio. Los logs son eventos discretos con contexto, caros en volumen, y explican por que cambio. Las trazas siguen el recorrido de una sola peticion por varios servicios y son necesarias porque la Clase 4 convirtio el sistema en distribuido: cuando la peticion pasa por la API y por el servicio de notificaciones, saber cual de los dos tardo es imposible con metricas agregadas. La practica minima documentable es el log estructurado: cada linea es un objeto con campos fijos como fecha, nivel, identificador de peticion, ruta, codigo de estado y duracion en milisegundos. Con ese identificador propagado entre servicios se reconstruye el recorrido: una traza pobre, pero real.
### Las cuatro senales de oro, con definicion operativa - diapositiva 7
Las cuatro senales de oro son latencia, trafico, errores y saturacion, y cada una necesita definicion operativa. Trafico es cuanta demanda llega, en peticiones por segundo o por minuto. Errores es la proporcion de peticiones que fallan, tipicamente el porcentaje de respuestas 5xx; conviene expresarlo como disponibilidad, y aqui hay aritmetica que el docente debe citar: 99,9 por ciento equivale a unos 43 minutos de indisponibilidad al mes y 99,99 por ciento a unos 4 minutos, lo cual no es convencion sino calculo sobre los 43.200 minutos de un mes de treinta dias. Saturacion es que tan cerca esta el recurso mas escaso de su limite: CPU, memoria, disco o, en la mayoria de las APIs reales, las conexiones libres del pool de la base de datos; la convencion es alertar cuando un recurso pasa del 70 u 80 por ciento sostenido, y es convencion, no ley. Latencia merece explicacion aparte porque introduce el percentil, el valor por debajo del cual cae un porcentaje dado de las mediciones: si el p95 de la API es 300 milisegundos, 95 de cada 100 peticiones respondieron en 300 milisegundos o menos y 5 tardaron mas. Es mas honesto que el promedio, y el ejemplo lo prueba: 99 peticiones de 50 milisegundos y una de 5 segundos dan un promedio de 99 milisegundos, que parece excelente, mientras el p99 es 5 segundos y corresponde a un usuario mirando una pantalla congelada.
### Segundo ejemplo: la tabla de senales de CloudLite con umbral y accion - diapositiva 7
Segundo ejemplo concreto: la tabla de cuatro a seis senales de CloudLite, con umbral y accion. Latencia p95 del inicio de sesion y del listado principal, con objetivo bajo 300 milisegundos; peticiones por minuto; porcentaje de respuestas 5xx, con alerta sobre el 1 por ciento sostenido; uso del pool de conexiones, con alerta sobre el 80 por ciento; crecimiento del almacenamiento de objetos donde viven los adjuntos de la Clase 7; y, si se modelaron notificaciones, los mensajes pendientes en la cola. La columna que convierte una lista de metricas en un plan de operacion es la ultima: que se hace cuando se cruza el umbral. Ahi entra la optimizacion: paginar, con veinte a cincuenta elementos por pagina, porque un endpoint que devuelve cincuenta mil registros es problema de latencia y de memoria; indexar la columna por la que se filtra, porque sin indice el motor recorre la tabla completa; cachear lecturas repetidas, donde una tasa de acierto del 90 por ciento significa que nueve de cada diez lecturas no llegan a la base; y limitar la tasa de peticiones, el control de denegacion de servicio de la Clase 6. Aparece la segunda pregunta previsible: «si no tenemos usuarios reales, que monitoreamos?». El entregable es el plan, no los datos, y el chequeo de salud que consulta el balanceador de la Clase 7 ya es monitoreo real. Con esto cierra el bloque del Parcial 2 de la Clase 9: los umbrales de hoy se prueban con carga en la Clase 12, la saturacion sera el disparador del autoescalado de la Clase 13 y el consumo medido es el que se costea en la Clase 10.
### Cierre conceptual y error tipico del docente (de la diapositiva 5 a la diapositiva 7)
Error tipico del docente que no domina el tema: presentar CI y CD como sinonimos intercambiables y hablar de «hacer CI/CD» sin separar que valida, que entrega y que despliega. La consecuencia aguas abajo es que el estudiante cree que su workflow puso la aplicacion en produccion, describe en el informe un despliegue que no existe y en la sustentacion de la Clase 15 defiende una capacidad operativa que no puede demostrar. El segundo tropiezo es dejar la tabla de monitoreo como una lista de palabras sueltas (latencia, errores, CPU) sin umbral, sin unidad y sin accion asociada; cuando eso pasa, la seccion de monitoreo no dice nada, la Clase 12 no tiene contra que comparar los resultados de la prueba de carga y la politica de autoescalado de la Clase 13 se inventa un disparador sin ninguna medida que lo sustente.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 8 · Monitoreo y optimización · CI/CD
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. CI/CD sin tarjeta
6. YAML mínimo
7. Monitoreo y optimización
8. .github/workflows/ci.yml — CI real, no un echo
9. Herramientas de hoy
10. Taller PI (paso a paso)
11. Para continuar (PI)
12. Clase 8 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 4]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**.
Entregable concreto: .github/workflows/ci.yml + sección Monitoreo/CI del informe.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **CI/CD sin tarjeta** · [Slide 5]
- **YAML mínimo** · [Slide 6]
- **Monitoreo y optimización** · [Slide 7]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 8]
Herramienta del día: **GitHub Actions · Google Docs**.
**Demo que usted debe poder repetir:** Un workflow de GitHub Actions que corra de verdad

1. Cree `.github/workflows/ci.yml` con on: push, un job y 3 steps: checkout, setup, y un comando de prueba real.
2. Haga commit y push, y abra la pestana Actions del repositorio para ver el run.
3. Espere el check verde y senale el log del step: «esto es evidencia, no una diapositiva que dice que tenemos CI».
4. Aclare la frontera: el pipeline llega hasta «listo para desplegar»; no despliega a ningun servidor real en este curso.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 8/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Run verde del workflow: build + test reales, no un `echo ok` [[captura: salida-actions-run.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 10]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 12]
Di: «Queda avanzado: Workflow Actions (build/test/simulate) + métricas de monitoreo del PI.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: escriba en la pregunta 7 el contenido completo del ci.yml con disparadores, entorno y los pasos de construccion, prueba y despliegue simulado, usando la imagen y el puerto del Dockerfile del Corte 1; verifique que ningun secreto quede escrito en claro dentro del YAML.
2. Paso 2: explique en la pregunta 8 que se compila o instala, que se ejecuta en la prueba y con que condicion el pipeline debe fallar; hagase la prueba mental de que error tendria que introducir para que el check salga rojo, y si no encuentra ninguno, su pipeline todavia no valida nada.
3. Paso 3: distinga en la pregunta 9 que valida CI y que hace CD, ubique cual de los dos construyo y diga que le faltaria para CD real; reconocer que su pipeline llega hasta «listo para desplegar» suma puntos, afirmar que ya tiene CD los resta.
4. Paso 4: liste en la pregunta 10 entre 4 y 6 senales con su umbral, atadas a operaciones de su dominio, y verifique que al menos una sea un registro y no una metrica numerica; una senal sin umbral no sirve para operar y no suma.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Un workflow que solo hace `echo ok`: es un pipeline decorativo. Exija que corra algo que pueda fallar de verdad.
- Decir que ya tienen CD porque el YAML dice deploy. En este curso el despliegue se simula; que lo digan asi.
- Golden signals sin umbral: «medimos latencia» no sirve; falta a partir de que valor se considera un problema.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que valida CI y que hace CD, y cual de los dos construyeron hoy?
1. Digan las 4 golden signals y el umbral de una de ellas.
1. Que pasaria en su pipeline si alguien sube codigo que no compila?

## Solución del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 8/Quiz Clase 8 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase08.png | receta: 1) Abre GitHub Actions · Google Docs y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 8/Capturas/demo-clase08.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase08.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 8/Capturas/evidencia-clase08.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
