# Guion docente — Clase 8: Monitoreo y optimización · CI/CD

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Explicar pipeline CI vs CD y qué es realista sin cloud de pago.
- Crear un workflow Actions que construya/pruebe un stub.
- Definir 4–6 señales de monitoreo para CloudLite.

## Hoy avanzamos el PI en…
**Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**

**Entregable concreto:** .github/workflows/ci.yml + sección Monitoreo/CI del informe

**Herramienta:** Navegador · editor de código del curso (YAML)

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 7] Integracion continua: el problema que resuelve, en definicion operativa (1/2)** — 3 vinetas.
  - Lo que se califica hoy son 25 de los 100 puntos de la actividad del Corte 2, en cuatro preguntas: 10 puntos el contenido completo del ci.yml, 5 explicar que hace de verdad la construccion y la prueba y con que condicion el pipeline debe fallar, 4 distinguir CI de CD y ubicar hasta donde llego el propio trabajo, y 6 la tabla de senales de monitoreo con umbral.
  - Conviene decir el reparto al abrir la clase, porque las dos preguntas que el grupo subestima, la 8 y la 10, valen juntas mas que el YAML.

**[Slide 8] Integracion continua: el problema que resuelve, en definicion operativa (2/2)** — 2 vinetas.

**[Slide 9] Entrega continua y despliegue continuo: la sigla CD es ambigua** — 6 vinetas.
  - Entrega continua significa que cada cambio que pasa la validacion queda listo para desplegarse, empaquetado y probado, pero un humano decide cuando se aprieta el boton.
  - El pipeline llega hasta «listo para desplegar» y la etapa final imprime un mensaje y publica un artefacto en lugar de subir a un servidor real.
  - Hay que decirlo explicito: lo simulado es el ultimo paso, no el pipeline; todo lo anterior es real y ejecutable.

**[Slide 10] GitHub Actions en cinco palabras (1/2)** — 5 vinetas.
  - Su vocabulario tiene cinco palabras.

**[Slide 11] GitHub Actions en cinco palabras (2/2)** — 3 vinetas.

**[Slide 12] Los tres bloques que la pregunta 7 califica, y el orden de los pasos (1/2)** — 5 vinetas.

**[Slide 13] Los tres bloques que la pregunta 7 califica, y el orden de los pasos (2/2)** — 4 vinetas.

**[Slide 14] Monitorear y observar: la segunda mitad cambia de lado (1/2)** — 5 vinetas.
  - Se apoya en tres tipos de senal.

**[Slide 15] Monitorear y observar: la segunda mitad cambia de lado (2/2)** — 3 vinetas.

**[Slide 16] Las cuatro senales de oro, con definicion operativa (1/2)** — 5 vinetas.
  - Errores es la proporcion de peticiones que fallan, tipicamente el porcentaje de respuestas 5xx; conviene expresarlo como disponibilidad, y aqui hay aritmetica que el docente debe citar: 99,9 por ciento equivale a unos 43 minutos de indisponibilidad al mes y 99,99 por ciento a unos 4 minutos, lo cual no es convencion sino calculo sobre los 43.200 minutos de un mes de treinta dias.

**[Slide 17] Las cuatro senales de oro, con definicion operativa (2/2)** — 2 vinetas.

**[Slide 18] La tabla de senales de la pregunta 10, con sus tres columnas exactas (1/2)** — 4 vinetas.
  - «Medimos la latencia» no permite decidir nada
  - Una tabla de referencia para CloudLite, que el docente puede llenar en vivo: latencia p95 del inicio de sesion y del listado principal, con objetivo bajo 300 milisegundos; peticiones por minuto en la hora pico, con un valor esperado que sirva de linea base; porcentaje de respuestas 5xx, con alerta sobre el 1 por ciento sostenido; uso del pool de conexiones, con alerta sobre el 80 por ciento; y la fila que casi nadie escribe y vale un punto, un REGISTRO: el log estructurado de cada reserva rechazada y de cada intento de inicio de sesion fallido, con identificador de peticion, ruta y codigo, cuyo umbral es un evento observable, por ejemplo mas de cinco fallos del mismo usuario en diez minutos se revisa.
  - Conviene proyectar esa fila y decir «esta es la que falta en el 80 por ciento de las entregas».
  - Ahi entra la optimizacion de la segunda mitad del tema: paginar, con veinte a cincuenta elementos por pagina, porque un endpoint que devuelve cincuenta mil registros es problema de latencia y de memoria; indexar la columna por la que se filtra, porque sin indice el motor recorre la tabla completa; cachear lecturas repetidas, donde una tasa de acierto del 90 por ciento significa que nueve de cada diez lecturas no llegan a la base; y limitar la tasa de peticiones, el control de denegacion de servicio de la Clase 6.

**[Slide 19] La tabla de senales de la pregunta 10, con sus tres columnas exactas (2/2)** — 4 vinetas.

**[Slide 20] El pipeline del stub de CloudLite, paso por paso (1/2)** — 4 vinetas.
  - El workflow se dispara en push y en pull_request.

**[Slide 21] El pipeline del stub de CloudLite, paso por paso (2/2)** — 3 vinetas.

**[Slide 22] La condicion de fallo: la pregunta que separa un CI de una decoracion verde** — 5 vinetas.
  - Uno y medio, que se compila o se instala.
  - Uno y medio, que se ejecuta en la prueba y que comprueba exactamente.
  - La forma de responderlo es una prueba mental que el docente debe hacer en voz alta y en vivo: que error tendria que introducir yo en el codigo para que este pipeline lo detecte.
  - Si la respuesta no aparece en diez segundos, el pipeline no valida nada todavia.
  - La respuesta es que una sola prueba que verifique que el endpoint /health responde 200 detecta la clase de error mas costosa en operacion, que la aplicacion ya no arranca; y con eso la condicion de fallo se escribe sola: el check sale rojo si /health deja de responder 200, si falta una dependencia declarada o si el docker build no compila.
  - Conviene romper el pipeline a proposito en la demo, porque un check rojo proyectado ensena mas que el parrafo anterior.

**[Slide 23] Donde se ejecuta de verdad la politica de secretos de la Clase 6 (1/2)** — 3 vinetas.
  - Los valores sensibles se guardan en el repositorio bajo Settings, Secrets and variables, Actions; el workflow los referencia por nombre y la plataforma los inyecta como variables de entorno solo durante la corrida.
  - Dos detalles evitan sustos.

**[Slide 24] Donde se ejecuta de verdad la politica de secretos de la Clase 6 (2/2)** — 2 vinetas.

**[Slide 25] Preguntas frecuentes del grupo (1/2)** — 4 vinetas.
  - Cuatro que aparecen todos los semestres.
  - Un umbral justificado asi vale, aunque despues la medicion lo corrija.

**[Slide 26] Preguntas frecuentes del grupo (2/2)** — 4 vinetas.

**[Slide 27] El workflow de CI: el archivo completo** — 22 vinetas.

**[Slide 28] Secretos en el workflow, y hasta donde llega el pipeline** — 10 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 8 · Monitoreo y optimización · CI/CD
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. CI/CD sin tarjeta
5. YAML mínimo
6. Monitoreo y optimización
7. Integracion continua: el problema que resuelve, en definicion operativa (1/2)
8. Integracion continua: el problema que resuelve, en definicion operativa (2/2)
9. Entrega continua y despliegue continuo: la sigla CD es ambigua
10. GitHub Actions en cinco palabras (1/2)
11. GitHub Actions en cinco palabras (2/2)
12. Los tres bloques que la pregunta 7 califica, y el orden de los pasos (1/2)
13. Los tres bloques que la pregunta 7 califica, y el orden de los pasos (2/2)
14. Monitorear y observar: la segunda mitad cambia de lado (1/2)
15. Monitorear y observar: la segunda mitad cambia de lado (2/2)
16. Las cuatro senales de oro, con definicion operativa (1/2)
17. Las cuatro senales de oro, con definicion operativa (2/2)
18. La tabla de senales de la pregunta 10, con sus tres columnas exactas (1/2)
19. La tabla de senales de la pregunta 10, con sus tres columnas exactas (2/2)
20. El pipeline del stub de CloudLite, paso por paso (1/2)
21. El pipeline del stub de CloudLite, paso por paso (2/2)
22. La condicion de fallo: la pregunta que separa un CI de una decoracion verde
23. Donde se ejecuta de verdad la politica de secretos de la Clase 6 (1/2)
24. Donde se ejecuta de verdad la politica de secretos de la Clase 6 (2/2)
25. Preguntas frecuentes del grupo (1/2)
26. Preguntas frecuentes del grupo (2/2)
27. El workflow de CI: el archivo completo
28. Secretos en el workflow, y hasta donde llega el pipeline
29. .github/workflows/ci.yml — CI real, no un echo
30. Herramientas de hoy
31. PI CloudLite — entregable de hoy
32. Manos a la obra (paso a paso)
33. Para continuar (PI)
34. Clase 8 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 31]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Workflow Actions (build/test/simulate) + métricas de monitoreo del PI**.
Entregable concreto: .github/workflows/ci.yml + sección Monitoreo/CI del informe.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **CI/CD sin tarjeta** · [Slide 4]
- **YAML mínimo** · [Slide 5]
- **Monitoreo y optimización** · [Slide 6]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 29]
Herramienta del día: **Navegador · editor de código del curso (YAML)**.
**Demo que usted debe poder repetir:** Un workflow de GitHub Actions que corra de verdad, con los tres pasos calificados

1. Cree `.github/workflows/ci.yml` copiando la diapositiva del ci.yml: `on: [push, pull_request]`, `runs-on: ubuntu-latest` y los pasos en ORDEN — Construir, Probar, Despliegue SIMULADO.
2. Senale los tres bloques mientras los escribe: «disparadores, entorno y pasos: son 2, 1.5 y 4 puntos de la pregunta 7».
3. En el paso Construir use la MISMA imagen de la Clase 3: `npm ci && docker build -t cloudlite-api:0.1.0 .` — la coherencia con el Dockerfile del Corte 1 vale 1 pt.
4. Haga commit y push, abra la pestana Actions y espere el check verde; abra el log del paso Probar: «esto es evidencia, no una diapositiva que dice que tenemos CI».
5. Rompa el pipeline a proposito, 60 segundos: cambie la asercion de la prueba (o borre `server.js`), haga push y muestre el check ROJO. Diga: «esta es la respuesta de la pregunta 8: con que condicion falla. Si no pueden romperlo, no estan validando nada».
6. Vuelva a dejarlo verde y lea en voz alta el nombre del ultimo paso: «Despliegue SIMULADO (no despliega a ningun servidor)». Aclare la frontera: el pipeline llega hasta «listo para desplegar», y decirlo asi SUMA en la pregunta 9 — afirmar que ya hay CD resta la mitad.
7. Cierre en Settings > Secrets and variables > Actions: «los secretos viven aqui y se referencian por nombre. Un secreto escrito en claro dentro del YAML es cero en toda la pregunta 7».

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 8/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Run verde del workflow: build + test reales, no un `echo ok` [[captura: salida-actions-run.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 32]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 34]
Di: «Queda avanzado: Workflow Actions (build/test/simulate) + métricas de monitoreo del PI.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en la plataforma del curso. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: escriba en la pregunta 7 el contenido completo del ci.yml con disparadores, entorno y los pasos de construccion, prueba y despliegue simulado, usando la imagen y el puerto del Dockerfile del Corte 1; verifique que ningun secreto quede escrito en claro dentro del YAML.
2. Paso 2: explique en la pregunta 8 que se compila o instala, que se ejecuta en la prueba y con que condicion el pipeline debe fallar; hagase la prueba mental de que error tendria que introducir para que el check salga rojo, y si no encuentra ninguno, su pipeline todavia no valida nada.
3. Paso 3: distinga en la pregunta 9 que valida CI y que hace CD, ubique cual de los dos construyo y diga que le faltaria para CD real; reconocer que su pipeline llega hasta «listo para desplegar» suma puntos, afirmar que ya tiene CD los resta.
4. Paso 4: liste en la pregunta 10 entre 4 y 6 senales con su umbral, atadas a operaciones de su dominio, y verifique que al menos una sea un registro y no una metrica numerica; una senal sin umbral no sirve para operar y no suma.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Un workflow que solo hace `echo ok`: es un pipeline decorativo. Exija que corra algo que pueda fallar de verdad.
- Decir que ya tienen CD porque el YAML dice deploy. En este curso el despliegue se simula; que lo digan asi.
- Golden signals sin umbral: «medimos latencia» no sirve; falta a partir de que valor se considera un problema.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que valida CI y que hace CD, y cual de los dos construyeron hoy?
1. Digan las 4 golden signals y el umbral de una de ellas.
1. Que pasaria en su pipeline si alguien sube codigo que no compila?

## Solución del taller (privada)
`Kit docente/Clase 8/Solucion Taller Clase 8 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 8/Quiz Clase 8 - Monitoreo optimizacion y CI-CD.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 8/Quiz Clase 8 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase08.png | receta: 1) Abre Navegador · editor de código del curso (YAML) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 8/Capturas/demo-clase08.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase08.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 8/Capturas/evidencia-clase08.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: la plataforma del curso (la plataforma del curso). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
