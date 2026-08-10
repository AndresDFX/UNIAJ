# Guion docente — Clase 7: Redes y almacenamiento cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Modelar red lógica (cliente, edge, app, datos) sin VPC de pago.
- Elegir tipo de almacenamiento según el caso de uso CloudLite.
- Completar el diagrama de despliegue del PI.

## Hoy avanzamos el PI en…
**Diagrama de despliegue: red, zonas, almacenamiento**

**Entregable concreto:** Diagrama Deployment (draw.io) + elección de storage (objeto/bloque/relacional conceptual)

**Herramienta:** draw.io

## Fundamento teórico para el docente
El diagrama de despliegue (deployment) muestra DONDE corre cada pieza del sistema y como se conectan a traves de la red, distinguiendo zonas de confianza: una subred publica (expuesta a internet, ej. balanceador de carga) y una subred privada (solo accesible desde dentro, ej. base de datos) — sin necesidad de una VPC real de pago, el concepto se dibuja igual con draw.io.

Balanceo de carga y DNS en una frase cada uno: el DNS traduce un nombre humano (miapp.com) a una direccion de red; un balanceador de carga reparte las peticiones entrantes entre varias instancias del mismo servicio para que ninguna se sature sola.

Almacenamiento: Object storage (ej. tipo S3) guarda archivos/blobs con acceso via URL, ideal para imagenes o backups; storage de base de datos guarda registros estructurados con consultas complejas. La eleccion depende del tipo de dato: un PDF de factura va a object storage, el registro de la factura en si va a la base de datos.

Coherencia con Clase 4: los nombres de servicios en este diagrama de despliegue deben ser LOS MISMOS que los contenedores definidos en el C4 Containers — es el mismo sistema visto desde otro angulo, no un sistema nuevo.

Error de docente que no domina el tema: dibujar "la nube" como una sola caja difusa sin distinguir zona publica de zona privada — esa distincion es precisamente lo que demuestra que el equipo entiende superficie de exposicion, tema central de la clase de seguridad anterior.

Referencia de slides: `Clases/Clase 7 - Redes y almacenamiento cloud/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Diagrama de despliegue: red, zonas, almacenamiento**.
Entregable concreto: Diagrama Deployment (draw.io) + elección de storage (objeto/bloque/relacional conceptual).
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**draw.io**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 7/Capturas/`.
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
1. Dibujen Deployment en draw.io (zonas pública/privada/datos).
2. Etiqueten puertos y tipo de storage por componente.
3. Alineen nombres con el diagrama C4 de Clase 4.
4. Actualicen informe: sección Redes y almacenamiento.
5. Entrega domingo 23:59.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 7/Quiz Clase 7 - Redes y almacenamiento cloud.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase07.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). La UNIAJC no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
