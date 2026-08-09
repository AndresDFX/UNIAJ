# Guion docente — Clase 12: Pruebas de rendimiento · Preparación de presentación final

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Definir métricas/objetivos de rendimiento realistas para CloudLite.
- Diseñar un escenario de prueba (aunque sea cualitativo/simulado).
- Ensayar el pitch de sustentación (prep PI; Parcial 3 es otro día).

## Hoy avanzamos el PI en…
**Escenario de rendimiento + ensayo 5–8 min de sustentación**

**Entregable concreto:** Sección Rendimiento + guion de pitch + paquete casi-final

**Herramienta:** Google Docs · draw.io · (opcional) lab contenedor

## Fundamento teórico para el docente
Rendimiento en arquitectura se analiza con tres piezas: objetivo medible (ej. "p95 de tiempo de respuesta menor a 300ms" — el percentil 95 indica que el 95% de las peticiones responden en ese tiempo o menos, una medida mas honesta que el promedio porque no la distorsionan casos extremos), escenario de carga (cuantas peticiones por segundo, RPS, se simulan) y bottleneck (el componente especifico que limita el rendimiento del sistema completo — nunca "todo es lento", siempre hay una pieza que limita primero).

Diferencia entre stress test (aumentar la carga progresivamente hasta encontrar el punto de quiebre del sistema) y spike test (una subida SUBITA y grande de trafico, simulando un pico real como una promocion o una noticia viral) — evaluan cosas distintas: capacidad maxima vs capacidad de reaccion ante lo inesperado.

El pitch de 5-8 minutos se ensaya HOY como preparacion, distinto del Parcial 3 (Clase 14) que es la evaluacion escrita formal — no deben confundirse ni mezclar contenido de uno con el otro en esta clase.

Error de docente que no domina el tema: pedir "que la app sea rapida" sin definir p95, RPS objetivo ni el bottleneck sospechado — sin esas tres piezas, "rendimiento" es una palabra vacia, no un analisis.

Referencia de slides: `Clases/Clase 12 - Pruebas de rendimiento y preparacion final/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Escenario de rendimiento + ensayo 5–8 min de sustentación**.
Entregable concreto: Sección Rendimiento + guion de pitch + paquete casi-final.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**Google Docs · draw.io · (opcional) lab contenedor**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 12/Capturas/`.
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
1. Escriban escenario de carga + 3 métricas objetivo + bottleneck esperado.
2. Ensayen pitch 5–8 min (cronómetro); feedback entre equipos.
3. Cierren backlog de Clase 11.
4. Dejen paquete casi-final en Drive/repo.
5. Entrega de avance domingo 23:59.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 12/Quiz Clase 12 - Pruebas de rendimiento y preparacion final.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase12.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
