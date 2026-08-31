# Solución del taller — Clase 2: Línea de tiempo del periodo

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni compartir pantalla con él antes de que los equipos trabajen: es la respuesta completa del entregable, y verla antes convierte el taller en copia.

## Para qué sirve este documento

Este documento resuelve el taller completo para **un** periodo, el de 1968–1975, que es el más difícil de los cinco porque sus hitos son ideas y no aparatos. Sirve para tres cosas: ver el nivel de detalle que se espera, tener respuesta lista si un equipo se atasca, y calificar con un referente en vez de con una impresión. Al final hay una nota por cada uno de los otros cuatro periodos con lo que no puede faltar.

## El caso que se resuelve aquí

**Periodo 1968–1975 · De la crisis del software al mes-hombre mítico**

Es el periodo del equipo 2. Se eligió para esta solución porque es donde los equipos fallan más: los hitos no son máquinas que se puedan describir, son **artículos y conferencias**, y el estudiante de primer semestre tiende a escribir «en 1968 hubo una conferencia» sin poder decir de qué se habló ni por qué importa.

> Si el docente solo alcanza a leer una parte de este documento antes de clase, que sea el bloque «QUÉ SIGUE VIVO HOY»: es el que decide el 30 % de la nota y el que casi ningún equipo hace bien sin ayuda.

## Consigna que se les dio

> A su equipo le corresponde un periodo de la historia de la Ingeniería de Sistemas. Armen la línea de tiempo de **ese periodo** con **cuatro hitos**, y para cada hito respondan las cuatro preguntas del método. No metan más de cuatro: una línea de tiempo con diez fechas no se puede exponer en 3 min y no se califica mejor.

**Entregable:** un diagrama de línea de tiempo con 4 hitos en diagrams.net (draw.io), guardado en la carpeta del equipo en Drive, más las cuatro respuestas escritas por hito en el documento del equipo · **17 min de trabajo · 3 min de exposición**

## Respuesta bloque por bloque

### 1. LOS CUATRO HITOS

**Se pedía:** Cuatro hechos de su periodo, con año, puestos en orden en la línea de tiempo.

**Respuesta modelo:**

**1968 · Conferencia de la OTAN en Garmisch, Alemania.** Se reúne un grupo de académicos e ingenieros de la industria a discutir por qué los grandes proyectos de software fracasan, y se populariza el término «ingeniería de software».

**1968 · «Go To Statement Considered Harmful», de Edsger Dijkstra.** Un artículo de dos páginas que sostiene que cierta forma de escribir programas los vuelve imposibles de entender, y propone la programación estructurada.

**1970 · «Managing the Development of Large Software Systems», de Winston Royce.** El artículo que contiene el esquema que después se llamó «cascada», presentado con la advertencia de que en forma puramente lineal es riesgoso.

**1975 · «The Mythical Man-Month», de Fred Brooks.** El libro donde el director del OS/360 de IBM explica por qué su propio proyecto se atrasó, y formula que agregar gente a un proyecto atrasado lo atrasa más.

**Cómo calificar:** 20 pts si están los cuatro con año y en orden. Se acepta cambiar Dijkstra por «1969 · primer nodo de ARPANET» o por «1972 · C y Unix», que también caen en el periodo. **No** se acepta meter 1991 (Linux) ni 2001 (ágil): están fuera del periodo y es la señal de que el equipo no leyó su asignación. Reste 5 pts por hito sin año.

### 2. QUÉ DOLÍA ANTES

**Se pedía:** Para cada hito: el problema concreto que existía antes y a quién le pasaba.

**Respuesta modelo:**

**Garmisch 1968:** proyectos como el sistema operativo OS/360 de IBM y el software del programa Apollo movían cientos o miles de personas y varios años, y se pasaban de plazo y de presupuesto de forma escandalosa. Le dolía a quien pagaba —empresas y gobiernos— y a los propios equipos, que trabajaban sin saber si iban bien. No existía manera de estimar, medir el avance ni repartir el trabajo.

**Dijkstra 1968:** los programas se escribían con saltos libres de un punto a otro del código. Le dolía a quien tenía que corregir un programa que no había escrito: seguir el flujo era casi imposible, así que un error pequeño costaba días.

**Royce 1970:** no había una respuesta compartida a «¿en qué orden se hace el trabajo?». Cada proyecto grande improvisaba su propio orden, y le dolía al cliente, que no tenía en qué momento revisar nada ni con qué comparar lo prometido.

**Brooks 1975:** cuando un proyecto se atrasaba, la reacción administrativa era contratar más programadores. Le dolía a todos, porque el atraso empeoraba y nadie entendía por qué.

**Cómo calificar:** 25 pts. Lo que se califica es que esté escrito como **problema que le pasa a alguien**, no como carencia. «No había métodos» es una carencia y vale la mitad; «el cliente no tenía en qué momento revisar nada» es un problema y vale completo. Exija el «a quién le pasaba» en los cuatro hitos: es el hábito que se evalúa en la sesión 6.

### 3. QUÉ PROPUSO

**Se pedía:** Para cada hito: la idea, el método o la herramienta, en una frase que ustedes puedan explicar.

**Respuesta modelo:**

**Garmisch:** tratar la construcción de software como una ingeniería —con método, medición, estándares y responsabilidad profesional— en vez de depender del talento de individuos.

**Dijkstra:** escribir programas con tres estructuras claras (secuencia, decisión y repetición) en vez de saltos libres, para que el programa se pueda leer de arriba abajo y razonar sobre él.

**Royce:** hacer el trabajo en fases identificables, cada una con un producto que se pueda revisar, y —esta es la parte que la industria olvidó— **recorrerlas dos veces**, usando la primera pasada como prototipo para aprender.

**Brooks:** la comunicación crece mucho más rápido que el equipo, así que agregar gente a un proyecto atrasado le agrega coordinación y lo atrasa más. Corolario: hay trabajo que no se puede paralelizar.

**Cómo calificar:** 20 pts. El criterio es **que el equipo pueda explicar la frase sin leerla**. Pregúntele al vocero qué significa «programación estructurada» o «no se puede paralelizar»: si no lo sabe, es una frase copiada y vale la mitad. Se acepta lenguaje coloquial correcto; no se acepta jerga sin comprensión.

### 4. QUÉ SIGUE VIVO HOY

**Se pedía:** Para **al menos dos** de los cuatro hitos: qué parte de ese problema todavía no está resuelta, con un ejemplo de algo que ustedes hayan visto.

**Respuesta modelo:**

**De Brooks (el más fácil de aterrizar):** sigue vivo entero. Cinco personas son diez parejas que se tienen que entender; diez personas son cuarenta y cinco. Un ejemplo propio y verificable: en el taller de la sesión 1 el equipo tuvo 14 minutos; si en el minuto 10 hubiera entrado un integrante nuevo, habría habido que contarle todo el contexto y el equipo habría terminado con menos, no con más. Es la razón declarada por la que los equipos de este curso son de cinco.

**De Garmisch:** sigue vivo el problema de fondo, que es estimar y medir avance en algo que no se ve. Ejemplo propio: cuando un equipo dice «ya casi terminamos el documento», nadie puede verificar ese «casi». Es exactamente el problema de 1968 en escala de 17 minutos, y es el que se ataca en la sesión 7 con hitos y entregables.

**De Royce:** sigue vivo el malentendido. Cualquier búsqueda rápida presenta la cascada como un método malo que Royce propuso, cuando el artículo dice lo contrario. Ejemplo propio: comparen dos resúmenes de internet sobre la cascada y verán que ninguno cita la advertencia.

**De Dijkstra:** está en buena parte resuelto, y decirlo es correcto. Los lenguajes actuales ya no ofrecen saltos libres; lo que sobrevive es la idea general de que **el código se escribe para que otro humano lo lea**.

**Cómo calificar:** 30 pts, el bloque que decide la nota. Exija **dos hitos como mínimo y un ejemplo propio en cada uno**. «Sigue vigente porque los proyectos todavía se atrasan» es una afirmación sin ejemplo y vale 10 de 30. Un ejemplo tomado de la experiencia del propio equipo en este curso vale completo: es la señal de que entendieron. Vale también reconocer que Dijkstra está resuelto: distinguir lo cerrado de lo abierto es parte de la habilidad.

### 5. LA FUENTE

**Se pedía:** De dónde sacaron cada dato: autor o institución, y año. Si usaron una cifra («el 70 % de los proyectos…»), la fuente es obligatoria.

**Respuesta modelo:**

Para este periodo las fuentes primarias existen y son cortas: las actas de la conferencia de Garmisch de 1968 (Naur y Randell, editores), el artículo de Dijkstra en Communications of the ACM (1968), el de Royce en las actas de la IEEE WESCON (1970) y el libro de Brooks (Addison-Wesley, 1975). Lo aceptable en primer semestre es **autor o institución + año**, no una cita en formato APA completo.

**Cómo calificar:** 15 pts. Un enlace pegado sin autor ni año vale 0 en ese hito. Si el equipo usó una cifra de fracaso de proyectos y no trae fuente, reste todo el bloque y dígalo en voz alta: es el punto donde el curso empieza a exigir rigor, y es más útil que se note hoy que en la sesión 9.

## Rúbrica del taller

| Criterio | Peso | Por qué pesa eso |
|---|---|---|
| Los cuatro hitos están, con año y en orden | **20 %** | Es el mínimo verificable del entregable: sin esto no hay línea de tiempo. |
| «Qué dolía antes» está escrito como problema, no como falta de tecnología | **25 %** | Es la habilidad que el curso entero entrena y la que se evalúa en la sesión 6. |
| «Qué sigue vivo hoy» en al menos dos hitos, con ejemplo propio | **30 %** | Es lo único que no se puede copiar de internet, y por eso es lo que más pesa. |
| Fuentes con autor o institución y año | **15 %** | Primer ejercicio de rigor bibliográfico del curso. Se vuelve a exigir en la sesión 9. |
| La exposición cupo en 3 min y habló el vocero | **10 %** | El presupuesto de 15 min de exposiciones no se puede estirar. |

> Suma **100 %**. La nota es del equipo, no del vocero.

## Si el equipo trabajó otro caso

**Periodo 1945–1957 · Equipo 1.** Hitos esperables: ENIAC (1945), arquitectura de von Neumann (1945), el primer «bug» documentado de Grace Hopper y su trabajo en compiladores, Fortran (1957). Lo que **no** puede faltar: que el problema de la época era **traducir** —hablarle a la máquina sin usar su idioma— y que el trabajo cabía en pocas personas. Error típico: contar la historia del hardware sin decir qué problema humano resolvía.

**Periodo 1976–1990 · Equipo 3.** Hitos esperables: el computador personal (Apple II 1977, IBM PC 1981), las primeras bases de datos relacionales comerciales sobre el modelo de Codd, el modelo en espiral de Boehm (1988), la aparición de los estándares IEEE de software. Lo que **no** puede faltar: el problema muda a **muchos usuarios que no son técnicos**, y con eso nace el requisito de usabilidad. Error típico: quedarse en las marcas de computadores.

**Periodo 1991–2005 · Equipo 4.** Hitos esperables: la web (1991), Linux (1991), los patrones de diseño (1994), el Manifiesto Ágil (2001). Lo que **no** puede faltar: el problema es que **los requisitos cambian mientras se construye**, y que ágil no elimina las fases sino que las hace pequeñas y repetidas. Error típico: presentar ágil como «trabajar sin plan».

**Periodo 2006–hoy · Equipo 5.** Hitos esperables: la nube como servicio por horas (AWS, 2006), el teléfono inteligente como plataforma (2007–2008), DevOps y la entrega continua, la IA generativa en producción (2022 en adelante). Lo que **no** puede faltar: cuando construir se vuelve barato, la pregunta difícil deja de ser «¿se puede?» y pasa a ser **«¿se debe, a quién afecta y quién responde?»**. Error típico: convertirlo en una lista de productos.

## Errores que hay que ver y no dejar pasar

- **«Antes no había internet / no había computadores»** → Es una carencia de tecnología, no un problema. Qué no podía hacer una persona concreta por eso. «Un banco no podía consultar un saldo desde otra ciudad».
- **«En 1968 hubo una conferencia importante»** → No dice de qué se habló ni por qué importó. El problema que llevó a convocarla y la palabra que salió de ahí.
- **«Royce inventó la cascada y estaba equivocado»** → Royce propuso ese esquema advirtiendo que lineal es riesgoso. Que lo cuenten con la advertencia incluida, y que digan de dónde sacaron la versión sin ella.
- **«El 70 % de los proyectos fracasa»** → Es una cifra que circula sin fuente y con definiciones distintas de «fracaso». Autor o institución y año. Si no lo tienen, que lo digan como afirmación general sin número.
- **«Sigue vigente hoy» (sin más)** → Es la parte que más pesa y así escrita no dice nada. Un ejemplo concreto que ellos hayan visto, aunque sea de este mismo curso.

## Cierre: qué decir en los 3 minutos finales

Tres minutos, una sola idea: **la ingeniería de sistemas nació de un fracaso de organización, no de un invento técnico.** En 1968 se reconoció en público que no se sabía coordinar el trabajo de mil personas construyendo algo invisible, y de ahí salieron el método, las fases y los estándares. Cierre con la aritmética de Brooks porque los toca directamente: cinco personas son diez parejas que se tienen que entender, diez personas son cuarenta y cinco, y por eso los equipos de este curso son de cinco y no de diez. Y anuncie la sesión 3 con una pregunta abierta: si el problema de fondo es coordinar y entender, entonces hay que aprender a mirar un sistema completo y no solo su software.

## Con qué se conecta

Hacia atrás: la sesión 1 dejó cinco problemas del entorno escritos, y hoy se vio que los proyectos que fracasan en la historia fracasan por no tener el problema bien planteado. Hacia adelante: la sesión 7 retoma a Royce para el ciclo de vida, la sesión 9 vuelve sobre las fuentes y el rigor bibliográfico, y la sesión 6 —cierre del corte— exige el problema del proyecto escrito con el mismo criterio que hoy se le exigió a «qué dolía antes».
