# Guion docente — Clase 3: Virtualización y contenedores

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Diferenciar VM vs contenedor y el rol de la imagen.
- Ejecutar un contenedor en lab de navegador (sin Docker Desktop obligatorio).
- Publicar el puerto y verificar el servicio con un endpoint de salud (ruta, código, cuerpo).
- Dejar evidencia PI: Dockerfile del stub CloudLite + bitácora + captura.

## Hoy avanzamos el PI en…
**Contenerizar un stub del servicio principal de CloudLite**

**Entregable concreto:** Dockerfile del stub + bitácora de 5 comandos con la salida real + captura del lab

**Herramienta:** Killercoda · alterna si no carga: LabEx Docker Playground

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 8] De donde viene la clase y que se entrega hoy** — 4 vinetas.
  - Conviene decir desde el minuto uno por que esto importa para la arquitectura y no solo para la operacion: el contenedor es la unidad de despliegue con la que se razona en todos los diagramas siguientes, y sin entender que es exactamente, el nivel de contenedores del modelo C4 que se dibuja en la Clase 4 queda en pura metafora.

**[Slide 9] Antes de la virtualizacion: un servidor por aplicacion** — 5 vinetas.
  - Los ordenes de magnitud que el docente debe poder citar: una maquina virtual ocupa varios gigabytes en disco y tarda entre 30 segundos y unos minutos en arrancar, porque debe iniciar un sistema operativo completo.

**[Slide 10] Recorrer el diagrama de las dos pilas, de abajo hacia arriba** — 5 vinetas.
  - Conviene cerrar con lo que el dibujo NO muestra y la seccion anterior si dijo: en la nube las dos pilas se apilan, con los contenedores corriendo DENTRO de maquinas virtuales.

**[Slide 11] El contenedor: aislamiento sin otro sistema operativo (1/2)** — 5 vinetas.

**[Slide 12] El contenedor: aislamiento sin otro sistema operativo (2/2)** — 5 vinetas.

**[Slide 13] Dockerfile, imagen, contenedor y registro: los cuatro terminos (1/2)** — 6 vinetas.

**[Slide 14] Dockerfile, imagen, contenedor y registro: los cuatro terminos (2/2)** — 3 vinetas.

**[Slide 15] Primer ejemplo: el stub de la API de CloudLite (1/3)** — 7 vinetas.
  - Su Dockerfile tiene siete instrucciones —esa cifra se califica, asi que conviene contarlas en voz alta— y el docente debe poder explicar cada una.

**[Slide 16] Primer ejemplo: el stub de la API de CloudLite (2/3)** — 7 vinetas.

**[Slide 17] Primer ejemplo: el stub de la API de CloudLite (3/3)** — 4 vinetas.

**[Slide 18] Construir, correr y verificar: los tres comandos y el contrato de salud (1/3)** — 8 vinetas.

**[Slide 19] Construir, correr y verificar: los tres comandos y el contrato de salud (2/3)** — 7 vinetas.

**[Slide 20] Construir, correr y verificar: los tres comandos y el contrato de salud (3/3)** — 4 vinetas.

**[Slide 21] Segundo ejemplo: leer las siete columnas de docker ps (1/2)** — 8 vinetas.
  - De ahi sale la regla operativa del dia, y hay que decirla como consecuencia del limite y no como consejo suelto: el Dockerfile se escribe en la carpeta del proyecto y se PEGA en el laboratorio, nunca al contrario, y las capturas se guardan antes de cerrar.

**[Slide 22] Segundo ejemplo: leer las siete columnas de docker ps (2/2)** — 7 vinetas.

**[Slide 23] Preguntas frecuentes y cierre conceptual () (1/3)** — 7 vinetas.
  - Tres preguntas se repiten en esta clase.

**[Slide 24] Preguntas frecuentes y cierre conceptual () (2/3)** — 8 vinetas.

**[Slide 25] Preguntas frecuentes y cierre conceptual () (3/3)** — 5 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 3 - Virtualizacion y contenedores/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 3 · Virtualización y contenedores
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. VM vs contenedor
5. Lab en navegador (pasos demo)
6. Dockerfile mínimo para el stub
7. Construir, correr y verificar el contenedor
8. De donde viene la clase y que se entrega hoy
9. Antes de la virtualizacion: un servidor por aplicacion
10. Recorrer el diagrama de las dos pilas, de abajo hacia arriba
11. El contenedor: aislamiento sin otro sistema operativo (1/2)
12. El contenedor: aislamiento sin otro sistema operativo (2/2)
13. Dockerfile, imagen, contenedor y registro: los cuatro terminos (1/2)
14. Dockerfile, imagen, contenedor y registro: los cuatro terminos (2/2)
15. Primer ejemplo: el stub de la API de CloudLite (1/3)
16. Primer ejemplo: el stub de la API de CloudLite (2/3)
17. Primer ejemplo: el stub de la API de CloudLite (3/3)
18. Construir, correr y verificar: los tres comandos y el contrato de salud (1/3)
19. Construir, correr y verificar: los tres comandos y el contrato de salud (2/3)
20. Construir, correr y verificar: los tres comandos y el contrato de salud (3/3)
21. Segundo ejemplo: leer las siete columnas de docker ps (1/2)
22. Segundo ejemplo: leer las siete columnas de docker ps (2/2)
23. Preguntas frecuentes y cierre conceptual () (1/3)
24. Preguntas frecuentes y cierre conceptual () (2/3)
25. Preguntas frecuentes y cierre conceptual () (3/3)
26. Máquinas virtuales vs. contenedores
27. Maquina virtual vs contenedor — que cambia de verdad
28. Dockerfile minimo del stub CloudLite
29. Herramientas de hoy
30. PI CloudLite — entregable de hoy
31. Manos a la obra (paso a paso)
32. Para continuar (PI)
33. Clase 3 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 30]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Contenerizar un stub del servicio principal de CloudLite**.
Entregable concreto: Dockerfile del stub + bitácora de 5 comandos con la salida real + captura del lab.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~7 min cada uno, con su diapositiva:
- **VM vs contenedor** · [Slide 4]
- **Lab en navegador (pasos demo)** · [Slide 5]
- **Dockerfile mínimo para el stub** · [Slide 6]
- **Construir, correr y verificar el contenedor** · [Slide 7]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 28]
Herramienta del día: **Killercoda · alterna si no carga: LabEx Docker Playground**.
**Demo que usted debe poder repetir:** Construir, correr y verificar el stub en Killercoda — los 5 comandos de la bitacora

1. Abra killercoda.com, inicie sesion con la cuenta gratuita y lance un escenario Ubuntu (advierta en voz alta: la sesion caduca a 1 h, guarden capturas antes de cerrarla).
2. Escriba el Dockerfile del stub en vivo, en el mismo orden de la diapositiva «Dockerfile minimo del stub CloudLite»: FROM node:20-alpine, WORKDIR, COPY package*.json, RUN npm ci --omit=dev, COPY . ., EXPOSE 8080, CMD. Y cree al lado un `.dockerignore` con `.env` y `node_modules` — diga: «sin este archivo, el COPY . . se lleva el .env a la imagen y son 5 puntos».
3. Comando 1 — `docker build -t cloudlite-api:0.1.0 .` Senale la etiqueta `0.1.0`: «sin ella la imagen queda como latest y la de hoy no es la de manana». Senale en el log que `COPY package*.json` corre ANTES que `COPY . .`.
4. Comando 2 — `docker images | grep cloudlite-api` y lea en voz alta el TAG y el SIZE: «esto es lo que va en la fila 2 de la bitacora, pegado, no descrito».
5. Comando 3 — `docker run -d -p 8081:8080 --name api cloudlite-api:0.1.0`. Escriba en el tablero «8081 = anfitrion, por donde entro yo» y «8080 = contenedor, el del EXPOSE», y aclare por que los puse DISTINTOS: para que se vea cual es cual.
6. Comando 4 — `docker ps`: senale IMAGE, STATUS y la columna PORTS con `0.0.0.0:8081->8080/tcp`. Ejecute `date` justo antes: «la hora del sistema en la misma captura vale 0.5 puntos».
7. Comando 5 — `curl -i http://localhost:8081/health` y lea los TRES datos del contrato: la ruta, el `HTTP/1.1 200 OK` y el cuerpo JSON con su campo verificable.
8. Error a proposito, 60 segundos: pare el contenedor y relancelo con los puertos invertidos (`-p 8080:8081`). `docker ps` sigue diciendo Up y el `curl` se queda colgado: «el sintoma no dice la causa; por eso la pregunta 10 pide explicar que pasa si los inviertes».
9. Si Killercoda no carga, la alterna es LabEx Docker Playground (ojo: solo 3 sesiones al dia en el plan gratuito); si falla la red, proyecte las capturas de `Kit docente/Clase 3/Capturas/`.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 3/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Build y run del stub en el lab del navegador (lo que debe verse en pantalla) [[captura: salida-docker-build-run.png]]
📸 Evidencia del entregable: el contenedor corriendo (`docker ps`) [[captura: salida-docker-ps.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 31]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 3/Quiz Clase 3 - Virtualizacion y contenedores.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 33]
Di: «Queda avanzado: Contenerizar un stub del servicio principal de CloudLite.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: elija en la pregunta 8 cual servicio de su C4 Context va a contenedorizar y justifiquelo en 2 o 3 frases; escriba a continuacion el Dockerfile completo con la imagen base ligera y con etiqueta fija, el COPY de dependencias antes del COPY del codigo, el EXPOSE y el CMD, verificando que no copie el .env ni ninguna clave.
2. Paso 2: explique en la pregunta 9, sobre su propio Dockerfile, la diferencia entre imagen y contenedor, que instrucciones de SU archivo crean capa, por que el orden aprovecha el cache y en que se diferencia su contenedor de una maquina virtual; verifique que no escribio que un contenedor es una VM ligera.
3. Paso 3: describa en la pregunta 10 el ciclo completo con los comandos exactos de build y de run, explicando que lado del mapeo de puertos es el anfitrion y que lado el contenedor, y cierre con el contrato del endpoint de salud (ruta, codigo de estado y cuerpo); verifique que el puerto sea el mismo que puso en el EXPOSE.
4. Paso 4: ejecute de verdad el ciclo en Killercoda y reporte en la pregunta 11 la tabla de 5 filas con la salida real pegada textualmente, la descripcion de la captura con prompt, docker ps y hora del sistema, y una fila de incidente; recuerde que la sesion caduca a 1 hora, asi que capture la evidencia ANTES de cerrarla.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Decir que el contenedor «es una VM ligera». Insista en la diferencia real: kernel propio vs kernel compartido.
- Confundir imagen con contenedor al hablar. Corrija en el momento: la imagen es el molde, el contenedor la instancia corriendo.
- Perder el trabajo porque la sesion del lab caduco a la hora. Es el error mas comun del dia: recuerdeles que el Dockerfile se escribe en la carpeta del PI y se PEGA en el lab, nunca al contrario.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que comparten los contenedores de una misma maquina que las VM no comparten?
1. Cual es la diferencia entre imagen y contenedor?
1. Que pasa con su trabajo cuando caduca la sesion del lab, y donde deberia vivir el Dockerfile?

## Solución del taller (privada)
`Kit docente/Clase 3/Solucion Taller Clase 3 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 3/Quiz Clase 3 - Virtualizacion y contenedores.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 3/Quiz Clase 3 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase03.png | receta: 1) Abre Killercoda · alterna si no carga: LabEx Docker Playground y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 3/Capturas/demo-clase03.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase03.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 3/Capturas/evidencia-clase03.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
