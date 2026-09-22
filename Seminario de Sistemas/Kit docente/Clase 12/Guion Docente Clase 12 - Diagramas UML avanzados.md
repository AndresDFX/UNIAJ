# Guion docente · Clase 12 · Diagramas UML avanzados

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda modelada la dinamica de VetCare: el diagrama de secuencia del caso de uso Agendar cita y el diagrama de actividad del proceso de atencion en el consultorio.
- **Entregable de hoy:** Un PDF con el diagrama de secuencia de Agendar cita incluyendo el fragmento alt para horario ocupado, el diagrama de actividad del proceso de atencion con calles por rol, y la tabla que mapea cada mensaje del diagrama de secuencia a una operacion del diagrama de clases, subido a ExamLab.
- **Herramienta:** draw.io · Mermaid Live Editor
- **Slides:** `Clases/Clase 12 - Diagramas UML avanzados/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Hasta ahora todos los modelos de VetCare han sido estaticos: el... (1/2)** — 4 vinetas.

**Hasta ahora todos los modelos de VetCare han sido estaticos: el... (2/2)** — 3 vinetas.

**El diagrama de actividad responde a otra pregunta completamente... (1/2)** — 3 vinetas.

**El diagrama de actividad responde a otra pregunta completamente... (2/2)** — 4 vinetas.

**La pregunta practica es cuando usar cada uno, y la respuesta se decide...** — 7 vinetas.

**Estos diagramas no se inventan desde cero: se derivan de lo que ya esta...** — 7 vinetas.

**Los flujos alternos tambien se modelan, y para eso existen los...** — 7 vinetas.


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
