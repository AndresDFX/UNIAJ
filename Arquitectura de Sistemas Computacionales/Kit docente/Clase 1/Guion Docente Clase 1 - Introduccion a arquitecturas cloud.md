# Guion docente — Clase 1: Introducción a arquitecturas cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Ubicar el curso como diseño de arquitecturas cloud al servicio del PI CloudLite App.
- Distinguir nube vs on-prem y los bloques de una arquitectura cloud simple.
- Dejar el dominio y alcance del PI escritos y compartibles.

## Hoy avanzamos el PI en…
**Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases**

**Entregable concreto:** Ficha PI: dominio, capacidades, actores y boceto C4 Context (Excalidraw/draw.io)

**Herramienta:** Padlet · Excalidraw / draw.io

## Fundamento teórico para el docente
Arquitectura de software = las decisiones estructurales dificiles de cambiar despues: como se dividen los componentes, como se comunican, donde se despliegan, y que atributos de calidad priorizan (rendimiento, seguridad, disponibilidad, costo). No es "el diagrama bonito": es el conjunto de decisiones que ese diagrama documenta.

El modelo C4 (Context, Containers, Components, Code) da niveles de zoom consistentes. Hoy se usa SOLO el nivel Context: un diagrama con el sistema como una caja, las personas que lo usan (actores) y los sistemas externos con los que se conecta (ej. pasarela de pagos, servicio de correo) — sin entrar todavia a que hay DENTRO del sistema (eso es Clase 4, nivel Containers).

El estudiante no necesita una cuenta cloud real de pago: CloudLite App se modela y simula con herramientas gratuitas (draw.io, Excalidraw, Play with Docker). La arquitectura se aprende razonando sobre decisiones y trade-offs, no memorizando la consola de un proveedor especifico.

Error de docente que no domina el tema: confundir "arquitectura" con "el stack tecnologico" (ej. "usamos React y Node, esa es la arquitectura") — el stack es una decision DENTRO de la arquitectura, no la arquitectura completa. Lo que se evalua hoy es si el diagrama Context responde con claridad quien usa el sistema y que toca hacia afuera.

Referencia de slides: `Clases/Clase 1 - Introduccion a arquitecturas cloud/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases**.
Entregable concreto: Ficha PI: dominio, capacidades, actores y boceto C4 Context (Excalidraw/draw.io).
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**Padlet · Excalidraw / draw.io**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 1/Capturas/`.
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
1. Formen equipo de 2–3 (o individual autorizado).
2. Elijan dominio concreto (no «red social genérica»).
3. Escriban: problema (2–3 frases), 3–5 capacidades, 2–3 actores.
4. En Excalidraw o draw.io: diagrama **C4 Context** (CloudLite + actores + sistemas externos).
5. Entrega en **ExamLab** (Talleres): Doc/enlace con ficha + PNG del diagrama (domingo 23:59).

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 1/Quiz Clase 1 - Introduccion a arquitecturas cloud.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase01.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
