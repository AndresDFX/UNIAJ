# Guion docente · Clase 14 · Preparacion de la presentacion final · Sustentacion de VetCare

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.
- **Entregable de hoy:** Guion de sustentacion con bloques, responsable y minutos, mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 14 - Preparacion de la presentacion final/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Sustentar un proyecto de software no es exponer diapositivas: es demostrar, delante de un jurado que duda con razon, que un problema real quedo resuelto por un programa que corre. El jurado no compra promesas ni diagramas bonitos, compra evidencia; por eso la regla practica es que al menos la mitad del tiempo debe ser aplicacion corriendo en pantalla. El orden que funciona es siempre el mismo y va de lo humano a lo tecnico y de vuelta a lo humano: primero el problema de la clinica Huellitas en una frase concreta (todo en papel, se pierden expedientes, no se sabe quien tiene cita manana), luego la solucion en una frase (una aplicacion de escritorio en Java que registra duenos y mascotas, agenda citas y conserva los datos), despues la arquitectura en treinta segundos (las clases Dueno, Mascota y Cita y como se relacionan), enseguida la demo en vivo que es el corazon, y al cerrar los aprendizajes y las limitaciones. Empezar por el diagrama de clases o por la lista de tecnologias es el error mas comun: nadie sabe todavia para que sirve eso.

La sustentacion es una coreografia de equipo y hay que repartirla como se reparte una obra de teatro. Cada integrante toma un bloque completo con inicio y final, no frases sueltas, y ademas se define quien maneja el mouse, quien narra mientras el otro opera y quien tiene el computador de respaldo con el proyecto ya abierto. Las transiciones se dicen en voz alta, con una formula corta del tipo 'para mostrar como quedan guardados esos datos, sigue Julian', porque los silencios incomodos entre integrantes son lo que mas se nota. La regla de oro es que ninguno se queda callado, aunque uno domine mas el codigo: el jurado evalua al equipo y siempre pregunta quien hizo que. Un guion escrito, con minutos por bloque y nombre del responsable, convierte una exposicion nerviosa en algo que se puede ensayar y medir; en VetCare ese guion tiene cinco bloques y suma siete minutos, con cuatro dedicados a la demo.

La demo en vivo no falla por mala suerte, falla por falta de preparacion, y se blinda con un chequeo previo que llamaremos pre-vuelo. Lo primero es sembrar datos de demostracion: tres duenos, cuatro mascotas y tres citas ya cargadas en los CSV, porque una aplicacion con la lista vacia parece una aplicacion que no funciona, y ademas los datos deben ser creibles del dominio (Marta Lopez con Firulais, labrador de 4 anios) y nunca 'aaa' ni 'prueba1'. Lo segundo es tener ensayado el camino feliz exacto, es decir la secuencia de clics que se va a hacer, sin improvisar busquedas ni teclear rutas largas frente al publico. Lo tercero es la higiene de pantalla: aumentar el tamano de fuente del IDE, cerrar notificaciones y pestanas ajenas, dejar el proyecto ya compilado y, si es posible, ejecutar el .jar en lugar de compilar delante del jurado. Lo cuarto es el plan B: un video de dos o tres minutos de la ruta feliz y seis capturas de pantalla listas, para que si el computador falla la presentacion continue sin panico. Y hay un quinto detalle que suma puntos: provocar a proposito un error de edad para mostrar la validacion de la clase 13 como una fortaleza, no como un accidente.

Las preguntas del jurado son casi siempre las mismas y se pueden preparar una por una. Donde esta la herencia y por que la usaron; por que ArrayList y no un arreglo fijo; que pasa si borro el archivo mascotas.csv; como controlan que alguien escriba texto donde va la edad; quien programo cada parte; que harian distinto si empezaran de nuevo. La forma de responder tiene tres reglas: responda con la aplicacion o el codigo en pantalla, porque mostrar vale mas que explicar; no se demore mas de treinta o cuarenta segundos por respuesta; y si no sabe, digalo con dignidad y proponga como lo averiguaria, que eso el jurado lo respeta mucho mas que un invento. Tambien conviene tener a la mano el archivo de cada respuesta ya abierto en una pestana del IDE (Dueno.java para la herencia, Mascota.java para las validaciones, la clase de persistencia para el CSV), de modo que la respuesta sea abrir una pestana y no buscar en vivo.

El manejo del tiempo y del nervio se entrena, no se improvisa. Un ensayo cronometrado revela cosas que el papel no muestra: que la introduccion se come tres minutos, que la demo se atasca en un formulario, que el cierre queda cortado. Por eso hoy ensayamos con reloj y anotamos el tiempo real de cada bloque frente al planeado, y se repite hasta que el total caiga entre cinco y ocho minutos con margen. Hay cosas que restan puntos siempre: leer las diapositivas de espaldas al jurado, pedir disculpas por el proyecto antes de mostrarlo, culpar al computador, hablar de lo que 'iban a hacer' en vez de mostrar lo que hicieron, y pasarse del tiempo, porque eso obliga al jurado a cortar justo en la parte que mas les costo. Al reves, suman: hablar mirando al jurado, usar el vocabulario del dominio (dueno, mascota, cita, historia clinica) y reconocer con naturalidad las limitaciones conocidas.

Error tipico del docente que no domina el tema: dejar la sustentacion para el ultimo dia, decir 'preparen una exposicion' y confiar en que el estudiante que mas sabe hable por todos. Eso produce equipos donde tres personas se quedan mudas, demos improvisadas con la aplicacion vacia y proyectos que se ponen a compilar en vivo mientras el jurado espera. Otras variantes: no cronometrar nunca, permitir que el estudiante muestre codigo linea por linea en lugar de la aplicacion corriendo, y no exigir plan B, para despues perder media hora del examen porque el computador de uno de los equipos no encendio. La clase de hoy no tiene tema tecnico nuevo, pero tiene un producto verificable, y ese es el punto: si al final del bloque cada equipo no tiene guion escrito, datos sembrados y dos ensayos cronometrados, la clase no se cumplio.

**Demo que usted debe poder repetir:** El docente sustenta VetCare en 6 minutos delante del grupo, provoca a proposito un error de edad para mostrar la validacion, y luego repite la misma demo con la lista vacia para que se vea el desastre de no sembrar datos.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente sustenta VetCare en 6 minutos delante del grupo, provoca a proposito un error de edad para mostrar la validacion, y luego repite la misma demo con la lista vacia para que se vea el desastre de no sembrar datos.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 14/Codigo/EnsayoSustentacionVetCare.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. Escriban el guion de la sustentacion en una tabla de cinco bloques con tres columnas: bloque, responsable y minutos planeados; el total debe sumar entre 5 y 7 minutos, dejando margen, y la demo en vivo debe ocupar por lo menos la mitad.
2. Paso 2. Ejecuten el sembrador de datos de demostracion para dejar datos_demo con duenos.csv, mascotas.csv y citas.csv, y corran el chequeo pre-vuelo hasta que las tres lineas salgan en [OK] con filas mayores que cero.
3. Paso 3. Hagan el ensayo numero uno con el cronometro del programa: cada integrante habla su bloque completo de pie, y al final anoten tiempo real contra tiempo planeado de cada bloque en la planilla.
4. Paso 4. Graben el plan B: un video de dos a tres minutos con la ruta feliz completa (registrar dueno, registrar mascota, agendar cita, buscar por ID, cerrar y volver a abrir mostrando que los datos siguen ahi) y exporten seis capturas de pantalla de esos mismos momentos.
5. Paso 5. Intercambien con otro equipo una ronda de cinco preguntas de jurado, ajusten el guion con lo que fallo, hagan el ensayo numero dos y suban a ExamLab el guion, la planilla de tiempos de los dos ensayos y el video de respaldo.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Guion de sustentacion con bloques, responsable y minutos, mas la planilla de tiempos de dos ensayos y el video de respaldo de la ruta feliz, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 14/Quiz Clase 14 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: VetCare queda con guion de sustentacion, juego de datos de demostracion sembrado y ensayo cronometrado dentro de la ventana de 5 a 8 minutos.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 14/Solucion Taller Clase 14 - VetCare.docx` — no proyectar completa.
