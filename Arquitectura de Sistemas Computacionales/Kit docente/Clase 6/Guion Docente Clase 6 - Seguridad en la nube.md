# Guion docente — Clase 6: Seguridad en la nube

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Aplicar un modelo de amenazas simple al dominio CloudLite.
- Mapear controles (authn/z, secretos, superficie de red) sin cloud de pago.
- Dejar la sección Seguridad del informe lista en borrador.

## Hoy avanzamos el PI en…
**Modelo de amenazas mínimo + controles para CloudLite**

**Entregable concreto:** Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI

**Herramienta:** Excalidraw · Google Docs

## Fundamento teórico para el docente
Seguridad en la nube no es "poner un firewall": es identificar amenazas especificas del sistema y mapear cada una a un control verificable. STRIDE (metodologia de modelado de amenazas) da 6 categorias en una frase cada una: Spoofing (alguien se hace pasar por otro), Tampering (alguien modifica datos sin autorizacion), Repudiation (alguien niega haber hecho una accion sin evidencia que lo contradiga), Information disclosure (datos sensibles expuestos a quien no debe verlos), Denial of service (el sistema deja de responder), Elevation of privilege (alguien obtiene mas permisos de los que deberia tener).

Aplicado a CloudLite: por cada categoria relevante al dominio del equipo, se identifica una amenaza concreta (ej. Tampering: alguien modifica el precio de un producto via la API sin autorizacion) y un control que la mitiga (ej. autenticacion + validacion de rol antes de aceptar el cambio).

Gestion de secretos: una credencial (API key, contraseña de BD) NUNCA se escribe dentro de la imagen del contenedor ni se sube al repositorio en texto plano — eso queda expuesto a quien tenga acceso a la imagen o al historial de Git. Se usan mecanismos de secretos del propio pipeline (ej. GitHub Actions Secrets), inyectados en tiempo de ejecucion, nunca guardados en el codigo.

Error de docente que no domina el tema: tratar "seguridad" como una sola diapositiva generica de buenas practicas — el entregable de hoy exige amenaza especifica -> control especifico -> evidencia en el diagrama o repo, no una lista generica de consejos.

Referencia de slides: `Clases/Clase 6 - Seguridad en la nube/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Modelo de amenazas mínimo + controles para CloudLite**.
Entregable concreto: Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**Excalidraw · Google Docs**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 6/Capturas/`.
Di: «Copien la estructura, no el dominio de mi demo.»
📸 Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto) [[captura: salida-secreto-en-imagen.png]]


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
1. Listen 5 amenazas STRIDE-lite aplicadas a su dominio.
2. Para cada una: control + dónde se ve en el diagrama.
3. Definan política de secretos del repo/Actions.
4. Redacten sección Seguridad del informe PI (1–1.5 páginas).
5. Entrega domingo 23:59 (avance PI).

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase06.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). La UNIAJC no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
