# Solución del taller — Clase 11: Prototipo v2 con IA

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento trae el ejercicio completo del caso de la biblioteca: el prompt literal, las tres variantes, la elección, las correcciones con su origen y los descartes. Su valor está en el bloque de correcciones, donde **cada una se rastrea a una sesión anterior** — es la demostración de que el corte 2 estaba conectado. Si el docente solo alcanza a leer un bloque, que sea **LO QUE CORREGIMOS A MANO**.

**Aviso:** un asistente no devuelve dos veces lo mismo. Las variantes de este documento son representativas de lo que devuelve un prompt sin restricciones, no una transcripción a reproducir. Si lo prueba antes de clase y le devuelve otra cosa, mejor: úselo como ejemplo en vivo.

## El caso que se resuelve aquí

**La biblioteca del barrio · prototipo v2 con asistente**

Prototipo v1 de la sesión 10: tres pantallas —consultar, resultado con sus tres estados, y actualizar para la voluntaria—, con la fecha de última actualización visible. Restricciones y requisitos vigentes: sin cuenta, sin computador en el mostrador, se aprende sin manual, menos de 200 KB por consulta, alcance mínimo sin reservas ni historial. La pregunta del prototipo: *¿la voluntaria puede actualizar la lista en menos de 30 segundos sin equivocarse?*

> Porque el asistente propone cinco cosas sensatas y las cinco son incorrectas aquí, cada una por una razón que el equipo ya había escrito en una sesión distinta. Es la manera más clara de mostrar que la documentación de las sesiones 6 a 10 no era un trámite: es lo que les permite objetar a una herramienta que suena más segura que ellos.

## Consigna que se les dio

> Mejoren el prototipo con ayuda de un asistente, y dejen el rastro completo. Escriban un **prompt con contexto, restricciones y prohibiciones**, pidan **tres variantes**, elijan una **con criterio**, **corrijan a mano** lo que la IA no podía saber, y anoten **qué descartaron y por qué**.

**Entregable:** el prototipo v2 corregido (PNG en la carpeta del equipo) y el registro completo en el documento del equipo: prompt, las tres variantes, la elegida con su razón, la lista de correcciones y la de descartes · **27 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. EL PROMPT QUE USAMOS

**Se pedía:** El prompt completo, copiado tal cual. Tiene que incluir **el problema en una frase, quién lo usa, las restricciones y lo que está prohibido proponer**.

**Respuesta modelo:**

El prompt, tal cual:

> Estoy diseñando un prototipo de baja fidelidad para una biblioteca comunitaria de barrio, en un proyecto universitario de primer semestre.
>
> **Problema:** los usuarios no saben si un libro está disponible antes de ir, y hacen viajes que terminan sin préstamo (4 de cada 10 visitas).
>
> **Quiénes lo usan:** vecinos del barrio que consultan desde su celular, y voluntarias que rotan cada pocas semanas y actualizan la información al cerrar el día.
>
> **Restricciones que no se pueden cambiar:** presupuesto cero; no hay computador disponible en el mostrador durante la atención; las voluntarias rotan y no se les puede exigir capacitación larga; nadie puede atender un teléfono en horario fijo; cada consulta debe mover menos de 200 KB porque muchos usuarios tienen datos móviles limitados.
>
> **Prohibido proponer:** crear cuentas de usuario o contraseñas; pedir datos personales de cualquier tipo (correo, teléfono, documento); instalar aplicaciones; funciones de reserva o historial por usuario; imágenes.
>
> **Lo que ya tengo:** tres pantallas —consultar, resultado (disponible / prestado / no está) y actualizar para la voluntaria—, con la fecha de última actualización visible al usuario.
>
> **Lo que necesito:** dame **tres maneras distintas** de organizar la pantalla de actualización de la voluntaria para que pueda marcar un préstamo en menos de 30 segundos y sin manual. Para cada una, dime qué gana y qué pierde.

**Los cinco elementos que hacen bueno este prompt**, y que hay que señalar uno por uno: el problema con su cifra, los actores reales, las restricciones explícitas, **la lista de lo prohibido**, y una petición de tres variantes con sus contras. Nótese que todo eso ya existía escrito: el problema es de la sesión 6, las restricciones son del árbol de la sesión 6, las prohibiciones son los requisitos no funcionales de la sesión 7 más el alcance de la sesión 8 y el indicador de la sesión 5. **El prompt no se inventó hoy: se armó copiando lo ya documentado.**

**Comparación con el prompt malo**, para mostrar en clase: «mejora esta pantalla de biblioteca para que sea más fácil de usar». Devuelve la solución promedio de internet, que incluye cuentas de usuario y notificaciones por correo.

**Cómo calificar:** 20 pts. Verificación por partes: contexto y actores (5), restricciones explícitas (7), **lista de lo prohibido** (5), petición de variantes (3). El bloque de prohibiciones es el que más equipos van a omitir, y es el que evita el problema entero: si falta, muéstreles la conexión con lo que les devolvió la IA. Un prompt de dos líneas vale 5, y la conversación que sigue vale más que el descuento — dígales que su prompt malo explica por sí solo la variante mala que recibieron.

### 2. LAS TRES VARIANTES

**Se pedía:** Las tres opciones que devolvió, resumidas en dos o tres líneas cada una. **No una sola respuesta**: tres.

**Respuesta modelo:**

**Variante 1 · Lista con un botón por título.** Todos los títulos registrados en una lista; cada uno con un botón que alterna entre «Marcar prestado» y «Marcar devuelto». *Gana: un solo toque por movimiento. Pierde: si la lista crece, hay que buscar el título desplazándose.*

**Variante 2 · Buscar y marcar.** Un campo de búsqueda arriba; la voluntaria escribe el título, aparece uno solo y lo marca. *Gana: funciona con muchos títulos. Pierde: exige escribir, que es más lento y se equivoca más en un celular.*

**Variante 3 · Dos columnas: prestados y disponibles.** Los títulos repartidos en dos listas, y se mueven de una a otra al tocarlos. *Gana: se ve de un vistazo el estado completo. Pierde: en pantalla de celular las dos columnas quedan muy angostas.*

Las tres son razonables y las tres respetan las prohibiciones — porque el prompt las incluía. **Eso ya es un resultado**: la calidad de las tres variantes es consecuencia directa de la calidad del prompt, y conviene decirlo al comparar con lo que reciban los equipos que escribieron dos líneas.

**Cómo calificar:** 15 pts, 5 por variante registrada de forma comprensible. El criterio duro es que **sean tres y sean distintas**: si el equipo pidió una sola respuesta, vale 5 en total y hay que explicar por qué —una respuesta única invita a aceptarla, y aceptar no es decidir—. Valore que hayan pedido «qué gana y qué pierde» cada variante: es la matriz de la sesión 8 hecha en una línea.

### 3. LA QUE ELEGIMOS Y POR QUÉ

**Se pedía:** Cuál eligieron y el criterio, apoyado en sus **requisitos y restricciones** — no en «nos gustó más».

**Respuesta modelo:**

**Elegimos la variante 1: lista con un botón por título.**

**El criterio, apoyado en requisitos escritos antes:**

- El requisito no funcional **«se aprende en menos de cinco minutos y sin manual»** (sesión 7) favorece la que tiene menos decisiones: un toque, un cambio. La variante 2 exige escribir, y escribir en un celular con una fila de gente enfrente es donde se cometen los errores.
- El criterio de aceptación **«registra un préstamo en menos de 30 segundos»** (sesión 7) también favorece la 1: tocar es más rápido que escribir.
- La contra de la variante 1 —que la lista crezca— **no aplica en el alcance mínimo** (sesión 8), porque solo se registran los títulos que se prestan, que son pocas decenas. Si algún día crece, se agrega la búsqueda: eso queda anotado en «versión siguiente».

Nótese que la razón por la que la contra no aplica **sale de una decisión de la sesión 8**. Sin ese alcance escrito, la variante 2 habría parecido más segura, y el equipo habría elegido lo más complicado por miedo a un problema que su propio alcance ya había descartado.

**Lo que no es un criterio:** «nos gustó más», «se ve más moderna», «la IA dijo que era la mejor». La última es la más peligrosa de las tres, porque suena a argumento.

**Cómo calificar:** 20 pts. Una sola verificación: **¿el criterio se rastrea a un requisito o restricción escrito antes de hoy?** Si sí, 20. Si es «nos gustó más» o «se ve mejor», 6. Y si es **«la IA recomendó esta»**, vale 0 en este bloque y hay que decir por qué en voz alta: la recomendación de la herramienta no es un criterio del equipo, es la ausencia de criterio con buena redacción.

### 4. LO QUE CORREGIMOS A MANO

**Se pedía:** Cada corrección con **la razón y la sesión de donde sale**: qué proponía la IA, qué quedó, y por qué. Es el bloque que más pesa.

**Respuesta modelo:**

Las correcciones, cada una con su razón **y la sesión de donde sale** — este es el bloque que hay que leer en voz alta en clase:

**1 · Quitamos la pantalla de ingreso con contraseña para la voluntaria.** El asistente la agregó igual, pese a la prohibición, «para proteger la lista». *Razón:* el requisito no funcional «se aprende sin manual» y la rotación de voluntarias hacen inviable administrar contraseñas — y pedir un correo para recuperarla sería recolectar datos personales. **Sesiones 7 y 4 (Ley 1581 de 2012).** *Cómo lo resolvimos en su lugar:* la pantalla de actualización vive en un enlace distinto que solo se comparte con las voluntarias. No es seguridad fuerte, y lo anotamos como limitación conocida en el informe.

**2 · Quitamos el campo «nombre de quien presta».** *Razón:* es un dato personal y no hace falta para el requisito —el usuario solo necesita saber si está o no está—. **Sesión 4.** *En su lugar:* el estado es «prestado», sin decir a quién.

**3 · Cambiamos «Fecha de vencimiento: 12/09» por «Se esperaba de vuelta el lunes».** *Razón:* lenguaje de persona y no de sistema, y además admite que es una expectativa. **Sesión 10 (textos reales).**

**4 · Agregamos la fecha de última actualización, que la variante había eliminado.** *Razón:* es la manera de ser honestos con el sacrificio aceptado al decidir —la información no está al minuto—. **Sesiones 8 y 10.** Sin esa línea, la solución miente por omisión.

**5 · Reescribimos «No se encontraron resultados» por «No encontramos «X» en la lista. Pregunte en el mostrador o intente con el autor».** *Razón:* un mensaje de error tiene que decir qué hacer. **Sesión 10.**

**6 · Quitamos los íconos de colores de cada título.** *Razón:* suben el peso de la página y el límite es 200 KB por consulta. **Sesión 5.**

**El hallazgo, y la lección de cierre del corte:** las seis correcciones salen de cinco sesiones distintas, y **ninguna se podía hacer sin tener esas decisiones escritas**. Un equipo sin requisitos no funcionales, sin alcance definido y sin indicador ambiental habría aceptado las seis propuestas, todas razonables en abstracto. El corte 2 no fue documentar por documentar: fue construir el criterio con el que hoy se objeta a una herramienta que suena más segura que uno.

**Cómo calificar:** 30 pts, el bloque que decide la nota. 5 pts por corrección con **razón explícita**, hasta 30; sin razón, 2 pts cada una. Valore el doble —dígalo en la retroalimentación— a las correcciones que **citan la sesión de origen**: es la señal de que el estudiante está acumulando y no empezando de cero. Y atención al caso crítico: si un equipo dice **«no corregimos nada, quedó perfecto»**, revíselo delante de ellos contra sus propios requisitos no funcionales. Siempre hay algo, y encontrarlo juntos enseña más que el descuento. Si de verdad no hay nada que corregir, casi siempre significa que el prompt era tan detallado que el equipo ya había hecho todo el trabajo — dígalo, es un resultado válido y bueno.

### 5. LO QUE DESCARTAMOS Y POR QUÉ

**Se pedía:** Las propuestas que se rechazaron completas, y el motivo: fuera del alcance, viola una restricción, viola la ley, o consume demasiado.

**Respuesta modelo:**

Propuestas rechazadas completas, con motivo verificable:

- **Avisos automáticos por correo cuando el libro se devuelva.** *Motivo:* exige pedir el correo del usuario, es decir recolectar datos personales, con todo lo que eso implica en autorización, finalidad y custodia. **Ley 1581 de 2012 · sesión 4.** Y además nadie en la biblioteca puede responder por esos datos.
- **Sistema de reservas con historial por usuario.** *Motivo:* quedó explícitamente fuera del alcance mínimo y está en la lista de «versión siguiente». **Sesión 8.** No es una mala idea: es una idea para otro semestre.
- **Imágenes de portadas para reconocer los libros.** *Motivo:* rompe el límite de 200 KB por consulta, que es un requisito no funcional derivado del indicador ambiental. **Sesiones 5 y 7.**
- **Estadísticas de los libros más prestados.** *Motivo:* interesante y fuera del problema; el problema es el viaje en vano. **Frontera de la sesión 6.** Anotado como idea para el informe final, no para el prototipo.

**Y la declaración del uso**, que va en el documento del equipo y en el informe final:

> *Para la pantalla de actualización se usó un asistente de IA (nombre y versión, fecha) pidiendo tres variantes de organización. Se eligió una y se le hicieron seis correcciones, documentadas arriba. Se descartaron cuatro propuestas por violar restricciones del proyecto o la Ley 1581 de 2012. No se le entregó ningún dato personal ni información de la biblioteca distinta de la ya publicada en este documento.*

Esa última frase importa y hay que señalarla: **la trazabilidad incluye decir qué NO se le entregó a la herramienta.**

**Cómo calificar:** 15 pts. Se califica que cada descarte tenga un **motivo verificable** —fuera del alcance, viola una restricción, viola la ley, consume demasiado— y no una impresión (10 pts), y que exista la **declaración del uso** con asistente, fecha y qué se aceptó y descartó (5 pts). Un equipo que descarta diciendo «no nos convenció» vale 4. Y valore que digan qué **no** le entregaron al asistente: es el nivel de trazabilidad que se espera en un entorno profesional.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| El prompt incluye el problema, los actores, las restricciones y lo prohibido | **20 %** | Sin contexto la IA devuelve la solución promedio de internet, que no es la del proyecto. |
| Se pidieron y se registraron tres variantes distintas | **15 %** | Una sola respuesta invita a aceptarla; tres obligan a comparar, y comparar es el trabajo del ingeniero. |
| La variante elegida se justifica con un requisito o restricción escrito antes | **20 %** | Es la matriz de decisión de la sesión 8 aplicada a lo que devuelve una herramienta. |
| Hay al menos tres correcciones a mano, cada una con su razón y su origen | **30 %** | Es la prueba de que el equipo ejerció criterio: lo que se califica no es la variante, es la corrección. |
| Se declara qué se descartó y por qué, con motivo verificable | **15 %** | Declarar el uso y los límites de una herramienta es la práctica profesional; esconderlo es la falta. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Equipos que dicen «no corregimos nada, quedó perfecto».** Es la señal más clara de que aceptaron sin leer. No lo discuta: abra su lista de requisitos no funcionales y revise la variante contra ella, punto por punto, delante de ellos. En dos minutos aparece algo — casi siempre un dato personal, un texto de sistema o un elemento que pesa. Encontrarlo juntos enseña la sesión entera. Si de verdad no hay nada, felicítelos: significa que su prompt era tan bueno que ya habían hecho el trabajo, y eso también hay que reconocerlo.

**Equipos sin acceso a un asistente o que se quedan sin cupo gratuito.** Pasa y no puede costarle la nota a nadie. Dos salidas: que trabajen con el asistente de un compañero del equipo compartiendo pantalla —es trabajo en equipo, no copia—, o que hagan el ejercicio con **las variantes de este documento de solución** como si las hubiera devuelto un asistente, declarándolo así. Lo que se califica es el criterio con el que corrigen, y eso se puede evaluar igual. **Ningún estudiante tiene que pagar por nada.**

**Equipos que le pasaron datos reales al asistente.** Ocurre sin mala intención: el nombre de la coordinadora, la dirección de la biblioteca, un teléfono de contacto. Hay que decirlo sin dramatizar y con precisión: **lo que se escribe ahí salió del computador y no vuelve.** No hay manera de deshacerlo, así que la corrección es hacia adelante — que lo declaren en el registro y que no vuelva a pasar. Es exactamente la sesión 4 ocurriendo en vivo, y como lección vale más que cualquier advertencia previa.

**Proyectos de proceso o gestión, sin pantallas.** El ejercicio es idéntico cambiando el objeto: se piden **tres maneras distintas de organizar el formato o la secuencia de pasos**. El asistente es especialmente útil aquí para pedir **casos que no se previeron** —«¿qué pasa si el paso 2 se hizo pero el 1 no?»—, y esa lista es un insumo directo para la prueba de la sesión 12.

## Errores que hay que ver y no dejar pasar

- **«Mejora esta pantalla de biblioteca para que sea más fácil de usar»** → Sin contexto ni restricciones devuelve la solución promedio de internet, que incluye cuentas de usuario y notificaciones por correo. El problema en una frase, los actores, las restricciones y **la lista de lo prohibido**. Todo eso ya lo tienen escrito de las sesiones 6, 7 y 8.
- **«La IA dijo que esta era la mejor opción»** → La recomendación de la herramienta no es un criterio del equipo: es la ausencia de criterio con buena redacción. El requisito o la restricción en la que se apoya la elección. Si no hay ninguno, todavía no eligieron.
- **«No corregimos nada, quedó perfecto»** → Significa que aceptaron sin revisar. Revisado contra los propios requisitos no funcionales, siempre aparece algo. Revisar la variante punto por punto contra su lista de requisitos, delante de usted. Aparece en dos minutos.
- **Datos reales de personas escritos en el prompt** → Lo que se escribe ahí sale del computador y no vuelve: es tratamiento de datos personales sin autorización. Que lo declaren en el registro y que en adelante usen roles y datos inventados. La corrección es hacia adelante.
- **Un registro escrito al final, de memoria** → Las correcciones y sus razones se olvidan en minutos, y sin razones el bloque de 30 puntos no se puede calificar. Que una persona del equipo escriba el registro **mientras** los otros corrigen. Si se deja para el final, no se hace.

## Cierre: qué decir en los 3 minutos finales

Tres minutos, y hay dos cosas que decir. La primera es la idea del corte: **el equipo pudo corregir al asistente porque tenía sus decisiones escritas.** Las seis correcciones del caso modelo salen de cinco sesiones distintas —el requisito sin cuenta de la 7, la Ley 1581 de la 4, el alcance de la 8, el indicador de la 5, los textos reales de la 10— y ninguna se podía hacer sin ese material. Dígalo con estas palabras, porque es la respuesta a la pregunta que todos se hacen en primer semestre: documentar no fue un trámite, fue construir el criterio con el que hoy se le objeta a una herramienta que suena más segura que uno. La segunda es operativa: recuerde que la evaluación del corte 2 viene inmediatamente después de las exposiciones, en ExamLab, individual y a libro abierto sobre sus propios documentos — que sea a libro abierto premia exactamente al equipo que documentó—. Y anuncie el corte 3, que empieza con la sesión 12: el prototipo se prueba **con una persona ajena al equipo**, y es la única retroalimentación gratis del semestre.

## Con qué se conecta

Hacia atrás: la **sesión 10** dejó el prototipo que hoy se mejora; la **sesión 8** dejó el alcance que descarta la mitad de las propuestas; la **sesión 7** dejó los requisitos no funcionales que se copian en el prompt; la **sesión 5** dejó el límite de datos; la **sesión 4** dejó la Ley 1581, que hoy se aplica dos veces; la **sesión 3** dejó la regla de entregar el prompt y las correcciones. Hacia adelante: la **sesión 12** prueba este prototipo v2 con una persona ajena; la **sesión 13** evalúa el impacto social y ambiental de la solución; la **sesión 14** sube la fidelidad para la presentación; y el **informe final de la sesión 16** incluye la declaración del uso de IA que hoy quedó escrita.
