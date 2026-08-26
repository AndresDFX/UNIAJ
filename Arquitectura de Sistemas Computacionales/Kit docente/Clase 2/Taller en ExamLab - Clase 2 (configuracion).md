# Taller de la Clase 2 en ExamLab - configuracion

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Taller:** Actividad del Corte 1 (preguntas 5 a 7) - Modelos de servicio y ADR-001
- **Preguntas:** 3 · **Total:** 24 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve
- **Entregable de la clase:** ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Las preguntas 5 a 7 de la actividad del Corte 1. El estudiante compara IaaS, PaaS y SaaS sobre las capacidades de su propio dominio, decide un modelo dominante y lo documenta como ADR-001 con sus alternativas descartadas y sus consecuencias.

---

## Pregunta 5 - Respuesta escrita · 6.25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Matriz IaaS / PaaS / SaaS para su dominio

Partiendo de la **ficha** y del **C4 Context** del mismo dominio que cerro en la Clase 1,
construya una matriz que compare los tres modelos de servicio **aplicados a las
capacidades de SU dominio**.

Encabezados exactos: `Criterio | IaaS | PaaS | SaaS`, con **estas cuatro filas** y en este
orden:

1. **Control**: cuanto puede ajustar usted del entorno.
2. **Costo cualitativo**: bajo, medio o alto, y por que. No hace falta ningun precio.
3. **Operacion**: **quien opera el sistema operativo y el runtime**, usted o el proveedor.
4. **Time-to-demo**: cuanto tarda en tener la primera demo de su CloudLite funcionando.

Cada celda: **maximo 2 lineas**, y siempre referida a su dominio y a sus capacidades. Una
celda que dice «mas control» no dice nada; «puedo instalar la libreria de codigos de barras
que necesita el prestamo» si.

> La fila de **Operacion** es la que mas se equivoca. La responsabilidad no desaparece al
> subir de nivel: se **reparte**. Cuanto se reparte es exactamente lo que distingue los
> tres modelos, y en los tres usted sigue respondiendo por su propia aplicacion, sus
> permisos y sus datos.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2 pts la matriz con los cuatro criterios en el orden pedido y las cuatro columnas. 3 pts que las doce celdas de comparacion hablen del dominio propio y de sus capacidades, no de teoria general; se descuenta por cada fila escrita en abstracto. 1.25 pts que la fila de operacion reparta correctamente la responsabilidad en los tres modelos y no afirme que en PaaS o SaaS el equipo deja de responder por su aplicacion.

---

## Pregunta 6 - Respuesta escrita · 12.5 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## ADR-001: modelo de servicio dominante de CloudLite

Redacte el **ADR-001** con estas cuatro secciones rotuladas, en este orden y sin agregar
otras:

1. **Titulo**: `ADR-001 Modelo de servicio dominante de CloudLite App`.
2. **Estado**: `Aceptado` mas la fecha.
3. **Decision**: **una sola frase** que nombre **un unico modelo dominante** —IaaS, PaaS o
   SaaS— para la aplicacion propia de CloudLite.
4. **Alternativas descartadas**: **exactamente 2**, cada una con el motivo del descarte
   **expresado en terminos de su dominio**, no en abstracto.

> **Si la seccion 3 nombra dos modelos, esa seccion vale cero.** «Un poco de PaaS y un poco
> de IaaS» no es una decision: es no haber decidido. Puede aclarar en las alternativas que
> consume **SaaS satelite** para identidad y correo; eso no rompe la regla, porque el
> modelo dominante se refiere a **su** aplicacion.

Un ADR (Architecture Decision Record) es un formato real, usado en equipos reales: sirve
para que dentro de seis meses alguien —incluido usted— entienda **por que** se decidio asi
y **que se descarto**. Un ADR con una sola opcion no documenta una decision: documenta un
hecho.

Este ADR se reutiliza en el informe del PI y en la sustentacion de la Clase 15.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2 pts titulo y estado con fecha. 4 pts la decision en UNA frase con UN modelo dominante; cero en este criterio si nombra dos o mas modelos. 6.5 pts las dos alternativas descartadas con el motivo del descarte atado al dominio: 3.25 pts cada una, y se pierde la mitad de cada una si el motivo es generico («es mas caro», «es mas complejo») sin decir mas caro o mas complejo PARA QUE de su sistema.

---

## Pregunta 7 - Respuesta escrita · 6.25 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Consecuencias del ADR-001

Escriba las **consecuencias** de la decision que tomo en la pregunta anterior, cubriendo
**los tres ejes** y rotulandolos:

- **Operacion**: que tiene que hacer usted a partir de ahora, y que deja de hacer.
- **Costo**: que se abarata y que se encarece, en terminos cualitativos.
- **Aprendizaje**: que tiene que aprender para sostener esa decision durante el semestre.

En cada eje escriba **al menos una consecuencia positiva y una negativa**, rotuladas con
`+` y `-`. **Al menos una de las negativas debe hablar de amarre al proveedor o de perdida
de control**: es la contrapartida que casi nunca se escribe y la que la sustentacion de la
Clase 15 va a pedir.

> Una consecuencia no es una ventaja de folleto. «Es mas facil» no es una consecuencia;
> «no voy a poder instalar la libreria de codigos de barras y tendre que buscar una
> alternativa que el proveedor soporte» si lo es, porque describe algo que cambia en su
> trabajo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

3 pts los tres ejes presentes y rotulados (operacion, costo, aprendizaje). 2 pts que cada eje traiga al menos una consecuencia positiva y una negativa marcadas con + y -. 1.25 pts que al menos una negativa hable de amarre al proveedor o de perdida de control. Se descuenta por cada consecuencia escrita como ventaja de folleto («es mas facil», «es mas moderno») en vez de como algo que cambia en el trabajo del estudiante.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **24**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
