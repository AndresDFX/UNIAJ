# Plan de curso propuesto — Arquitectura de Sistemas Computacionales · 2026-2
> **CSV eventos:** `Plan curso/2026-2/calendario_eventos_2026-2.csv` (UTF-8 BOM). Importar en hoja/calendario cuando exista el listado de estudiantes (una fila = una clase; filtrar `es_parcial=si` para parciales síncronos).

- **Código:** FI303380
- **Grupo:** **6303C**
- **Periodo:** **2026-2** · 10/08/2026 – 22/11/2026
- **Horario:** **Lunes 10:00 – 12:00** (120 min)
- **Modalidad:** **Presencialidad asistida** (Clase 1 y parciales presencial síncrono · resto virtual síncrona · festivos = clase autónoma)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Fuente oficial:** Microcurrículo FI303380 (Enfoque Cloud) + Plan_de_curso FI303380
- **Calendario:** `Plan curso/2026-2/CALENDARIO_2026-2.md` · `.config/calendario/semestre_2026_2.json`
- **Listado de estudiantes:** `[PENDIENTE listado]`

## Ajuste 16 → 15 clases

El Plan oficial trae 16 sesiones. En 2026-2 hay **15 clases**: el cierre de la sesión 16 se integra en la **Clase 15**.

Criterio de modalidad por sesión (fijo 2026-2 · Arquitectura): oferta = Presencialidad asistida. Clase 1 = presencial; demás clases regulares = virtual (síncrona); parciales = siempre presenciales y síncronos; festivos = clase autónoma (sin parcial). Los parciales NUNCA se programan en día festivo ni en clase autónoma. Si el cierre teórico del corte cae en festivo/autónoma, el parcial se mueve a la última clase regular anterior del mismo corte; la clase autónoma de cierre queda como refuerzo sin parcial.

Parciales de este curso: Clases **5 / 9 / 14** (07/09/2026, 05/10/2026, 09/11/2026) — presencial síncrono.

> **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo. Si un tema técnico estaba mezclado con el parcial, se reasigna a la última clase regular anterior del mismo corte.

> **Sesión 0 (no es clase temática):** `Clases/Presentacion del Curso - ….pptx` (logística, acuerdo, Padlet, evaluación, CONTENIDO). En el **día 1** puede ir Sesión 0 + Clase 1 dentro del bloque de 120 min. Se mantienen **15 clases** temáticas (1–15).

## Tabla Clase · Fecha · Tipo · Tema

| Clase | Fecha | Tipo | Tema (Trabajo dirigido) |
|---|---|---|---|
| 1 | 10/08/2026 | Presencial | Diagnóstico · Introducción a arquitecturas cloud |
| 2 | 17/08/2026 | Autónoma (festivo) | Modelos de servicio: IaaS, PaaS, SaaS (Asunción de la Virgen) |
| 3 | 24/08/2026 | Virtual (síncrona) | Virtualización y contenedores |
| 4 | 31/08/2026 | Virtual (síncrona) | Microservicios · Arquitecturas distribuidas |
| 5 | 07/09/2026 | Presencial (síncrona) | **Parcial 1** |
| 6 | 14/09/2026 | Virtual (síncrona) | Seguridad en la nube |
| 7 | 21/09/2026 | Virtual (síncrona) | Redes y almacenamiento cloud |
| 8 | 28/09/2026 | Virtual (síncrona) | Monitoreo y optimización · Integración continua y despliegue (CI/CD) |
| 9 | 05/10/2026 | Presencial (síncrona) | **Parcial 2** |
| 10 | 12/10/2026 | Autónoma (festivo) | Costos y sostenibilidad cloud · refuerzo sin parcial |
| 11 | 19/10/2026 | Virtual (síncrona) | Avance del proyecto final |
| 12 | 26/10/2026 | Virtual (síncrona) | Pruebas de rendimiento · Preparación de presentación final |
| 13 | 02/11/2026 | Autónoma (festivo) | Escalabilidad automática (Todos los Santos) |
| 14 | 09/11/2026 | Presencial (síncrona) | **Parcial 3** |
| 15 | 16/11/2026 | Autónoma (festivo) | Presentación del proyecto + cierre · refuerzo sin parcial |

## Herramientas del curso (lista ajustada)

> Criterio UNIAJC: **herramientas gratuitas + en el navegador**, **sin tarjeta de crédito**. Los estudiantes **no deben instalar** hipervisores, IDEs pesados ni CLIs obligatorias en su PC. Se eliminaron AWS / GCP / Oracle Cloud Free Tier (y cualquier IaaS/PaaS que exija tarjeta).

| Uso en clase | Herramienta (gratis / navegador) | Acceso | Notas |
|---|---|---|---|
| Arquitectura / C4 / diagramas | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Componentes, despliegue, redes |
| Bocetos y talleres colaborativos | **Excalidraw** (https://excalidraw.com) | Navegador | Bajo roce, sin cuenta |
| Contenedores conceptuales (sin Docker local) | **Play with Docker** (https://labs.play-with-docker.com) o **Killercoda** (https://killercoda.com) | Navegador | Labs temporales en browser |
| Kubernetes intro (opcional) | **Killercoda** (labs gratuitos) | Navegador | Solo demos guiadas |
| CI/CD conceptual (opcional) | **GitHub Actions** (cuenta free) + repo free | Navegador | Pipelines simples; sin runner local; sin tarjeta para demos básicas |
| Documentación / entregas | **Google Docs / Drive** o Word Online | Navegador | Talleres en `.docx` en `Clases/` |
| Rompe-hielo / muro | **Padlet** del curso | Navegador | URL institucional del docente |

### Qué NO pediremos
- Cloud IaaS/PaaS que exija **tarjeta** (AWS Free Tier, GCP Free Tier, Oracle Cloud Free Tier, Azure, etc.).
- Instalar VirtualBox/VMware/Docker Desktop/WSL como requisito del curso.
- Software de modelado de pago (Enterprise Architect, Visio de pago, etc.).
- Costos de cloud de pago (el estudiante no asume costos).

### Estado
- **Lista ajustada — pendiente OK docente para generar Clase N.**

## Evaluación teórica (Acuerdo 2026-2)

| Corte | % | Ventana | Parcial de cierre |
|---|---|---|---|
| 1 | 30% | 10/08 – 13/09/2026 | Parcial 1 en Clase 5 (07/09/2026) (10%) + Talleres/Quiz 10% + Asistencia 10% |
| 2 | 30% | 14/09 – 18/10/2026 | Parcial 2 en Clase 9 (05/10/2026) (10%) + Talleres/Quiz 10% + Asistencia 10% |
| 3 | 40% | 19/10 – 22/11/2026 | Parcial 3 en Clase 14 (09/11/2026) (15%) + Proyecto Integrador 20% + Asistencia 5% |

## Objeto / objetivo / RAA (microcurrículo)

- **Objeto:** Arquitecturas de sistemas computacionales en entornos cloud.
- **Objetivo:** Diseñar e implementar arquitecturas con cloud, virtualización y escalabilidad.
- **RAA1** IaaS/PaaS/SaaS · **RAA2** Virtualización y distribuidos · **RAA3** Seguridad, rendimiento y sostenibilidad.
