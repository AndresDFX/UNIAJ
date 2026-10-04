# Guion docente — Clase 1: Introducción a arquitecturas cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Ubicar el curso como diseño de arquitecturas cloud al servicio del PI CloudLite App.
- Cerrar el dominio del PI en una ficha de cinco bloques, con capacidades de negocio y no piezas tecnicas.
- Dejar el dominio y alcance del PI escritos y compartibles.

## Hoy avanzamos el PI en…
**Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases**

**Entregable concreto:** Ficha PI de 5 bloques + C4 Context en Mermaid renderizado en la plataforma (boceto previo en Excalidraw/draw.io)

**Herramienta:** Navegador · editor de diagramas del curso · boceto libre (papel o Excalidraw) opcional

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] La ficha de dominio de 5 bloques** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La ficha de dominio es individual, tiene cinco bloques rotulados y siempre en el mismo orden, y no vuelve a cambiar en el resto del semestre.
  - PROBLEMA nombra en tres frases quien sufre la situacion, como se resuelve hoy sin el sistema y una cifra medible del dolor; sin esa cifra el problema es una opinion y no algo que un diseno pueda mejorar o empeorar de forma verificable.
  - ACTORES son las personas que usan el sistema, cada una con una frase de que espera obtener, y en el mismo bloque los dos o tres sistemas externos con los que intercambia informacion (un proveedor de identidad, un servicio de correo, una pasarela de pagos)
  - Esos sistemas externos son exactamente los que despues aparecen como System_Ext en el diagrama C4 Context, asi que se escriben aqui ANTES de dibujar.
  - CAPACIDADES son los verbos de negocio que el sistema debe permitir (reservar, publicar, cancelar, notificar), nunca piezas tecnicas como login o cache, porque las capacidades describen el fin y la tecnologia es solo el medio.
  - NOTAS:
  - DOMINIO fija en una linea el problema de negocio elegido (AgendaU, BiblioLite, InventarioLab, TurnosClinica, EventosCampus u otro del mismo tamano); un dominio generico (una red social, una tienda en linea sin mas detalle) hace imposible evaluar las decisiones de las clases siguientes, porque no hay nada concreto que arquitecturar.
  - FUERA DE ALCANCE cierra la ficha nombrando tres cosas que el sistema no hara este semestre; ese bloque evita que el alcance crezca sin control clase a clase.

**[Slide 5] Qué es arquitectura cloud (mapa mental)** — 6 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Arquitectura de software es el conjunto de decisiones estructurales que resultan costosas o imposibles de cambiar despues: como se dividen los componentes
  - Como se comunican, donde se despliegan y que atributos de calidad se priorizan cuando entran en conflicto.
  - La prueba practica para saber si una decision es arquitectonica consiste en preguntar cuanto costaria revertirla en tres meses.
  - Cambiar el color de un boton no es arquitectura; cambiar de base de datos relacional a documental si lo es, porque arrastra el modelo de datos, las consultas, el codigo de acceso y las pruebas.
  - El stack es la lista de tecnologias concretas; la arquitectura es la estructura y las razones.
  - Dos proyectos pueden usar el mismo stack y tener arquitecturas opuestas: uno con un solo proceso que hace todo, otro con tres servicios que se comunican por red.
  - Los atributos de calidad son las propiedades medibles que el sistema debe exhibir, y son el vocabulario con el que se justifica cualquier decision.
  - Los cuatro que este curso usa de forma permanente son rendimiento, disponibilidad, seguridad y costo.
  - Disponibilidad se expresa como porcentaje de tiempo en que el sistema responde, y ahi el numero si es aritmetica exacta: 99 % permite unas 7 horas de caida al mes, 99,9 % (los llamados tres nueves) alrededor de 43 minutos, y 99,99 % poco mas de 4 minutos.
  - El punto central es que estos atributos compiten entre si: mas disponibilidad exige redundancia, la redundancia cuesta dinero, y por eso la arquitectura es sobre todo el oficio de elegir que se sacrifica.
  - El cambio economico que esto produce es lo relevante para la arquitectura, porque la infraestructura deja de ser una compra que se hace por adelantado y se amortiza a largo plazo, y pasa a ser un gasto operativo que cambia con cada decision de diseno.
  - NOTAS:
  - Nadie puede contestar, porque el stack no contiene esa informacion; las respuestas viven en la arquitectura.
  - Hacer visible ese vacio en los primeros veinte minutos ahorra tres semanas de malentendidos.
  - Nube no significa internet ni «el servidor de otra persona».
  - (No se proyecta) Esa asimetria de costo es la razon de existir de la materia: si el docente no la instala el primer dia, el curso se percibe como una coleccion de diagramas decorativos y el estudiante concluye que la arquitectura es documentacion que se produce para la nota.
  - (No se proyecta) Conviene separar de entrada dos cosas que el estudiante confunde siempre: el stack tecnologico y la arquitectura.
  - (No se proyecta) Una forma rapida de demostrarlo es escribir en el tablero «React + Node + PostgreSQL» y preguntar al curso cuantos usuarios simultaneos soporta eso, o que ocurre si la base de datos deja de responder.
  - (No se proyecta) Rendimiento se expresa en tiempo de respuesta: una convencion de usabilidad ampliamente aceptada dice que una interaccion web se siente inmediata por debajo de 100 milisegundos, aceptable hasta unos 300 y claramente lenta por encima de 1 segundo; son convenciones, no leyes fisicas, y conviene decirlo asi.
  - (No se proyecta) Vale hacer ese calculo en el tablero, porque 43 minutos al mes es un dato que el estudiante recuerda, mientras que la expresion «alta disponibilidad» no significa nada.
  - (No se proyecta) Es un modelo operativo con cinco rasgos que conviene enunciar tal cual, porque son el estandar con el que se define el termino: autoservicio bajo demanda, es decir que quien necesita recursos los aprovisiona sin pedir permiso ni esperar dias; acceso amplio por red; agrupacion de recursos, donde el proveedor comparte hardware fisico entre muchos clientes mediante virtualizacion, tema de la Clase 3; elasticidad rapida, con capacidad que sube y baja en minutos y no en semanas; y medicion del servicio, o pago por lo consumido.
  - (No se proyecta) Por eso en la nube el costo se convierte en un atributo de calidad tecnico y no solo administrativo, idea que el curso retoma de forma explicita en la Clase 10.

**[Slide 6] CloudLite App — el hilo conductor** — 6 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El diagrama de contexto correcto tiene una sola caja llamada CloudLite Turnos, tres actores alrededor (el cliente que reserva
  - El barbero que consulta su agenda del dia y el administrador que configura horarios y precios) y dos o tres sistemas externos con la flecha etiquetada: una pasarela de pagos
  - Con la etiqueta «envia solicitud de cobro y recibe confirmacion»; un proveedor de correo, con la etiqueta «envia recordatorio de turno»; y quizas un servicio de mapas.
  - Nada mas: la API, la base de datos y el almacenamiento de fotos no aparecen todavia porque son interiores.
  - Un sistema que depende de una pasarela de pagos hereda su disponibilidad, y esa herencia es una decision arquitectonica aunque nadie la haya escrito.
  - NOTAS:
  - Aterricemos en CloudLite App, el proyecto integrador que atraviesa las quince clases.
  - Supongamos que un estudiante elige como dominio la gestion de turnos de una barberia.
  - (No se proyecta) El valor de ese diagrama de cinco o seis elementos esta en que obliga a responder dos preguntas que el estudiante no se habia hecho: quien exactamente usa esto y de que terceros depende para funcionar.

**[Slide 7] De dominio a arquitectura (mini-método)** — 6 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El modelo C4 es la notacion que este curso usa para dibujar arquitectura, y su virtud es ofrecer cuatro niveles de zoom con reglas claras sobre que se muestra en cada uno, en lugar de un unico diagrama que mezcla todo.
  - Nivel 1, Contexto: el sistema es una sola caja negra y alrededor aparecen unicamente las personas que lo usan y los sistemas externos con los que intercambia informacion.
  - Nivel 2, Contenedores: se abre esa caja y se ven las aplicaciones, servicios y bases de datos que la componen.
  - Nivel 3, Componentes: se abre un contenedor y se ven sus modulos internos.
  - Nivel 4, Codigo: clases y funciones, que en la practica casi nunca se dibuja porque el codigo mismo ya lo documenta.
  - El segundo artefacto de hoy es la ficha con cuatro capacidades y el problema en tres frases.
  - Una capacidad se escribe como un verbo de negocio que el usuario puede ejecutar, no como una pieza tecnica: «reservar un turno disponible», «cancelar o reprogramar hasta dos horas antes», «consultar la agenda del dia» y «cobrar un anticipo» son capacidades
  - «tener login con JWT», «usar cache» o «tener panel administrativo» no lo son, porque son medios y no fines.
  - El limite de cuatro capacidades es una decision pedagogica deliberada y no una regla de la industria: con cada estudiante trabajando de forma individual durante doce semanas, un alcance de ocho capacidades garantiza que el proyecto no llegue a ninguna parte.
  - El enunciado del problema debe nombrar a quien le duele y que pierde hoy, con alguna cifra aunque sea estimada: «la barberia agenda por mensajeria instantanea
  - Pierde alrededor de tres turnos diarios por doble reserva y no tiene registro de cuantos clientes no se presentaron».
  - NOTAS:
  - Un problema sin afectado concreto y sin magnitud produce arquitecturas que nadie puede evaluar, porque no hay contra que comparar.
  - (No se proyecta) Hoy se trabaja unicamente el nivel 1, y la regla es estricta: si en el diagrama de contexto aparecen las palabras PostgreSQL, Docker o Redis, el diagrama esta mal, porque eso es interior del sistema y corresponde al nivel 2 de la Clase 4.

**[Slide 8] Ejemplo de diagrama C4 - nivel Context** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un diagrama de contexto tiene tres tipos de elemento: Person, System y System_Ext.
  - Cada flecha lleva un verbo de negocio, por ejemplo «Cliente reserva turno en CloudLite Turnos» o «CloudLite Turnos envia recordatorio por el proveedor de correo».
  - El error mas comun es dibujar la base de datos o la API en este nivel: son piezas internas y pertenecen al nivel 2, Containers.
  - Un Context legible tiene entre 4 y 8 elementos; si tiene mas, la caja del sistema ya se esta abriendo.
  - NOTAS:
  - En el diagrama proyectado (System, dos Person, System_Ext) el nivel Context muestra el sistema como UNA sola caja, sin abrir por dentro.
  - PREGUNTAS FRECUENTES Y CIERRE CONCEPTUAL ()
  - Respuesta: es una diferencia de alcance y de reversibilidad, no de naturaleza
  - Arquitectura son las decisiones que afectan a todo el sistema y son caras de revertir, diseno son las decisiones internas de un componente que se pueden cambiar sin tocar a los demas.
  - La segunda: por que no usamos una cuenta real de un proveedor de nube.
  - La tercera: cuantas cajas debe tener mi diagrama.
  - Respuesta: en el nivel de contexto, entre cuatro y ocho elementos en total; si hay veinte, es casi seguro que se colaron piezas internas.
  - La primera: cual es la diferencia entre arquitectura y diseno.
  - Respuesta, y hay que darla sin disculparse: porque este curso evalua razonamiento arquitectonico y no el manejo de una consola que cambia de aspecto cada semestre; ninguna actividad exigira tarjeta de credito ni cuenta de pago, todo se hace con draw.io, Excalidraw, Killercoda y el nivel gratuito de GitHub Actions, y quien aprende a justificar un trade-off lo aplica luego en cualquier proveedor en una tarde.
  - (No se proyecta) Es el mismo modelo C4 explicado arriba, ahora aplicado con nombres concretos, y sirve de puente directo hacia la pregunta 2 del taller en la plataforma del curso (el diagrama Mermaid que cada estudiante entrega hoy).

**[Slide 9] El C4 Context en Mermaid: el sistema es una sola caja** — 12 vinetas.

**[Slide 10] Ejemplo de diagrama C4 — nivel Context** — 4 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 1 - Introduccion a arquitecturas cloud/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 1 · Introducción a arquitecturas cloud
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. La ficha de dominio de 5 bloques
5. Qué es arquitectura cloud (mapa mental)
6. CloudLite App — el hilo conductor
7. De dominio a arquitectura (mini-método)
8. Ejemplo de diagrama C4 - nivel Context
9. El C4 Context en Mermaid: el sistema es una sola caja
10. Ejemplo de diagrama C4 — nivel Context
11. Del boceto al código Mermaid
12. Clase 1 · cierre conceptual

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3]
Di casi literal:
> "Hoy avanzamos el PI CloudLite App en: Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases. Entregable concreto: Ficha PI de 5 bloques + C4 Context en Mermaid renderizado en la plataforma (boceto previo en Excalidraw/draw.io). Teoría breve y luego taller; no es un lab suelto."

**[Nota docente]:** pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.

**[Nota docente]:** pregunta de arranque (1 min) para detectar estudiantes rezagados antes de avanzar:
> "¿En qué quedó tu CloudLite la clase pasada?"

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **Qué es arquitectura cloud (mapa mental)** · [Slide 5]
- **CloudLite App — el hilo conductor** · [Slide 6]
- **De dominio a arquitectura (mini-método)** · [Slide 7]

**[Nota docente]: ninguna se salta** — cada una de esas diapositivas es el mecanismo con que se
resuelve al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente», ya dividido
por diapositiva: esa sección está escrita para que puedas dictarla sin consultar otra fuente.

**[Nota docente]:** cada 8–10 min amarra al artefacto («esto es lo que van a dejar hoy en su informe/diagrama/repo»)
y pide un estudiante voluntario para usar SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 11]
Herramienta del día: **Navegador · editor de diagramas del curso · boceto libre (papel o Excalidraw) opcional**.
**Demo que usted debe poder repetir:** Dibujar en vivo el C4 Context de un CloudLite de ejemplo

1. Abra draw.io en blanco y dibuje UNA caja al centro rotulada «CloudLite App».
2. Agregue 2 monigotes a la izquierda (Usuario final, Administrador) con flechas rotuladas «consulta», «administra».
3. Agregue 1 caja gris a la derecha rotulada «Pasarela de pagos (externo)» y una flecha «cobra».
4. Diga en voz alta: «no dibuje que hay ADENTRO de la caja; eso es Clase 4».

**Referencia del resultado:** C4 Context de la demo (el mismo de `Capturas/demo-clase01.png`). Si la red falla o prefiere no dibujar a mano, pegue este codigo en la pregunta de diagrama de la actividad y proyectelo renderizado; tambien sirve para volver a generar la imagen en cualquier editor que soporte Mermaid.

```mermaid
C4Context
    title CloudLite App - nivel Context (demo de clase)
    Person(usuario, "Usuario final", "Consulta y usa el servicio")
    Person(admin, "Administrador", "Configura y opera")
    System(cloudlite, "CloudLite App", "El sistema completo, como caja negra")
    System_Ext(pagos, "Pasarela de pagos", "Servicio de terceros")
    Rel(usuario, cloudlite, "consulta", "HTTPS")
    Rel(admin, cloudlite, "administra", "HTTPS")
    Rel(cloudlite, pagos, "cobra", "API REST sobre HTTPS")
```


**[Nota docente]:** narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 1/Capturas/`.
Cierra la demo diciendo:
> "Copien la estructura, no el dominio de mi ejemplo."

**Si se hace el taller, cierra la demo en la plataforma del curso** (sin diapositiva: el flujo está en el `Taller … .docx`) — es el paso que el estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, pegalo en la pregunta de diagrama y muestralo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `C4Context`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en la plataforma del curso** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de la plataforma del curso.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 C4 Context de la demo en vivo: asi debe quedar el tablero al terminar [[captura: demo-clase01.png]]


### 55–100 · Taller guiado PI (individual) · opcional · sin diapositiva
**[Nota docente]:** el taller es **opcional** y ya no está en el deck: si se hace hoy, comparte el `Taller … .docx`
de `Clases/Clase 1 - Introduccion a arquitecturas cloud/` (los pasos también están en la sección «Actividad / taller» de este guion). Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas
a ver hoy. A los 80 min anuncia:
> "Faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador."

### 100–115 · Comprobación y evidencias
**[Nota docente]:** haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - Introduccion a arquitecturas cloud.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 12]
Di:
> "Queda avanzado: Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases. Criterio de éxito: el estudiante explica su artefacto en 60 s. Entrega domingo 23:59 en la plataforma del curso. Siguiente hito del PI según el plan."


## Actividad / taller (detalle)
1. Paso 1: elija un dominio concreto entre AgendaU, BiblioLite, InventarioLab, TurnosClinica o EventosCampus (o uno propio del mismo tamano) y escriba en la pregunta 1 el problema en 2 o 3 frases, diciendo QUIEN lo sufre con un rol concreto y COMO se mide con una cifra, aunque sea estimada; verifique que su enunciado no sirva igual para cualquier otro sistema, porque entonces el dominio todavia es generico.
2. Paso 2: complete en la pregunta 2 la ficha de cinco bloques (DOMINIO, PROBLEMA, ACTORES, CAPACIDADES, FUERA DE ALCANCE) con 3 a 5 capacidades en la forma verbo mas objeto de negocio, 2 a 3 actores con lo que espera cada uno, los sistemas externos dentro del bloque ACTORES, y lo que el sistema no hara este semestre; verifique que ninguna capacidad nombre tecnologia.
3. Paso 3: dibuje primero el boceto del C4 Context en Excalidraw o draw.io, que es donde se piensa el modelo, y despues pidale a una IA que lo traduzca a Mermaid («convierta este diagrama a Mermaid usando C4Context»); peguelo en la pregunta 3 y verifique en el diagrama ya renderizado que el sistema sea UNA sola caja, que no aparezca ninguna caja interna (eso es la pregunta 13) y que cada flecha lleve verbo y protocolo.
4. Paso 4: elija en la pregunta 4 dos atributos de calidad de los cuatro del curso, escriba por que pesan en SU dominio y como los mediria con un numero y una unidad, y cierre diciendo cual sacrificaria y que gana a cambio; revise ademas que los nombres de actores y de sistemas externos sean EXACTAMENTE los mismos en la ficha y en el diagrama, porque las preguntas 12 a 15 los reutilizan. Las preguntas 5 a 15 se resuelven en las Clases 2, 3 y 4: la actividad se entrega completa al cierre del Corte 1, no hoy.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por el estudiante (muestreo).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Dominio vago tipo «una red social» o «un e-commerce»: sin problema concreto no hay decisiones que tomar. Exija sector, usuario y dolor observable.
- Dibujar lo que hay DENTRO del sistema en el nivel Context (base de datos, API). Se corrige recordando que eso es el nivel Containers de la Clase 4.
- Confundir capacidad con pantalla: «tener un login» no es capacidad; «autenticar usuarios» si.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Cual es la diferencia entre arquitectura y stack tecnologico?
1. Que va DENTRO y que va FUERA de la caja en un diagrama C4 Context?
1. Digan una capacidad de su CloudLite que NO sea una pantalla.

## Solución del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 1/Quiz Clase 1 - Introduccion a arquitecturas cloud.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 1/Quiz Clase 1 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase01.png | receta: 1) Abre Navegador · editor de diagramas del curso · boceto libre (papel o Excalidraw) opcional y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 1/Capturas/demo-clase01.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase01.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 1/Capturas/evidencia-clase01.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- La entrega oficial se hace respondiendo las preguntas abiertas del taller en la plataforma del curso. El documento/ficha en Word o Google Docs es opcional, solo para que el estudiante conserve sus respuestas; lo que califica es lo que quede escrito en las preguntas de la actividad.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
