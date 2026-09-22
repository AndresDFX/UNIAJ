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

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Documentar no es llenar el codigo de comentarios** — 6 vinetas.

**Un bloque Javadoc se escribe con /** y se cierra con */, y va...** — 7 vinetas.

**La mejor documentacion es la que no hay que escribir, y eso se logra...** — 6 vinetas.

**La segunda mitad de la clase es control de calidad** — 8 vinetas.

**JUnit es la herramienta que convierte esos casos en codigo que se... (1/2)** — 6 vinetas.

**JUnit es la herramienta que convierte esos casos en codigo que se... (2/2)** — 4 vinetas.


**Demo que usted debe poder repetir:** El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente escribe un bloque Javadoc, genera la documentacion HTML con javadoc desde la terminal integrada y luego corre las pruebas mostrando la barra en rojo, corrige la regla y la muestra en verde.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 8/Codigo/VetCareQADemo.java`

### 60-105 · Taller guiado = avance del PI
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
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Las clases del dominio de VetCare quedan documentadas con Javadoc y la regla 'mascota inactiva no agenda' queda respaldada por pruebas que se ejecutan solas.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx` — no proyectar completa.
