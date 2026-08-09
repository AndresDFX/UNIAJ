# Guion docente — Clase 4: Microservicios · Arquitecturas distribuidas

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Contrastar monolito vs microservicios con criterios de equipo y acoplamiento.
- Modelar CloudLite en C4 Container/Componentes sin exceso de servicios.
- Definir 3 contratos/API entre partes del sistema.

## Hoy avanzamos el PI en…
**Diagramar componentes/servicios de CloudLite y sus contratos**

**Entregable concreto:** Diagrama C4 Container/Componentes v0.9 + lista de APIs entre servicios

**Herramienta:** draw.io / diagrams.net

## Fundamento teórico para el docente
Un microservicio es una unidad de despliegue independiente: se construye, se despliega y se escala por separado de los demas servicios, con su propia frontera de responsabilidad (ej. servicio de citas, servicio de notificaciones). La frontera correcta se define por responsabilidad de negocio, no por capricho tecnico.

Con equipos de 2-3 estudiantes, 2-5 contenedores logicos es un tamano realista para CloudLite (ej. API, base de datos, un servicio de notificaciones) — mas que eso se vuelve "microservicios teatro": servicios separados solo de nombre, sin razon de negocio real que justifique la separacion.

C4 Containers (nivel 2 del modelo visto en Clase 1) muestra que aplicaciones/servicios/bases de datos componen el sistema y COMO se comunican entre si (protocolo, formato de datos) — un contrato explicito, no flechas sin etiqueta.

Consecuencia inevitable de distribuir: lo que antes era una llamada de funcion local ahora es una llamada de red, que puede fallar, tardar, o llegar fuera de orden. Un sistema distribuido no es "el mismo sistema pero en varias partes" — introduce latencia real y fallos parciales (un servicio cae, los demas deben seguir funcionando o degradarse con gracia) que un monolito no tiene.

Error de docente que no domina el tema: aplaudir un diagrama con 8 microservicios sin preguntar por que cada uno existe — el numero de servicios no es una medida de calidad arquitectonica; la justificacion de cada frontera si lo es.

Referencia de slides: `Clases/Clase 4 - Microservicios y arquitecturas distribuidas/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Diagramar componentes/servicios de CloudLite y sus contratos**.
Entregable concreto: Diagrama C4 Container/Componentes v0.9 + lista de APIs entre servicios.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**draw.io / diagrams.net**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 4/Capturas/`.
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
1. Abran draw.io y creen diagrama Containers/Componentes de CloudLite.
2. Limiten a 2–5 servicios/contenedores lógicos justificados.
3. Listen 3 contratos (quién llama a quién, verbo HTTP o evento).
4. Exporten PNG + archivo .drawio al Drive/repo del PI.
5. En el informe: sección «Arquitectura lógica» + riesgos de distribución.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 4/Quiz Clase 4 - Microservicios y arquitecturas distribuidas.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase04.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
