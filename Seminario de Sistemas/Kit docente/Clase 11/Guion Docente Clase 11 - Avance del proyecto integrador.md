# Guion docente · Clase 11 · Avance del proyecto integrador

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.
- **Entregable de hoy:** Un documento con la matriz de trazabilidad RF a CU a Clase, el glosario de nombres canonicos, el acta de revision entre pares con hallazgos clasificados por severidad y el backlog priorizado de correcciones, subido a ExamLab.
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 11 - Avance del proyecto integrador/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un paquete de diseño no es una carpeta de archivos sueltos: es un sistema de documentos que deben decir lo mismo con las mismas palabras. El problema es que esos documentos se escribieron en semanas distintas, muchas veces por personas distintas del equipo, y cada semana el entendimiento del dominio cambio un poquito. Asi es como en VetCare aparece un requisito RF-07 que promete recordatorio de cita por mensajeria, un diagrama de casos de uso donde no existe ningun caso de uso de recordatorio, y un diagrama de clases donde no hay nada parecido a una clase Notificacion. Ninguno de los tres documentos esta mal por si solo; lo que esta mal es el conjunto. Un defecto de consistencia cuesta poco corregirlo hoy, en una hoja, y cuesta carisimo corregirlo cuando ya se construyo sobre el, porque para entonces hay pantallas, tablas y codigo apoyados en la contradiccion. Por eso esta sesion no agrega tema nuevo: agrega confianza en lo que ya existe, que es un trabajo de arquitecto tan legitimo como dibujar.

La herramienta central para eso es la trazabilidad, y se verifica en dos direcciones. Hacia adelante se pregunta si todo requisito funcional llega a algun caso de uso y si ese caso de uso llega a alguna clase, atributo u operacion que lo soporte; si un RF no llega a nada, es un requisito huerfano y significa que el equipo prometio algo que el diseño no cumple. Hacia atras se pregunta si todo elemento del diseño nace de algun requisito; si un caso de uso o una clase no viene de ningun RF, es un elemento viudo y casi siempre significa que alguien agrego funcionalidad por gusto propio o que la fila de la matriz quedo sin diligenciar. En VetCare esto se vuelve concreto rapidisimo: RF-05, consultar el expediente de una mascota, junto con el RNF-02 que exige que el resultado aparezca en menos de tres segundos, debe llegar a CU-02 Buscar expediente y de ahi a las clases Mascota y Consulta, con una operacion de busqueda por codigo o por nombre; si ese camino se rompe en cualquier punto, el problema numero dos de la clinica Huellitas sigue sin resolverse aunque el equipo tenga veinte paginas escritas. La matriz de trazabilidad es apenas una tabla de cuatro columnas, pero es la unica prueba objetiva de que el paquete es coherente.

El segundo eje de la auditoria es el lenguaje. Un sistema se diseña bien cuando existe un solo nombre para cada concepto y todos lo usan, desde la entrevista con la clinica hasta el nombre de la clase. Cuando en un documento se lee Dueño, en otro Propietario, en otro Cliente y en el mockup Responsable, no hay cuatro sinonimos: hay cuatro oportunidades de que alguien crea que son cuatro cosas distintas y termine con cuatro tablas. La solucion es un glosario canonico donde cada concepto de VetCare tiene un nombre unico, una definicion de una linea y una lista explicita de sinonimos prohibidos. Ese glosario manda sobre todos los artefactos: si el nombre canonico es Propietario, entonces el requisito, el caso de uso, el mockup, el diccionario de datos y la clase se llaman Propietario, sin excepciones y sin diminutivos. El glosario tambien separa parejas peligrosas: en Huellitas, Cita es la reserva de un horario futuro y Consulta es el registro de una atencion ya realizada, y confundirlas produce un modelo donde nadie sabe si se esta agendando o atendiendo. La ganancia es inmediata para el compañero que solo cursa Programacion II, porque puede buscar una palabra en el documento y encontrarla en todos lados; y tambien para el que solo cursa Seminario, porque su documento de diseño se lee como un texto y no como un rompecabezas.

La revision entre pares se hace con reglas o no sirve. Se revisa el artefacto, nunca a la persona, y para eso se asignan tres roles: el autor, que entrega su paquete y permanece en silencio mientras lo revisan; el revisor, que recorre la rubrica punto por punto y solo reporta hechos observables; y el moderador, que controla el tiempo y escribe los hallazgos. Cada hallazgo se anota con ubicacion exacta, descripcion de la inconsistencia y severidad: bloqueante cuando impide construir el sistema, mayor cuando obliga a rehacer un artefacto completo, menor cuando es cosmetico. Prohibido discutir la solucion durante la revision, porque ahi es donde se van los cuarenta minutos y no se revisa nada. En VetCare, un hallazgo bien escrito se ve asi: en el diagrama de clases, la clase Consulta no tiene relacion con Veterinario, pero el flujo principal de CU-03 dice que toda consulta queda a nombre del veterinario que atendio; severidad mayor. Eso es util. En cambio esta mal hecho, no me gusta o le falta orden no es un hallazgo, es una opinion.

Todo lo que se encuentra se convierte en backlog de deuda de diseño, no en angustia. Cada hallazgo pasa a ser un item con responsable, severidad, criterio de cierre verificable y un estado que puede ser aceptado, rechazado con justificacion escrita o aplazado por acuerdo. Rechazar un hallazgo es legitimo si se argumenta, y aprender a hacerlo es parte del oficio del analista. Sobre ese backlog se define lo que en la industria se llama definicion de terminado del paquete de diseño de VetCare: catalogo de RF y RNF numerado y sin huerfanos, diagrama y especificaciones de casos de uso, diagrama de clases con multiplicidades, mockups de las pantallas criticas y diccionario de datos. Aqui es donde los tres casos de matricula se hacen visibles y conviene decirlo en voz alta en el aula: el que cursa las dos materias entrega estos planos aca y el codigo alla; el que solo cursa Programacion II recibe este paquete y todo lo que hoy quede ambiguo lo va a pagar en horas de reproceso; y el que solo cursa Seminario cierra con este mismo documento mas el prototipo navegable, que es una ruta completa y valida, no una version reducida del curso.

Error tipico del docente que no domina el tema: usar la sesion de avance como una hora libre para que los equipos adelanten lo que les falta, sin producto propio y sin evidencia. Cuando eso pasa, la clase se convierte en un salon de gente escribiendo en silencio y el docente pasando por los puestos preguntando como van, que es exactamente lo que no se debe hacer, porque el checkpoint tambien tiene entregable. El segundo error es pedir a los equipos que se revisen entre si sin rubrica: sin criterios escritos, la revision se vuelve un intercambio de cortesias donde todos dicen que el trabajo del otro esta muy bien y nadie encuentra nada. El tercero es confundir consistencia con completitud y celebrar que el paquete este completo cuando en realidad esta completo pero se contradice: veinte requisitos, ocho casos de uso, quince clases y ninguna trazabilidad entre ellos. Y el cuarto, el mas silencioso, es no exigir que los hallazgos queden por escrito con severidad y responsable; si los hallazgos se dicen de palabra, en la siguiente sesion nadie recuerda ninguno y la auditoria no cambia nada del proyecto.

**Demo que usted debe poder repetir:** El docente proyecta el paquete de un equipo ficticio de VetCare y encuentra en vivo tres inconsistencias: un RF sin caso de uso, una clase llamada Dueño que en el catalogo de requisitos se llama Propietario, y un caso de uso que ninguna clase puede soportar.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta el paquete de un equipo ficticio de VetCare y encuentra en vivo tres inconsistencias: un RF sin caso de uso, una clase llamada Dueño que en el catalogo de requisitos se llama Propietario, y un caso de uso que ninguna clase puede soportar.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 11/Plantillas/Auditoria-Cruzada-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Construir en Google Docs la matriz de trazabilidad de VetCare con las columnas RF, Caso de uso, Clase o clases implicadas y Mockup, incluyendo todos los requisitos del catalogo, y marcar en rojo cada fila incompleta.
2. Levantar el glosario de nombres canonicos con minimo ocho conceptos del dominio (Propietario, Mascota, Consulta, Cita, Veterinario, Vacuna, Expediente, Bitacora), cada uno con definicion de una linea y sinonimos prohibidos, y renombrar en los artefactos todo lo que no coincida.
3. Intercambiar el paquete completo con otro estudiante (o con otro equipo, si el docente autorizo trabajo en equipo) y aplicar la rubrica de auditoria de seis puntos durante veinte minutos cronometrados, registrando cada hallazgo con ubicacion exacta, descripcion y severidad bloqueante, mayor o menor; queda prohibido proponer soluciones durante la revision.
4. Recibir los hallazgos propios y clasificarlos en aceptado, rechazado con justificacion escrita o aplazado por acuerdo, sin borrar ninguno del acta, de modo que quede evidencia de la decision tomada.
5. Armar el backlog priorizado de correcciones con responsable y criterio de cierre verificable para cada item, ordenado por severidad, y aplicar en clase al menos las dos correcciones bloqueantes antes de subir el paquete corregido a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento con la matriz de trazabilidad RF a CU a Clase, el glosario de nombres canonicos, el acta de revision entre pares con hallazgos clasificados por severidad y el backlog priorizado de correcciones, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx` — no proyectar completa.
