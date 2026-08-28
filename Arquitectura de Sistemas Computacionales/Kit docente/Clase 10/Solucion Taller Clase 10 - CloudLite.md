# Solucion — Actividad del Corte 2, preguntas 11 y 12 (tabla de costos cualitativa y sostenibilidad verificable)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las dos ultimas preguntas del Corte 2 sobre **BiblioLite**, y las dos con la misma trampa: se pueden responder con palabras que suenan bien y no dicen nada. La pregunta 11 la corta con dos reglas mecanicas —**driver contable** y **al menos un Alto y un Bajo**— y la 12 con una sola: **si no se puede comprobar mirando un artefacto, vale cero**. Con esas tres reglas, las dos preguntas se califican en diez minutos.

> Estas 2 preguntas cierran los **100 puntos** de la actividad del Corte 2 (Clases 6, 7, 8 y 10). La 11 vale 16.25 puntos, mas que cualquier otra pregunta del corte: es la que hay que atender primero en el taller. La tabla se construye **sobre el diagrama de despliegue de la Clase 7**, componente por componente, y quien no lo tenga a la vista va a dejar filas fuera.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 10 - Costos y sostenibilidad cloud/`
- Configuracion en la plataforma: `Kit docente/Clase 10/Taller en ExamLab - Clase 10 (configuracion).md`
- Hito del PI: Estimación cualitativa de costos + notas de sostenibilidad
- Entregable: Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)
- **Estas preguntas: 25.0 puntos** en 2 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 11 | Tabla de costos de BiblioLite | `abierta` | 16.25 |
| 12 | Tres acciones de sostenibilidad tecnica verificables | `abierta` | 8.75 |

---

## Pregunta 11 · Tabla de costos de BiblioLite · 16.25 pts

### Respuesta esperada

| Componente | Driver de costo | Nivel B/M/A | Apalancamiento |
|---|---|---|---|
| `API de prestamos` | **Horas de instancia encendida**: 24 x 30 = **720 h/mes** aunque la biblioteca este cerrada de noche. El costo no depende de las reservas, depende del reloj. | **A** | Escalar a cero fuera del horario de biblioteca (6:00 a 22:00): de 720 h a **480 h/mes**, un 33% menos. **Comprobable** en la politica de escalado y en el conteo de horas facturables. |
| `Base de datos de prestamos` | **Horas encendida** (no se puede apagar sin perder el servicio) **mas GB almacenados**, que solo crecen: un prestamo cerrado nunca se borra. | **A** | Politica de retencion: los prestamos cerrados con mas de 2 anos se mueven a un archivo en almacenamiento de objetos y se borran de la tabla caliente. Y resolver la lentitud con **indices** antes que con mas CPU. **Comprobable** en el tamano de la tabla mes a mes. |
| Almacenamiento de objetos (bundle de la `Aplicacion web` + respaldos) | **GB almacenados**: el bundle pesa unos 2 MB y cada `dump` diario unos 40 MB comprimidos. Mas **GB de transferencia de salida** cada vez que alguien descarga el bundle. | **B** | Retencion de 30 respaldos diarios y 6 mensuales en vez de guardarlos todos, y comprimir el `dump`. **Comprobable** en la politica de retencion escrita y en el listado del bucket. |
| Integracion continua (GitHub Actions) | **Minutos de CI por mes**: cada corrida del `ci.yml` de la Clase 8 consume entre 3 y 5 minutos, y se dispara en cada `push` a `main` y en cada solicitud de cambios. | **M** | Cache de `npm` y de capas de Docker (el `cache: 'npm'` ya esta en el YAML), y disparar el pipeline solo en `main` y en solicitudes de cambios, no en cada rama. **Comprobable** en el bloque `on:` del `ci.yml` y en la duracion de dos corridas consecutivas. |
| `Edge / balanceador` | **GB de transferencia de salida**: todo lo que sale hacia el navegador pasa por aqui, y la salida se paga; la entrada casi nunca. | **M** | Cachear el bundle con `Cache-Control` de un ano usando el hash en el nombre del archivo, y comprimir con gzip o brotli. **Comprobable** en los encabezados de respuesta: un `curl -I` los muestra. |

**Por que dos Altos y un Bajo, y no todo Medio.** La API y la base son Alto por el mismo motivo y vale decirlo en voz alta: **su costo no depende del uso, depende del tiempo**. Se pagan encendidas aunque nadie reserve un libro a las tres de la manana. El almacenamiento de objetos es Bajo porque BiblioLite no digitaliza contenidos —lo dice el «fuera de alcance» de la ficha de la Clase 1— y por eso guarda megabytes, no terabytes. CI y edge quedan en Medio porque crecen con la actividad, no con el reloj, y la actividad de un proyecto de curso es pequena.

La escala es **ordinal**: afirma que la API cuesta mas que el edge, **no cuantas veces mas**. Ese matiz es la razon de que la pregunta prohiba precios: con B/M/A se puede ordenar honestamente sin inventar una factura, y ordenar es lo que permite decidir donde apalancar primero.

**Sin precios en dolares, a proposito.** No hay una sola cifra de moneda en la tabla. Cualquier precio que pusiera seria inventado: no tengo cuenta de nube de pago —eso es la politica del curso desde el ADR-001— y los precios cambian por region y por nivel. Lo que si es verificable es la aritmetica de las **720 horas**, que sale del calendario y no de una lista de precios.

**El componente que mas ensena.** La fila de la base de datos es la unica cuyo driver crece solo, sin que nadie haga nada: cada prestamo cerrado que se acumula suma GB para siempre. Es la fila donde el apalancamiento tiene que ser una politica escrita (retencion) y no una accion puntual, y es la que conecta con la Clase 13, donde se vera que esa tabla es tambien la que no escala.

### Como calificar

- 4 pts **una fila por cada componente del despliegue, sin dejar ninguno fuera**. Se compara con el diagrama de la Clase 7 y se prorratea. Los sistemas externos (identidad, correo) pueden omitirse porque no los factura el estudiante, pero si los incluye con su driver, mejor.
- 5 pts los **drivers**: cada uno tiene que ser una **variable contable** —horas encendidas, GB de salida, GB almacenados, minutos de CI— y **no «el uso»** ni «la cantidad de usuarios». La prueba: ¿se puede poner un numero al final del mes? Si no, no es un driver.
- 3.25 pts los niveles, **con al menos un Alto y un Bajo justificados**. **Si todo es Medio, este criterio vale cero**, sin prorrateo: es la respuesta que la pregunta busca descartar.
- 4 pts los **apalancamientos, uno por fila, concretos y comprobables**. «Optimizar», «reducir costos» o «usar mejor los recursos» no suman. La forma que vale: una accion y donde se ve que se aplico.
- **Se descuenta fuerte por inventar precios en dolares** o por presentar una factura de un proveedor. La escala es cualitativa y el motivo es honestidad: el estudiante no tiene cuenta de pago, asi que cualquier cifra seria adivinada.
- Que el nivel Alto se justifique con «el costo depende del tiempo, no del uso» es la mejor version de esta respuesta. Si aparece, comentelo: es la idea central del tema y la que hace util toda la tabla.
- Un driver aritmeticamente verificable (las 720 horas del mes, los 5 minutos por corrida) vale mas que uno correcto pero abstracto. No es un criterio aparte: es lo que distingue el 5 de 5 del 3 de 5 en los drivers.

### Errores frecuentes y que hacer

- Todo en Medio. Es la respuesta que evita pensar y el criterio de niveles queda en cero, 3.25 puntos. Anunciarlo antes del taller: «necesito al menos un Alto y un Bajo, y necesito el motivo».
- Inventar precios: «la base cuesta 25 dolares al mes». Se descuenta fuerte y ademas es falso, porque nadie en el curso tiene esa factura. La escala cualitativa existe justamente para poder responder con honestidad.
- «El uso» como driver. No es contable. La pregunta de correccion es directa: «¿el uso de que, medido en que unidad, al final del mes?».
- Dejar fuera la integracion continua o el edge porque «no cuestan». Los minutos de CI y los GB de salida son los dos costos que mas sorprenden a un equipo real. El enunciado los nombra explicitamente como componentes de la tabla.
- Incluir una fila de almacenamiento de objetos del dominio cuando el dominio no maneja archivos. Es el mismo error de la pregunta 5 de la Clase 7: agregar la pieza porque suena a cloud.
- Apalancamientos que son deseos: «reducir el consumo», «ser mas eficientes». Sin una accion y sin donde se comprueba, la fila no suma. Anticipa que la pregunta 12 tambien va a fallar.
- Confundir el driver con el apalancamiento: poner «cachear» en la columna del driver. El driver es lo que **hace crecer** la factura; el apalancamiento es lo que la **baja**.

---

## Pregunta 12 · Tres acciones de sostenibilidad tecnica verificables · 8.75 pts

### Respuesta esperada

| Accion | En que artefacto se comprueba | Como se comprueba |
|---|---|---|
| **1.** Imagen base ligera y sin dependencias de desarrollo: `node:20-alpine` con etiqueta fija y `npm ci --omit=dev`. | El `Dockerfile` de la Clase 3: su **primera linea** y su instruccion `RUN`. | `docker images` muestra **142 MB** en vez de los ~1.1 GB de `node:20` completo. Cualquiera lo reproduce construyendo las dos imagenes y comparando. Menos bytes = menos descarga en cada corrida de CI y menos almacenamiento en el registro. |
| **2.** Apagar la `API de prestamos` fuera del horario de la biblioteca: escalar a cero de 22:00 a 6:00. | La **politica de escalado** (la que la Clase 13 formaliza) y el registro de horas encendidas. | La politica dice el rango horario y el conteo de horas facturables del mes baja de **720 a 480**. Se comprueba con el registro de arranques y paradas: si sigue en 720, no se aplico. |
| **3.** No ejecutar el pipeline en cada `push` de cada rama, y reutilizar cache de `npm` y de capas de Docker. | El `ci.yml` de la Clase 8: el bloque `on:` y la clave `cache: 'npm'`. | Se lee el YAML —los disparadores son `main` y solicitudes de cambios, no `push` a cualquier rama— y se comparan las duraciones de dos corridas seguidas: la segunda debe ser mas corta porque reutilizo el cache. Si las dos duran lo mismo, el cache no esta funcionando. |

**El vinculo con los drivers de costo de la pregunta 11**

Las tres se apalancan sobre un driver de la tabla anterior, y la segunda es la mas directa:

- **Accion 2 -> driver «horas de instancia encendida» de la fila `API de prestamos` (nivel A).** Es literalmente el mismo apalancamiento escrito en esa fila: pasar de 720 a 480 horas al mes. Un tercio menos de horas es un tercio menos de energia consumida y un tercio menos de factura; la misma decision baja las dos cosas.
- **Accion 3 -> driver «minutos de CI».** Menos corridas y corridas mas cortas.
- **Accion 1 -> driver «GB almacenados» del registro y, de rebote, «minutos de CI»**, porque una imagen ocho veces mas pequena se descarga y arranca mas rapido en cada corrida.

Que costo y sostenibilidad se apalanquen con la misma decision no es una coincidencia retorica: el recurso que no se consume no se paga y no se genera. Por eso la pregunta pide atar al menos una.

**Por que estas tres pasan la prueba de los seis meses.** El enunciado da el criterio: si otra persona abre el repositorio dentro de seis meses, ¿puede decir si la accion se aplico? Con las tres, si: la primera linea del `Dockerfile` esta ahi, el bloque `on:` del `ci.yml` esta ahi, y la politica de escalado esta escrita con su rango horario. Ninguna depende de que alguien recuerde haber tenido buenas intenciones.

**Una cuarta que quedo fuera, por si el grupo la propone:** apagar el escenario de Killercoda al terminar la sesion, comprobable en la bitacora del laboratorio de la Clase 3. Es valida y esta bien formada —artefacto y comprobacion—, pero es la que viene como ejemplo en el enunciado, asi que la use como referencia y no como respuesta.

### Como calificar

- 2.5 pts por accion verificable, hasta 3 acciones: **suma completo solo si nombra el artefacto Y como se comprueba**. Las dos columnas pesan igual, asi que una accion con artefacto pero sin metodo de comprobacion vale 1.25.
- 1.25 pts por **atar al menos una accion a un driver de costo de la pregunta 11**. Se exige que el driver exista en su propia tabla: atarla a un driver que no listo no cuenta.
- **Una accion que no se pueda comprobar mirando un artefacto vale cero, aunque sea razonable.** «Concientizar al equipo», «ser mas eficientes», «usar la nube de forma responsable»: cero, sin discusion. La regla es mecanica a proposito.
- El artefacto tiene que ser **del proyecto**: el `Dockerfile`, el `ci.yml`, la politica de escalado, la bitacora del laboratorio, el diagrama. Un «documento de buenas practicas» escrito para la ocasion no es un artefacto del sistema.
- Se aceptan las tres acciones del ejemplo del enunciado **si el estudiante las aterriza a su proyecto** con su artefacto y su metodo. Copiar la frase sin aterrizarla vale la mitad; el enunciado dice que son ejemplos de forma.
- La prueba de los seis meses del enunciado es el mejor criterio de arbitraje cuando una accion queda en la frontera: «si otra persona abre el repositorio dentro de seis meses, ¿puede decir si se aplico?». Uselo tal cual en la retroalimentacion.

### Errores frecuentes y que hacer

- «Concientizar al equipo sobre el uso responsable de los recursos». Es la respuesta que la pregunta esta diseñada para descartar: no hay artefacto y no hay comprobacion. Cero, y conviene decirlo antes del taller para que nadie gaste tres lineas en ella.
- Acciones ambientales sin conexion con el diseno: reciclar, imprimir menos, apagar las luces del salon. La pregunta dice **sostenibilidad tecnica** y **verificable en el propio diseno**. No se descuenta la intencion, pero no suma.
- Nombrar el artefacto y dejar en blanco el como. Es la mitad de cada accion. La pregunta de correccion: «abro ese archivo, ¿que linea me dice que se aplico?».
- Atar la accion a un driver que no aparece en su tabla de la pregunta 11. Se ve poniendo las dos respuestas al lado y cuesta el 1.25. Suele pasar cuando la tabla se hizo de ultimo y sin revisar la 12.
- Tres acciones que son la misma: cache de npm, cache de Docker y cache del navegador. Son tres formas de una decision. Pida que toquen artefactos distintos.
- Proponer apagar la base de datos por la noche. No se puede sin perder el servicio y sin arriesgar el respaldo: es el ejemplo de una accion que suena sostenible y rompe el sistema. Corrijala mostrando que la fila de la base tiene otro apalancamiento (la retencion).

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Puedo poner precios reales si los busco en la calculadora del proveedor?**

No, y se descuenta fuerte. El curso no abre cuentas de pago y los precios cambian por region y por nivel: cualquier cifra seria una adivinanza con aspecto de dato. La escala es B/M/A y con eso alcanza para decidir donde apalancar.

**¿Que hago con un componente al que no le encuentro driver?**

Volver al diagrama de la Clase 7, que es lo que dice el enunciado. Si un componente no tiene una variable que haga crecer su factura, o esta mal entendido o no deberia estar en el diagrama. Las dos conclusiones son utiles.

**¿Por que no puede ser todo Medio?**

Porque entonces la tabla no ordena nada, y ordenar es lo unico que la escala ordinal permite hacer. Sin un Alto no se sabe donde apalancar primero, y ese es el proposito del ejercicio. El criterio de niveles queda en cero.

**¿La escala B/M/A dice cuantas veces mas cuesta un componente?**

No. Es ordinal: dice que uno cuesta mas que otro, no cuantas veces mas. Confundirlo es lo que lleva a inventar precios; el orden es suficiente para decidir.

**¿Los minutos de CI cuestan de verdad?**

En repositorios publicos son ilimitados y en privados hay 2000 al mes gratis, asi que en el curso no se paga nada. Aun asi es un driver real: en un equipo con repositorio privado y varias ramas, los 2000 minutos se agotan a mitad de mes.

**¿Sostenibilidad es lo ambiental?**

Aqui es sostenibilidad **tecnica**: decisiones de diseno que reducen el recurso consumido y se pueden comprobar en un artefacto. Casi siempre coinciden con lo ambiental —el recurso que no se consume no se genera— pero la que se califica es la verificable.

**¿Vale apagar el laboratorio de Killercoda como una de las tres?**

Es valida y esta bien formada, pero viene como ejemplo en el enunciado. Si la usa, aterricela a su bitacora concreta; y busque al menos dos que salgan de sus propios artefactos.

**¿Tengo que atar las tres acciones a un driver de costo?**

Solo una es obligatoria y vale 1.25 pts. Atar las tres no suma mas, pero suele ser lo que pasa naturalmente: la misma decision baja el costo y el consumo.

---

## Cierre de la clase

Lo que queda de hoy es que una decision de arquitectura se puede defender con una variable contable en la mano: no «la nube es cara», sino «esta pieza se paga por horas encendidas y la mia esta encendida 720 al mes». Deje anotadas las tres conexiones hacia adelante: el apalancamiento de escalar a cero es la politica que la Clase 13 va a escribir con su metrica y su ventana de enfriamiento, la fila de la base de datos es el componente que alli se vera que **no** escala, y la tabla completa es una de las piezas del paquete que el checkpoint de la Clase 11 revisa. Con esto cierra el Corte 2: el sistema ya tiene amenazas con controles, un lugar donde ejecutarse, un pipeline que lo verifica y un costo que se puede ordenar.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. Gratis + navegador; sin cuentas cloud de pago ni tarjeta.
