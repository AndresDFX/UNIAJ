# Guion docente · Clase 11 · Revisión de código cruzada

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.
- **Entregable de hoy:** Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 11 - Revision de codigo cruzada/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Una revisión de código es la lectura sistemática del código de otra...** — 7 vinetas.
  - Conviene decirlo claro porque el estudiante llega con dos ideas equivocadas: que la revisión es un examen donde lo van a rajar, o que es un trámite para poner 'todo bien' y salir rápido.

**Revisar no es leer de arriba a abajo a ver qué salta: se revisa por... (1/2)** — 6 vinetas.

**Revisar no es leer de arriba a abajo a ver qué salta: se revisa por... (2/2)** — 4 vinetas.

**La retroalimentación útil tiene una estructura, y esa estructura se... (1/2)** — 8 vinetas.

**La retroalimentación útil tiene una estructura, y esa estructura se... (2/2)** — 3 vinetas.

**El checklist es lo que impide que la revisión se vuelva una... (1/2)** — 6 vinetas.

**El checklist es lo que impide que la revisión se vuelva una... (2/2)** — 6 vinetas.

**Recibir la crítica también se practica, y es la mitad difícil** — 7 vinetas.


**Demo que usted debe poder repetir:** El docente proyecta VetCareParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta VetCareParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 11/Codigo/VetCareParaRevisar.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Intercambien proyectos: cada estudiante entrega su carpeta comprimida más un archivo de tres líneas con las instrucciones de ejecución, y recibe el proyecto de otro compañero (si el docente autorizó equipos, el de otro equipo; la revisión funciona igual); lo primero es abrirlo en VS Code y ejecutarlo, anotando si arrancó y, si no, el mensaje de error exacto copiado tal cual.
2. Recorran el proyecto recibido con el checklist de doce ítems (clase de dominio, encapsulamiento, colección, interfaz gráfica, try-catch en fronteras, persistencia, catch vacío, métodos largos, duplicación, nombres, números mágicos, validación de casos borde) marcando cumple / no cumple / no aplica y escribiendo la evidencia archivo:línea en cada 'no cumple'.
3. Provoquen a propósito los cuatro casos borde de VetCare (edad con letras, campos vacíos, buscar un ID inexistente, borrar o dañar una línea de mascotas.csv) y registren qué hizo la aplicación en cada uno, con el texto del mensaje o de la excepción.
4. Redacten cinco hallazgos priorizados como bloqueante, mayor o menor, cada uno con el formato Evidencia + Impacto + Sugerencia, todos referidos al código y ninguno a la persona; incluyan al menos un bloqueante si existe.
5. Hagan la devolución cruzada de ocho minutos por proyecto revisado y cierren con el plan de corrección escrito por su autor: qué acepta y corrige, qué justifica y deja igual, y qué difiere, con responsable en cada línea.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx` — no proyectar completa.
