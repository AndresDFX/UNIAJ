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
- **Un solo .zip** (cualquier tipo de archivo, máx. 50 MB) con:
  - **scripts/** — Los scripts SQL, numerados en el orden en que se ejecutan: el DDL (tablas, llaves y restricciones), los roles y privilegios, los procedimientos, funciones y disparadores con sus casos de prueba, y las consultas de optimización antes y después. Corren en PostgreSQL tal cual, sin retoques.
  - **Diagrama ER** — El modelo exportado en PNG o SVG: el mismo que implementa el DDL.
  - **Informe** — PDF o DOCX: el plan de respaldo y recuperación, la justificación de cada optimización y el contrato de integración app ↔ BD con su ejemplo.
  - **capturas/** — La ejecución de los scripts y de los casos de prueba, con la salida visible.
- **Enlace obligatorio:** el repositorio de GitHub o la carpeta de Drive del equipo, con los mismos scripts.
- **Proyecto en equipo de 4 a 5 integrantes (máximo 5)** — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** lunes 16/11/2026, en la última clase (sesión 13; es festivo, pero sí hay clase), por Meet: 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** ejecutar en vivo un procedimiento y un disparador con sus casos de prueba, y una consulta antes y después de optimizarla.

## Rúbrica (100 pts)

Modelo/DDL 20 · Seguridad/respaldo 15 · Programables 25 · Optimización 15 · Integración 10 · Informe+sustentación 15.
