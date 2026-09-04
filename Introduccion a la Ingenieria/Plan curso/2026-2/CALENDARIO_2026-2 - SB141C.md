# Calendario 2026-2 — Introducción a la Ingeniería · Grupo SB141C

- **Código:** FI300101
- **Grupo:** SB141C
- **Periodo:** 2026-2 · **08/09/2026 – 17/11/2026**
- **Horario:** Martes **14:30 – 16:00** (90 min) · **inicio efectivo 14:40** (se arranca 10 min después de la hora oficial para esperar a que los estudiantes se conecten)
- **Modalidad:** Virtual (síncrona) por Google Meet · actividades en plataformas gratuitas en la nube
- **Docente:** Julian Andres Castaño · `julianacastano@profesores.uniajc.edu.co`
- **Total sesiones:** 11 · **temas del microcurrículo:** 16 — N:1 con 5 excepciones — 11 sesiones de calendario cubren los 16 temas del microcurrículo. La correspondencia por defecto es Sesión N = Clase N (Sesión 1 = Clase 1, Sesión 4 = Clase 6, Sesión 7 = Clase 11, etc.), y en 5 sesiones «dobles» se dictan DOS clases en el mismo bloque de 90 min (Sesión 2 = Clases 2+3, Sesión 3 = Clases 4+5, Sesión 5 = Clases 7+8, Sesión 6 = Clases 9+10, Sesión 11 = Clases 15+16). El mapeo exacto vive en `grupos[].sesiones[].clases_material`; las carpetas `Clases/Clase N - …` y `Kit docente/Clase N/` NO se renumeran — es el mismo patrón que ya usan los otros cuatro cursos (`semestre_2026_2.json`, campo `clases_material` + `sesion_doble`).
- **Semanas de calendario:** 11

> 11 semanas de calendario para 11 sesiones, cerrando antes de la semana institucional del 22/11/2026. Ningún festivo de 2026 cae en martes, así que no hay semana autónoma. Las sesiones 2, 3, 5, 6, 11 son dobles: cada una dicta dos Clases del microcurrículo en el mismo bloque de 90 min.

## Fechas de fin

**RESUELTO — el curso se comprimió a 11 sesiones para cerrar el 19-20/11.** El 2026-09-04 el docente confirmó que la última semana de clases es la del 20/11/2026, igual que los otros cuatro cursos del semestre (cierre institucional 22/11/2026). Con el inicio corrido una semana (08/09 martes, 10/09 jueves) solo caben 11 sesiones semanales antes de esa fecha, no las 16 que pedían los 16 temas del microcurrículo. Se aprobó fusionar 5 parejas de temas afines en un solo bloque de 90 min cada una (ver `mapa_sesion_tema` en `curso` y `clases_material`/`sesion_doble` en cada sesión), dejando los 16 temas cubiertos en 11 sesiones. El material de cada Clase (guion, taller, ExamLab) NO se reescribió: sigue completo por Clase, solo cambió cuándo se dicta.

> Ya aplicado: no queda plan B pendiente. Si el programa pidiera MÁS compresión todavía, la siguiente candidata sería fusionar Sesión 8+9 (Clases 12+13, avance y evaluación de impacto), que hoy quedaron sueltas a propósito para no recargar una sola sesión con tres bloques de proyecto seguidos.

## Dinámica de la sesión (90 min)

| Reloj | Duración | Bloque | Qué pasa |
|---|---|---|---|
| 14:30 – 14:40 | 10 min | Apertura | Se espera a que los estudiantes se conecten. No es tiempo muerto: en pantalla compartida queda la pregunta de entrada de la sesión y quien va entrando la responde en el muro del curso. Se pide cámara encendida solo durante el saludo y en la exposición del equipo. |
| 14:40 – 15:25 | 45 min | Teoría y guía del docente | Bloque teórico completo de la sesión, dictado con el guion docente y sus diapositivas por pantalla compartida. Las preguntas van por chat y se responden en voz alta. Cierra enunciando la consigna de la actividad y abriendo las salas de grupo. |
| 15:25 – 15:42 | 17 min | Actividad en equipos | Los 5 equipos pasan a sus salas de grupo de Meet y trabajan en paralelo sobre la misma consigna, cada uno en su documento en la nube. El docente entra y sale de las cinco salas (unos 3 min en cada una). A los 15 min se avisa por el chat general y se cierran las salas. |
| 15:42 – 15:57 | 15 min | Exposiciones | Vuelven todos a la sala principal y los 5 equipos exponen: 3 min por equipo, cronómetro proyectado, el vocero comparte pantalla con el documento YA abierto. No hay turno de preguntas por equipo; la retroalimentación va en el cierre. |
| 15:57 – 16:00 | 3 min | Cierre | Una idea que se llevan, el trabajo independiente de la semana y el tema de la siguiente sesión. Antes de salir, el enlace del documento de cada equipo queda pegado en el chat. |

**Equipos: 5, fijos.** El presupuesto de exposiciones es el que no se puede estirar: 5 equipos × 3 min = 15 min y la sesión cierra a los 90. Si se dejara fijo el tamaño del equipo (por ejemplo «de 4 en 4»), un grupo de 35 daría 9 equipos = 27 min de exposición y la sesión se pasaría 12 min. Por eso lo fijo son los 5 equipos y lo variable es cuánta gente hay en cada uno.

| Matriculados | Integrantes por equipo | Minutos de exposición |
|---|---|---|
| 20 | 4 | 5 equipos × 3 min = 15 min |
| 25 | 5 | 5 equipos × 3 min = 15 min |
| 30 | 6 | 5 equipos × 3 min = 15 min |
| 35 | 7 | 5 equipos × 3 min = 15 min |

> **Excepción:** Si un grupo tiene menos de 10 matriculados se baja a 4 equipos y los 3 min liberados se suman a la actividad. Es la única excepción prevista.
> **Rotación:** Los equipos son estables todo el semestre (el proyecto de ABPr es del equipo), pero el VOCERO rota en cada sesión y se anota en la bitácora del equipo: al final del semestre todos han expuesto y todos han compartido pantalla.

## Cortes (30% / 30% / 40%)

| Corte | % | Ventana | Sesiones | Cierre de corte | Desglose |
|---|---|---|---|---|---|
| Corte 1 | 30% | 08/09 – 29/09/2026 | 1-4 | Sesión 4 · 29/09/2026 | Evaluación de corte (sesión 4) · 10% · Exposiciones de equipo y actividades en clase · 12% · Asistencia y participación · 8% |
| Corte 2 | 30% | 06/10 – 20/10/2026 | 5-7 | Sesión 7 · 20/10/2026 | Evaluación de corte (sesión 7) · 10% · Exposiciones de equipo y actividades en clase · 12% · Asistencia y participación · 8% |
| Corte 3 | 40% | 27/10 – 17/11/2026 | 8-11 | Sesión 11 · 17/11/2026 | Exposición final del proyecto — Clase 15 (sesión 11) · 15% · Informe final del proyecto — Clase 16 (sesión 11) · 20% · Asistencia y participación · 5% |

> Los tres cierres de corte (sesiones 4, 7 y 11) NUNCA caen en festivo. En este calendario ninguno lo hace: los tres festivos de 2026 en el rango del curso (12/10, 02/11, 16/11) son lunes, y las 11 sesiones semanales son todas martes o jueves.

## Sesiones

> La columna **Clase de material** indica la carpeta `Clases/Clase N - …` y `Kit docente/Clase N/` que se usa. En este curso **Sesión N = Clase N**.

| Sesión | Fecha | Tipo | Clase de material | Tema | Trabajo independiente | Nota |
|---|---|---|---|---|---|---|
| 1 | 08/09/2026 | Virtual (síncrona) | Clase 1 | Presentación del curso y diagnóstico inicial | Revisión de la historia de la Ingeniería de Sistemas | — |
| 2 | 15/09/2026 | Virtual (síncrona) | Clase 2 y 3 | Historia y evolución de la Ingeniería + Fundamentos básicos de la Ingeniería de Sistemas | Elaboración de línea de tiempo + Ensayo sobre impacto social | sesión doble |
| 3 | 22/09/2026 | Virtual (síncrona) | Clase 4 y 5 | Principios éticos en la Ingeniería + El rol del ingeniero en el contexto ambiental | Análisis crítico del código ético + Informe sobre sostenibilidad | sesión doble |
| 4 | 29/09/2026 | Virtual (síncrona) | Clase 6 | Análisis de problemas tecnológicos del entorno | Propuesta inicial de solución | cierra Corte 1 (30%) |
| 5 | 06/10/2026 | Virtual (síncrona) | Clase 7 y 8 | Ciclo de vida de los proyectos de ingeniería + Taller de aplicación del ciclo de vida | Infografía explicativa + Ajuste de propuestas de solución | sesión doble |
| 6 | 13/10/2026 | Virtual (síncrona) | Clase 9 y 10 | Estrategias de innovación en Ingeniería + Herramientas digitales aplicadas a la Ingeniería | Propuesta de mejora + Práctica básica con herramientas digitales | sesión doble |
| 7 | 20/10/2026 | Virtual (síncrona) | Clase 11 | Taller de prototipado inicial con IA | Corrección del prototipo | cierra Corte 2 (30%) |
| 8 | 27/10/2026 | Virtual (síncrona) | Clase 12 | Presentación de avances de proyectos | Revisión entre pares | — |
| 9 | 03/11/2026 | Virtual (síncrona) | Clase 13 | Evaluación de impacto social y ambiental | Informe de evaluación del impacto | — |
| 10 | 10/11/2026 | Virtual (síncrona) | Clase 14 | Preparación de la presentación final | Ensayo general | — |
| 11 | 17/11/2026 | Virtual (síncrona) | Clase 15 y 16 | Exposición final de proyectos + Socialización y evaluación final del curso | Ajustes del informe final + Autoevaluación | sesión doble · cierra Corte 3 (40%) |

## Festivos Colombia 2026 (rango del periodo)

- 12/10/2026 — Día de la Diversidad Étnica y Cultural (lunes) — no cae en día de clase de este grupo
- 02/11/2026 — Todos los Santos (lunes) — no cae en día de clase de este grupo
- 16/11/2026 — Independencia de Cartagena (lunes) — no cae en día de clase de este grupo
- 08/12/2026 — Inmaculada Concepción (MARTES — fecha fija, no la mueve la Ley Emiliani) — no cae en día de clase de este grupo
- 25/12/2026 — Navidad (viernes) — no cae en día de clase de este grupo

> No se omite el festivo: si un festivo cayera en día de clase, la semana se marcaría como AUTÓNOMA con tarea concreta. En el calendario de 11 sesiones (08/09–19/11) ningún festivo de 2026 cae en martes ni en jueves, así que este curso no tiene ninguna semana autónoma.

## Pendiente

- Carpetas de Drive del curso (clases y grabadas) y su ID, una por grupo, para que MoverGrabaciones.gs archive las grabaciones de Meet como en los otros cuatro cursos. Al ser tres grupos hacen falta tres pares de carpetas.
- Enlace fijo de Google Meet de cada grupo (SB141B, SB141C, LB141F) y las cinco salas de grupo creadas de una vez para las 11 sesiones.

Fuente: `config/calendario/introduccion_ingenieria_2026_2.json` (generado por `config/slides/build_uniajc_intro_ing_curso.py`).
