# Taller de la Clase 10 en ExamLab - configuracion

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Taller:** Actividad del Corte 2 (preguntas 11 y 12) - Costos y sostenibilidad
- **Preguntas:** 2 · **Total:** 25 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Estimación cualitativa de costos + notas de sostenibilidad
- **Entregable de la clase:** Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Las preguntas 11 y 12 de la actividad del Corte 2, que la cierran. Clase autonoma: el estudiante construye la tabla de costos cualitativa de CloudLite y propone tres acciones de sostenibilidad verificables en sus propios artefactos.

---

## Pregunta 11 - Respuesta escrita · 16.25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Tabla de costos de CloudLite

Construya la tabla de costos con **una fila por componente** —API, base de datos,
almacenamiento de objetos si lo tiene, integracion continua y edge— y **estas cuatro
columnas**:

`Componente | Driver de costo | Nivel B/M/A | Apalancamiento`

- **Driver de costo**: la variable concreta que, si crece, hace crecer la factura de ese
  componente. Drivers a considerar: **tiempo inactivo** (instancias encendidas sin trabajo),
  **transferencia de salida**, **almacenamiento** y **minutos de CI**.
- **Nivel**: **B**ajo, **M**edio o **A**lto. Es una escala **ordinal**: ordena, no mide
  distancias. Decir que la base de datos es Alto y el edge es Bajo afirma que una cuesta mas
  que la otra, no cuantas veces mas.
- **Apalancamiento**: **que palanca concreta baja ese costo**. No «optimizar»: algo que se
  pueda hacer y comprobar.

> **Prohibido inventar precios en dolares o facturas de un proveedor.** La estimacion es
> **cualitativa B/M/A**. Un componente al que no le sabe poner driver es un componente que
> todavia no entiende: vuelva al diagrama antes de escribir la fila.

**Fuerce al menos un Alto y un Bajo.** Marcar todo como «Medio» para no pensar es la
respuesta que esta pregunta busca descartar.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

4 pts una fila por cada componente del despliegue, sin dejar ninguno fuera. 5 pts los drivers: cada uno tiene que ser una variable contable (horas encendidas, GB de salida, GB almacenados, minutos de CI) y no «el uso». 3.25 pts los niveles, con al menos un Alto y un Bajo justificados; si todo es Medio, este criterio vale cero. 4 pts los apalancamientos, uno por fila, concretos y comprobables. **Se descuenta fuerte por inventar precios en dolares**: la escala es cualitativa.

---

## Pregunta 12 - Respuesta escrita · 8.75 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Tres acciones de sostenibilidad tecnica

Proponga **3 acciones de sostenibilidad tecnica** aplicables al diseno de CloudLite. La
condicion que las hace validas es que sean **verificables en el propio diseno**: debe poder
comprobarse **si se aplico o no** mirando los artefactos del sistema.

Para cada accion escriba: `Accion | En que artefacto se comprueba | Como se comprueba`.

Ejemplos de la **forma** esperada, no para copiarlos:

- apagar los laboratorios al terminar la sesion — se comprueba en la bitacora del lab;
- usar imagenes base ligeras — se comprueba en la primera linea del `Dockerfile`;
- no sobredimensionar instancias — se comprueba en la politica de escalado.

> Una accion como «ser mas eficientes» o «concientizar al equipo» no se puede comprobar
> mirando un artefacto, y por eso no cuenta. La prueba: si otra persona abre su repositorio
> dentro de seis meses, ¿puede decir si la accion se aplico? Si la respuesta es no, todavia
> es una intencion.

Ate al menos una de las tres a un **driver de costo** de la tabla anterior: sostenibilidad y
costo suelen apalancarse con la misma decision.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2.5 pts por accion verificable, hasta 3 acciones: suma completo solo si nombra el artefacto y como se comprueba. 1.25 pts por atar al menos una accion a un driver de costo de la pregunta 11. Una accion que no se pueda comprobar mirando un artefacto vale cero, aunque sea razonable.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **25**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
