# Guia docente · Clase 9 · Parcial 2 (solo evaluacion)

> Dia de **parcial = solo evaluacion**. No hay tema nuevo ni avance de PI en clase.
> Bloque **120 min** · **virtual sincrona por Google Meet**.
> Enunciado: `Parciales/Parcial 2 - Optimizacion indices y transacciones.docx` · la solucion es el mismo nombre con
> «- SOLUCION» y **no se publica** en `Clases/`.

## Que evalua el instrumento

Solo estas clases de material (asi las lista la portada del enunciado):

- Clase 6 · 28/09 · Optimización de consultas
- Clase 7 · 05/10 · Índices y particionamiento (sesión doble)
- Clase 8 · 05/10 · Tuning de bases de datos · Gestión de transacciones (sesión doble)
- Clase 10 · 12/10 · Control de concurrencia (sesión autónoma)

Sus cuatro secciones y lo que vale cada una:

- A. Selección múltiple — 20 pts
- B. Emparejamiento — 20 pts
- C. Optimización SQL — 25 pts
- D. Caso transacciones, tuning y concurrencia — 35 pts

Total **100 puntos** · nota = puntos / 20 sobre 5.0 · peso **10% del Corte 2 (30%)** ·
fecha **19/10/2026** · tiempo de resolucion previsto **90–100 minutos**.

## Antes de abrir la sesion (10 min)

1. Abre `Parciales/Parcial 2 - Optimizacion indices y transacciones.docx` y **decide el canal de entrega**. El enunciado
   remite a «el medio que el docente indique al abrir la sesion», asi que si no lo
   decides tu, no existe. Lo que funciona en Meet:
   - **Documento editable** (recomendado): compartes el .docx por el chat al minuto 0,
     cada estudiante lo llena y lo devuelve por el mismo canal o por correo. El SQL se
     escribe como texto; **no** se pide captura de ejecucion en el parcial.
   - **Foto de hoja escrita a mano**: solo como plan B si a alguien no le abre el
     documento. Exige que se lea y que traiga nombre en cada pagina.
2. Ten la solucion **a la mano pero cerrada**: hoy no se califica en vivo, y menos con
   la pantalla compartida.
3. Revisa que el enunciado no pregunte nada fuera de las Clases 6, 7, 8 y 10. Si algo se cuela
   de otro corte se anula esa pregunta y se reparten sus puntos, no se descuenta.

## Checklist 120 min

| Min | Accion |
|---|---|
| 0-10 | Asistencia por lista. Proyecta la **diapositiva 2** (alcance y reparto de puntos, que es lo primero que preguntan) y luego la **diapositiva 3**. Anuncia: canal de entrega, cierre en el minuto 110, que material esta autorizado (por defecto **nada**) y que las dudas de contenido no se responden. |
| 10-15 | Comparte el enunciado y **confirma en voz alta que todos lo abrieron** antes de arrancar el reloj. Deja la **diapositiva 3** en pantalla: ahorra la mitad de los mensajes por privado. |
| 15-100 | Desarrollo (silencio de evaluacion). Camara y microfono abiertos: es la unica supervision que hay. Avisa el tiempo a los 50 y a los 80 minutos. |
| 100-110 | Aviso de 10 min. Recibe las entregas y **acusa recibo por el chat, uno por uno**. Anota quien no entrego. |
| 110-120 | Cierre. «El PI VetCare continúa en la siguiente clase; hoy no hay tarea nueva.» Sin comentarios sobre el parcial: todavia hay quien esta subiendo el archivo. |

## Que se responde y que no durante el parcial

La linea es una sola: **si la respuesta a la duda es un dato que la pregunta evalua, no se responde.**

- Se responde: «¿esto pide una consulta o una explicacion?», «¿cuantas lineas?», «¿el
  punto b) es obligatorio?», «no puedo abrir el archivo».
- No se responde, en este parcial: «¿que nivel de aislamiento evita la lectura fantasma?» · «¿que es un deadlock?» · «¿esta opcion es la correcta?».

Cuando la duda es de contenido, la respuesta es siempre la misma: «Eso es lo que la
pregunta evalua; responde con lo que recuerdes de la clase.» Dila igual para todos: en
Meet las preguntas llegan por privado y nadie ve que a otro le dijiste lo mismo.

## Errores tipicos del docente que no domina el tema

- **Responder la duda de contenido porque parece inofensiva.** «¿que nivel de aislamiento evita la lectura fantasma?» es
  literalmente la respuesta de una pregunta de este parcial.
- **No decidir el canal de entrega antes de empezar.** Si no lo anunciaste al minuto 0,
  lo vas a improvisar al minuto 105 con medio grupo escribiendo por privado.
- **No acusar recibo.** Es la fuente numero uno de reclamos de un parcial virtual y se
  resuelve escribiendo el nombre de cada uno en el chat cuando llega su archivo.
- **Exigir salida de ejecucion.** El parcial se responde con SQL escrito; ExamLab no
  interviene y nadie tiene que abrir un motor. Si un estudiante escribe una consulta
  correcta con un nombre de tabla que no existe en el enunciado, se descuenta por el
  nombre, no por la consulta.
- **Descontar por el termino de manual.** Antes de restar puntos por una palabra que el
  estudiante no uso, busca la diapositiva donde se proyecto. Vale la respuesta que
  describe el mecanismo correcto aunque no lo nombre.
- **Sintaxis de otro motor.** Las clases se dictan sobre **PostgreSQL**; una respuesta
  con sintaxis de Oracle que expresa bien la idea no pierde los puntos del concepto.
- **Tratar el dia como clase.** Ni tema nuevo, ni avance del PI, ni «aprovechemos que
  terminaron temprano».

## Preguntas frecuentes del grupo

**¿Puedo usar mis apuntes?** Lo que digas al minuto 0 y nada mas. Por defecto: no.
Decidelo antes de abrir la sesion: cambiarlo a mitad del parcial invalida el de quien ya
respondio sin ellos.

**¿Se me cayo el internet?** Que siga respondiendo el documento sin conexion y te escriba
por correo al reconectarse. El tiempo perdido por una caida comprobable no se descuenta, y
el criterio se anuncia al minuto 0 para que nadie lo use como excusa despues.

**¿Entra lo de la Clase 10?** Si, es lo mas reciente que entra y se evalua igual, aunque se haya trabajado sin sesion en vivo: es la que mas se olvida al estudiar. La portada del
enunciado lista las clases evaluadas con su fecha; fuera de esa lista no hay nada.

**¿Tengo que ejecutar el SQL?** No. Se responde escrito y se califica la logica de la
consulta: los alias, el JOIN, el WHERE, el orden. No se pide captura.

**¿Cuanto vale cada seccion?** Esta en la portada: A. Selección múltiple — 20 pts · B. Emparejamiento — 20 pts · C. Optimización SQL — 25 pts · D. Caso transacciones, tuning y concurrencia — 35 pts.
Total 100 puntos, nota = puntos / 20.

**¿Cuanto tiempo tengo?** El instrumento preve 90–100 minutos y el bloque son 120: hay
holgura, pero el envio cierra en el minuto 110 y eso no se mueve.

**¿Cuando veo la nota?** En la siguiente sesion, con la retroalimentacion escrita sobre el
mismo documento que entregaste.

## Notas

- No mezclar «Tema · Parcial»: hoy no se dicta nada.
- Hoy no se avanza en el PI: se retoma en la **Clase 10** (sesion autonoma). La preparacion de la presentacion es la **Clase 12** y la sustentacion la **Clase 15**.
- Solucion privada: archivo «- SOLUCION.docx» en `Parciales/`, nunca en `Clases/`.
