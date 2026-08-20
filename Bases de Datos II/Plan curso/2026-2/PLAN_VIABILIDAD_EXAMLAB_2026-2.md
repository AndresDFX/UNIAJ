# Plan de viabilidad — ExamLab (Bases de Datos II · 2026-2)

| Campo | Valor |
|---|---|
| Curso | Bases de Datos II |
| Docente | Julian Andres Castaño Espinosa |
| PI | **VetCare** (inferido del título de Clase 1 — "Revisión BD I y arranque VetCare". **No hay ningún documento de PI todavía**: `Clases/Proyecto Integrador/` y `Kit docente/Proyecto Integrador/` están vacíos) |
| Fecha | 2026-08-08 |
| Estado | **Borrador para aprobación docente** — no hay `Plan curso/2026-2` previo en este curso; es la primera vez que se documenta |
| Relación con otros planes | Complementa (no reemplaza) el plan de viabilidad de Floci de Arquitectura — ver §4. Ese plan es sobre **herramientas de laboratorio Docker**; este es sobre la **plataforma de evaluación** (dónde viven parciales/talleres/proyecto y cómo se califican) |

---

## 0. De dónde sale este documento

Este curso **no tiene material propio todavía**. Todo lo que existe son las 15 carpetas de `Clases/` con el nombre del tema (sin archivos adentro) y dos README de plantilla. A diferencia del plan de Arquitectura, acá no hay parciales ni actividades que "refactorizar" — es diseño desde cero. La estructura de cortes/fechas de abajo se **confirmó** en el calendario del semestre (`config/calendario/semestre_2026_2.json`, fuente de verdad): 13 sesiones que cubren los 15 temas, parciales en las **sesiones 5/9/12** y la **sesión 13 dedicada a las sustentaciones del PI**. Ese JSON manda sobre cualquier número escrito aquí.

## 1. Resumen ejecutivo

**Veredicto: viable con una condición fuerte.**

Todo lo que NO es "ejecutar SQL de verdad" está cubierto hoy por ExamLab sin desarrollo nuevo: diagramas entidad-relación, teoría, análisis de casos, gestión del PI con sustentación, y hasta el modelo de pesos/cortes coincide con el esquema institucional (ver §6).

Lo que SÍ es el corazón del curso — procedimientos almacenados, disparadores, control de concurrencia, particionamiento, tuning — **no tiene un runner nativo en ExamLab hoy**. Hay un camino que funciona **ya mismo, sin tocar infraestructura** (Python + `sqlite3`, dentro del tipo de pregunta `codigo` que ya existe), pero cubre solo un subconjunto real del temario: dialecto SQLite, sin PL/pgSQL, con concurrencia de un solo escritor. Para los temas avanzados hace falta más, y apareció una alternativa concreta que vale la pena evaluar (**PGlite** — Postgres real compilado a WASM, corre en el navegador, sin Docker, sin servidor — ver §5).

| Bloque del curso | Cobertura ExamLab hoy |
|---|---|
| Modelado ER, teoría, análisis de casos | **Completa** |
| Gestión del PI (grupos, sustentación, entrega) | **Completa** |
| SQL básico (DDL/DML, vistas, índices, transacciones simples) | **Parcial, ya funciona** (Python + `sqlite3`) |
| Procedimientos almacenados con dialecto real, disparadores completos | **No** — requiere motor real |
| Control de concurrencia (multi-sesión), particionamiento, tuning a escala | **No** — ningún camino actual lo cubre bien, ni siquiera parcialmente |

## 2. Qué existe HOY en ExamLab que sirve para este curso, sin cambios

| Capacidad | Dónde vive (repo ExamLab) | Para qué sirve acá |
|---|---|---|
| Formas de pizarra **DB · Tabla / Entidad / Relación / Atributo** (notación ER) | `src/modules/whiteboard/excalidraw-libraries.ts` | Modelado relacional y normalización — Clase 1 (arranque VetCare), Clase 2 |
| Tipo de pregunta `abierta` + calificación IA | `questions.type` | Preguntas conceptuales, análisis de casos — Clase 13 |
| Tipo `codigo` con `language="python"` + módulo `sqlite3` (stdlib, **sin instalar nada**) | `src/modules/code/CodeEditor.tsx`, runner `execute-code` | SQL real de verdad: `CREATE TABLE`, `INSERT`, `SELECT`, vistas, índices, transacciones `BEGIN/COMMIT/ROLLBACK` — Clases 2, 6, y la mitad "básica" de 7 y 8 |
| Proyectos con grupos (`teacher_assigned`), sustentación (`defense_factor`), link a repo, `codigo_zip` | `supabase/migrations/20260507170000_*`, `20260507150000_*` | Proyecto Integrador VetCare — Clases 11, 12, 15 |
| Reto en vivo (encuestas tipo Kahoot) | módulo `polls` | Repaso rápido de vocabulario/teoría por clase (candidatas: 2, 4, 10) |
| Modelo de pesos por corte (`cut.weight` + buckets `exam_weight`/`workshop_weight`/`project_weight`) | CLAUDE.md § "Modelo de pesos / cortes" | Representa **1:1** el esquema "X% del Corte, Corte = Y% de la nota" que ya usa Arquitectura con el mismo docente — ver §6 |
| `so_consola` (Linux real vía v86 en el navegador) | `docs/server-console-v86.md` | Práctica de administración de SO como base conceptual de "administración de bases de datos" (Clase 2) — **con un límite importante**: sin red, así que no hay cliente `psql`/`mysql` real contra un servidor. Sirve para permisos de archivos, procesos, backups a disco — no para administrar un motor de BD real |

## 3. La brecha real

- **SQL con dialecto real** (procedimientos almacenados PL/pgSQL o T-SQL, disparadores completos con `NEW`/`OLD`, control de concurrencia multi-sesión, particionamiento, `EXPLAIN ANALYZE` de verdad): **no existe**. El camino de Python+`sqlite3` cubre aproximadamente la primera mitad del temario (Clases 1-8, con matices) y no cubre nada de la segunda (Clases 7-10 en su parte avanzada).
- **Tipo de pregunta "emparejamiento"**: no existe como tipo nativo en ningún nivel de la plataforma (`questions`, `workshop_questions`, `project_files`, `question_bank`). Si este docente usa el mismo formato de examen que en Arquitectura (sección fija de emparejamiento, 20% del parcial — confirmado en los 3 parciales de ese curso), acá se repetiría el mismo hueco. Workaround disponible hoy: pregunta `abierta` pidiendo "escriba los pares X-Y", calificada por IA — funciona, pero pierde la interacción de arrastrar/emparejar.
- **Estado persistente entre clases**: cada ejecución de `codigo` es efímera y aislada — no hay una base de datos que persista entre envíos o entre estudiantes. Para este curso pesa más que en otros, porque el PI (VetCare) es literalmente una base de datos que se construye clase a clase. Mitigación práctica: cada ejercicio de clase es autocontenido (crea su propio esquema con datos de muestra al inicio del script), y el AVANCE real del PI se entrega como `codigo_zip` (dump `.sql` + capturas), no como estado vivo entre sesiones.

## 4. Relación con el plan de Floci (Arquitectura)

Son dos preguntas distintas y no hay que confundirlas:

- **Floci** responde "¿cómo practican los estudiantes contra una nube real, sin cuenta ni tarjeta?" — necesita Docker, por eso ese plan lo marca como excepción a "solo navegador".
- **Este plan** responde "¿dónde viven y se califican los parciales/talleres/proyecto de este curso?" — es sobre la plataforma de evaluación, no sobre el laboratorio.

No compiten. Si mañana se aprueba un piloto de Floci o de un motor de BD real para Bases de Datos II, la evidencia de ese trabajo (capturas, dump SQL, código) se **entrega a través de ExamLab** igual que cualquier otro taller — vía `codigo_zip` o `abierta` con adjuntos.

## 5. Caminos para SQL real — para decidir, no implementados

| Camino | Qué da | Costo | Estado |
|---|---|---|---|
| **A — Python + `sqlite3`** (ya disponible) | DDL/DML, vistas, índices, transacciones básicas, hasta triggers y CTEs simples (SQLite los soporta) | Cero — funciona con el tipo `codigo` que ya existe, hoy | **Verificar antes de anunciarlo**: confirmar que el runner Python (AL2023, `/usr/bin/python3`) trae el módulo `sqlite3` compilado — es lo estándar, pero no está probado contra el runner real de ExamLab en este análisis |
| **B — PGlite** (`@electric-sql/pglite`, verificado en npm: Apache-2.0, v0.5.4) | **Postgres real** compilado a WASM — corre dentro del navegador del estudiante, sin servidor, sin Docker, sin red. Soporta PL/pgSQL, triggers completos, transacciones reales, extensiones | Dependencia npm nueva (el repo usa `bun.lock`; alguien con `bun` tiene que instalarla y commitear el lockfile) + trabajo de integración (nuevo tipo de pregunta o modo del editor de código, ejecución en el navegador en vez de en el runner Lambda) + validar tamaño real del bundle WASM antes de cargarlo por defecto | **Camino más prometedor, sin validar.** No se probó contra este proyecto — es una pista para un spike técnico, no una capacidad confirmada |
| **C — Servidor Postgres efímero por estudiante** (ej. schema descartable en un proyecto Supabase aparte) | Postgres real, multi-sesión de verdad (control de concurrencia real con 2+ conexiones) | Alto: edge function nueva, aprovisionamiento/limpieza de schemas, requiere red — **no apto para examen con proctoring**, solo para taller/práctica | No evaluado en profundidad; solo la opción si control de concurrencia multi-sesión real es un objetivo de aprendizaje no-negociable |

**Recomendación de esta sección**: no bloquear el curso por esto. Empezar con el Camino A (ya funciona) para Clases 1-8, y agendar un spike de medio día para PGlite (Camino B) antes de diseñar las Clases 7-10 en detalle — si PGlite funciona bien ahí, cambia sustancialmente qué se puede pedir en esas clases.

## 6. Cortes y pesos — el modelo de ExamLab ya encaja

Arquitectura (mismo docente, mismo periodo) usa: Corte 1 = 30% de la nota (parcial vale 10% de ese 30%), Corte 2 = 30% (parcial 10%), Corte 3 = 40% (parcial 15%). El modelo de pesos de ExamLab (`cut.weight` = % de la nota final; `exam.weight` = % de la nota final para ESE examen, acotado por el bucket `cut.exam_weight`) representa esto **exactamente**, sin adaptación. Si BD II sigue el mismo esquema institucional (a confirmar), la configuración de cortes es una copia directa.

## 7. Mapeo clase por clase (borrador — sujeto a la revisión de §5)

| Clase | Tema | Actividad en ExamLab | Tipo / módulo |
|---:|---|---|---|
| 1 | Revisión BD I y arranque VetCare | Diagrama ER inicial del dominio VetCare | Pizarra (`DB · Entidad/Relación/Atributo`) |
| 2 | Administración de bases de datos | Práctica de permisos/backup a disco | `so_consola` (con la limitación de red anotada en §2) |
| 3 | Procedimientos almacenados | Ejercicios básicos (funciones SQLite) | `codigo` (Python + `sqlite3`) — **limitado**, ver §3 |
| 4 | Funciones, disparadores, seguridad, respaldo | Triggers básicos + reflexión de seguridad | `codigo` + `abierta` |
| [5] | *(Parcial 1, inferido)* | Selección múltiple + desarrollo + diagrama | `cerrada` + `abierta`/`diagrama` — **sin emparejamiento nativo**, ver §3 |
| 6 | Optimización de consultas | `EXPLAIN QUERY PLAN` (SQLite) sobre datos de muestra | `codigo` |
| 7 | Índices y particionamiento | Índices sí (SQLite); particionamiento **no cubierto** hoy | `codigo` (parcial) + `abierta` conceptual para particionamiento |
| 8 | Tuning y transacciones | Transacciones básicas sí; tuning a escala **no cubierto** | `codigo` (parcial) + `abierta` conceptual |
| [9] | *(Parcial 2, inferido)* | Igual que Parcial 1 | ídem |
| 10 | Control de concurrencia | **Sin camino bueno hoy** (SQLite es single-writer) | `abierta` conceptual únicamente, hasta resolver §5 |
| 11 | Avance del proyecto final | Avance VetCare: dump `.sql` + capturas | Proyecto — `codigo_zip` |
| 12 | Integración y preparación final | Integración del esquema completo | Proyecto — `codigo_zip` |
| 13 | Análisis de casos reales | Casos + justificación de decisiones de diseño | `abierta` con rúbrica IA |
| [14] | *(Parcial 3, inferido)* | Caso de diseño + sustentación parcial | `abierta`/`diagrama` |
| 15 | Presentación del proyecto y cierre | Sustentación VetCare (pitch + Q&A) | Proyecto — `DefensePanel` (nota entrega × factor de sustentación) |

## 8. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Se anuncia "SQL real" a estudiantes sin verificar que `sqlite3` esté disponible en el runner de producción | Alto (clase se cae en vivo) | Probar UN script Python con `import sqlite3` en el ambiente real antes de la Clase 3 |
| Se diseña la Clase 10 (concurrencia) asumiendo PGlite sin haber hecho el spike | Alto | No comprometer la Clase 10 en el plan de curso final hasta tener el spike de §5 hecho |
| El docente espera "emparejamiento" nativo y no aparece hasta el día del parcial | Medio | Decidir el workaround (`abierta` con pares) ANTES de maquetar el primer parcial en la plataforma |
| Fechas/pesos de este documento (inferidos de Arquitectura) no coinciden con el Acuerdo real de BD II | Medio | Confirmar contra el Acuerdo institucional de este curso antes de publicar |

## 9. Decisión recomendada y próximos pasos

1. Aprobar este plan como punto de partida (no reescribe nada porque no había nada escrito).
2. Confirmar fechas/pesos reales de BD II contra el Acuerdo institucional (§6 es una inferencia).
3. Decidir el workaround de "emparejamiento" antes de maquetar el primer parcial.
4. Probar `import sqlite3` contra el runner real de ExamLab (5 minutos, cero riesgo).
5. Agendar el spike de PGlite (medio día) antes de diseñar el detalle de Clases 7-10.
6. Recién con 4 y 5 resueltos, escribir el Kit docente de Clases 1-15 con las actividades concretas.

## 10. Fuentes internas

| Recurso | Ruta |
|---|---|
| Catálogo de formas de pizarra (incluye ER) | `src/modules/whiteboard/excalidraw-libraries.ts` (repo ExamLab) |
| Tipos de pregunta soportados | `supabase/migrations/*` (buscar `CHECK (type IN`) |
| Modelo de pesos/cortes | `CLAUDE.md` § "Modelo de pesos / cortes" (repo ExamLab) |
| Plan de viabilidad Floci (complementario, no se solapa) | `../../../Arquitectura de Sistemas Computacionales/Plan curso/2026-2/PLAN_VIABILIDAD_FLOCI_2026-2.md` |
| PGlite | https://github.com/electric-sql/pglite · npm `@electric-sql/pglite` (verificado 2026-08-08: Apache-2.0, v0.5.4) |

---

*Documento interno Plan de curso · no distribuir a estudiantes hasta aprobación docente.*
