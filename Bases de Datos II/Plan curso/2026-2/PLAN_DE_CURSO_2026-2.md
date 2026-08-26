# Plan de curso — Bases de Datos II · 2026-2
> **CSV eventos:** `Plan curso/2026-2/calendario_eventos_2026-2.csv` (UTF-8 BOM). Importar en hoja/calendario cuando exista el listado de estudiantes (una fila = una sesión; filtrar `es_parcial=si` para parciales síncronos).

- **Código:** FI303215 · **Grupo:** **641A-2**
- **Periodo:** **2026-2** · **24/08/2026 – 22/11/2026**
- **Horario:** **Lunes 18:00 – 20:00** (120 min)
- **Modalidad:** Virtual (todas las sesiones por Meet, incluidos los parciales · festivos = clase autónoma)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Calendario:** `Plan curso/2026-2/CALENDARIO_2026-2.md` · `config/calendario/semestre_2026_2.json`

## Ajuste 2026-2: 13 sesiones para 15 temas

Semestre 2026-2 acortado: inicio **24/08/2026** (fin fijo **22/11/2026**) = **13 sesiones**. Se conservan los **15 temas** del microcurrículo: **2 sesiones son dobles** (dos temas afines en el mismo bloque de 120 min). El material existente (`Clases/Clase N - …`, `Kit docente/Clase N/`) **no se renumera**: cambia solo el mapeo Sesión → Clase(s) de material.

Sesiones dobles de este curso: **Sesión 7** (05/10/2026) = Clase 7 + Clase 8 · **Sesión 10** (26/10/2026) = Clase 11 + Clase 12.

**Bases de Datos II** (Lunes 18:00 – 20:00) · Modalidad: Virtual. Todas las sesiones son **virtual síncrona** por Google Meet, incluidos la Sesión 1 y los parciales (sesiones **5/9/12**). No hay sesiones presenciales. Festivos = clase autónoma, no se omiten: Sesión 8 (12/10/2026, Día de la Diversidad Étnica y Cultural) · Sesión 11 (02/11/2026, Todos los Santos). Sesión 13 (16/11/2026) se dedica a las **sustentaciones del Proyecto Integrador** (no es parcial). Día de parcial = solo evaluación. Los parciales NUNCA se programan en festivo ni en clase autónoma. Sesión 0 = Presentación del Curso (no es sesión temática).

Parciales de este curso: Sesiones **5 / 9 / 12** (21/09/2026, 19/10/2026, 09/11/2026) — virtual síncrono.

> **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo.

> **Sesión 0 (no es sesión temática):** `Clases/Presentacion del Curso - ….pptx` (logística, acuerdo, Padlet, evaluación, CONTENIDO, socialización del Proyecto Integrador). En el **día 1** va Sesión 0 + Sesión 1 en el bloque de 120 min.

> **Sesión 13 (16/11/2026) = sustentaciones del Proyecto Integrador** (Cae en festivo (Independencia de Cartagena). Por decision docente esta sesion se usa para las sustentaciones del proyecto final; no es parcial.)

## Tabla Sesión · Fecha · Tipo · Clase(s) de material · Tema

| Sesión | Fecha | Tipo | Clase(s) de material | Tema (Trabajo dirigido) |
|---|---|---|---|---|
| 1 | 24/08/2026 | Virtual (síncrona) | Clase 1 | Diagnóstico · Revisión de Bases de Datos I (VetCare) |
| 2 | 31/08/2026 | Virtual (síncrona) | Clase 2 | Administración de bases de datos |
| 3 | 07/09/2026 | Virtual (síncrona) | Clase 3 | Procedimientos almacenados |
| 4 | 14/09/2026 | Virtual (síncrona) | Clase 4 | Funciones y disparadores · Seguridad y respaldo |
| 5 | 21/09/2026 | Virtual (síncrona) | Clase 5 | **Parcial 1** (solo evaluación) |
| 6 | 28/09/2026 | Virtual (síncrona) | Clase 6 | Optimización de consultas |
| 7 | 05/10/2026 | Virtual (síncrona) | Clase 7 + Clase 8 **(doble)** | Índices y particionamiento + Tuning y gestión de transacciones |
| 8 | 12/10/2026 | Autónoma (festivo) | Clase 10 | Control de concurrencia |
| 9 | 19/10/2026 | Virtual (síncrona) | Clase 9 | **Parcial 2** (solo evaluación) |
| 10 | 26/10/2026 | Virtual (síncrona) | Clase 11 + Clase 12 **(doble)** | Avance del proyecto final + Integración de apps externas y preparación final |
| 11 | 02/11/2026 | Autónoma (festivo) | Clase 13 | Análisis de casos reales |
| 12 | 09/11/2026 | Virtual (síncrona) | Clase 14 | **Parcial 3** (solo evaluación) |
| 13 | 16/11/2026 | Sustentación PI (festivo) | Clase 15 | Presentación del proyecto y cierre (sustentaciones PI) |

## Evaluación teórica (Acuerdo 2026-2)

| Corte | % | Ventana | Parcial de cierre |
|---|---|---|---|
| 1 | 30% | 24/08/2026 – 27/09/2026 | Parcial 1 en Sesión 5 (21/09/2026) · 10% Parcial 1 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia |
| 2 | 30% | 28/09/2026 – 25/10/2026 | Parcial 2 en Sesión 9 (19/10/2026) · 10% Parcial 2 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia |
| 3 | 40% | 26/10/2026 – 22/11/2026 | Parcial 3 en Sesión 12 (09/11/2026) · 15% Parcial 3 (cierre de corte) · 20% Proyecto Integrador · 5% Asistencia |

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

## Objeto / objetivo / RAA (microcurrículo)

- **Objeto:** Gestión avanzada y optimización de bases de datos relacionales.
- **Objetivo:** Diseñar, administrar y optimizar bases de datos relacionales avanzadas.
- **RAA1** Seguridad y respaldo · **RAA2** Procedimientos y disparadores · **RAA3** Optimización.
