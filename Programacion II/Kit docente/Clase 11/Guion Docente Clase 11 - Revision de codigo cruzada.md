# Guion docente · Clase 11 · Revisión de código cruzada

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.
- **Entregable de hoy:** Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.
- **Herramienta:** Visual Studio Code (Java)
- **Slides:** `Clases/Clase 11 - Revision de codigo cruzada/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Las ideas de cada concepto estan proyectadas y el desarrollo completo esta en las notas del presentador de su lamina. Aqui va, por lamina y en su orden, lo que hay que subrayar.

**[Slide 4] Qué es una revisión de código** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Conviene decirlo claro porque el estudiante llega con dos ideas equivocadas: que la revisión es un examen donde lo van a rajar, o que es un trámite para poner 'todo bien' y salir rápido.

**[Slide 5] El código a revisar: main()** — programa completo (50 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 6] Revisar por capas** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Se ejecuta antes de opinar.
  - Subrayar: Y solo al final, la sexta: formato e indentación, que es la que menos vale y la que todo el mundo comenta primero.
  - Subrayar: Si un informe de revisión de VetCare tiene ocho comentarios de espacios y ninguno sobre el NullPointerException al buscar un ID inexistente, esa revisión no sirvió.

**[Slide 7] proceso(): ¿qué capas fallan?** — programa completo (39 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 8] Retroalimentación: evidencia, impacto, sugerencia** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: La retroalimentación útil tiene una estructura, y esa estructura se enseña con plantilla porque a punta de buena intención no sale.
  - Subrayar: Cuarto, se propone una salida concreta.
  - Subrayar: Compare las dos versiones.
  - Subrayar: La segunda se puede atender esta tarde; la primera solo produce rabia.

**[Slide 9] Dos búsquedas casi iguales** — programa completo (36 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 10] El checklist de revisión** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: ¿la interfaz gráfica muestra la lista y permite registrar y buscar?
  - Subrayar: ¿hay algún catch vacío?
  - Subrayar: ¿algún método pasa de cincuenta líneas?
  - Subrayar: ¿hay bloques duplicados?

**[Slide 11] imprimirFicha(): el mismo bucle otra vez** — programa completo (28 lineas): se copia en Main.java y corre solo. Leerlo de arriba abajo y ejecutarlo; la salida esperada esta en las notas del presentador.

**[Slide 12] Recibir la crítica** — 4 ideas proyectadas; el desarrollo, en las notas del presentador.
  - Subrayar: Hay tres antipatrones que van a aparecer y conviene nombrarlos de una vez: la revisión de sello, que aprueba en dos minutos sin haber ejecutado nada; la revisión de gusto personal, que solo señala estilo e indentación; y la revisión que rediseña el proyecto ajeno, donde el revisor propone rehacer VetCare con su propia arquitectura en vez de señalar problemas concretos del que tiene enfrente.

## Errores tipicos del docente que no domina el tema

Material de preparacion: no se proyecta.

- Error tipico del docente que no domina el tema: cree que revisar código es leer y decir si le gusta, entonces la sesión se convierte en un intercambio de opiniones sobre llaves e indentación mientras el NullPointerException sigue vivo; o peor, convierte la revisión en calificación entre estudiantes y se le arma la pelea en clase, porque nadie recibe bien que un compañero le ponga la nota. Otro error muy frecuente es no exigir que el revisor ejecute el proyecto antes de escribir: así aparecen hallazgos inventados y el autor se defiende con razón, con lo cual la actividad pierde toda autoridad. Y un tercero: no dar plantilla ni checklist, esperando que el criterio salga solo. El manejo correcto es explícito desde el minuto uno: la nota la pone el docente y el informe de quien revisa es un insumo, no una sentencia; todo hallazgo va con evidencia reproducible; se revisa el código y nunca a la persona; y el docente modela en vivo, con ClinicaParaRevisar.java proyectado, cómo se reescribe un comentario agresivo en uno accionable. Un docente que nunca ha recibido una revisión de su propio código tiende a defender el suyo igual que el estudiante, y por eso conviene que empiece dejando revisar el archivo de la demo.


**Demo que usted debe poder repetir:** El docente proyecta ClinicaParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de concepto y en las de codigo
(lo que hay que subrayar esta tambien en las notas del presentador de cada lamina). Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta ClinicaParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 11/Codigo/ClinicaParaRevisar.java`

### 60-105 · Taller guiado (opcional) = avance del PI
Opcional: no tiene lamina en el deck. La guia esta en
`Clases/Clase 11 - Revision de codigo cruzada/Taller PI - Clase 11 - VetCare.docx`; si hoy no se hace, se extiende la demo y la practica libre.
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Intercambien proyectos: cada estudiante entrega su carpeta comprimida más un archivo de tres líneas con las instrucciones de ejecución, y recibe el proyecto de otro compañero (si el docente autorizó equipos, el de otro equipo; la revisión funciona igual); lo primero es abrirlo en VS Code y ejecutarlo, anotando si arrancó y, si no, el mensaje de error exacto copiado tal cual.
2. Recorran el proyecto recibido con el checklist de doce ítems (clase de dominio, encapsulamiento, colección, interfaz gráfica, try-catch en fronteras, persistencia, catch vacío, métodos largos, duplicación, nombres, números mágicos, validación de casos borde) marcando cumple / no cumple / no aplica y escribiendo la evidencia archivo:línea en cada 'no cumple'.
3. Provoquen a propósito los cuatro casos borde de VetCare (edad con letras, campos vacíos, buscar un ID inexistente, borrar o dañar una línea de mascotas.csv) y registren qué hizo la aplicación en cada uno, con el texto del mensaje o de la excepción.
4. Redacten cinco hallazgos priorizados como bloqueante, mayor o menor, cada uno con el formato Evidencia + Impacto + Sugerencia, todos referidos al código y ninguno a la persona; incluyan al menos un bloqueante si existe.
5. Hagan la devolución cruzada de ocho minutos por proyecto revisado y cierren con el plan de corrección escrito por su autor: qué acepta y corrige, qué justifica y deja igual, y qué difiere, con responsable en cada línea.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Si hubo taller, repasar los criterios de exito del `Taller PI - Clase 11 - VetCare.docx` (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx` — no proyectar completa.
