# Guion docente · Clase 13 · Diseño de interfaces

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Quedan listas las pantallas de Registrar mascota y Buscar expediente de VetCare, anotadas y conectadas en un prototipo navegable.
- **Entregable de hoy:** Un archivo de Figma o Penpot con las dos pantallas anotadas y minimo tres transiciones navegables, mas la hoja de anotaciones que amarra cada campo a un RF y a un atributo del diccionario de datos, subido a ExamLab.
- **Herramienta:** Figma o Penpot · Excalidraw · Google Docs
- **Slides:** `Clases/Clase 13 - Diseño de interfaces/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**Un wireframe, un mockup y un prototipo no son tres nombres elegantes... (1/2)** — 5 vinetas.

**Un wireframe, un mockup y un prototipo no son tres nombres elegantes... (2/2)** — 3 vinetas.

**Los principios de usabilidad no son gusto ni estetica, son reglas... (1/2)** — 5 vinetas.

**Los principios de usabilidad no son gusto ni estetica, son reglas... (2/2)** — 4 vinetas.

**Una pantalla suelta no sirve para nada; lo que se diseña es un flujo de... (1/2)** — 5 vinetas.

**Una pantalla suelta no sirve para nada; lo que se diseña es un flujo de... (2/2)** — 3 vinetas.

**La interfaz no se inventa: se deriva de los artefactos que el equipo ya...** — 4 vinetas.
  - Por eso los wireframes se entregan anotados: se ponen numeritos sobre el dibujo y al lado una tabla que dice, por ejemplo, el numero uno es el campo Nombre de la mascota que sale del atributo Mascota.nombre, texto de sesenta caracteres, obligatorio, exigido por RF-03; el numero cuatro es el mensaje de confirmacion que cumple el RNF-02 de respuesta menor a tres segundos.
  - Esa anotacion tiene un efecto secundario muy util: si aparece un campo en la pantalla que no esta en el diccionario de datos, entonces o falta un requisito o sobra el campo, y ambas cosas hay que resolverlas hoy y no cuando el compañero de Programacion II ya escribio la tabla.

**Una interfaz se puede evaluar sin programarla, y esa es una de las...** — 5 vinetas.
  - Eso obliga a decisiones de diseño concretas: letra grande, pocos campos obligatorios, nada de scroll interminable, tolerancia a la interrupcion para que si la llaman y vuelve en tres minutos no haya perdido lo escrito, y mensajes en lenguaje de clinica y no de sistemas, es decir Esta mascota ya tiene ficha en la clinica y no Violacion de restriccion de unicidad.


**Demo que usted debe poder repetir:** El docente dibuja en vivo el wireframe de Registrar mascota en Penpot, le pone tres anotaciones numeradas y lo conecta con Buscar expediente para que la clase vea en la misma pantalla la diferencia entre wireframe, mockup y prototipo.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Quedan listas las pantallas de Registrar mascota y Buscar expediente de VetCare, anotadas y conectadas en un prototipo navegable. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente dibuja en vivo el wireframe de Registrar mascota en Penpot, le pone tres anotaciones numeradas y lo conecta con Buscar expediente para que la clase vea en la misma pantalla la diferencia entre wireframe, mockup y prototipo.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 13/Plantillas/Wireframes-Anotados-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1. En Excalidraw o en papel, dibujen el wireframe en gris de la pantalla Registrar mascota de VetCare, sin colores ni logos, ubicando bloque de dueño, bloque de datos de la mascota y zona de accion; el wireframe debe caber en una sola vista sin scroll y no puede tener mas de nueve campos.
2. Paso 2. Numeren de uno a seis los elementos criticos del wireframe y llenen la tabla de anotaciones indicando para cada numero el atributo del diccionario de datos que lo respalda, el RF que lo exige y si es obligatorio u opcional; si un elemento no tiene RF, borrenlo o creen el requisito y dejenlo escrito.
3. Paso 3. Diseñen la pantalla Buscar expediente resolviendo explicitamente el caso de resultados multiples: definan los tres criterios de busqueda, las columnas de la lista de resultados que permiten desambiguar y el mensaje exacto que se muestra cuando no hay ningun resultado.
4. Paso 4. Pasen las dos pantallas a Figma o Penpot como mockup y conecten minimo tres transiciones navegables: Registrar mascota hacia la confirmacion con codigo, confirmacion hacia Buscar expediente, y un resultado de la lista hacia la ficha del paciente; escriban al lado de cada transicion que principio de usabilidad estan cumpliendo.
5. Paso 5. Hagan prueba de pasillo con otro compañero, denle la tarea registrar la mascota Luna de la señora Perez y encontrar su ficha, no le expliquen nada, cronometren, cuenten clics y anoten los dos puntos donde dudo; escriban abajo los dos cambios concretos que haran al diseño por lo observado.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un archivo de Figma o Penpot con las dos pantallas anotadas y minimo tres transiciones navegables, mas la hoja de anotaciones que amarra cada campo a un RF y a un atributo del diccionario de datos, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 13/Quiz Clase 13 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Quedan listas las pantallas de Registrar mascota y Buscar expediente de VetCare, anotadas y conectadas en un prototipo navegable.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 13/Solucion Taller Clase 13 - VetCare.docx` — no proyectar completa.
