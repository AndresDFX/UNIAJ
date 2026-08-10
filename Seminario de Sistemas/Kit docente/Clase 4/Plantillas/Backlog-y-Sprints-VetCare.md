# Backlog agil y plan de sprints - Proyecto Integrador VetCare
**Clinica Veterinaria Huellitas** | Equipo: ______________

> Agil NO es trabajar sin documentacion. Aqui el incremento de cada sprint ES un artefacto de diseno.

---

## 1. Product Backlog priorizado

| # | Historia (Como / quiero / para) | Prioridad | Valor para Huellitas | Sprint |
|---|---|---|---|---|
| 1 | Como auxiliar quiero registrar un paciente con su propietario para no perder la ficha | Alta | Ataca el dolor de fichas extraviadas | 1 |
| 2 | Como veterinaria quiero buscar la historia por nombre o documento para no ir al archivador | Alta | Ataca el dolor de busqueda lenta | 1 |
| 3 | Como veterinaria quiero registrar la consulta con diagnostico y tratamiento | Alta | Historia clinica completa | 2 |
| 4 | Como veterinaria quiero ver la historia clinica completa del paciente | Media | Contexto para la atencion | 2 |
| 5 | Como administradora quiero ver consultas por mes y por especie | Media | Ataca el dolor de cero metricas | 3 |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

---

## 2. Plantilla de historia con criterios de aceptacion

```
HU-__  Titulo
  Como  <rol en la clinica>
  quiero <lo que necesita hacer>
  para  <el beneficio de negocio>

Criterio 1 (camino feliz)
  Dado que ...
  Cuando ...
  Entonces ...

Criterio 2 (camino alternativo o de error)
  Dado que ...
  Cuando ...
  Entonces ...
```
Regla: si no hay al menos un criterio de error, la historia esta incompleta.

---

## 3. Definicion de Terminado (DoD) del equipo

Una tarjeta pasa a **Aprobado** solo si cumple TODO:

- [ ] Diagrama hecho en draw.io y exportado a PDF
- [ ] Mockup de la pantalla asociada (Figma o Penpot)
- [ ] Nombres de campos coinciden con el diccionario de datos
- [ ] Revisado por un companero distinto al autor
- [ ] Visto bueno del cliente en la revision de sprint

---

## 4. Plan de sprints del semestre

| Sprint | Objetivo (en una frase, en lenguaje de la clinica) | Incremento que la clinica puede VER | Fecha de revision |
|---|---|---|---|
| 1 | | Mockup navegable de la ficha del paciente | |
| 2 | | Prototipo de busqueda + diagrama de clases | |
| 3 | | Diccionario de datos + mockup del tablero de metricas | |

**Prohibido:** sprint 1 = analisis, sprint 2 = diseno, sprint 3 = construccion. Eso es cascada disfrazada.

---

## 5. Tablero de flujo (Kanban)

```
| Por hacer | Modelando (WIP 2) | En revision del cliente (WIP 2) | Aprobado |
|-----------|-------------------|---------------------------------|----------|
|           |                   |                                 |          |
```
Politica de columna: nadie empieza una tarjeta nueva si la columna ya llego a su limite; se ayuda a destrabar la que esta atascada.

---

## 6. Retrospectiva (3 lineas al cierre de cada sprint)

- Que funciono: ______________________________________
- Que no funciono: ___________________________________
- Que cambiamos el proximo sprint: ___________________

---

## 7. Checklist antes de subir a ExamLab

- [ ] Backlog priorizado con justificacion de valor.
- [ ] Tres historias con criterios Dado/Cuando/Entonces y camino de error.
- [ ] Cada sprint termina en algo visible para el cliente.
- [ ] El tablero declara DoD y limites de trabajo en curso.
