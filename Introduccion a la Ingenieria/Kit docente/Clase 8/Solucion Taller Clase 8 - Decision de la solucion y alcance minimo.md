# Solución del taller — Clase 8: Decisión de la solución y alcance mínimo

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento trae la decisión completa del caso de la biblioteca: dos alternativas, la matriz con pesos y justificaciones, lo que se pierde, el alcance mínimo y el plan de validación. Es el modelo para las salas, y su valor está en dos detalles que ningún equipo hace solo: **los pesos escritos antes de calificar** y **la justificación por casilla**. Si el docente solo alcanza a leer un bloque, que sea **LA MATRIZ Y LA DECISIÓN**.

## El caso que se resuelve aquí

**La biblioteca del barrio · decidir entre dos alternativas**

Requisito que ataca la causa elegida: *el usuario puede saber si un libro está disponible sin ir a la biblioteca*. Las dos alternativas que salieron del trabajo independiente: **(A) una lista de disponibilidad publicada** que la voluntaria actualiza una vez al día desde su celular, consultable por cualquiera con un enlace; **(B) una aplicación web con el registro completo de préstamos**, donde la voluntaria registra cada préstamo y devolución en el momento y la disponibilidad se actualiza sola. Restricciones vigentes: presupuesto cero, sin computador en el mostrador, voluntarias que rotan y sin capacitación larga, nadie atendiendo en horario fijo, y el requisito de menos de 200 KB por consulta.

> Porque la alternativa que suena peor —una lista actualizada una vez al día— gana la matriz, y eso es exactamente lo que un estudiante de primer semestre necesita ver. La solución más completa no es la mejor decisión cuando las restricciones mandan.

## Consigna que se les dio

> Decidan qué van a construir. Escriban sus **dos alternativas** en una frase cada una, comparen con una **matriz de criterios con pesos definidos antes de calificar**, decidan y digan **qué se pierde**. Después fijen el **alcance mínimo** del semestre, la lista de lo que queda fuera, y el **plan de validación**.

**Entregable:** la matriz de decisión, el alcance mínimo con su lista de exclusiones y el plan de validación en el documento del equipo, más el flujo de la alternativa elegida en draw.io · **40 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. LAS DOS ALTERNATIVAS

**Se pedía:** Cada alternativa en **una frase**, sin adjetivos, diciendo qué hace y cómo resuelve la causa elegida en el árbol de la sesión 6.

**Respuesta modelo:**

**(A) Lista de disponibilidad publicada.** La voluntaria marca, una vez al día y desde su celular, qué títulos están prestados; cualquiera consulta la lista con un enlace, sin cuenta y sin instalar nada.

**(B) Registro de préstamos en línea.** La voluntaria registra cada préstamo y devolución en el momento en que ocurre; la disponibilidad se calcula sola y se consulta en cualquier momento.

Las dos atacan la misma causa —que el registro solo se puede consultar en el mostrador— y son genuinamente distintas: cambian quién hace el trabajo, cuándo lo hace y qué tan actualizada queda la información.

**Ejemplo de dos alternativas falsas**, para mostrar en clase: «(A) una app y (B) una app con más funciones». Es la misma idea dos veces; no hay decisión que tomar y la matriz no va a enseñar nada.

**Cómo calificar:** 15 pts. La verificación es una pregunta: **¿cambian algo estructural entre A y B —quién trabaja, cuándo, con qué información— o solo el tamaño?** Si solo cambia el tamaño, vale 6 y hay que hacerles escribir una segunda alternativa de verdad en la sala. Un buen truco para desbloquearlos: pedir una alternativa que **no use ninguna tecnología nueva**.

### 2. LOS CRITERIOS Y SUS PESOS

**Se pedía:** De 3 a 5 criterios sacados de sus **requisitos no funcionales y restricciones**, cada uno con un peso, **escritos antes de calificar**.

**Respuesta modelo:**

Escritos **antes** de mirar las alternativas, con su origen:

| Criterio | Peso | De dónde sale |
|---|---|---|
| Funciona sin computador en el mostrador | 3 | RNF1 · restricción del árbol |
| Se aprende sin manual (voluntarias que rotan) | 3 | RNF2 · restricción del árbol |
| Se puede construir y probar en las sesiones que quedan | 2 | Plan de hitos de la sesión 7 |
| Cumple menos de 200 KB por consulta | 1 | Indicador ambiental de la sesión 5 |
| Qué tan actualizada queda la información | 2 | Deriva del criterio de éxito de la sesión 6 |

Los pesos 3 son las dos restricciones duras: si una alternativa falla ahí, no importa lo demás. Nótese que **«qué tan actualizada queda la información» pesa 2 y no 3**, y esa decisión de peso es la que define el resultado — por eso hay que tomarla antes y por escrito, con el argumento: el criterio de éxito de la sesión 6 pedía bajar los viajes en vano de 4 a menos de 2 de cada 10, y para eso no hace falta información al segundo; basta con que esté al día.

**Criterios que se rechazan:** «lo más innovador», «lo que más nos gusta», «lo que se ve mejor en la exposición». No se pueden calificar y no se pueden defender ante nadie.

**Cómo calificar:** 25 pts. Dos verificaciones: (a) **cada criterio tiene un origen rastreable** a un requisito o restricción escrito antes (15 pts); (b) **los pesos están escritos antes de las calificaciones** (10 pts). Para (b), en la primera ronda de salas mire el documento: si las calificaciones y los pesos aparecieron al mismo tiempo, dígalo y hágalos justificar los pesos por separado. No es un formalismo: es el punto donde se cuela la decisión ya tomada.

### 3. LA MATRIZ Y LA DECISIÓN

**Se pedía:** Cada alternativa calificada criterio por criterio (escala 1-3) con **media línea de justificación por casilla**, el resultado, y la decisión.

**Respuesta modelo:**

| Criterio (peso) | A · Lista publicada | B · Registro en línea |
|---|---|---|
| Sin computador en mostrador (3) | **3** — se actualiza una vez al día desde el celular, con calma, al cerrar | **1** — exige registrar en el momento mientras se atiende, y el celular está ocupado |
| Se aprende sin manual (3) | **3** — es marcar en una lista; se explica en un minuto | **2** — hay que aprender a registrar préstamo y devolución sin equivocarse |
| Construible en las sesiones que quedan (2) | **3** — el prototipo es la lista misma | **1** — implica registro, estados y corrección de errores |
| Menos de 200 KB por consulta (1) | **3** — es texto | **2** — depende de cómo se construya |
| Información actualizada (2) | **1** — al día, no al minuto: un libro prestado en la mañana aparece disponible hasta el cierre | **3** — actualizada al momento |
| **Total ponderado** | **3·3+3·3+2·3+1·3+2·1 = 29** | **3·1+3·2+2·1+1·2+2·3 = 19** |

**Decisión: la alternativa A, la lista publicada.**

Y el argumento en una frase, que es lo que hay que exigir: *A gana porque las dos restricciones duras —sin computador en el mostrador y sin capacitación— son las que más pesan, y B falla justamente ahí; la información al minuto sería mejor, pero no es lo que el criterio de éxito exige.*

**Esta es la lección de la sesión:** la alternativa que suena más profesional, más completa y más parecida a «un sistema de verdad» **pierde**, porque las restricciones del contexto son reales. Un equipo que elige B tiene que explicar cómo resuelve el celular ocupado y la rotación de voluntarias; si lo resuelve con un argumento sólido, su decisión también es válida — lo que no es válido es ignorar los pesos que ellos mismos escribieron.

**Cómo calificar:** 20 pts. El criterio central es **la justificación por casilla** (12 pts): una matriz de puros números vale 6, aunque la aritmética esté impecable, y hay que decir por qué —el número no se puede discutir, la justificación sí—. Los otros 8 son por la coherencia entre el total y la decisión: si el equipo eligió la alternativa con menor puntaje, tiene que explicar el porqué explícitamente; si lo explica bien, dé los 8 completos, porque una matriz es una ayuda para pensar y no un oráculo.

### 4. QUÉ SE PIERDE

**Se pedía:** Lo que la decisión sacrifica, en dos o tres líneas. Toda decisión sacrifica algo.

**Respuesta modelo:**

**Se pierde la actualización inmediata.** Un libro prestado a las nueve de la mañana va a aparecer como disponible hasta que la voluntaria actualice al cierre. Eso significa que **algunos viajes en vano van a seguir ocurriendo**, y hay que decirlo sin maquillar: la solución elegida no lleva el problema a cero, lo baja.

**Se pierde también** el registro histórico de préstamos, que habría servido para el otro problema de la biblioteca —los libros que no vuelven—, y que en la sesión 6 se declaró explícitamente fuera de la frontera.

**Y se gana:** que funcione sin computador, que cualquier voluntaria nueva lo use sin capacitación, que se pueda construir y probar de verdad en las sesiones que quedan, y que consuma casi nada de datos. El intercambio es explícito y defendible.

Un equipo que escriba «no perdemos nada» no comparó: si una alternativa fuera mejor en todos los criterios, no habría habido decisión que tomar.

**Cómo calificar:** 15 pts. Se califica que haya **una pérdida concreta y verificable**, no una fórmula de cortesía. «Perdemos un poco de funcionalidad» vale 5; «un libro prestado en la mañana aparece disponible hasta el cierre, así que algunos viajes en vano van a seguir» vale los 15. «No perdemos nada» vale 0 y hay que explicar por qué en el momento: significa que no compararon.

### 5. ALCANCE MÍNIMO Y PLAN DE VALIDACIÓN

**Se pedía:** Qué se construye este semestre (un requisito funcional completo, cumpliendo los no funcionales), la lista de lo que queda para «versión siguiente», y el plan de validación: **con quién** se prueba, **qué tareas** se le piden y **qué se observa**.

**Respuesta modelo:**

**Alcance mínimo del semestre:** *la lista de disponibilidad consultable por enlace, con la pantalla de consulta para el usuario y la pantalla de actualización para la voluntaria, funcionando desde un celular y sin cuenta.* Un solo requisito funcional completo, cumpliendo los tres no funcionales.

Pasa la prueba: si se construye solo eso y se pone delante de un estudiante que necesita un libro, **le sirve** — puede saber si vale la pena el viaje.

**Versión siguiente (declarado fuera):** búsqueda por tema · registro histórico de préstamos · aviso automático de devolución · el catálogo completo del acervo · reservas.

**Plan de validación:**

- **Con quién:** la coordinadora (rol de voluntaria) y **dos usuarios reales en la puerta de la biblioteca**, ninguno del equipo.
- **Qué tareas se le piden**, tomadas de los criterios de aceptación de la sesión 7: *(1) averigüe si el libro «X» está disponible; (2) marque este libro como prestado; (3) dígame qué haría si el libro que busca no aparece.*
- **Qué se observa:** cuánto tarda, dónde duda, qué toca por error, qué busca y no encuentra, y si termina la tarea sin ayuda. **Se observa en silencio**: no se explica, no se ayuda y no se pregunta si le gustó.

La tarea (3) es la más valiosa y casi nadie la incluye: pregunta por el caso en que el sistema **no** tiene la respuesta, que es donde se cae la mayoría de los prototipos.

**Cómo calificar:** 25 pts. Dos requisitos duros: (a) **el alcance mínimo resuelve algo por sí solo** (12 pts) — aplique la prueba en voz alta: «si construyen solo esto, ¿le sirve a la persona que vive el problema?»; si la respuesta es no, es un pedazo y vale 5; (b) **la persona de la prueba es ajena al equipo** (13 pts). Si planean probar entre ellos, corríjalo en la sala, no en la nota: es la trampa que arruina la Clase 12. Valore mucho que haya una tarea sobre el caso en que el sistema no tiene la respuesta.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| Las dos alternativas son realmente distintas y atacan la misma causa | **15 %** | Comparar dos versiones de la misma idea es simular una decisión. |
| Los criterios se rastrean a requisitos o restricciones, y los pesos están antes de las calificaciones | **25 %** | Es la garantía de que la decisión no estaba tomada antes de analizar: el sesgo más común de la ingeniería. |
| Cada casilla de la matriz tiene una justificación de media línea | **20 %** | El resultado de una matriz no es el número: es el argumento. Sin justificación no hay nada que defender. |
| Se nombra concretamente qué se pierde con la decisión | **15 %** | Reconocer el sacrificio es lo que distingue decidir de preferir. |
| El alcance mínimo resuelve algo por sí solo y el plan de validación usa una persona ajena | **25 %** | Es lo que hace posible aprender algo real en la Clase 12, en vez de una demostración entre amigos. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Equipos que llegan sin las dos alternativas.** Va a pasar en al menos un equipo. No los deje discutir el trabajo independiente durante veinte minutos: deles cinco para escribir dos frases, y sugiera el truco que desbloquea siempre — **una de las dos alternativas no puede usar ninguna tecnología nueva**. La comparación entre «lo que se puede hacer con lo que ya existe» y «lo que queremos construir» es la más instructiva de todas.

**Equipos donde la alternativa ambiciosa gana la matriz.** Puede ser legítimo y no hay que forzar el resultado de la biblioteca. La verificación es si los pesos son coherentes: si «construible en las sesiones que quedan» pesa 1 y la alternativa exige diez semanas de trabajo, el problema no es la matriz, es el peso. Pregunte «¿qué pasa si en la Clase 12 no está listo?» y deje que ajusten el peso ellos.

**Proyectos de proceso o gestión, sin pantallas.** El alcance mínimo suele ser **un formato más un acuerdo de quién lo llena y cuándo**; el prototipo de la sesión 10 será ese formato. El plan de validación se hace igual: se le pide a una persona ajena que ejecute el proceso siguiendo solo el formato, sin preguntar nada, y se observa dónde se queda trabada. Funciona igual de bien que con pantallas.

**Equipos que planean probar entre ellos.** Es el error más costoso de la sesión, porque no se ve hasta la 12, cuando ya no hay tiempo de arreglarlo. Exija hoy **el nombre del rol** de la persona ajena que va a probar —no el nombre propio, por la regla de datos personales— y cómo la van a contactar. Si no pueden nombrar a nadie ajeno, el proyecto no pasó el criterio de acceso a los actores de la sesión 6 y hay que reducirlo ya.

## Errores que hay que ver y no dejar pasar

- **«(A) una app y (B) una app con más funciones»** → Es la misma idea dos veces: no hay decisión que tomar y la matriz no enseña nada. Una alternativa que **no use ninguna tecnología nueva**. La comparación entre lo que ya se puede hacer y lo que se quiere construir es la más instructiva.
- **Los pesos y las calificaciones escritos al mismo tiempo** → Ahí se cuela la decisión ya tomada: sin mala intención, los pesos se acomodan para que gane el favorito. Los criterios y los pesos primero, en el documento, y solo después las calificaciones.
- **Una matriz de puros números, sin justificaciones** → El número no se puede discutir ni defender; la justificación sí. Sin ella la matriz es un adorno. Media línea por casilla: por qué ese número para esa alternativa en ese criterio.
- **«No perdemos nada con esta decisión»** → Si una alternativa fuera mejor en todos los criterios no habría habido nada que decidir. Qué se sacrifica, concreto y verificable. Y que se diga en la exposición final.
- **«Vamos a probar el prototipo entre nosotros»** → Quien construyó sabe dónde hay que tocar: la prueba está decidida antes de empezar. Es el error del Therac-25 en pequeño. El rol de una persona ajena al equipo y cómo la van a contactar, hoy mismo.

## Cierre: qué decir en los 3 minutos finales

Cinco minutos hoy, que es más de lo habitual, y conviene usarlos en tres cosas. Primero, la idea de la sesión: **decidir no es acertar.** Una decisión de ingeniería se sostiene con criterios escritos antes, una justificación por criterio y la lista de lo que se sacrificó; sin eso es una preferencia con tabla. Segundo, el hallazgo del caso modelo, que vale la pena decir con estas palabras: **la alternativa que sonaba más profesional perdió**, porque las restricciones del contexto son reales y ellos mismos les habían puesto el peso más alto. Tercero, las dos trampas de la validación —no probar con el equipo, no preguntar «¿le gusta?»— porque se aplican en la Clase 12 y es donde se gana o se pierde el corte 3. Anuncie la sesión 9: antes de construir hay que saber qué ya existe y quién lo intentó, con fuentes verificables — y una respuesta de asistente de IA no es una fuente.

## Con qué se conecta

Hacia atrás: la **sesión 7** dejó los requisitos y los criterios de aceptación, que hoy se volvieron los criterios de la matriz y las tareas del plan de validación; la **sesión 6** dejó las restricciones, que son los pesos altos; la **sesión 5** dejó el indicador ambiental, que es un criterio más; la **sesión 4** dejó el Therac-25, que es el argumento contra evaluarse a sí mismo. Hacia adelante: la **sesión 9** busca antecedentes de la alternativa elegida; la **Clase 10** prototipa exactamente el alcance mínimo de hoy; la **Clase 11** lo corrige y cierra el corte 2; la **Clase 12** ejecuta este plan de validación con una persona ajena; y la lista de «versión siguiente» se muestra en la **exposición final de la Clase 15**.
