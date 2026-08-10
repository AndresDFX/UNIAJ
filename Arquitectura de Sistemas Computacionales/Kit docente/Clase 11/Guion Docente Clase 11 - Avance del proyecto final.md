# Guion docente — Clase 11: Avance del proyecto final

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI)
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Consolidar evidencias PI en un paquete revisable.
- Detectar huecos (nombres inconsistentes, servicios de más, sin seguridad).
- Salir con backlog claro hacia Clase 12/15.

## Hoy avanzamos el PI en…
**Integrar diagramas v1 + checklist de avance PI**

**Entregable concreto:** Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+

**Herramienta:** draw.io · GitHub · Google Docs

## Fundamento teórico para el docente
Esta clase no introduce teoria de un tema tecnico nuevo, y eso es deliberado, pero si tiene teoria propia: la teoria de la revision y la evaluacion. Una revision de arquitectura, en ingles architecture review, es una practica profesional formal en la que alguien distinto de quien diseno el sistema examina el diseno antes de que este construido, buscando riesgos y decisiones sin justificar. Existe en la industria con nombres concretos: ATAM en su version academica, design review o RFC review en empresas de producto, comite de arquitectura en organizaciones grandes. Todas comparten la premisa economica que sostiene el curso: un riesgo detectado en el diseno cuesta una fraccion de lo que cuesta cuando ya esta implementado y con usuarios encima. La revision no juzga si el diagrama es bonito; busca tres cosas: decisiones sin argumento, incoherencias entre artefactos y riesgos que nadie ha nombrado. Hoy el docente no dicta, audita, y el estudiante no aprende un concepto, demuestra que los que ya tiene forman un sistema.

El insumo es el paquete CloudLite v1, que a estas alturas debe tener seis piezas producidas antes: el C4 de Contexto de la Clase 1, el C4 de Contenedores de la Clase 4, el modelo de amenazas con controles de la Clase 6, el diagrama de despliegue con zonas publica y privada de la Clase 7, el workflow de GitHub Actions y las metricas de monitoreo de la Clase 8, y la tabla de costos con drivers y right-sizing de la Clase 10. El criterio central de auditoria se llama trazabilidad: la propiedad de que un elemento se pueda seguir de un artefacto al siguiente sin cambiar de nombre ni desaparecer. No es una formalidad burocratica, es el unico detector confiable de que el equipo penso el sistema en vez de producir seis tareas independientes para seis notas distintas. Y se audita con preguntas mecanicas que cualquier docente puede hacer sin ser experto en el dominio del equipo, lo que hace esta tecnica ensenable.

Las preguntas de coherencia, aplicadas a CloudLite, son cinco y conviene hacerlas en orden. Primera: cada contenedor del C4 de la Clase 4 aparece en el diagrama de despliegue de la Clase 7 y con el mismo nombre; si el C4 dice "servicio de notificaciones" y el despliegue dice "worker de correos", o son la misma cosa mal nombrada o son dos cosas y falta una. Segunda: cada actor y sistema externo del diagrama de Contexto sigue existiendo; el caso frecuente es que el equipo dibujo en la Clase 1 una pasarela de pagos y hoy ningun contenedor habla con ella, asi que o desaparecio del alcance y hay que borrarla o esta olvidada y es un hueco. Tercera: cada amenaza del modelo STRIDE de la Clase 6 tiene un control visible en el despliegue; si la amenaza es acceso no autorizado a la base de datos y el diagrama la muestra en la subred publica, el control existe en el documento y no en el diseno. Cuarta: los componentes de la tabla de costos de la Clase 10 son los mismos contenedores, no una lista inventada. Quinta: el workflow de Actions se ejecuto al menos una vez con resultado visible, porque un archivo YAML que nunca corrio es una intencion, no evidencia. Ese es el nucleo del acta: no una nota, sino cuales de estas cinco cadenas estan rotas en cada equipo.

Hay dos patologias con nombre propio que arruinan las sustentaciones. La primera es el scope creep, el crecimiento no controlado del alcance: el sistema suma capacidades clase por clase, cada una razonable por si misma, hasta que el equipo tiene un alcance que no puede documentar ni defender en el tiempo restante. Se detecta con un dato objetivo, no con intuicion: en la Clase 1 cada equipo definio entre tres y cinco capacidades para CloudLite, asi que basta contar las de hoy y compararlas con esa linea base; si eran cuatro y hoy son nueve, hay scope creep, y da igual que las nuevas suenen interesantes. La respuesta correcta no es prohibir ideas sino congelar el alcance y abrir una lista de aparcamiento, un anexo donde las capacidades extra quedan escritas como "fuera de alcance v1, candidatas a v2": preserva la idea, protege el cronograma y es lo que hace un equipo profesional al cerrar un release. La segunda patologia es el teatro de microservicios: servicios separados en el diagrama que en la practica no son unidades independientes. Se detecta con cuatro preguntas de una linea, todas respondibles por el estudiante: se puede desplegar ese servicio sin desplegar los otros, tiene sus propios datos o comparte tablas con el vecino, puede fallar sin tumbar a los demas, y existe una razon de negocio por la que cambiaria en un momento distinto al resto. En CloudLite el caso clasico es el "servicio de autenticacion" dibujado como caja aparte que en el repositorio es un modulo dentro de la misma API, escribe en las mismas tablas y se despliega en el mismo contenedor. No es un microservicio, es un modulo, y decirlo no castiga al equipo: corrige el vocabulario antes del Parcial 3, donde esa distincion se evalua.

La retroalimentacion es la mitad del valor del dia y tiene tecnica propia. Una retroalimentacion accionable tiene cuatro partes: observacion, evidencia, impacto y accion con fecha. "Falta seguridad" no cumple ninguna. "En el diagrama de despliegue la base de datos esta en la subred publica, contradice el control que ustedes escribieron para la amenaza de acceso no autorizado; si lo sustentan asi en la Clase 15 el evaluador concluira que el modelo de amenazas se escribio sin mirar el diagrama; muevanla a subred privada y dejen solo la API expuesta, antes de la Clase 12" cumple las cuatro. El docente debe apuntar a tres hallazgos por equipo como maximo y marcar cual es el bloqueante, porque un equipo que recibe once observaciones no corrige ninguna: se paraliza. Conviene nombrar tambien una fortaleza concreta, no por amabilidad sino porque el estudiante necesita saber que conservar; si solo escucha fallas, en la siguiente version cambia todo, incluido lo que estaba bien. Y la revision entre pares cumple una funcion que la del docente no puede: explicarle el sistema a otro equipo obliga a verbalizar decisiones que nunca se dijeron en voz alta, y ahi el propio equipo descubre sus huecos. El formato eficiente es de siete a ocho minutos por equipo, con reloj visible, y el equipo revisor entregando por escrito una observacion y una pregunta.

Falta el criterio para decidir si un equipo va a tiempo, y aqui el docente necesita un umbral y no una impresion. Con seis artefactos esperados la regla practica es un semaforo: verde si estan los seis y a lo sumo una cadena de trazabilidad rota; amarillo si hay cinco de seis, o dos o tres cadenas rotas pero corregibles editando documentos; rojo si falta el C4 de Contenedores o el diagrama de despliegue, que son la columna vertebral y sin los cuales el resto no se puede evaluar, o si el repositorio no existe. El umbral de seis no es una ley de la ingenieria, es la contabilidad de este curso, y decirlo asi evita que el estudiante lo memorice como estandar internacional. Lo transferible es la idea de fondo: un checkpoint se evalua por evidencia presente, no por promesas. Cuando un equipo dice "eso ya lo tenemos, solo falta subirlo", el estado es amarillo y el acta lo registra con fecha de cierre; no es desconfianza, es que en un proyecto lo que no esta en el repositorio no existe. Para un equipo en rojo el plan de recuperacion debe reducir alcance, nunca agregar trabajo: menos capacidades, menos servicios, y toda la energia en las dos piezas que faltan.

Tres preguntas se repiten y el docente debe responderlas sin titubear. La primera es si esto se califica; la respuesta honesta es que este checkpoint no es la sustentacion final, que ocurre en la Clase 15, ni el Parcial 3, que es la evaluacion escrita de la Clase 14, y que hoy se registra estado y compromisos, pero el acta es el insumo con el que se mirara la entrega final: un gap senalado hoy y no cerrado pesa mucho mas que uno que aparecio despues. La segunda es por que revisa otro equipo si el que califica es el docente, y la respuesta es que la revision por pares es practica estandar en la industria y que su valor no esta en el juicio del par sino en la obligacion de explicar; ademas el par pregunta lo que el docente ya asume, y esas son justo las preguntas que llegan en un Q&A real. La tercera, la mas delicada, es si cambiar el diagrama ahora significa perder el trabajo hecho, y la respuesta debe ser tajante: no, porque el artefacto no es el entregable, la decision documentada lo es; un diagrama corregido con una nota de por que cambio vale mas que uno intacto, y ese cambio justificado es exactamente lo que un ADR registra. Conviene cerrar diciendo que lo que se estabilice hoy es la base sobre la que la Clase 12 agregara el analisis de rendimiento y la Clase 13 la politica de escalado, y que un equipo con el paquete v1 incoherente no puede hacer ninguna de las dos, porque no se puede medir ni escalar un sistema que todavia no esta definido.

Error tipico del docente que no domina el tema: dejar pasar el checkpoint con un "todo bien, sigan asi". La consecuencia no se ve hoy, se ve en la Clase 15, cuando varios equipos sustentan con la base de datos expuesta, con servicios que no son servicios y con nueve capacidades que nunca cerraron, y el docente descubre que las tenia todas a la vista un mes antes; ademas el estudiante interpreta el silencio como aprobacion, asi que el error queda ratificado y luego reclama con razon que nadie se lo advirtio. El segundo error es convertir el checkpoint en clase magistral: cuando el docente detecta un vacio conceptual y se pone a reexplicar contenedores o STRIDE durante veinte minutos, se consume el tiempo de los equipos que faltan, la mitad del curso queda sin retroalimentacion y el acta sale a medias. Lo correcto es anotar el vacio, dar la accion concreta con fecha y seguir; si el vacio es general al grupo, se atiende en cinco minutos al cierre para todos, no equipo por equipo.

Referencia de slides: `Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Integrar diagramas v1 + checklist de avance PI**.
Entregable concreto: Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿en qué quedó su CloudLite la clase pasada?» — sirve para detectar equipos rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller)
Cubre estos conceptos, en este orden, ~10 min cada uno (son los títulos de las diapositivas de teoría):
- Checklist de avance (obligatorio)
- Errores frecuentes a corregir
- Rúbrica (recordatorio)

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un equipo voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo
Herramienta del día: **draw.io · GitHub · Google Docs**.
**Demo que usted debe poder repetir:** Auditar en vivo el paquete de un equipo voluntario

1. Pida a un equipo que proyecte su C4 Containers y su diagrama de despliegue lado a lado.
2. Compare nombre por nombre: todo servicio del Containers debe existir en el despliegue y viceversa.
3. Senale en voz alta el primer gap concreto que encuentre y escribalo como accion con responsable y fecha.
4. Modele el tono: el hallazgo es sobre el artefacto, nunca sobre la persona.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 11/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»


### 55–100 · Taller guiado PI (equipos)
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 11/Quiz Clase 11 - Avance del proyecto final.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 equipos en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre
Di: «Queda avanzado: Integrar diagramas v1 + checklist de avance PI.
Criterio de éxito: cualquier integrante explica el artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Completen el checklist en el informe (sí/no + enlace evidencia).
2. Unifiquen nombres entre C4 y Deployment.
3. Empaqueten ZIP/repo: diagramas PNG, Dockerfile, YAML, informe.
4. Feedback docente 1:1 corto (cola).
5. Backlog escrito: 5 ítems para Clase 12.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Traer el paquete de la Clase 1 sin actualizar y presentarlo como avance. Compare contra la version anterior.
- Un solo integrante conoce el paquete completo. Pregunte al azar; si solo uno responde, ese es el hallazgo principal.
- Confundir este checkpoint con la sustentacion final o con el Parcial 3. Aclarelo al abrir la sesion.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que gap concreto identificaron hoy y quien lo cierra?
1. Su diagrama de despliegue usa los mismos nombres que su C4 Containers?
1. Que evidencia de la rubrica les falta todavia?

## Solución del taller (privada)
`Kit docente/Clase 11/Solucion Taller Clase 11 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los equipos. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 11/Quiz Clase 11 - Avance del proyecto final.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 11/Quiz Clase 11 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase11.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (https://examlab.lovable.app/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
