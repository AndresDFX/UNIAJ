# Guion docente · Clase 11 · Avance del proyecto integrador

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.
- **Entregable de hoy:** Un documento con la matriz de trazabilidad RF a CU a Clase, el glosario de nombres canonicos, el acta de revision entre pares con hallazgos clasificados por severidad y el backlog priorizado de correcciones, subido a ExamLab.
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 11 - Avance del proyecto integrador/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un paquete de diseño no es una carpeta de archivos sueltos: es un...** — 3 vinetas.
  - Asi es como en VetCare aparece un requisito RF-07 que promete recordatorio de cita por mensajeria, un diagrama de casos de uso donde no existe ningun caso de uso de recordatorio, y un diagrama de clases donde no hay nada parecido a una clase Notificacion.
  - Un defecto de consistencia cuesta poco corregirlo hoy, en una hoja, y cuesta carisimo corregirlo cuando ya se construyo sobre el, porque para entonces hay pantallas, tablas y codigo apoyados en la contradiccion.
  - Por eso esta sesion no agrega tema nuevo: agrega confianza en lo que ya existe, que es un trabajo de arquitecto tan legitimo como dibujar.

**La herramienta central para eso es la trazabilidad, y se verifica en... (1/2)** — 5 vinetas.

**La herramienta central para eso es la trazabilidad, y se verifica en... (2/2)** — 4 vinetas.

**El segundo eje de la auditoria es el lenguaje (1/2)** — 4 vinetas.
  - Un sistema se diseña bien cuando existe un solo nombre para cada concepto y todos lo usan, desde la entrevista con la clinica hasta el nombre de la clase.

**El segundo eje de la auditoria es el lenguaje (2/2)** — 3 vinetas.

**La revision entre pares se hace con reglas o no sirve (1/2)** — 4 vinetas.
  - Eso es util.

**La revision entre pares se hace con reglas o no sirve (2/2)** — 3 vinetas.

**Todo lo que se encuentra se convierte en backlog de deuda de diseño, no... (1/2)** — 4 vinetas.
  - Todo lo que se encuentra se convierte en backlog de deuda de diseño, no en angustia.

**Todo lo que se encuentra se convierte en backlog de deuda de diseño, no... (2/2)** — 3 vinetas.

**El glosario de nombres canonicos: el hueco mas comun** — 11 vinetas.


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
