# Guía docente — Proyecto Integrador · Arquitectura

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Peso:** el que fije el Acuerdo pedagógico del semestre
- **Dominio estudiante:** CloudLite App
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Arquitectura de Sistemas Computacionales.docx`

## Hitos (por clase del material)

Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance PI — diagramas v1 · Pruebas de rendimiento · **preparación de la sustentación** |
| Clase 13 | Escalabilidad automática aplicada al PI |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre |

## Entrega y sustentación

- **Plazo único:** el que publique el docente en ExamLab, el mismo para todos los grupos.
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
- **Proyecto en equipo** (el número de integrantes lo indica el docente cada semestre) — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** en la última clase del curso, 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** el diagrama de despliegue, el contenedor corriendo en el lab (o sus capturas, si la sesión del lab caducó) y el workflow con sus etapas.

## Rúbrica (100 pts)

Dominio/servicio 15 · Diagramas 25 · Contenedores 20 · CI/CD 15 · Seg/costos/escala 10 · Informe+sustentación 15.

## Herramientas

draw.io · LabEx Docker Playground / Killercoda · GitHub Actions · **sin** AWS/GCP/Oracle Cloud con tarjeta.
