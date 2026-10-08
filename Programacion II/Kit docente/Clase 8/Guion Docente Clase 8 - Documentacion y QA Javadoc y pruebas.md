# Guion docente · Clase 8 · Documentacion y QA · Javadoc y pruebas

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.
- **Entregable de hoy:** Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 8 - Documentacion y QA Javadoc y pruebas/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Documentar no es comentar cada línea** — 3 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La documentacion tecnica no describe la implementacion, describe la promesa.

**[Slide 5] Anatomía de un bloque Javadoc** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La primera frase debe ser un resumen corto que termine en punto, porque esa frase es la que aparece en las tablas resumen del HTML generado.
  - Subrayar: Lo que se genera es un sitio web: en VS Code se corre la herramienta del JDK desde la terminal integrada, «javadoc -d docs -private src/clinica/*.java», que crea la carpeta docs/ y deja un index.html que se abre en el navegador con la misma cara que tiene la documentacion oficial de Java.

**[Slide 6] Javadoc de un constructor** — programa completo (25 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 7] El contrato de agendar(), en Javadoc** — programa completo (47 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] agendar(): cada @throws en el código** — programa completo (49 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 9] Nombres que se explican solos** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Ahora bien, la mejor documentacion es la que no hay que escribir, y eso se logra con nombres que se explican solos.

**[Slide 10] Un caso de prueba: preparar, ejecutar, verificar** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Un caso de prueba tiene cuatro partes y conviene escribirlas en el tablero antes de tocar el teclado: un nombre que se lea como una frase, unos datos o estado de partida, una accion concreta y un resultado esperado.

**[Slide 11] nuevaAgenda(): el mismo estado de partida** — programa completo (45 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 12] Caso positivo y caso negativo** — programa completo (46 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 13] JUnit: pruebas que corren solas** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La diferencia con la prueba manual es importante y hay que decirla completa: la prueba unitaria es automatica, repetible, rapida y prueba logica aislada, y por eso se corre cada vez que se toca el codigo; la prueba manual la hace un humano usando la interfaz, sirve para lo que no se puede automatizar facil (que el JOptionPane se lea bien, que la ventana no se congele, que el flujo tenga sentido para la recepcionista) y no reemplaza a la otra.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: confundir Javadoc con comentarios normales y escribir // encima de los metodos creyendo que eso genera documentacion, o abrir el bloque con /* en vez de /** y despues no entender por que el HTML sale vacio. Muy de la mano va el vicio de documentar lo obvio (un @return 'retorna el nombre' sobre getNombre()) y dejar sin una sola linea el metodo agendar, que es justo donde vive la regla de negocio que nadie adivina. En pruebas los errores son igual de tipicos: llamar 'prueba' a un main con System.out.println donde el docente mira la consola y dice 'si, funciono' (eso no es automatico ni repetible, y nadie se entera cuando se rompe tres semanas despues); escribir pruebas que dependen del orden porque comparten un Singleton sucio de la prueba anterior; e intentar probar la ventana en vez del servicio, que es el sintoma clasico de haber metido la logica dentro del boton. Y el peor de todos, el que hay que desarmar en voz alta: creer que 'si compila, funciona'. Compilar solo significa que la sintaxis esta bien; que la mascota inactiva no pueda agendar cita es algo que solo se sabe si alguien lo comprueba.


**Demo que usted debe poder repetir:** El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 8/Codigo/ClinicaQADemo.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 8 - Documentacion y QA Javadoc y pruebas/Taller PI - Clase 8 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Documente con Javadoc las clases Mascota y Cita y el servicio AgendaService: bloque de clase con resumen y @author, y en cada metodo publico @param por parametro, @return si aplica y @throws por cada excepcion; el metodo agendar debe dejar escrita la regla 'una mascota inactiva no puede agendar'.
2. Renombre al menos tres identificadores pobres del proyecto (por ejemplo validar por agendar, b por mascotaActiva, dato1 por idMascota) usando Rename Symbol (F2) de VS Code para que el cambio se propague sin romper nada.
3. Genere la documentacion con clic derecho sobre el proyecto y Generate Javadoc, abra el HTML y verifique que en la ficha de AgendaService se lee la regla de negocio y las tres excepciones documentadas; guarde una captura.
4. Cree en Test Packages la clase AgendaServiceTest con un metodo de preparacion que registre M-001 Kira activa, M-002 Michi activa y M-009 Rocky inactiva, y escriba cuatro casos: mascota activa agenda, mascota inactiva lanza IllegalStateException, ID inexistente lanza NoSuchElementException y horario ocupado no duplica la cita.
5. Rompa a proposito la regla (comente la validacion de mascota inactiva), corra las pruebas y capture la barra roja; restaure la validacion, corra otra vez y capture la barra verde; escriba ademas dos pruebas manuales que NO se pueden automatizar y suba todo a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Mascota, Cita y AgendaService con Javadoc completo, la carpeta HTML generada y una clase de pruebas con cuatro casos, subidos a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 8 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx` — no proyectar completa.
