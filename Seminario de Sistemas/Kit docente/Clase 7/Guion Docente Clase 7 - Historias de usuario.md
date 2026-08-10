# Guion docente · Clase 7 · Historias de usuario

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el backlog inicial de VetCare: dos epicas descompuestas en ocho historias priorizadas, con criterios de aceptacion y talla en puntos.
- **Entregable de hoy:** Tablero de backlog con 8 historias en formato Como/quiero/para, cada una con 2 o 3 criterios de aceptacion en Dado-Cuando-Entonces, estimacion en puntos y trazabilidad al RF de la clase 6, subido a ExamLab.
- **Herramienta:** Google Docs · Excalidraw
- **Slides:** `Clases/Clase 7 - Historias de usuario/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Una historia de usuario no es un requisito abreviado ni una moda de las metodologias agiles: es el recordatorio corto de una conversacion pendiente entre quien necesita el sistema y quien lo va a construir. Su formato canonico tiene tres partes: Como <rol> quiero <accion> para <beneficio>. El rol obliga a nombrar a alguien concreto (la auxiliar Marcela, el veterinario de turno, el dueno de la mascota) y no al generico usuario, que no existe en ninguna clinica del mundo; la accion describe algo que esa persona hace, no algo que hace la base de datos por dentro; y el para es la parte que casi todo el mundo borra por afan y es la mas valiosa, porque es la unica que explica por que vale la pena gastar tiempo y plata en eso. En VetCare, Como auxiliar quiero buscar la ficha de una mascota por el documento del dueno para no revolver la carpeta fisica mientras el paciente espera en el meson se entiende sin traduccion; en cambio El sistema debe tener un buscador no dice a quien le sirve ni que dolor cura. Ron Jeffries lo resumio en tres C: Card, la tarjeta corta; Conversation, la charla que aclara los detalles; y Confirmation, los criterios de aceptacion. La tarjeta sin conversacion es un titulo huerfano, y la conversacion sin criterios es un acuerdo que nadie puede cobrar. Frente al requisito tradicional de la clase pasada, la historia no lo reemplaza: el requisito es el contrato formal y la historia es la unidad de trabajo con la que se planea la entrega.

Los criterios de aceptacion son la parte que convierte una historia bonita en una historia entregable, y se escriben en el patron Dado <contexto inicial> Cuando <accion del usuario> Entonces <resultado observable>. Cada criterio debe poder responderse con un si o un no mirando la pantalla, nunca con un depende. Para la historia de buscar el historial en VetCare los criterios serian: Dado un dueno con tres mascotas registradas, cuando busco por su documento, entonces el sistema lista las tres mascotas con nombre y especie; Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo sus atenciones de la mas reciente a la mas antigua; Dado un documento que no existe, cuando busco, entonces el sistema muestra un mensaje claro y ofrece crear el dueno. Fijense que el tercer criterio es el que casi siempre falta: el camino alterno, el caso feo, el error. Una historia con solo criterios felices es una historia a medio pensar. Ademas, los criterios de aceptacion son el puente directo con el prototipo navegable y con las pruebas que hara el companero de Programacion II, porque son literalmente el guion de lo que se va a revisar.

INVEST es la lista de chequeo para saber si una historia esta bien cortada, y conviene revisarla letra por letra con VetCare en la mano. Independiente: se puede hacer sin esperar a otra; si la historia de agendar cita necesita obligatoriamente que exista la de registrar mascota, hay dependencia y toca ordenarlas. Negociable: la historia describe la necesidad, no la solucion tecnica; decir quiero un combo desplegable con autocompletar en JavaScript ya no es historia, es diseno impuesto. Valiosa: alguien de la clinica gana algo real; si nadie de Huellitas nota la diferencia, no es historia sino tarea interna. Estimable: el equipo entiende lo suficiente para tallarla; si nadie sabe cuanto pesa, falta conversacion o hace falta investigar aparte. Small o pequena: cabe en una iteracion; si toma tres semanas es una epica disfrazada. Testeable: tiene criterios verificables, que es exactamente la misma regla de oro de la clase pasada aplicada en formato agil. Una historia que falla dos letras de INVEST no se planea todavia, se vuelve a partir.

Una epica es una historia grande que todavia no cabe en una iteracion, y descomponerla es una habilidad que se aprende cortando mal varias veces. El corte correcto es vertical, como una rebanada de pastel que trae bizcocho, crema y cubierta: cada historia atraviesa pantalla, logica y datos y deja algo que el usuario puede usar. El corte equivocado es horizontal, por capas: una historia para la pantalla, otra para la logica y otra para la base de datos; asi ninguna de las tres sirve sola y el cliente no ve nada hasta que estan las tres. En VetCare la epica Historial clinico se parte en: consultar historial por documento del dueno, registrar una atencion nueva, adjuntar resultados de laboratorio y filtrar el historial por rango de fechas; cada una entregable y demostrable por separado. Otros ejes utiles para cortar son por tipo de dato (primero solo perros y gatos, despues otras especies), por regla de negocio (primero sin control de acceso, luego con perfiles) y por camino (primero el flujo feliz, luego los errores). El nombre de la epica se conserva como etiqueta en cada historia para no perder el hilo.

Estimar en agil no es adivinar horas sino comparar tamanos, y esa es la razon de los puntos de historia: son una medida relativa que mezcla esfuerzo, complejidad e incertidumbre. Se toma una historia mediana y conocida como referencia (por ejemplo registrar un dueno vale 3 puntos) y todas las demas se comparan contra ella usando una escala tipo Fibonacci 1, 2, 3, 5, 8, 13, donde el salto grande refleja que entre mas grande la historia, menos confiable la estimacion; si algo llega a 13 o mas, la senal no es de dificultad sino de que hay que partirla. La tecnica de sala es el planning poker: todos muestran su carta al tiempo y lo importante no es el numero sino la discusion cuando alguien dice 2 y otro dice 8, porque ahi aparece el requisito que unos entendieron y otros no. Con dos o tres iteraciones se conoce la velocidad del equipo y recien ahi se puede prometer fechas. En el Proyecto Integrador este backlog es la lista de trabajo que se le entrega al companero de Programacion II para que sepa por donde empezar; y quien solo cursa Seminario usa el mismo backlog para ordenar las pantallas de su prototipo navegable, en el mismo orden de prioridad.

Error tipico del docente que no domina el tema: pensar que la historia de usuario es simplemente el mismo requisito escrito con la formula Como/quiero/para y calificar que la formula este completa. Con ese criterio pasan barbaridades como Como usuario quiero un boton de guardar para guardar, que cumple la plantilla y no dice absolutamente nada: el rol es generico, la accion es una solucion tecnica y el beneficio es una repeticion circular de la accion. Tambien es tipico aceptar historias sin criterios de aceptacion porque parece que alargan la tarea, permitir el corte horizontal por capas porque a los estudiantes les suena logico, y pedir estimacion en horas porque el docente no entiende para que sirven los puntos, con lo cual el ejercicio se vuelve un cronograma falso. El antidoto es revisar cada historia con tres preguntas en voz alta: quien es esta persona con nombre y cargo en la clinica Huellitas, que gana ella cuando esto exista, y con que prueba concreta se acepta. Si la respuesta al beneficio repite la accion, la historia se devuelve sin negociar.

**Demo que usted debe poder repetir:** El docente toma el RF-03 del catalogo, lo convierte en vivo en historia con criterios y luego muestra una historia partida por capas para tumbarla con INVEST.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el backlog inicial de VetCare: dos epicas descompuestas en ocho historias priorizadas, con criterios de aceptacion y talla en puntos. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente toma el RF-03 del catalogo, lo convierte en vivo en historia con criterios y luego muestra una historia partida por capas para tumbarla con INVEST.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 7/Plantillas/Backlog-Historias-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: agrupe los RF del catalogo de la clase 6 en dos epicas de VetCare (por ejemplo Gestion de pacientes e Historial y agenda) y escriba el nombre y el objetivo de cada epica en una linea.
2. Paso 2: descomponga las dos epicas en 8 historias con el formato Como <rol de la clinica Huellitas> quiero <accion> para <beneficio>, usando roles concretos (auxiliar, veterinario, administrador) y nunca la palabra usuario.
3. Paso 3: escriba 2 o 3 criterios de aceptacion por historia en Dado-Cuando-Entonces, e incluya obligatoriamente un criterio de camino alterno o de error en al menos cuatro de las ocho historias.
4. Paso 4: revise cada historia contra INVEST marcando las seis letras con si o no; toda historia que falle dos o mas letras debe reescribirse o partirse antes de continuar.
5. Paso 5: estime en puntos con la escala 1, 2, 3, 5, 8 tomando 'registrar un dueno = 3' como referencia, ordene el backlog de mayor a menor prioridad, agregue la columna de trazabilidad al RF de origen y suba el tablero a ExamLab.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Tablero de backlog con 8 historias en formato Como/quiero/para, cada una con 2 o 3 criterios de aceptacion en Dado-Cuando-Entonces, estimacion en puntos y trazabilidad al RF de la clase 6, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 7/Quiz Clase 7 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el backlog inicial de VetCare: dos epicas descompuestas en ocho historias priorizadas, con criterios de aceptacion y talla en puntos.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 7/Solucion Taller Clase 7 - VetCare.docx` — no proyectar completa.
