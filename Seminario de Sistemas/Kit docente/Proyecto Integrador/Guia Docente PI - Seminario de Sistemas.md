# Guía docente — Proyecto Integrador · Seminario de Sistemas

**Privado docente** · No compartir en `Clases/`.

## Producto
**VetCare** — arquitectura y diseño del sistema para la Clínica Veterinaria «Huellitas».
PI **compartido con Programación II**: mismo producto, distinto entregable
(aquí los planos, allá el software).

## Casos de matrícula
- **A** (ambas materias): aquí se califican los planos; el código se califica en Prog II.
- **C** (solo Seminario): cierra con SDD + mockup navegable. Ruta completa y válida,
  **no** una versión reducida — decirlo desde Clase 1.
- **B** (solo Prog II): no aplica aquí.

## Fases
1. Ingeniería de requisitos (RF/RNF)
2. Modelado UML (casos de uso, clases, dinámico)
3. Diseño de interfaz (wireframes + mockup navegable)
4. Arquitectura de datos (diccionario de datos)

## Hitos (por clase del material)
Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Requisitos + casos de uso y UML avanzado |
| Clase 13 | Wireframes y mockup |
| Clase 14 | Documento consolidado + ensayo |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | Sustentación 15 + 5 min |

## Rúbrica (100 pts)
Requisitos 20 · UML 25 · Interfaz 20 · Arquitectura de datos 15 · Plan de pruebas 10 · Sustentación 10

## Errores frecuentes
- Requisitos no verificables («debe ser rápido») sin criterio medible.
- Diagrama de clases que no corresponde a los casos de uso.
- Mockup que no cubre el flujo crítico (registrar → buscar → ver historial).
- Diccionario de datos sin tipos ni restricciones.

## Entrega y sustentación

- **Plazo único:** el que publique el docente en ExamLab, el mismo para todos los grupos.
- **Un solo .zip** (máx. 50 MB) con esta forma —los estudiantes tienen la carpeta «Plantilla de entrega» ya armada—:

```
Equipo <nombre>.zip
├── Documento de diseno.docx  ← requisitos, UML y datos, en el orden de la plantilla
├── diagramas/  ← cada diagrama en PNG + su archivo fuente
├── mockup/
│   └── Mockup.pdf  ← las pantallas exportadas
└── Plan de pruebas.docx  ← la tabla de casos de prueba de la plantilla
```

- **Qué debe traer cada pieza:**
  - **Documento de diseno.docx** — Requisitos RF y RNF verificables y trazables, casos de uso, diagrama de clases, un diagrama dinámico (actividad o secuencia), diccionario de datos con el formato de almacenamiento y el enlace al mockup navegable.
  - **diagramas/** — Casos de uso, clases y el dinámico, en PNG, con su archivo fuente.
  - **mockup/Mockup.pdf** — Las pantallas del flujo crítico (registrar, buscar y ver el historial), exportadas desde Figma, Penpot o Balsamiq.
  - **Plan de pruebas.docx** — Un caso de prueba por requisito crítico, trazado a su RF.
- **Sin enlace:** el campo de enlace de ExamLab está apagado; todo va dentro del .zip.
- **Proyecto en equipo** (el número de integrantes lo indica el docente cada semestre) — solo el proyecto: los demás entregables conservan su modalidad. **Uno de los integrantes sube la entrega del equipo** en ExamLab y queda para todos.
- **Sustentación:** en la última clase del curso, 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** el mockup navegable recorriendo el flujo crítico (registrar, buscar y ver el historial) y la trazabilidad de un requisito hasta su caso de uso y su caso de prueba.

Enunciado del estudiante en `Clases/Proyecto Integrador/`.
