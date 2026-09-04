# Guion docente — Clase 6: Análisis de problemas tecnológicos del entorno

## Información de la clase
- Asignatura: Introducción a la Ingeniería (FI300101)
- Duración del bloque: **90 min**
- Tipo: Clase virtual sincrónica por Google Meet · Sesión 4 de 11 · corresponde al tema 6 del microcurrículo
- Modalidad: **Virtual (síncrona)** por Google Meet · actividades en plataformas gratuitas en la nube · los 5 equipos trabajan en **salas de grupo**
- Corte **1** (30%) · RAA: **RAA2** · **cierra el corte**
- **Material general para los tres grupos** (SB141B, SB141C, LB141F): sin fechas ni horarios de reloj. El reloj de pared de cada grupo está en su `CALENDARIO_2026-2 - <GRUPO>.md`.
- Enfoque: Aprendizaje basado en competencia + Aprendizaje Invertido · Estrategia: ABPr — Aprendizaje Basado en Proyectos

> **Esta sesión cierra el corte 1 (30 %).** Trae dos cosas que las demás no tienen: la **ficha del problema del proyecto**, que es el producto del corte y gobierna el resto del semestre, y la **evaluación de corte en ExamLab**, que se aplica en los últimos 20 minutos y cubre las sesiones 1 a 6. Por eso el bloque de teoría baja de 45 a 25 minutos: hay que llegar con tiempo, no con la explicación a medias.

## Objetivos de la clase
- Distinguir un **problema** de un **síntoma** y de una **solución disfrazada de problema**.
- Construir el **árbol de causas** de un problema del entorno.
- Escribir una **línea base**: una cifra que se pueda decir hoy sobre el problema.
- Verificar que el problema elegido **cabe en un semestre** con los cuatro criterios.
- Entregar la **ficha del problema** del proyecto del equipo.

## Hoy avanzamos el proyecto en…

**Cerrar el problema del proyecto del semestre: enunciado en una frase, línea base con cifra, árbol de causas, actores y criterio de éxito medible. Es el entregable del corte 1**

**Entregable concreto:** la ficha de cinco bloques en el documento del equipo, más el árbol de causas en Excalidraw exportado a PNG en la carpeta del equipo

**Herramientas de esta sesión:** Excalidraw · Google Drive (Docs y Slides)

> El árbol de causas se dibuja en **Excalidraw** —a mano alzada, que es lo que sirve para pensar— y la ficha se escribe en el **documento del equipo en Drive**. Hoy **no se usa IA**: el problema tiene que salir de lo que ellos conocen del entorno, y un asistente lo devuelve genérico. La evaluación de corte se responde en **ExamLab**, con el enlace en el chat.

## Fundamento teórico para el docente

Esta sección está escrita para dictar la clase **sin consultar otra fuente**, y va dividida por diapositiva: cada bloque dice a qué diapositiva corresponde.

### La pregunta de entrada: la solución disfrazada de problema - diapositiva 4

«En el barrio falta una app» es la frase que un profesor de primer semestre va a oír docenas de veces, y es el error más costoso del curso porque no se ve: parece un problema, tiene sujeto, tiene carencia, y sin embargo ya trae la solución adentro. Si el problema es «falta una app», entonces cualquier app resuelve el problema, y el proyecto se convierte en un ejercicio de construir algo sin saber para qué.

La prueba que conviene enseñar es de una sola pregunta y sirve para toda la vida: **¿esto se podría resolver sin ninguna app?** Si la respuesta es sí —y casi siempre lo es—, entonces el problema es otro y hay que buscarlo. Si el problema verdadero es que la gente no sabe si el libro que necesita está disponible, eso se puede resolver con una app, con una lista pegada en la puerta o con un número de WhatsApp. Que existan varias soluciones posibles es la señal de que el problema está bien escrito.

Recoja las respuestas del muro en los diez minutos de apertura y no las corrija: en el minuto 12, con la primera diapositiva, van a ver ellos mismos que casi todo lo que escribieron era un síntoma o una solución.

### Las tres cosas que se confunden y cómo se escribe un problema - diapositiva 5

**El síntoma** es la señal visible: la queja, la demora, la pérdida. «La gente se queja del servicio» es un síntoma perfecto y un problema inservible, porque no dice de qué se queja ni qué no puede hacer. Los síntomas son útiles —son la pista que lleva al problema— pero atacar un síntoma produce soluciones cosméticas: si el síntoma es que la fila es larga, poner sillas mejora la fila y no toca el problema.

**La solución disfrazada** es la más peligrosa porque se ve profesional. «Falta un sistema», «hay que digitalizar el proceso», «queremos hacerlo con IA». Las tres eligen la herramienta antes de saber qué se va a resolver, y cierran el análisis: una vez que el equipo decidió que va a hacer una app con IA, va a interpretar cualquier hallazgo como confirmación.

**El juicio** es la tercera y la más común en primer semestre: «no hay tecnología en el negocio», «el proceso es muy anticuado». Son opiniones sobre un estado de cosas y no dicen a quién le cuesta qué. Un negocio sin tecnología puede estar funcionando perfectamente; la falta de tecnología no es un problema por sí misma, y esta es una idea que hay que decir en voz alta en un curso de ingeniería de sistemas, porque va contra el reflejo del gremio.

**La fórmula del enunciado**, y conviene dictarla para que la copien: *a QUIÉN le pasa QUÉ, con qué CONSECUENCIA*, más una cifra. Ejemplo bien escrito: «los usuarios de la biblioteca del barrio no saben si un libro está disponible antes de ir, así que hacen viajes en vano; de cada diez visitas, unas cuatro terminan sin préstamo». Tiene sujeto (los usuarios), tiene el qué (no saben la disponibilidad), tiene la consecuencia (viajes en vano) y tiene una cifra. Y no menciona ninguna tecnología, que es lo que deja el espacio para diseñar.

### El árbol del problema: la herramienta que evita las soluciones cosméticas - diapositiva 6

El árbol de problemas es una técnica vieja y muy usada en formulación de proyectos, y para primer semestre tiene una virtud enorme: es un dibujo, así que se puede hacer en quince minutos y se puede discutir señalando con el dedo.

Se dibuja con el **problema en el tronco**, una sola frase. Hacia arriba, las **ramas son los efectos**: lo que se ve, lo que la gente reporta, lo que duele. Hacia abajo, las **raíces son las causas**, y hay dos niveles: las causas directas (por qué ocurre el problema) y las causas de fondo (por qué ocurre cada causa). Se dibuja de arriba hacia abajo y **se lee de abajo hacia arriba**, porque así se ve la cadena completa: esta causa de fondo produce esta causa, que produce el problema, que produce estos efectos.

La regla que hay que repetir hasta el cansancio: **el proyecto ataca una causa, no una rama**. Si el equipo diseña para los efectos, produce algo que alivia la molestia y deja el problema intacto. Y la segunda regla, práctica: dos o tres causas directas, no diez. Un árbol con diez raíces no es un análisis, es una lista de todo lo que se les ocurrió, y con eso no se puede decidir.

El momento de aprendizaje real ocurre en el segundo nivel de raíces, y conviene provocarlo en las salas: cuando el equipo baja de «no hay un registro actualizado» a «el registro se actualiza a mano al final del día y nadie tiene tiempo», ahí aparece por primera vez algo que un estudiante de primer semestre puede efectivamente cambiar en un semestre. Antes de ese nivel, todo se ve demasiado grande.

Un detalle metodológico que ahorra discusiones: si una causa no se puede afectar con nada que el equipo pueda hacer —el presupuesto del municipio, la cultura ciudadana, la ley—, se dibuja igual, pero se marca. Se llama restricción y no es una derrota: es información. Un proyecto que sabe qué no puede cambiar es más serio que uno que promete cambiarlo todo.

### La línea base y los cuatro criterios de viabilidad - diapositivas 7 y 8

**La línea base** es la exigencia que más resistencia genera y la que más valor tiene. Es una cifra sobre el problema **como está hoy**, antes de que el equipo toque nada, y su función es simple: sin ella no hay forma de saber si el proyecto sirvió. En la Clase 16 el informe final va a pedir comparar, y un equipo sin línea base solo puede escribir «mejoramos el proceso», que es una afirmación vacía.

Hay que quitarles de encima la idea de que medir requiere presupuesto o estadística. La línea base de un proyecto de este curso se consigue de tres maneras: **preguntando** a la persona que hace el trabajo, **contando** durante una semana, o **midiendo con un cronómetro** un caso. «La secretaria dedica unas dos horas diarias a confirmar citas por teléfono, según lo que ella misma estima» es una línea base perfectamente aceptable, siempre que se diga que es una estimación y de quién viene. La regla de honestidad es la de la sesión 5, aplicada de nuevo: **cifra con método y fecha, o no va**.

Y hay un diagnóstico gratis escondido en esta exigencia: **si el problema no admite ninguna cifra, está mal delimitado**, y casi siempre es porque es demasiado grande. «La deserción estudiantil» no se puede medir con lo que tiene un equipo de primer semestre; «cuántos de los 30 compañeros de mi grupo no saben en qué semestre pierden el beneficio de la beca» sí. Bajar el problema hasta que se pueda contar algo es la manera más rápida de volverlo abordable.

**Los cuatro criterios** son un filtro y hay que aplicarlos en voz alta a cada problema propuesto, uno por uno. *Abordable* con navegador y herramientas gratuitas: nada que exija comprar equipos, contratar servicios de pago o conseguir permisos institucionales que no van a llegar en un semestre. *Medible*: existe la cifra. *Con acceso a los actores*: pueden hablar esta semana con alguien que vive el problema, sin trámites; este criterio es el que descarta más propuestas y hay que ser firme, porque un proyecto sobre una entidad a la que nadie puede preguntarle nada termina siendo un ejercicio de imaginación con aspecto de proyecto. *Con dueño del problema*: hay una persona o un grupo concreto al que le duele y que reconocería la mejora; si el afectado es «la sociedad», no hay a quién mostrarle el resultado en la Clase 15.

Una advertencia sobre el ánimo del grupo: aplicar estos criterios va a matar algunas ideas ambiciosas y eso frustra. Vale la pena decirles por qué se hace: **es mejor resolver algo pequeño de verdad que simular algo grande**, y en un primer semestre el objetivo es que aprendan a formular y a demostrar, no que salven la ciudad. Un proyecto pequeño y verificable saca mejor nota que uno grandioso e imposible, y hay que decirlo hoy, antes de que se enamoren de la idea.

### Cómo cerrar el corte: la ficha y la evaluación en ExamLab - diapositiva 9

El reparto del tiempo de hoy es distinto al de las otras sesiones y hay que respetarlo: **teoría 25 minutos**, no 45. El corte se cierra con dos entregas y las dos ocurren en clase, así que quedarse largo en la explicación significa aplicar la evaluación con la gente apurada, que es la peor manera de evaluar.

**La ficha del problema** es el producto del corte 1 y conviene decirle al grupo exactamente qué peso tiene en el semestre: a partir de la sesión 7 todo se hace sobre ella. El ciclo de vida de la sesión 7 se aplica a ese problema; el prototipo de las sesiones 10 y 11 resuelve ese problema; la evaluación de impacto de la Clase 13 evalúa esa solución; el informe final de la Clase 16 compara contra esa línea base. Un equipo que hoy escriba una ficha vaga va a arrastrar el problema diez sesiones.

**La evaluación de corte** son los últimos veinte minutos, en ExamLab, individual, y cubre las sesiones 1 a 6. Tres cosas operativas: el enlace va en el chat de la reunión, hay que decir explícitamente que **ExamLab no es una plataforma oficial de la universidad** sino la herramienta que usa este curso, y hay que pedir que cualquier problema para abrirlo se avise **en el chat, en el momento**, no al día siguiente por correo. En un curso virtual el problema técnico no reportado se vuelve un reclamo de nota dos semanas después.

Una última recomendación de manejo del grupo: no anuncie la evaluación al final de las exposiciones, anúnciela en el minuto uno, cuando presente la agenda. La gente organiza su atención distinto cuando sabe que hay una evaluación al cierre, y además evita que alguien se desconecte después de exponer.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 6 - Analisis de problemas tecnologicos del entorno/Presentacion.pptx`. Las etiquetas [Slide N] del plan y las referencias del fundamento apuntan aquí.

1. Portada · Clase 6
2. Agenda de hoy (90 min)
3. Objetivos de la sesión
4. Pregunta de entrada
5. Síntoma, problema y solución disfrazada
6. El árbol del problema
7. La línea base: la cifra de hoy
8. Cuándo un problema cabe en un semestre
9. Cómo cierra el corte 1 hoy
10. Taller de hoy: Ficha del problema del proyecto
11. Cómo se expone en 3 minutos
12. Para la Clase 7
13. Cierre · Cerró el corte 1 · nos vemos en la sesión 7

## Plan de clase minuto a minuto (90 min)

### 00:00–00:10 · Apertura · [Slide 4]

Comparta pantalla antes de que entre el primero:

> «En el barrio falta una app. ¿Eso es un problema, o es una solución a la que todavía no le encontramos el problema?»

**[Nota docente]:** en el minuto 2, con la agenda [Slide 2] en pantalla, **anuncie que hoy cierra el corte y que los últimos 20 min son la evaluación en ExamLab**. No lo deje para el final: cambia cómo prestan atención y evita que alguien se desconecte después de exponer.

**[Nota docente]:** pida que tengan abierto el documento del equipo con las cuatro cosas de las sesiones anteriores (problema inicial, ficha de sistema, regla ética, indicador ambiental). La ficha se arma con eso.

### 00:10–00:35 · Teoría (25 min, comprimida) · [Slide 5][Slide 6][Slide 7][Slide 8][Slide 9]

Reparto estricto. Hoy el reloj manda:

- **6 min** · Síntoma, problema y solución disfrazada [Slide 5]. **Vuelva al muro** y clasifique en voz alta dos o tres respuestas de la apertura. Dicte la fórmula: a quién le pasa qué, con qué consecuencia, más una cifra.

- **7 min** · El árbol del problema [Slide 6]. Dibújelo en vivo con un ejemplo, no lo explique en abstracto. Repita la regla: **el proyecto ataca una causa, no una rama**.

- **5 min** · La línea base [Slide 7]. Lo esencial: se consigue preguntando, contando o cronometrando; y si no hay cifra posible, el problema está muy grande.

- **5 min** · Los cuatro criterios [Slide 8]. Aplíquelos en voz alta a una idea que haya salido en el muro, incluida la parte incómoda de descartar.

- **2 min** · Cómo cierra el corte [Slide 9]. Ficha + evaluación, y que ExamLab no es plataforma oficial de la universidad.

**[Nota docente]:** si va retrasado, recorte los criterios a tres minutos quedándose con *medible* y *acceso a los actores*, que son los dos que más descartan. **No recorte el árbol**: es la herramienta del taller.

### 00:35–00:52 · Taller en salas de grupo · [Slide 10]

**2 min** para repartir: cada equipo trabaja **su propio problema**, el que viene desde la sesión 1. Excalidraw para el árbol, documento del equipo para la ficha.

**15 min** en salas. Entre a las cinco, ~3 min cada una, con **una sola pregunta por sala: ¿cuál es la cifra?** Es lo que falta en el 80 % de las fichas.

**[Nota docente]:** si un equipo tiene un problema que no pasa el criterio de acceso a los actores, **redúzcalo con ellos ahí mismo**, no lo deje para después. La técnica que funciona: pregunte «¿a quién de este problema le pueden preguntar algo esta semana?» y reescriba el problema alrededor de esa persona.

**[Nota docente]:** el árbol de diez raíces es el otro error frecuente. Pida que escojan las dos causas que sí pueden tocar y marquen el resto como restricciones.

### 00:52–01:07 · Exposiciones · [Slide 11]

5 equipos × 3 min. **El minuto obligatorio de hoy es el problema en una frase más la cifra.** Si no hay cifra, dígalo en el momento y déjelo anotado: se corrige esta semana y entra en la sesión 7.

**[Nota docente]:** los cinco enlaces de Excalidraw en el chat antes de arrancar.

**[Nota docente]:** anote las cinco fichas. Son el insumo directo de la sesión 7 y la referencia para el informe final.

**[Nota docente]:** sea puntual con el corte a los 15 min. Lo que sigue es evaluación y no hay margen.

### 01:07–01:27 · Evaluación de corte 1 en ExamLab (20 min)

**[Nota docente]:** pegue el enlace en el chat y verifique **por respuesta de cada uno en el chat** que abrió. No asuma: en virtual el que no abrió se queda callado.

**[Nota docente]:** repita que ExamLab **no es una plataforma oficial de la universidad**, que es la herramienta de evaluación de este curso, y que cualquier problema se avisa **en el chat en el momento**.

Es individual, cubre las sesiones 1 a 6 y se responde en la sesión. Mantenga la reunión abierta con el micrófono libre para dudas de enunciado —no de contenido—.

**[Nota docente]:** si alguien pierde la conexión durante la evaluación, anótelo y resuélvalo con reposición el mismo día. No lo deje para la próxima sesión.

### 01:27–01:30 · Cierre · [Slide 12][Slide 13]

Una idea: **el problema ya está escrito y de aquí en adelante todo se hace sobre esa ficha.** El corte 1 cierra con un producto, no con una nota.

Anuncie la sesión 7: arranca el corte 2 con el **ciclo de vida de los proyectos de ingeniería**, y se aplica al problema de hoy.

## Errores frecuentes y cómo cortarlos en caliente

| Lo que dice el equipo | Por qué no sirve | Qué pedir en su lugar |
|---|---|---|
| «Falta una app / un sistema para X» | Es una solución disfrazada de problema: cierra el diseño antes de empezar y hace que cualquier app «resuelva» el problema. | Que respondan «¿esto se podría resolver sin ninguna app?». Si es sí, el problema es otro y hay que escribirlo. |
| «La gente se queja» / «se pierden libros» | Es un síntoma: la señal visible. Atacar el síntoma produce soluciones cosméticas. | A quién le pasa qué, con qué consecuencia. Y la cifra. |
| Una cifra sin decir de dónde salió | No se puede volver a medir en la Clase 16, así que no sirve como línea base. | Número, unidad y método: preguntando a quién, contando qué, o cronometrando cuándo. |
| Un árbol con diez raíces | Es una lista de todo lo que se les ocurrió, no un análisis, y con eso no se puede decidir qué atacar. | Dos o tres causas directas, su segundo nivel, y las que no pueden cambiar marcadas como restricciones. |
| «El éxito es tener 200 usuarios en la app» | Mide la adopción de la solución, no la resolución del problema. Se puede tener 200 usuarios y el problema intacto. | El criterio con la misma medición de la línea base: de X a Y, medido así. |

## Dudas frecuentes del estudiante

**Nuestro problema es muy grande y nos dijeron que lo bajemos. ¿No es peor un proyecto pequeño?**

No: saca mejor nota. En este curso se evalúa que sepan formular, medir y demostrar, no el tamaño de la ambición. Un problema pequeño resuelto y medido de verdad es un proyecto completo; uno grande simulado es una presentación bonita sin evidencia. Y el informe final de la Clase 16 pide comparar con la línea base: eso solo se puede hacer con algo acotado.

**¿Cómo conseguimos una cifra si no tenemos acceso a datos?**

Preguntando, contando o cronometrando. Tres preguntas a la persona que hace el trabajo, un conteo de una semana con una hoja, o el tiempo de un caso medido con el celular. Se acepta una muestra pequeña y una estimación, **siempre que digan que lo es y de dónde viene**. Lo que no se acepta es un número sin origen.

**¿Podemos cambiar el problema después?**

Sí, pero cuesta. Todo lo que sigue se construye sobre esta ficha: el ciclo de vida de la Clase 7, el prototipo de la 10 y la 11, el impacto de la 13, el informe de la 16. Un cambio en la Clase 8 es un ajuste; en la Clase 12 es empezar de nuevo. Por eso vale la pena discutirlo hoy hasta que quede.

**¿Y si ya sabemos qué tecnología queremos usar?**

Perfecto, pero no va en el enunciado del problema. Escriban el problema sin mencionarla y en la sesión 10 la eligen con argumentos. Si la tecnología está en la frase del problema, ya no hay nada que diseñar: solo queda ejecutar una decisión que nadie justificó.

**¿La evaluación de corte cubre todo, incluidas las lecturas?**

Cubre las sesiones 1 a 6: qué es y qué no es la ingeniería, historia y hitos, los cinco elementos de un sistema, los principios éticos y las tres normas colombianas, las cuatro etapas de la huella, y problema contra síntoma. Se responde en ExamLab en los últimos 20 minutos de la sesión, es individual, y si el enlace no le abre lo avisa **en el chat en el momento**.

## Notas operativas

- **El reparto de tiempo de hoy es distinto: teoría 25 min, no 45.** Quedarse largo en la explicación significa aplicar la evaluación de corte con el grupo apurado. Ponga una alarma a los 35 minutos.
- **Anuncie la evaluación de corte en el minuto 2**, con la agenda en pantalla. La gente organiza la atención distinto sabiendo que hay evaluación al cierre, y así nadie se desconecta después de exponer.
- **Prepare el enlace de ExamLab antes de la sesión** y verifique que abre. Al pegarlo, pida que cada uno confirme en el chat que entró: en virtual, el que no pudo abrir se queda callado.
- Diga en voz alta que **ExamLab no es una plataforma oficial de la universidad**: es la herramienta de evaluación de este curso.
- Si alguien pierde la conexión durante la evaluación, anótelo y **resuélvalo el mismo día**. Un problema técnico no atendido se vuelve un reclamo de nota dos semanas después.
- En las salas, haga **una sola pregunta: ¿cuál es la cifra?** Es lo que falta en la mayoría de las fichas y es el 25 % de la rúbrica.
- **Anote las cinco fichas** al terminar las exposiciones. Son el insumo directo de la sesión 7 y la referencia del informe final.
- Hoy no se usa IA: el problema tiene que salir del entorno que ellos conocen, y un asistente lo devuelve genérico y sin cifra.

## Material de esta clase

- Deck: `Clases/Clase 6 - Analisis de problemas tecnologicos del entorno/Presentacion.pptx`
- Taller del estudiante: `Clases/Clase 6 - Analisis de problemas tecnologicos del entorno/Taller Clase 6 - Ficha del problema del proyecto.docx`
- Solución del taller (**solo docente**): `Kit docente/Clase 6/Solucion Taller Clase 6 - Ficha del problema del proyecto.docx`
- Este guion: `Kit docente/Clase 6/Guion Docente Clase 6 - Analisis de problemas tecnologicos del entorno.docx`

> **Recordatorio de datos personales:** ninguna actividad de este curso sube nombres, cédulas, teléfonos ni fotos de terceros. Si el caso del equipo los trae, se usa el rol («la dueña de la papelería», «el auxiliar de la biblioteca»).
