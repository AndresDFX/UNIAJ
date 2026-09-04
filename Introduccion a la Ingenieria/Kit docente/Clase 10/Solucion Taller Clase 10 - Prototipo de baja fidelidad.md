# Solución del taller — Clase 10: Prototipo de baja fidelidad

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento trae el prototipo completo del caso de la biblioteca: las tres pantallas descritas caja por caja, los textos exactos, el estado vacío y el de error, y el guion de prueba. Su valor está en dos cosas que ningún equipo hace solo: **los mensajes de error escritos con su texto exacto** y **la fecha de última actualización visible en pantalla**, que es la consecuencia de diseño de lo que se perdió al decidir en la sesión 8. Si el docente solo alcanza a leer un bloque, que sea **EL ESTADO VACÍO Y EL DE ERROR**.

## El caso que se resuelve aquí

**La biblioteca del barrio · el prototipo de la lista de disponibilidad**

Alcance mínimo de la sesión 8: la lista de disponibilidad consultable por enlace, con una pantalla de consulta para el usuario y una de actualización para la voluntaria, funcionando desde un celular y sin cuenta. Propuesta de mejora de la sesión 9: publicar la disponibilidad **sin catalogar el acervo completo y sin administrar un sistema**, solo los títulos que se prestan. Requisitos no funcionales vigentes: sin computador en el mostrador, se aprende sin manual, menos de 200 KB por consulta.

> Porque el prototipo obliga a resolver visualmente el sacrificio que el equipo aceptó en la sesión 8: la información no está al minuto. La solución de diseño —mostrar en pantalla cuándo se actualizó por última vez— es pequeña, evidente en retrospectiva, y ningún equipo la piensa solo. Ver eso es ver cómo una decisión de la sesión 8 se convierte en un elemento de interfaz en la 10.

## Consigna que se les dio

> Dibujen el **flujo principal del alcance mínimo** en tres pantallas o tres pasos: cada una con su frase de propósito, un solo camino principal, **textos reales**, el **estado vacío y el de error**, y una flecha con destino por cada botón. Después escriban el **guion de prueba** con tres tareas.

**Entregable:** el prototipo de tres pantallas en Excalidraw o draw.io (PNG en la carpeta del equipo) y el guion de prueba en el documento del equipo · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. EL FLUJO EN TRES PASOS

**Se pedía:** El camino principal del alcance mínimo, en tres pantallas o tres pasos, y **una frase de propósito por cada uno**.

**Respuesta modelo:**

**Pantalla 1 · Consultar.** *Aquí el usuario busca un título para saber si está disponible.*

**Pantalla 2 · Resultado.** *Aquí el usuario ve si el título está disponible, prestado o no está en la biblioteca.*

**Pantalla 3 · Actualizar (solo la voluntaria).** *Aquí la voluntaria marca un título como prestado o como devuelto, al cerrar el día.*

Las tres frases tienen un solo verbo y un solo actor. Nótese que la pantalla 2 contempla **tres resultados posibles** desde el enunciado —disponible, prestado, no está—, y ese tercer caso es el que la mayoría de los equipos descubre solo cuando un usuario lo encuentra.

**Ejemplo de frase mal escrita**, para contrastar: «aquí el usuario busca un libro **y** la voluntaria registra el préstamo». Tiene una «y» y dos actores: son dos pantallas, y juntarlas es el error que obliga a la voluntaria y al usuario a compartir el mismo teléfono.

**Cómo calificar:** 20 pts. La verificación es mecánica y rápida: **¿la frase de propósito necesita una «y»?** Si la necesita, la pantalla hace dos cosas y vale la mitad; hágalos partirla en la sala, toma dos minutos. Y verifique que el flujo sea el **alcance mínimo de la sesión 8** y no una idea nueva: si aparecieron funciones que estaban en la lista de «versión siguiente», el equipo se está saliendo del alcance que él mismo fijó, y eso hay que cortarlo hoy.

### 2. LAS TRES PANTALLAS DIBUJADAS

**Se pedía:** Las tres dibujadas de verdad, con el camino principal grande y primero, y una **flecha con destino** por cada botón.

**Respuesta modelo:**

**Pantalla 1 · Consultar** — de arriba abajo:

- Título: «Biblioteca del barrio · ¿está disponible?»
- **Un campo de texto grande**, con la indicación «Escriba el título o el autor» — es el camino principal y ocupa el centro de la pantalla
- Botón grande: «Buscar» → *va a la pantalla 2*
- Debajo, en letra pequeña: «Lista actualizada el viernes a las 6:00 p. m.»
- Enlace pequeño al pie: «Ver todos los títulos prestados» → *va a una lista simple*

**Pantalla 2 · Resultado** — tres versiones dibujadas, porque son tres estados distintos:

- *Disponible:* «**Cien años de soledad** — Disponible. Última actualización: viernes 6:00 p. m.» + botón «Buscar otro» → *vuelve a la 1*
- *Prestado:* «**Cien años de soledad** — Prestado. Se esperaba de vuelta el lunes.» + «Buscar otro»
- *No está:* «No encontramos «Cien años de soledad» en la lista. Puede que no esté en la biblioteca o que no esté registrado.» + «Buscar otro»

**Pantalla 3 · Actualizar (voluntaria)** — de arriba abajo:

- Título: «Actualizar la lista»
- Lista de los títulos registrados, cada uno con **un solo botón que alterna**: «Marcar prestado» / «Marcar devuelto» → *cambia el estado en la misma pantalla*
- Campo pequeño abajo: «Agregar un título que no está en la lista» + botón «Agregar»
- Botón grande al final: «Publicar cambios» → *muestra «Lista publicada. Los usuarios ya ven la información nueva.»*

**Dos decisiones de diseño que hay que señalar en clase, porque son las que salvan el proyecto:**

1. **La fecha de última actualización aparece en las dos pantallas del usuario.** No es un detalle estético: es la manera de ser honesto con el sacrificio que el equipo aceptó en la sesión 8 —la información no está al minuto—. Si el usuario ve «actualizada el viernes a las 6:00 p. m.», puede decidir por sí mismo si vale la pena el viaje. **Sin esa línea, la solución miente por omisión.**
2. **Un solo botón que alterna** en la pantalla de la voluntaria, en vez de dos botones separados: menos decisiones, menos errores, y cumple el requisito no funcional «se aprende sin manual».

**Cómo calificar:** 25 pts. Tres verificaciones: (a) **¿cada botón tiene destino escrito?** Un botón huérfano es una decisión no tomada; reste 3 por cada uno; (b) **¿se distingue a primera vista qué es lo principal?** Si las ocho cosas tienen el mismo tamaño, es la «pantalla democrática» y vale 12; (c) que estén **las tres pantallas dibujadas**, no descritas en texto. Dé puntos extra informales —dígalo en la retroalimentación— al equipo que resuelva un estado visible de honestidad como la fecha de actualización: casi ninguno lo hace y es la marca de un buen diseñador.

### 3. EL ESTADO VACÍO Y EL DE ERROR

**Se pedía:** Qué se ve la primera vez sin datos, qué se ve cuando la búsqueda no encuentra nada, y qué se ve cuando algo falla. **Con el texto exacto del mensaje.**

**Respuesta modelo:**

**Estado vacío** (la primera vez, o cuando no hay nada registrado):

> «Todavía no hay títulos en la lista. La biblioteca la está armando: por ahora, pregunte en el mostrador.»

**Búsqueda sin resultados** (el caso más frecuente y el más olvidado):

> «No encontramos «Cien años de soledad» en la lista. Puede que no esté en la biblioteca o que no esté registrado. **Pregunte en el mostrador o intente con el nombre del autor.**»

**Error** (no carga, no hay conexión):

> «No pudimos cargar la lista. Revise su conexión e intente otra vez. **Si no funciona, la biblioteca abre de 2 a 6 p. m.**»

**Y un cuarto estado que casi nadie dibuja y que este caso exige: información vieja.**

> «Esta lista se actualizó hace 3 días. Puede estar desactualizada.»

**Lo que hace buenos a estos mensajes**, y es lo que hay que enseñar: los cuatro **dicen qué hacer**, no solo que algo salió mal. Compare con las versiones malas, que son las que van a escribir los equipos: «Error», «No hay resultados», «Sin datos», «Ha ocurrido un problema». Todas informan y ninguna ayuda. La regla en una línea: **un mensaje de error sin una salida es una puerta cerrada con un letrero.**

Nótese además que dos de los cuatro mensajes mandan al usuario **fuera del sistema** —al mostrador, al horario de la biblioteca—. Eso es correcto y hay que decirlo: la solución no tiene que resolver todo, tiene que no dejar tirada a la persona.

**Cómo calificar:** 20 pts, y es el bloque que más diferencia. Se califica que **los tres estados existan dibujados** (12 pts) y que **cada mensaje diga qué hacer** (8 pts). «Error» o «No hay resultados» a secas vale 2 en ese estado: hágalos reescribir uno en la sala, en voz alta, y los otros salen solos. Valore especialmente el estado de información desactualizada si el proyecto lo necesita: es el puente entre la decisión de la sesión 8 y la interfaz, y es lo que separa un prototipo honesto de uno que oculta su limitación.

### 4. LOS TEXTOS REALES

**Se pedía:** Todos los rótulos y mensajes escritos como van a quedar. **Cero relleno**, cero «texto aquí», cero «lorem ipsum».

**Respuesta modelo:**

Los rótulos que costó decidir, con el porqué —esta es la parte que conviene leer en voz alta en clase:

- **«¿está disponible?»** en el título, en vez de «Sistema de gestión de préstamos». El usuario no viene a gestionar nada: viene a saber si vale la pena caminar.
- **«Escriba el título o el autor»** en vez de «Buscar». La primera dice qué escribir; la segunda deja al usuario adivinando si acepta temas, códigos o solo títulos exactos.
- **«Marcar prestado» / «Marcar devuelto»** en vez de «Editar estado». La voluntaria no piensa en estados: piensa en que alguien se llevó un libro.
- **«Publicar cambios»** en vez de «Guardar». «Guardar» no dice si alguien más ya lo ve; «publicar» sí, y en esta solución esa diferencia es justamente el momento en que la información se vuelve pública.
- **«Se esperaba de vuelta el lunes»** en vez de «Fecha de vencimiento: lunes». El segundo es lenguaje de sistema; el primero es lenguaje de persona, y además admite honestamente que es una expectativa y no una certeza.

**Lo que revela este bloque:** al escribir «Publicar cambios» el equipo descubrió una decisión que no había tomado —¿los cambios se ven de inmediato o hay un momento de publicación?—. **Eso es exactamente lo que hacen los textos reales**: obligan a decidir lo que el relleno permite postergar. Si hubieran escrito «botón aquí», la pregunta no habría aparecido hasta la Clase 12, con un usuario delante.

**Cómo calificar:** 15 pts. Verificación literal: **recorra el dibujo buscando «texto», «botón», «aquí va», «lorem ipsum»**. Cada uno resta 4. Y haga la pregunta que enseña: «¿por qué este botón se llama así?». Si no saben responder, ese botón no tiene función definida, y eso es un hallazgo más valioso que la nota. Valore mucho al equipo que cuente que un texto los obligó a tomar una decisión que no habían tomado: entendió el punto entero de la diapositiva.

### 5. EL GUION DE PRUEBA

**Se pedía:** Tres tareas para pedirle a una persona ajena, salidas de los **criterios de aceptación de la sesión 7**, y una de ellas sobre el caso en que el sistema **no** tiene la respuesta.

**Respuesta modelo:**

**Con quién:** la coordinadora (rol de voluntaria) y dos usuarios reales en la puerta de la biblioteca. **Ninguno del equipo** —viene del plan de validación de la sesión 8.

**Las tres tareas**, derivadas de los criterios de aceptación de la sesión 7:

1. *«Averigüe si el libro X está disponible.»* — mide el criterio «en menos de un minuto, sin ayuda».
2. *«Acaba de prestar el libro X. Déjelo registrado.»* (a la voluntaria) — mide «en menos de 30 segundos, sin manual».
3. *«Busque un libro que sabemos que no está en la lista. Dígame qué haría ahora.»* — **es la tarea del caso sin respuesta**, y la más valiosa: prueba el estado de error, que es donde se cae todo.

**Qué se observa, sin intervenir:** cuánto tarda · dónde duda · qué toca por error · qué busca y no encuentra · si termina sin ayuda · **y si se da cuenta de que la información puede estar desactualizada** (¿lee la fecha?).

**Las reglas del que aplica la prueba**, que hay que escribir en el guion porque en el momento se olvidan:

- No explicar nada antes. Se entrega y se dice la tarea.
- **No ayudar**, aunque duela. El silencio incómodo es el dato.
- No preguntar «¿le gusta?» ni «¿se entiende?». Se pregunta «¿qué está pensando?» mientras lo hace.
- Al final, una sola pregunta abierta: «¿qué esperaba que pasara y no pasó?».
- **Se anota lo que hizo, no lo que opinó.**

Y la regla de datos del curso: en las notas de la prueba se escribe el **rol** —«usuaria 1», «voluntaria»—, nunca el nombre, el teléfono ni la foto de la persona.

**Cómo calificar:** 20 pts. Tres verificaciones: (a) **¿son tareas o son preguntas de opinión?** «¿Le parece claro?» no es una tarea: reste a la mitad; (b) **¿hay una tarea sobre el caso sin respuesta?** Vale 7 de los 20 por sí sola, porque es la que prueba el estado de error; (c) **¿la persona es ajena al equipo?** Si planean probar entre ellos, corríjalo hoy — es la trampa de la sesión 8 reapareciendo y arruina la Clase 12. Valore que estén escritas las reglas del que aplica la prueba: sin ellas, el equipo ayuda al usuario sin darse cuenta y la prueba no mide nada.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| El flujo son tres pasos con una frase de propósito por pantalla, cada una haciendo una sola cosa | **20 %** | Una pantalla que hace dos cosas confunde al usuario y esconde una decisión de diseño no tomada. |
| Las tres pantallas están dibujadas, con el camino principal destacado y cada botón con destino | **25 %** | Un botón sin destino es una decisión que va a tomar el usuario por ustedes, mal, en la Clase 12. |
| Existen el estado vacío y el de error, con el texto exacto del mensaje | **20 %** | El camino feliz es la minoría de los casos reales: un prototipo sin errores no prueba nada. |
| Todos los textos son reales, sin relleno | **15 %** | Los textos falsos esconden los problemas: el rótulo que no se sabe escribir es una función que no está definida. |
| El guion de prueba tiene tres tareas ejecutables y una cubre el caso sin respuesta | **20 %** | Es lo que hace posible la validación de la Clase 12: se pide hacer, no opinar. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Equipos que se ponen a elegir colores, íconos y tipografías.** Es el desperdicio de taller más común de esta sesión. Córtelo en caliente y con el argumento, no con la orden: la paradoja de la fidelidad dice que cuanto más terminado se vea, menos crítica útil van a recibir en la Clase 12, así que **pulir hoy es perder información mañana**. Redirija con la pregunta del estado de error, que es lo que les falta.

**Proyectos de proceso o gestión, sin pantallas.** Las «tres pantallas» son **tres pasos del proceso** o **el formato que alguien va a llenar**, y draw.io es la herramienta. Los cinco pasos aplican igual, incluido el estado de error: en un proceso, el estado de error es **qué pasa cuando el paso anterior no se hizo** o cuando falta un dato, y es exactamente donde fallan los procesos en la vida real. El guion de prueba es el mismo: una persona ajena ejecuta el proceso siguiendo solo el formato.

**Equipos que dibujan solo el camino feliz.** Va a pasar en la mayoría. La intervención de tres segundos que funciona: entre a la sala, señale el campo de búsqueda y diga «busco un libro que no existe, ¿qué veo?». El silencio que sigue es la clase. Hágalos dibujar ese estado ahí mismo, y los otros dos salen por sí solos.

**Equipos que quieren usar una herramienta de prototipado profesional que no está en la lista.** Se permite **si es gratuita, si abre en el navegador y si no pide tarjeta** — esa es la regla del curso y no se negocia. Pero adviértales el riesgo real: aprender la herramienta se les va a comer el tiempo de diseñar, y lo que se califica es el diseño. Si a los cinco minutos no tienen nada dibujado, mándelos a papel y una foto: es un entregable perfectamente válido.

## Errores que hay que ver y no dejar pasar

- **Un prototipo con «texto aquí» y botones sin nombre** → El relleno esconde los problemas: un botón que no se supo cómo llamar es una función que no está definida. Los rótulos reales, y la pregunta «¿por qué este botón se llama así?» para cada uno.
- **Solo el camino feliz, sin búsqueda vacía ni error** → En la vida real el camino feliz es la minoría de los casos, así que el prototipo no prueba nada. «Busco algo que no existe, ¿qué veo?». Que lo dibujen en la sala, con el mensaje exacto.
- **«Error» o «No hay resultados» como mensaje** → Informa que algo salió mal y no ofrece salida: es una puerta cerrada con un letrero. Un mensaje que diga **qué hacer ahora**, aunque la salida sea fuera del sistema.
- **Media hora eligiendo colores y tipografías** → La fidelidad alta reduce la crítica útil: pulir hoy es perder información en la Clase 12. El estado de error y los textos reales. Los colores, en la Clase 14.
- **Datos de personas reales en el prototipo, «porque es solo de prueba»** → Es tratamiento de datos personales sin autorización: la Ley 1581 de 2012 no distingue entre prueba y producción. Datos inventados, siempre. Y en las notas de la prueba, el rol y no el nombre.

## Cierre: qué decir en los 3 minutos finales

Tres minutos y una idea que hay que dejar bien plantada: **el prototipo no es una maqueta, es una pregunta**, y se hace feo a propósito para que la gente se atreva a decir lo que está mal. Repita las tres exigencias concretas, porque son las que van a definir la nota y la calidad de la Clase 12: textos reales, estado de error con salida, datos inventados. Vale la pena cerrar con el hallazgo del caso modelo, que es pequeño y memorable: la línea «lista actualizada el viernes a las 6:00 p. m.» es la manera de ser honesto en la interfaz con el sacrificio que el equipo aceptó en la sesión 8 — sin esa línea, la solución miente por omisión, y con ella el usuario decide por sí mismo si vale la pena el viaje. Es una decisión de diseño de dos segundos que nace de un análisis de dos sesiones atrás, y esa cadena es lo que se está enseñando. Anuncie la sesión 11: prototipo v2 con IA autorizada, con entrega del prompt y de las correcciones, y **cierra el corte 2** con la evaluación en ExamLab sobre las sesiones 7 a 11.

## Con qué se conecta

Hacia atrás: la **sesión 8** fijó el alcance mínimo que hoy se dibuja y el plan de validación que hoy se convierte en guion; la **sesión 9** aportó el diseño de pantalla que se reusa de los antecedentes; la **sesión 7** dejó los criterios de aceptación, que son las tareas de la prueba; la **sesión 4** dejó la Ley 1581, que es la regla de datos inventados. Hacia adelante: la **sesión 11** genera variantes de estas pantallas con IA y corrige a mano; la **Clase 12** ejecuta este guion con una persona ajena; la **Clase 14** sube la fidelidad solo para la presentación; y el **informe final** documenta la evolución del prototipo.
