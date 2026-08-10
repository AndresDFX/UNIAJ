# Guion docente · Clase 11 · Avance PI · VetCare DB

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** REGULAR
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy avanzamos el PI en:** Demo parcial + checklist de avance (hito formal PI)
- **Entregable de hoy:** Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
- **Herramienta:** Live SQL / DB Fiddle + draw.io + ExamLab
- **Slides:** Clases/Clase 11 - Avance del proyecto final/Presentacion.pptx

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.

- Hoy no hay tema nuevo: se cierran huecos del PI con rubrica.
- Evidencias: ER, DDL, roles, >=2 procs, >=1 fn, >=2 triggers, 1 opt.
- Feedback entre pares: 10 min por equipo.

### Desarrollo del tema (para dictar sin consultar otra fuente)

Una revision tecnica es una reunion con un proposito unico: encontrar defectos en un artefacto antes de que cuesten caro, y salir con un producto escrito. No es una reunion de avance, no es una calificacion y no es una demostracion para lucirse. La practica tiene nombres y roles establecidos desde hace decadas en ingenieria de software: el autor presenta, uno o mas revisores buscan defectos, un moderador cuida el tiempo y el tono, y un escriba registra los hallazgos. El estandar clasico, IEEE 1028, distingue la inspeccion (formal, con lista de verificacion y metricas), el walkthrough (el autor guia y explica) y la revision tecnica propiamente dicha (los pares evaluan si el artefacto sirve para su proposito). Lo que se hace hoy es una revision tecnica con lista de verificacion, comprimida a diez minutos por equipo. Dos reglas gobiernan la sesion y hay que decirlas en voz alta antes de empezar: se revisa el artefacto y no la persona, y no se resuelve el problema dentro de la revision, solo se registra. Un equipo que se pone a corregir el DDL en vivo consume el tiempo de los demas y sale con un hallazgo menos que si hubiera seguido escuchando.

Lo que se audita en una base de datos no es cada pieza por separado sino la coherencia entre piezas. Un artefacto es cualquier producto de trabajo entregable: el diagrama entidad-relacion, el script DDL, la matriz de roles, los procedimientos, el informe de optimizacion. Coherencia significa que todas esas piezas describen el mismo sistema. Es perfectamente posible que un equipo tenga un ER bien dibujado, un DDL que ejecuta sin errores, y que ambos describan bases de datos distintas, porque el ER se dibujo en la Clase 1 y el DDL se fue parchando en las Clases 3 a 8 sin volver a actualizar el diagrama. Esa divergencia es el hallazgo mas comun del checkpoint y tambien el mas facil de detectar si se sabe donde mirar. Las cuatro verificaciones cruzadas que el docente debe correr son: que el DDL corresponda al ER, que los GRANT correspondan a los roles declarados, que los procedimientos listados existan y sean invocables, y que la optimizacion tenga medicion antes y despues. Cada una toma dos o tres minutos si se ejecuta con criterio, y juntas cubren los cuatro criterios de rubrica que mas peso tienen.

Verificacion uno, ER contra DDL. Se recorre el diagrama entidad por entidad y se busca su CREATE TABLE: toda entidad sin tabla es un hallazgo. Luego se recorre en sentido contrario, porque es el que nadie hace: toda tabla sin entidad en el diagrama tambien es un hallazgo, ya que significa que el modelo crecio sin registrarse. Despues se verifican las relaciones. Si el ER dice que una cita pertenece a exactamente una mascota, el DDL debe tener id_mascota con NOT NULL y una FOREIGN KEY hacia Mascota; si dice que un dueno puede tener varias mascotas pero una mascota tiene un solo dueno, la clave foranea vive en Mascota y no en Dueno. Una cardinalidad dibujada que no tiene su restriccion correspondiente en el DDL es decoracion, no modelo. Verificacion dos, roles contra GRANT. Se toma la matriz de la Clase 2 y se comprueba que los cuatro roles declarados existan en el script y que las celdas se hayan traducido en sentencias. El hallazgo tipico aqui es el rol AUDITOR que en la matriz solo lee y en el script recibio privilegios de escritura, porque alguien copio el bloque de RECEPCION y cambio unicamente el nombre.

Verificacion tres, procedimientos invocables. La distincion que separa a un equipo que va bien de uno que va mal es esta: un procedimiento que compila no es un procedimiento que funciona. La prueba de humo dura un minuto y consiste en pedir dos ejecuciones y no una. Primero CALL sp_agendar_cita con datos validos, que debe insertar la cita y devolver confirmacion. Segundo, CALL sp_agendar_cita con el caso invalido que el propio equipo declaro, es decir una mascota inactiva o un horario ya tomado, que debe devolver el mensaje de negocio y no un error crudo del motor. Si el equipo no puede mostrar la segunda ejecucion, el procedimiento no tiene manejo de errores y eso resta puntos en los 25 de objetos programables. Verificacion cuatro, optimizacion. Un informe de optimizacion sin medicion no es optimizacion, es una opinion. Se exige la consulta original, el plan de ejecucion que la acompanaba, el cambio aplicado (indice creado o consulta reescrita) y el plan despues, mostrando que el motor paso de recorrido completo de tabla a acceso por indice. Si el equipo creo tres indices y no puede senalar cual consulta aprovecha cada uno, el hallazgo es que indexo por costumbre y no por medicion, que es exactamente el error que se analiza como caso real en la Clase 13.

Scope creep es el crecimiento no controlado del alcance: funcionalidad que se va agregando sin que nadie decida agregarla y sin que se quite nada a cambio. En un proyecto de base de datos tiene un sintoma cuantificable, que es el numero de entidades. VetCare pide seis entidades minimas (Dueno, Mascota, Veterinario, Cita, Insumo y Factura con su detalle) y el rango sano al llegar a la Clase 11 es de seis a nueve, contando una o dos ampliaciones propias justificadas como Consulta o historial clinico. Un equipo que llega con quince entidades porque agrego proveedores, inventario multialmacen, portal para duenos y notificaciones no esta adelantado: esta repartiendo el mismo esfuerzo en el doble de superficie, y termina con quince tablas vacias en vez de siete tablas con procedimientos probados. La rubrica no da puntos por cantidad de tablas: da 20 por modelo coherente y 25 por objetos programables con casos de prueba. La accion correctiva es explicita y se registra en el acta: las entidades que sobran se mueven a una seccion de alcance futuro del informe, con una frase que diga por que quedaron fuera. Eso no resta puntos, al contrario, declarar el limite es una senal de madurez que se valora en la sustentacion. Existe tambien el problema inverso y menos visible: el equipo que recorto tanto que ya no tiene material para los 25 puntos de procedimientos, funciones y disparadores, y ese caso tambien es un hallazgo que hay que escribir.

La retroalimentacion util tiene una anatomia fija, y conviene que el docente la escriba siempre igual porque asi el acta se vuelve una lista de tareas y no un desahogo. Un hallazgo bien formulado tiene cinco partes: artefacto, observacion verificable, impacto, accion y responsable con fecha. Comparense los dos extremos. Retroalimentacion inutil: «el modelo esta flojo, mejorenlo»; no dice que mirar ni como saber cuando esta resuelto. Retroalimentacion accionable: «Artefacto: script DDL. Observacion: la tabla detalle_factura no tiene FOREIGN KEY hacia insumo, aunque el ER dibuja la relacion. Impacto: se pueden insertar detalles con insumos que no existen; afecta los 20 puntos de modelo coherente. Accion: agregar la restriccion y volver a ejecutar el script completo desde cero en un entorno limpio. Responsable: Carlos. Fecha: antes de la Clase 12.» La diferencia entre las dos no es cortesia, es verificabilidad: el segundo hallazgo se puede cerrar y cualquiera puede comprobar que se cerro. La regla de dosificacion es de tres a cinco hallazgos por equipo, priorizados por puntos de rubrica en riesgo; mas de cinco desmoraliza y nadie los cierra, y menos de tres casi siempre significa que la revision fue superficial.

Para decidir si un equipo va a tiempo hay que hacer la aritmetica del calendario en voz alta, porque los estudiantes casi siempre creen que tienen mas tiempo del que tienen. Al terminar la Clase 11 quedan cuatro clases: la 12 de integracion, la 13 de casos reales, la 14 que es el Parcial 3 y la 15 que es entrega y sustentacion, y esta ultima es autonoma por festivo. Es decir, quedan aproximadamente dos sesiones utiles de trabajo acompanado. Con ese dato, el umbral razonable a esta altura es tener cerrados los 20 puntos de modelo mas DDL y los 15 de seguridad y respaldo, o sea 35 de los 100, y tener al menos la mitad de los 25 de objetos programables: dos procedimientos, uno de ellos probado con su caso invalido. Con ese criterio el semaforo es objetivo y se puede decir a la cara sin que suene arbitrario. Verde: modelo cerrado, roles definidos, dos procedimientos que ejecutan y una consulta optimizada con medicion. Amarillo: modelo cerrado pero procedimientos que compilan sin pruebas, o roles que solo existen en papel. Rojo: ER que aun cambia semana a semana, o DDL que no ejecuta de principio a fin en un entorno limpio. A un equipo en rojo no se le pide que avance; se le pide que congele el alcance hoy mismo y dedique la semana a cerrar el DDL, porque sin una base ejecutable no hay nada sobre lo que montar procedimientos, disparadores ni optimizacion.

Un checkpoint sin hallazgos concretos es un checkpoint desperdiciado, y esa afirmacion merece justificacion porque suena severa. El unico valor de un punto de control intermedio es que todavia existe tiempo para corregir, y ese valor se realiza solo si de la sesion sale una lista escrita de cosas por corregir. Cuando el docente dice «todo bien, sigan asi», el equipo interpreta legitimamente que su trabajo esta aprobado, deja de revisarlo, y el defecto reaparece en la entrega final cuando ya no hay clases para arreglarlo: es un costo diferido, no un ahorro. Aqui aparecen las dos preguntas previsibles del estudiante. La primera: «esto tiene nota?». La respuesta es que el checkpoint en si no califica el producto, pero es la ultima oportunidad de mover puntos de la rubrica antes de la entrega, y por eso conviene llegar con lo peor y no con lo mejor: un equipo que esconde su parte floja para no verse mal pierde justamente la revision que la habria arreglado. La segunda: «si el equipo que nos audita nos encuentra fallas, nos baja la nota?». No, porque el auditor par no califica. Y revisar a otro equipo tiene un beneficio propio bien documentado: los defectos ajenos se ven mucho mas rapido que los propios, y casi siempre el equipo auditor vuelve a su carpeta y arregla en silencio el mismo problema que acaba de senalar. Todo esto se apoya en lo hecho hasta la Clase 10 (el informe de escenarios de concurrencia es una de las evidencias que hoy se audita) y alimenta directamente la Clase 12, donde el contrato de operaciones solo puede escribirse sobre procedimientos que existan y funcionen, y la Clase 15, donde se sustenta.

Error tipico del docente que no domina el tema: el primero es dar retroalimentacion global y amable, del tipo «va bien, faltan detalles», porque revisar en serio incomoda y a esta altura del semestre el grupo esta cansado. La consecuencia aguas abajo es que los defectos de coherencia entre ER y DDL llegan intactos a la Clase 15, cuando ya no se pueden corregir, y se descuentan sobre los 20 puntos de modelo con un equipo que reclama, con razon, que nadie se lo dijo cuando habia tiempo. El segundo error es aceptar como evidencia lo que el equipo dice en vez de lo que el equipo muestra: creer que el procedimiento funciona porque el vocero afirma que funciona, sin pedir la ejecucion con el caso invalido. La consecuencia es un checkpoint marcado en verde para un equipo que en realidad esta en amarillo, y una sorpresa desagradable el dia de la entrega, cuando ya no hay margen. Un tercer tropiezo muy frecuente: convertir el checkpoint en una clase magistral de repaso porque incomoda no tener tema nuevo que dictar; el tiempo se consume explicando, ningun equipo sale con su acta de gaps escrita, y el acta era el unico entregable del dia.


**Demo que usted debe poder repetir:** Recorrido de checklist + ejemplo demo de 3 min.

## Referencias a diapositivas
1. Slide 1 portada (Clase N + titulo VetCare)
2. Slide Agenda 120 min
3. Slide Objetivo PI de la clase
4. Slide Teoria Core
5. Slide Demo del dia
6. Slide Herramientas de hoy (logos 3-4)
7. Bloque Taller ampliado: contexto / objetivo / escenario / pasos / pistas
8. Slide Criterios de exito / entregable
9. Slide Para el PI esta semana
10. Slide Cierre
11. Solucion PRIVADA: Kit docente/Clase N/Solucion Taller Clase N - VetCare.docx

## Plan minuto a minuto (120 min) — texto casi literal

### 0-10 · Encuadre
**Decir:** «Buenas. Hoy el hilo es VetCare DB. Avanzamos el PI en: Demo parcial + checklist de avance (hito formal PI).
La teoria sera corta; el peso esta en el taller del proyecto.»
Mostrar slide Agenda + Objetivo PI.
Pasar asistencia. Recordar herramientas gratis+nube.

### 10-35 · Teoria Core (breve)
**Decir:** «Solo lo necesario para el entregable de hoy.»
Cubrir:
- Hoy no hay tema nuevo: se cierran huecos del PI con rubrica.
- Evidencias: ER, DDL, roles, >=2 procs, >=1 fn, >=2 triggers, 1 opt.
- Feedback entre pares: 10 min por equipo.
Referencia: slide Teoria Core.
Pregunta al aire (2 min): ¿como se conecta esto con su VetCare?

### 35-55 · Demo paso a paso
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Recorrido de checklist + ejemplo demo de 3 min.
Herramienta: Live SQL / DB Fiddle + draw.io + ExamLab
📸 Pantallazo: [CAP: demo VetCare Clase 11]
Dejar script/enlace en el chat o en ExamLab.

### 55-105 · Taller guiado = tarea del PI
**Decir:** «Equipos: abran su carpeta VetCare. Esto suma a la rubrica del PI. Al final suben el taller en ExamLab.»
Usar bloque Taller ampliado (contexto->pistas). Solucion en Kit docente/Solucion Taller... (no proyectar completa).
Actividades:
1. Completar checklist de avance (si/no/parcial).
2. Demo 3-5 min: ER + 1 proc + 1 trigger.
3. Lista de gaps con responsable.
4. Subir avance intermedio a ExamLab (Talleres) si se pide.
Circular por equipos (o salas). Empujar evidencia, no perfectionismo.
Entregable: Checklist firmada + enlace/ZIP avance (DDL+procs+ER)
📸 Pantallazo: [CAP: avance equipo / playground Clase 11]

### 105-115 · Criterios de exito + quiz corto
Repasar checklist del dia (slide Criterios).
Pasar quiz 8–10 min **en ExamLab** (preguntas de esta clase; ver Guia Docente - Parte Practica). Version impresa/proyectable de respaldo: `Quiz Clase 11 - VetCare.docx`. Clave para usted: `Quiz Clase 11 - CLAVE DOCENTE.docx` (**no proyectar**).

### 115-120 · Cierre
**Decir:** «Queda avanzado: Demo parcial + checklist de avance (hito formal PI). Suban el taller a ExamLab hoy domingo 23:59 si aplica. Enunciado PI en Clases/Proyecto Integrador.»
Slide cierre. Dudas finales.


## Codigo / scripts
Carpeta Codigo/ — archivo 11_checklist_seed.sql.

## Capturas
Carpeta Capturas/. Placeholders [CAP: ...] arriba; reemplazar por PNG reales cuando pueda
(Playwright/manual en DB Fiddle, draw.io, Live SQL).

## Criterios de exito del dia
- Equipos tienen el entregable o gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
