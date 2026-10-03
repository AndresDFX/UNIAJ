# Guion docente · Clase 3 · Metodologias tradicionales

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar.
- **Practica (opcional):** `Clases/Clase 3 - Metodologias tradicionales/Taller PI - Clase 3 - VetCare.docx` — no esta en el deck
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 3 - Metodologias tradicionales/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**El modelo en cascada es el recorrido lineal llevado a su version... (1/2)** — 4 vinetas.

**El modelo en cascada es el recorrido lineal llevado a su version... (2/2)** — 2 vinetas.

**El modelo en V toma la cascada y la dobla en forma de letra V para...** — 5 vinetas.
  - Los requisitos se emparejan con las pruebas de aceptacion, el diseño de la arquitectura con las pruebas de integracion y el diseño detallado con las pruebas unitarias.

**Cuando SI tienen sentido estos modelos?** — 5 vinetas.
  - Cuando SI tienen sentido estos modelos?

**Cuando NO tienen sentido? (1/2)** — 3 vinetas.
  - Cuando NO tienen sentido?

**Cuando NO tienen sentido? (2/2)** — 2 vinetas.

**En el mundo tradicional la documentacion no acompaña al producto: en...** — 3 vinetas.
  - Cada documento tiene numero de version, fecha, autor y aprobador, y todo cambio entra por una solicitud formal donde se evalua impacto en alcance, tiempo y costo antes de aceptarla.

**El modelo en V con trazabilidad** — 17 vinetas.

**La solicitud de cambio sobre linea base** — 14 vinetas.


**Demo que usted debe poder repetir:** El docente dibuja en draw.io el modelo en V de VetCare y traza en vivo la linea punteada que conecta el requisito RF-03 'buscar historial' con su prueba de aceptacion CP-ACEP-07.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Metodologias tradicionales. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente dibuja en draw.io el modelo en V de VetCare y traza en vivo la linea punteada que conecta el requisito RF-03 'buscar historial' con su prueba de aceptacion CP-ACEP-07.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 3/Plantillas/ERS-y-Matriz-en-V-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 3 - Metodologias tradicionales/Taller PI - Clase 3 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. En Google Docs escriba el indice del ERS de VetCare con al menos estas secciones numeradas: 1. Proposito y alcance, 2. Glosario del dominio veterinario, 3. Requisitos funcionales, 4. Requisitos no funcionales, 5. Reglas de negocio, 6. Matriz de trazabilidad, 7. Control de versiones y aprobaciones.
2. Escriba cuatro requisitos de VetCare en formato de ficha completa (ID, nombre, fuente, prioridad, estabilidad, descripcion, precondicion, criterio de aceptacion, version y estado); al menos uno debe ser no funcional y al menos uno debe declarar dependencia de otro.
3. Construya la matriz en V en una tabla de cuatro columnas: Fase de la izquierda / Artefacto / Nivel de prueba emparejado / Caso de prueba de VetCare que lo verifica, y asegurese de que cada uno de sus cuatro requisitos aparezca con su codigo de prueba.
4. En draw.io dibuje el modelo en V de VetCare con las fases de bajada y de subida, y trace lineas punteadas horizontales que unan cada fase con su nivel de prueba; rotule al menos dos de esas lineas con el ID del requisito y el ID del caso de prueba.
5. Diligencie el formato de solicitud de cambio con este caso real: la clinica pide, ya aprobada la linea base, que la busqueda tambien funcione por numero de microchip; describa el requisito afectado, el impacto en diseño y pruebas, y la decision (aprobar, aplazar o rechazar) con su justificacion. Exporte todo a PDF y suba a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento en Google Docs con el indice del ERS de VetCare, cuatro requisitos escritos en formato de ficha con version y linea base, la matriz en V (requisito - nivel de prueba - criterio de aceptacion) y un formato de solicitud de cambio diligenciado; mas el diagrama en V dibujado en draw.io y subido a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx` — no proyectar completa.
