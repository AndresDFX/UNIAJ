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

**Herramienta:** Navegador · editor de código del curso (YAML)

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Integracion continua: el problema que resuelve, en definicion operativa** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El problema que resuelve la integracion continua tiene nombre historico, infierno de integracion: varios desarrolladores trabajan semanas por separado y al juntar el codigo aparecen conflictos y fallas que nadie sabe de donde vienen.
  - Su version cotidiana en un equipo de estudiantes es la frase «en mi maquina funciona».
  - Integracion continua, definida operativamente, es esto: cada vez que alguien sube un cambio al repositorio, un servidor automatico toma el codigo en un entorno limpio, lo construye, le corre las pruebas y avisa en minutos si algo se rompio.
  - El valor no esta en la automatizacion sino en el intervalo de retroalimentacion: encontrar el error tres minutos despues de escribirlo, cuando el autor recuerda que hizo, cuesta una fraccion de hallarlo tres semanas despues en el computador de otra persona.
  - (No se proyecta) Esta clase junta dos temas que parecen distintos y son el mismo asunto en dos momentos: automatizar la verificacion antes de que un cambio llegue a los usuarios, y observar el sistema despues de que llego.
  - (No se proyecta) Lo que se califica hoy son 25 de los 100 puntos de la actividad del Corte 2, en cuatro preguntas: 10 puntos el contenido completo del ci.yml, 5 explicar que hace de verdad la construccion y la prueba y con que condicion el pipeline debe fallar, 4 distinguir CI de CD y ubicar hasta donde llego el propio trabajo, y 6 la tabla de senales de monitoreo con umbral.
  - (No se proyecta) Conviene decir el reparto al abrir la clase, porque las dos preguntas que el grupo subestima, la 8 y la 10, valen juntas mas que el YAML.

**[Slide 5] Entrega continua y despliegue continuo: la sigla CD es ambigua** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La sigla CD es ambigua y ahi esta la confusion que hay que desarmar en el primer minuto.
  - Despliegue continuo significa que ese ultimo paso tambien es automatico y el cambio llega a produccion sin intervencion.
  - Las dos comparten la sigla CD, no son lo mismo, y ninguna es sinonimo de integracion continua: CI valida, CD entrega o despliega.
  - Se puede tener CI sin nada de CD, y es lo que se construye hoy porque el curso no usa infraestructura de pago ni pide tarjeta de credito.
  - La forma tipica del error es tener un paso llamado deploy que solo imprime un mensaje y concluir que ya hay despliegue continuo; el nombre del paso no despliega nada.
  - NOTAS:
  - Entrega continua significa que cada cambio que pasa la validacion queda listo para desplegarse, empaquetado y probado, pero un humano decide cuando se aprieta el boton.
  - El pipeline llega hasta «listo para desplegar» y la etapa final imprime un mensaje y publica un artefacto en lugar de subir a un servidor real.
  - (No se proyecta) Hay que decirlo explicito: lo simulado es el ultimo paso, no el pipeline; todo lo anterior es real y ejecutable.
  - (No se proyecta) Y hay que anunciar como se califica esa frontera, porque es contraintuitivo para el estudiante que cree que reconocer un limite es admitir una carencia: la pregunta 9 SUMA un punto por ubicar correctamente el propio trabajo y decir que llega hasta «listo para desplegar», y DESCUENTA la mitad de la pregunta a quien afirme haber construido CD.

**[Slide 6] CI/CD sin tarjeta** — 4 vinetas.

**[Slide 7] GitHub Actions en cinco palabras** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - GitHub Actions es la herramienta del dia porque es gratis, corre en el navegador y produce evidencia verificable.
  - Un workflow es un archivo YAML en la carpeta.github/workflows; el nombre es libre y ci.yml es la convencion.
  - El evento o disparador declara cuando corre: on push para cada subida, on pull_request para cada propuesta de cambio, workflow_dispatch para un boton manual, schedule para una hora fija.
  - Un job es un conjunto de pasos que corre en un runner, una maquina virtual limpia que se crea para esa ejecucion y se destruye al terminar.
  - Un step es un comando o el uso de una action, unidad reutilizable publicada por otros.
  - Que el runner sea limpio y efimero es el punto pedagogico central: demuestra que la construccion no depende de nada instalado a mano en el portatil de nadie.
  - NOTAS:
  - Su vocabulario tiene cinco palabras.
  - (No se proyecta) Advertencias: el YAML se indenta con espacios y nunca con tabulaciones, causa numero uno de un pipeline que no arranca; y en el nivel gratuito los repositorios publicos tienen minutos ilimitados mientras los privados tienen una cuota del orden de 2000 minutos al mes, cifra que conviene confirmar en la pagina de facturacion porque el proveedor la cambia.

**[Slide 8] Los tres bloques de un workflow, y el orden de los pasos** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un workflow no es un archivo cualquiera: tiene tres bloques nombrados y tres pasos en orden.
  - El primer bloque son los DISPARADORES, es decir la clave on, y basta con on push y pull_request bien escritos.
  - Los tres PASOS van presentes y en ORDEN: construccion, prueba y despliegue simulado.
  - El orden no es capricho ni estetica: probar antes de construir no prueba el artefacto que se va a entregar, y desplegar antes de probar es exactamente lo que la integracion continua existe para impedir.
  - Un punto y medio adicional es que el paso de despliegue este ROTULADO como simulado y no prometa un despliegue real; con escribir «Despliegue SIMULADO (no despliega a ningun servidor)» en el nombre del paso se cumple.
  - (No se proyecta) Un punto y medio es el ENTORNO de ejecucion, la clave runs-on, tipicamente ubuntu-latest; es el bloque que el estudiante omite mas y el mas facil de recuperar.
  - (No se proyecta) Y un punto es la coherencia con el Dockerfile del Corte 1: la misma imagen y el mismo puerto, es decir cloudlite-api con su etiqueta 0.1.0 y el 8080 del EXPOSE de la Clase 3.
  - (No se proyecta) Falta la sancion, que conviene anunciar dos veces: la pregunta vale CERO completa si aparece un secreto escrito en claro dentro del YAML, sin importar lo bien que este el resto.
  - (No se proyecta) Es la misma politica que el estudiante escribio en la pregunta 3 del Corte 2, y esta es la clase donde se comprueba si la cumple.

**[Slide 9] YAML mínimo** — 5 vinetas.

**[Slide 10] .github/workflows/ci.yml — CI real, no un echo** — 15 vinetas.

**[Slide 11] Monitorear y observar: la segunda mitad cambia de lado** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Monitorear es vigilar indicadores decididos de antemano; observabilidad es la capacidad de responder preguntas nuevas sobre el sistema a partir de lo que el sistema emite, sin agregar codigo por cada duda.
  - Las metricas son numeros medidos en el tiempo, baratas porque se agregan, y detectan que algo cambio.
  - Los logs, o registros, son eventos discretos con contexto, caros en volumen, y explican por que cambio.
  - La distincion entre metrica y registro importa: al menos una de las senales de un plan deberia ser un REGISTRO y no una metrica numerica, es decir algo que se escribe para poder reconstruir que paso despues.
  - La practica minima documentable es el log estructurado: cada linea es un objeto con campos fijos como fecha, nivel, identificador de peticion, ruta, codigo de estado y duracion en milisegundos.
  - Con ese identificador propagado entre servicios se reconstruye el recorrido: una traza pobre, pero real.
  - Un ejemplo de linea estructurada es: fecha 2026-10-03 10:15:02, nivel INFO, peticion a91f, ruta POST /turnos, estado 201, duracion 84 ms.
  - Un error comun es escribir logs como frases libres: se leen bien, pero no se pueden filtrar ni contar.
  - NOTAS:
  - Se apoya en tres tipos de senal.
  - (No se proyecta) La segunda mitad de la clase cambia de lado: ya no se trata de validar antes, sino de saber que pasa despues.
  - (No se proyecta) Las trazas siguen el recorrido de una sola peticion por varios servicios y son necesarias porque la Clase 4 convirtio el sistema en distribuido: cuando la peticion pasa por la API y por el servicio de notificaciones, saber cual de los dos tardo es imposible con metricas agregadas.

**[Slide 12] Las cuatro senales de oro, con definicion operativa** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Las cuatro senales de oro son latencia, trafico, errores y saturacion, y cada una necesita definicion operativa.
  - Trafico es cuanta demanda llega, en peticiones por segundo o por minuto.
  - Saturacion es que tan cerca esta el recurso mas escaso de su limite: CPU, memoria, disco o, en la mayoria de las APIs reales, las conexiones libres del pool de la base de datos
  - La convencion es alertar cuando un recurso pasa del 70 u 80 por ciento sostenido, y es convencion, no ley.
  - Latencia merece explicacion aparte porque introduce el percentil, el valor por debajo del cual cae un porcentaje dado de las mediciones: si el p95 de la API es 300 milisegundos
  - 95 de cada 100 peticiones respondieron en 300 milisegundos o menos y 5 tardaron mas.
  - Es mas honesto que el promedio, y el ejemplo lo prueba: 99 peticiones de 50 milisegundos y una de 5 segundos dan un promedio de 99 milisegundos, que parece excelente, mientras el p99 es 5 segundos y corresponde a un usuario mirando una pantalla congelada.
  - En CloudLite Turnos las cuatro senales son: latencia, el p95 del endpoint de reserva; trafico, las reservas por minuto; errores, el porcentaje de respuestas 5xx; saturacion, el uso del pool de conexiones a la base de datos.
  - Un error comun es medir solo la CPU: es una senal de saturacion entre varias, y en una API que espera a la base de datos casi nunca es la primera en agotarse.
  - (No se proyecta) Errores es la proporcion de peticiones que fallan, tipicamente el porcentaje de respuestas 5xx; conviene expresarlo como disponibilidad, y aqui hay aritmetica que el docente debe citar: 99,9 por ciento equivale a unos 43 minutos de indisponibilidad al mes y 99,99 por ciento a unos 4 minutos, lo cual no es convencion sino calculo sobre los 43.200 minutos de un mes de treinta dias.

**[Slide 13] Monitoreo y optimización** — 5 vinetas.

**[Slide 14] La tabla de senales, con sus tres columnas** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El plan de monitoreo es una tabla de entre 4 y 6 filas con TRES columnas: «Senal», «Que se mide en MI dominio» y «Umbral u objetivo».
  - La regla que decide la mitad de la nota se dice en una frase: una senal sin umbral NO SUMA, aunque este bien elegida.
  - «el listado de disponibilidad debe responder en menos de 400 milisegundos y si pasa de 800 se revisa» si, porque define cuando hay que actuar.
  - La segunda columna tiene que referirse a operaciones del dominio propio, asi que «el sistema» no es una respuesta y «el listado de disponibilidad de canchas» o «el registro de una reserva» si.
  - Cada umbral necesita su accion: que se HACE cuando se cruza es lo que convierte una lista de metricas en un plan de operacion.
  - Un ejemplo de fila completa es: Senal «latencia del listado de turnos»
  - Que se mide «p95 del GET /turnos»
  - Umbral «menos de 300 ms; si se supera durante 5 minutos, se revisa el indice de la consulta».
  - Un error comun es un umbral sin numero, como «latencia alta»: no dice cuando actuar.
  - Otro es una senal generica, como «el sistema»: la fila tiene que nombrar una operacion concreta del dominio.
  - NOTAS:
  - «Medimos la latencia» no permite decidir nada
  - Esa accion no es una cuarta columna: se escribe dentro del umbral, como en el ejemplo del listado.
  - La fila tiene senal, objeto concreto del dominio y una accion atada al umbral.
  - (No se proyecta) El reparto de sus 6 puntos es un punto por senal bien formada con su umbral hasta la cuarta, hasta un punto adicional entre las senales quinta y sexta, y un punto por que al menos una sea un registro.
  - (No se proyecta) El umbral puede ser discutible, y hay que decir que se acepta discutible: lo que no puede es faltar.
  - (No se proyecta) Una tabla de referencia para CloudLite, que el docente puede llenar en vivo: latencia p95 del inicio de sesion y del listado principal, con objetivo bajo 300 milisegundos; peticiones por minuto en la hora pico, con un valor esperado que sirva de linea base; porcentaje de respuestas 5xx, con alerta sobre el 1 por ciento sostenido; uso del pool de conexiones, con alerta sobre el 80 por ciento; y la fila que casi nadie escribe y vale un punto, un REGISTRO: el log estructurado de cada reserva rechazada y de cada intento de inicio de sesion fallido, con identificador de peticion, ruta y codigo, cuyo umbral es un evento observable, por ejemplo mas de cinco fallos del mismo usuario en diez minutos se revisa.
  - (No se proyecta) Conviene proyectar esa fila y decir «esta es la que falta en el 80 por ciento de las entregas».
  - (No se proyecta) Ahi entra la optimizacion de la segunda mitad del tema: paginar, con veinte a cincuenta elementos por pagina, porque un endpoint que devuelve cincuenta mil registros es problema de latencia y de memoria; indexar la columna por la que se filtra, porque sin indice el motor recorre la tabla completa; cachear lecturas repetidas, donde una tasa de acierto del 90 por ciento significa que nueve de cada diez lecturas no llegan a la base; y limitar la tasa de peticiones, el control de denegacion de servicio de la Clase 6.

**[Slide 15] El pipeline del stub de CloudLite, paso por paso** — 2 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un job corre en ubuntu-latest y hace, en este orden: descargar el codigo con la action de checkout, instalar el runtime con la action de setup del lenguaje
  - Un paso Construir que instala dependencias y ejecuta docker build con la imagen etiquetada, un paso Probar que corre las pruebas
  - Y un paso final rotulado como despliegue simulado que imprime la etiqueta de version y publica un artefacto, un archivo que queda guardado junto a la corrida.
  - Que docker build forme parte de la construccion tiene un valor extra: comprueba en cada cambio que el Dockerfile sigue siendo valido, que es una de las cosas que se rompen en silencio.
  - Un pipeline sano falla rapido: si la construccion falla, la prueba no se ejecuta, y el autor del cambio recibe el aviso en minutos.
  - En GitHub Actions cada paso que termina con un codigo de salida distinto de 0 detiene el job y lo marca en rojo: esa es la condicion de fallo que convierte el workflow en una verificacion real.
  - Un ejemplo de fallo util: alguien cambia la respuesta de /health y no actualiza la prueba; el paso de prueba termina con codigo 1, la corrida queda en rojo y el cambio no se integra hasta corregirlo.
  - NOTAS:
  - El workflow se dispara en push y en pull_request.
  - (No se proyecta) El ejemplo concreto es el pipeline del stub de CloudLite, que ya existe desde la Clase 3 como Dockerfile y contenedor, y la diapositiva del ci.yml es el molde que se puede copiar.
  - (No se proyecta) La evidencia del entregable es doble: el archivo ci.yml en el repositorio y la captura de una corrida en verde con los nombres de los pasos visibles; si Actions falla por cuota o por red se acepta el YAML con la explicacion paso por paso, pero eso es plan B y hay que decir que lo es.

**[Slide 16] La condicion de fallo: la pregunta que separa un CI de una decoracion verde** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un ci.yml propio se explica en tres campos.
  - Y el tercero, el corazon del asunto: con que condicion el pipeline debe FALLAR.
  - Un pipeline que no puede fallar nunca no sirve: un workflow cuyo unico paso imprime un mensaje de exito siempre sale verde, y un check que siempre sale verde no aporta ninguna informacion; es una decoracion.
  - Los tres campos son: que se construye, que se prueba y que condicion vuelve rojo el pipeline.
  - Un ejemplo de condicion real es: la corrida falla si npm test devuelve un codigo distinto de 0, por ejemplo cuando GET /health no responde 200.
  - NOTAS:
  - Uno y medio, que se compila o se instala.
  - Uno y medio, que se ejecuta en la prueba y que comprueba exactamente.
  - Si la respuesta no aparece en diez segundos, el pipeline no valida nada todavia.
  - (No se proyecta) La forma de responderlo es una prueba mental que el docente debe hacer en voz alta y en vivo: que error tendria que introducir yo en el codigo para que este pipeline lo detecte.
  - (No se proyecta) Aqui es donde aparece la pregunta previsible del grupo, y hay que salir a su encuentro: para que escribir pruebas de un stub que casi no hace nada.
  - (No se proyecta) La respuesta es que una sola prueba que verifique que el endpoint /health responde 200 detecta la clase de error mas costosa en operacion, que la aplicacion ya no arranca; y con eso la condicion de fallo se escribe sola: el check sale rojo si /health deja de responder 200, si falta una dependencia declarada o si el docker build no compila.
  - (No se proyecta) Conviene romper el pipeline a proposito en la demo, porque un check rojo proyectado ensena mas que el parrafo anterior.

**[Slide 17] Donde se ejecuta de verdad la politica de secretos de la Clase 6** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La plataforma enmascara los secretos en el registro de salida, pero enmascarar no es impedir la fuga: si un paso imprime el valor transformado, por ejemplo codificado, sale en claro; la regla es no imprimir secretos nunca.
  - Y por diseno los secretos no se entregan a las corridas disparadas por un pull_request que viene de un fork, para que un extrano no pueda proponer un cambio que los imprima.
  - La consecuencia practica es que la validacion de un cambio externo no puede depender de credenciales, y por eso las pruebas del stub deben correr sin acceso a servicios reales, con valores ficticios o un doble simulado.
  - NOTAS:
  - Los valores sensibles se guardan en el repositorio bajo Settings, Secrets and variables, Actions; el workflow los referencia por nombre y la plataforma los inyecta como variables de entorno solo durante la corrida.
  - Dos detalles evitan sustos.
  - PREGUNTAS FRECUENTES DEL GRUPO
  - «Mi proyecto no tiene pruebas automatizadas, que pongo en el paso Probar?» Una prueba, aunque sea una: que el proceso arranca y que /health responde 200.
  - «Puedo poner solo metricas numericas?» No sin perder un punto: al menos una senal tiene que ser un registro.
  - La mas facil de justificar es el log de los rechazos de negocio del propio dominio, que ademas es la unica forma de contestar despues por que se rechazo una operacion concreta.
  - Cuatro que aparecen todos los semestres.
  - Un umbral justificado asi vale, aunque despues la medicion lo corrija.
  - (No se proyecta) El pipeline es tambien donde se ejecuta de verdad la politica de secretos escrita en la Clase 6.
  - (No se proyecta) Y el recordatorio de calificacion: un secreto en claro en el YAML no descuenta, anula la pregunta 7 entera.

**[Slide 18] Secretos en el workflow, y hasta donde llega el pipeline** — 17 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 8 · Monitoreo y optimización · CI/CD
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Integracion continua: el problema que resuelve, en definicion operativa
5. Entrega continua y despliegue continuo: la sigla CD es ambigua
6. CI/CD sin tarjeta
7. GitHub Actions en cinco palabras
8. Los tres bloques de un workflow, y el orden de los pasos
9. YAML mínimo
10. .github/workflows/ci.yml — CI real, no un echo
11. Monitorear y observar: la segunda mitad cambia de lado
12. Las cuatro senales de oro, con definicion operativa
13. Monitoreo y optimización
14. La tabla de senales, con sus tres columnas
15. El pipeline del stub de CloudLite, paso por paso
16. La condicion de fallo: la pregunta que separa un CI de una decoracion verde
17. Donde se ejecuta de verdad la politica de secretos de la Clase 6
18. Secretos en el workflow, y hasta donde llega el pipeline
19. Clase 8 · cierre conceptual

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**.
Entregable concreto: .github/workflows/ci.yml + sección Monitoreo/CI del informe.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 6]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **CI/CD sin tarjeta** · [Slide 6]
- **YAML mínimo** · [Slide 9]
- **Monitoreo y optimización** · [Slide 13]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 10]
Herramienta del día: **Navegador · editor de código del curso (YAML)**.
**Demo que usted debe poder repetir:** Un workflow de GitHub Actions que corra de verdad, con los tres pasos calificados

1. Cree `.github/workflows/ci.yml` copiando la diapositiva del ci.yml: `on: [push, pull_request]`, `runs-on: ubuntu-latest` y los pasos en ORDEN — Construir, Probar, Despliegue SIMULADO.
2. Senale los tres bloques mientras los escribe: «disparadores, entorno y pasos: son 2, 1.5 y 4 puntos de la pregunta 7».
3. En el paso Construir use la MISMA imagen de la Clase 3: `npm ci && docker build -t cloudlite-api:0.1.0 .` — la coherencia con el Dockerfile del Corte 1 vale 1 pt.
4. Haga commit y push, abra la pestana Actions y espere el check verde; abra el log del paso Probar: «esto es evidencia, no una diapositiva que dice que tenemos CI».
5. Rompa el pipeline a proposito, 60 segundos: cambie la asercion de la prueba (o borre `server.js`), haga push y muestre el check ROJO. Diga: «esta es la respuesta de la pregunta 8: con que condicion falla. Si no pueden romperlo, no estan validando nada».
6. Vuelva a dejarlo verde y lea en voz alta el nombre del ultimo paso: «Despliegue SIMULADO (no despliega a ningun servidor)». Aclare la frontera: el pipeline llega hasta «listo para desplegar», y decirlo asi SUMA en la pregunta 9 — afirmar que ya hay CD resta la mitad.
7. Cierre en Settings > Secrets and variables > Actions: «los secretos viven aqui y se referencian por nombre. Un secreto escrito en claro dentro del YAML es cero en toda la pregunta 7».

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 8/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Run verde del workflow: build + test reales, no un `echo ok` [[captura: salida-actions-run.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · opcional · sin diapositiva
El taller es **opcional** y ya no está en el deck: si se hace hoy, comparte el `Taller … .docx` de
`Clases/Clase 8 - Monitoreo optimizacion y CI-CD/` (los pasos también están en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 19]
Di: «Queda avanzado: Workflow Actions (build/test/simulate) + métricas de monitoreo del PI.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en la plataforma del curso. Siguiente hito del PI según el plan.»


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
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase08.png | receta: 1) Abre Navegador · editor de código del curso (YAML) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 8/Capturas/demo-clase08.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase08.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 8/Capturas/evidencia-clase08.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
