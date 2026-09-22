# Guion docente — Clase 2: Modelos de servicio: IaaS, PaaS, SaaS

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Comparar IaaS, PaaS y SaaS con criterios de control, operación y velocidad.
- Elegir el modelo dominante de CloudLite con justificación.
- Documentar la decisión como ADR reutilizable en el informe PI.

## Hoy avanzamos el PI en…
**Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**

**Entregable concreto:** ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio

**Herramienta:** Google Docs · draw.io (opcional)

## Fundamento teórico para el docente
## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 8] De que se parte y que se decide hoy (1/2)** — 3 vinetas.

**[Slide 9] De que se parte y que se decide hoy (2/2)** — 2 vinetas.

**[Slide 10] La pila de responsabilidades: donde se corta la linea (1/2)** — 3 vinetas.
  - Los tres modelos de servicio se distinguen exactamente por donde se traza la linea que separa lo que administra el proveedor de lo que administra el cliente.

**[Slide 11] La pila de responsabilidades: donde se corta la linea (2/2)** — 4 vinetas.

**[Slide 12] IaaS, PaaS y SaaS: los tres cortes, uno por uno (1/4)** — 4 vinetas.
  - Lo que gana es control total, porque puede instalar cualquier version de cualquier cosa, abrir los puertos que quiera y afinar el sistema.
  - Lo que paga es trabajo operativo permanente, que en la practica se mide en horas de persona por semana dedicadas a aplicar parches de seguridad, rotar certificados y vigilar el espacio en disco.
  - Para CloudLite Turnos, el ejemplo de la barberia con agendamiento de citas, elegir IaaS significaria que el estudiante se compromete a administrar el sistema operativo donde corren la API y la base de datos; en un curso de doce semanas, y trabajando solo o con dos companeros, eso consume justamente el tiempo que deberia dedicarse a disenar la arquitectura y a sustentarla.

**[Slide 13] IaaS, PaaS y SaaS: los tres cortes, uno por uno (2/4)** — 4 vinetas.

**[Slide 14] IaaS, PaaS y SaaS: los tres cortes, uno por uno (3/4)** — 4 vinetas.

**[Slide 15] IaaS, PaaS y SaaS: los tres cortes, uno por uno (4/4)** — 3 vinetas.

**[Slide 16] Responsabilidad compartida: quien responde por que (1/2)** — 5 vinetas.
  - De ahi sale el trade-off central, que se escribe como regla practica: a mas abstraccion, menos control y menos trabajo operativo.

**[Slide 17] Responsabilidad compartida: quien responde por que (2/2)** — 3 vinetas.

**[Slide 18] El ADR-001: seis secciones rotuladas y una sola decision (1/4)** — 5 vinetas.
  - Conviene mostrar la diferencia entre contexto y analisis con el ejemplo, porque es donde se pierde la seccion 3 completa.
  - Eso es contexto: son restricciones, no teoria.
  - La prueba que el docente puede aplicar en voz alta mientras pasa por los grupos es una sola: si del contexto no se puede deducir por que se descarta IaaS, todavia no es contexto.
  - Que identidad y correo se consuman como SaaS satelite se aclara aqui y no en la decision, porque el modelo dominante se refiere a la aplicacion propia.

**[Slide 19] El ADR-001: seis secciones rotuladas y una sola decision (2/4)** — 5 vinetas.

**[Slide 20] El ADR-001: seis secciones rotuladas y una sola decision (3/4)** — 4 vinetas.

**[Slide 21] El ADR-001: seis secciones rotuladas y una sola decision (4/4)** — 3 vinetas.

**[Slide 22] La pila dibujada: nombres reales para IaaS, PaaS y SaaS (1/2)** — 3 vinetas.

**[Slide 23] La pila dibujada: nombres reales para IaaS, PaaS y SaaS (2/2)** — 3 vinetas.

**[Slide 24] Preguntas frecuentes y cierre conceptual () (1/3)** — 5 vinetas.
  - Tres preguntas salen en voz alta en esta clase casi sin falta y conviene tener la respuesta lista, porque las tres se contestan en treinta segundos y desbloquean el taller.

**[Slide 25] Preguntas frecuentes y cierre conceptual () (2/3)** — 5 vinetas.

**[Slide 26] Preguntas frecuentes y cierre conceptual () (3/3)** — 4 vinetas.


## Referencias a diapositivas
Numeración real del deck `Clases/Clase 2 - Modelos de servicio IaaS PaaS SaaS/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 2 · Modelos de servicio: IaaS, PaaS, SaaS
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. IaaS · PaaS · SaaS (sin cloud de pago)
5. Cómo decidir para CloudLite
6. Responsabilidad compartida: quién responde por qué
7. Plantilla ADR-001
8. De que se parte y que se decide hoy (1/2)
9. De que se parte y que se decide hoy (2/2)
10. La pila de responsabilidades: donde se corta la linea (1/2)
11. La pila de responsabilidades: donde se corta la linea (2/2)
12. IaaS, PaaS y SaaS: los tres cortes, uno por uno (1/4)
13. IaaS, PaaS y SaaS: los tres cortes, uno por uno (2/4)
14. IaaS, PaaS y SaaS: los tres cortes, uno por uno (3/4)
15. IaaS, PaaS y SaaS: los tres cortes, uno por uno (4/4)
16. Responsabilidad compartida: quien responde por que (1/2)
17. Responsabilidad compartida: quien responde por que (2/2)
18. El ADR-001: seis secciones rotuladas y una sola decision (1/4)
19. El ADR-001: seis secciones rotuladas y una sola decision (2/4)
20. El ADR-001: seis secciones rotuladas y una sola decision (3/4)
21. El ADR-001: seis secciones rotuladas y una sola decision (4/4)
22. La pila dibujada: nombres reales para IaaS, PaaS y SaaS (1/2)
23. La pila dibujada: nombres reales para IaaS, PaaS y SaaS (2/2)
24. Preguntas frecuentes y cierre conceptual () (1/3)
25. Preguntas frecuentes y cierre conceptual () (2/3)
26. Preguntas frecuentes y cierre conceptual () (3/3)
27. Quién administra cada capa — IaaS vs PaaS vs SaaS
28. ADR-001 — las 6 secciones caben en una pagina
29. Herramientas de hoy
30. PI CloudLite — entregable de hoy
31. Manos a la obra (paso a paso)
32. Para continuar (PI)
33. Clase 2 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 30]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**.
Entregable concreto: ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 4]
Cubre estos conceptos, en este orden, ~7 min cada uno, con su diapositiva:
- **IaaS · PaaS · SaaS (sin cloud de pago)** · [Slide 4]
- **Cómo decidir para CloudLite** · [Slide 5]
- **Responsabilidad compartida: quién responde por qué** · [Slide 6]
- **Plantilla ADR-001** · [Slide 7]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 28]
Herramienta del día: **Google Docs · draw.io (opcional)**.
**Demo que usted debe poder repetir:** Llenar un ADR-001 delante del grupo, con sus 6 secciones rotuladas

1. Abra un Google Doc y escriba los 6 encabezados en orden: 1. Titulo · 2. Estado · 3. Contexto · 4. Decision · 5. Alternativas descartadas · 6. Consecuencias.
2. Titulo: «ADR-001 Modelo de servicio dominante de CloudLite App». Estado: «Aceptado» y la fecha de hoy. Diga en voz alta: «estos dos rotulos valen 1.5 puntos y son los que se citan en la sustentacion».
3. Contexto: «lo desarrolla una persona en doce semanas, sin presupuesto ni tarjeta, y tiene que estar en linea el dia de la sustentacion». Subraye que son RESTRICCIONES: «existen tres modelos y hay que elegir uno» no es contexto, es el apunte de clase.
4. Decision, en una sola frase: «la aplicacion de CloudLite se despliega sobre PaaS». Tache en vivo un segundo modelo si alguien lo propone: «esta seccion vale cero si nombra dos».
5. Alternativas descartadas, exactamente dos: IaaS, porque habria que operar el sistema operativo sin tiempo para ello; SaaS como nucleo, porque no quedaria arquitectura que disenar. Aclare aqui —y no en la decision— que identidad y correo siguen siendo SaaS satelite.
6. Consecuencias: escriba UN eje (operacion) con su + y su -, y deje los otros dos al grupo. Diga: «un ADR de una pagina que se entiende vale mas que 5 paginas que nadie lee».

Narra los clics en voz alta. Si falla la red, proyecta la [Slide 28], que ya trae el resultado de la demo, y recórrela rótulo por rótulo.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 31]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 33]
Di: «Queda avanzado: Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: relea su ficha y su C4 Context de la Clase 1. No cambie de dominio: las preguntas 5 a 7 se califican sobre el mismo sistema, y el ADR que redacte hoy se reutiliza en el informe del PI y en la sustentacion de la Clase 15.
2. Paso 2: construya en la pregunta 5 la matriz «Criterio | IaaS | PaaS | SaaS» con las cuatro filas en orden (control, costo cualitativo, operacion, time-to-demo) y maximo 2 lineas por celda; verifique que cada celda nombre una capacidad o una restriccion de SU dominio, y que la fila de operacion no afirme que en PaaS o SaaS usted deja de responder por su propia aplicacion.
3. Paso 3: redacte en la pregunta 6 el ADR-001 con las cinco secciones rotuladas —titulo, estado con fecha, contexto con sus restricciones reales, la decision en UNA sola frase con UN modelo dominante, y exactamente 2 alternativas descartadas con el motivo atado a su dominio—; verifique que la seccion de decision no nombre dos modelos, porque en ese caso vale cero.
4. Paso 4: escriba en la pregunta 7 la seccion 6 del mismo ADR, las consecuencias en los tres ejes (operacion, costo y aprendizaje), con al menos una positiva y una negativa por eje marcadas con + y -, y verifique que al menos una negativa hable de amarre al proveedor o de perdida de control; guarde y continue, que la actividad se entrega completa al cierre del corte.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Elegir el modelo de servicio por moda y no por trade-off. Pida la frase «aceptamos perder X para ganar Y» escrita en el ADR.
- ADR sin alternativas descartadas: un ADR con una sola opcion no documenta una decision, documenta un hecho.
- Nombrar productos de marca en vez del modelo conceptual; el modelo aplica a cualquier proveedor.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Quien administra el sistema operativo en IaaS, en PaaS y en SaaS?
1. Que perdieron y que ganaron con el modelo que eligieron?
1. Por que un ADR necesita las alternativas que descartaron?

## Solución del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 2/Quiz Clase 2 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase02.png | receta: 1) Abre Google Docs · draw.io (opcional) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 2/Capturas/demo-clase02.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase02.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 2/Capturas/evidencia-clase02.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
