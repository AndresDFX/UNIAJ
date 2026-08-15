# Guion docente · Clase 2 · Ciclos de vida del software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.
- **Entregable de hoy:** Un documento de una pagina en Google Docs con la tabla Fase / Pregunta que responde / Artefacto de VetCare / Quien lo aprueba, mas dos diagramas en draw.io (recorrido lineal y recorrido en tres vueltas) exportados a PDF y subidos a ExamLab.
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 2 - Ciclos de vida del software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un ciclo de vida del software es el orden en que se recorren las etapas que van desde que alguien dice 'necesito un sistema' hasta que ese sistema se apaga definitivamente. Las etapas clasicas son cinco: requisitos, diseño, construccion, pruebas y mantenimiento. Lo importante no es memorizar los nombres sino entender que cada fase tiene tres cosas: una entrada (lo que recibe de la fase anterior), una salida tangible llamada artefacto (un documento, un diagrama, un programa) y un criterio para decir 'esto ya quedo'. Si una fase no produce un artefacto verificable, esa fase no existe, existe una conversacion. En VetCare la fase de requisitos no termina cuando el equipo 'ya entendio' el problema de Huellitas: termina cuando existe una lista numerada de requisitos funcionales y no funcionales que la clinica leyo y aprobo.

Vale la pena decir con precision que produce cada fase, porque ahi se cae la mitad de los equipos. Requisitos responde la pregunta QUE debe hacer el sistema y produce la lista de RF y RNF, el glosario y las reglas de negocio. Diseño responde COMO se va a lograr y produce casos de uso, diagramas de clases, modelo de datos, wireframes y mockups. Construccion es escribir el codigo y produce el ejecutable. Pruebas verifica que lo construido corresponde a lo pedido y produce casos de prueba y evidencias. Mantenimiento arregla, ajusta y evoluciona el sistema ya en uso. En nuestro Proyecto Integrador esto se reparte: Seminario de Sistemas vive en requisitos y diseño (los planos), y Programacion II vive en construccion y pruebas (la obra). Por eso aqui nunca se califica codigo: se califica que los planos esten completos, coherentes y sean construibles.

La gran decision no es cuales fases hacer, sino cuantas veces recorrerlas y con cuanto sistema a la vez. Recorrerlas una sola vez y en orden significa cerrar requisitos de TODO VetCare, luego diseñar TODO VetCare, luego construir TODO. Recorrerlas en ciclos significa tomar un pedazo util del sistema y pasarlo por las cinco fases en una vuelta corta, y despues repetir con el siguiente pedazo. En VetCare la vuelta 1 podria ser solo la ficha del paciente (requisitos de la ficha, diseño de la ficha, mockup de la ficha, revision con la clinica); la vuelta 2, la historia clinica y la busqueda; la vuelta 3, los reportes y metricas. La diferencia practica es brutal: en el recorrido unico la clinica ve algo hasta el final y un malentendido de la semana 2 se descubre en la semana 15; en el recorrido en ciclos la clinica opina cada dos o tres semanas y el error se corrige cuando todavia es barato corregirlo.

Hay que separar dos palabras que los equipos usan como sinonimos y no lo son: proyecto y producto. Un proyecto es un esfuerzo temporal, con inicio, fin, alcance, presupuesto y responsables; se acaba y se cierra. Un producto es el sistema vivo, que la gente usa, que tiene versiones y que sigue existiendo cuando el proyecto ya se cerro. En VetCare el proyecto es 'entregar los planos y el prototipo de VetCare en este semestre'; el producto es el sistema que Huellitas usaria durante los proximos años, con su version 1.0, su 1.1 cuando pidan vacunacion a domicilio y su 2.0 cuando quieran facturacion electronica. Esta distincion tiene una consecuencia dura: la fase mas larga y mas costosa de la vida de un sistema no es construirlo, es mantenerlo, y por eso el diseño y la documentacion que hacemos aqui no son un tramite, son lo que permite que otro entienda el sistema dentro de dos años.

Como se elige el recorrido? Con criterios, no con moda. Si los requisitos son estables, el contrato es cerrado y el sistema es critico, conviene un recorrido lineal con aprobaciones formales. Si el dominio es nuevo, el cliente descubre lo que quiere cuando lo ve, y hay margen para ajustar, conviene un recorrido en ciclos. En VetCare aplican los dos matices: los datos basicos de un paciente (nombre, especie, raza, propietario) son estables y se pueden cerrar temprano; el tablero de metricas es incierto porque la clinica nunca ha visto uno y va a cambiar de opinion apenas lo vea. Ademas, el ciclo elegido debe caber en la realidad del curso: el estudiante que solo cursa Seminario cierra con documento de diseño y prototipo navegable, y esa es una ruta completa, porque el ciclo de vida del software incluye fases donde no se escribe una sola linea de codigo y aun asi se produce valor.

Error tipico del docente que no domina el tema: confundir ciclo de vida con metodologia y decir que 'cascada es malo y agil es bueno'. Ciclo de vida es el conjunto de fases; metodologia es la forma organizada de recorrerlas. Agil no elimina el analisis ni el diseño, los distribuye en vueltas cortas. El segundo error, mas fino, es llamar iterativo a algo que solo es incremental: si el equipo entrega el modulo de pacientes, luego el de citas y luego el de reportes, y nunca vuelve a tocar lo entregado, eso es incremental pero no iterativo; iterar es volver sobre lo mismo y mejorarlo tras la retroalimentacion del cliente. El tercer error es proyectar el diagrama de cascada con flechitas hacia atras y decir 'ven, es iterativo': esas flechas son retrabajo por errores detectados, no vueltas planificadas de mejora.

**Demo que usted debe poder repetir:** El docente arma en vivo en draw.io el ciclo de VetCare en dos versiones, una sola pasada y tres vueltas, y muestra que las cajas son identicas y lo unico que cambia es el recorrido.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente arma en vivo en draw.io el ciclo de VetCare en dos versiones, una sola pasada y tres vueltas, y muestra que las cajas son identicas y lo unico que cambia es el recorrido.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 2/Plantillas/Mapa-Ciclo-de-Vida-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. En Google Docs cree la tabla de cuatro columnas (Fase / Pregunta que responde / Artefacto concreto de VetCare / Quien lo aprueba) y llenela con las cinco fases; en la columna del artefacto esta prohibido escribir generalidades: debe decir cosas como 'Lista RF-01 a RF-12 de Huellitas' o 'Mockup de la ficha del paciente'.
2. Marque con relleno amarillo la fila de la fase donde esta el equipo hoy y escriba debajo dos evidencias verificables que lo demuestren (por ejemplo: 'existe la entrevista transcrita' y 'no existe ningun diagrama aprobado').
3. En draw.io dibuje el recorrido lineal de VetCare: cinco cajas en fila, y sobre cada flecha escriba el artefacto que se entrega para poder pasar a la siguiente fase.
4. Duplique la pagina en draw.io y dibuje el recorrido en tres vueltas: las mismas cinco cajas, pero con las vueltas rotuladas Incremento 1 (ficha del paciente), Incremento 2 (historia clinica y busqueda) e Incremento 3 (reportes y metricas), y una flecha de retroalimentacion desde la clinica hacia requisitos.
5. Escriba al final del documento un parrafo de tres renglones titulado 'Producto vs proyecto en VetCare' que responda: cuando termina el proyecto, cuando terminaria el producto y un ejemplo concreto de una solicitud de mantenimiento; exporte a PDF y suba el archivo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento de una pagina en Google Docs con la tabla Fase / Pregunta que responde / Artefacto de VetCare / Quien lo aprueba, mas dos diagramas en draw.io (recorrido lineal y recorrido en tres vueltas) exportados a PDF y subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - VetCare.docx` — no proyectar completa.
