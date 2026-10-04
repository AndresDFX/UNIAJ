# Guion docente · Clase 2 · Ciclos de vida del software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.
- **Practica (opcional):** `Clases/Clase 2 - Ciclos de vida del software/Taller PI - Clase 2 - VetCare.docx` — no esta en el deck
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 2 - Ciclos de vida del software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Qué es un ciclo de vida** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un ciclo de vida del software es el orden en que se recorren las etapas que van desde que alguien dice 'necesito un sistema' hasta que ese sistema se apaga definitivamente.
  - Las etapas clasicas son cinco: requisitos, diseño, construccion, pruebas y mantenimiento.
  - En la clinica la fase de requisitos no termina cuando el equipo 'ya entendio' el problema de la clinica: termina cuando existe una lista numerada de requisitos funcionales y no funcionales que la clinica leyo y aprobo.
  - NOTAS:
  - Lo importante no es memorizar los nombres sino entender que cada fase tiene tres cosas: una entrada (lo que recibe de la fase anterior), una salida tangible llamada artefacto (un documento, un diagrama, un programa) y un criterio para decir 'esto ya quedo'.
  - Si una fase no produce un artefacto verificable, esa fase no existe, existe una conversacion.

**[Slide 5] El recorrido lineal del ciclo de vida** — 6 vinetas.

**[Slide 6] El ciclo de vida en Mermaid: mismas cajas, dos recorridos** — 12 vinetas.

**[Slide 7] Qué produce cada fase** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Requisitos responde la pregunta QUE debe hacer el sistema y produce la lista de RF y RNF, el glosario y las reglas de negocio.
  - Construccion es escribir el codigo y produce el ejecutable.
  - En un proyecto de software esto se reparte: Seminario de Sistemas vive en requisitos y diseño (los planos), y Programacion II vive en construccion y pruebas (la obra).
  - NOTAS:
  - Vale la pena decir con precision que produce cada fase, porque ahi se cae la mitad de los equipos.
  - Diseño responde COMO se va a lograr y produce casos de uso, diagramas de clases, modelo de datos, wireframes y mockups.
  - Pruebas verifica que lo construido corresponde a lo pedido y produce casos de prueba y evidencias.
  - Mantenimiento arregla, ajusta y evoluciona el sistema ya en uso.
  - Por eso aqui nunca se revisa codigo: se revisa que los planos esten completos, coherentes y sean construibles.

**[Slide 8] Una vuelta o varias vueltas** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La gran decision no es cuales fases hacer, sino cuantas veces recorrerlas y con cuanto sistema a la vez.
  - En la clinica la vuelta 1 podria ser solo la ficha del paciente (requisitos de la ficha, diseño de la ficha, mockup de la ficha, revision con la clinica); la vuelta 2, la historia clinica y la busqueda; la vuelta 3, los reportes y metricas.
  - La diferencia practica es brutal: en el recorrido unico la clinica ve algo hasta el final y un malentendido de la semana 2 se descubre en la semana 15
  - En el recorrido en ciclos la clinica opina cada dos o tres semanas y el error se corrige cuando todavia es barato corregirlo.
  - NOTAS:
  - Recorrerlas una sola vez y en orden significa cerrar requisitos de TODO el sistema, luego diseñar TODO el sistema, luego construir TODO.
  - Recorrerlas en ciclos significa tomar un pedazo util del sistema y pasarlo por las cinco fases en una vuelta corta, y despues repetir con el siguiente pedazo.

**[Slide 9] El mismo ciclo en tres vueltas** — 15 vinetas.

**[Slide 10] Proyecto, producto y la segunda vida del sistema** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Hay que separar dos palabras que los equipos usan como sinonimos y no lo son: proyecto y producto.
  - Un proyecto es un esfuerzo temporal, con inicio, fin, alcance, presupuesto y responsables; se acaba y se cierra.
  - Un producto es el sistema vivo, que la gente usa, que tiene versiones y que sigue existiendo cuando el proyecto ya se cerro.
  - En la clinica el proyecto es 'entregar los planos y el prototipo del sistema en este semestre'
  - El producto es el sistema que la clinica usaria durante los proximos años, con su version 1.0, su 1.1 cuando pidan vacunacion a domicilio y su 2.0 cuando quieran facturacion electronica.
  - Esta distincion tiene una consecuencia dura: la fase mas larga y mas costosa de la vida de un sistema no es construirlo, es mantenerlo
  - Y por eso el diseño y la documentacion que hacemos aqui no son un tramite, son lo que permite que otro entienda el sistema dentro de dos años.
  - En la industria se estima que el mantenimiento se lleva entre el 60 y el 80 por ciento del costo total de un sistema a lo largo de su vida.
  - En la clinica, agregar dentro de un año los recordatorios de vacunas es mantenimiento: quien lo haga necesitara saber como se relacionan mascota, dueño y cita sin leer todo el codigo.
  - El error comun es dar el proyecto por cerrado cuando se entrega la version 1.0 y no dejar escrito nada para esa segunda vida del producto.

**[Slide 11] Cómo se elige el recorrido** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Si los requisitos son estables, el contrato es cerrado y el sistema es critico, conviene un recorrido lineal con aprobaciones formales.
  - Si el dominio es nuevo, el cliente descubre lo que quiere cuando lo ve, y hay margen para ajustar, conviene un recorrido en ciclos.
  - En la clinica aplican los dos matices: los datos basicos de un paciente (nombre, especie, raza, propietario) son estables y se pueden cerrar temprano
  - El tablero de metricas es incierto porque la clinica nunca ha visto uno y va a cambiar de opinion apenas lo vea.
  - Ademas, el ciclo elegido debe caber en la realidad del curso: el estudiante que solo cursa Seminario cierra con documento de diseño y prototipo navegable
  - Y esa es una ruta completa, porque el ciclo de vida del software incluye fases donde no se escribe una sola linea de codigo y aun asi se produce valor.
  - Un ciclo de vida es, por definicion, la secuencia de fases que recorre un sistema desde la idea hasta su retiro, y elegir el recorrido es decidir cuantas veces y en que orden se pasa por ellas.
  - El error comun es elegir el ciclo por costumbre del equipo y no por la estabilidad de los requisitos.
  - NOTAS:
  - Como se elige el recorrido?
  - Con criterios, no con moda.
  - En la clinica, un recorrido en ciclos permitiria mostrar primero la ficha del paciente y ajustar la agenda despues de escuchar a la recepcionista.


**Demo que usted debe poder repetir:** El docente arma en vivo en draw.io el ciclo de VetCare en dos versiones, una sola pasada y tres vueltas, y muestra que las cajas son identicas y lo unico que cambia es el recorrido.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Ciclos de vida del software. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente arma en vivo en draw.io el ciclo de VetCare en dos versiones, una sola pasada y tres vueltas, y muestra que las cajas son identicas y lo unico que cambia es el recorrido.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 2/Plantillas/Mapa-Ciclo-de-Vida-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 2 - Ciclos de vida del software/Taller PI - Clase 2 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. En Google Docs cree la tabla de cuatro columnas (Fase / Pregunta que responde / Artefacto concreto de VetCare / Quien lo aprueba) y llenela con las cinco fases; en la columna del artefacto esta prohibido escribir generalidades: debe decir cosas como 'Lista RF-01 a RF-12 de Huellitas' o 'Mockup de la ficha del paciente'.
2. Marque con relleno amarillo la fila de la fase donde esta el equipo hoy y escriba debajo dos evidencias verificables que lo demuestren (por ejemplo: 'existe la entrevista transcrita' y 'no existe ningun diagrama aprobado').
3. En draw.io dibuje el recorrido lineal de VetCare: cinco cajas en fila, y sobre cada flecha escriba el artefacto que se entrega para poder pasar a la siguiente fase.
4. Duplique la pagina en draw.io y dibuje el recorrido en tres vueltas: las mismas cinco cajas, pero con las vueltas rotuladas Incremento 1 (ficha del paciente), Incremento 2 (historia clinica y busqueda) e Incremento 3 (reportes y metricas), y una flecha de retroalimentacion desde la clinica hacia requisitos.
5. Escriba al final del documento un parrafo de tres renglones titulado 'Producto vs proyecto en VetCare' que responda: cuando termina el proyecto, cuando terminaria el producto y un ejemplo concreto de una solicitud de mantenimiento; exporte a PDF y suba el archivo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento de una pagina en Google Docs con la tabla Fase / Pregunta que responde / Artefacto de VetCare / Quien lo aprueba, mas dos diagramas en draw.io (recorrido lineal y recorrido en tres vueltas) exportados a PDF y subidos a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx` — no proyectar completa.
