# Solución del taller — Clase 3: Anatomía del sistema

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento resuelve el taller completo sobre un sistema concreto —el de préstamo de libros de una biblioteca de barrio— y muestra además **una respuesta real de asistente de IA con sus errores señalados**, que es la parte que el docente necesita tener lista: sin un ejemplo de cómo se ve una corrección bien hecha, los equipos entregan «la IA se equivocó en varias cosas» y no hay con qué calificar.

## El caso que se resuelve aquí

**Sistema de préstamo de una biblioteca de barrio**

El auxiliar anota los préstamos en un cuaderno: nombre, libro y fecha. No hay registro de devoluciones aparte de tachar el renglón. Cuando alguien pregunta si un libro está disponible, el auxiliar va al estante a mirar. En el último año **se perdieron dos cajas de libros** y nadie sabe quién los tenía. Es el mismo caso que se usa en la solución de la sesión 1, a propósito: permite ver cómo el mismo problema se ve distinto cuando se le aplica una herramienta nueva.

> Se eligió porque tiene los cinco elementos visibles, tiene un actor no-usuario claro (quien nunca encuentra el libro porque está prestado y no figura) y su retroalimentación **no existe**, que es el hallazgo más frecuente y el más rentable.

## Consigna que se les dio

> Tomen **el problema del entorno que su equipo escribió en la sesión 1** y descríbanlo como sistema, con los cinco pasos del método. Úsenlo así: primero lo piensan ustedes, después le piden al asistente de IA que lo complete, y por último **corrigen a mano lo que la IA se inventó**. Lo que se califica es la corrección, no el texto.

**Entregable:** una ficha de sistema de cinco bloques en el documento del equipo, con el prompt usado y una lista de las correcciones hechas a la respuesta de la IA · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. PROPÓSITO Y FRONTERA

**Se pedía:** Para qué existe el sistema, en una frase. Y qué queda **dentro** y qué **fuera** de él, con la razón de cada exclusión importante.

**Respuesta modelo:**

**Propósito:** que los libros de la biblioteca lleguen a quien los necesita y vuelvan al estante.

**Dentro de la frontera:** el estante y su contenido, el cuaderno de préstamos, el auxiliar, el lector que pide, el acto de entregar y el de devolver.

**Fuera de la frontera, con su razón:** (a) la **compra** de libros nuevos, porque depende de un presupuesto que la biblioteca no maneja y mejorarla no reduce las pérdidas; (b) el **estado físico** del libro (páginas rotas), porque es un problema real pero distinto y meterlo obligaría a un inventario de condición que no cabe en un semestre; (c) el **transporte** del lector, porque aquí —a diferencia del caso de las citas médicas— la biblioteca es del barrio y la distancia no explica ninguna pérdida.

**Lo que se discutió y se decidió dejar DENTRO:** el lector que no devuelve. Es tentador dejarlo fuera («eso es un problema de las personas, no del sistema»), pero si se deja fuera desaparece el problema que se quería resolver.

**Cómo calificar:** 20 pts. Lo que se califica es que **haya exclusiones con razón**, no cuáles. Un equipo que excluya el estado físico del libro explicando por qué está bien; un equipo que escriba «dentro: todo lo de la biblioteca» vale 5. La discusión sobre si el lector que no devuelve entra o sale es la señal de que el equipo entendió que la frontera es una decisión: si aparece, dé los 20 completos.

### 2. ENTRADAS, PROCESO Y SALIDAS

**Se pedía:** Qué entra, qué se hace con eso y qué sale. Señalen **dónde está el software**, si hay.

**Respuesta modelo:**

**Entradas:** la solicitud de préstamo (un lector que llega y pide un título), el libro devuelto, y el catálogo de lo que existe en el estante.

**Proceso:** el auxiliar busca físicamente en el estante; si está, anota nombre, libro y fecha en el cuaderno y entrega; cuando el libro vuelve, tacha el renglón y lo devuelve al estante.

**Salidas:** el libro en manos del lector, el renglón en el cuaderno y —esto es lo que hay que notar— **ninguna información utilizable**: el cuaderno no permite responder «¿qué libros están afuera hoy?» sin leerlo página por página.

**Dónde está el software:** hoy **no hay**. Y esto es importante para el curso: el sistema existe, funciona a medias y no tiene una línea de código. Si se introdujera software, iría en un solo punto del proceso —el registro del préstamo y la consulta de disponibilidad—, no en todo el sistema. El acto de buscar el libro, entregarlo y recibirlo sigue siendo humano y físico.

**Cómo calificar:** 15 pts. El punto que decide es el último: **el software ubicado como una parte del proceso**. Un equipo que escriba «el proceso es un sistema de gestión de biblioteca» no entendió la sesión y vale 5. Un equipo que diga «hoy no hay software y el sistema igual existe» vale los 15 completos, porque es exactamente la idea de la clase.

### 3. LOS ACTORES

**Se pedía:** Todos los afectados, con su rol y qué le importa a cada uno. Incluyan **al menos uno que no use el sistema pero sí sufra el resultado**.

**Respuesta modelo:**

**El lector que pide** (le importa encontrar el libro y llevárselo rápido). **El auxiliar** (le importa no equivocarse y no pasar la tarde buscando en el estante; hoy hace trabajo doble). **Quien responde por el inventario** —la coordinación de la biblioteca— (le importa que no se pierdan libros, porque reponerlos cuesta y a veces no se puede).

**El actor no-usuario, que es el que se olvida:** el lector que llega, pregunta por un libro, el auxiliar mira el estante y no lo encuentra, y se va con la idea de que **la biblioteca no tiene ese libro**. En realidad el libro existe y está prestado, pero como el cuaderno no se consulta hacia atrás, nadie puede decirle «vuelva el jueves». Esa persona no usa el sistema de préstamo —nunca llega a firmar el cuaderno— y es la más perjudicada: pierde el acceso y además se lleva una idea falsa del inventario.

**Un segundo no-usuario, si el equipo lo encuentra:** quien donó libros a la biblioteca y ve que se pierden.

**Cómo calificar:** 25 pts. La mitad depende del no-usuario. «El lector» genérico no cuenta como no-usuario: hay que nombrar a alguien que **queda fuera del sistema y sufre el resultado**. Si el equipo describe al lector que se va creyendo que el libro no existe, dé los 25: es el mejor hallazgo posible en este caso. Si solo lista lector, auxiliar y coordinación, 12.

### 4. LA RETROALIMENTACIÓN

**Se pedía:** ¿Cómo se entera este sistema de que algo salió mal? Si no se entera, escríbanlo: es un hallazgo, no un error suyo.

**Respuesta modelo:**

**No hay.** Esta es la respuesta correcta y hay que decirlo así. El sistema no tiene ninguna manera de enterarse de que algo salió mal: un libro que no volvió no dispara nada, porque el renglón sin tachar solo se ve si alguien se pone a revisar el cuaderno hacia atrás, y nadie lo hace. Las dos cajas perdidas en un año son la consecuencia directa: no se perdieron de golpe, se fueron perdiendo de uno en uno sin que nada avisara.

**Y de ahí sale la mejor oportunidad de mejora, que además es barata:** cualquier mecanismo que convierta «renglón sin tachar» en un aviso. Puede ser software, pero también puede ser una hoja aparte con los préstamos vencidos que el auxiliar revise los viernes. Que la solución más obvia no requiera programar es un buen argumento para una clase de primer semestre.

**Cómo calificar:** 10 pts (dentro del bloque de actores/retroalimentación según su reparto). «No hay retroalimentación» **es la respuesta completa** si viene con la consecuencia (las cajas perdidas). Si el equipo escribe «la retroalimentación es que el auxiliar se da cuenta», pregunte cómo se da cuenta: ahí se cae solo.

### 5. LA IA: PROMPT Y CORRECCIONES

**Se pedía:** El prompt exacto que usaron, y una lista de **al menos tres cosas que la IA escribió mal** y cómo las corrigieron.

**Respuesta modelo:**

**Prompt de ejemplo (aceptable):** «Describe como sistema el préstamo de libros de una biblioteca de barrio donde los préstamos se anotan en un cuaderno. Dame entradas, proceso, salidas, actores y retroalimentación.»

**Lo que un asistente típicamente devuelve y hay que corregir:**

**(1) Cifras inventadas.** Escribe cosas como «en promedio se pierde el 5 % del inventario anual» o «el tiempo de búsqueda es de 3 a 5 minutos». **Corrección:** ese dato no existe para esta biblioteca. Lo único que se sabe es lo observado: dos cajas en un año. Se borra el porcentaje y se deja el dato real.

**(2) Software que no existe.** Suele describir el proceso como si hubiera un sistema de gestión, con «registro en la base de datos» y «consulta al catálogo digital». **Corrección:** aquí el registro es un cuaderno de papel y el catálogo es el estante. Es el error más importante de detectar, porque es justo la confusión de la clase de hoy: la IA asume software donde no hay.

**(3) Normas o instituciones inventadas.** Puede citar una ley o un reglamento de bibliotecas públicas colombianas con número y año. **Corrección:** se elimina lo que no se pueda verificar en la fuente original. No se «arregla» una cita: se quita.

**(4) Actores genéricos, sin el no-usuario.** Lista «usuarios, personal y administración». **Corrección:** se reemplaza por roles concretos y se agrega el lector que se va creyendo que el libro no existe, que la IA casi nunca propone porque no está en la descripción que se le dio.

**(5) Retroalimentación optimista.** Suele afirmar que «el sistema se retroalimenta con el registro de devoluciones». **Corrección:** el registro existe pero **nadie lo lee hacia atrás**, así que no hay retroalimentación. La IA describe el sistema como debería ser, no como es.

**Cómo calificar:** 30 pts, el bloque que decide la nota. Exija **tres correcciones con su razón**. Vale más una corrección profunda (la (2) o la (5)) que tres cosméticas de redacción. Si el equipo entrega el texto de la IA sin correcciones, 0 en este bloque, y dígaselo en voz alta con el argumento correcto: no es castigo por usar la herramienta, es que sin verificación no hay nada de ingeniería que calificar. **Corrección de tipo (1) o (3) —cifra o norma inventada— cuenta doble**: es la falla que más daño hace en un trabajo profesional.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| La frontera está definida con al menos una exclusión justificada | **20 %** | Sin frontera defendible, el proyecto del semestre no cabe en un semestre. |
| Entradas, proceso y salidas, con el software ubicado como una parte | **15 %** | Es la verificación de que entendieron que el sistema no es el software. |
| Hay un actor afectado que no usa el sistema | **25 %** | Es el actor que se olvida siempre y el que más problemas causa. Alimenta la sesión 13. |
| Las tres correcciones a la IA, con su razón | **30 %** | Es el criterio propio de esta sesión: verificar en vez de copiar. Sin esto no hay trabajo de ingeniería que evaluar. |
| La exposición cupo en 3 min e incluyó el minuto de la IA | **10 %** | El minuto de la IA es obligatorio: es lo que distingue esta exposición de un resumen teórico. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Si el equipo trabaja un sistema de citas o turnos.** El no-usuario es quien deja de conseguir cita porque otro madrugó, o quien no puede madrugar. La frontera se discute en el transporte. La retroalimentación suele existir a medias: se enteran cuando alguien reclama, que es tarde y sesgado (solo reclaman algunos).

**Si el equipo trabaja un sistema de ventas o inventario de un negocio.** El no-usuario es el cliente que se fue porque le dijeron que no había producto cuando sí había. La frontera se discute en el proveedor. La retroalimentación casi siempre es el conteo físico de fin de mes, que detecta el problema treinta días tarde: ese retardo es el hallazgo.

**Si el equipo trabaja un sistema de transporte o rutas.** El no-usuario es el vecino que sufre el tráfico sin usar el servicio. La frontera se discute en el andén y el paradero. Cuidado con las cifras: es el caso donde la IA inventa más datos de tiempos y frecuencias, así que es el mejor para el bloque de correcciones.

**Si el equipo trabaja un sistema académico de la propia universidad.** Está permitido y funciona bien porque lo conocen de primera mano, pero **sin nombres de funcionarios**: se usa el rol. El no-usuario suele ser el aspirante que no alcanzó a matricularse. La retroalimentación es el punto fuerte: casi siempre existe un canal de reclamos y casi nunca cambia el proceso, lo que permite hablar de retroalimentación que no retroalimenta.

## Errores que hay que ver y no dejar pasar

- **«El sistema es la app / la plataforma»** → Confunde el sistema con una de sus partes; es la falla que la clase entera ataca. Que señalen dónde está el software DENTRO del proceso, y qué partes del sistema no son software.
- **«Los usuarios» como actor** → No es un rol: no dice qué le importa a quién ni permite encontrar al perjudicado. Roles concretos y, obligatorio, uno que no use el sistema y sí sufra el resultado.
- **«Dentro de la frontera: todo lo relacionado»** → Una frontera sin exclusiones no es una frontera, y produce proyectos que no se acaban. Una cosa que dejen fuera a propósito, con la razón escrita.
- **«La retroalimentación es que el usuario se queja»** → Es tardía y sesgada: solo se queja una parte, y ya pasó el daño. Cómo se enteraría el sistema ANTES de que alguien reclame. Si no hay manera, que lo escriban: es un hallazgo.
- **Un dato con cifra que salió de la IA** → El asistente inventa cifras locales con total naturalidad y sin avisar. La fuente. Si salió de la IA, que lo borren y lo anoten como corrección: eso es lo que se califica.

## Cierre: qué decir en los 3 minutos finales

Tres minutos, una idea: **el sistema no es el software.** Muéstrelo con el caso de la biblioteca, que es un sistema completo sin una línea de código, y con el de la app de citas impecable junto a la fila que no se movió. Enuncie el criterio de éxito del curso con esas palabras: un proyecto de aquí se juzga por si **el problema del entorno se redujo y se puede medir**, no por si el prototipo funciona. Y cierre con lo de la IA, que es la idea que se llevan para el semestre: la herramienta solo se puede verificar si uno sabe del tema, así que no reemplaza aprender el contenido — lo vuelve más necesario. Anuncie la sesión 4: hoy vimos que un sistema puede funcionar y ser injusto; la próxima, qué responsabilidad tiene el ingeniero cuando eso pasa.

## Con qué se conecta

Hacia atrás: la sesión 1 dejó el problema del entorno y la sesión 2 mostró que los proyectos fracasan por no entenderlo. Hacia adelante: la frontera y los actores de hoy son dos de los cinco campos de la ficha del problema que se entrega en la **sesión 6** (cierre del corte 1); el actor no-usuario es el insumo directo de la **sesión 13** (impacto social y ambiental); y el uso declarado de IA se vuelve a exigir, con más nivel, en la **sesión 11**.
