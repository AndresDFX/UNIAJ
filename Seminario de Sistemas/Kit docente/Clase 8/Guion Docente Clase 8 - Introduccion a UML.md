# Guion docente · Clase 8 · Introduccion a UML

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion.
- **Entregable de hoy:** Diagrama de clases de VetCare hecho en draw.io, exportado a PNG y al archivo .drawio, con 5 clases, atributos tipados, metodos propios y 4 asociaciones con multiplicidad y nombre de rol, subido a ExamLab.
- **Herramienta:** draw.io · Mermaid
- **Slides:** `Clases/Clase 8 - Introduccion a UML/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**UML significa Lenguaje Unificado de Modelado y nacio en los anos... (1/2)** — 4 vinetas.

**UML significa Lenguaje Unificado de Modelado y nacio en los anos... (2/2)** — 2 vinetas.

**Los diagramas se agrupan en dos grandes vistas** — 5 vinetas.
  - Los diagramas se agrupan en dos grandes vistas.
  - Un mismo sistema necesita las dos, igual que una casa necesita el plano de plantas y tambien el plano de instalaciones.
  - En VetCare vamos a usar clases hoy, casos de uso y secuencia mas adelante, y el resto se menciona para que sepan que existen.

**El diagrama de clases se dibuja con una caja de tres compartimentos:... (1/2)** — 4 vinetas.

**El diagrama de clases se dibuja con una caja de tres compartimentos:... (2/2)** — 2 vinetas.

**Las lineas entre clases son la mitad del valor del diagrama (1/2)** — 4 vinetas.
  - Cita relaciona a Mascota y a Veterinario, cada cita con exactamente una mascota y un veterinario, y cada veterinario con muchas citas.

**Las lineas entre clases son la mitad del valor del diagrama (2/2)** — 3 vinetas.

**El diagrama que dibujamos hoy no se queda en la clase: es la pieza que...** — 5 vinetas.
  - Por eso el diagrama debe estar limpio: nombres en singular, sin atributos repetidos en dos clases, sin lineas sueltas y sin cajas que no correspondan a ningun requisito.

**El diagrama de clases en Mermaid: la sintaxis completa** — 19 vinetas.

**Lo que NO es una clase del dominio** — 12 vinetas.


**Demo que usted debe poder repetir:** El docente dibuja en vivo Dueno, Mascota y Cita en draw.io y borra tres atributos mal ubicados explicando a que clase pertenecen de verdad.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente dibuja en vivo Dueno, Mascota y Cita en draw.io y borra tres atributos mal ubicados explicando a que clase pertenecen de verdad.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 8/Plantillas/Diagrama-Clases-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: subraye en el catalogo de requisitos y en el backlog los sustantivos del negocio de VetCare y arme la lista de clases candidatas, descartando las que sean pantallas, reportes o cosas tecnicas.
2. Paso 2: dibuje en draw.io las cinco clases Dueno, Mascota, Cita, Veterinario y Atencion con la caja de tres compartimentos, en singular y con mayuscula inicial.
3. Paso 3: coloque minimo cuatro atributos por clase con visibilidad y tipo (por ejemplo -documento: String, -fechaNacimiento: Date) verificando que ningun atributo este repetido en dos clases distintas.
4. Paso 4: agregue al menos un metodo propio del dominio por clase (por ejemplo +calcularEdad(): int en Mascota, +reprogramar(nuevaFecha: Date) en Cita) y descarte metodos tecnicos como conectarBD o guardarEnDisco.
5. Paso 5: trace las cuatro asociaciones con nombre de relacion y multiplicidad en ambos extremos, leala cada una en voz alta como frase completa, exporte a PNG y .drawio y suba ambos archivos a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Diagrama de clases de VetCare hecho en draw.io, exportado a PNG y al archivo .drawio, con 5 clases, atributos tipados, metodos propios y 4 asociaciones con multiplicidad y nombre de rol, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - VetCare.docx` — no proyectar completa.
