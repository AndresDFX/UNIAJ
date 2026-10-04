# Guion docente · Clase 4 · Metodologias agiles

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda listo el backlog priorizado de VetCare repartido en sprints del semestre, con las primeras historias de usuario escritas con criterios de aceptacion.
- **Practica (opcional):** `Clases/Clase 4 - Metodologias agiles/Taller PI - Clase 4 - VetCare.docx` — no esta en el deck
- **Herramienta:** draw.io · Excalidraw · Google Docs
- **Slides:** `Clases/Clase 4 - Metodologias agiles/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] El manifiesto ágil** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El manifiesto agil se firmo en 2001 por diecisiete personas cansadas de proyectos que entregaban documentos perfectos y sistemas inservibles.
  - Tiene cuatro valores y la clave esta en la palabra que los une: 'sobre'.
  - Dice sobre, no 'en vez de': lo de la derecha sigue teniendo valor, solo que lo de la izquierda tiene mas.
  - Ademas hay doce principios, y tres son muy utiles aqui: entregar valor pronto y con frecuencia, aceptar el cambio incluso tarde, y mantener un ritmo sostenible.
  - En la clinica esto se traduce en algo muy concreto: es mejor mostrarle a la clinica un mockup imperfecto de la ficha en la semana tres que un documento de ochenta paginas en la semana quince.
  - NOTAS:
  - Individuos e interacciones SOBRE procesos y herramientas; software funcionando SOBRE documentacion exhaustiva; colaboracion con el cliente SOBRE negociacion contractual; respuesta ante el cambio SOBRE seguir un plan.

**[Slide 5] Scrum: roles, eventos y artefactos** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Scrum es un marco de trabajo, no una metodologia completa: define lo minimo y deja que cada equipo llene el resto.
  - Tiene tres roles: el Product Owner, que decide QUE se hace y en que orden, y es el dueño del Product Backlog; el Scrum Master, que facilita, protege al equipo y quita impedimentos
  - Y que no es el jefe; y el equipo de desarrollo, que decide COMO hacerlo y se autoorganiza.
  - Tiene cinco eventos: el Sprint, que es el contenedor de duracion fija (una a cuatro semanas), la Planificacion, la Reunion diaria de quince minutos para sincronizarse
  - La Revision donde se le muestra el incremento al cliente, y la Retrospectiva donde se mejora la forma de trabajar.
  - Y tiene tres artefactos: Product Backlog, Sprint Backlog e Incremento, este ultimo gobernado por la Definicion de Terminado.
  - NOTAS:
  - En la clinica el docente actua como vocero de la clinica en el rol de Product Owner, y cada estudiante -o cada equipo, si el docente lo autoriza- hace de equipo de desarrollo que se compromete con un objetivo de sprint.

**[Slide 6] El plan de sprints en Mermaid (gantt)** — 15 vinetas.

**[Slide 7] Kanban y el límite de trabajo en curso** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Kanban viene de otra tradicion y su promesa es distinta: no impone iteraciones ni roles, sino que hace visible el flujo del trabajo.
  - Sus practicas centrales son visualizar el trabajo en un tablero, limitar el trabajo en curso, gestionar el flujo detectando donde se acumulan las tarjetas, hacer explicitas las politicas de cada columna y mejorar de forma continua.
  - El limite de trabajo en curso es la parte que mas cuesta y la que mas sirve: si el equipo pone limite dos en la columna 'Modelando', nadie puede empezar una tercera tarea sin terminar alguna.
  - El estudiante que abre cinco diagramas al tiempo y no termina ninguno es exactamente el problema que el limite de trabajo en curso resuelve.
  - NOTAS:
  - En la clinica el tablero seria Por hacer / Modelando / En revision del cliente / Aprobado, y la politica de la ultima columna podria ser 'solo pasa a Aprobado si tiene diagrama, mockup y visto bueno de la clinica'.

**[Slide 8] El tablero de flujo con limite de trabajo en curso** — 20 vinetas.

**[Slide 9] Iteración e incremento** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Hay dos palabras que se usan como sinonimos y significan cosas distintas: iteracion e incremento.
  - Incremento es agregar un pedazo nuevo y utilizable al sistema; iteracion es volver sobre algo que ya existe y mejorarlo con base en la retroalimentacion.
  - En la clinica el incremento 1 es el mockup de la ficha del paciente; cuando la veterinaria lo mira y dice 'me falta el campo de alergias y la foto de la mascota', y el equipo produce la version 2 de ese mismo mockup, eso es iteracion.
  - Y aqui aparece una regla practica que salva proyectos: cada entrega debe ser una rebanada vertical, algo que el cliente pueda ver y opinar, no una capa horizontal invisible.
  - Entregar 'todas las tablas de la base de datos' no es un incremento util para la clinica; entregar 'registrar y consultar una ficha completa de principio a fin' si lo es.
  - NOTAS:
  - Agil hace las dos cosas al mismo tiempo.

**[Slide 10] Historia de usuario con criterios de aceptacion** — 14 vinetas.

**[Slide 11] Ágil no es trabajar sin documentación** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Agil no significa trabajar sin documentacion, y este es el malentendido que mas daño hace.
  - El manifiesto dice software funcionando sobre documentacion exhaustiva: lo que se rechaza es el documento inflado que nadie lee, no el documento util.
  - Para este curso esto es central: en Seminario de Sistemas el producto ES documentacion de diseño, y aun asi el trabajo puede ser perfectamente agil, porque se produce por incrementos, se revisa con el cliente y se corrige.
  - El estudiante que solo cursa esta materia trabaja con sprints igual que los demas: sus incrementos son mockups, casos de uso y diccionario de datos, y cierra con un prototipo navegable que se puede recorrer y criticar.
  - NOTAS:
  - Un equipo agil documenta historias de usuario con criterios de aceptacion, la Definicion de Terminado, las decisiones de arquitectura, el diccionario de datos y los diagramas que hagan falta, pero los escribe justo a tiempo y los mantiene vivos.


**Demo que usted debe poder repetir:** El docente arma en pantalla el tablero de VetCare, arrastra una tarjeta de 'Por hacer' a 'En revision del cliente' y muestra que pasa cuando se rompe el limite de trabajo en curso.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Metodologias agiles. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente arma en pantalla el tablero de VetCare, arrastra una tarjeta de 'Por hacer' a 'En revision del cliente' y muestra que pasa cuando se rompe el limite de trabajo en curso.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 4/Plantillas/Backlog-y-Sprints-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 4 - Metodologias agiles/Taller PI - Clase 4 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. En Google Docs escriba el Product Backlog de VetCare con al menos ocho items redactados como historias de usuario cortas, cada uno con prioridad (Alta/Media/Baja) y una justificacion de valor para Huellitas en una linea.
2. Priorice el backlog en orden de arriba hacia abajo y explique por escrito, en dos renglones, por que el primer item es el primero (pista: resuelve uno de los tres dolores de la clinica).
3. Escriba tres historias completas con criterios de aceptacion en formato Dado/Cuando/Entonces, y asegurese de que cada historia tenga al menos un escenario alternativo o de error, no solo el camino feliz.
4. Redacte la Definicion de Terminado para artefactos de diseño (por ejemplo: tiene diagrama en draw.io, tiene mockup, esta revisado por un compañero y tiene el visto bueno del cliente) y escribala en la cabecera del tablero.
5. En draw.io o Excalidraw arme el tablero con las columnas Por hacer / Modelando / En revision del cliente / Aprobado, ponga el limite de trabajo en curso en dos para las columnas del medio, distribuya las tarjetas en tres sprints con su objetivo y entregable de diseño, exporte a PDF y suba a ExamLab.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un tablero en draw.io o Excalidraw con el Product Backlog priorizado de VetCare y las columnas de flujo con limite de trabajo en curso, mas un documento con el plan de tres sprints (objetivo y entregable de diseño de cada uno), la Definicion de Terminado y tres historias de usuario con criterios en formato Dado/Cuando/Entonces.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 4/Quiz Clase 4 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda listo el backlog priorizado de VetCare repartido en sprints del semestre, con las primeras historias de usuario escritas con criterios de aceptacion.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 4/Solucion Taller Clase 4 - VetCare.docx` — no proyectar completa.
