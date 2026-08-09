# Guion docente — Clase 3: Virtualización y contenedores

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Diferenciar VM vs contenedor y el rol de la imagen.
- Ejecutar un contenedor en lab de navegador (sin Docker Desktop obligatorio).
- Dejar evidencia PI: Dockerfile del stub CloudLite + captura.

## Hoy avanzamos el PI en…
**Contenerizar un stub del servicio principal de CloudLite**

**Entregable concreto:** Dockerfile (+ compose opcional) + captura/enlace lab navegador

**Herramienta:** Play with Docker (PWD) · alterna si no carga: Killercoda

## Fundamento teórico para el docente
Virtualizacion (maquinas virtuales): un hipervisor crea varias maquinas virtuales sobre un mismo hardware fisico, y cada VM tiene su PROPIO sistema operativo completo (kernel incluido), aislado de las demas. Es aislamiento fuerte, pero cada VM carga el peso completo de un SO.

Contenedores: en cambio, todos los contenedores de una maquina COMPARTEN el kernel del sistema operativo anfitrion; cada contenedor solo empaqueta la aplicacion y sus dependencias (librerias, configuracion), no un SO completo. Por eso arrancan en segundos (no minutos) y pesan megabytes (no gigabytes) comparado con una VM.

Distincion clave que se confunde seguido: una IMAGEN es la plantilla inmutable (el "molde": codigo + dependencias + configuracion); un CONTENEDOR es una instancia en ejecucion de esa imagen (el "objeto" corriendo). De una misma imagen se pueden lanzar muchos contenedores identicos.

Para evitar depender de Docker Desktop (que requiere licencia/recursos en equipos institucionales), se usa Play with Docker (labs.play-with-docker.com, sesiones de 4h) como lab principal en el navegador — da una terminal Linux real con Docker instalado, sin instalar nada localmente. Killercoda queda como alterna si PWD no esta disponible.

Error de docente que no domina el tema: decir que un contenedor "es una VM ligera" sin mas — la diferencia arquitectonica real es el aislamiento (kernel propio vs kernel compartido), no solo el tamano.

Referencia de slides: `Clases/Clase 3 - Virtualizacion y contenedores/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Contenerizar un stub del servicio principal de CloudLite**.
Entregable concreto: Dockerfile (+ compose opcional) + captura/enlace lab navegador.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**Play with Docker (PWD) · alterna si no carga: Killercoda**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase 3/Capturas/`.
Di: «Copien la estructura, no el dominio de mi demo.»
📸 Build y run del stub en Play with Docker (lo que debe verse en pantalla) [[captura: salida-docker-build-run.png]]
📸 Evidencia del entregable: el contenedor corriendo (`docker ps`) [[captura: salida-docker-ps.png]]


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
1. Definan qué servicio contenerizan hoy (API stub o front estático del dominio).
2. En Play with Docker: construyan y corran el contenedor (si no carga, Killercoda como alterna).
3. Documenten Dockerfile (y compose si aplica) en el repo/ZIP del PI.
4. Capturen evidencia (PNG) o enlace de sesión + nota de caducidad.
5. Actualicen informe: sección Contenedores + enlace a diagrama de despliegue futuro.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase 3/Quiz Clase 3 - Virtualizacion y contenedores.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase03.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
