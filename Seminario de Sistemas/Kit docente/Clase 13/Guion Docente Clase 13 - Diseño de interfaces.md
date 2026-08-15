# Guion docente · Clase 13 · Diseño de interfaces

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Quedan listas las pantallas de Registrar mascota y Buscar expediente de VetCare, anotadas y conectadas en un prototipo navegable.
- **Entregable de hoy:** Un archivo de Figma o Penpot con las dos pantallas anotadas y minimo tres transiciones navegables, mas la hoja de anotaciones que amarra cada campo a un RF y a un atributo del diccionario de datos, subido a ExamLab.
- **Herramienta:** Figma o Penpot · Excalidraw · Google Docs
- **Slides:** `Clases/Clase 13 - Diseño de interfaces/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un wireframe, un mockup y un prototipo no son tres nombres elegantes para lo mismo: son tres momentos distintos del diseño y cada uno responde una pregunta diferente. El wireframe es el esqueleto en gris, cajas, lineas y etiquetas, sin colores ni logos, y responde a la pregunta que informacion va en esta pantalla y en que orden la va a leer la persona. El mockup ya es la foto fija de como se vera: tipografia, color, iconos, el logo de la clinica Huellitas, los espacios reales entre elementos; responde a la pregunta como se ve. El prototipo es el mockup con clic, es decir uno oprime Guardar y la herramienta lo lleva a otra pantalla; responde a la pregunta como se siente usarlo. En VetCare esto se traduce asi: el wireframe de Registrar mascota se hace en diez minutos en Excalidraw y solo dice que arriba va la busqueda del dueño, en el centro los datos de la mascota y abajo el boton Guardar; el mockup de esa misma pantalla ya usa el verde de la clinica y una tipografia grande porque la recepcionista tiene el monitor lejos; y el prototipo permite que el docente, en la sustentacion, oprima Guardar y aterrice en la ficha del paciente recien creado. La razon de hacerlo en ese orden es puramente economica: mover una caja en un wireframe cuesta treinta segundos, mover esa misma caja cuando ya esta programada en Programacion II cuesta dos sesiones de trabajo. Diseñar es equivocarse barato.

Los principios de usabilidad no son gusto ni estetica, son reglas observables que se pueden verificar sobre el papel. Visibilidad del estado del sistema significa que la persona siempre sepa que esta pasando: si la recepcionista oprime Guardar y la pantalla no dice nada, ella va a oprimir Guardar otra vez y VetCare va a terminar con la mascota registrada dos veces; por eso el diseño debe incluir el mensaje concreto Ficha guardada, codigo M-0421, y el boton debe quedar deshabilitado mientras se guarda. Prevencion de errores significa que es mejor impedir el error que ponerle un mensaje bonito despues: la fecha de nacimiento se escoge en un calendario y no se teclea, la especie se elige de una lista cerrada con Canino, Felino y Otro, y el sistema pide confirmacion antes de eliminar una historia clinica. Consistencia significa que la misma accion se llame igual y viva en el mismo lugar en todas las pantallas: si en Registrar mascota el boton principal se llama Guardar y esta abajo a la derecha, en Registrar dueño no puede llamarse Aceptar ni estar arriba a la izquierda. Reconocer antes que recordar significa que la persona escoja de una lista en vez de acordarse de un codigo: la recepcionista no tiene por que memorizar que el codigo de raza mestiza es 07, se lo mostramos. Cada uno de estos cuatro principios se puede auditar sobre un wireframe impreso, sin una sola linea de codigo, y esa auditoria es exactamente lo que se evalua en esta asignatura.

Una pantalla suelta no sirve para nada; lo que se diseña es un flujo de tarea completo, es decir el recorrido que hace una persona real desde que tiene una intencion hasta que la cumple. El flujo tiene un camino feliz y tiene caminos alternos, y los caminos alternos son donde se cae el diseño de los principiantes. En VetCare el camino feliz de registrar una mascota es: llega el dueño, la recepcionista lo busca, lo encuentra, registra la mascota y el sistema devuelve el codigo. Pero los caminos alternos son igual de reales: el dueño no esta registrado y hay que crearlo sin perder lo que ya se habia escrito de la mascota; la mascota ya existe porque otro turno la registro ayer y hay que avisarlo en vez de duplicarla; el dueño no trae documento y hay que permitir el registro con telefono como identificador temporal. En Buscar expediente pasa lo mismo: el camino feliz es buscar por documento del dueño y encontrar una sola ficha, pero hay que diseñar que ocurre cuando la busqueda por nombre devuelve doce mascotas llamadas Firulais, y ahi la respuesta de diseño es mostrar en la lista de resultados la especie, la edad y el nombre del dueño para poder desambiguar de un vistazo. Un flujo que solo dibuja el camino feliz no es un diseño, es una postal.

La interfaz no se inventa: se deriva de los artefactos que el equipo ya construyo en las clases anteriores. Cada pantalla debe poder señalar el requisito funcional que la origina, cada campo debe existir en el diccionario de datos con su tipo y su longitud, y cada boton debe corresponder a una operacion que aparece en el diagrama de casos de uso o en el de secuencia. Por eso los wireframes se entregan anotados: se ponen numeritos sobre el dibujo y al lado una tabla que dice, por ejemplo, el numero uno es el campo Nombre de la mascota que sale del atributo Mascota.nombre, texto de sesenta caracteres, obligatorio, exigido por RF-03; el numero cuatro es el mensaje de confirmacion que cumple el RNF-02 de respuesta menor a tres segundos. Esa anotacion tiene un efecto secundario muy util: si aparece un campo en la pantalla que no esta en el diccionario de datos, entonces o falta un requisito o sobra el campo, y ambas cosas hay que resolverlas hoy y no cuando el compañero de Programacion II ya escribio la tabla. La trazabilidad no es burocracia, es el mecanismo que hace que los planos y la casa coincidan.

Una interfaz se puede evaluar sin programarla, y esa es una de las habilidades mas valiosas que se lleva un analista. El metodo mas barato es el recorrido cognitivo: se toma una tarea concreta, por ejemplo registrar la mascota Luna de la señora Perez, y una persona que no participo en el diseño intenta hacerla sobre el prototipo sin que nadie le explique nada, mientras usted cuenta cuantos clics necesito, donde dudo y donde se equivoco. La variante de bolsillo es la prueba de pasillo: se le pide a tres compañeros de otro grupo que lo intenten y se anota, sin defenderse ni explicar. Para VetCare hay que evaluar pensando en la usuaria real, que es la recepcionista de Huellitas: no es experta en computadores, escribe lento, contesta el telefono mientras registra y tiene un perro ladrando al lado. Eso obliga a decisiones de diseño concretas: letra grande, pocos campos obligatorios, nada de scroll interminable, tolerancia a la interrupcion para que si la llaman y vuelve en tres minutos no haya perdido lo escrito, y mensajes en lenguaje de clinica y no de sistemas, es decir Esta mascota ya tiene ficha en la clinica y no Violacion de restriccion de unicidad.

Error tipico del docente que no domina el tema: creer que diseñar interfaces es escoger colores y decir que quede bonito, y por lo tanto calificar el mockup mas vistoso. Eso produce tres daños. Primero, se premian pantallas lindas que no se pueden usar: fondos oscuros con letra delgada que la recepcionista no alcanza a leer, iconos sin texto que nadie entiende, animaciones que estorban. Segundo, se acepta un conjunto de pantallas sueltas sin flujo, sin caminos alternos y sin un solo mensaje de error diseñado, lo cual garantiza que en Programacion II el equipo va a improvisar la mitad del comportamiento. Tercero, se pierde la trazabilidad: aparecen campos que nadie pidio, como el correo de la mascota o el numero de chip cuando el diccionario de datos ni lo contempla, y desaparecen campos obligatorios del requisito. El antidoto es sencillo y verificable: exigir siempre wireframe antes que mockup, exigir anotaciones que citen el RF y el atributo del diccionario, exigir al menos dos caminos alternos por flujo y hacer la prueba de pasillo en clase con un otro compañero. Si el docente no se siente seguro juzgando estetica, no importa; lo que debe evaluar es si la tarea se completa sin ayuda y si cada elemento dibujado tiene un requisito que lo respalde.

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
