# CLAVE DOCENTE · Evaluación del Corte 2 (sesión 7)

> **Documento interno.** No va en `Clases/` ni se comparte con el grupo. Contiene las respuestas y las bandas de calificación.

- **Curso:** Introducción a la Ingeniería (FI300101)
- **Cubre:** las Clases 7 a 11 · **Total:** 100 puntos
- **Peso:** 10% de la nota final del curso
- **Reparto:** 6 cerradas (51 pts) y 4 abiertas (49 pts)

Las **6 cerradas** las califica la plataforma. Lo que exige tiempo del docente son las **4 abiertas** (49 puntos, el 49 % de la evaluación): esta clave existe para que esas se califiquen con el mismo criterio en los tres grupos.

---

## Pregunta 1 · Seleccion unica · 7 pts · sale de la Clase 7

**Donde cuesta mas corregir un requisito mal escrito**

**Opciones y respuesta:**

- [x] Después de entregado: hay que rehacer el requisito, el diseño y lo construido, con el usuario ya usándolo y con el daño que el error alcanzó a hacer.
- [ ] En la fase de requisitos: es cuando el documento tiene más detalle y hay más que reescribir.
- [ ] En el diseño: es la fase con más diagramas que actualizar.
- [ ] Cuesta lo mismo en cualquier fase, porque un requisito es una sola línea de texto.

**Respuesta modelo:**

La primera. El costo no es el de reescribir la línea: es el de rehacer todo lo que se apoyó en ella. En la definición del problema cuesta una conversación; después de entregado cuesta órdenes de magnitud más.

**Cómo se califica:**

7 puntos si marca la primera. 0 en cualquier otra.

**Error común (y qué significa si aparece mucho):**

Marcar la cuarta. Confunde el tamaño del texto con el costo del cambio, que es exactamente lo que la tabla de la sesión 7 desmonta.

---

## Pregunta 2 · Seleccion multiple · 8 pts · sale de la Clase 7

**Requisito funcional o no funcional**

**Opciones y respuesta:**

- [x] «Funciona en un computador de siete años.»
- [x] «Se puede usar sin crear cuenta.»
- [x] «No guarda datos personales de los usuarios.»
- [ ] «El usuario puede consultar si un libro está disponible sin ir a la biblioteca.»
- [ ] «El auxiliar puede registrar un préstamo.»

**Respuesta modelo:**

No funcionales: las tres primeras. Son condiciones que la solución debe cumplir, y salen de las restricciones del árbol de la sesión 6. Las dos últimas son funcionales: describen algo que la solución hace, escrito desde el usuario.

**Cómo se califica:**

8 puntos con las tres y ninguna de más. 4 puntos con dos y ninguna de más. 0 si marca una funcional.

**Error común (y qué significa si aparece mucho):**

Marcar la cuarta porque incluye «sin ir a la biblioteca» y suena a condición. No lo es: describe lo que el usuario logra hacer, que es la definición de requisito funcional.

---

## Pregunta 3 · Respuesta escrita · 13 pts · sale de la Clase 7

**Un requisito de su proyecto, con su criterio de aceptacion**

**Lo que dice el enunciado:**

> Abra el documento de su equipo. Copie **un requisito funcional** de su proyecto y escriba debajo su **criterio de aceptación**: un caso concreto con la persona, la tarea y la condición que se puede comprobar (tiempo, cantidad o resultado observable).
>
> No vale «que funcione bien» ni «que sea fácil de usar»: eso no se puede comprobar. Si el criterio que tienen escrito no se puede comprobar, corríjalo aquí y diga que lo corrigió.

**Respuesta modelo:**

Ejemplo con el caso de la biblioteca:

Requisito funcional: «el vecino puede consultar si un libro está disponible sin ir a la biblioteca».

Criterio de aceptación: «una persona que nunca ha visto el prototipo encuentra la disponibilidad de un título que se le dicta, en menos de un minuto y sin que nadie del equipo le indique dónde buscar».

Tiene los tres pedazos: la persona (alguien ajeno), la tarea (encontrar la disponibilidad de un título dictado) y la condición comprobable (menos de un minuto, sin ayuda).

**Cómo se califica:**

13 puntos repartidos así:

- **4 pts** · el requisito es funcional y está escrito desde el usuario. 2 pts si está escrito desde la tecnología («el sistema tendrá una base de datos»).
- **6 pts** · el criterio nombra persona, tarea y condición comprobable. 2 pts por cada pieza presente.
- **3 pts** · la condición se puede comprobar de verdad: hay un número, un conteo o un resultado observable. 0 pts a «que sea intuitivo».

Si el estudiante declara que corrigió un criterio no verificable de su documento, se le dan los 3 pts completos: eso es exactamente lo que se quiere.

**Error común (y qué significa si aparece mucho):**

Copiar el requisito y poner como criterio el mismo requisito en otras palabras. El criterio no repite el qué: dice cómo se comprueba.

---

## Pregunta 4 · Seleccion unica · 8 pts · sale de la Clase 8

**Para que sirve la matriz de criterios**

**Opciones y respuesta:**

- [x] Para hacer explícito el criterio con el que se decide: los pesos se fijan antes de mirar las alternativas, y la decisión queda con su argumento y con lo que se pierde.
- [ ] Para que el resultado del cálculo decida por el equipo, y así nadie tenga que argumentar la decisión.
- [ ] Para demostrar que la alternativa que el equipo prefería desde el principio era la mejor.
- [ ] Para comparar las dos tecnologías y quedarse con la más moderna.

**Respuesta modelo:**

La primera. El orden importa: los pesos se deciden antes de mirar las alternativas, porque si se deciden después se acomodan al favorito. Y la matriz no reemplaza el argumento: lo obliga.

**Cómo se califica:**

8 puntos si marca la primera. 0 en cualquier otra.

**Error común (y qué significa si aparece mucho):**

Marcar la segunda. Es la trampa de la sesión 8: la matriz ordena el razonamiento, no lo sustituye. Quien la usa para no decidir sigue decidiendo, solo que sin decirlo.

---

## Pregunta 5 · Respuesta escrita · 14 pts · sale de la Clase 8

**Que quedo fuera del alcance minimo de su proyecto**

**Lo que dice el enunciado:**

> Abra el documento de su equipo y responda las tres cosas:
>
> 1. El **alcance mínimo** en una frase: lo más pequeño que ya resuelve algo del problema y se puede probar con un usuario real.
> 2. **Dos cosas que quedaron FUERA**, y por qué cada una.
> 3. **Con quién** van a probar en la Clase 12 y **qué tarea** le van a pedir. No «¿le gusta?»: una tarea.
>
> Si su alcance mínimo no resuelve nada por sí solo, no se va a poder probar. Si está así, dígalo y corríjalo aquí.

**Respuesta modelo:**

1. «Una página que muestra si un libro está disponible, consultable desde el celular sin crear cuenta.» Resuelve algo por sí sola: evita el viaje a la biblioteca para averiguar.

2. Fuera: (a) reservas e historial por usuario, porque exigen identificar a la persona y eso rompe el requisito de no guardar datos personales; (b) imágenes de portadas, porque rompen el límite de 200 KB por consulta que el equipo fijó en la sesión 5.

3. Con una vecina que usa la biblioteca y no es del equipo. Tarea: «averigüe si el libro que le voy a dictar está disponible». Se observa en silencio dónde duda, y se cronometra.

**Cómo se califica:**

14 puntos repartidos así:

- **5 pts** · el alcance mínimo resuelve algo por sí solo. 2 pts si es «la primera parte de todo lo que soñamos» y no sirve suelto.
- **5 pts** · dos exclusiones CON su razón (2,5 cada una). Sin razón, la mitad.
- **4 pts** · la validación: persona ajena al equipo (2 pts) y una tarea, no una opinión (2 pts). 0 pts si va a probar con un integrante del equipo, y 0 pts si la pregunta es «¿le gusta?».

Declarar que el alcance estaba mal y corregirlo aquí puntúa completo.

**Error común (y qué significa si aparece mucho):**

Probar con un integrante del equipo. Quien construyó sabe dónde tocar, así que todo le funciona: es la trampa 1 de la sesión 8 y no prueba nada.

---

## Pregunta 6 · Seleccion multiple · 10 pts · sale de la Clase 9

**Que hace utilizable una fuente**

**Opciones y respuesta:**

- [x] Una cita que no se abrió no se puede usar: hay que verificar que el enlace existe y anotar la fecha de consulta.
- [x] «No encontramos nada» es un resultado válido, si se escribe qué se buscó, con qué términos, en qué sitios y qué fue lo más cercano.
- [x] Un asistente de IA sirve para encontrar términos y sinónimos con los que buscar mejor, pero no es una fuente y no se cita.
- [ ] El primer resultado del buscador es el más confiable, porque el buscador ya ordenó por calidad.
- [ ] Si la idea del proyecto ya existe, el proyecto pierde validez y hay que cambiar de tema.

**Respuesta modelo:**

Correctas: las tres primeras. La cuarta es falsa: se filtra por calidad —autor, año, dónde se publicó, si se puede verificar—, no por posición. La quinta es falsa y al revés: encontrar que la idea ya existe confirma que el problema es real y da de dónde partir.

**Cómo se califica:**

10 puntos con las tres y ninguna de más. 5 puntos con dos y ninguna de más. 0 si marca la cuarta o la quinta.

**Error común (y qué significa si aparece mucho):**

Dejar sin marcar la segunda. Cuesta creer que «no encontramos nada» puntúe, pero es un hallazgo cuando está documentado; lo que no puntúa es no haber buscado.

---

## Pregunta 7 · Respuesta escrita · 12 pts · sale de la Clase 9

**Uno de sus antecedentes, y que van a hacer distinto**

**Lo que dice el enunciado:**

> Abra las fichas de antecedentes de su equipo. Escriba **uno** con sus cinco datos: responsable o autor, año, dónde está publicado, qué hace, y **qué le falta para su caso**.
>
> Después, en una frase: **qué van a hacer distinto** ustedes, y por qué eso importa para su problema.
>
> Si el enlace de esa ficha no abre hoy, dígalo. Vale más declararlo que sostener una cita que no se puede verificar.

**Respuesta modelo:**

Ficha: «Biblioteca pública municipal de (ciudad) · 2023 · catálogo en línea publicado en el sitio de la alcaldía · permite consultar disponibilidad por título y autor · le falta para nuestro caso que exige crear una cuenta y que no funciona bien en celular, y nuestra biblioteca no tiene quien administre cuentas.»

Qué haremos distinto: «consulta sin cuenta y pensada para celular, porque nuestros usuarios entran desde el teléfono y no hay nadie que administre registros.»

Cualquier antecedente sirve. Lo que se califica es que los cinco datos estén y que el «qué le falta» sea específico de su caso, no genérico.

**Cómo se califica:**

12 puntos repartidos así:

- **5 pts** · los cinco datos de la ficha, 1 pt cada uno.
- **4 pts** · el «qué le falta para nuestro caso» es específico del proyecto. 1 pt si es genérico («le falta ser más moderno»).
- **3 pts** · el «qué haremos distinto» se apoya en ese faltante y en el contexto propio. 0 pts si es «lo haremos mejor».

Declarar que el enlace no abre no descuenta: descuenta sostener una cita sin verificar. Si el estudiante inventa una ficha, la pregunta es 0 y hay que hablar con el equipo.

**Error común (y qué significa si aparece mucho):**

Traer una ficha sin el «qué le falta». Es el único de los seis campos que obliga a comparar contra el propio problema, y es el que se olvida.

---

## Pregunta 8 · Seleccion unica · 8 pts · sale de la Clase 10

**Que nivel de fidelidad conviene**

**Opciones y respuesta:**

- [x] Baja fidelidad: cuesta un minuto cambiarlo y, al verse como un borrador, la gente se atreve a criticar el flujo.
- [ ] Alta fidelidad: si se ve terminado, la persona lo toma en serio y la crítica es más útil.
- [ ] Funcional: solo se puede saber si el flujo sirve cuando el sistema ya corre de verdad.
- [ ] Media siempre: es el nivel intermedio y por eso es el más seguro en cualquier caso.

**Respuesta modelo:**

La primera. Es la paradoja de la fidelidad: cuanto más terminado se ve un prototipo, peor retroalimentación recibe. Delante de un dibujo a lápiz la gente dice «no entiendo dónde busco»; delante de una pantalla con colores dice «está muy bonito».

**Cómo se califica:**

8 puntos si marca la primera. 0 en cualquier otra.

**Error común (y qué significa si aparece mucho):**

Marcar la segunda. Es la intuición natural y es exactamente la que la sesión 10 contradice con la paradoja de la fidelidad.

---

## Pregunta 9 · Seleccion multiple · 10 pts · sale de la Clase 10

**Que se califica de un prototipo**

**Opciones y respuesta:**

- [x] El estado vacío y el estado de error tienen que estar dibujados: es donde se cae casi todo prototipo.
- [x] Los textos tienen que ser reales («Buscar título»), no relleno: un texto falso esconde el problema de un botón que nadie sabe qué hace.
- [x] Si el prototipo lleva datos, tienen que ser inventados: ni nombres, ni cédulas, ni teléfonos, ni fotos de personas reales, ni del propio equipo.
- [ ] Lo que más pesa es que el prototipo se vea pulido, con colores y tipografías propias.
- [ ] Un prototipo que solo vio el equipo ya sirve como validación, si el equipo se puso de acuerdo.

**Respuesta modelo:**

Correctas: las tres primeras. La cuarta es falsa —pulir no es lo que se califica, y además empeora la retroalimentación—. La quinta es falsa: un prototipo que solo vio el equipo no probó nada, su única razón de existir es que alguien de afuera intente usarlo delante de ustedes.

**Cómo se califica:**

10 puntos con las tres y ninguna de más. 5 puntos con dos y ninguna de más. 0 si marca la cuarta o la quinta.

**Error común (y qué significa si aparece mucho):**

Dejar sin marcar la tercera. La regla de datos inventados se lee como una formalidad del curso y es la Ley 1581 de 2012 de la sesión 4.

---

## Pregunta 10 · Respuesta escrita · 10 pts · sale de la Clase 11

**Una correccion que le hicieron al asistente**

**Lo que dice el enunciado:**

> Abra el registro del taller de hoy. Escriba **una** corrección que su equipo le hizo a lo que devolvió el asistente de IA, y para ella:
>
> 1. Qué propuso el asistente.
> 2. Qué pusieron ustedes en su lugar.
> 3. **De qué sesión salió el criterio** con el que lo corrigieron: el requisito no funcional, el alcance, el indicador, la norma…
>
> Y al final, en una línea: **qué dato NO se le puede pasar** a un asistente de IA en este curso, y por qué.

**Respuesta modelo:**

1. El asistente propuso un aviso automático por correo cuando el libro se devuelva.
2. Lo quitamos: la consulta no pide correo y no se avisa nada.
3. El criterio salió de la sesión 4: pedir el correo es recolectar un dato personal, y la Ley 1581 de 2012 exige autorización previa y finalidad. Además choca con el requisito no funcional de la sesión 7 de usar sin crear cuenta.

Dato que no se le pasa: ningún dato personal de una persona real —nombre, cédula, teléfono, dirección, foto, datos de salud—, porque lo que se escribe en el asistente sale del computador y no vuelve, y ninguna de esas personas autorizó ese tratamiento.

**Cómo se califica:**

10 puntos repartidos así:

- **3 pts** · qué propuso el asistente, concreto.
- **3 pts** · qué pusieron en su lugar, concreto.
- **2 pts** · la sesión de la que salió el criterio, con el criterio nombrado. 1 pt si dice la sesión sin el criterio.
- **2 pts** · el dato que no se le pasa, con su razón. 1 pt sin la razón.

Si la «corrección» es de redacción o de estilo, la primera mitad vale la mitad: lo que se pedía es una corrección de criterio, no de forma.

**Error común (y qué significa si aparece mucho):**

Reportar como corrección un cambio de palabras. La sesión 11 es explícita: se califica lo que corrigieron por criterio, y un equipo que entrega tal cual lo que devolvió el asistente tiene la nota más baja del corte.

---

## Al terminar de calificar

- Cuente en cuántas de las cerradas falló más de la mitad del grupo. Cada una está amarrada a una sesión: eso dice qué sesión hay que retomar, y conviene retomarla en la siguiente aunque el corte ya esté cerrado.
- Los errores comunes de arriba no son adorno: si el error común es la respuesta mayoritaria, el problema fue la explicación en clase, no el grupo.
- Las abiertas se califican con la rúbrica y no por impresión general. Si dos respuestas parecidas reciben notas distintas, el criterio que falló es el suyo.
- Esta evaluación es a libro abierto sobre los documentos del equipo. Un estudiante que no pudo responder las preguntas que piden copiar del documento está diciendo que su equipo no documentó: hable con el equipo antes del corte siguiente, porque el informe final se construye sobre esos mismos documentos.
- Exporte los resultados de la plataforma y guárdelos junto a este documento. Es la evidencia del corte.
