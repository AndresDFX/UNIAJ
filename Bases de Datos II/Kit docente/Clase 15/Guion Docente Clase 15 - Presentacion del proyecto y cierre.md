# Guion docente · Clase 15 · Presentacion PI · Cierre VetCare

- **Curso:** Bases de Datos II (FI303215) · 120 min
- **Tipo:** SUSTENTACION DEL PI **EN VIVO** (sincrona)
- **Hilo:** Proyecto Integrador **VetCare DB**
- **Hoy cerramos el PI:** Sustentacion en vivo y entrega final del PI (20% Corte 3)
- **Entregable de hoy:** ZIP/PDF final subido antes del turno + sustentacion en vivo 5-8 min + Q&A
- **Herramienta:** ExamLab (Proyectos) + slides propias
- **Slides:** Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx
- **Caso de estudio (anexo del estudiante):** `Clases/Proyecto Integrador/Anexo - Caso de estudio Clinica Huellitas - Bases de Datos II.docx`
  — perfil de la clinica, las 8 entidades, las 3 reglas, el elenco de nombres y la escala por clase.
  Remita a este anexo cada vez que alguien pregunte «que datos guarda» o «de que tamano es esto».

> Sin mapa completo del curso, sin bio del docente, sin fechas de periodo.
> Presentacion del Curso / Acuerdo cubren logistica global.

## Fundamento teorico para el docente (al servicio del PI)

El objetivo de la clase no es «cubrir un capitulo» aislado, sino producir evidencia
del PI VetCare. La teoria se limita a desbloquear el taller.


## Guion por diapositiva

Es el mismo texto que llevan las **notas del presentador** de cada lámina: qué decir al entrar y en cada clic, el ejemplo, las preguntas típicas y el puente a la siguiente.

### [Slide 2] Encuadre de hoy · Objetivo proyecto

QUÉ ES (dilo así): Hoy no hay tema nuevo: es la sustentación en vivo del proyecto y el cierre del curso. Cada estudiante, o equipo, defiende sus decisiones en 5 a 8 minutos y responde preguntas al azar.

CÓMO DARLA (≈2 min):
- Al entrar: Lee la lámina y anuncia lo práctico: el orden de los turnos se sortea en un momento, el paquete tenía que estar subido antes del turno y la sustentación no se reemplaza por un video.
- Antes del primer turno: Lee en voz alta el reparto de los 100 puntos del proyecto: 20 modelo y DDL, 15 seguridad y respaldo, 25 procedimientos, funciones y disparadores con pruebas, 15 optimización, 10 integración y 15 informe y sustentación. Vale el 20 % del Corte 3; el Parcial 3 vale 15 % y la asistencia 5 %. El proyecto no reemplaza al parcial.

CUIDADO: Los 15 puntos de sustentación son la sexta parte, pero la sustentación es como se verifica que los otros 85 son de quien presenta. Dilo para evitar el reclamo de «solo vale 15».

PASA A LA SIGUIENTE: Cómo se reparte el bloque de hoy.

### [Slide 3] Mapa del bloque de hoy (120 min)

QUÉ ES (dilo así): El bloque es casi todo turnos: encuadre y sorteo, sustentaciones con su Q&A, y el cierre del curso al final.

CÓMO DARLA (≈1 min):
- Al entrar: Señala los tres tramos. Las láminas de concepto que siguen son lo que se va a preguntar: recórrelas en unos 12 minutos, así que los turnos empiezan hacia el minuto 15 y no en el 10.

PASA A LA SIGUIENTE: Lo primero que hay que tener claro: sustentar no es describir.

### [Slide 4] Sustentar no es describir: el eje de toda la clase

QUÉ ES (dilo así): La sustentación no es una visita guiada por el diagrama. Es explicar por qué cada decisión quedó como quedó y qué se descartó, porque en una base de datos deshacer una decisión cuesta caro.

CÓMO DARLA (≈2 min):
- Al entrar: A la izquierda, describir: una lista de «tenemos…». Pregunta: ¿qué aprende el evaluador de esa lista que no vea ya en el diagrama? Nada.
- Clic 1: A la derecha, sustentar: por qué quedó así y qué se descartó. Son las dos preguntas que se van a hacer en cada turno.
- Clic 2: El costo de revertir: cambiar código es la barra corta; cambiar un esquema con datos (partir una tabla con cien mil filas y seis procedimientos apuntándole) es la barra larga: migración, ventana de mantenimiento y riesgo de perder datos.

EJEMPLO: Describir: «hay una tabla cita con una FK». Sustentar: «la FK va en cita y no en mascota porque una mascota tiene muchas citas; sin ella podría existir una cita de una mascota que no existe».

SI PREGUNTAN:
- «¿Entonces no muestro el diagrama?» → Sí, pero como apoyo de dos decisiones justificadas, no para nombrar las tablas una por una.

CUIDADO: No califiques bien un recorrido de seis minutos por el ER porque «explicaron todo»: si nadie dio un porqué, no hubo sustentación.

PASA A LA SIGUIENTE: Las preguntas de porqué que casi siempre llegan son cuatro.

### [Slide 5] Las cuatro preguntas de por que que se hacen casi siempre

QUÉ ES (dilo así): Casi toda sustentación de bases de datos termina en las mismas cuatro preguntas. Quien las trae respondidas sustenta; quien no, improvisa.

CÓMO DARLA (≈3 min):
- Al entrar: Normalización: «está en tercera forma normal», es decir, cada atributo depende de la clave completa y de nada más (el teléfono del dueño vive en dueno, no repetido en cada mascota). Y si existe, la desnormalización deliberada: guardar el total en factura porque es un valor histórico.
- Clic 1: Índice: nombrar la consulta que lo usa (la agenda filtra por veterinario y ordena por hora, de ahí un índice sobre (id_veterinario, fecha_hora)) y mostrar EXPLAIN ANALYZE antes y después.
- Clic 2: Tipo de dato: la fecha es TIMESTAMP porque se compara y se ordena; el teléfono es VARCHAR porque no se hace aritmética con él y un tipo numérico pierde el cero inicial.
- Clic 3: La cuarta, la del disparador, es la que más se falla: tiene lámina propia.

EJEMPLO: «Guardamos el total en factura aunque se pueda sumar del detalle, porque es un valor histórico: si mañana sube el precio del insumo, la factura de ayer no debe cambiar.»

SI PREGUNTAN:
- «¿Desnormalizar es un error?» → No, si es deliberado y está escrito con su razón. El error es desnormalizar sin saberlo.

CUIDADO: «Está normalizado», sin decir qué forma normal ni dar un ejemplo, no responde la pregunta.

PASA A LA SIGUIENTE: La cuarta pregunta, la que más se falla.

### [Slide 6] La cuarta pregunta, la que mas se falla

QUÉ ES (dilo así): La pregunta es por qué una regla vive en un disparador y no en la aplicación. La respuesta que vale es una sola, la cobertura, y hay que saber también el contra-argumento.

CÓMO DARLA (≈2 min):
- Al entrar: Regla en la aplicación: escriben en insumo la aplicación, un script de carga y alguien con un cliente SQL. Solo el primero pasa por la regla; los otros dos llegan a la tabla con la X roja.
- Clic 1: Regla en el disparador: la barra del trigger está pegada a la tabla y los tres caminos pasan por ella.
- Clic 2: A favor: cobertura. En contra: lógica invisible (no aparece en el código de la aplicación, sorprende al que depura y puede dispararse en cascada). Criterio: disparadores para integridad y auditoría; el flujo de negocio, en procedimientos que se llaman a propósito.

EJEMPLO: La auditoría de precios: si alguien cambia a mano el precio de una vacuna desde un cliente SQL, solo un disparador deja constancia de quién y cuándo.

SI PREGUNTAN:
- «¿Un CHECK no hace lo mismo?» → Para una regla que mira una sola fila, sí, y es preferible (Clase 4). El disparador se justifica cuando mira otra fila u otra tabla, o escribe en otra tabla, como la auditoría.

CUIDADO: Si el estudiante solo da el argumento a favor, pide el contra-argumento: es la mitad de la respuesta.

PASA A LA SIGUIENTE: Además de defenderse, el proyecto tiene que poder correrlo otra persona.

### [Slide 7] Reproducible: un tercero llega a la misma base sin hablar con el autor

QUÉ ES (dilo así): Reproducible quiere decir que otra persona ejecuta tus archivos en una base vacía y obtiene lo mismo que tú, sin preguntarte nada. Es la prueba que el evaluador aplica literalmente.

CÓMO DARLA (≈2 min):
- Al entrar: La carpeta con nueve archivos numerados: 00_LEEME, 01_ddl, 02_datos_prueba, 03_roles, 04_procedimientos, 05_funciones, 06_triggers, 07_optimizacion y 08_pruebas.
- Clic 1: Por qué el orden importa: una FOREIGN KEY no se crea antes que la tabla a la que apunta, y un trigger no se puede crear si su tabla todavía no existe.
- Clic 2: La definición, en la caja final. Repasa los cuatro detalles que la rompen: no declarar motor y versión, suponer un estado previo, no ser idempotente (los DROP … IF EXISTS van primero, en orden inverso) y un LEEME que no sirve.

EJEMPLO: Un LEEME que sirve: «Motor: PostgreSQL 16.4 (lo dice SELECT version()). Ejecutar 01 a 08 en orden. Verificación: SELECT COUNT(*) FROM cita; devuelve 10. Límite: los datos de prueba no traen facturas anuladas.»

SI PREGUNTAN:
- «¿Cuántos datos de prueba hacen falta?» → Con dos filas por tabla no se demuestra nada. Un mínimo razonable: 3 dueños, 5 mascotas, 2 veterinarios, 10 citas, 5 insumos y 3 facturas, incluidos los casos borde: una mascota inactiva y un insumo con stock 1.
- «¿Qué es idempotente?» → Que se puede correr dos veces seguidas sin fallar: por eso los DROP TABLE IF EXISTS van primero, en orden inverso al de creación.

CUIDADO: Evalúalo ejecutando en una base limpia: un script que se ve bien puede fallar en la tercera sentencia por una FK que apunta a una tabla creada más abajo.

PASA A LA SIGUIENTE: Con el paquete listo: ¿cómo caben las decisiones en 5 a 8 minutos?

### [Slide 8] El reparto de los 5 a 8 minutos

QUÉ ES (dilo así): Siete minutos no alcanzan para todo, así que el reparto es una decisión. Este es el que funciona; es una convención, no una regla dura.

CÓMO DARLA (≈1 min):
- Al entrar: Lo que se cuenta: 45 s para el problema de la clínica en lenguaje de negocio, sin tablas en pantalla, y 90 s para el modelo: el ER y dos decisiones justificadas, no quince.
- Clic 1: Lo que se demuestra ejecutando: 60 s de seguridad (la matriz de roles y por qué recepción no ve el historial clínico), 90 s de automatización (un procedimiento con su caso válido y su caso inválido, en vivo) y 60 s de optimización (el plan antes y después).
- Clic 2: El cierre: 45 s de integración con su punto débil declarado y 30 s finales. En total, unos 7 minutos de un máximo de 8.

EJEMPLO: Los 45 segundos del problema: «la clínica atiende unas 150 citas al día con agenda de papel; perder una cita o dar dos en la misma franja le cuesta clientes».

SI PREGUNTAN:
- «¿Puedo mostrar capturas en vez de ejecutar?» → No para la automatización: el caso válido y el inválido se ejecutan en vivo. Una consulta corriendo delante del evaluador es la evidencia más difícil de fingir.
- «Si trabajamos en equipo, ¿cada uno presenta su parte?» → Cada integrante debe poder explicar cualquier parte en 60 segundos, porque el Q&A se dirige al azar.

CUIDADO: Cronometra cada turno: el que pasa de 8 minutos le quita tiempo al Q&A, que es donde se verifica la autoría.

PASA A LA SIGUIENTE: Después del pitch, las preguntas: las de modelado se repiten.

### [Slide 9] El Q&A de modelado, con las respuestas listas

QUÉ ES (dilo así): El Q&A de modelado tiene preguntas que se repiten, y todas son de porqué, no de qué. Tener las respuestas listas sirve para formularlas bien y para calificar igual a todos.

CÓMO DARLA (≈2 min):
- Al entrar: Dos mascotas del mismo dueño con el mismo nombre: la tabla las acepta porque cada una tiene su id_mascota. No pasa nada.
- Clic 1: Si se quisiera prohibirlo: UNIQUE (id_dueno, nombre), y la segunda Pelusa se rechaza.
- Clic 2: Es una decisión que se defiende en cualquiera de los dos sentidos; lo que no vale es no haberla pensado. Repasa las otras: nombre y apellido separados (para ordenar y buscar por apellido) y citas canceladas (borrado lógico con un campo de estado).

EJEMPLO: «¿Cuánto mejoró esa consulta?» Respuesta válida: «No lo medimos con volumen real porque la base de práctica se reinicia, pero el plan pasa de Seq Scan a Index Scan; la prueba sería cargar cincuenta mil citas y comparar los tiempos».

SI PREGUNTAN:
- «¿Por qué nombre y apellido separados?» → Para ordenar y buscar por apellido; separar después un campo unido falla con los nombres compuestos.
- «¿Por qué no borrar las citas canceladas?» → Son información de negocio (quién cancela siempre) y una cita con consulta y factura no se puede borrar sin dejar filas huérfanas: la FK lo impide.

CUIDADO: Anuncia la regla antes del primer turno: «no lo medimos» no penaliza si viene con cómo se mediría. Inventar un número se cae en la siguiente pregunta.

PASA A LA SIGUIENTE: Ahora, cómo se ordena la sesión; el cierre del curso viene al final de los turnos.

### [Slide 10] El cierre del curso: conectar lo hecho con el trabajo real

QUÉ ES (dilo así): El cierre conecta el semestre con el trabajo: lo que se produjo es lo que hace un desarrollador de bases de datos o un administrador junior en su primer año. Se termina con una autoevaluación concreta, no con una reflexión vaga.

CÓMO DARLA (≈5 min):
- Al entrar: Dala al final, después del último turno (minuto 110). Recorre la columna de la izquierda, los siete productos del semestre, y la flecha a «tareas del primer año». Subraya la caja azul: leer un plan y decidir si un índice sobra.
- Banda del medio: Las herramientas: PostgreSQL en el navegador, Excalidraw o draw.io y Mermaid se usaron por equidad, porque funcionan en cualquier navegador. El SQL es el mismo de un servidor PostgreSQL de producción.
- Banda amarilla: Lanza la autoevaluación y pide la respuesta escrita en el chat. Lee dos o tres en voz alta.

EJEMPLO: Una respuesta útil: «separar nombre y apellido; lo noté en la Clase 6, cuando la búsqueda por apellido sobre un nombre completo no podía usar un índice».

SI PREGUNTAN:
- «¿Vale la pena guardar los scripts?» → Sí: son portafolio. El paquete (ER, DDL, roles, procedimientos, triggers y optimización) se muestra en una entrevista técnica mejor que un certificado.

CUIDADO: No cierres con «¿qué aprendieron?»: da respuestas genéricas. La consigna concreta da material real para ajustar el curso el próximo semestre.

PASA A LA SIGUIENTE: La lámina de cierre.

### [Slide 11] Como se ordena la sesion de hoy

QUÉ ES (dilo así): Las reglas de los turnos, dichas una vez para todos. Después de esta lámina empiezan las sustentaciones, que ocupan el resto del bloque hasta el minuto 110.

CÓMO DARLA (≈3 min):
- Al entrar: Lee las cinco reglas y sortea el orden en voz alta; pega la lista en el chat de Meet para que cada quien sepa cuándo le toca.
- En cada turno: El estudiante comparte su pantalla. Cronometra 5 a 8 minutos de pitch con la ejecución real de un procedimiento (caso válido y caso rechazado) y haz dos o tres preguntas de porqué, al azar, a cualquier integrante.
- Entre turnos: Anota la calificación en 30 segundos, antes de llamar al siguiente: al final del bloque ya no se recuerda quién dijo qué.
- Si alguien se desconecta: Pasa al siguiente turno y vuelve a llamarlo al final de la lista. Si no logra reconectarse, deja constancia de la hora y acuerda por correo cómo se completa la sustentación.

EJEMPLO: Con turnos de unos 11 minutos (7 de pitch y 3-4 de Q&A) caben unos 8 en el bloque; si el grupo es más grande, reduce el Q&A a dos preguntas y anúncialo al sortear.

CUIDADO: Haz las preguntas a quien no está hablando: si siempre responde el mismo integrante, no se verifica que el trabajo sea de todos.

PASA A LA SIGUIENTE: Al terminar el último turno, vuelve a «El cierre del curso».


**Demo que usted debe poder repetir:** Checklist final de empaquetado del ZIP.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 15 · Presentacion proyecto · Cierre la clínica
2. Encuadre de hoy · Objetivo proyecto
3. Mapa del bloque de hoy (120 min)
4. Sustentar no es describir: el eje de toda la clase
5. Las cuatro preguntas de por que que se hacen casi siempre
6. La cuarta pregunta, la que mas se falla
7. Reproducible: un tercero llega a la misma base sin hablar con el autor
8. El reparto de los 5 a 8 minutos
9. El Q&A de modelado, con las respuestas listas
10. El cierre del curso: conectar lo hecho con el trabajo real
11. Como se ordena la sesion de hoy
12. Cierre · Clase 15

> Privado, no se proyecta: `Kit docente/Clase 15/Solucion Taller Clase 15 - VetCare.docx`

## Plan minuto a minuto (120 min) — sesion de SUSTENTACIONES EN VIVO

> Este bloque es sincrono y se dedica completo a las sustentaciones del PI VetCare DB.
> **No es clase autonoma y no es parcial.** No autorice reemplazar la defensa por un video
> grabado: el Q&A dirigido al azar es el unico instrumento con el que verifica que el modelo,
> los procedimientos y la optimizacion son de quien los presenta. El dia cae en festivo de
> calendario, pero la sesion esta destinada por decision docente a sustentar: anunciela por
> escrito la semana anterior para que nadie asuma que no hay clase.

### Antes de la sesion (semana previa)
1. Publique el orden y la duracion del turno: **5-8 min de pitch + 2-4 min de Q&A**. Con 12
   sustentaciones son ~110 min; si el grupo es mas grande, baje a 5 + 2 y avisele antes.
2. Exija el paquete subido a ExamLab (modulo Proyectos) **antes** del bloque, y abra usted
   mismo dos o tres ZIP en un playground limpio: quien llega a subir archivos consume su turno.
3. Tenga la rubrica impresa por estudiante y las preguntas de Q&A ya escogidas por tipo
   (verificacion, profundizacion, hipotetica), para no preguntar lo mismo a todos.

### 0-10 · Encuadre y orden de turnos
**Decir:** «Hoy sustentamos. De 5 a 8 minutos de pitch y hasta 4 de preguntas. Corto a los 8
minutos: si no llegaron a optimizacion, esa parte no se califica. El orden lo sorteo ahora.»
Sortee el orden delante del grupo, proyecte el cronometro y pida que el resto escuche.

### 10-110 · Sustentaciones (turnos consecutivos)
Por cada turno:
1. **5-8 min de pitch.** No interrumpa ni para corregir: anote y pregunte despues. Exija que se
   vea al menos **una ejecucion real** (procedimiento con caso valido e invalido, o el plan de
   ejecucion antes/despues), no solo capturas fijas.
2. **2-4 min de Q&A.** Una pregunta de verificacion («muestreme el DDL de esa tabla»), una de
   profundizacion («por que esa regla esta en un disparador y no en la aplicacion») y, si hay
   tiempo, una hipotetica («si manana entran cien mil citas, que consulta se cae primero»). Si
   autorizo equipo, dirija cada pregunta a un integrante distinto.
3. **Cierre el turno con la nota puesta**, no al final del dia.

### 110-120 · Cierre del curso
**Decir:** «Lo que entregaron —ER justificado, DDL con restricciones, matriz de privilegios,
procedimientos con manejo de errores, disparadores y analisis de plan— es el contenido real de
las tareas de un desarrollador de base de datos junior. Conserven el repositorio.»
Recuerde los pesos sin abrir discusion de notas: el PI vale **20% del Corte 3** y el Parcial 3
ya se aplico en su propia sesion; el proyecto no lo reemplaza ni lo compensa.

### Si alguien no se presenta o falla la conexion
Deje constancia escrita en el momento (hora, motivo) y reprograme dentro de la misma semana por
Meet, sustentando igualmente en vivo. Aceptar un video «por esta vez» elimina el Q&A, que es la
mitad de lo que se evalua, y vuelve regla la excepcion el semestre siguiente.


## Reparto del bloque y logistica (no se proyecta)

### Evaluar con rubrica: puntos a evidencia observable

Evaluar con rubrica es asignar puntos a evidencia observable y no a impresion general. Los 100 puntos del PI VetCare DB se reparten en 20 por modelo y DDL coherente, 15 por seguridad y respaldo, 25 por procedimientos, funciones y disparadores con casos de prueba, 15 por optimizacion con antes y despues, 10 por la integracion aplicacion-base de datos documentada como contrato, y 15 por informe y sustentacion. Leer ese reparto en voz alta al abrir la sesion, antes del primer turno, evita el reclamo mas comun: los 15 puntos de sustentacion son solo la sexta parte del total, pero la sustentacion es el instrumento con el que el evaluador verifica que los otros 85 son de su autor, y un modelo excelente que nadie sabe defender abre una duda de autoria que ningun documento cierra. Y va el recordatorio de pesos: estos 100 puntos valen 20% del Corte 3, el Parcial 3 de la Clase 14 (virtual sincrono por Meet y escrito, el 9 de noviembre) vale 15%, y la asistencia 5%. El proyecto no reemplaza ni compensa el parcial: son dos evaluaciones distintas del mismo corte, y confundirlas produce reclamos que se evitan diciendolo una sola vez, hoy, con los numeros a la vista.

## Codigo / scripts
Carpeta Codigo/ — archivo N/A.

## Capturas
Carpeta `Kit docente/Clase 15/Capturas/`. Cada linea de pantallazo de arriba trae
el nombre exacto del archivo y, si todavia no existe, el paso a paso para producirlo:
tomelo, guardelo con ese nombre y vuelva a generar el guion — la imagen se embebe sola.
Detalle por captura en `Capturas/README_capturas.txt`.

## Criterios de exito del dia
- Cada estudiante tiene el entregable o sus gaps escritos.
- Queda claro el vinculo con la rubrica del PI (modelo, seguridad, procs, opt, integracion).
