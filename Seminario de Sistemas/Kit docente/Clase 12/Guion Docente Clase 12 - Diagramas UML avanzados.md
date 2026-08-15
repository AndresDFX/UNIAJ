# Guion docente · Clase 12 · Diagramas UML avanzados

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda modelada la dinamica de VetCare: el diagrama de secuencia del caso de uso Agendar cita y el diagrama de actividad del proceso de atencion en el consultorio.
- **Entregable de hoy:** Un PDF con el diagrama de secuencia de Agendar cita incluyendo el fragmento alt para horario ocupado, el diagrama de actividad del proceso de atencion con calles por rol, y la tabla que mapea cada mensaje del diagrama de secuencia a una operacion del diagrama de clases, subido a ExamLab.
- **Herramienta:** draw.io · Mermaid Live Editor
- **Slides:** `Clases/Clase 12 - Diagramas UML avanzados/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Hasta ahora todos los modelos de VetCare han sido estaticos: el diagrama de clases dice que existe una clase Cita con sus atributos, y la especificacion de caso de uso dice que la recepcionista agenda. Lo que ninguno de los dos muestra es la conversacion interna del sistema en el momento exacto en que eso ocurre. Para eso existe el diagrama de secuencia, que es un modelo del tiempo: arriba se dibujan los participantes, de cada uno baja una linea de vida y el tiempo transcurre hacia abajo, de modo que el orden vertical de las flechas es el orden real de los eventos. Cada flecha es un mensaje, es decir, la peticion de un objeto a otro para que haga algo; la flecha llena representa una llamada sincrona, donde quien pide se queda esperando la respuesta, y la flecha punteada representa el retorno con el resultado. Sobre la linea de vida se dibujan barras de activacion que muestran durante cuanto tiempo ese objeto esta trabajando. En VetCare, agendar una cita se ve como una cadena corta y clara: la recepcionista le habla a la pantalla de agenda, la pantalla le habla al control de agenda, el control verifica la mascota, le pregunta al repositorio de citas por la disponibilidad y devuelve una confirmacion con el identificador de la cita.

El diagrama de actividad responde a otra pregunta completamente distinta: no quien le habla a quien, sino en que orden ocurre el trabajo y quien es responsable de cada paso, incluyendo pasos que suceden fuera del computador. Sus elementos son nodo inicial, acciones, nodos de decision con condiciones escritas entre corchetes, nodos de union, barras de bifurcacion y sincronizacion para el trabajo que ocurre en paralelo, y nodo final. La herramienta que lo vuelve realmente util en un proyecto como VetCare son las particiones o calles: una franja por cada rol, de modo que al mirar el dibujo se sabe de un vistazo que hace el Propietario, que hace la Recepcionista, que hace el Veterinario y que hace el sistema. Eso permite modelar el proceso completo de atencion en Huellitas: el propietario llega y pregunta, la recepcionista verifica la cita, si no la tiene se decide entre esperar o reagendar, el veterinario atiende, registra la consulta y si formula medicamentos el flujo se abre en dos ramas paralelas, una de facturacion y otra de programacion del control. Ese dibujo revela algo que ni los casos de uso ni las clases muestran: donde estan los cuellos de botella del proceso real de la clinica.

La pregunta practica es cuando usar cada uno, y la respuesta se decide por el tipo de duda que se quiere resolver. Si la duda es de responsabilidades, es decir, cual objeto deberia encargarse de esto y con quien tiene que hablar para lograrlo, el diagrama correcto es el de secuencia, porque obliga a que cada mensaje tenga un destinatario concreto y por lo tanto una clase que lo sepa atender. Si la duda es de proceso, es decir, en que orden hace la gente las cosas, donde se decide algo y que pasa en paralelo, el diagrama correcto es el de actividad, porque admite pasos manuales, decisiones del negocio y actores humanos que no son objetos de software. Una regla practica para el aula: el diagrama de secuencia se dibuja para un caso de uso y suele cubrir su flujo principal; el diagrama de actividad se dibuja para un proceso de negocio que puede atravesar varios casos de uso. En VetCare, CU-04 Agendar cita se modela con secuencia; la atencion completa desde que el propietario entra por la puerta hasta que sale con la factura se modela con actividad, porque incluye conversaciones y esperas que ningun objeto del sistema ejecuta.

Estos diagramas no se inventan desde cero: se derivan de lo que ya esta escrito, y ahi esta la parte que separa a un estudiante que entendio de uno que solo dibujo. Cada paso del flujo principal del caso de uso se convierte en uno o varios mensajes del diagrama de secuencia, en el mismo orden y con los mismos nombres del glosario canonico que se fijo en la auditoria de la clase once. Si el paso 2 de CU-04 dice que el sistema verifica la disponibilidad del veterinario para esa fecha, entonces debe existir un mensaje llamado consultarDisponibilidad dirigido a algun participante, y ese participante debe ser una clase que exista en el diagrama de clases. Aqui aparece el hallazgo tipico y valiosisimo: al dibujar la secuencia el equipo descubre que envio un mensaje a una clase que no tiene esa operacion, o peor, a una clase que no existe. Eso no es un fracaso del diagrama de secuencia, es su mayor utilidad, porque es la unica manera barata de detectar que el modelo estatico estaba incompleto. Por eso el entregable de hoy incluye la tabla de mapeo mensaje a operacion: obliga a cerrar el circulo entre lo dinamico y lo estatico.

Los flujos alternos tambien se modelan, y para eso existen los fragmentos combinados, que son esos recuadros con una etiqueta en la esquina. El fragmento alt representa caminos excluyentes con sus condiciones de guarda escritas entre corchetes, y es el que usamos en VetCare para el horario ocupado: si hay disponibilidad se guarda la cita y se confirma, si no la hay el sistema ofrece alternativas del dia siguiente. El fragmento opt es un camino opcional que puede ocurrir o no, como enviar el recordatorio si el propietario autorizo mensajeria. El fragmento loop repite un bloque, por ejemplo mientras el veterinario agrega varias vacunas al expediente. La disciplina que hay que enseñar aqui es de alcance: un diagrama de secuencia no debe intentar mostrar los quince alternos posibles, porque se vuelve ilegible y nadie lo lee. La practica sana es dibujar el camino feliz completo mas uno o dos fragmentos que representen las decisiones criticas del negocio, y dejar el resto documentado en el texto de la especificacion, que para eso existe.

Error tipico del docente que no domina el tema: confundir el diagrama de secuencia con un diagrama de flujo y poner rombos de decision colgando de las lineas de vida, cuando las decisiones en secuencia se representan con fragmentos alt y no con rombos. El segundo error es dibujar la secuencia con participantes que no son objetos, como Base de datos, Internet, Usuario final o incluso Sistema, a secas: si el participante no corresponde a una clase del modelo o a un actor legitimo, el diagrama no sirve para verificar responsabilidades y se vuelve un adorno. El tercero es olvidar las flechas de retorno y quedarse solo con las flechas de ida, con lo cual nunca se ve que informacion devuelve cada llamada, que es justamente lo que despues define el resultado esperado de cada operacion en Programacion II. El cuarto es usar diagrama de actividad sin calles, dibujando quince cajitas seguidas donde no se sabe quien hace que, con lo cual se pierde precisamente la ventaja del diagrama. Y el quinto, el mas grave para el proyecto integrador, es dibujar una secuencia que contradice el caso de uso ya especificado: el texto dice que primero se verifica la existencia de la mascota y el dibujo empieza guardando la cita, y como nadie compara los dos artefactos, la contradiccion viaja intacta hasta la construccion.

**Demo que usted debe poder repetir:** El docente toma el flujo principal ya escrito de CU-04 Agendar cita y lo convierte linea por linea en mensajes de un diagrama de secuencia en Mermaid, mostrando en vivo que cada mensaje necesita una clase dueña que lo pueda responder.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda modelada la dinamica de VetCare: el diagrama de secuencia del caso de uso Agendar cita y el diagrama de actividad del proceso de atencion en el consultorio. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente toma el flujo principal ya escrito de CU-04 Agendar cita y lo convierte linea por linea en mensajes de un diagrama de secuencia en Mermaid, mostrando en vivo que cada mensaje necesita una clase dueña que lo pueda responder.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 12/Plantillas/Secuencia-Actividad-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Tomar el flujo principal escrito de CU-04 Agendar cita, y si todavia no esta especificado diligenciar primero la plantilla de la clase nueve, para luego numerar en el documento cual paso genera cual mensaje, de manera que quede una lista de entre seis y ocho mensajes antes de dibujar cualquier cosa.
2. Dibujar el diagrama de secuencia en Mermaid Live Editor o draw.io con la recepcionista como actor y minimo tres participantes que correspondan a clases reales del diagrama de clases de VetCare, incluyendo las flechas de retorno con el dato que devuelven.
3. Agregar un fragmento alt que modele el horario ocupado con sus dos condiciones de guarda escritas, y verificar que el camino del else corresponda a un flujo alterno documentado en la especificacion del caso de uso.
4. Construir la tabla de mapeo mensaje a operacion con tres columnas, mensaje, clase destinataria y operacion que debe existir, y agregar al diagrama de clases toda operacion que hoy falte; ninguna fila puede quedar con la clase en blanco.
5. Dibujar el diagrama de actividad del proceso de atencion en el consultorio con cuatro calles (Propietario, Recepcionista, Veterinario y Sistema VetCare), con minimo dos nodos de decision y una bifurcacion en paralelo, y exportar todo a PDF para subirlo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un PDF con el diagrama de secuencia de Agendar cita incluyendo el fragmento alt para horario ocupado, el diagrama de actividad del proceso de atencion con calles por rol, y la tabla que mapea cada mensaje del diagrama de secuencia a una operacion del diagrama de clases, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 12/Quiz Clase 12 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda modelada la dinamica de VetCare: el diagrama de secuencia del caso de uso Agendar cita y el diagrama de actividad del proceso de atencion en el consultorio.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 12/Solucion Taller Clase 12 - VetCare.docx` — no proyectar completa.
