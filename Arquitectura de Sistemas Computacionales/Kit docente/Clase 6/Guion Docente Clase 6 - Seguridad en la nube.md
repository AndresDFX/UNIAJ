# Guion docente — Clase 6: Seguridad en la nube

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Aplicar un modelo de amenazas simple al dominio CloudLite.
- Mapear controles (authn/z, secretos, superficie de red) sin cloud de pago.
- Dejar la sección Seguridad del informe lista en borrador.

## Hoy avanzamos el PI en…
**Modelo de amenazas mínimo + controles para CloudLite**

**Entregable concreto:** Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI

**Herramienta:** Google Docs para la tabla y la política · ExamLab para entregar

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 10] Seguridad como propiedad del diseno: la triada CIA (1/2)** — 3 vinetas.
  - Casi todos los incidentes reales ocurren del lado del cliente.

**[Slide 11] Seguridad como propiedad del diseno: la triada CIA (2/2)** — 2 vinetas.

**[Slide 12] Modelar amenazas: las cuatro preguntas y el vocabulario (1/2)** — 4 vinetas.
  - Hace falta vocabulario preciso, porque el estudiante usa estas palabras como sinonimos.

**[Slide 13] Modelar amenazas: las cuatro preguntas y el vocabulario (2/2)** — 3 vinetas.

**[Slide 14] STRIDE: seis categorias, cada una niega una propiedad** — 4 vinetas.
  - Tampering modifica datos sin autorizacion y niega la integridad.
  - Denial of service agota un recurso hasta que el sistema deja de responder y niega la disponibilidad.
  - Elevation of privilege obtiene mas permisos de los asignados y niega la autorizacion.
  - De ahi sale la distincion que mas se confunde: autenticacion es demostrar quien eres, autorizacion es determinar que puedes hacer una vez identificado.
  - Un sistema puede autenticar impecablemente y seguir siendo inseguro si despues no verifica permisos.

**[Slide 15] Los controles gratuitos, en tres familias (1/2)** — 4 vinetas.
  - Los controles que el estudiante puede citar sin pagar nada se ordenan en tres familias.

**[Slide 16] Los controles gratuitos, en tres familias (2/2)** — 2 vinetas.

**[Slide 17] Menor privilegio: la resta que hay que poder nombrar (1/2)** — 4 vinetas.
  - Si la respuesta no tiene un verbo en negativo, no esta aplicado.
  - Menor privilegio no evita el ataque, acota el dano; decirlo asi evita la objecion de «entonces igual me atacan».
  - Conviene ademas dar la version de la que casi nadie se acuerda: el principio aplica a personas igual que a servicios, y en un proyecto de un semestre el caso mas cercano es que no todo integrante del equipo necesita permiso de administracion en el repositorio.

**[Slide 18] Menor privilegio: la resta que hay que poder nombrar (2/2)** — 3 vinetas.

**[Slide 19] Gestion de secretos: el error mas repetido y el mas facil de verificar (1/2)** — 5 vinetas.
  - Con herramientas gratis, el valor real vive en los secretos del repositorio y se inyecta como variable de entorno en ejecucion, versionando solo un archivo de ejemplo con los nombres de las variables.

**[Slide 20] Gestion de secretos: el error mas repetido y el mas facil de verificar (2/2)** — 4 vinetas.

**[Slide 21] La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (1/3)** — 5 vinetas.
  - Conviene recorrer renglon por renglon, porque el estudiante que solo escucho «no los pongas en el Dockerfile» responde una de las cinco y pierde las otras cuatro.
  - Esa distincion entre el nombre de un secreto, que es publico, y su valor, que no lo es, es la senal de que el estudiante entendio el tema.

**[Slide 22] La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (2/3)** — 6 vinetas.

**[Slide 23] La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (3/3)** — 3 vinetas.

**[Slide 24] Primer ejemplo: autenticacion con token en CloudLite** — 6 vinetas.
  - Primer ejemplo concreto.
  - En CloudLite el usuario final se autentica contra la API y recibe un token, una cadena firmada que acompana cada peticion posterior para no volver a pedir la contrasena.

**[Slide 25] Segundo ejemplo: PII y las tres amenazas de identidad** — 5 vinetas.
  - Segundo ejemplo concreto.
  - La respuesta que devuelve mas de lo necesario: el endpoint de perfil serializa la fila completa e incluye el hash de la contrasena o el correo de otros usuarios; el control es declarar que campos salen.

**[Slide 26] El entregable: tres columnas, y la tercera es una caja o una flecha (1/2)** — 4 vinetas.
  - Conviene decirlo con esos nombres porque la tercera reparte 2.5 de los 8.75 puntos y es la que se responde mal: solo admite el nombre de una CAJA o de una FLECHA del C4 Containers o del Despliegue, escrito igual que en el diagrama.
  - «la flecha App web -> API de turnos lleva HTTPS y el identificador se toma del token» si.

**[Slide 27] El entregable: tres columnas, y la tercera es una caja o una flecha (2/2)** — 4 vinetas.

**[Slide 28] Preguntas frecuentes del grupo (1/2)** — 3 vinetas.
  - Estas aparecen todos los semestres, y las cuatro se responden con material que ya esta proyectado.
  - Lo que se descuenta es la misma amenaza escrita dos veces con otras palabras.

**[Slide 29] Preguntas frecuentes del grupo (2/2)** — 3 vinetas.

**[Slide 30] La politica de secretos, en comandos** — 14 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 6 - Seguridad en la nube/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 6 · Seguridad en la nube
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. Amenazas que sí importan al PI
5. Controles prácticos (gratis)
6. Menor privilegio: qué deja de poder hacer
7. Política de secretos: las cuatro preguntas
8. Ejercicio guiado
9. La tabla que se califica: una fila por amenaza
10. Seguridad como propiedad del diseno: la triada CIA (1/2)
11. Seguridad como propiedad del diseno: la triada CIA (2/2)
12. Modelar amenazas: las cuatro preguntas y el vocabulario (1/2)
13. Modelar amenazas: las cuatro preguntas y el vocabulario (2/2)
14. STRIDE: seis categorias, cada una niega una propiedad
15. Los controles gratuitos, en tres familias (1/2)
16. Los controles gratuitos, en tres familias (2/2)
17. Menor privilegio: la resta que hay que poder nombrar (1/2)
18. Menor privilegio: la resta que hay que poder nombrar (2/2)
19. Gestion de secretos: el error mas repetido y el mas facil de verificar (1/2)
20. Gestion de secretos: el error mas repetido y el mas facil de verificar (2/2)
21. La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (1/3)
22. La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (2/3)
23. La politica en cuatro respuestas: quien rota, cada cuanto y que se hace ante una filtracion (3/3)
24. Primer ejemplo: autenticacion con token en CloudLite
25. Segundo ejemplo: PII y las tres amenazas de identidad
26. El entregable: tres columnas, y la tercera es una caja o una flecha (1/2)
27. El entregable: tres columnas, y la tercera es una caja o una flecha (2/2)
28. Preguntas frecuentes del grupo (1/2)
29. Preguntas frecuentes del grupo (2/2)
30. La politica de secretos, en comandos
31. El secreto en la imagen: por qué borrarlo no sirve
32. Herramientas de hoy
33. PI CloudLite — entregable de hoy
34. Manos a la obra (paso a paso)
35. Para continuar (PI)
36. Clase 6 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 33]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Modelo de amenazas mínimo + controles para CloudLite**.
Entregable concreto: Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~5 min cada uno, con su diapositiva:
- **Amenazas que sí importan al PI** · [Slide 4]
- **Controles prácticos (gratis)** · [Slide 5]
- **Menor privilegio: qué deja de poder hacer** · [Slide 6]
- **Política de secretos: las cuatro preguntas** · [Slide 7]
- **Ejercicio guiado** · [Slide 8]
- **La tabla que se califica: una fila por amenaza** · [Slide 9]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 31]
Herramienta del día: **Google Docs para la tabla y la política · ExamLab para entregar**.
**Demo que usted debe poder repetir:** De amenaza STRIDE a control verificable, en vivo

1. Escriba en el tablero, con las dos partes que exige la rubrica: «Tampering: un cliente mueve la franja de un turno ajeno porque la API no revisa de quien es el turno».
2. Pregunte al grupo cual seria el control; guie hasta «validar el rol y la propiedad del turno antes de aceptar el cambio».
3. Agregue la tercera columna preguntando «sobre que CAJA o sobre que FLECHA del C4 Containers cae ese control». Aqui la respuesta es la caja «API de turnos». Un nombre de archivo no vale: si no se puede senalar en el diagrama, el control todavia es una intencion.
4. Repita con una segunda fila cuyo control caiga en una FLECHA, para que se vea que las dos formas cuentan: «un cliente reserva a nombre de otro» -> «el id se toma del token» -> flecha «App web -> API de turnos».
5. Demo de 1 minuto del anti-patron, con la diapositiva del historial de capas proyectada: un Dockerfile con la llave en texto plano, el `docker history` que la lee, y el `rm` posterior que no la borra sino que la tapa.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 6/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
📸 Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto) [[captura: salida-secreto-en-imagen.png]]


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 34]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 36]
Di: «Queda avanzado: Modelo de amenazas mínimo + controles para CloudLite.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: liste en la pregunta 1 cinco amenazas de SU dominio, cada una nombrando el actor o el dato concreto que pone en riesgo y el camino por el que ocurre; use STRIDE como guia de categorias y verifique que ninguna sea una frase de manual que sirva igual para cualquier sistema.
2. Paso 2: complete en la pregunta 2 la tabla amenaza-control-donde, senalando para cada control la caja o la flecha concreta del C4 Containers o del Despliegue donde se ve; incluya el principio de menor privilegio aplicado a un componente, diciendo que deja de poder hacer.
3. Paso 3: escriba en la pregunta 3 la politica de secretos respondiendo donde viven, quien los rota, cada cuanto y que esta prohibido, y cierre con el procedimiento ante una filtracion; verifique que su politica no admita secretos en el Dockerfile, el README ni el YAML en claro.
4. Paso 4: guarde y continue. Esta actividad es una sola para las Clases 6, 7, 8 y 10 y se entrega completa al cierre del Corte 2: hoy resuelve las preguntas 1 a 3 y las 4 a 12 se resuelven en las clases siguientes.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Entregar una lista generica de buenas practicas en vez de amenaza -> control -> donde se ve. Devuelva la tabla si no tiene las 3 columnas con esos nombres.
- Escribir credenciales en el Dockerfile o en el repositorio. Es el error mas costoso y hay que cortarlo el mismo dia.
- Cubrir las 6 categorias STRIDE de forma superficial en vez de las CINCO amenazas bien argumentadas que pide el enunciado. Dos amenazas de la misma letra son validas si el camino y el control son distintos.
- Amenazas sin sujeto ni camino: «podrian hackear la base de datos». Valen la mitad. La prueba rapida es preguntar si esa frase se podria copiar en el trabajo de otro estudiante sin cambiar nada.
- Poner un nombre de archivo en la tercera columna («.dockerignore», «el contrato del endpoint»). No suma: son 2.5 pts que se reparten por senalar una caja o una flecha del diagrama.
- Menor privilegio recitado y no aplicado. Pida las dos frases: sobre que componente, y que deja de poder hacer al aplicarlo.
- Politica de secretos sin responsable ni frecuencia («deberian rotarse periodicamente»). Son 3 de los 7.5 pts de la pregunta 3, y se pierden por escribir en tercera persona.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que significa la T de STRIDE y una amenaza concreta de su CloudLite?
1. Donde guardan una API key y por que NO dentro de la imagen?
1. Sobre que caja o sobre que flecha de SU diagrama cae uno de sus controles? Digalo con el nombre que tiene alli.
1. Quien rota los secretos de su repositorio y cada cuanto? Un rol y un evento del calendario, no «periodicamente».
1. Si manana se filtra su cadena de conexion, cual es el PRIMER paso y por que no es borrar el commit?
1. Sobre que componente aplican menor privilegio, y que deja de poder hacer ese componente al aplicarlo?

## Solución del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 6/Quiz Clase 6 - Seguridad en la nube.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 6/Quiz Clase 6 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase06.png | receta: 1) Abre Google Docs para la tabla y la política · ExamLab para entregar y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 6/Capturas/demo-clase06.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase06.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 6/Capturas/evidencia-clase06.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
