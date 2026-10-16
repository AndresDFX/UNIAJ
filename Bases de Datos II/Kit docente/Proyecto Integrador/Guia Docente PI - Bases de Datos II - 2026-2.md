# Guía docente — Proyecto Integrador · Bases de Datos II · 2026-2

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Bases de Datos II (FI303215 · 641A-2)
- **Peso:** 20% Corte 3 (Acuerdo)
- **Dominio estudiante:** VetCare DB
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Bases de Datos II - 2026-2.docx`

## Hitos (Plan 2026-2 · semestre acortado a 13 sesiones)

Las carpetas de material siguen numeradas 1–15; lo que cambia es en qué sesión se dicta cada una.
Toda entrega intermedia cierra el **domingo siguiente a la sesión, a las 11:59 p. m.**

| Sesión | Fecha | Material | Foco | Cierre de entrega |
|---|---|---|---|---|
| S10 (doble) | 26/10/2026 | Clases 11 + 12 | Avance PI — checklist · Integración app ↔ BD · **preparación de la sustentación** | dom 01/11/2026, 11:59 p. m. |
| S11 (autónoma) | 02/11/2026 | Clase 13 | Análisis de casos reales aplicado al PI | dom 08/11/2026, 11:59 p. m. |
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
├── Informe.docx  ← el informe, con las secciones de la plantilla
├── diagrama/
│   └── Diagrama ER.png  ← el modelo: el mismo que crea el DDL
├── scripts/  ← corren en PostgreSQL tal cual, en orden
│   ├── 01_ddl.sql  ← tablas, llaves y restricciones
│   ├── 02_roles_y_privilegios.sql  ← roles, GRANT y REVOKE
│   ├── 03_programables.sql  ← procedimientos, funciones, disparadores y pruebas
│   └── 04_optimizacion.sql  ← consultas antes y después
└── capturas/  ← la salida de cada script y de cada prueba
```

- **Qué debe traer cada pieza:**
  - **Informe.docx** — Las secciones de la plantilla: portada con integrantes, modelo, seguridad y respaldo (con el plan de respaldo y recuperación), objetos programables, optimización, integración app ↔ BD y cómo correr los scripts.
  - **Diagrama ER.png** — Las entidades del caso Huellitas (ver el anexo), con sus llaves y cardinalidades. Coincide con el DDL.
  - **01_ddl.sql** — Todas las tablas, con llaves primarias y foráneas y las restricciones de las reglas del negocio.
  - **02_roles_y_privilegios.sql** — Al menos 2 roles con privilegios distintos.
  - **03_programables.sql** — Al menos 2 procedimientos, 1 función y 2 disparadores, cada uno con su caso de prueba.
  - **04_optimizacion.sql** — Al menos 2 consultas con su EXPLAIN antes y después, y el índice o la reescritura que las mejora.
  - **capturas/** — La salida de cada script y de cada caso de prueba.
- **Enlace obligatorio:** el repositorio de GitHub o la carpeta de Drive del equipo, con los mismos archivos.
- **Proyecto en equipo de 4 a 5 integrantes (máximo 5)** — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** lunes 16/11/2026, en la última clase (es festivo, pero sí hay clase), por Meet: 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** ejecutar en vivo un procedimiento y un disparador con sus casos de prueba, y una consulta antes y después de optimizarla.

## Rúbrica (100 pts)

Modelo/DDL 20 · Seguridad/respaldo 15 · Programables 25 · Optimización 15 · Integración 10 · Informe+sustentación 15.
