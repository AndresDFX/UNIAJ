# Guion docente — Clase 11: Taller de prototipado inicial con IA

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 7 de 11 · corresponde al tema 11 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **2** (30%) · RAA: **RAA3** · **cierra el corte**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

> **Esta sesión cierra el corte 2 (30 %).** La teoría baja a 17 minutos y la actividad a 27 para que quepan los **20 minutos de evaluación** al final, en ExamLab, sobre las sesiones 7 a 11. Es además la **segunda y última sesión con asistente de IA autorizado** —la otra fue la sesión 3—, y aplica la misma regla, hoy con más peso: se entrega el prompt usado y la lista de lo que se corrigió a mano.

## Objetivos de la clase
- Escribir un **prompt con contexto**: problema, actores y **restricciones** del proyecto.
- Pedir **variantes** en vez de una respuesta, y elegir una con criterio propio.
- Detectar y **corregir lo que la IA no podía saber**: el contexto local y las restricciones.
- Dejar **trazabilidad del uso de IA**: el prompt, lo corregido y lo descartado.

## Hoy avanzamos el proyecto en…

**Prototipo v2 corregido, con el registro del prompt, las variantes, lo corregido a mano y lo descartado — cierra el corte 2**

**Entregable concreto:** el prototipo v2 corregido (PNG en la carpeta del equipo) y el registro completo en el documento del equipo: prompt, las tres variantes, la elegida con su razón, la lista de correcciones y la de descartes

**Herramientas de esta sesión:** Asistente de IA · Excalidraw · Google Drive (Docs y Slides)

> Hoy **sí se usa asistente de IA**, con dos condiciones que son la mitad de la nota: **se entrega el prompt completo** y **la lista de lo que se corrigió a mano**. Cualquier asistente gratuito sirve, sin pagar y sin tarjeta. El prototipo corregido se edita en **Excalidraw** o **draw.io** y el registro va en el **documento del equipo**. Regla que no se negocia: **no se le pasan datos personales a un asistente**, ni de ustedes ni de nadie — lo que se escribe ahí sale del computador.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: mejor y además ilegal - diapositiva 4

El gancho de hoy es un hecho concreto y reproducible, no una hipótesis: si se le pide a un asistente que mejore un prototipo de consulta de disponibilidad de libros, **con altísima probabilidad va a proponer cuentas de usuario con correo y contraseña, y avisos automáticos por correo cuando el libro esté disponible**. Las dos propuestas son razonables en abstracto, están en casi todos los sistemas parecidos del mundo, y las dos son incorrectas para este proyecto: violan el requisito no funcional «sin crear cuenta» de la sesión 7 y convierten al equipo en responsable del tratamiento de datos personales bajo la Ley 1581 de 2012, que vieron en la sesión 4.

El punto que hay que hacer explícito, y que es el eje de toda la sesión: **el asistente no se equivocó por ser malo. Se equivocó porque nadie le dijo las restricciones.** Propuso la solución promedio de internet, que es exactamente lo que hace bien; el problema es que la solución promedio no es la solución de un proyecto con restricciones locales duras. Y lo hizo **con total seguridad**, sin ninguna señal de advertencia, que es la parte peligrosa.

Vale la pena hacerlo en vivo si el tiempo alcanza —dos minutos de pantalla compartida con un prompt sin restricciones—, porque verlo proponer la cuenta de usuario delante de todos vale más que la diapositiva. Si no alcanza, la apertura sola sirve: en el muro, la pregunta «¿cómo puede pasar eso?» produce respuestas que ya contienen la respuesta correcta.

Recuerde el encuadre general del curso, que hoy se cierra: la IA está autorizada en dos sesiones de dieciséis, con la misma regla en las dos —se entrega el prompt y lo que se corrigió—. Hoy esa regla vale la mitad de la nota del taller.

### Qué hace bien y qué hace mal: un mapa honesto - diapositiva 5

Conviene ser preciso y no moralizante, porque estos estudiantes van a trabajar con estas herramientas toda su carrera y lo que necesitan es criterio, no prohibición.

**Hace bien: variantes.** Pedir tres maneras distintas de organizar una pantalla o diez nombres para un botón es un uso excelente. La razón es concreta: un equipo que lleva dos horas mirando su propio dibujo pierde la capacidad de ver alternativas, y abrir opciones es justo lo que más cuesta en ese momento.

**Hace bien: textos y casos de prueba.** Rótulos, mensajes de error y, sobre todo, **listas de casos que a nadie se le ocurrieron** — «¿qué pasa si el usuario escribe el título con una tilde de más?», «¿qué pasa si dos personas piden el mismo libro el mismo día?». Aquí la IA es genuinamente superior a un equipo de primer semestre, porque enumerar casos es exactamente lo que hace bien. Vale la pena decírselo, porque es el uso que más les va a servir en la Clase 12.

**Hace mal: el contexto local.** No sabe que no hay computador en el mostrador, que las voluntarias rotan, que el presupuesto es cero, que la conexión es intermitente. Y como no lo sabe, propone para un contexto que no es el suyo.

**Hace mal: inventar con seguridad.** Esta es la característica que hay que dejar instalada para siempre, y ya la vieron en la sesión 9 con las referencias bibliográficas inexistentes: **un modelo de lenguaje genera texto plausible, y no tiene manera de señalar cuándo lo plausible es incorrecto**. Va a proponer funciones que violan las restricciones del equipo y a veces la ley, con el mismo tono seguro con el que propone las buenas. No hay una alarma; la alarma son ustedes.

### El método: cinco pasos y por qué el primero decide todo - diapositiva 6

**Paso 1: dar el contexto que no puede saber** — el problema en una frase de la sesión 6, quién lo usa, y las restricciones. Es el paso que decide la calidad de todo lo demás, y el que los estudiantes se saltan. La diferencia entre «mejora esta pantalla de biblioteca» y un prompt de diez líneas con las cuatro restricciones escritas no es de grado: es la diferencia entre recibir la solución promedio de internet y recibir tres opciones aplicables.

**Paso 2: pedir variantes, no una respuesta.** «Dame tres maneras distintas de…». El argumento es psicológico y hay que decirlo: una sola respuesta invita a aceptarla —está ahí, está completa, está bien escrita—; tres obligan a comparar, y comparar es donde ellos aportan. Es la matriz de decisión de la sesión 8 aplicada a lo que devuelve un asistente.

**Paso 3: prohibir explícitamente lo prohibido.** «Sin crear cuentas de usuario, sin pedir datos personales, sin instalar nada, sin imágenes.» La regla en cuatro palabras: **si no lo dice, lo va a proponer**. Y aquí hay una lección de ingeniería más general que vale la pena señalar: los requisitos no funcionales que escribieron en la sesión 7 son precisamente lo que hay que poner en el prompt, porque son lo que el mundo no adivina. Un equipo que tiene sus requisitos no funcionales escritos hace un prompt bueno sin esfuerzo; uno que no los tiene, no puede.

**Paso 4: corregir a mano y anotar qué se corrigió.** Esa lista **es el entregable**, y hay que decirlo sin ambigüedad porque cambia cómo trabajan: es la prueba de que pensaron, y es lo que más pesa en la rúbrica de hoy —30 de 100—. Un equipo que no corrigió nada no usó el asistente: lo obedeció.

**Paso 5: declarar el uso.** Qué asistente, para qué, qué se aceptó y qué se descartó. El encuadre correcto no es de sospecha sino de profesión: **declarar el uso de una herramienta es lo normal en ingeniería** —nadie esconde que usó una calculadora o una biblioteca de código—, y esconderlo es lo que constituye la falta. En la vida laboral esto ya es requisito en muchas organizaciones, y acostumbrarse ahora les ahorra un problema después.

### El antes y después, y cómo cierra el corte - diapositivas 7 y 8

La diapositiva de antes y después es el corazón didáctico de la sesión, y hay que recorrerla con una insistencia: **ninguna de las cinco propuestas del asistente era absurda**. Cuentas de usuario, avisos por correo, reservas con historial, portadas, y un mensaje de error estándar: las cinco están en sistemas reales de bibliotecas en todo el mundo. **Las cinco eran incorrectas para este proyecto**, y cada una por una razón distinta que el equipo ya había escrito en una sesión anterior — el requisito «sin cuenta» de la sesión 7, la Ley 1581 de la sesión 4, el alcance mínimo de la sesión 8, el límite de 200 KB de la sesión 5, y la regla de mensajes con salida de la sesión 10.

Ese es el hallazgo que hay que dejar dicho en voz alta, porque justifica todo el corte: **el equipo pudo corregir al asistente porque tenía sus decisiones escritas.** Un equipo sin requisitos no funcionales, sin alcance definido y sin indicador ambiental no habría tenido con qué objetar, y habría aceptado las cinco. La documentación de las sesiones 6 a 10 no era burocracia académica: es lo que hoy les permite ejercer criterio frente a una herramienta que suena más segura que ellos.

**El cierre del corte.** Los últimos 20 minutos son la evaluación del corte 2 en ExamLab, individual y a libro abierto sobre sus propios documentos del equipo. Cubre las sesiones 7 a 11: fases y costo del cambio, requisitos y criterios de aceptación, matriz de decisión y alcance mínimo, calidad de fuentes, fidelidad de prototipos y uso responsable de IA. Que sea a libro abierto es deliberado y conviene explicarlo: **premia al equipo que documentó**, que es exactamente la conducta que el corte entero intentó enseñar.

Hay que decir con claridad, como en la sesión 6, que **ExamLab es la herramienta que usa este curso para las evaluaciones y no es una plataforma oficial de la universidad**; el enlace se comparte en el chat en el momento y, si algo falla, la evaluación se reprograma y se avisa por el canal del curso. Y la advertencia final del taller, que hay que repetir aunque ya esté en la diapositiva: **no se le pasan datos personales a un asistente** —ni propios ni de terceros—, porque lo que se escribe ahí sale del computador y no vuelve.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 11 - Taller de prototipado inicial con IA/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 11
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Qué hace bien y qué hace mal la IA en prototipado
6. Cómo se le pide algo a la IA en este curso
7. La variante de la IA y la corrección del equipo
8. Cómo cierra el corte 2 hoy
9. Taller de hoy: Prototipo v2 con IA
10. Cómo se expone en 3 minutos
11. Para la Clase 12
12. Cierre · Cierra el corte 2 · Nos vemos en la Clase 12

## Plan de clase minuto a minuto (90 min)

### 00:00–00:08 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «Le pedí a un asistente que mejorara el prototipo de la biblioteca. Me devolvió algo mejor... y además ilegal. ¿Cómo puede pasar eso?»

**[Nota docente]:** avise de una vez el reparto de hoy: **teoría 17 min, taller 27 min, exposiciones 15 min y evaluación del corte 2 al final, 20 min en ExamLab**. Que nadie se vaya antes.

**[Nota docente]:** si tiene dos minutos, hágalo en vivo: un prompt sin restricciones sobre su prototipo, y muestre cómo propone la cuenta de usuario. Vale más que la diapositiva.

### 00:08–00:25 · Teoría (17 min) · [Slide 5][Slide 6][Slide 7][Slide 8]

Reparto estricto, hoy no hay margen:

- **4 min** · Qué hace bien y qué mal [Slide 5]. Destaque el uso bueno que más les va a servir: **pedir listas de casos de prueba**.

- **6 min** · Los cinco pasos [Slide 6]. El paso 3 es el que salva la sesión: **si no lo dice, lo va a proponer**. Y diga que el paso 4 vale 30 puntos.

- **5 min** · El antes y después [Slide 7]. Recórralo fila por fila diciendo **de qué sesión sale cada corrección**. Es la diapositiva que justifica el corte entero.

- **2 min** · Cómo cierra el corte [Slide 8]. Diga que es a libro abierto **sobre sus propios documentos** y que ExamLab no es plataforma oficial de la universidad.

### 00:25–00:52 · Taller en salas de grupo (27 min) · [Slide 9]

**2 min** para abrir el asistente, el prototipo y el documento del equipo.

Ritmo sugerido dentro de la sala, dígaselo al repartir:

- 8 min · escribir el prompt **con contexto, restricciones y prohibiciones** y pedir tres variantes.

- 7 min · elegir una con criterio y escribir por qué.

- 8 min · corregir a mano y **anotar cada corrección con la razón**.

- 2 min · dejar el registro y el PNG en la carpeta.

**[Nota docente]:** entre a las cinco salas y pida ver **el prompt**, no el resultado. Un prompt de dos líneas explica por sí solo una mala variante.

**[Nota docente]:** si un equipo dice «quedó perfecto, no corregimos nada», revíselo contra sus propios requisitos no funcionales: siempre hay algo. Es la señal más clara de que aceptaron sin leer.

### 00:52–01:07 · Exposiciones · [Slide 10]

5 equipos × 3 min. **El minuto obligatorio es «qué corregimos y por qué»**, no la variante elegida.

**[Nota docente]:** los cinco enlaces en el chat antes de arrancar. Sea estricto con el tiempo: detrás viene la evaluación y no se puede recortar.

**[Nota docente]:** pregunte a cada equipo **de qué sesión salió una de sus correcciones**. Es la manera de cerrar el corte mostrando que todo estaba conectado.

### 01:07–01:27 · Evaluación del corte 2 en ExamLab (20 min) · [Slide 8]

Cierre las salas y devuelva a todos a la sala principal antes de compartir el enlace.

**[Nota docente]:** el enlace de ExamLab va **en el chat**, no en la diapositiva. Confirme por chat que los cinco equipos lo abrieron antes de arrancar el cronómetro.

Recuerde en voz alta: **individual y a libro abierto sobre sus propios documentos del equipo**. Cubre las sesiones 7 a 11.

**[Nota docente]:** deje claro que **ExamLab no es una plataforma oficial de la universidad** y que si algo falla la evaluación se reprograma y se avisa por el canal del curso. Tenga a mano el plan B: si la herramienta no responde, la evaluación se reprograma — no la improvise por chat.

Quédese con la cámara encendida y el micrófono abierto para dudas de enunciado, sin resolver contenido.

### 01:27–01:30 · Cierre · [Slide 11][Slide 12]

Una idea: **pudieron corregir al asistente porque tenían sus decisiones escritas.** Eso es lo que hicieron en el corte 2.

Anuncie el corte 3: empieza con la **presentación de avances** de la Clase 12, donde el prototipo se prueba con una persona ajena al equipo. Es la única retroalimentación gratis del semestre.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «Mejora esta pantalla de biblioteca para que sea más fácil de usar» | Sin contexto ni restricciones devuelve la solución promedio de internet, que incluye cuentas de usuario y notificaciones por correo. | El problema en una frase, los actores, las restricciones y **la lista de lo prohibido**. Todo eso ya lo tienen escrito de las sesiones 6, 7 y 8. |
| «La IA dijo que esta era la mejor opción» | La recomendación de la herramienta no es un criterio del equipo: es la ausencia de criterio con buena redacción. | El requisito o la restricción en la que se apoya la elección. Si no hay ninguno, todavía no eligieron. |
| «No corregimos nada, quedó perfecto» | Significa que aceptaron sin revisar. Revisado contra los propios requisitos no funcionales, siempre aparece algo. | Revisar la variante punto por punto contra su lista de requisitos, delante de usted. Aparece en dos minutos. |
| Datos reales de personas escritos en el prompt | Lo que se escribe ahí sale del computador y no vuelve: es tratamiento de datos personales sin autorización. | Que lo declaren en el registro y que en adelante usen roles y datos inventados. La corrección es hacia adelante. |
| Un registro escrito al final, de memoria | Las correcciones y sus razones se olvidan en minutos, y sin razones el bloque de 30 puntos no se puede calificar. | Que una persona del equipo escriba el registro **mientras** los otros corrigen. Si se deja para el final, no se hace. |

## Dudas frecuentes del estudiante

**¿Podemos usar IA en las otras sesiones?**

No. Este curso la autoriza en dos sesiones de dieciséis —la 3 y hoy— y en las dos con la misma regla: se entrega el prompt y lo que se corrigió. En las demás el trabajo es propio, y la razón no es desconfianza: es que hay cosas —escribir un requisito, dibujar un flujo, leer una fuente— que solo se aprenden haciéndolas. En el informe final se declara todo uso de IA del semestre.

**¿Cuál asistente hay que usar?**

Cualquiera gratuito. **No se paga nada y no se dan datos de tarjeta**: es regla del curso. Si a alguien se le agota el cupo gratuito, trabaja con el de un compañero compartiendo pantalla, o hace el ejercicio con las variantes del documento de la clase declarándolo así. Nadie pierde nota por no tener acceso.

**¿Es trampa usar IA para el proyecto?**

No, si se declara y si el criterio es suyo. Lo que sería falta es presentar como propio algo que no se revisó ni se entendió — igual que copiar un texto sin citarlo, que ya vieron en la sesión 9. La declaración del uso es lo que convierte una herramienta en una herramienta: **declararla es lo profesional; esconderla es la falta.**

**¿La evaluación del corte es a libro abierto de verdad?**

Sí, individual y con sus propios documentos del equipo a la vista: la ficha del problema, la tabla de requisitos, la matriz de decisión, las fichas de antecedentes y el prototipo. Es deliberado — **premia al equipo que documentó**, que es justo lo que el corte intentó enseñar. Lo que no se puede es resolverla entre varios: es individual.

## Notas operativas

- **El reparto de hoy es distinto y hay que anunciarlo en el minuto 2:** teoría 17 min · taller 27 min · exposiciones 15 min · **evaluación del corte 2, 20 min al final**. Que nadie se vaya antes.
- **Prepare la evaluación en ExamLab con anticipación** y téngala abierta antes de la sesión. El enlace va **en el chat**, nunca en la diapositiva.
- **Cierre las salas de grupo y devuelva a todos a la sala principal** antes de compartir el enlace de la evaluación. Confirme por chat que los cinco equipos lo abrieron antes de arrancar el cronómetro.
- Diga en voz alta que **ExamLab no es una plataforma oficial de la universidad** y que si falla la evaluación se reprograma por el canal del curso. **Tenga el plan B decidido de antemano:** reprogramar, no improvisar por chat.
- En las salas pida ver **el prompt**, no el resultado. Un prompt de dos líneas explica por sí solo la variante mala que recibieron.
- Si un equipo dice que no corrigió nada, revise la variante contra sus requisitos no funcionales **delante de ellos**. Aparece algo en dos minutos y enseña más que el descuento.
- **Ningún estudiante paga nada.** Si a alguien se le agotó el cupo gratuito, comparte pantalla con un compañero o usa las variantes del documento de clase declarándolo.
- Repita la regla dura: **no se le pasan datos personales a un asistente.** Si ya pasó, se declara en el registro y no vuelve a pasar — no hay manera de deshacerlo.
- Sea estricto con el tiempo de las exposiciones: detrás viene la evaluación y no se puede recortar.

## Material de esta clase

- Deck: `Clases/Clase 11 - Taller de prototipado inicial con IA/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 11 - Taller de prototipado inicial con IA/Taller Clase 11 - Prototipo v2 con IA.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 11/Solucion Taller Clase 11 - Prototipo v2 con IA.docx`
- Este guion: `Kit docente/Clase 11/Guion Docente Clase 11 - Taller de prototipado inicial con IA.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
