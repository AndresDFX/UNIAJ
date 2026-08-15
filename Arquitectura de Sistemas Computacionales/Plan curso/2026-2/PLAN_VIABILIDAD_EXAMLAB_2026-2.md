# Plan de viabilidad — ExamLab (Arquitectura de Sistemas Computacionales · 2026-2)

| Campo | Valor |
|---|---|
| Curso | Arquitectura de Sistemas Computacionales (FI303380) |
| Grupo | **6303C** |
| Docente | Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co` |
| PI | **CloudLite** |
| Fecha | 2026-08-08 |
| Estado | **Borrador para aprobación docente** |
| Relación con otros planes | Complementa `PLAN_VIABILIDAD_FLOCI_2026-2.md` (mismo carpeta). Floci = herramienta de laboratorio Docker; **este plan = dónde vive y se califica la evaluación** (parciales, actividades autónomas, PI). No se solapan |

---

## 0. De dónde sale este documento

A diferencia de Bases de Datos II (curso vacío), acá **sí hay material real** para refactorizar: 3 parciales completos con solución (`Parciales/*.docx`), 2 actividades autónomas del PI con su guion completo (Clases 13 y 15), y el trabajo ya hecho de viabilidad de Floci. Todo eso vive hoy en **Word + Campus Virtual UNIAJC + Google Docs/Drive** — nada está en ExamLab todavía. Este plan mapea ese material real a construcciones de la plataforma, no inventa contenido nuevo.

## 1. Resumen ejecutivo

**Veredicto: viable, y más avanzado de lo esperado.**

El hallazgo central: la **pizarra de ExamLab ya tiene un catálogo de formas diseñado específicamente para este tipo de curso** — 9 íconos de arquitectura AWS (EC2, S3, RDS, Lambda, API Gateway, SQS, SNS, CloudFront, DynamoDB, VPC) más una topología de redes completa (router, switches L2/L3, firewall, balanceador, nube WAN, plantilla de LAN) más formas UML/POO (clase, interfaz, clase abstracta, enum, herencia). Esto no es un ajuste menor: es prácticamente el 100% de lo que este curso necesita para diagramar, y ya existe.

Lo que ExamLab **no** intenta resolver, y no debería, es lo que Floci ya está evaluando: ejecutar contenedores o emular APIs cloud reales. Eso requiere Docker (ver el plan de Floci) y queda fuera de la plataforma de evaluación a propósito — el `so_consola` de ExamLab (Linux real en el navegador) no tiene red ni puede correr Docker-en-Docker, así que no compite con Floci ni lo reemplaza.

| Bloque del curso | Cobertura ExamLab hoy |
|---|---|
| Diagramas de arquitectura (C4, red, AWS, UML) | **Completa** — catálogo ya construido |
| Parciales (opción múltiple, V/F, desarrollo, caso) | **Casi completa** — falta el tipo "emparejamiento" (ver §3) |
| Actividades autónomas del PI (documentos + capturas) | **Completa** — `abierta` con adjuntos |
| PI CloudLite (grupos, sustentación, pitch, Q&A) | **Completa** |
| Laboratorio Docker/cloud real (Floci) | **Fuera de alcance de ExamLab a propósito** — es el objeto del otro plan |

## 2. Qué existe HOY en ExamLab que sirve para este curso, sin cambios

| Capacidad | Dónde vive (repo ExamLab) | Para qué sirve acá |
|---|---|---|
| 9 íconos AWS (EC2/S3/RDS/Lambda/API Gateway/SQS/SNS/CloudFront/DynamoDB/VPC) | `src/modules/whiteboard/excalidraw-libraries.ts` | Clase 1 (intro cloud), Clase 7 (redes/almacenamiento), diagramas del PI |
| Topología de redes (router, switch L2/L3, firewall, balanceador, WAN, LAN) | mismo archivo | Clase 3 (virtualización/contenedores), Clase 7 |
| Formas UML/POO (clase, interfaz, clase abstracta, enum, herencia) | mismo archivo | Clase 4 (microservicios/distribuidos) — diagramas de componentes |
| Tipo `cerrada` (opción única) + V/F como caso de 2 opciones | `questions.type` | Secciones A y B de los 3 parciales existentes (ver §4) |
| Tipo `abierta` + calificación IA con rúbrica | `questions.type` | Secciones C/D de desarrollo y caso — y las 2 actividades autónomas del PI (Clases 13, 15) |
| Proyectos con grupos, `defense_factor`, `repository_url`, `codigo_zip` | mig. `20260507150000_*`, `20260507160000_*`, `20260507170000_*` | PI CloudLite completo: avance (Clase 11-12), paquete final + pitch + Q&A (Clase 15) |
| Modelo de pesos por corte | CLAUDE.md § "Modelo de pesos / cortes" | Coincide exacto con el esquema ya usado: Corte 1=30% (parcial 10%), Corte 2=30% (parcial 10%), Corte 3=40% (parcial 15%) — verificado en los headers de los 3 `.docx` de `Parciales/` |
| `so_consola` (Linux real, sin red) | `docs/server-console-v86.md` | Práctica conceptual de Clase 3 (contenedores a nivel de SO) — **no** para correr Docker de verdad, eso sigue siendo Floci |

## 3. La brecha real

- **Tipo de pregunta "emparejamiento"**: los 3 parciales existentes usan una sección fija de emparejamiento (20 de 100 puntos, igual en los tres). **No existe como tipo nativo** en `questions`/`workshop_questions`/`project_files`/`question_bank` — confirmado contra el código, no supuesto. Workaround disponible hoy: `abierta` pidiendo escribir los pares, calificada por IA — funciona pero pierde la interacción de arrastrar. Si se refactoriza el Parcial 1 a la plataforma, esta sección es la única que no traslada 1:1.
- **No hay red en `so_consola`**: Clase 6 (Seguridad en la nube) y Clase 8 (parte de monitoreo/CI-CD) tienen componentes que idealmente tocarían un servicio real (escaneo de puertos, un pipeline que de verdad corra). Eso sigue correspondiendo a Floci/Killercoda, no a ExamLab — no es un gap de ExamLab, es una frontera de diseño correcta.

## 4. Refactor de los 3 parciales existentes → estructura ExamLab

Los 3 documentos ya tienen la misma estructura fija (extraída del `.docx`, no inferida): A. Selección múltiple (20 pts) · B. Emparejamiento o V/F (20 pts) · C. Desarrollo (25 pts) · D. Caso (35 pts) · Total 100 → nota /20 sobre 5.0.

| Parcial | Corte | Clases evaluadas | Sección A→B→C→D en ExamLab |
|---|---|---|---|
| 1 — Cloud, virtualización, distribuidos | Corte 1 (10% de 30%) | 1-4 | `cerrada` ×4 → `abierta` (pares, ver §3) → `abierta`/`diagrama` → `abierta`/`diagrama` con rúbrica |
| 2 — Seguridad, redes, monitoreo, CI/CD | Corte 2 (10% de 30%) | 6-8 | `cerrada` ×4 → `cerrada` (V/F, nativo, sin gap) → `abierta` → `abierta`/`diagrama` |
| 3 — Rendimiento, escalabilidad, cierre | Corte 3 (15% de 40%) | 11-13 | `cerrada` ×4 → `abierta` (pares) → `abierta` → `abierta`/`diagrama` con sustentación |

La clave de solución de cada parcial (`... - SOLUCION.docx`) ya trae la respuesta correcta marcada (`→ Clave: b`) — se traslada directo al campo de respuesta correcta / rúbrica de cada pregunta, sin rediseñar el contenido.

## 5. Actividades autónomas del PI (Clases 13 y 15) → ExamLab

Ambas ya tienen guion completo (contexto, objetivo, entregable, herramientas, pasos, criterios de éxito, checklist, entrega). Mapeo directo:

- **Clase 13 — Política de autoescalado**: entregable = documento con triggers/límites. → Pregunta `abierta` de proyecto (o `diagrama` si se pide el esquema de triggers), con **envío individual**: la modalidad del curso es individual por defecto y la entrega en ExamLab siempre es individual, incluso si el docente autorizó trabajar el artefacto en equipo. (ExamLab tiene un `group_mode` de proyectos con "un envío por equipo, cualquier miembro edita"; **no se usa**, porque se evalúa la respuesta escrita de cada estudiante.)
- **Clase 15 — Sustentación final**: paquete + pitch 5-8 min + Q&A escrito. → `codigo_zip` (o adjuntos) para el paquete, más el `DefensePanel` del docente para registrar la sustentación (nota entrega × factor) — es exactamente para esto que existe ese componente.

Los criterios de éxito de cada actividad (ya escritos, ej. ">=2 triggers + min/max + cooldown narrado") se trasladan directo como rúbrica de la pregunta — de nuevo, no hay que redactar contenido nuevo, solo trasladarlo.

## 6. Relación con el plan Floci

No se tocan. Un ejemplo concreto de cómo conviven: si se aprueba el piloto de Floci en la Clase 7, la evidencia de ese laboratorio (capturas de "bucket creado / objeto subido / listado") se **entrega a través de ExamLab** como pregunta `abierta` con adjuntos o como parte del `codigo_zip` del PI — igual que cualquier otro taller. ExamLab es la plataforma de evaluación; Floci es la herramienta de laboratorio. Uno no sustituye al otro.

## 7. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Se intenta forzar "emparejamiento" nativo antes de decidir el workaround | Bajo-medio | Usar `abierta` con pares para el refactor del Parcial 1 (el más próximo, Clase 5) |
| Se asume que `so_consola` puede sustituir a Floci para las Clases 3/6 | Medio | Dejar explícito en el Kit docente que `so_consola` es Linux SIN red — no reemplaza el piloto Floci |
| Las fechas/pesos de este documento quedan desactualizadas si cambia el Acuerdo | Bajo | Ya están verificados contra los `.docx` reales (2026-08-08); revisar si el Acuerdo institucional cambia |

## 8. Decisión recomendada y próximos pasos

1. Aprobar este plan como base del refactor (no reemplaza el material existente, lo traslada).
2. Empezar el refactor por el **Parcial 1** (más cercano, Clase 5) para validar el workaround de emparejamiento con datos reales antes de tocar los otros dos.
3. Cargar el catálogo de formas de pizarra en el Kit docente de Clases 1, 3, 4, 7 (ya existe, solo falta señalarlo en el guion de cada clase).
4. Trasladar las 2 actividades autónomas del PI (Clases 13, 15) como proyecto con grupos + `DefensePanel`.
5. Mantener el plan Floci corriendo en paralelo, sin mezclarlo con este documento.

## 9. Fuentes internas

| Recurso | Ruta |
|---|---|
| Catálogo de formas de pizarra (AWS + redes + UML) | `src/modules/whiteboard/excalidraw-libraries.ts` (repo ExamLab) |
| Modelo de pesos/cortes | `CLAUDE.md` § "Modelo de pesos / cortes" (repo ExamLab) |
| Proyectos: sustentación + grupos | `CLAUDE.md` § "Proyectos: sustentación + link al repo" y "Trabajo en grupo" |
| Los 3 parciales (contenido fuente de §4) | `../../Parciales/*.docx` |
| Actividades autónomas (contenido fuente de §5) | `../../Clases/Clase 13 - .../Actividad autonoma...docx`, `../../Clases/Clase 15 - .../Actividad autonoma...docx` |
| Plan de viabilidad Floci (complementario) | `PLAN_VIABILIDAD_FLOCI_2026-2.md` (misma carpeta) |

---

*Documento interno Plan de curso · no distribuir a estudiantes hasta aprobación docente.*
