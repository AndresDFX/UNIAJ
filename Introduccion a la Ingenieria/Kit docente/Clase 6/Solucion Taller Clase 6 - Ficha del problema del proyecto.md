# Solución del taller — Clase 6: Ficha del problema del proyecto

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento trae la ficha completa del caso de la biblioteca —el mismo que se usó en las sesiones 1 y 3, para que se vea el problema madurar— y al final las claves de los cuatro tipos de proyecto frecuentes. Es la solución más importante del corte, porque lo que se escriba hoy gobierna diez sesiones más. Si el docente solo alcanza a leer dos bloques antes de clase, que sean **LA LÍNEA BASE** y **EL CRITERIO DE ÉXITO**: son los dos que casi ningún equipo hace bien solo.

## El caso que se resuelve aquí

**La biblioteca del barrio · ficha del problema completa**

La biblioteca comunitaria de un barrio presta libros con un cuaderno. Atiende de lunes a sábado con dos personas voluntarias que rotan. Los usuarios son sobre todo estudiantes de colegio y de universidad del sector. La coordinadora dice que «se pierden libros» y que «la gente se queja». Es el mismo caso de las sesiones 1 y 3: hoy se le exige lo que en la sesión 1 todavía no se sabía pedir.

> Se mantiene el caso de las sesiones 1 y 3 a propósito. En la sesión 1 el problema se enunció como «falta un sistema para la biblioteca»; en la 3 apareció que el sistema es el proceso de préstamo y no el software; hoy queda escrito como un problema medible. Mostrar esa progresión en tres versiones de la misma frase es la lección de la sesión.

## Consigna que se les dio

> Cierren el problema del proyecto del semestre. Cinco bloques: el problema en **una frase**, la **línea base** con una cifra, el **árbol de causas** en Excalidraw, los **actores y la frontera**, y un **criterio de éxito medible**. Esta ficha es el entregable del corte 1 y gobierna el resto del semestre.

**Entregable:** la ficha de cinco bloques en el documento del equipo, más el árbol de causas en Excalidraw exportado a PNG en la carpeta del equipo · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. EL PROBLEMA EN UNA FRASE

**Se pedía:** Una sola frase con la fórmula: **a quién le pasa qué, con qué consecuencia**. Sin mencionar ninguna tecnología ni ninguna solución.

**Respuesta modelo:**

**Versión final (la que se acepta):**

> «Los usuarios de la biblioteca no pueden saber si un libro está disponible antes de ir, así que hacen viajes que terminan sin préstamo; de cada 10 visitas, unas 4 salen sin el libro que buscaban.»

**Por qué esta funciona:** dice a quién le pasa (los usuarios), qué le pasa (no pueden saber la disponibilidad antes de ir), con qué consecuencia (viajes en vano), y trae una cifra. **No menciona ninguna tecnología**, y eso es lo que deja abierto el diseño: se podría resolver con una lista publicada, con un número de WhatsApp o con una aplicación. Que haya varias soluciones posibles es la prueba de que el problema está bien escrito.

**La progresión, que vale mostrarla en pantalla:**

1. Sesión 1: «Falta un sistema para la biblioteca del barrio.» → solución disfrazada.
2. Sesión 3: «El proceso de préstamo no tiene registro confiable de qué está prestado.» → mejor, pero sigue siendo una causa, no el problema del usuario.
3. Sesión 6: la versión final de arriba. → problema del actor, con consecuencia y cifra.

**Enunciados que se rechazan y por qué:** «se pierden libros» (síntoma, y además es el problema de la coordinadora, no del usuario — puede ser un segundo problema, no este); «la biblioteca no está digitalizada» (juicio con solución adentro); «los usuarios necesitan una app de consulta» (solución disfrazada).

**Cómo calificar:** 25 pts. Dos verificaciones mecánicas y rápidas: (a) **busque la palabra «app», «sistema», «plataforma» o «digital» en la frase**; si aparece, máximo 10; (b) pregúntese si se entiende **a quién le cuesta qué**; si el sujeto es «la biblioteca» o «el barrio», máximo 12, porque falta la persona. Los 25 son para la fórmula completa con consecuencia. No exija elegancia: exija estructura.

### 2. LA LÍNEA BASE

**Se pedía:** Una cifra que describa el problema **hoy**, antes de que ustedes toquen nada, más **cómo la obtuvieron** y cuándo. Si es estimación, escriban «estimado».

**Respuesta modelo:**

**Cifra:** «De cada 10 visitas, unas 4 terminan sin el libro buscado.»

**Método:** *un conteo hecho por el equipo durante seis días de atención, preguntando a la salida a cada persona que salió sin libro si el que buscaba estaba disponible. Se contaron 63 visitas, 26 salieron sin préstamo por indisponibilidad. Datos tomados en la semana del …*

**Segunda cifra útil, más fácil de conseguir:** «La coordinadora estima que responde entre 15 y 20 llamadas semanales preguntando por disponibilidad» — marcada explícitamente como **estimación de la coordinadora**, no como medición.

Las dos son aceptables y la diferencia hay que enseñarla: la primera es una **medición** con método declarado; la segunda es una **estimación de un informante**, igual de legítima si se dice qué es y de quién viene. Lo que no es aceptable es una cifra sin origen.

**Cómo se consigue esto sin presupuesto, que es la pregunta real de los equipos:** tres preguntas a la persona que hace el trabajo, un conteo de una semana con una hoja, o el tiempo de un caso medido con el cronómetro del celular. Nada de esto necesita permiso institucional ni encuesta científica.

**Cómo calificar:** 25 pts, y es el bloque donde se cae la mayoría. Tres requisitos: **número, unidad y método**. Sin método, máximo 10, sin importar lo verosímil que suene la cifra — y dígalo con el argumento, porque es la lección: una cifra sin origen no se puede volver a medir en la Clase 16, así que no sirve. Una estimación bien declarada («estimado por la coordinadora») vale los 25 completos: se califica la honestidad del método, no la precisión.

### 3. EL ÁRBOL DE CAUSAS

**Se pedía:** En Excalidraw: el problema en el tronco, los efectos arriba, dos o tres causas directas abajo y el segundo nivel de cada una. Marquen con un símbolo las causas que **no** pueden cambiar (restricciones).

**Respuesta modelo:**

**TRONCO:** los usuarios no pueden saber si un libro está disponible antes de ir.

**EFECTOS (arriba):** viajes en vano · los usuarios dejan de ir y usan otras fuentes · la coordinadora pierde tiempo respondiendo llamadas · la percepción de que «la biblioteca no sirve».

**CAUSAS DIRECTAS (abajo):**

1. **No existe un registro consultable de qué está prestado.**
2. **No hay ningún canal para preguntar antes de ir**, salvo llamar cuando hay quien contesta.

**SEGUNDO NIVEL:**

- De la causa 1: el préstamo se anota en un cuaderno que está en el mostrador y solo se puede consultar ahí · rotan dos voluntarias y cada una anota distinto · las devoluciones se anotan al final del día, cuando hay tiempo.
- De la causa 2: el teléfono de la biblioteca es el celular personal de la coordinadora y no siempre está atendido · no hay horario declarado de atención telefónica.

**RESTRICCIONES marcadas (lo que el equipo NO puede cambiar):** el presupuesto de la biblioteca es cero · las voluntarias rotan y no se les puede exigir capacitación larga · no hay computador disponible en el mostrador durante la atención · no se puede pedir que alguien atienda un teléfono en horario fijo.

**La causa que se ataca:** la 1, y dentro de ella el segundo nivel «el registro solo se puede consultar en el mostrador». Es la que tiene mayor efecto y la única que no depende de conseguir tiempo de una persona. Y nótese que las restricciones **no bloquean el proyecto: lo delimitan** —obligan a que la solución funcione sin computador en el mostrador y sin capacitación larga, lo cual es información de diseño valiosísima que aparece en la sesión 7.

**Cómo calificar:** 20 pts. Requisitos: **dos niveles de causas** (10 pts) y **al menos una restricción marcada** (10 pts). El error a corregir en vivo es el árbol con ocho o diez raíces sin jerarquía: eso es una lista, no un análisis, y vale 8. El segundo error es poner efectos entre las causas —«la gente se queja» abajo—; señálelo señalando el dibujo, es la manera más rápida de que se entienda. Si el equipo marca restricciones **y** explica cómo delimitan la solución, está haciendo ingeniería de verdad.

### 4. ACTORES Y FRONTERA

**Se pedía:** Quién vive el problema (el dueño del problema), quién más se afecta sin ser usuario, y qué queda **fuera** de lo que ustedes van a abordar. Digan además **a quién le pueden preguntar algo esta semana**.

**Respuesta modelo:**

**Dueño del problema:** los usuarios que van a buscar un libro concreto, sobre todo los estudiantes de colegio con tarea para el día siguiente. Son quienes reconocerían la mejora de inmediato.

**Actor con quien se puede hablar esta semana:** la coordinadora de la biblioteca, y dos o tres usuarios en la puerta un sábado. Sin trámites, sin permisos. **Este es el criterio que decide si el proyecto es real.**

**Afectado que no es usuario** (viene de la sesión 3): las voluntarias, que van a tener que usar lo que el equipo construya y que no pidieron nada. Si la solución les agrega trabajo, no se va a usar, y el proyecto fracasa aunque funcione. Es el mismo punto de la sesión 4: hay un afectado que no está en la reunión.

**Frontera — lo que queda FUERA, declarado explícitamente:**

- La pérdida de libros y el cobro de multas: es otro problema, con otro dueño (la coordinadora). No se aborda.
- La catalogación completa del acervo: no cabe en un semestre.
- La compra de libros o de equipos: presupuesto cero, es restricción.
- La reserva de libros en línea: se deja fuera de esta primera versión porque exige que alguien atienda las reservas, y eso choca con la restricción de personal.

Declarar lo que queda fuera es lo que evita que el proyecto crezca sin control en la sesión 10, cuando aparezcan las ganas de agregarle funciones.

**Cómo calificar:** 15 pts. Lo que se califica de verdad es **el actor con quien se puede hablar esta semana** (8 pts): si el equipo no puede nombrarlo, el proyecto no es viable y hay que rediseñarlo hoy, no en la sesión 10. Los otros 7 son por la frontera declarada; un equipo que no deja nada fuera no ha delimitado. Si aparece el afectado no-usuario —las voluntarias— súbale: significa que la sesión 3 quedó aprendida.

### 5. EL CRITERIO DE ÉXITO

**Se pedía:** Una frase de la forma: «el proyecto sirvió si <la cifra de la línea base> pasa de X a Y, medido así». Y la causa del árbol que van a atacar.

**Respuesta modelo:**

**Criterio:** «El proyecto sirvió si las visitas que terminan sin el libro buscado bajan de 4 de cada 10 a menos de 2 de cada 10, medido con el mismo conteo de seis días a la salida de la biblioteca.»

**Causa atacada:** la 1 — que el registro solo se puede consultar en el mostrador.

**Por qué este criterio funciona:** usa **la misma medición** de la línea base, así que es comparable; tiene un valor de partida y uno de llegada; y se puede ejecutar en la Clase 16 con lo que el equipo tiene. Nótese que no promete cero: prometer la eliminación total del problema es una señal de que el equipo no lo entendió.

**Criterio secundario, más barato de verificar:** «la coordinadora puede decir qué está prestado sin abrir el cuaderno, en menos de 30 segundos». Es un sí/no cronometrable y sirve como verificación intermedia en la Clase 12.

**Criterios que se rechazan:** «que la biblioteca funcione mejor» (no medible); «que el 100 % de los usuarios encuentren su libro» (imposible: algunos libros simplemente están prestados); «que la app tenga 200 usuarios» (mide adopción de la solución, no la resolución del problema — es la trampa más frecuente y hay que nombrarla).

**Cómo calificar:** 15 pts. El requisito duro es que **use la misma medición de la línea base**: si mide otra cosa, máximo 6, porque no habrá comparación posible en la Clase 16. Rechace los criterios que miden la solución en vez del problema («cantidad de descargas», «usuarios registrados») y explique el porqué en voz alta: es un error que arrastran hasta el informe final. Prometer el 100 % resta: indica que no entendieron el problema.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| El problema está en una frase, con la fórmula, y sin ninguna tecnología dentro | **25 %** | Es la habilidad central del corte: un problema con la solución adentro cierra el diseño antes de empezar. |
| La línea base tiene número, unidad y método declarado | **25 %** | Sin línea base el informe final de la Clase 16 no puede demostrar nada. |
| El árbol tiene dos niveles de causas y al menos una restricción marcada | **20 %** | Distinguir la causa que se puede tocar de la que no es lo que vuelve el proyecto realizable. |
| Hay un actor concreto al que se le puede preguntar esta semana y una frontera declarada | **15 %** | El acceso a los actores es el criterio que más proyectos imposibles descarta. |
| El criterio de éxito es verificable con la misma medición de la línea base | **15 %** | Cierra el ciclo: el proyecto queda con una manera de saber si sirvió. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Proyecto en un negocio pequeño (tienda, taller, restaurante).** Es el caso más frecuente y el más fácil de aterrizar, porque el dueño del problema está ahí y se le puede preguntar. La trampa típica es enunciar «el negocio no tiene sistema»: hay que llevarlos al actor y a la consecuencia («el dueño no sabe qué producto se está agotando hasta que un cliente lo pide y no está»). Línea base fácil y honesta: contar cuántas veces en una semana un cliente pidió algo que no había. Restricción casi segura: el dueño no va a dedicar media hora diaria a registrar datos. Frontera: la contabilidad y la facturación electrónica quedan fuera.

**Proyecto en la propia universidad.** Buen acceso a los actores —los compañeros— y por eso funciona bien, pero **hay dos reglas firmes**: no se usan nombres de funcionarios (se usa el rol) y no se recogen datos personales de compañeros, por la Ley 1581 de 2012 vista en la sesión 4. Línea base típica: preguntar a los 30 compañeros del grupo algo concreto y contar. La trampa es elegir un problema cuya solución depende de una decisión administrativa: eso no lo puede cambiar el equipo, y va marcado como restricción. Redirija hacia el problema de **información** del estudiante, que sí es abordable.

**Proyecto comunitario o de barrio (junta, colegio, huerta, ruta).** Alto valor y el riesgo más alto: casi siempre el problema viene demasiado grande («la inseguridad», «la movilidad»). La técnica de reducción que funciona en la sala: pregunte «¿a quién de esto le pueden preguntar algo esta semana?» y reescriba el problema alrededor de esa persona. La cifra suele salir de un conteo hecho por ellos mismos, y hay que aceptar muestras pequeñas siempre que digan el tamaño. Vigile que no aparezcan fotos ni nombres de terceros: la regla del curso aplica igual fuera del campus.

**Proyecto donde el equipo ya decidió la tecnología.** El equipo llega diciendo «vamos a hacer una app con IA para X». No lo pelee de frente: pídale que llene la ficha **sin mencionar la tecnología**, y haga la pregunta clave — «¿esto se podría resolver sin ninguna app?». Si la respuesta es sí, el problema aparece solo. La tecnología puede seguir siendo la elegida en la sesión 10; lo que no puede es estar dentro del enunciado del problema, porque cierra el diseño antes de empezar. Si al final de los 17 minutos el equipo no logró sacar la tecnología de la frase, ese es el punto que se le anota como corrección para la sesión 7.

## Errores que hay que ver y no dejar pasar

- **«Falta una app / un sistema para X»** → Es una solución disfrazada de problema: cierra el diseño antes de empezar y hace que cualquier app «resuelva» el problema. Que respondan «¿esto se podría resolver sin ninguna app?». Si es sí, el problema es otro y hay que escribirlo.
- **«La gente se queja» / «se pierden libros»** → Es un síntoma: la señal visible. Atacar el síntoma produce soluciones cosméticas. A quién le pasa qué, con qué consecuencia. Y la cifra.
- **Una cifra sin decir de dónde salió** → No se puede volver a medir en la Clase 16, así que no sirve como línea base. Número, unidad y método: preguntando a quién, contando qué, o cronometrando cuándo.
- **Un árbol con diez raíces** → Es una lista de todo lo que se les ocurrió, no un análisis, y con eso no se puede decidir qué atacar. Dos o tres causas directas, su segundo nivel, y las que no pueden cambiar marcadas como restricciones.
- **«El éxito es tener 200 usuarios en la app»** → Mide la adopción de la solución, no la resolución del problema. Se puede tener 200 usuarios y el problema intacto. El criterio con la misma medición de la línea base: de X a Y, medido así.

## Cierre: qué decir en los 3 minutos finales

Tres minutos y una idea, con estas palabras: **el problema ya está escrito, y de aquí en adelante todo se hace sobre esa ficha.** El corte 1 no cierra con una nota: cierra con un producto que gobierna diez sesiones. Muestre la progresión de la frase de la biblioteca en sus tres versiones —sesión 1, sesión 3, sesión 6— porque es la prueba visible de que aprendieron algo en cinco semanas. Recuerde las dos exigencias que se van a cobrar en la Clase 16: la **línea base con método** y el **criterio de éxito con la misma medición**. Y anuncie la sesión 7 sin misterio: arranca el corte 2 con el ciclo de vida de los proyectos de ingeniería, aplicado a este problema, no en abstracto.

## Con qué se conecta

Este documento cierra el corte 1 y es el que más hacia adelante mira. Hacia atrás recoge las cuatro sesiones: el problema inicial de la **sesión 1**, la frontera y los actores de la **sesión 3**, el afectado y la regla ética de la **sesión 4**, el indicador ambiental de la **sesión 5**. Hacia adelante: la **sesión 7** aplica el ciclo de vida a esta ficha; la **sesión 8** ajusta la propuesta de solución sobre la causa elegida; las **sesiones 10 y 11** prototipan respetando las restricciones marcadas hoy; la **Clase 13** evalúa el impacto de esa solución; y el **informe final de la Clase 16** compara contra la línea base de hoy. Una ficha vaga hoy es un semestre difícil.
