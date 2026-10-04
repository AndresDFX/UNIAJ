# Guion docente · Clase 11 · Avance del proyecto integrador

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.
- **Practica (opcional):** `Clases/Clase 11 - Avance del proyecto de diseno/Taller PI - Clase 11 - VetCare.docx` — no esta en el deck
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 11 - Avance del proyecto de diseno/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] El paquete de diseño es un sistema de documentos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un paquete de diseño no es una carpeta de archivos sueltos: es un sistema de documentos que deben decir lo mismo con las mismas palabras.
  - El problema es que esos documentos se escribieron en semanas distintas, muchas veces por personas distintas del equipo, y cada semana el entendimiento del dominio cambio un poquito.
  - Ninguno de los tres documentos esta mal por si solo; lo que esta mal es el conjunto.
  - NOTAS:
  - Asi es como en la clinica aparece un requisito RF-07 que promete recordatorio de cita por mensajeria, un diagrama de casos de uso donde no existe ningun caso de uso de recordatorio, y un diagrama de clases donde no hay nada parecido a una clase Notificacion.
  - Un defecto de consistencia cuesta poco corregirlo hoy, en una hoja, y cuesta carisimo corregirlo cuando ya se construyo sobre el, porque para entonces hay pantallas, tablas y codigo apoyados en la contradiccion.
  - Por eso esta sesion no agrega tema nuevo: agrega confianza en lo que ya existe, que es un trabajo de arquitecto tan legitimo como dibujar.

**[Slide 5] Requisitos huérfanos y elementos viudos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La herramienta central para eso es la trazabilidad, y se verifica en dos direcciones.
  - Hacia adelante se pregunta si todo requisito funcional llega a algun caso de uso y si ese caso de uso llega a alguna clase, atributo u operacion que lo soporte
  - Si un RF no llega a nada, es un requisito huerfano y significa que el equipo prometio algo que el diseño no cumple.
  - Hacia atras se pregunta si todo elemento del diseño nace de algun requisito
  - Si un caso de uso o una clase no viene de ningun RF, es un elemento viudo y casi siempre significa que alguien agrego funcionalidad por gusto propio o que la fila de la matriz quedo sin diligenciar.
  - En la clinica esto se vuelve concreto rapidisimo: RF-05, consultar el expediente de una mascota, junto con el RNF-02 que exige que el resultado aparezca en menos de tres segundos
  - Debe llegar a CU-02 Buscar expediente y de ahi a las clases Mascota y Consulta, con una operacion de busqueda por codigo o por nombre
  - Si ese camino se rompe en cualquier punto, el problema numero dos de la clinica sigue sin resolverse aunque el equipo tenga veinte paginas escritas.
  - La matriz de trazabilidad es apenas una tabla de cuatro columnas, pero es la unica prueba objetiva de que el paquete es coherente.

**[Slide 6] Auditoria cruzada: la matriz que delata contradicciones** — 14 vinetas.

**[Slide 7] El glosario canónico** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El segundo eje de la auditoria es el lenguaje.
  - Cuando en un documento se lee Dueño, en otro Propietario, en otro Cliente y en el mockup Responsable, no hay cuatro sinonimos: hay cuatro oportunidades de que alguien crea que son cuatro cosas distintas y termine con cuatro tablas.
  - La solucion es un glosario canonico donde cada concepto del dominio tiene un nombre unico, una definicion de una linea y una lista explicita de sinonimos prohibidos.
  - Ese glosario manda sobre todos los artefactos: si el nombre canonico es Propietario, entonces el requisito, el caso de uso, el mockup, el diccionario de datos y la clase se llaman Propietario, sin excepciones y sin diminutivos.
  - El glosario tambien separa parejas peligrosas: en la clinica, Cita es la reserva de un horario futuro y Consulta es el registro de una atencion ya realizada, y confundirlas produce un modelo donde nadie sabe si se esta agendando o atendiendo.
  - La ganancia es inmediata para el compañero que solo cursa Programacion II, porque puede buscar una palabra en el documento y encontrarla en todos lados; y tambien para el que solo cursa Seminario
  - Porque su documento de diseño se lee como un texto y no como un rompecabezas.
  - NOTAS:
  - Un sistema se diseña bien cuando existe un solo nombre para cada concepto y todos lo usan, desde la entrevista con la clinica hasta el nombre de la clase.

**[Slide 8] El glosario de nombres canonicos: el hueco mas comun** — 11 vinetas.

**[Slide 9] Revisión entre pares con reglas** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La revision entre pares se hace con reglas o no sirve.
  - Se revisa el artefacto, nunca a la persona, y para eso se asignan tres roles: el autor, que entrega su paquete y permanece en silencio mientras lo revisan; el revisor
  - Que recorre la lista de verificacion punto por punto y solo reporta hechos observables; y el moderador, que controla el tiempo y escribe los hallazgos.
  - Cada hallazgo se anota con ubicacion exacta, descripcion de la inconsistencia y severidad: bloqueante cuando impide construir el sistema, mayor cuando obliga a rehacer un artefacto completo, menor cuando es cosmetico.
  - Prohibido discutir la solucion durante la revision, porque ahi es donde se van los cuarenta minutos y no se revisa nada.
  - En la clinica, un hallazgo bien escrito se ve asi: en el diagrama de clases, la clase Consulta no tiene relacion con Veterinario, pero el flujo principal de CU-03 dice que toda consulta queda a nombre del veterinario que atendio; severidad mayor.
  - En cambio esta mal hecho, no me gusta o le falta orden no es un hallazgo, es una opinion.
  - NOTAS:
  - Eso es util.

**[Slide 10] Del hallazgo al backlog de deuda de diseño** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Cada hallazgo pasa a ser un item con responsable, severidad, criterio de cierre verificable y un estado que puede ser aceptado, rechazado con justificacion escrita o aplazado por acuerdo.
  - Rechazar un hallazgo es legitimo si se argumenta, y aprender a hacerlo es parte del oficio del analista.
  - Sobre ese backlog se define lo que en la industria se llama definicion de terminado del paquete de diseño de la clinica: catalogo de RF y RNF numerado y sin huerfanos
  - Diagrama y especificaciones de casos de uso, diagrama de clases con multiplicidades, mockups de las pantallas criticas y diccionario de datos.
  - Aqui se hacen visibles los tres casos de matricula: el que cursa las dos materias entrega estos planos aca y el codigo alla; el que solo cursa Programacion II recibe este paquete y todo lo que hoy quede ambiguo lo va a pagar en horas de reproceso
  - Y el que solo cursa Seminario cierra con este mismo documento mas el prototipo navegable, que es una ruta completa y valida, no una version reducida del curso.
  - NOTAS:
  - Todo lo que se encuentra se convierte en backlog de deuda de diseño, no en angustia.


**Demo que usted debe poder repetir:** El docente proyecta el paquete de un equipo ficticio de VetCare y encuentra en vivo tres inconsistencias: un RF sin caso de uso, una clase llamada Dueño que en el catalogo de requisitos se llama Propietario, y un caso de uso que ninguna clase puede soportar.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Avance del proyecto integrador. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta el paquete de un equipo ficticio de VetCare y encuentra en vivo tres inconsistencias: un RF sin caso de uso, una clase llamada Dueño que en el catalogo de requisitos se llama Propietario, y un caso de uso que ninguna clase puede soportar.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 11/Plantillas/Auditoria-Cruzada-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 11 - Avance del proyecto de diseno/Taller PI - Clase 11 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Construir en Google Docs la matriz de trazabilidad de VetCare con las columnas RF, Caso de uso, Clase o clases implicadas y Mockup, incluyendo todos los requisitos del catalogo, y marcar en rojo cada fila incompleta.
2. Levantar el glosario de nombres canonicos con minimo ocho conceptos del dominio (Propietario, Mascota, Consulta, Cita, Veterinario, Vacuna, Expediente, Bitacora), cada uno con definicion de una linea y sinonimos prohibidos, y renombrar en los artefactos todo lo que no coincida.
3. Intercambiar el paquete completo con otro estudiante (o con otro equipo, si el docente autorizo trabajo en equipo) y aplicar la rubrica de auditoria de seis puntos durante veinte minutos cronometrados, registrando cada hallazgo con ubicacion exacta, descripcion y severidad bloqueante, mayor o menor; queda prohibido proponer soluciones durante la revision.
4. Recibir los hallazgos propios y clasificarlos en aceptado, rechazado con justificacion escrita o aplazado por acuerdo, sin borrar ninguno del acta, de modo que quede evidencia de la decision tomada.
5. Armar el backlog priorizado de correcciones con responsable y criterio de cierre verificable para cada item, ordenado por severidad, y aplicar en clase al menos las dos correcciones bloqueantes antes de subir el paquete corregido a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento con la matriz de trazabilidad RF a CU a Clase, el glosario de nombres canonicos, el acta de revision entre pares con hallazgos clasificados por severidad y el backlog priorizado de correcciones, subido a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx` — no proyectar completa.
