# Solucion — Actividad del Corte 1, preguntas 5 a 7 (matriz de modelos de servicio, ADR-001 y consecuencias)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las tres preguntas que corresponden a la Clase 2, resueltas sobre el mismo dominio **BiblioLite** con el que se resolvieron las preguntas 1 a 4. La continuidad es deliberada: el ADR-001 de la pregunta 6 decide sobre las capacidades que quedaron escritas en la ficha de la pregunta 2, y esta solucion solo sirve para calificar si se lee como continuacion de aquella.

> Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1, que es **una sola para las Clases 1 a 4** y se entrega completa al cierre del corte. Hoy se resuelven las preguntas **5, 6 y 7**; las 8 a 15 corresponden a las Clases 3 y 4. El estudiante puede volver sobre las anteriores: la plataforma guarda y no cierra la actividad hoy.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 2 - Modelos de servicio IaaS PaaS SaaS/`
- Configuracion en la plataforma: `Kit docente/Clase 2/Taller en ExamLab - Clase 2 (configuracion).md`
- Hito del PI: Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve
- Entregable: ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio
- **Estas preguntas: 25.0 puntos** en 3 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 5 | Matriz IaaS / PaaS / SaaS para su dominio | `abierta` | 6.25 |
| 6 | ADR-001: modelo de servicio dominante de CloudLite | `abierta` | 12.5 |
| 7 | Consecuencias del ADR-001 | `abierta` | 6.25 |

---

## Pregunta 5 · Matriz IaaS / PaaS / SaaS para su dominio · 6.25 pts

### Respuesta esperada

| Criterio | IaaS | PaaS | SaaS |
|---|---|---|---|
| **Control** | Total: puedo instalar la libreria nativa que lee el codigo de barras del lomo del libro y compilarla en la maquina. | Medio: elijo runtime y version de Node, no el sistema operativo. Esa libreria tiene que existir como paquete puro o no la uso. | Ninguno: uso el modulo de prestamos que traiga el proveedor y BiblioLite deja de ser un sistema propio. |
| **Costo cualitativo** | Bajo en factura y alto en horas mias: una instancia pequena aguanta los 400 prestamos al mes, pero los parches los pago yo. | Medio: el nivel gratuito cubre la demo y el semestre completo; sube si la semana de matricula obliga a mas de una instancia. | Alto y por usuario: pagar licencia por cada uno de los auxiliares no lo sostiene el presupuesto de una biblioteca universitaria. |
| **Operacion** | **Yo** opero sistema operativo y runtime: parches, version de Node, arranque del servicio. El proveedor responde por hardware y red. | **El proveedor** opera sistema operativo y runtime; **yo sigo respondiendo** por el codigo de BiblioLite, sus permisos y los datos de los prestamos. | **El proveedor** opera todo el stack; **yo sigo respondiendo** por quien tiene cuenta, que rol le doy y que datos cargo. |
| **Time-to-demo** | Dias: crear la instancia, instalar runtime, configurar servicio y proxy antes de ver la primera consulta de disponibilidad. | Horas: un push del repositorio y el endpoint de disponibilidad responde. Es lo unico que cabe en doce semanas. | Minutos, pero no demuestra nada mio: la demo seria del producto del proveedor y no de BiblioLite. |

La fila que decide la nota es **Operacion**, y conviene leerla antes que las otras tres. En los tres modelos la responsabilidad no desaparece: se reparte. Lo que cambia de columna a columna es **cuanto** se reparte, y lo que NO cambia nunca es que el equipo responde por su propia aplicacion, por sus permisos y por sus datos. Una matriz que en la columna de PaaS o de SaaS escriba «el proveedor se encarga de todo» esta mal aunque las otras once celdas esten bien, porque es exactamente la creencia que la clase existe para corregir.

Las otras tres filas se califican por una sola cosa: que hablen de BiblioLite. «Mas control» es una celda vacia; «puedo instalar la libreria que lee el codigo de barras» es una celda llena, porque nombra una capacidad de la ficha y dice que se puede o no se puede hacer con ella. El mismo criterio para el costo: no se pide ningun precio, se pide que diga bajo, medio o alto **y por que en este dominio**.

Un detalle que suele confundir al calificar: es correcto que la matriz mencione **SaaS satelite** para identidad y correo, porque esos dos sistemas externos ya estaban en el C4 Context de la pregunta 3 y se consumen como servicio. Eso no contradice nada: la matriz compara donde vive **la aplicacion propia**, no de donde sale cada dependencia.

### Como calificar

- 2 pts la matriz con los **cuatro criterios en el orden pedido** (control, costo, operacion, time-to-demo) y las **cuatro columnas** con los encabezados exactos.
- 3 pts que las **doce celdas** de comparacion hablen del dominio propio y de sus capacidades. Se descuenta **por cada fila** escrita en abstracto: una fila entera de teoria general vale 0 de esos 3 pts.
- 1.25 pts que la fila de **Operacion** reparta bien la responsabilidad en los tres modelos. **Cero en este criterio** si en PaaS o en SaaS dice que el equipo deja de responder por su aplicacion, sus permisos o sus datos.
- No se descuenta por celdas de dos lineas; si se descuenta por celdas de un parrafo. El limite es parte del ejercicio: obliga a decidir que es lo esencial de cada casilla.
- No se exige ningun precio y no se premia haberlo puesto. Un numero de factura inventado no suma; si contradice la columna (por ejemplo SaaS mas barato que IaaS sin explicar por que) se descuenta de los 3 pts.

### Errores frecuentes y que hacer

- «En PaaS el proveedor se encarga de todo». Es el error central del dia. Se corrige en el momento con una pregunta: si manana un estudiante ve los prestamos de otro por un permiso mal puesto, ¿a quien reclama la biblioteca? El proveedor no escribio ese permiso.
- Matriz correcta pero generica, copiada de cualquier comparativa de internet. Se detecta rapido: si se le quita el encabezado, no hay forma de saber de que sistema habla. Devuelvala pidiendo que cada celda nombre una capacidad de su propia ficha.
- Confundir el criterio de costo con una cotizacion. La pregunta pide costo **cualitativo**; el estudiante que se va a buscar precios pierde la hora del taller y llega con tres celdas.
- Invertir control y operacion: escribir que en IaaS el proveedor opera el sistema operativo. Es el mismo malentendido de la fila de operacion visto del otro lado, y arrastra la decision de la pregunta 6.
- Cambiar de dominio a mitad de matriz (control de BiblioLite, costo de un e-commerce). Suele pasar cuando se copia de dos fuentes distintas; verifique que las doce celdas hablen del mismo sistema.

---

## Pregunta 6 · ADR-001: modelo de servicio dominante de CloudLite · 12.5 pts

### Respuesta esperada

**1. Titulo** ADR-001 Modelo de servicio dominante de CloudLite App

**2. Estado** Aceptado — 31 de agosto de 2026

**3. Contexto** BiblioLite gestiona los prestamos de la biblioteca universitaria: unos 400 prestamos al mes, con un pico en la semana de matricula, y 38 devoluciones tardias el semestre pasado. El proyecto lo sostiene **una sola persona durante doce semanas**, **sin presupuesto de nube y sin tarjeta de credito**, y tiene que estar en linea el dia de la sustentacion de la Clase 15. La unica capacidad que pide algo del sistema operativo es la lectura del codigo de barras del lomo del libro, que necesitaria una libreria nativa.

**4. Decision** (una sola frase, un unico modelo dominante) La aplicacion de BiblioLite se desplegara sobre **PaaS**: se entrega el codigo de la API de prestamos y del front al proveedor, que opera el sistema operativo y el runtime, mientras el equipo conserva la responsabilidad del codigo, de los permisos y de los datos de prestamo.

**5. Alternativas descartadas** (exactamente 2, con el motivo en terminos del dominio)

- **IaaS.** Se descarta porque el proyecto lo sostiene una sola persona durante doce semanas, y en IaaS esa persona tendria que operar el sistema operativo: parchear la instancia, sostener la version de Node y levantar el servicio despues de cada reinicio. Cada hora gastada en eso es una hora que no se gasta en la regla de negocio que de verdad cuesta, que es la de renovaciones vencidas. La libreria nativa de codigo de barras, que es el unico argumento real a favor de IaaS en este dominio, se reemplaza por lectura manual del ISBN en el mostrador: es una perdida aceptable frente al costo de operar la maquina.

- **SaaS.** Se descarta porque un sistema de prestamos comprado ya resuelve el problema, y entonces no queda nada que arquitecturar ni nada que sustentar en la Clase 15: el entregable del semestre seria una configuracion. Ademas el modelo de licenciamiento por usuario no encaja con una biblioteca donde el auxiliar de mostrador rota cada semestre, y las 38 devoluciones tardias del semestre pasado se resolverian con la regla que traiga el producto, no con la que la biblioteca necesita.

**Nota de alcance** (no es una seccion aparte; se escribe dentro de las alternativas) Identidad y correo se siguen consumiendo como **SaaS satelite**, tal como quedaron en el C4 Context de la pregunta 3. Eso no rompe la decision: el modelo dominante se refiere a **la aplicacion propia**.

La **seccion 6, Consecuencias**, es la pregunta 7 y esta resuelta ahi mismo. El ADR completo del curso son esas seis secciones; ninguna otra.

### Como calificar

- 1.5 pts titulo y estado. El titulo tiene que traer el **numero** del ADR y el estado tiene que traer **fecha**; «Aceptado» solo, sin fecha, vale la mitad de este criterio.
- 2 pts el **contexto**: nombra el dominio, el plazo y al menos una restriccion real de quien sostiene el proyecto (una persona, sin presupuesto, sin tarjeta). **Cero en este criterio** si es teoria general o un resumen del tema de la clase. La prueba rapida: si el contexto no permite deducir por que se descarto IaaS, no es contexto.
- 3.5 pts la decision en **una frase** con **un** modelo dominante. **Cero en este criterio si nombra dos o mas modelos**: «un poco de PaaS y un poco de IaaS» no es una decision, es no haber decidido. Es el criterio que hay que revisar primero, antes de leer el resto.
- 5.5 pts las dos alternativas descartadas con el motivo atado al dominio: **2.75 pts cada una**. Se pierde **la mitad de cada una** si el motivo es generico («es mas caro», «es mas complejo») sin decir mas caro o mas complejo **para que** de su sistema.
- **Exactamente dos** alternativas. Con una sola, el ADR no documenta una decision sino un hecho: se califica solo la que este. Con tres o mas, se califican las dos primeras y se descuenta 1 pt por no seguir el formato, que es parte de lo que se evalua.
- Mencionar SaaS satelite para identidad y correo **no** penaliza y no cuenta como segundo modelo dominante. Si penaliza que la seccion 3 diga «PaaS para la app y SaaS para identidad» como si fueran dos decisiones dominantes: ahi ya se nombraron dos modelos.
- Elegir IaaS o SaaS como dominante **no se penaliza en absoluto**. Lo que se califica es que el motivo del descarte de los otros dos este atado al dominio. Un ADR que elige IaaS porque necesita la libreria nativa de codigo de barras y lo sustenta esta perfecto.

### Errores frecuentes y que hacer

- Decision con dos modelos. Es el error mas frecuente y el mas caro: cuesta 3.5 de los 12.5 puntos. Suele venir de querer no equivocarse. Devuelvala con una sola instruccion: «tache uno».
- Contexto escrito como resumen del tema: «los modelos de servicio son IaaS, PaaS y SaaS y hay que elegir uno». Eso no es contexto, es apunte de clase, y vale 0 de los 2 pts. La instruccion que lo corrige es una pregunta: «¿que tienes tu que no tiene otro equipo, y cuanto tiempo tienes?». Lo que responda es el contexto.
- Alternativas descartadas con motivo de folleto: «IaaS es mas complejo». Pregunte «mas complejo para hacer que, en BiblioLite» y la respuesta que dé el estudiante es exactamente lo que debia haber escrito.
- Una sola alternativa descartada, casi siempre SaaS, porque es la facil. La que enseña algo es IaaS, que es la que obliga a mirar el costo de operacion propio.
- Estado «Propuesto» o «En estudio». El enunciado pide `Aceptado` con fecha porque el ADR tiene que quedar cerrado hoy: las Clases 3, 7 y 15 construyen sobre esta decision y no puede seguir abierta.
- Agregar secciones que no se pidieron (participantes, diagramas, riesgos, opciones consideradas). No es un error conceptual, pero el enunciado dice cinco secciones y sin agregar otras: se descuenta del formato. Ojo con «Opciones consideradas»: en este curso las opciones son la matriz de la pregunta 5, y lo que va en el ADR son las dos **descartadas**.
- ADR que contradice la matriz de la pregunta 5. Si la matriz dijo que PaaS no sirve porque hace falta la libreria nativa, y el ADR elige PaaS sin resolver eso, hay una incoherencia que la sustentacion de la Clase 15 va a encontrar. Marquela hoy.

---

## Pregunta 7 · Consecuencias del ADR-001 · 6.25 pts

### Respuesta esperada

**Operacion**
- `+` Dejo de administrar el sistema operativo y el runtime: no vuelvo a parchear la instancia ni a levantar el servicio a mano despues de un reinicio. En terminos concretos, las tres o cuatro horas al mes que eso costaba se van a la regla de renovaciones.
- `-` Pierdo el acceso a la maquina: cuando la consulta de disponibilidad se ponga lenta no podre entrar por SSH a mirar procesos, solo tendre los registros y las metricas que el proveedor exponga. Depurar pasa a depender de lo que el panel me deje ver.

**Costo**
- `+` Se abarata el arranque: el nivel gratuito cubre la demo y el semestre, asi que el proyecto no necesita presupuesto para existir.
- `-` Se encarece el pico: la semana de matricula, que es cuando todos consultan los libros de reserva a la vez, es justo cuando el plan gratuito se queda corto y hay que escalar. El costo llega concentrado en la peor semana, no repartido.

**Aprendizaje**
- `+` Tengo que aprender a desplegar con un push y a leer los registros del proveedor, que es la forma en que se trabaja en la mayoria de los equipos que voy a encontrar.
- `-` **Amarre al proveedor**: cada archivo de configuracion, cada variable de entorno y cada nombre de servicio que escriba es especifico de esta plataforma. Si el ano entrante hay que mover BiblioLite a otra parte, la aplicacion se mueve pero la configuracion se reescribe completa, y no tengo forma de saber cuanto cuesta eso hasta que toque hacerlo. Ademas no voy a poder instalar la libreria nativa de codigo de barras: tendre que buscar una alternativa que el proveedor soporte o dejar la lectura manual del ISBN.

### Como calificar

- 3 pts los **tres ejes** presentes y rotulados: operacion, costo y aprendizaje. 1 pt cada uno.
- 2 pts que **cada eje** traiga al menos una consecuencia positiva y una negativa, **marcadas con `+` y `-`**. Un eje con solo positivas vale la mitad: la mitad que falta es justo la que la Clase 15 va a preguntar.
- 1.25 pts que **al menos una negativa** hable de **amarre al proveedor o de perdida de control**. Es la contrapartida que casi nunca se escribe y por eso se califica aparte.
- Se descuenta por cada consecuencia escrita como ventaja de folleto («es mas facil», «es mas moderno», «es mas escalable») en vez de como algo que cambia en el trabajo del estudiante. La prueba: si la frase no dice que hace o deja de hacer el estudiante, no es una consecuencia.
- Las consecuencias tienen que corresponder a **la decision de la pregunta 6**, no al modelo que le hubiera gustado. Si eligio IaaS y escribe «dejo de operar el sistema operativo», el criterio de operacion vale cero: esta describiendo otra decision.

### Errores frecuentes y que hacer

- Los tres ejes con solo consecuencias positivas. Es el error dominante. La instruccion que lo corrige: «por cada `+` escriba el `-` que vendria en el mismo paquete».
- Confundir consecuencia con ventaja: «es mas facil de usar». Pida que reescriba la frase empezando por «a partir de ahora tengo que...» o «dejo de...»; lo que salga ya es una consecuencia.
- No hablar nunca de amarre al proveedor. Se pierde 1.25 pts de 6.25, que es un quinto de la pregunta. Vale la pena anunciarlo en voz alta al abrir el taller.
- Consecuencias del eje aprendizaje escritas como lista de tecnologias («aprender Docker, Kubernetes, Terraform»). El eje pregunta que hay que aprender **para sostener esta decision durante el semestre**, que en PaaS es bastante menos que eso.
- Repetir en las consecuencias lo que ya dijo la matriz de la pregunta 5. La matriz compara; las consecuencias comprometen. Si el texto es identico, todavia no hay consecuencias.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿La actividad se entrega hoy?**

No. Sigue siendo la misma actividad de 15 preguntas de las Clases 1 a 4, y cierra al final del Corte 1. Hoy se resuelven la 5, la 6 y la 7. Conviene repetirlo aunque se haya dicho en la Clase 1: siempre hay alguien que llego hoy por primera vez.

**¿Puede cambiar el dominio ahora que entendio mejor el tema?**

No. El ADR-001 decide sobre las capacidades de la ficha de la pregunta 2, y las preguntas 8 a 15 siguen construyendo sobre lo mismo. Si el dominio le quedo grande, se recorta el bloque «fuera de alcance».

**¿Puede elegir dos modelos si su sistema tiene dos partes?**

No en la seccion de decision, y esta es la duda que hay que atajar antes de que empiecen a escribir. El modelo dominante es el de **su aplicacion**. Que identidad y correo sean SaaS ya estaba decidido desde la Clase 1 y se menciona en las alternativas, no en la decision.

**¿Elegir IaaS baja la nota?**

No. Se califica el sustento, no la eleccion. Un ADR que elige IaaS porque necesita una libreria nativa concreta y asume el costo de operarla esta mejor que uno que elige PaaS «porque es lo moderno».

**¿Hay que poner precios en la matriz?**

No, y buscarlos es la forma mas rapida de perder la hora del taller. El criterio dice **costo cualitativo**: bajo, medio o alto, con el por que de este dominio.

**¿Que fecha se le pone al estado del ADR?**

La de hoy, la de la sesion en que se decide. El ADR es un documento fechado: sirve precisamente para que en seis meses se sepa cuando se decidio y con que informacion.

**¿Cuantas secciones tiene el ADR y donde va cada una?**

**Seis**, y son las mismas en todo el curso: Titulo, Estado, Contexto, Decision, Alternativas descartadas y Consecuencias. Las cinco primeras se entregan en la pregunta 6 y la sexta en la pregunta 7, pero es **un solo documento**: el que se cita en la sustentacion de la Clase 15 y el que sirve de molde para el ADR-002 en adelante. No hay seccion de «Opciones consideradas»: ese analisis es la matriz de la pregunta 5.

**El contexto y la matriz de la pregunta 5, ¿no son lo mismo?**

No, y conviene decirlo antes de que empiecen a escribir. La matriz **compara** los tres modelos sobre las capacidades del dominio; el contexto son las **restricciones** bajo las que se decide: quien sostiene el proyecto, cuanto tiempo hay y con que presupuesto. La matriz es el analisis, el contexto es el terreno. Si el contexto repite la matriz, no cumple.

**¿Las consecuencias pueden ser las mismas para los tres ejes?**

No. Si la misma frase sirve para operacion, costo y aprendizaje, es una frase generica. Cada eje pregunta algo distinto: que hago, que pago y que tengo que aprender.

**¿Hay que abrir cuenta en algun proveedor cloud para responder esto?**

No. Toda la actividad es de decision y documentacion; no se despliega nada y no se pide tarjeta de credito en ningun momento del semestre.

---

## Cierre de la clase

El ADR-001 no es un ejercicio suelto: es el documento que la Clase 3 usa para saber si el contenedor que se va a construir corre en una instancia propia o sobre un runtime del proveedor, el que la Clase 7 usa para decidir que dibuja en el diagrama de despliegue, y el que la Clase 15 le va a pedir en voz alta cuando pregunte «¿por que asi y no de otra forma?». Cierre la clase diciendo exactamente eso: quien salga hoy sin decision cerrada llega a la Clase 3 sin saber que esta contenedorizando.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. Gratis + navegador; sin cuentas cloud de pago ni tarjeta.
