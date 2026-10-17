# Guía docente — Proyecto Integrador · Bases de Datos II

**Privado docente** · No compartir en `Clases/`.

- **Curso:** Bases de Datos II (FI303215)
- **Peso:** el que fije el Acuerdo pedagógico del semestre
- **Dominio estudiante:** VetCare DB
- **Enunciado:** `Clases/Proyecto Integrador/Enunciado Proyecto Integrador - Bases de Datos II.docx`

## Hitos (por clase del material)

Sin sesiones ni fechas: cambian cada semestre y están en el calendario (`config/calendario/`).

| Material | Foco |
|---|---|
| Clases 11 + 12 | Avance PI — checklist · Integración app ↔ BD · **preparación de la sustentación** |
| Clase 13 | Análisis de casos reales aplicado al PI |
| Antes de la última clase | **Paquete final** en ExamLab, en la fecha y la hora que publique el docente |
| Clase 15 (la última) | **Sustentación en vivo del PI** (15 min + 5 de preguntas, turno de 20) + cierre |

## Entrega y sustentación

- **Plazo único:** el que publique el docente en ExamLab, el mismo para todos los grupos.
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
- **Proyecto en equipo** (el número de integrantes lo indica el docente cada semestre) — solo el proyecto: los demás entregables conservan su modalidad. **Cada integrante sube la entrega del equipo** desde su propia cuenta: el mismo .zip y el mismo enlace; una sola entrega por estudiante.
- **Sustentación:** en la última clase del curso, 15 minutos de exposición + 5 minutos de preguntas por equipo (turno de 20 minutos); hablan todos los integrantes.
- **Qué muestran:** ejecutar en vivo un procedimiento y un disparador con sus casos de prueba, y una consulta antes y después de optimizarla.

## Rúbrica (100 pts)

Modelo/DDL 20 · Seguridad/respaldo 15 · Programables 25 · Optimización 15 · Integración 10 · Informe+sustentación 15.
