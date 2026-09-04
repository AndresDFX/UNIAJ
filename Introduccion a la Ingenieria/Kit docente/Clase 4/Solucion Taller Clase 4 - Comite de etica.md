# Solución del taller — Clase 4: Comité de ética

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento resuelve el caso Therac-25 completo —el más difícil de los cinco, porque exige entender una decisión técnica— y trae al final la clave de los otros cuatro. Sirve para calificar con un referente y, sobre todo, para tener listo el numeral citado: es el bloque que decide el 30 % y el que los equipos improvisan si el docente no lo tiene a mano.

## El caso que se resuelve aquí

**Therac-25 · La máquina de radioterapia que dio sobredosis (1985–1987)**

Máquina de radioterapia de la Atomic Energy of Canada Limited (AECL). Entre 1985 y 1987 se documentaron seis accidentes con sobredosis masivas de radiación, con muertos entre los pacientes. Los modelos anteriores (Therac-6 y Therac-20) tenían **seguros físicos** que impedían mecánicamente la configuración peligrosa; en el Therac-25 se eliminaron y se dejó la protección **solo en el software**, reutilizando código de los modelos previos. Existía una condición de carrera que se activaba cuando la operadora corregía la pantalla muy rápido —justo lo que hacían las operadoras con experiencia—. Los mensajes de error eran crípticos («MALFUNCTION 54») y tan frecuentes que se ignoraban. No hubo revisión independiente del código, y el fabricante sostuvo inicialmente que una sobredosis era imposible.

> Si el docente solo alcanza a leer una parte antes de clase, que sea el bloque «EL MOMENTO EN QUE SE PUDO PARAR»: es el que casi ningún equipo hace bien solo, porque exige distinguir el error de programación de la decisión que lo volvió letal.

## Consigna que se les dio

> Su equipo es un comité de ética profesional y le toca **un caso**. Emitan un veredicto con el código en la mano: qué principio o norma se violó (**con el numeral**), quién decidió, en qué momento se pudo parar y qué debía hacer el ingeniero ahí. No se acepta «actuaron mal»: eso no es un veredicto.

**Entregable:** un acta de comité de cinco bloques en el documento del equipo, con al menos un numeral de código o de norma citado literalmente · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. LOS HECHOS, SIN ADJETIVOS

**Se pedía:** Qué pasó, en cinco líneas máximo: qué sistema era, qué hizo, a quién afectó y cómo se supo. Sin opinión todavía.

**Respuesta modelo:**

El Therac-25 era un acelerador lineal de uso médico para radioterapia, fabricado por AECL y operado en hospitales de Estados Unidos y Canadá. Entre junio de 1985 y enero de 1987 se documentaron seis casos en que entregó dosis de radiación muy superiores a la prescrita; hubo pacientes muertos y otros con lesiones graves.

Los afectados fueron los pacientes, y en segundo lugar las operadoras, a las que en varios casos se responsabilizó antes de identificar la causa. Se supo por el reporte insistente de los hospitales y por la investigación de los reguladores; la reconstrucción técnica de referencia es la de Nancy Leveson y Clark Turner publicada en 1993.

**Cómo calificar:** 15 pts. Se califica que **no haya juicio todavía**. Un equipo que escriba «la empresa fue criminalmente negligente al vender una máquina mortal» pierde la mitad: eso es el veredicto, y va en el bloque 3. Exija además el «cómo se supo»: es la parte que los equipos omiten y la que enseña que los casos no se descubren solos, alguien los reporta.

### 2. QUIÉN DECIDIÓ QUÉ

**Se pedía:** La decisión concreta que causó el daño y **quién la tomó** (el rol: el diseñador, el gerente de producto, el ingeniero que ejecutó). Si fueron varias personas en cadena, escriban la cadena.

**Respuesta modelo:**

**La decisión que causó el daño: eliminar los seguros físicos (interlocks de hardware) que tenían los modelos anteriores y trasladar esa protección al software.** La tomó el equipo de diseño del producto en AECL, en la fase de diseño del Therac-25, no un programador en una madrugada.

**La cadena completa, que es lo que se pide si fueron varias personas:**

1. **El diseñador del producto** decide quitar los seguros físicos confiando en el software.
2. **Quien decide reutilizar el código** de los modelos Therac-6 y 20 sin volver a verificarlo en el contexto nuevo. Ese código arrastraba errores que antes eran inofensivos **porque el seguro físico los tapaba**.
3. **Quien decide no someter el software a revisión independiente**, en un equipo donde el software era ahora la única barrera entre el paciente y una dosis letal.
4. **Quien diseña la interfaz** con mensajes como «MALFUNCTION 54», sin decir qué pasó ni qué hacer, y sin distinguir un aviso trivial de uno grave.
5. **Quien responde los primeros reportes de accidente** afirmando que la sobredosis era imposible, en vez de investigarla. Esta es la decisión que convirtió el primer accidente en seis.

Nótese que **el error de programación no aparece en la lista como causa principal**. La condición de carrera existía; lo que la volvió letal fueron las decisiones 1, 2 y 3.

**Cómo calificar:** 20 pts. Un equipo que responda «el programador que dejó el bug» vale 8: es la respuesta intuitiva y es la equivocada, y hay que corregirla en voz alta porque es exactamente la confusión que la clase ataca. Los 20 completos son para quien identifique la eliminación de los seguros físicos como la decisión de fondo. Punto extra de reconocimiento —no de nota— si detectan la decisión 5, que es la que multiplicó el daño.

### 3. EL NUMERAL QUE SE VIOLÓ

**Se pedía:** Cite **literalmente** al menos un principio del código ACM/IEEE o un artículo de la Ley 842 de 2003, la Ley 1581 de 2012 o la Ley 1273 de 2009, y explique en dos líneas por qué aplica a este caso.

**Respuesta modelo:**

**Código ACM/IEEE de Ética del Ingeniero de Software (1999), Principio 1 — PÚBLICO:** «Los ingenieros de software actuarán de manera consistente con el interés público». Y en particular el compromiso 1.03: **aprobar el software solo si existe la creencia fundada de que es seguro, cumple las especificaciones, ha pasado las pruebas apropiadas y no degrada la calidad de vida, la privacidad ni daña el ambiente**. Aplica de forma directa: el software se aprobó como única barrera de seguridad de una máquina capaz de matar, sin revisión independiente y sin pruebas que cubrieran la secuencia de teclas que las operadoras usaban a diario. No había creencia fundada de que era seguro; había una suposición.

**También aplica el Principio 3 — PRODUCTO**, sobre asegurar que el producto cumpla los estándares profesionales más altos posibles, y el **Principio 6 — PROFESIÓN**, por sostener públicamente que la sobredosis era imposible cuando ya había reportes.

**En Colombia, si el caso ocurriera aquí: Ley 842 de 2003**, que en sus deberes del profesional frente a la sociedad obliga a que el ejercicio de la ingeniería no ponga en riesgo la vida ni la integridad de las personas, y establece las faltas contra la ética profesional sancionables por el COPNIA, incluida la suspensión de la matrícula profesional. El equipo debe citar el artículo concreto del texto que se compartió en la carpeta del curso, no la ley en general.

**Cómo calificar:** 30 pts, el bloque que decide. Requisitos: (a) **cita literal**, entre comillas o transcrita, no un resumen; (b) identificación del principio o artículo por su número; (c) dos líneas que conecten el numeral con **este** hecho. Si falta (a), máximo 15. Si el equipo cita «el código de ética dice que hay que ser responsable», 0: eso no está en ningún numeral. Se acepta cualquiera de los principios 1, 3 o 6, o la Ley 842; el 1 es el más fuerte y conviene decirlo al cerrar.

### 4. EL MOMENTO EN QUE SE PUDO PARAR

**Se pedía:** El momento **más temprano** en que alguien con la información disponible podía cambiar el resultado, y qué debía hacer exactamente ahí (a quién decirle qué, y por escrito o no).

**Respuesta modelo:**

**El momento más temprano y más barato fue la reunión de diseño en que se decidió eliminar los seguros físicos.** Ahí, antes de escribir una línea de código, alguien tenía que hacer una pregunta que no requería ser experto en software: *si el software falla, ¿qué impide que el paciente reciba una dosis letal?* La respuesta era «nada», y esa respuesta bastaba para no seguir. Costo de parar en ese punto: una reunión y un rediseño. Costo de no parar: seis accidentes y muertos.

**Qué debía hacer el ingeniero, concretamente:** dejar por escrito —no dicho de pasada— que al retirar los interlocks el software queda como única barrera de seguridad, y que en esa condición se requiere revisión independiente del código y pruebas específicas de las secuencias de operación reales. Dirigido a quien decide el diseño, con copia a quien responde por la certificación del equipo. Eso es escalar temprano y dejar rastro: no es renunciar ni denunciar, es que la decisión la tome quien tiene la autoridad **sabiendo** el riesgo.

**Segundo momento, más caro pero todavía útil:** el primer reporte de accidente. Ahí la acción correcta era retirar las máquinas del servicio mientras se investigaba, en vez de afirmar que la sobredosis era imposible. Cinco de los seis accidentes ocurrieron después del primero.

**Cómo calificar:** 25 pts. Se califica que el momento sea **anterior al daño** y que la acción sea ejecutable. «Debieron probar mejor el software» vale 10: es correcto y es tardío, porque no toca la decisión que creó el riesgo. «Debieron ser más responsables» vale 0. Los 25 son para quien ubique la reunión de diseño y escriba a quién había que decirle qué. Si el equipo identifica el segundo momento —el primer reporte—, es señal de muy buena lectura del caso.

### 5. LA REGLA QUE SE LLEVAN

**Se pedía:** Una regla en una frase, escrita para ustedes mismos, que evite repetir esto en el proyecto de este curso. Tiene que ser verificable.

**Respuesta modelo:**

Ejemplos de reglas verificables que salen bien de este caso:

- «Cuando quitemos una validación de nuestro prototipo porque *el código ya la cubre*, lo escribimos en el documento del equipo con la fecha y quién lo decidió.»
- «Ningún mensaje de error de nuestro prototipo dice solo un código: dice qué pasó y qué hacer.»
- «Si algo de nuestro sistema puede dañar a una persona, no dependemos de una sola comprobación.»

Las tres son comprobables por otra persona, que es el requisito. La primera es la que más se parece al caso; la segunda es la más fácil de cumplir y aun así rara.

**Cómo calificar:** 10 pts. El único criterio es **que se pueda comprobar**. Lea la regla y pregúntese: ¿podría yo revisar el documento del equipo en la Clase 12 y decir si la cumplieron? Si la respuesta es no, es una intención, no una regla, y vale 3.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| Los hechos están sin adjetivos de juicio y son verificables | **15 %** | Un comité que empieza opinando no puede juzgar. Separar hecho de juicio es la habilidad base. |
| Hay un sujeto y una decisión concreta, no «la empresa» | **20 %** | Es lo que convierte el caso en algo aplicable: las decisiones las toman personas con un cargo. |
| Se cita literalmente un numeral del código o un artículo de ley, y se conecta con el hecho | **30 %** | Es la diferencia entre un argumento profesional y una opinión. Es lo que se evalúa en el corte. |
| El momento de parar es anterior al daño y la acción propuesta es concreta | **25 %** | Es el valor de ingeniería de la sesión: la ética se ejerce decidiendo, no lamentando. |
| La regla propia es verificable y aplica al proyecto del curso | **10 %** | Cierra el ciclo: lo aprendido se convierte en una restricción de su propio trabajo. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Equipo 2 · Volkswagen (2015).** **Decisión:** escribir un software cuyo único propósito era detectar la prueba de emisiones y comportarse distinto durante ella. **Cadena:** quien definió la meta imposible (cumplir el límite sin rediseñar el motor), quien propuso el atajo, quien lo programó. **Numeral:** ACM/IEEE Principio 1 (interés público: se contamina a terceros que no son parte del negocio) y Principio 6 (profesión). **Momento de parar:** cuando le pidieron programar la detección de la prueba; no hace falta saber de emisiones para ver que un código que se comporta distinto durante el examen existe para engañar. **Dato duro que hay que exigir:** el ingeniero que ejecutó fue condenado a 40 meses de prisión, así que la defensa de la obediencia ya fue probada en un tribunal y falló.

**Equipo 3 · Boeing 737 MAX (2018–2019).** **Decisión:** que un sistema capaz de mover el avión dependiera de **un solo sensor**, y no documentarlo en el manual de vuelo para no obligar a reentrenar pilotos. **Numeral:** ACM/IEEE 1.03 (aprobar solo con creencia fundada de que es seguro) y Principio 3 (producto). **Momento de parar:** la decisión de arquitectura del sensor único; segundo momento, después del primer accidente, cuando se optó por un boletín informativo en vez de dejar la flota en tierra. **Detalle que hay que exigir porque es el más revelador:** la alerta de discrepancia entre sensores era una opción de pago; una función de seguridad convertida en accesorio comercial es una decisión ética, no técnica.

**Equipo 4 · Cambridge Analytica (2018).** **Decisión:** diseñar una interfaz en la que el consentimiento de un usuario alcanzaba para entregar datos **de sus amigos**, que nunca instalaron nada. **Numeral:** ACM/IEEE Principio 1 y, en Colombia, **Ley 1581 de 2012**, principios de **finalidad** (los datos se usaron para algo distinto de lo declarado) y **libertad** (no hubo autorización previa, expresa e informada de los afectados). **Momento de parar:** el diseño de esa interfaz, años antes del escándalo. **Lo que hay que exigir:** que digan explícitamente que **era legal** según las reglas de la plataforma y aun así indefendible. Es el caso que prueba que la ley es el piso.

**Equipo 5 · El caso local (está en el taller del estudiante).** El enunciado que reciben: *un equipo desarrolla la app de citas de un consultorio de barrio. Para que el sistema «recuerde» al paciente, guardan nombre, cédula, teléfono y el motivo de la consulta en una hoja de cálculo compartida por enlace público, porque era la manera rápida de que todos pudieran editarla. Nadie le dijo nada a los pacientes.* **Decisión:** usar un enlace público para datos de salud, por comodidad de desarrollo. **Numeral:** Ley 1581 de 2012 —principios de **seguridad**, **acceso restringido** y **libertad**, y el tratamiento reforzado de los **datos sensibles**, entre los que está la salud— y ACM/IEEE 1.03, que menciona explícitamente no degradar la privacidad. **Momento de parar:** cuando se eligió la hoja compartida; la alternativa (permisos por persona) costaba cinco minutos. **Por qué este caso está aquí:** es el que le puede pasar a cualquiera de ellos este semestre, y por eso el curso prohíbe subir nombres y cédulas. La regla del curso no es una formalidad: es esta ley.

## Errores que hay que ver y no dejar pasar

- **«La empresa actuó con negligencia»** → «La empresa» no decide: deciden personas con un cargo, y sin sujeto el caso no enseña nada. Quién tomó la decisión (el rol), en qué momento y con qué información.
- **«El culpable fue el programador que dejó el error»** → En los cuatro casos el software hizo lo que se le pidió; el error, cuando existió, era inofensivo hasta que alguien quitó la barrera. La decisión de diseño o de negocio que convirtió el error en daño.
- **«El código de ética dice que hay que ser responsable»** → Eso no está en ningún numeral; es una paráfrasis vacía y no puntúa el bloque más pesado. El número del principio o del artículo y la cita literal del texto compartido.
- **«Debieron probar mejor el software»** → Es correcto y es tardío: no toca la decisión que creó el riesgo. El momento más temprano en que alguien pudo cambiar el resultado, y qué debía hacer ahí.
- **«Si era legal, no hay problema ético»** → Cambridge Analytica era legal según las reglas de la plataforma y es indefendible. Que apliquen la pregunta 3: ¿aguanta que se sepa? Y que digan quién quedó sin saber.

## Cierre: qué decir en los 3 minutos finales

Tres minutos, una idea, dicha con estas palabras: **en los cuatro casos el software funcionó.** No hubo un error de programación que causara el desastre; falló lo que se pidió construir y el hecho de que nadie con información suficiente lo detuvo. Recuerde el dato de Volkswagen —el ingeniero que ejecutó fue a prisión— porque desarma la idea de que la responsabilidad es siempre del jefe, y cierre con la salida práctica, que es la que se llevan para su vida laboral: no se les pide heroísmo, se les pide **no ser los únicos que saben**. Un correo que deje el riesgo por escrito y escale temprano cambia el caso y protege a quien lo escribe. Callar es la única postura sin defensa. Y aterrice en el curso: la regla de no subir nombres ni cédulas de terceros no es una formalidad del docente, es la Ley 1581 de 2012. Anuncie la sesión 5: hoy el daño tenía víctimas con nombre; la próxima, el daño que no tiene nombre y casi nadie mide.

## Con qué se conecta

Hacia atrás: la sesión 3 dejó identificado el **actor no-usuario** de cada sistema —el afectado que no lo usa—, y hoy ese actor es exactamente quien aparece en los cuatro casos. Hacia adelante: la **sesión 5** extiende el análisis al afectado ambiental, que no tiene voz; la **sesión 6** exige que la ficha del problema del proyecto declare a quién puede perjudicar; la **Clase 13** vuelve sobre impacto social con el proyecto ya construido; y todo el manejo de datos del proyecto queda amarrado a la Ley 1581 desde hoy.
