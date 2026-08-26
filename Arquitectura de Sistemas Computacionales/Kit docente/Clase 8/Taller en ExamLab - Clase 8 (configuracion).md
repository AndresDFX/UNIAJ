# Taller de la Clase 8 en ExamLab - configuracion

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Taller:** Actividad del Corte 2 (preguntas 7 a 10) - Integracion continua y monitoreo
- **Preguntas:** 4 · **Total:** 25 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Workflow Actions (build/test/simulate) + métricas de monitoreo del PI
- **Entregable de la clase:** .github/workflows/ci.yml + sección Monitoreo/CI del informe

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Las preguntas 7 a 10 de la actividad del Corte 2. El estudiante escribe el workflow de CI de su stub, explica que valida de verdad, ubica hasta donde llega su pipeline y define las senales con las que operaria CloudLite.

---

## Pregunta 7 - Respuesta escrita · 10.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## El workflow de integracion continua

Escriba el **contenido completo** del archivo `.github/workflows/ci.yml` para el stub de
CloudLite. Debe incluir:

1. **Disparadores** (`on`): cuando corre el pipeline.
2. **Entorno de ejecucion** (`runs-on`).
3. **Pasos** de **construccion**, **prueba** y **despliegue simulado**.

> **Los secretos se referencian desde la configuracion del repositorio**, con la sintaxis de
> *secrets* del proyecto, **nunca escritos en claro dentro del YAML**. Es la misma politica
> que definio en la pregunta 3.

El **despliegue simulado** es deliberado: en este curso el pipeline llega hasta «listo para
desplegar» y no despliega a ningun servidor real, porque no abrimos cuentas de nube de pago.
Dejelo explicito en el nombre del paso para no prometer lo que no hace.

Use la imagen y el puerto **del Dockerfile que escribio en el Corte 1**: es el mismo
servicio.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2 pts los disparadores declarados. 1.5 pts el entorno de ejecucion. 4 pts los tres pasos presentes y en orden (construccion, prueba, despliegue simulado). 1.5 pts que el despliegue este rotulado como simulado y no prometa un despliegue real. 1 pt coherencia con el Dockerfile del Corte 1 (misma imagen, mismo puerto). **Cero en toda la pregunta si aparece un secreto escrito en claro en el YAML.**

---

## Pregunta 8 - Respuesta escrita · 5.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Que hace realmente su paso de construccion y prueba

Explique, sobre **su propio** `ci.yml`:

1. **Que se compila o se instala** en el paso de construccion.
2. **Que se ejecuta** en el paso de prueba: que comprueba exactamente.
3. **Con que condicion el pipeline debe FALLAR**: que tiene que pasar para que el check
   salga rojo.

> **Un CI que solo imprime un mensaje de exito no es CI.** Si su pipeline no puede fallar
> nunca, no esta validando nada: es una decoracion verde. La pregunta que hay que poder
> responder es «que error tendria que introducir yo en el codigo para que este pipeline lo
> detecte», y su respuesta tiene que decirlo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1.5 pts que se compila o instala. 1.5 pts que se ejecuta en la prueba y que comprueba. 2 pts la condicion de fallo, expresada como algo que el pipeline detectaria. **Cero en la condicion de fallo si el pipeline no puede fallar nunca** (solo `echo`, o pruebas que siempre pasan): es el criterio central de la pregunta.

---

## Pregunta 9 - Respuesta escrita · 4.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Hasta donde llega su pipeline: CI, CD y lo que es realista aqui

Distinga los dos terminos y ubique su propio trabajo:

1. **Que valida la integracion continua (CI)** y en que momento del ciclo actua.
2. **Que hace la entrega o despliegue continuo (CD)**, y en que se diferencia de lo
   anterior.
3. **Cual de los dos construyo usted hoy**, y hasta que punto exacto llega su `ci.yml`.
4. **Que le faltaria** para tener CD de verdad, y **por que este curso no lo pide**.

> La frontera importa mas de lo que parece: decir «ya tenemos CD» porque el YAML tiene un
> paso llamado `deploy` es de las afirmaciones que un evaluador tumba en dos preguntas. En
> este curso el despliegue **se simula**, y decirlo asi no resta puntos: los suma, porque
> demuestra que sabe donde esta el limite de lo que construyo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1 pt la definicion de CI atada a cuando actua. 1 pt la de CD y su diferencia. 1 pt ubicar correctamente su propio trabajo, reconociendo que llega hasta «listo para desplegar». 1 pt lo que faltaria para CD real y por que el curso no lo exige. Se descuenta la mitad si afirma haber construido CD.

---

## Pregunta 10 - Respuesta escrita · 6.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Metricas y registros de CloudLite en produccion

Liste entre **4 y 6 metricas o registros** que observaria en la produccion hipotetica de su
CloudLite, **cada una con su umbral u objetivo**.

Orientacion: use las **senales doradas** en version reducida, aterrizadas a su dominio:

- **Latencia**: cuanto tarda la operacion que mas se usa.
- **Trafico**: cuantas peticiones u operaciones por unidad de tiempo.
- **Errores**: que proporcion falla, y cuales cuentan como fallo de negocio.
- **Saturacion**: que recurso se agota primero.

Formato: `Senal | Que se mide en MI dominio | Umbral u objetivo`.

> **Una metrica sin umbral no sirve para operar.** «Medimos la latencia» no permite decidir
> nada; «el listado de disponibilidad debe responder en menos de 400 ms y si pasa de 800 ms
> se revisa» si, porque define cuando hay que actuar. El umbral puede ser discutible; lo que
> no puede es faltar.

Al menos una de las senales debe ser un **registro** y no una metrica numerica: algo que se
escribe para poder reconstruir que paso despues.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1 pt por senal bien formada con su umbral, hasta 4 senales; las senales 5 y 6 suman hasta 1 pt adicional entre las dos. 1 pt que al menos una sea un registro y no una metrica numerica. **Una senal sin umbral no suma**, aunque este bien elegida. Se descuenta si las senales no se refieren a operaciones del dominio propio.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **25**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
