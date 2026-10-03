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


## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Sustentar no es describir: el eje de toda la clase (1/2)** — 5 vinetas.
  - Eso convierte cada eleccion del ER en algo que se debe poder defender, y es exactamente lo que un evaluador (o un lider tecnico en una entrevista) va a probar con dos o tres preguntas bien elegidas.

**[Slide 5] Sustentar no es describir: el eje de toda la clase (2/2)** — 3 vinetas.

**[Slide 6] Las cuatro preguntas de por que que se hacen casi siempre (1/2)** — 3 vinetas.
  - Esa segunda mitad es la que distingue al estudiante que entendio, porque normalizar no es un dogma sino un punto de partida del que se sale con razones escritas.

**[Slide 7] Las cuatro preguntas de por que que se hacen casi siempre (2/2)** — 3 vinetas.

**[Slide 8] La cuarta pregunta, la que mas se falla (1/2)** — 3 vinetas.
  - La cuarta pregunta merece parrafo propio porque es la que mas se falla: por que esa regla esta en un disparador y no en la aplicacion.
  - Si vive en la aplicacion, los dos ultimos caminos la evaden sin esfuerzo.
  - Por eso la convencion sana, que el estudiante puede citar como criterio propio, es reservarlos para invariantes de integridad y auditoria, y dejar el flujo de negocio en procedimientos que se invocan explicitamente.

**[Slide 9] La cuarta pregunta, la que mas se falla (2/2)** — 3 vinetas.

**[Slide 10] Reproducible: un tercero llega a la misma base sin hablar con el autor (1/3)** — 5 vinetas.
  - Esa es la definicion operativa y es la unica prueba que importa; el docente puede aplicarla literalmente abriendo el ZIP en un playground limpio y ejecutando.
  - Sobre esa base, cuatro detalles rompen la reproducibilidad y son los que el docente debe buscar primero al abrir el paquete.

**[Slide 11] Reproducible: un tercero llega a la misma base sin hablar con el autor (2/3)** — 5 vinetas.

**[Slide 12] Reproducible: un tercero llega a la misma base sin hablar con el autor (3/3)** — 3 vinetas.

**[Slide 13] El reparto de los 5 a 8 minutos (1/2)** — 5 vinetas.
  - Lo que si hay que exigir dentro del turno es la ejecucion real: que el estudiante corra el procedimiento en el playground, con su caso valido y su caso invalido, en vez de proyectar capturas fijas.
  - El paquete, en cambio.
  - Fuera de la lamina (habla de la practica): Lo que si hay que exigir dentro del turno es la ejecucion real: que el estudiante corra el procedimiento en el playground, con su caso valido y su caso invalido, en vez de proyectar capturas fijas, porque una consulta ejecutandose delante del evaluador es la evidencia mas dificil de fingir y la mas rapida de calificar.
  - Fuera de la lamina (habla de la practica): El paquete, en cambio, se sube al modulo de Proyectos de PostgreSQL en el navegador ANTES del turno: quien llega a subir archivos consume su propio tiempo de sustentacion.

**[Slide 14] El reparto de los 5 a 8 minutos (2/2)** — 4 vinetas.

**[Slide 15] El Q&A de modelado, con las respuestas listas (1/2)** — 4 vinetas.
  - El Q&A sobre modelado tiene preguntas que se repiten, y conviene que el docente tenga las respuestas listas para poder calificarlas y para poder formularlas.
  - Aqui vale la regla general del Q&A tecnico, que el docente debe anunciar antes de empezar: decir «no lo medimos» no penaliza si viene acompanado de como se mediria, por ejemplo «no medimos con volumen real porque el playground se reinicia, pero el plan de ejecucion pasa de recorrido completo a busqueda por indice, y la prueba seria cargar cincuenta mil citas y comparar los tiempos».
  - Inventar un numero, en cambio, se cae con la siguiente pregunta y cuesta mucho mas que admitir el limite.

**[Slide 16] El Q&A de modelado, con las respuestas listas (2/2)** — 4 vinetas.

**[Slide 17] El cierre del curso: conectar lo hecho con el trabajo real** — 4 vinetas.
  - Lo que el estudiante produjo (un ER justificado, un DDL con restricciones declarativas, una matriz de privilegios, procedimientos con manejo de errores, disparadores de auditoria, un analisis de plan de ejecucion y un contrato de operaciones) es literalmente el contenido de las tareas de un desarrollador de base de datos o de un administrador junior en su primer ano de trabajo.
  - Conviene tambien cerrar la duda sobre las herramientas, porque alguien la trae: Oracle Live SQL, DB Fiddle y draw.io se usaron por equidad y porque funcionan en cualquier navegador, no porque sean juguetes.
  - Esa respuesta es la que mejor predice si aprendieron, y ademas le da al docente material real para ajustar el curso el proximo semestre.


**Demo que usted debe poder repetir:** Checklist final de empaquetado del ZIP.

## Referencias a diapositivas
Numeracion real del deck `Clases/Clase 15 - Presentacion del proyecto y cierre/Presentacion.pptx`.
Las etiquetas [Slide N] del plan y del fundamento apuntan aqui.

1. Portada · Clase 15 · Presentacion proyecto · Cierre la clínica
2. Encuadre de hoy · Objetivo proyecto
3. Mapa del bloque de hoy (120 min)
4. Sustentar no es describir: el eje de toda la clase (1/2)
5. Sustentar no es describir: el eje de toda la clase (2/2)
6. Las cuatro preguntas de por que que se hacen casi siempre (1/2)
7. Las cuatro preguntas de por que que se hacen casi siempre (2/2)
8. La cuarta pregunta, la que mas se falla (1/2)
9. La cuarta pregunta, la que mas se falla (2/2)
10. Reproducible: un tercero llega a la misma base sin hablar con el autor (1/3)
11. Reproducible: un tercero llega a la misma base sin hablar con el autor (2/3)
12. Reproducible: un tercero llega a la misma base sin hablar con el autor (3/3)
13. El reparto de los 5 a 8 minutos (1/2)
14. El reparto de los 5 a 8 minutos (2/2)
15. El Q&A de modelado, con las respuestas listas (1/2)
16. El Q&A de modelado, con las respuestas listas (2/2)
17. El cierre del curso: conectar lo hecho con el trabajo real
18. Como se ordena la sesion de hoy
19. Cierre · Clase 15

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
