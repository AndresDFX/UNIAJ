# Taller de la Clase 6 en ExamLab - configuracion

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Taller:** Actividad del Corte 2 (preguntas 1 a 3) - Amenazas, controles y secretos
- **Preguntas:** 3 · **Total:** 25 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Modelo de amenazas mínimo + controles para CloudLite
- **Entregable de la clase:** Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Las preguntas 1 a 3 de la actividad del Corte 2, que es una sola para las Clases 6, 7, 8 y 10. El estudiante deja el modelo de amenazas de su dominio con sus controles ubicados en los diagramas y la politica de secretos escrita.

---

## Pregunta 1 - Respuesta escrita · 8.75 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Cinco amenazas STRIDE-lite de SU dominio

Liste **5 amenazas** aplicadas a su CloudLite. **No una lista generica copiada de
internet**: cada amenaza tiene que nombrar **el actor o el dato concreto de su dominio** que
pone en riesgo.

Use STRIDE como guia de categorias: **S**poofing (suplantacion), **T**ampering (alteracion),
**R**epudiation (negacion), **I**nformation disclosure (fuga), **D**enial of service y
**E**levation of privilege. No hacen falta las seis: hacen falta cinco amenazas reales.

Amenazas tipicas del curso, como referencia de la **forma** esperada, no para copiarlas:

- secretos dentro de la imagen del contenedor
- API sin autenticacion
- registros que guardan tokens
- datos personales viajando sin TLS

> La diferencia entre una amenaza y una frase de manual es el complemento. «Fuga de
> informacion» no es una amenaza; «un estudiante puede consultar por identificador las
> reservas de otro porque el endpoint no valida a quien pertenece» si lo es, porque nombra
> al actor, el dato y el camino.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1.75 pts por amenaza bien formada, hasta 5. Una amenaza suma completo solo si nombra el actor o el dato concreto del dominio y el camino por el que ocurre. Una amenaza generica («podrian hackear la base de datos») vale la mitad. Se descuenta si dos amenazas son la misma con otras palabras.

---

## Pregunta 2 - Respuesta escrita · 8.75 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## El control de cada amenaza y donde se ve

Para **cada una de las 5 amenazas** de la pregunta anterior indique:

1. **El CONTROL que la mitiga.** Concreto y verificable, no «mejorar la seguridad».
2. **DONDE se ve ese control en sus diagramas**: sobre que **caja** o sobre que **flecha**
   del C4 Containers o del diagrama de Despliegue aplica.

Presentelo como tabla: `Amenaza | Control | Donde se ve (caja o flecha)`.

**Debe aparecer el principio de menor privilegio**, aunque sea narrado: que cada componente
y cada rol reciba exactamente los permisos que necesita y ni uno mas. Diga sobre que
componente de SU sistema lo aplica y que deja de poder hacer al aplicarlo.

> Un control que no se puede senalar en un artefacto no existe todavia: es una intencion.
> Por eso la segunda columna vale tanto como la primera. Si no encuentra donde ubicarlo,
> probablemente le falta una caja o una frontera en el diagrama.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1 pt por cada control concreto y verificable, hasta 5. 2.5 pts por senalar correctamente la caja o la flecha de cada uno; se prorratea. 1.25 pts por el principio de menor privilegio aplicado a un componente concreto, diciendo que deja de poder hacer. Un control tipo «usar buenas practicas» no suma.

---

## Pregunta 3 - Respuesta escrita · 7.5 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Politica de secretos del repositorio y de la CI

Defina la politica de secretos de CloudLite respondiendo estas cuatro preguntas:

1. **Donde viven** los secretos.
2. **Quien los rota**.
3. **Con que frecuencia** se rotan.
4. **Que esta explicitamente prohibido**.

> **Regla del curso:** los secretos van en la **configuracion del repositorio** (los
> `secrets` del proyecto), **nunca** en el `Dockerfile`, en el `README` ni en el YAML en
> claro. Un secreto escrito en el Dockerfile queda en el **historial de capas** de la imagen
> para siempre: cualquiera que tenga la imagen lo lee, aunque el archivo se borre en una
> capa posterior.

Cierre nombrando **que haria si un secreto se filtra**: el primer paso no es borrar el
commit, es **rotar la credencial**, porque el historial ya salio del equipo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1.5 pts cada una de las cuatro preguntas respondida de forma concreta (donde, quien, cada cuanto, que se prohibe): 6 pts. 1.5 pts el procedimiento ante filtracion empezando por rotar la credencial y no por borrar el commit. Cero en la primera pregunta si la respuesta admite guardar secretos en el repositorio en claro.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **25**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
