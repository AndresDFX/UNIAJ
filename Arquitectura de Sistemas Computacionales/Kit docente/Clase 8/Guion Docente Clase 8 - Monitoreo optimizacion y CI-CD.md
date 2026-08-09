# Guion docente — Clase 8: Monitoreo y optimización · CI/CD

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Explicar pipeline CI vs CD y qué es realista sin cloud de pago.
- Crear un workflow Actions que construya/pruebe un stub.
- Definir 4–6 señales de monitoreo para CloudLite.

## Hoy avanzamos el PI en…
**Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**

**Entregable concreto:** .github/workflows/ci.yml + sección Monitoreo/CI del informe

**Herramienta:** GitHub Actions · Google Docs

## Fundamento teórico para el docente
CI (Integracion Continua) automatiza la VALIDACION del codigo cada vez que alguien sube un cambio: correr pruebas, verificar que compila/construye, revisar estilo — sin que un humano lo haga manualmente cada vez. CD (Entrega/Despliegue Continuo) automatiza el PASO SIGUIENTE, llevar ese cambio validado a produccion; en este curso, sin infraestructura real de pago, CD se SIMULA (el pipeline llega hasta "listo para desplegar", no despliega a un servidor real).

Un archivo YAML de GitHub Actions es evidencia real y verificable de CI: define triggers (cuando correr, ej. en cada push), jobs (que tareas ejecutar) y steps (comandos concretos). Aunque sea minimo (ej. solo correr un linter), es un pipeline real, no una simulacion en papel.

Monitoreo con golden signals (los 4 indicadores clasicos de observabilidad): latencia (cuanto tarda en responder), errores (que porcentaje de peticiones falla), saturacion (que tan cerca esta el sistema de su limite de capacidad), trafico (cuantas peticiones recibe). Aplicados a CloudLite de forma conceptual: aunque no haya trafico real, se documenta QUE se mediria y COMO se detectaria un problema con cada señal.

Error de docente que no domina el tema: presentar CI/CD como sinonimos intercambiables — CI valida, CD despliega; un pipeline puede tener CI sin CD (validar sin desplegar automaticamente), y eso es exactamente lo que se construye hoy.

Referencia de slides: `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**.
Entregable concreto: .github/workflows/ci.yml + sección Monitoreo/CI del informe.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**GitHub Actions · Google Docs**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 8/Capturas/`.
Di: «Copien la estructura, no el dominio de mi demo.»
📸 Run verde del workflow: build + test reales, no un `echo ok` [[captura: salida-actions-run.png]]


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
1. Creen repo free (o usen el del equipo) con stub mínimo.
2. Agreguen `.github/workflows/ci.yml` (build/test + deploy simulado).
3. Listen 4–6 métricas/logs a observar en producción hipotética.
4. Peguen captura del run verde (o YAML + explicación si Actions falla por cuota).
5. Actualicen informe secciones CI/CD y Monitoreo.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase08.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
