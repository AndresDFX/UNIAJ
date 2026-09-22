# Guion docente · Clase 6 · Requerimientos de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.
- **Entregable de hoy:** Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 6 - Requerimientos de software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un requerimiento no es lo que el cliente dijo, es lo que el sistema... (1/2)** — 4 vinetas.

**Un requerimiento no es lo que el cliente dijo, es lo que el sistema... (2/2)** — 3 vinetas.

**Con las necesidades en la mano se separan dos familias (1/2)** — 3 vinetas.
  - Con las necesidades en la mano se separan dos familias.
  - Esa separacion importa porque el RF se prueba haciendo clic y el RNF se prueba midiendo o intentando lo prohibido.

**Con las necesidades en la mano se separan dos familias (2/2)** — 2 vinetas.

**La regla de oro del oficio es dura y se enuncia asi: si no se puede... (1/2)** — 5 vinetas.

**La regla de oro del oficio es dura y se enuncia asi: si no se puede... (2/2)** — 2 vinetas.

**Priorizar no es ordenar por gusto sino decidir con el cliente que pasa... (1/2)** — 4 vinetas.

**Priorizar no es ordenar por gusto sino decidir con el cliente que pasa... (2/2)** — 3 vinetas.

**El ultimo pedazo es la trazabilidad, que es poder seguir cada requisito...** — 4 vinetas.
  - Se lleva en una matriz simple de cuatro columnas y se actualiza cada clase.
  - Esto no es burocracia: es lo que permite que cuando el cliente cambie de opinion, usted sepa en dos minutos que se rompe y cuanto cuesta; y en el Proyecto Integrador es lo que hace posible que el companero que solo cursa Programacion II reciba estos planos y sepa exactamente que implementar y por que, sin tener que volver a entrevistar al veterinario.


**Demo que usted debe poder repetir:** El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 6/Plantillas/RF-RNF-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: copie en la plantilla las cinco frases crudas de la entrevista al Dr. Ramirez y marque cada una como NECESIDAD, anotando al lado quien la dijo y en que contexto; esa columna es el origen y no se puede dejar vacia.
2. Paso 2: traduzca las necesidades a requisitos funcionales usando la plantilla el sistema debe permitir a <actor> <accion> <objeto>, hasta llegar a minimo 8 RF numerados de RF-01 a RF-08; ningun RF puede contener la palabra y uniendo dos capacidades distintas.
3. Paso 3: derive 4 RNF, uno por categoria (desempeno, control de acceso, usabilidad y respaldo), y escriba en cada uno al menos un numero: segundos, cantidad de registros, frecuencia o porcentaje.
4. Paso 4: asigne prioridad MoSCoW a los 12 requisitos, verifique que los Must no pasen de seis y justifique en una linea por que los dos Won't quedan fuera de esta version de VetCare.
5. Paso 5: complete la matriz de trazabilidad con las columnas Necesidad, RF/RNF, Pantalla prevista y Prueba de aceptacion, exporte el documento a PDF y subalo a ExamLab con el nombre RF-RNF-VetCare-<sus apellidos>.pdf.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx` — no proyectar completa.
