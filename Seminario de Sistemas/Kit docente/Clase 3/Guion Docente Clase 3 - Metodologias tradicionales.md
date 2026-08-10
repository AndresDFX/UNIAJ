# Guion docente · Clase 3 · Metodologias tradicionales

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar.
- **Entregable de hoy:** Un documento en Google Docs con el indice del ERS de VetCare, cuatro requisitos escritos en formato de ficha con version y linea base, la matriz en V (requisito - nivel de prueba - criterio de aceptacion) y un formato de solicitud de cambio diligenciado; mas el diagrama en V dibujado en draw.io y subido a ExamLab.
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 3 - Metodologias tradicionales/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

El modelo en cascada es el recorrido lineal llevado a su version formal: las fases van una detras de otra y cada una termina con un documento que alguien firma. Ese documento es la puerta de entrada a la siguiente fase; si no esta aprobado, no se avanza. Cuando el documento de requisitos se aprueba, se convierte en linea base, es decir, la version oficial contra la cual se va a medir todo lo demas. La idea de fondo es sencilla y muy usada en ingenieria civil: corregir un plano cuesta una borrada, corregir un muro construido cuesta demoler. Trasladado a VetCare: si Huellitas aprueba que la busqueda se hace por nombre de la mascota y por documento del propietario, ese acuerdo queda escrito, fechado y versionado, y a partir de ahi el equipo diseña con la tranquilidad de que el piso no se le va a mover.

El modelo en V toma la cascada y la dobla en forma de letra V para dejar visible algo que la cascada esconde: cada fase de la izquierda tiene su prueba correspondiente a la derecha. Los requisitos se emparejan con las pruebas de aceptacion, el diseño de la arquitectura con las pruebas de integracion y el diseño detallado con las pruebas unitarias. La consecuencia practica es enorme: la prueba se diseña al mismo tiempo que el requisito, no al final. En VetCare, cuando se escribe el requisito RF-03 'la veterinaria busca la historia clinica por nombre o por documento', en ese mismo momento se escribe el caso de prueba CP-ACEP-07: con 5.000 fichas cargadas, escribir Rocky y obtener la ficha en menos de tres segundos y en maximo tres clics. Aqui aparecen dos palabras que hay que distinguir: verificar es preguntarse si construimos el sistema correctamente segun el documento; validar es preguntarse si construimos el sistema correcto para la clinica.

Cuando SI tienen sentido estos modelos? Cuando los requisitos son estables y se conocen desde el principio, cuando el contrato es a precio fijo o viene de una licitacion publica y el alcance debe estar cerrado para poder cotizar, cuando el sistema es critico o esta regulado (equipos medicos, aviacion, banca, manejo de historia clinica con normativa de proteccion de datos) y cuando hay varios proveedores que necesitan un documento comun para poder trabajar en paralelo. En VetCare hay partes que caben perfecto en este enfoque: los datos basicos de un paciente casi no cambian, y si mañana la clinica conecta facturacion electronica, las reglas de esa parte vienen impuestas por la norma y no se negocian con el cliente. En esos casos escribir todo el detalle antes no es burocracia, es la unica forma de estimar y de cumplir.

Cuando NO tienen sentido? Cuando el cliente no sabe lo que quiere hasta que lo ve, cuando el dominio es nuevo para el equipo, cuando el tiempo hasta la primera entrega visible es tan largo que el negocio cambia antes de recibir nada, y cuando integrar todo de un solo golpe al final concentra el riesgo en el peor momento. El costo de corregir crece de forma brutal a medida que se avanza: cambiar una frase en el documento de requisitos vale casi nada; cambiar la misma idea cuando ya hay diseño, codigo y datos migrados puede costar semanas. En VetCare esto se ve clarito con el tablero de metricas: la administradora dice 'quiero ver cuantos pacientes atendemos', pero cuando vea el primer grafico va a pedir por especie, por veterinario y por mes. Congelar ese requisito en la semana dos es congelar una suposicion.

En el mundo tradicional la documentacion no acompaña al producto: en buena parte ES el producto contratado. Los entregables tipicos son la Especificacion de Requisitos de Software (ERS o SRS, con estructura tipo IEEE 830 / ISO 29148), el Documento de Diseño (SDD), la matriz de trazabilidad que muestra que cada requisito tiene diseño y prueba, y el acta de aprobacion. Cada documento tiene numero de version, fecha, autor y aprobador, y todo cambio entra por una solicitud formal donde se evalua impacto en alcance, tiempo y costo antes de aceptarla. Para el estudiante que solo cursa Seminario de Sistemas esto es una gran noticia: su entregable final -documento de diseño mas prototipo navegable- es exactamente el tipo de producto que se factura en un proyecto tradicional, y por eso su ruta es completa y no una version reducida del curso.

Error tipico del docente que no domina el tema: presentar la cascada como un modelo torpe inventado por gente que no sabia trabajar, y de paso repetir que 'Royce la propuso' cuando en realidad el articulo de 1970 la describia y advertia sus riesgos. El segundo error es decir que el modelo en V es 'la cascada con un dibujito mas bonito': lo que agrega es la planeacion de las pruebas desde el inicio y la trazabilidad requisito-prueba, que es justamente lo que salva proyectos. El tercero, el mas costoso en el aula, es enseñar que congelar requisitos significa que ya no se admiten cambios: los cambios siempre llegan; lo que hace el enfoque tradicional es obligarlos a pasar por un control de cambios donde se dice cuanto cuestan y cuanto atrasan, en vez de aceptarlos de palabra en un pasillo.

**Demo que usted debe poder repetir:** El docente dibuja en draw.io el modelo en V de VetCare y traza en vivo la linea punteada que conecta el requisito RF-03 'buscar historial' con su prueba de aceptacion CP-ACEP-07.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente dibuja en draw.io el modelo en V de VetCare y traza en vivo la linea punteada que conecta el requisito RF-03 'buscar historial' con su prueba de aceptacion CP-ACEP-07.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 3/Plantillas/ERS-y-Matriz-en-V-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. En Google Docs escriba el indice del ERS de VetCare con al menos estas secciones numeradas: 1. Proposito y alcance, 2. Glosario del dominio veterinario, 3. Requisitos funcionales, 4. Requisitos no funcionales, 5. Reglas de negocio, 6. Matriz de trazabilidad, 7. Control de versiones y aprobaciones.
2. Escriba cuatro requisitos de VetCare en formato de ficha completa (ID, nombre, fuente, prioridad, estabilidad, descripcion, precondicion, criterio de aceptacion, version y estado); al menos uno debe ser no funcional y al menos uno debe declarar dependencia de otro.
3. Construya la matriz en V en una tabla de cuatro columnas: Fase de la izquierda / Artefacto / Nivel de prueba emparejado / Caso de prueba de VetCare que lo verifica, y asegurese de que cada uno de sus cuatro requisitos aparezca con su codigo de prueba.
4. En draw.io dibuje el modelo en V de VetCare con las fases de bajada y de subida, y trace lineas punteadas horizontales que unan cada fase con su nivel de prueba; rotule al menos dos de esas lineas con el ID del requisito y el ID del caso de prueba.
5. Diligencie el formato de solicitud de cambio con este caso real: la clinica pide, ya aprobada la linea base, que la busqueda tambien funcione por numero de microchip; describa el requisito afectado, el impacto en diseño y pruebas, y la decision (aprobar, aplazar o rechazar) con su justificacion. Exporte todo a PDF y suba a ExamLab.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un documento en Google Docs con el indice del ERS de VetCare, cuatro requisitos escritos en formato de ficha con version y linea base, la matriz en V (requisito - nivel de prueba - criterio de aceptacion) y un formato de solicitud de cambio diligenciado; mas el diagrama en V dibujado en draw.io y subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - VetCare.docx` — no proyectar completa.
