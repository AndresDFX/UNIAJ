# Guion docente · Clase 1 · Introduccion a la Programacion Orientada a Objetos

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Entorno de desarrollo listo y la primera clase del dominio VetCare escrita
- **Entregable de hoy:** Proyecto Java con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 1 - Introduccion a POO/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Antes de la POO un programa era una lista de procedimientos que...** — 5 vinetas.

**La distincion que mas cuesta el primer dia es clase contra objeto** — 6 vinetas.

**Los cuatro pilares se entienden por el problema que resuelve cada uno** — 4 vinetas.

**Herencia es que una clase puede extender a otra y reutilizar lo que ya...** — 4 vinetas.

**El constructor es el metodo que se ejecuta al crear el objeto y deja...** — 4 vinetas.

**En Programacion I el estudiante trabajo con programacion estructurada:... (1/2)** — 6 vinetas.

**En Programacion I el estudiante trabajo con programacion estructurada:... (2/2)** — 3 vinetas.

**Ahora el punto que decide el semestre, y por eso va temprano: que es un... (1/2)** — 5 vinetas.

**Ahora el punto que decide el semestre, y por eso va temprano: que es un... (2/2)** — 5 vinetas.

**De lo anterior sale la pregunta que aparece sin falta en las primeras... (1/2)** — 5 vinetas.

**De lo anterior sale la pregunta que aparece sin falta en las primeras... (2/2)** — 4 vinetas.

**Recien ahora tiene sentido la analogia clasica (1/2)** — 7 vinetas.

**Recien ahora tiene sentido la analogia clasica (2/2)** — 4 vinetas.

**El encapsulamiento se ensena mal cuando se presenta como la orden de... (1/2)** — 8 vinetas.

**El encapsulamiento se ensena mal cuando se presenta como la orden de... (2/2)** — 7 vinetas.

**El constructor es la pieza que garantiza que el objeto nazca valido (1/2)** — 6 vinetas.

**El constructor es la pieza que garantiza que el objeto nazca valido (2/2)** — 4 vinetas.

**Queda el error mas frecuente de Java, y hay que nombrarlo hoy porque su... (1/2)** — 6 vinetas.

**Queda el error mas frecuente de Java, y hay que nombrarlo hoy porque su... (2/2)** — 5 vinetas.

**El entorno cierra la clase y tiene dos reglas duras que producen el... (1/2)** — 5 vinetas.

**El entorno cierra la clase y tiene dos reglas duras que producen el... (2/2)** — 4 vinetas.


**Demo que usted debe poder repetir:** Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Escribir en vivo la clase Mascota y un main que instancia dos mascotas con datos distintos, mostrando que salen del mismo molde
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Codigo/Mascota.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Instale y verifique el entorno (JDK 17+ y VS Code con el Extension Pack for Java) y cree un proyecto Java llamado VetCare con paquete vetcare. Este paso es el objetivo real del bloque: nadie puede quedarse sin entorno funcionando.
2. Escriba la clase Mascota con al menos tres atributos privados (id, nombre, especie) y un constructor que los reciba todos.
3. Agregue al menos un getter y sobreescriba toString() para que la mascota se imprima de forma legible.
4. En el main, cree DOS objetos Mascota con datos distintos e imprimalos: debe verse que salen del mismo molde pero con valores diferentes.
5. Si termina antes: agregue un setter que valide (por ejemplo, que rechace una edad negativa) y pruebelo desde el main.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Proyecto Java con la clase Mascota (atributos privados, constructor y toString) y un main que crea dos objetos distintos

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Entorno de desarrollo listo y la primera clase del dominio VetCare escrita. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
