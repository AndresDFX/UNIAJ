# Guion docente · Clase 11 · Revisión de código cruzada

- **Curso:** Programacion II (FI303204) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** (aplicacion Java de la clinica «Huellitas»)
- **Hoy avanzamos el PI en:** Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.
- **Entregable de hoy:** Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.
- **Herramienta:** Apache NetBeans
- **Slides:** `Clases/Clase 11 - Revision de codigo cruzada/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Una revisión de código es la lectura sistemática del código de otra persona con el fin de encontrar problemas antes de que lleguen al usuario, y de paso repartir conocimiento en el equipo. En la industria esto no es opcional: nadie mezcla su trabajo al proyecto sin que alguien más lo apruebe, y esa aprobación deja rastro escrito. Conviene decirlo claro porque el estudiante llega con dos ideas equivocadas: que la revisión es un examen donde lo van a rajar, o que es un trámite para poner 'todo bien' y salir rápido. No es ninguna de las dos. Es un control de calidad barato: encontrar hoy que buscarPorId devuelve null y nadie lo valida cuesta diez minutos; encontrarlo el día de la sustentación, con la ventana de VetCare congelada y la clínica Huellitas sin poder mostrar el expediente de Firulais, cuesta la nota y la credibilidad. Además la revisión enseña: quien lee el proyecto ajeno descubre una forma distinta de organizar el repositorio o de validar la edad, y se la lleva para el suyo. Hoy no hay tema técnico nuevo; hoy se entrena criterio, que es la habilidad que separa a alguien que escribe código de alguien que responde por él.

Revisar no es leer de arriba a abajo a ver qué salta: se revisa por capas y en orden de importancia, porque el tiempo es finito y el detalle cosmético es el que más tienta. Primera capa: ¿el proyecto abre y hace lo que dice hacer? Se ejecuta antes de opinar. Segunda capa: corrección y casos borde, que en VetCare son siempre los mismos y hay que buscarlos a propósito: edad negativa o con letras, campos vacíos, ID repetido, buscar un ID que no existe, cerrar sin haber registrado nada, archivo mascotas.csv inexistente o con una línea dañada. Tercera capa: diseño y responsabilidades, es decir si hay clases de verdad o solo arreglos de String, si los atributos son privados, y si la ventana está haciendo de repositorio escribiendo archivos por su cuenta. Cuarta capa: manejo de errores, con el catch vacío como sospechoso número uno. Quinta capa: legibilidad, o sea nombres, métodos largos y duplicación. Y solo al final, la sexta: formato e indentación, que es la que menos vale y la que todo el mundo comenta primero. Si un informe de revisión de VetCare tiene ocho comentarios de espacios y ninguno sobre el NullPointerException al buscar un ID inexistente, esa revisión no sirvió.

La retroalimentación útil tiene una estructura, y esa estructura se enseña con plantilla porque a punta de buena intención no sale. Primero, se habla del código y nunca de la persona: 'el método guarda sin validar' y jamás 'usted no valida nada'. Segundo, se aporta evidencia localizable: archivo y línea, o el paso exacto para reproducirlo. Tercero, se explica el impacto, es decir qué se rompe y cuándo, porque un hallazgo sin consecuencia no convence a nadie. Cuarto, se propone una salida concreta. Compare las dos versiones. Mala: 'el manejo de errores está horrible'. Buena: 'En VentanaPrincipal.java línea 84 el catch (Exception e) está vacío; si el disco está lleno la mascota registrada se pierde y el usuario ve el mensaje de éxito igual. Sugerencia: mostrar un JOptionPane con e.getMessage() y no limpiar el formulario hasta confirmar el guardado'. La segunda se puede atender esta tarde; la primera solo produce rabia. Dos reglas más: cuando hay duda se pregunta en vez de afirmar ('¿qué pasa si el usuario deja la edad vacía?'), y cada hallazgo se etiqueta como bloqueante, mayor o menor, porque un informe con cuarenta comentarios del mismo peso no lo atiende nadie.

El checklist es lo que impide que la revisión se vuelva una conversación de gustos. Se construye directamente con los requisitos del PI de VetCare, y sus ítems son binarios y verificables: ¿existe al menos una clase del dominio con atributos privados y getters, o los datos andan sueltos en arreglos de String? ¿se usa una colección de Java para administrar las mascotas? ¿la interfaz gráfica muestra la lista y permite registrar y buscar? ¿hay try-catch en las fronteras, es decir donde entra texto del usuario y donde se toca el archivo? ¿el proyecto guarda y recupera datos de un .txt o .csv? ¿hay algún catch vacío? ¿algún método pasa de cincuenta líneas? ¿hay bloques duplicados? Cada ítem se marca cumple, no cumple o no aplica, y el 'no cumple' obliga a escribir la evidencia archivo:línea. Esto tiene tres efectos: hace comparables las revisiones entre unos y otros, evita que el revisor se quede solo con lo que le llamó la atención, y le da al autor del proyecto una lista de trabajo en vez de una sensación. El checklist no reemplaza el criterio; lo ordena, que es distinto.

Recibir la crítica también se practica, y es la mitad difícil. La reacción natural del autor es defenderse en caliente y explicar por qué lo hizo así; el protocolo de clase es otro: escuchar completo, pedir aclaración si el hallazgo no se entiende, y luego decidir con una de tres respuestas escritas: acepto y corrijo (con responsable y fecha), justifico por qué se queda como está, o difiero para después de la entrega. Todo eso queda en el plan de corrección y es lo que el docente revisa. Del lado del revisor también hay deberes: verificar antes de acusar, porque un hallazgo falso como 'esto no compila' cuando en realidad faltaba abrir el proyecto correcto quema la credibilidad de todo el informe. Hay tres antipatrones que van a aparecer y conviene nombrarlos de una vez: la revisión de sello, que aprueba en dos minutos sin haber ejecutado nada; la revisión de gusto personal, que solo señala estilo e indentación; y la revisión que rediseña el proyecto ajeno, donde el revisor propone rehacer VetCare con su propia arquitectura en vez de señalar problemas concretos del que tiene enfrente.

Error tipico del docente que no domina el tema: cree que revisar código es leer y decir si le gusta, entonces la sesión se convierte en un intercambio de opiniones sobre llaves e indentación mientras el NullPointerException sigue vivo; o peor, convierte la revisión en calificación entre estudiantes y se le arma la pelea en clase, porque nadie recibe bien que un compañero le ponga la nota. Otro error muy frecuente es no exigir que el revisor ejecute el proyecto antes de escribir: así aparecen hallazgos inventados y el autor se defiende con razón, con lo cual la actividad pierde toda autoridad. Y un tercero: no dar plantilla ni checklist, esperando que el criterio salga solo. El manejo correcto es explícito desde el minuto uno: la nota la pone el docente y el informe de quien revisa es un insumo, no una sentencia; todo hallazgo va con evidencia reproducible; se revisa el código y nunca a la persona; y el docente modela en vivo, con VetCareParaRevisar.java proyectado, cómo se reescribe un comentario agresivo en uno accionable. Un docente que nunca ha recibido una revisión de su propio código tiende a defender el suyo igual que el estudiante, y por eso conviene que empiece dejando revisar el archivo de la demo.

**Demo que usted debe poder repetir:** El docente proyecta VetCareParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta VetCareParaRevisar.java, lo ejecuta en vivo, aplica el checklist delante del grupo y reescribe dos comentarios mal formulados del tipo 'este código es un desastre' en retroalimentación accionable.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 11/Codigo/VetCareParaRevisar.java`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Intercambien proyectos: cada estudiante entrega su carpeta comprimida más un archivo de tres líneas con las instrucciones de ejecución, y recibe el proyecto de otro compañero (si el docente autorizó equipos, el de otro equipo; la revisión funciona igual); lo primero es abrirlo en NetBeans y ejecutarlo, anotando si arrancó y, si no, el mensaje de error exacto copiado tal cual.
2. Recorran el proyecto recibido con el checklist de doce ítems (clase de dominio, encapsulamiento, colección, interfaz gráfica, try-catch en fronteras, persistencia, catch vacío, métodos largos, duplicación, nombres, números mágicos, validación de casos borde) marcando cumple / no cumple / no aplica y escribiendo la evidencia archivo:línea en cada 'no cumple'.
3. Provoquen a propósito los cuatro casos borde de VetCare (edad con letras, campos vacíos, buscar un ID inexistente, borrar o dañar una línea de mascotas.csv) y registren qué hizo la aplicación en cada uno, con el texto del mensaje o de la excepción.
4. Redacten cinco hallazgos priorizados como bloqueante, mayor o menor, cada uno con el formato Evidencia + Impacto + Sugerencia, todos referidos al código y ninguno a la persona; incluyan al menos un bloqueante si existe.
5. Hagan la devolución cruzada de ocho minutos por proyecto revisado y cierren con el plan de corrección escrito por su autor: qué acepta y corrige, qué justifica y deja igual, y qué difiere, con responsable en cada línea.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Informe de revisión de una página sobre el proyecto asignado (el de otro estudiante; si el docente autorizó equipos, el de otro equipo): checklist diligenciado con evidencia archivo:línea y cinco hallazgos priorizados con formato Evidencia + Impacto + Sugerencia, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Cada estudiante recibe un informe externo con hallazgos priorizados y deja escrito su plan de corrección de VetCare antes de la integración final.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx` — no proyectar completa.
