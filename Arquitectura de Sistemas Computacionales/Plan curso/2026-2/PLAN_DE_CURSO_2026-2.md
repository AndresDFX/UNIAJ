# Plan de curso — Arquitectura de Sistemas Computacionales · 2026-2
> **CSV eventos:** `Plan curso/2026-2/calendario_eventos_2026-2.csv` (UTF-8 BOM). Importar en hoja/calendario cuando exista el listado de estudiantes (una fila = una sesión; filtrar `es_parcial=si` para parciales síncronos).

- **Código:** FI303380 · **Grupo:** **6303C**
- **Periodo:** **2026-2** · **24/08/2026 – 22/11/2026**
- **Horario:** **Lunes 10:00 – 12:00** (120 min)
- **Modalidad:** **Presencialidad asistida** (Sesión 1 y parciales presencial síncrono · resto virtual síncrona · festivos = clase autónoma)
- **Docente:** Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co`
- **Calendario:** `Plan curso/2026-2/CALENDARIO_2026-2.md` · `config/calendario/semestre_2026_2.json`

## Ajuste 2026-2: 13 sesiones para 15 temas

Semestre 2026-2 acortado: inicio **24/08/2026** (fin fijo **22/11/2026**) = **13 sesiones**. Se conservan los **15 temas** del microcurrículo: **2 sesiones son dobles** (dos temas afines en el mismo bloque de 120 min). El material existente (`Clases/Clase N - …`, `Kit docente/Clase N/`) **no se renumera**: cambia solo el mapeo Sesión → Clase(s) de material.

Sesiones dobles de este curso: **Sesión 7** (05/10/2026) = Clase 7 + Clase 8 · **Sesión 10** (26/10/2026) = Clase 11 + Clase 12.

**Arquitectura de Sistemas Computacionales** (Lunes 10:00 – 12:00) · Modalidad: Presencialidad asistida. Sesión 1 presencial (encuadre) · parciales en las sesiones **5/9/12**, presencial síncrono · resto de sesiones regulares virtual síncrona. Festivos = clase autónoma, no se omiten: Sesión 8 (12/10/2026, Día de la Diversidad Étnica y Cultural) · Sesión 11 (02/11/2026, Todos los Santos). Sesión 13 (16/11/2026) se dedica a las **sustentaciones del Proyecto Integrador** (no es parcial). Día de parcial = solo evaluación. Los parciales NUNCA se programan en festivo ni en clase autónoma. Sesión 0 = Presentación del Curso (no es sesión temática).

Parciales de este curso: Sesiones **5 / 9 / 12** (21/09/2026, 19/10/2026, 09/11/2026) — presencial síncrono.

> **Día de parcial = solo evaluación:** sin tema de trabajo dirigido nuevo.

> **Sesión 0 (no es sesión temática):** `Clases/Presentacion del Curso - ….pptx` (logística, acuerdo, Padlet, evaluación, CONTENIDO, socialización del Proyecto Integrador). En el **día 1** va Sesión 0 + Sesión 1 en el bloque de 120 min.

> **Sesión 13 (16/11/2026) = sustentaciones del Proyecto Integrador** (Cae en festivo (Independencia de Cartagena). Por decision docente esta sesion se usa para las sustentaciones del proyecto final; no es parcial.)

## Tabla Sesión · Fecha · Tipo · Clase(s) de material · Tema

| Sesión | Fecha | Tipo | Clase(s) de material | Tema (Trabajo dirigido) |
|---|---|---|---|---|
| 1 | 24/08/2026 | Presencial (síncrona) | Clase 1 | Introducción a arquitecturas cloud (+ diagnóstico) |
| 2 | 31/08/2026 | Virtual (síncrona) | Clase 2 | Modelos de servicio IaaS / PaaS / SaaS |
| 3 | 07/09/2026 | Virtual (síncrona) | Clase 3 | Virtualización y contenedores |
| 4 | 14/09/2026 | Virtual (síncrona) | Clase 4 | Microservicios y arquitecturas distribuidas |
| 5 | 21/09/2026 | Presencial (síncrona) | Clase 5 | **Parcial 1** (solo evaluación) |
| 6 | 28/09/2026 | Virtual (síncrona) | Clase 6 | Seguridad en la nube |
| 7 | 05/10/2026 | Virtual (síncrona) | Clase 7 + Clase 8 **(doble)** | Redes y almacenamiento cloud + Monitoreo, optimización y CI/CD |
| 8 | 12/10/2026 | Autónoma (festivo) | Clase 10 | Costos y sostenibilidad cloud |
| 9 | 19/10/2026 | Presencial (síncrona) | Clase 9 | **Parcial 2** (solo evaluación) |
| 10 | 26/10/2026 | Virtual (síncrona) | Clase 11 + Clase 12 **(doble)** | Avance del proyecto final + Pruebas de rendimiento y preparación final |
| 11 | 02/11/2026 | Autónoma (festivo) | Clase 13 | Escalabilidad automática |
| 12 | 09/11/2026 | Presencial (síncrona) | Clase 14 | **Parcial 3** (solo evaluación) |
| 13 | 16/11/2026 | Sustentación PI (festivo) | Clase 15 | Presentación del proyecto y cierre (sustentaciones PI) |

## Evaluación teórica (Acuerdo 2026-2)

| Corte | % | Ventana | Parcial de cierre |
|---|---|---|---|
| 1 | 30% | 24/08/2026 – 27/09/2026 | Parcial 1 en Sesión 5 (21/09/2026) · 10% Parcial 1 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia |
| 2 | 30% | 28/09/2026 – 25/10/2026 | Parcial 2 en Sesión 9 (19/10/2026) · 10% Parcial 2 (cierre de corte) · 10% Talleres y Quiz · 10% Asistencia |
| 3 | 40% | 26/10/2026 – 22/11/2026 | Parcial 3 en Sesión 12 (09/11/2026) · 15% Parcial 3 (cierre de corte) · 20% Proyecto Integrador · 5% Asistencia |

## Herramientas del curso (lista ajustada)

> Criterio UNIAJC: **herramientas gratuitas + en el navegador**, **sin tarjeta de crédito**. Los estudiantes **no deben instalar** hipervisores, IDEs pesados ni CLIs obligatorias en su PC. Se eliminaron AWS / GCP / Oracle Cloud Free Tier (y cualquier IaaS/PaaS que exija tarjeta).

| Uso en clase | Herramienta (gratis / navegador) | Acceso | Notas |
|---|---|---|---|
| Arquitectura / C4 / diagramas | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Componentes, despliegue, redes |
| Bocetos y talleres colaborativos | **Excalidraw** (https://excalidraw.com) | Navegador | Bajo roce, sin cuenta |
| Contenedores conceptuales (sin Docker local) | **LabEx Docker Playground** (https://labex.io, login con Google/Microsoft) o **Killercoda** (https://killercoda.com) | Navegador | Labs temporales en browser |
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

## Objeto / objetivo / RAA (microcurrículo)

- **Objeto:** Arquitecturas de sistemas computacionales en entornos cloud.
- **Objetivo:** Diseñar e implementar arquitecturas con cloud, virtualización y escalabilidad.
- **RAA1** IaaS/PaaS/SaaS · **RAA2** Virtualización y distribuidos · **RAA3** Seguridad, rendimiento y sostenibilidad.
