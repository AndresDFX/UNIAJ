# Guion docente · Clase 2 · Ciclos de vida del software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.
- **Entregable de hoy:** Un documento de una pagina en Google Docs con la tabla Fase / Pregunta que responde / Artefacto de VetCare / Quien lo aprueba, mas dos diagramas en draw.io (recorrido lineal y recorrido en tres vueltas) exportados a PDF y subidos a ExamLab.
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 2 - Ciclos de vida del software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un ciclo de vida del software es el orden en que se recorren las etapas...** — 3 vinetas.
  - Lo importante no es memorizar los nombres sino entender que cada fase tiene tres cosas: una entrada (lo que recibe de la fase anterior), una salida tangible llamada artefacto (un documento, un diagrama, un programa) y un criterio para decir 'esto ya quedo'.
  - Si una fase no produce un artefacto verificable, esa fase no existe, existe una conversacion.

**Vale la pena decir con precision que produce cada fase, porque ahi se...** — 3 vinetas.
  - Vale la pena decir con precision que produce cada fase, porque ahi se cae la mitad de los equipos.
  - Diseño responde COMO se va a lograr y produce casos de uso, diagramas de clases, modelo de datos, wireframes y mockups.
  - Pruebas verifica que lo construido corresponde a lo pedido y produce casos de prueba y evidencias.
  - Mantenimiento arregla, ajusta y evoluciona el sistema ya en uso.
  - Por eso aqui nunca se califica codigo: se califica que los planos esten completos, coherentes y sean construibles.

**La gran decision no es cuales fases hacer, sino cuantas veces...** — 4 vinetas.
  - Recorrerlas una sola vez y en orden significa cerrar requisitos de TODO VetCare, luego diseñar TODO VetCare, luego construir TODO.
  - Recorrerlas en ciclos significa tomar un pedazo util del sistema y pasarlo por las cinco fases en una vuelta corta, y despues repetir con el siguiente pedazo.

**Hay que separar dos palabras que los equipos usan como sinonimos y no... (1/2)** — 5 vinetas.

**Hay que separar dos palabras que los equipos usan como sinonimos y no... (2/2)** — 2 vinetas.

**Como se elige el recorrido? (1/2)** — 3 vinetas.
  - Como se elige el recorrido?
  - Con criterios, no con moda.

**Como se elige el recorrido? (2/2)** — 2 vinetas.

**El recorrido lineal del ciclo de vida** — 6 vinetas.

**El mismo ciclo en tres vueltas** — 15 vinetas.


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
