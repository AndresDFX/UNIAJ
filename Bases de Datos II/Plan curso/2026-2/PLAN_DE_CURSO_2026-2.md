# Plan de curso propuesto — Bases de Datos II · 2026-2
> **CSV eventos:** `Plan curso/2026-2/calendario_eventos_2026-2.csv` (UTF-8 BOM). Importar en hoja/calendario cuando exista el listado de estudiantes (una fila = una clase; filtrar `es_parcial=si` para parciales síncronos).

- **Código:** FI303215
- **Grupo:** **641A-2**
- **Periodo:** **2026-2** · 10/08/2026 – 22/11/2026
- **Horario:** **Lunes 18:00 – 20:00** (120 min)
- **Modalidad:** **Presencialidad asistida** (Clase 1 y parciales presencial síncrono · resto virtual síncrona · festivos = clase autónoma)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Fuente oficial:** Microcurrículo FI303215 + Plan_de_curso FI303215
- **Calendario:** `Plan curso/2026-2/CALENDARIO_2026-2.md` · `config/calendario/semestre_2026_2.json`

## Ajuste 16 → 15 clases

El Plan oficial trae 16 sesiones. En 2026-2 hay **15 clases**: el cierre de la sesión 16 se integra en la **Clase 15**.

Criterio de modalidad por sesión (fijo 2026-2): modalidad del curso = Presencialidad asistida. Tipo por sesión = ver CSV. Parciales = siempre presenciales y síncronos; festivos = clase autónoma (sin parcial). Los parciales NUNCA se programan en día festivo ni en clase autónoma. Si el cierre teórico del corte cae en festivo/autónoma, el parcial se mueve a la última clase regular anterior del mismo corte; la clase autónoma de cierre queda como refuerzo sin parcial.

Parciales de este curso: Clases **5 / 9 / 14** (07/09/2026, 05/10/2026, 09/11/2026).

> **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo. Si un tema técnico estaba mezclado con el parcial, se reasigna a la última clase regular anterior del mismo corte.

> **Sesión 0 (no es clase temática):** `Clases/Presentacion del Curso - ….pptx` (logística, acuerdo, Padlet, evaluación, CONTENIDO). En el **día 1** puede ir Sesión 0 + Clase 1 dentro del bloque de 120 min. Se mantienen **15 clases** temáticas (1–15).

## Tabla Clase · Fecha · Tipo · Tema

| Clase | Fecha | Tipo | Tema (Trabajo dirigido) |
|---|---|---|---|
| 1 | 10/08/2026 | Virtual (síncrona) | Diagnóstico · Revisión de Bases de Datos I |
| 2 | 17/08/2026 | Autónoma (festivo) | Administración de bases de datos (Asunción de la Virgen) |
| 3 | 24/08/2026 | Virtual (síncrona) | Procedimientos almacenados |
| 4 | 31/08/2026 | Virtual (síncrona) | Funciones y disparadores · Seguridad y respaldo |
| 5 | 07/09/2026 | Presencial (síncrona) | **Parcial 1** |
| 6 | 14/09/2026 | Virtual (síncrona) | Optimización de consultas |
| 7 | 21/09/2026 | Virtual (síncrona) | Índices y particionamiento |
| 8 | 28/09/2026 | Virtual (síncrona) | Tuning de bases de datos · Gestión de transacciones |
| 9 | 05/10/2026 | Presencial (síncrona) | **Parcial 2** |
| 10 | 12/10/2026 | Autónoma (festivo) | Control de concurrencia · refuerzo sin parcial |
| 11 | 19/10/2026 | Virtual (síncrona) | Avance del proyecto final |
| 12 | 26/10/2026 | Virtual (síncrona) | Integración de aplicaciones externas · Preparación de presentación final |
| 13 | 02/11/2026 | Autónoma (festivo) | Análisis de casos reales (Todos los Santos) |
| 14 | 09/11/2026 | Presencial (síncrona) | **Parcial 3** |
| 15 | 16/11/2026 | Autónoma (festivo) | Presentación del proyecto + cierre · refuerzo sin parcial |

## Herramientas del curso (lista ajustada)

> Criterio UNIAJC: **herramientas gratuitas + en el navegador**, **sin tarjeta de crédito**. Los estudiantes **no deben instalar** software de escritorio de pago ni SGBD locales obligatorios. Cuenta gratuita (email) solo si el servicio lo exige.

| Uso en clase | Herramienta (gratis / navegador) | Acceso | Notas |
|---|---|---|---|
| SQL práctico (consultas, DDL/DML) | **DB Fiddle** (https://dbfiddle.uk / https://dbfiddle.dev) o **OneCompiler SQL** | Navegador | Playground inmediato; compartir enlace del ejercicio |
| Alternativa multi-motor (MySQL/PostgreSQL/Oracle-like) | **SQLTest.online Playground** (https://sqltest.online) o **RunSQL** (https://runsql.com) | Navegador | Comparar dialectos sin instalar SGBD |
| Procedimientos / PL-SQL orientativo | **Oracle Live SQL** (https://livesql.oracle.com) | Navegador + cuenta Oracle free | Ideal para procedimientos, funciones y triggers (cuenta free típica **sin tarjeta**) |
| Diagramas ER / modelo | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Exportar PNG/SVG a la entrega |
| Diseño colaborativo rápido | **Excalidraw** (https://excalidraw.com) | Navegador | Bocetos de modelo / flujo |
| Documentación / entregas | **Google Docs / Drive** o Word Online | Navegador | Talleres en `.docx` en carpeta `Clases/` |
| Rompe-hielo / muro | **Padlet** del curso | Navegador | URL institucional del docente |

### Qué NO pediremos
- Instalar Oracle/MySQL/PostgreSQL/SQL Server en el PC del estudiante.
- Licencias de escritorio de pago (Toad, DataGrip de pago, etc.).
- Docker obligatorio en el equipo del estudiante.
- Cloud IaaS/PaaS con tarjeta (no aplica a este curso).

### Estado
- **Lista ajustada — pendiente OK docente para generar Clase N.**

## Evaluación teórica (Acuerdo 2026-2)

| Corte | % | Ventana | Parcial de cierre |
|---|---|---|---|
| 1 | 30% | 10/08 – 13/09/2026 | Parcial 1 en Clase 5 (07/09/2026) (10%) + Talleres/Quiz 10% + Asistencia 10% |
| 2 | 30% | 14/09 – 18/10/2026 | Parcial 2 en Clase 9 (05/10/2026) (10%) + Talleres/Quiz 10% + Asistencia 10% |
| 3 | 40% | 19/10 – 22/11/2026 | Parcial 3 en Clase 14 (09/11/2026) (15%) + Proyecto Integrador 20% + Asistencia 5% |

## Objeto / objetivo / RAA (microcurrículo)

- **Objeto:** Gestión avanzada y optimización de bases de datos relacionales.
- **Objetivo:** Diseñar, administrar y optimizar bases de datos relacionales avanzadas.
- **RAA1** Seguridad y respaldo · **RAA2** Procedimientos y disparadores · **RAA3** Optimización.
