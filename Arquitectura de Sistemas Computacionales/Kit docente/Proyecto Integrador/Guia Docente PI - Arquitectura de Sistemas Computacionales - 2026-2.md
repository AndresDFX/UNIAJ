# Guía docente — Proyecto Integrador · Arquitectura · 2026-2

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380 · 6303C)
- **Peso:** 20% Corte 3 (Acuerdo)
- **Dominio estudiante:** CloudLite App
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Arquitectura de Sistemas Computacionales - 2026-2.docx`

## Hitos (Plan 2026-2 · semestre acortado a 13 sesiones)

Las carpetas de material siguen numeradas 1–15; lo que cambia es en qué sesión se dicta cada una.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Foco | Cierre de entrega |
|---|---|---|---|---|
| S10 (doble) | 26/10/2026 | Clases 11 + 12 | Avance PI — diagramas v1 · Pruebas de rendimiento · **preparación de la sustentación** | dom 01/11/2026, 11:59 p. m. |
| S11 (autónoma) | 02/11/2026 | Clase 13 | Escalabilidad automática aplicada al PI | dom 08/11/2026, 11:59 p. m. |
| S12 | 09/11/2026 | Clase 14 | **Parcial 3** (virtual síncrono por Meet · solo evaluación) | **paquete final:** dom 15/11/2026, 11:59 p. m. |
| S13 | 16/11/2026 | Clase 15 | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre (sesión síncrona) | — (el paquete ya está entregado) |

> S13 cae en festivo (Independencia de Cartagena), pero por decisión docente es sesión de
> sustentaciones: no es autónoma y no es parcial. El paquete final se sube a ExamLab a más
> tardar el **domingo 15/11/2026, 11:59 p. m.**; el 16/11 solo se defiende.

## Entrega y sustentación

- **Plazo único:** domingo 15 de noviembre de 2026, 11:59 p. m., en ExamLab.
- **Un solo .zip** (máx. 50 MB) con esta forma —los estudiantes tienen la carpeta «Plantilla de entrega» ya armada—:

```
Equipo <nombre>.zip
├── Documento de arquitectura.docx  ← con las secciones de la plantilla
├── diagramas/  ← cada uno en PNG + su fuente (.drawio o .mmd)
│   ├── 1 componentes.png
│   ├── 2 despliegue.png
│   └── 3 ci-cd.png
├── app/  ← el servicio mínimo (stub)
├── contenedores/
│   ├── Dockerfile  ← o docker-compose.yml
│   └── capturas/  ← el lab corriendo, con la fecha visible
└── .github/
    └── workflows/
        └── ci.yml  ← construye y prueba app/
```

- **Qué debe traer cada pieza:**
  - **Documento de arquitectura.docx** — Las secciones de la plantilla: dominio y alcance (3 a 5 capacidades), modelo de servicio (IaaS, PaaS o SaaS, y por qué), decisiones, despliegue y contenedores, CI/CD, seguridad · monitoreo · costos · escalabilidad, y riesgos.
  - **diagramas/** — Los tres —componentes (C4), despliegue y flujo de CI/CD—, legibles y con los mismos nombres en los tres.
  - **app/** — El servicio mínimo que se contiene y que el workflow construye y prueba.
  - **contenedores/** — El Dockerfile (o el docker-compose.yml) y las capturas del lab (LabEx o Killercoda) donde se ve corriendo, con la fecha visible.
  - **.github/workflows/ci.yml** — Las etapas de construir y probar, que pasan; el despliegue puede ser simulado.
- **Enlace obligatorio:** el repositorio de GitHub donde está el workflow, o la carpeta de Drive del equipo si el workflow se entrega solo como archivo.
- **Proyecto en equipo de 4 a 5 integrantes (máximo 5)** — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** lunes 16/11/2026, en la última clase (es festivo, pero sí hay clase), por Meet: 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** el diagrama de despliegue, el contenedor corriendo en el lab (o sus capturas, si la sesión del lab caducó) y el workflow con sus etapas.

## Rúbrica (100 pts)

Dominio/servicio 15 · Diagramas 25 · Contenedores 20 · CI/CD 15 · Seg/costos/escala 10 · Informe+sustentación 15.

## Herramientas

draw.io · LabEx Docker Playground / Killercoda · GitHub Actions · **sin** AWS/GCP/Oracle Cloud con tarjeta.
