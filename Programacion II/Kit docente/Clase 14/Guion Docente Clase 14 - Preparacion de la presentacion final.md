# Guion docente · Clase 14 · Preparacion de la presentacion final · Sustentacion de VetCare

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.
- **Entregable de hoy:** Guion de sustentacion con bloques, minutos y evidencia que se muestra (mas el responsable nominal solo si el docente autorizo equipo), mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 14 - Preparacion de la presentacion final/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Sustentar es demostrar** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 5] La sustentación es una coreografía** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Las transiciones entre bloques se dicen en voz alta, con una formula corta del tipo 'para mostrar como quedan guardados esos datos, abro de nuevo la aplicacion', porque los silencios incomodos al cambiar de tema son lo que mas se nota.
  - Subrayar: Un guion escrito, con minutos y evidencia por bloque (y el nombre del responsable si hay equipo), convierte una exposicion nerviosa en algo que se puede ensayar y medir; en VetCare ese guion tiene cinco bloques y suma siete minutos, con cuatro dedicados a la demo.

**[Slide 6] El guion de la sustentación en código** — programa completo (22 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] La demo blindada: el pre-vuelo** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La demo en vivo no falla por mala suerte, falla por falta de preparacion, y se blinda con un chequeo previo que llamaremos pre-vuelo.

**[Slide 8] sembrarDatosDemo(): datos creíbles** — programa completo (42 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] chequeoPreVuelo(): verde o no se presenta** — programa completo (50 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 10] Las preguntas del jurado** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.

**[Slide 11] Tiempo y nervios: el ensayo cronometrado** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Por eso hoy ensayamos con reloj y anotamos el tiempo real de cada bloque frente al planeado, y se repite hasta que el total caiga entre cinco y ocho minutos con margen.

**[Slide 12] ensayo(): planeado contra real** — programa completo (29 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: dejar la sustentacion para el ultimo dia, decir 'preparen una exposicion' y confiar en que el guion se arma solo. Eso produce demos improvisadas con la aplicacion vacia y proyectos que se ponen a compilar en vivo mientras el jurado espera. Otras variantes: no cronometrar nunca, permitir que el estudiante muestre codigo linea por linea en lugar de la aplicacion corriendo, y no exigir plan B, para despues perder media hora del examen porque el computador de alguien no encendio. Cuando el docente autoriza equipos aparece un problema extra: si nadie exige reparto escrito, tres personas se quedan mudas y la nota la sostiene un solo orador. La clase de hoy no tiene tema tecnico nuevo, pero tiene un producto verificable, y ese es el punto: si al final del bloque cada estudiante no tiene guion escrito, datos sembrados y dos ensayos cronometrados, la clase no se cumplio.


**Demo que usted debe poder repetir:** El docente sustenta VetCare en 6 minutos delante del grupo, provoca a proposito un error de edad para mostrar la validacion, y luego repite la misma demo con la lista vacia para que se vea el desastre de no sembrar datos.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente sustenta VetCare en 6 minutos delante del grupo, provoca a proposito un error de edad para mostrar la validacion, y luego repite la misma demo con la lista vacia para que se vea el desastre de no sembrar datos.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 14/Codigo/EnsayoSustentacionClinica.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 14 - Preparacion de la presentacion final/Taller PI - Clase 14 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Escriban el guion de la sustentacion en una tabla de cinco bloques con tres columnas: bloque, minutos planeados y evidencia exacta que se muestra en pantalla (si el docente autorizo equipo, agreguen una cuarta columna con el responsable); el total debe sumar entre 5 y 7 minutos, dejando margen, y la demo en vivo debe ocupar por lo menos la mitad.
2. Paso 2. Ejecuten el sembrador de datos de demostracion para dejar datos_demo con duenos.csv, mascotas.csv y citas.csv, y corran el chequeo pre-vuelo hasta que las tres lineas salgan en [OK] con filas mayores que cero.
3. Paso 3. Hagan el ensayo numero uno con el cronometro del programa: hablen cada bloque completo de pie y sin saltarse ninguno (si trabajan en equipo, cada integrante el suyo), y al final anoten tiempo real contra tiempo planeado de cada bloque en la planilla.
4. Paso 4. Graben el plan B: un video de dos a tres minutos con la ruta feliz completa (registrar dueno, registrar mascota, agendar cita, buscar por ID, cerrar y volver a abrir mostrando que los datos siguen ahi) y exporten seis capturas de pantalla de esos mismos momentos.
5. Paso 5. Intercambien con otro compañero (o con otro equipo, si el docente lo autorizo) una ronda de cinco preguntas de jurado, ajusten el guion con lo que fallo, hagan el ensayo numero dos y suban a ExamLab el guion, la planilla de tiempos de los dos ensayos y el video de respaldo.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Guion de sustentacion con bloques, minutos y evidencia que se muestra (mas el responsable nominal solo si el docente autorizo equipo), mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 14 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 14/Quiz Clase 14 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 14/Solucion Taller Clase 14 - VetCare.docx` — no proyectar completa.
