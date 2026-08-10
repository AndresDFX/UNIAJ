# Guion docente — Clase 11: Avance del proyecto final

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Consolidar evidencias PI en un paquete revisable.
- Detectar huecos (nombres inconsistentes, servicios de más, sin seguridad).
- Salir con backlog claro hacia Clase 12/15.

## Hoy avanzamos el PI en…
**Integrar diagramas v1 + checklist de avance PI**

**Entregable concreto:** Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+

**Herramienta:** draw.io · GitHub · Google Docs

## Fundamento teórico para el docente
Esta clase no introduce teoria nueva a proposito: es un checkpoint donde el equipo demuestra que las piezas ya vistas (C4 Context/Containers, seguridad, despliegue, CI) forman un sistema coherente, no fragmentos sueltos de distintas clases.

El rol del docente hoy es de auditor critico, no de instructor: bloquear dominios que crecieron sin limite desde la Clase 1 original (scope creep), y senalar "microservicios teatro" — servicios separados en el diagrama que en la practica no tienen frontera de responsabilidad real ni justificacion de por que estan separados.

Diferencia importante que evita confusion: esto NO es la sustentacion final (Clase 15) ni el Parcial 3 (Clase 14evaluacion escrita) — es un punto de control intermedio para corregir rumbo a tiempo, con retroalimentacion entre pares ademas de la del docente.

Error de docente que no domina el tema: dejar pasar un checkpoint sin retroalimentacion especifica por equipo ("todo bien, sigan asi") — el valor de un checkpoint es identificar el gap concreto que cada equipo debe cerrar antes de la sustentacion.

Referencia de slides: `Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Integrar diagramas v1 + checklist de avance PI**.
Entregable concreto: Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**draw.io · GitHub · Google Docs**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 11/Capturas/`.
Di: «Copien la estructura, no el dominio de mi demo.»


### 55–100 · Taller guiado PI (equipos)
Proyecta la lista de pasos del taller estudiante.
Recorre mesas/Meet: bloquea dominios vagos; exige nombres consistentes.
A los 80 min: «Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Quiz / evidencias
Aplica quiz corto (Kit). Mientras, revisa que el entregable esté en Drive/repo.
Retroalimenta 2–3 equipos en voz alta (errores frecuentes).

### 115–120 · Cierre
Di: «Criterio de éxito: cualquier integrante explica el artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Completen el checklist en el informe (sí/no + enlace evidencia).
2. Unifiquen nombres entre C4 y Deployment.
3. Empaqueten ZIP/repo: diagramas PNG, Dockerfile, YAML, informe.
4. Feedback docente 1:1 corto (cola).
5. Backlog escrito: 5 ítems para Clase 12.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 11/Quiz Clase 11 - Avance del proyecto final.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase11.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). La UNIAJC no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
