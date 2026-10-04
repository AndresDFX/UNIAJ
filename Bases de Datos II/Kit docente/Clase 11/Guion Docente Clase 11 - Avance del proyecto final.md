# Guion docente · Clase 11 · Avance PI · VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Demo parcial + checklist de avance (hito formal PI)
- **Entregable de hoy:** Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
- **Herramienta:** Live SQL / DB Fiddle + draw.io + ExamLab
- **Slides:** Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Que es una revision tecnica, y con que producto se sale** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Una revision tecnica es una reunion con un proposito unico: encontrar defectos en un artefacto antes de que cuesten caro, y salir con un producto escrito.
  - No es una reunion de avance, no es una calificacion y no es una demostracion para lucirse.
  - La practica tiene nombres y roles establecidos desde hace decadas en ingenieria de software: el autor presenta, uno o mas revisores buscan defectos, un moderador cuida el tiempo y el tono, y un escriba registra los hallazgos.
  - El estandar clasico, IEEE 1028, distingue la inspeccion (formal, con lista de verificacion y metricas), el walkthrough (el autor guia y explica) y la revision tecnica propiamente dicha (los pares evaluan si el artefacto sirve para su proposito).
  - NOTAS:
  - Lo que se hace hoy es una revision tecnica con lista de verificacion, comprimida a diez minutos por estudiante.
  - Dos reglas gobiernan la sesion y hay que decirlas en voz alta antes de empezar: se revisa el artefacto y no la persona, y no se resuelve el problema dentro de la revision, solo se registra.
  - Un estudiante que se pone a corregir el DDL en vivo consume el tiempo de los demas y sale con un hallazgo menos que si hubiera seguido escuchando.

**[Slide 5] Lo que se audita es la coherencia entre piezas** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un artefacto es cualquier producto de trabajo: el diagrama entidad-relacion, el script DDL, la matriz de roles, los procedimientos, el informe de optimizacion.
  - Es perfectamente posible que un estudiante tenga un ER bien dibujado, un DDL que ejecuta sin errores
  - Y que ambos describan bases de datos distintas, porque el ER se dibujo en la Clase 1 y el DDL se fue parchando en las Clases 3 a 8 sin volver a actualizar el diagrama.
  - Cada una toma dos o tres minutos si se ejecuta con criterio.
  - NOTAS:
  - Lo que se audita en una base de datos no es cada pieza por separado sino la coherencia entre piezas.
  - Coherencia significa que todas esas piezas describen el mismo sistema.
  - Esa divergencia es el hallazgo mas comun del checkpoint y tambien el mas facil de detectar si se sabe donde mirar.
  - Las cuatro verificaciones cruzadas que el docente debe correr son: que el DDL corresponda al ER, que los GRANT correspondan a los roles declarados, que los procedimientos listados existan y sean invocables, y que la optimizacion tenga medicion antes y despues.
  - Fuera de la lamina (habla de la practica): Cada una toma dos o tres minutos si se ejecuta con criterio, y juntas cubren los cuatro criterios de rubrica que mas peso tienen.

**[Slide 6] Verificaciones uno y dos: el ER contra el DDL** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Se recorre el diagrama entidad por entidad y se busca su CREATE TABLE: toda entidad sin tabla es un hallazgo.
  - Luego se recorre en sentido contrario, porque es el que nadie hace: toda tabla sin entidad en el diagrama tambien es un hallazgo, ya que significa que el modelo crecio sin registrarse.
  - Si el ER dice que una cita pertenece a exactamente una mascota, el DDL debe tener id_mascota con NOT NULL y una FOREIGN KEY hacia Mascota
  - Si dice que un dueno puede tener varias mascotas pero una mascota tiene un solo dueno, la clave foranea vive en Mascota y no en Dueno.
  - Una cardinalidad dibujada que no tiene su restriccion correspondiente en el DDL es decoracion, no modelo.
  - Se toma la matriz de la Clase 2 y se comprueba que los cuatro roles declarados existan en el script y que las celdas se hayan traducido en sentencias.
  - El hallazgo tipico aqui es el rol AUDITOR que en la matriz solo lee y en el script recibio privilegios de escritura, porque alguien copio el bloque de RECEPCION y cambio unicamente el nombre.
  - NOTAS:
  - Verificacion uno, ER contra DDL.
  - Despues se verifican las relaciones.
  - Verificacion dos, roles contra GRANT.

**[Slide 7] Verificacion tres: que compile no es que sirva** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La distincion que separa a un estudiante que va bien de uno que va mal es esta: un procedimiento que compila no es un procedimiento que funciona.
  - Primero CALL sp_agendar_cita con datos validos, que debe insertar la cita y devolver confirmacion.
  - Segundo, CALL sp_agendar_cita con el caso invalido que el propio estudiante declaro, es decir una mascota inactiva o un horario ya tomado, que debe devolver el mensaje de negocio y no un error crudo del motor.
  - Si el estudiante no puede mostrar la segunda ejecucion.
  - Un informe de optimizacion sin medicion no es optimizacion, es una opinion.
  - Si el estudiante creo tres indices y no puede senalar cual consulta aprovecha cada uno, el hallazgo es que indexo por costumbre y no por medicion, que es exactamente el error que se analiza como caso real en la Clase 13.
  - Ejemplo: un sp_agendar_cita que compila pero no valida la mascota inactiva pasa la primera ejecucion y falla la segunda, la que deberia haber sido rechazada.
  - NOTAS:
  - Verificacion tres, procedimientos invocables.
  - La prueba de humo dura un minuto y consiste en pedir dos ejecuciones y no una.
  - Verificacion cuatro, optimizacion.
  - Se exige la consulta original, el plan de ejecucion que la acompanaba, el cambio aplicado (indice creado o consulta reescrita) y el plan despues, mostrando que el motor paso de recorrido completo de tabla a acceso por indice.
  - Fuera de la lamina (habla de la practica): Si el estudiante no puede mostrar la segunda ejecucion, el procedimiento no tiene manejo de errores y eso resta puntos en los 25 de objetos programables.

**[Slide 8] La bateria de verificacion del avance** — 11 vinetas.

**[Slide 9] Scope creep: el crecimiento no controlado del alcance** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Scope creep es el crecimiento no controlado del alcance: funcionalidad que se va agregando sin que nadie decida agregarla y sin que se quite nada a cambio.
  - En un proyecto de base de datos tiene un sintoma cuantificable, que es el numero de entidades. la clínica pide seis entidades minimas (Dueno, Mascota, Veterinario, Cita
  - Insumo y Factura con su detalle) y el rango sano al llegar a la Clase 11 es de seis a nueve, contando una o dos ampliaciones propias justificadas como Consulta o historial clinico.
  - Un estudiante que llega con quince entidades porque agrego proveedores, inventario multialmacen, portal para duenos y notificaciones no esta adelantado: esta repartiendo el mismo esfuerzo en el doble de superficie
  - Y termina con quince tablas vacias en vez de siete tablas con procedimientos probados.
  - La accion correctiva es explicita y se registra en el acta: las entidades que sobran se mueven a una seccion de alcance futuro del informe, con una frase que diga por que quedaron fuera.
  - NOTAS:
  - Existe tambien el problema inverso y menos visible.
  - Fuera de la lamina (habla de la practica): La rubrica no da puntos por cantidad de tablas: da 20 por modelo coherente y 25 por objetos programables con casos de prueba.
  - Fuera de la lamina (habla de la practica): Eso no resta puntos, al contrario, declarar el limite es una senal de madurez que se valora en la sustentacion.
  - Fuera de la lamina (habla de la practica): Existe tambien el problema inverso y menos visible: el estudiante que recorto tanto que ya no tiene material para los 25 puntos de procedimientos, funciones y disparadores, y ese caso tambien es un hallazgo que hay que escribir.

**[Slide 10] La anatomia fija de la retroalimentacion util** — 3 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La retroalimentacion util tiene una anatomia fija, y conviene que el docente la escriba siempre igual porque asi el acta se vuelve una lista de tareas y no un desahogo.
  - Un hallazgo bien formulado tiene cinco partes: artefacto, observacion verificable, impacto, accion y responsable con fecha.
  - Retroalimentacion inutil: «el modelo esta flojo, mejorenlo»; no dice que mirar ni como saber cuando esta resuelto.
  - Retroalimentacion accionable: «Artefacto: script DDL.
  - Observacion: la tabla detalle_factura no tiene FOREIGN KEY hacia insumo, aunque el ER dibuja la relacion.
  - Impacto: se pueden insertar detalles con insumos que no existen.
  - Accion: agregar la restriccion y volver a ejecutar el script completo desde cero en un entorno limpio.
  - Fecha: antes de la Clase 12.» La diferencia entre las dos no es cortesia, es verificabilidad: el segundo hallazgo se puede cerrar y cualquiera puede comprobar que se cerro.
  - La regla de dosificacion es de tres a cinco hallazgos por estudiante.
  - NOTAS:
  - Comparense los dos extremos.
  - Responsable: Carlos.
  - Fuera de la lamina (habla de la practica): Impacto: se pueden insertar detalles con insumos que no existen; afecta los 20 puntos de modelo coherente.
  - Fuera de la lamina (habla de la practica): La regla de dosificacion es de tres a cinco hallazgos por estudiante, priorizados por puntos de rubrica en riesgo; mas de cinco desmoraliza y nadie los cierra, y menos de tres casi siempre significa que la revision fue superficial.

**[Slide 11] Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado, y esa afirmacion merece justificacion porque suena severa.
  - El unico valor de un punto de control intermedio es que todavia existe tiempo para corregir, y ese valor se realiza solo si de la sesion sale una lista escrita de cosas por corregir.
  - Cuando el docente dice «todo bien, sigan asi», el estudiante interpreta legitimamente que su trabajo esta aprobado, deja de revisarlo, y el defecto reaparece en la entrega final cuando ya no hay clases para arreglarlo: es un costo diferido, no un ahorro.
  - La primera: «esto tiene nota?».
  - La segunda: «si quien me audita encuentra fallas, me baja la nota?».
  - Y revisar el trabajo de otro tiene un beneficio propio bien documentado: los defectos ajenos se ven mucho mas rapido que los propios, y casi siempre quien audita vuelve a su carpeta y arregla en silencio el mismo problema que acaba de senalar.
  - Todo esto se apoya en lo hecho hasta la Clase 10 (el informe de escenarios de concurrencia es una de las evidencias que hoy se audita) y alimenta directamente la Clase 12
  - Donde el contrato de operaciones solo puede escribirse sobre procedimientos que existan y funcionen, y la Clase 15, donde se sustenta.
  - NOTAS:
  - Aqui aparecen las dos preguntas previsibles del estudiante.
  - Fuera de la lamina (habla de la practica): La respuesta es que el checkpoint en si no califica el producto, pero es la ultima oportunidad de mover puntos de la rubrica antes de la entrega, y por eso conviene llegar con lo peor y no con lo mejor: un estudiante que esconde su parte floja para no verse mal pierde justamente la revision que la habria arreglado.
  - Fuera de la lamina (habla de la practica): No, porque el auditor par no califica.

**[Slide 12] Integridad y objetos de negocio, contados** — 14 vinetas.


**Demo que usted debe poder repetir:** Recorrido de checklist + ejemplo demo de 3 min.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 11 · Avance proyecto · la base de la clínica
2. Encuadre de hoy · Tema y objetivo
3. Mapa del bloque de hoy (120 min)
4. Que es una revision tecnica, y con que producto se sale
5. Lo que se audita es la coherencia entre piezas
6. Verificaciones uno y dos: el ER contra el DDL
7. Verificacion tres: que compile no es que sirva
8. La bateria de verificacion del avance
9. Scope creep: el crecimiento no controlado del alcance
10. La anatomia fija de la retroalimentacion util
11. Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado
12. Integridad y objetos de negocio, contados
13. Demo del dia
14. Del boceto al código Mermaid
15. Cierre · Clase 11

> Privado, no se proyecta: `Kit docente/Clase 11/Solucion Taller Clase 11 - VetCare.docx`

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre · [Slide 2][Slide 3]
**Decir:** «Buenas. Hoy el hilo es VetCare DB y el tema es: Avance PI · VetCare DB.»
Proyectar [Slide 2] «Encuadre de hoy · Tema y objetivo» y [Slide 3] «Mapa del bloque de hoy».
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve) · desde 
**Decir:** «Esto es lo que hay que saber del tema de hoy.»
Proyecte estas diapositivas, en este orden, ~25 min cada una. Son la teoria
completa del dia: **ninguna se salta**, porque el taller cobra puntos por lo que se
proyecta en todas ellas.


El desarrollo completo de cada una esta arriba, en «Fundamento teorico», dividido por
diapositiva: esa seccion esta escrita para dictarla sin consultar otra fuente.
Ideas que tienen que quedar dichas:
- Hoy no hay tema nuevo: se cierran huecos del PI con rubrica.
- Evidencias: ER, DDL, roles, >=2 procs, >=1 fn, >=2 triggers, 1 opt.
- Revision cruzada entre estudiantes: 10 min por persona.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso · [Slide 13][Slide 14]
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Recorrido de checklist + ejemplo demo de 3 min.
Herramienta: Live SQL / DB Fiddle + draw.io + ExamLab

**Cierre la demo dentro de ExamLab** [Slide 14] — es la parte que el estudiante no adivina: pase el boceto a codigo Mermaid con ayuda de una IA, peguelo en la pregunta de diagrama y muestrelo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `erDiagram`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.
📸 Salida esperada de la demo de la Clase 11 [[captura: cap01_demo.png | receta: 1) Abra Live SQL / DB Fiddle + draw.io + ExamLab y repita la demo de este bloque sobre el dominio VetCare (no otro ejemplo).  2) Capture la ventana en el momento en que se ve el resultado, no el escritorio completo.  3) Recorte a ~1200 px de ancho.  4) Guardela como Kit docente/Clase 11/Capturas/cap01_demo.png.  5) Vuelva a generar el guion: la imagen queda embebida aqui sola.]]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Practica (opcional) · sin lamina
La practica es **opcional** y **no se proyecta**: a veces se hace en clase, a veces no. La guia
completa (contexto, escenario, pasos, pistas, plantilla y criterios) esta en `Clases/Clase 11 - Avance del proyecto final/Taller PI - Clase 11 - VetCare.docx`.
Si hoy se hace, el estudiante la abre desde la carpeta de la clase. Solucion en Kit docente/Solucion Taller... (no proyectar).
Si se hace, avanza el PI en: Demo parcial + checklist de avance (hito formal PI)
Actividades:
1. Completar checklist de avance (si/no/parcial).
2. Demo 3-5 min: ER + 1 proc + 1 trigger.
3. Lista de gaps con responsable.
4. Subir avance intermedio a ExamLab (Talleres) si se pide.
Circular por estudiantes (o salas). Empujar evidencia, no perfectionismo.
Entregable: Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
📸 Evidencia de avance de un estudiante (para su registro del corte) [[captura: cap02_taller.png | receta: 1) Con permiso del estudiante, capture SU pantalla con el artefacto de hoy a medio construir.  2) Recorte datos personales (nombre, correo) antes de guardar.  3) Guardela como Kit docente/Clase 11/Capturas/cap02_taller.png.  4) Sirve de referencia del nivel esperado en el proximo semestre; no se proyecta.]]

### 105-115 · Repaso + quiz corto
Repasar los conceptos del dia volviendo a las laminas de teoria que mas costaron.
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 11 - VetCare.docx`. Clave para usted: `Quiz Clase 11 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre · [Slide 15]
**Decir:** «Queda visto: Avance PI · VetCare DB. Si hicimos la practica, la guia y la entrega estan en la carpeta de la clase.»
Proyectar [Slide 15] slide de cierre. Dudas finales.


## Reparto del bloque y logistica (no se proyecta)

### La aritmetica del calendario, dicha en voz alta

Para decidir si un estudiante va a tiempo hay que hacer la aritmetica del calendario en voz alta, porque los estudiantes casi siempre creen que tienen mas tiempo del que tienen, y este semestre la cuenta es mas dura de lo que parece. Quedan cuatro Clases de material pero solo tres bloques mas de clase, y ninguno de los tres es de trabajo acompanado. La razon: este checkpoint cae en una sesion doble que continua el mismo dia con la Clase 12, la de integracion aplicacion-base de datos; despues viene la Clase 13, de casos reales, que es autonoma por festivo y el estudiante hace solo; luego el Parcial 3, que es solo evaluacion; y finalmente la sesion de cierre, que es la sustentacion en vivo del proyecto. Dicho de frente al grupo: hoy es la ultima vez que el docente revisa el proyecto con ellos delante, y lo que salga mal de aqui en adelante se corrige por cuenta propia, con retroalimentacion escrita entre sesiones. Con ese dato, el umbral razonable a esta altura es tener cerrados los 20 puntos de modelo mas DDL y los 15 de seguridad y respaldo, o sea 35 de los 100, y tener al menos la mitad de los 25 de objetos programables: dos procedimientos, uno de ellos probado con su caso invalido. Con ese criterio el semaforo es objetivo y se puede decir a la cara sin que suene arbitrario. Verde: modelo cerrado, roles definidos, dos procedimientos que ejecutan y una consulta optimizada con medicion. Amarillo: modelo cerrado pero procedimientos que compilan sin pruebas, o roles que solo existen en papel. Rojo: ER que aun cambia semana a semana, o DDL que no ejecuta de principio a fin en un entorno limpio. A un estudiante en rojo no se le pide que avance; se le pide que congele el alcance hoy mismo y dedique la semana a cerrar el DDL, porque sin una base ejecutable no hay nada sobre lo que montar procedimientos, disparadores ni optimizacion.

## Codigo / scripts
Carpeta Codigo/ — archivo 11_checklist_seed.sql.

## Capturas
Carpeta `Kit docente/Clase 11/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
