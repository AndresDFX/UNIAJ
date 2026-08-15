# Propuesta de herramientas — Arquitectura de Sistemas Computacionales (2026-2)

Grupo: **6303C** · FI303380 · Docente: Julian Andres Castaño Espinosa  
PI: **CloudLite**

## Herramientas del curso (propuesta para aprobación docente)

> Criterio UNIAJC: **herramientas gratuitas + en la nube / navegador**. Los estudiantes **no deben instalar** hipervisores, IDEs pesados ni CLIs obligatorias en su PC. Free tier / cuenta educativa solo si **no exige tarjeta**.

| Uso en clase | Herramienta (gratis / free tier) | Acceso | Notas |
|---|---|---|---|
| Arquitectura / C4 / diagramas | **draw.io / diagrams.net** (https://app.diagrams.net) | Navegador | Componentes, despliegue, redes |
| Bocetos y talleres colaborativos | **Excalidraw** (https://excalidraw.com) | Navegador | Bajo roce, sin cuenta |
| Contenedores conceptuales (sin Docker local) | **LabEx Docker Playground** o **Killercoda** | Navegador | Labs temporales en la nube |
| Kubernetes intro (opcional) | **Killercoda** | Navegador | Solo demos guiadas |
| CI/CD conceptual | **GitHub Actions** (cuenta free) | Navegador | Pipelines simples; sin runner local |
| Documentación / entregas | **Google Docs / Drive** o Word Online | Navegador | Talleres en `.docx` en `Clases/` |
| Rompe-hielo / muro | **Padlet** del curso | Navegador | URL institucional del docente |
| Emulador cloud local (piloto) | **Floci** (`floci` / `floci-az` / `floci-gcp` / `floci-oci`) | Docker local **o** lab navegador | **En evaluación / piloto** — ver plan de viabilidad |
| Evaluación (parciales, actividades autónomas, PI) | **ExamLab** | Navegador | Plataforma de evaluación del curso. Distinto de Floci: acá se califica, Floci es el laboratorio — ver `PLAN_VIABILIDAD_EXAMLAB_2026-2.md` |

### Qué NO pediremos (salvo demo docente opcional)
- Instalar VirtualBox/VMware/Docker Desktop como **requisito único** del curso.
- Software de modelado de pago (Enterprise Architect, Visio de pago, etc.).
- Cuentas **AWS / GCP / Oracle Cloud / Azure** de free tier que exijan **tarjeta** (retiradas del plan).
- Consumo de cloud de pago (el estudiante no asume costos).

### Floci — estado
- **En evaluación / piloto** (no reescribe el semestre hasta OK docente).
- Plan: `PLAN_VIABILIDAD_FLOCI_2026-2.md`
- Script MVP: `scripts/lab-floci.ps1` · `scripts/lab-floci.sh` · `scripts/README.md`
- Idea: APIs cloud **sin cuenta ni tarjeta**; trade-off = necesita Docker (local o Killercoda/LabEx).
- Piloto sugerido: **Clase 7** (almacenamiento) con variante `floci` (AWS/S3).

### ExamLab — estado
- **Plan de viabilidad borrador**: `PLAN_VIABILIDAD_EXAMLAB_2026-2.md`.
- Diagramas (AWS/redes/UML) ya cubiertos con el catálogo existente de la pizarra.
- Gap conocido: sin tipo de pregunta "emparejamiento" nativo (workaround: `abierta` con pares).

### Estado general
- Stack navegador: **pendiente / en uso según material de clase**.
- Floci: **piloto pendiente de aprobación**.
- ExamLab: **plan de viabilidad en borrador, pendiente de aprobación**.
