# -*- coding: utf-8 -*-
"""Especificacion de los talleres en ExamLab - Arquitectura de Sistemas Computacionales 2026-2.

La consume `examlab_talleres.py` para (a) decirle al estudiante, dentro del .docx
del taller, que va a encontrar en la plataforma y en que forma se responde cada
pregunta, y (b) generar en el Kit docente la guia con el texto exacto de cada
campo para crear el taller en ExamLab.

Por que existe: el taller decia «suba el resultado a ExamLab» y nada mas. El
estudiante no sabia que iba a encontrar, y el material pedia exportar PNG de
draw.io o correr SQL en DB Fiddle cuando la plataforma ya trae editor Mermaid,
PostgreSQL real (PGlite/WASM) y ejecucion de GUI de Java en el navegador.

Tipos usados, todos verificados contra el codigo de ExamLab
(`src/modules/workshops/WorkshopQuestions.tsx`):
    abierta · cerrada · cerrada_multi · codigo · diagrama · java_gui ·
    python_gui · codigo_zip · red_consola · red_gui · so_consola · bd_sql

Ademas de las preguntas, cada clase trae `pasos`: la reescritura de los 5 pasos del
taller del estudiante. Los originales eran one-liners sin cantidad ni criterio de
verificacion ("creen diagrama Containers"), que es justo lo que no se entendia.

Cada taller suma 100 puntos.
"""

# ---------------------------------------------------------------------------
# Actividad unica del Corte 1
# ---------------------------------------------------------------------------
# En ExamLab hay UNA actividad por CORTE, no un taller por clase:
#   Corte 1 -> Clases 1, 2, 3 y 4   ·   Corte 2 -> Clases 6, 7, 8 y 10
#   Corte 3 -> Clases 11, 12, 13 y 15
# Las Clases 5, 9 y 14 son parciales y no aportan preguntas.
# Las Clases 1 a 4 NO tienen un taller cada una: comparten UNA sola
# actividad de 15 preguntas, con numeracion continua y 25 % del peso por clase.
# Por eso cada `EXAMLAB[n]` de esas cuatro clases lleva solo sus preguntas, y
# cada pregunta declara su `n_global`: es el numero con el que el estudiante la
# ve en la plataforma. Sin eso, el material de la Clase 3 hablaria de «la
# pregunta 1» cuando en pantalla es la 7.
#
# Los puntos siguen la propuesta del curso (100 por actividad) y no los que
# muestra la plataforma, que usa otra escala.
ACTIVIDAD_CORTE1 = {
    "titulo": "Actividad del Corte 1 - CloudLite App: dominio, decision y contenedor",
    "clases": (1, 2, 3, 4),
    "preguntas": 15,
    "total": 100,
    "cierre": "domingo 23:59 de la semana de la Clase 4",
}


ACTIVIDAD_CORTE2 = {
    "titulo": "Actividad del Corte 2 - CloudLite App: seguridad, despliegue, CI y costos",
    "clases": (6, 7, 8, 10),
    "preguntas": 12,
    "total": 100,
    "cierre": "domingo 23:59 de la semana de la Clase 10",
}

ACTIVIDAD_CORTE3 = {
    "titulo": "Actividad del Corte 3 - CloudLite App: diagnostico, rendimiento y cierre",
    "clases": (11, 12, 13, 15),
    "preguntas": 8,
    "total": 100,
    "cierre": "antes del turno de sustentacion de la Clase 15",
}


EXAMLAB = {1: {'pasos': [
                            'Paso 1: elija un dominio concreto entre AgendaU, BiblioLite, InventarioLab, TurnosClinica o EventosCampus (o uno propio del mismo tamano) y escriba en la pregunta 1 el problema en 2 o 3 frases, diciendo QUIEN lo sufre con un rol concreto y COMO se mide con una cifra, aunque sea estimada; verifique que su enunciado no sirva igual para cualquier otro sistema, porque entonces el dominio todavia es generico.',
                            'Paso 2: complete en la pregunta 2 la ficha de cinco bloques (DOMINIO, PROBLEMA, ACTORES, CAPACIDADES, FUERA DE ALCANCE) con 3 a 5 capacidades en la forma verbo mas objeto de negocio, 2 a 3 actores con lo que espera cada uno, los sistemas externos dentro del bloque ACTORES, y lo que el sistema no hara este semestre; verifique que ninguna capacidad nombre tecnologia.',
                            'Paso 3: dibuje primero el boceto del C4 Context en Excalidraw o draw.io, que es donde se piensa el modelo, y despues pidale a una IA que lo traduzca a Mermaid («convierta este diagrama a Mermaid usando C4Context»); peguelo en la pregunta 3 y verifique en el diagrama ya renderizado que el sistema sea UNA sola caja, que no aparezca ninguna caja interna (eso es la pregunta 13) y que cada flecha lleve verbo y protocolo.',
                            'Paso 4: elija en la pregunta 4 dos atributos de calidad de los cuatro del curso, escriba por que pesan en SU dominio y como los mediria con un numero y una unidad, y cierre diciendo cual sacrificaria y que gana a cambio; revise ademas que los nombres de actores y de sistemas externos sean EXACTAMENTE los mismos en la ficha y en el diagrama, porque las preguntas 12 a 15 los reutilizan. Las preguntas 5 a 15 se resuelven en las Clases 2, 3 y 4: la actividad se entrega completa al cierre del Corte 1, no hoy.',
                        ],
     'preguntas': [
                      {
                          'n_global': 1,
                          'tipo': 'abierta',
                          'puntos': 5.0,
                          'enunciado': '''## Dominio y problema de CloudLite App

Elija un dominio **concreto** para CloudLite App y escriba el problema en **2 o 3 frases**.

Dominios sugeridos: **AgendaU** (asesorias academicas) · **BiblioLite** (prestamos de
biblioteca) · **InventarioLab** (equipos de laboratorio) · **TurnosClinica** (citas) ·
**EventosCampus** (inscripciones). Puede proponer uno propio del mismo tamano.

El problema debe decir dos cosas, y las dos se califican:

1. **QUIEN lo sufre.** Una persona concreta con un rol, no «los usuarios».
2. **COMO se mide.** Una cifra, aunque sea estimada: `se cruzan 40 correos por semana
   para cuadrar 12 asesorias`, `38 libros devueltos tarde el semestre pasado`.

> No vale un dominio generico. «Una red social», «una app de la universidad» o «un
> e-commerce» no permiten evaluar ninguna decision de arquitectura, porque no hay nada
> concreto que disenar. Si su enunciado sirve igual para cualquier otro sistema, todavia
> no es un dominio.

Este dominio **no vuelve a cambiar** en el resto del curso: las Clases 2, 3 y 4 de esta
misma actividad, y las Clases 7, 11 y 15, reutilizan estos nombres.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts el dominio concreto y del tamano adecuado. Si es generico (red social, app de la universidad), toda la pregunta vale cero: sin dominio no hay nada que arquitecturar en las clases siguientes. 1.5 pts que el problema nombre a QUIEN lo sufre con un rol concreto. 1.75 pts que incluya una cifra que mida el dolor; una cifra estimada sirve, «mucho tiempo» no. Se descuenta si el problema pasa de 3 frases.',
                      },
                      {
                          'n_global': 2,
                          'tipo': 'abierta',
                          'puntos': 7.0,
                          'enunciado': '''## Ficha del dominio

Complete la ficha del dominio que eligio en la pregunta anterior. Son **cinco bloques
rotulados**, en este orden:

```
DOMINIO
PROBLEMA
ACTORES
CAPACIDADES
FUERA DE ALCANCE
```

- **DOMINIO** y **PROBLEMA**: repita lo que escribio en la pregunta 1, para que la ficha
  se lea completa.
- **ACTORES**: de **2 a 3** actores humanos, cada uno con una frase de que espera del
  sistema. En este mismo bloque liste tambien **los sistemas externos** con los que
  CloudLite se conecta (por ejemplo un proveedor de identidad institucional o un servicio
  de correo transaccional). Esos sistemas externos son los que despues aparecen en el
  diagrama de la pregunta 3, asi que conviene escribirlos aqui **antes** de dibujar.
- **CAPACIDADES**: de **3 a 5**, en la forma **verbo + objeto de negocio**: `reservar una
  asesoria`, `publicar un cupo`, `cancelar una reserva`, `notificar el recordatorio`.
  **Prohibido nombrar tecnologia**: «tener login con JWT» o «usar cache» no son
  capacidades, son medios. Una capacidad describe lo que el usuario puede HACER.
- **FUERA DE ALCANCE**: que **no** va a hacer el sistema este semestre. Es el bloque que
  evita que el alcance crezca sin control, y es lo primero que se revisa cuando alguien
  pida mas tiempo en una entrega futura.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2 pts los cinco bloques presentes y rotulados en el orden pedido. 2.5 pts las capacidades (3 a 5) en verbo mas objeto de negocio, sin nombrar tecnologia; se descuenta por cada capacidad que sea una pieza tecnica. 2.25 pts los actores (2 a 3) con su expectativa explicita, mas los sistemas externos nombrados. 2 pts el fuera de alcance con exclusiones que un evaluador razonable si habria esperado. Los sistemas externos de este bloque deben ser los mismos que aparezcan en el diagrama de la pregunta 3.',
                      },
                      {
                          'n_global': 3,
                          'tipo': 'diagrama',
                          'puntos': 8.0,
                          'enunciado': '''## C4 Context de CloudLite App

Modele el diagrama **C4 de nivel Context** de su CloudLite, en Mermaid. La primera linea
debe ser exactamente `C4Context`.

El diagrama debe mostrar:

- El sistema como **UNA sola caja**: `System(...)`. Es el sistema completo, no un modulo
  interno.
- Los **actores que lo usan**: `Person(...)`, los mismos de su ficha.
- Los **sistemas externos** con los que se conecta: `System_Ext(...)`, los mismos que
  listo en el bloque ACTORES.
- **Cada flecha** (`Rel`) etiquetada con un **verbo de negocio** y un **protocolo**
  (`HTTPS`, `OIDC sobre HTTPS`, `SMTP`, `API REST sobre HTTPS`). Una flecha rotulada
  «usa», o sin protocolo, no cuenta.

> **No incluya todavia los contenedores internos.** Nada de base de datos, API, worker ni
> cache: en el nivel Context el sistema es una caja negra. Esas cajas son el diagrama de
> la pregunta 13 de esta misma actividad, que corresponde a la Clase 4. Si se dibujan aqui,
> ese diagrama se queda sin nada nuevo que mostrar.

**Antes de enviar, verifique renderizando dentro de ExamLab:** que el diagrama se dibuje
sin error de sintaxis, que cada flecha se lea en voz alta como una frase completa, y que
los nombres sean identicos a los de su ficha.

**Consejo de sintaxis:** no use comas dentro de las etiquetas entre comillas del C4;
separe con «y» o con guion.

**Tamano de referencia:** entre cuatro y ocho elementos en total. Si tiene veinte, es casi
seguro que se colaron piezas internas del sistema.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts una sola caja System para CloudLite completo. 2 pts los actores como Person, coherentes con la ficha. 2 pts los sistemas externos como System_Ext, los mismos que la ficha. 2 pts que TODA flecha lleve verbo de negocio y protocolo. 1 pt que el diagrama renderice sin error dentro de la plataforma. Si aparece un contenedor interno (base de datos, API, worker, cache) se pierden los 3 pts de la caja del sistema, porque eso es el nivel Container de la pregunta 13.',
                          'mermaid_esperado': '''C4Context
    title Contexto de CloudLite App - dominio AgendaU
    Person(estudiante, "Estudiante", "Reserva y cancela citas de asesoria")
    Person(coordinador, "Coordinador academico", "Publica cupos y revisa la ocupacion semanal")
    System(cloudlite, "CloudLite App", "Aplicacion web y API para reservar asesorias academicas")
    System_Ext(idp, "Proveedor de identidad institucional", "Login OIDC de la universidad")
    System_Ext(correo, "Correo transaccional SaaS", "Envio de confirmaciones y recordatorios")
    Rel(estudiante, cloudlite, "Reserva y cancela citas de asesoria", "HTTPS")
    Rel(coordinador, cloudlite, "Publica cupos y consulta la ocupacion", "HTTPS")
    Rel(cloudlite, idp, "Valida la identidad institucional del usuario", "OIDC sobre HTTPS")
    Rel(cloudlite, correo, "Solicita el envio de la confirmacion de cita", "API REST sobre HTTPS")
    Rel(correo, estudiante, "Entrega el recordatorio 24 horas antes", "SMTP")''',
                      },
                      {
                          'n_global': 4,
                          'tipo': 'abierta',
                          'puntos': 5.0,
                          'enunciado': '''## Atributos de calidad de su CloudLite

Los atributos de calidad son las propiedades **medibles** que el sistema debe exhibir, y
son el vocabulario con el que se justifica cualquier decision de arquitectura. Este curso
usa cuatro de forma permanente: **rendimiento**, **disponibilidad**, **seguridad** y
**costo**.

Elija **dos** de los cuatro, los que mas pesen en su dominio, y para cada uno escriba:

1. **Por que ese pesa en SU dominio.** Una frase que lo ate al problema de la pregunta 1,
   no a la teoria general.
2. **Como lo mediria**, con un **numero y una unidad**. Ejemplos de la forma esperada:
   `el listado de disponibilidad responde en menos de 300 ms`, `el sistema responde el
   99,9 % del mes, es decir que acepto hasta unos 43 minutos de caida`.

Cierre con **una frase de conflicto**: nombre **cual de los dos sacrificaria** si no puede
tener los dos al mismo tiempo, y **que gana** a cambio.

> El punto de la pregunta es ese cierre. Los atributos compiten entre si: mas
> disponibilidad exige redundancia, la redundancia cuesta dinero, y por eso la
> arquitectura es sobre todo el oficio de elegir que se sacrifica. Una respuesta que diga
> que los cuatro son igual de importantes no ha decidido nada.

Lo que escriba aqui vuelve dos veces en el curso: el **costo** se retoma en la Clase 10 y
el **rendimiento** con percentiles en la Clase 12.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt la eleccion de dos atributos con una razon atada al dominio propio y no a la teoria general. 2 pts las dos metricas, con numero Y unidad: una metrica sin numero («que sea rapido», «que sea seguro») no suma. 2 pts la frase de conflicto, que debe nombrar cual se sacrifica y que se gana; cero en este criterio si la respuesta afirma que los cuatro son igual de importantes o no elige.',
                      },
                  ],
     'resumen': '''Las preguntas 1 a 4 de la actividad del Corte 1, que es una sola para las Clases 1 a 4. El estudiante sale con el dominio de CloudLite cerrado en una ficha de cinco bloques y con el diagrama C4 Context renderizado dentro de ExamLab, que es la semilla de todos los diagramas del semestre.''',
     'titulo': '''Actividad del Corte 1 (preguntas 1 a 4) - Dominio, ficha, C4 Context y calidad'''},
 2: {'pasos': [
                  'Paso 1: relea su ficha y su C4 Context de la Clase 1. No cambie de dominio: las preguntas 5 a 7 se califican sobre el mismo sistema, y el ADR que redacte hoy se reutiliza en el informe del PI y en la sustentacion de la Clase 15.',
                  'Paso 2: construya en la pregunta 5 la matriz «Criterio | IaaS | PaaS | SaaS» con las cuatro filas en orden (control, costo cualitativo, operacion, time-to-demo) y maximo 2 lineas por celda; verifique que cada celda nombre una capacidad o una restriccion de SU dominio, y que la fila de operacion no afirme que en PaaS o SaaS usted deja de responder por su propia aplicacion.',
                  'Paso 3: redacte en la pregunta 6 el ADR-001 con las cinco secciones rotuladas —titulo, estado con fecha, contexto con sus restricciones reales, la decision en UNA sola frase con UN modelo dominante, y exactamente 2 alternativas descartadas con el motivo atado a su dominio—; verifique que la seccion de decision no nombre dos modelos, porque en ese caso vale cero.',
                  'Paso 4: escriba en la pregunta 7 la seccion 6 del mismo ADR, las consecuencias en los tres ejes (operacion, costo y aprendizaje), con al menos una positiva y una negativa por eje marcadas con + y -, y verifique que al menos una negativa hable de amarre al proveedor o de perdida de control; guarde y continue, que la actividad se entrega completa al cierre del corte.',
              ],
     'preguntas': [
                      {
                          'n_global': 5,
                          'tipo': 'abierta',
                          'puntos': 6.25,
                          'enunciado': '''## Matriz IaaS / PaaS / SaaS para su dominio

Partiendo de la **ficha** y del **C4 Context** del mismo dominio que cerro en la Clase 1,
construya una matriz que compare los tres modelos de servicio **aplicados a las
capacidades de SU dominio**.

Encabezados exactos: `Criterio | IaaS | PaaS | SaaS`, con **estas cuatro filas** y en este
orden:

1. **Control**: cuanto puede ajustar usted del entorno.
2. **Costo cualitativo**: bajo, medio o alto, y por que. No hace falta ningun precio.
3. **Operacion**: **quien opera el sistema operativo y el runtime**, usted o el proveedor.
4. **Time-to-demo**: cuanto tarda en tener la primera demo de su CloudLite funcionando.

Cada celda: **maximo 2 lineas**, y siempre referida a su dominio y a sus capacidades. Una
celda que dice «mas control» no dice nada; «puedo instalar la libreria de codigos de barras
que necesita el prestamo» si.

> La fila de **Operacion** es la que mas se equivoca. La responsabilidad no desaparece al
> subir de nivel: se **reparte**. Cuanto se reparte es exactamente lo que distingue los
> tres modelos, y en los tres usted sigue respondiendo por su propia aplicacion, sus
> permisos y sus datos.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2 pts la matriz con los cuatro criterios en el orden pedido y las cuatro columnas. 3 pts que las doce celdas de comparacion hablen del dominio propio y de sus capacidades, no de teoria general; se descuenta por cada fila escrita en abstracto. 1.25 pts que la fila de operacion reparta correctamente la responsabilidad en los tres modelos y no afirme que en PaaS o SaaS el equipo deja de responder por su aplicacion.',
                      },
                      {
                          'n_global': 6,
                          'tipo': 'abierta',
                          'puntos': 12.5,
                          'enunciado': '''## ADR-001: modelo de servicio dominante de CloudLite

Redacte el **ADR-001** con estas cinco secciones rotuladas, en este orden y sin agregar
otras:

1. **Titulo**: `ADR-001 Modelo de servicio dominante de CloudLite App`.
2. **Estado**: `Aceptado` mas la fecha.
3. **Contexto**: 2 o 3 lineas con el dominio que eligio y las **restricciones reales** bajo
   las que decide: quien sostiene el proyecto, en cuanto tiempo y con que presupuesto.
4. **Decision**: **una sola frase** que nombre **un unico modelo dominante** —IaaS, PaaS o
   SaaS— para la aplicacion propia de CloudLite.
5. **Alternativas descartadas**: **exactamente 2**, cada una con el motivo del descarte
   **expresado en terminos de su dominio**, no en abstracto.

Las **consecuencias** son la **seccion 6** del mismo documento y se entregan en la
**pregunta 7**: no las escriba aqui, y alla no repita la decision. Con las dos respuestas
juntas usted tiene el ADR completo —**seis secciones, ninguna mas**— para el informe del PI.

> **Si la seccion 4 nombra dos modelos, esa seccion vale cero.** «Un poco de PaaS y un poco
> de IaaS» no es una decision: es no haber decidido. Puede aclarar en las alternativas que
> consume **SaaS satelite** para identidad y correo; eso no rompe la regla, porque el
> modelo dominante se refiere a **su** aplicacion.

> El **contexto** no es un resumen del tema: es la lista de restricciones que hacen que su
> decision sea razonable. «Es un proyecto academico» no es contexto; «lo sostengo yo solo en
> doce semanas, sin presupuesto de nube y sin tarjeta de credito» si lo es, porque de ahi se
> deduce el descarte de IaaS. La matriz de la pregunta 5 es el analisis; el contexto son las
> restricciones.

Un ADR (Architecture Decision Record) es un formato real, usado en equipos reales: sirve
para que dentro de seis meses alguien —incluido usted— entienda **por que** se decidio asi
y **que se descarto**. Un ADR con una sola opcion no documenta una decision: documenta un
hecho.

Este ADR se reutiliza en el informe del PI y en la sustentacion de la Clase 15.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1.5 pts titulo con el numero del ADR y estado con fecha. 2 pts el contexto: nombra el dominio, el plazo y al menos una restriccion real de quien sostiene el proyecto; cero en este criterio si es teoria general o un resumen del tema de la clase. 3.5 pts la decision en UNA frase con UN modelo dominante; cero en este criterio si nombra dos o mas modelos. 5.5 pts las dos alternativas descartadas con el motivo del descarte atado al dominio: 2.75 pts cada una, y se pierde la mitad de cada una si el motivo es generico («es mas caro», «es mas complejo») sin decir mas caro o mas complejo PARA QUE de su sistema.',
                      },
                      {
                          'n_global': 7,
                          'tipo': 'abierta',
                          'puntos': 6.25,
                          'enunciado': '''## Consecuencias del ADR-001

Escriba la **seccion 6 del mismo ADR-001**, las **consecuencias** de la decision que tomo
en la pregunta anterior, cubriendo **los tres ejes** y rotulandolos:

- **Operacion**: que tiene que hacer usted a partir de ahora, y que deja de hacer.
- **Costo**: que se abarata y que se encarece, en terminos cualitativos.
- **Aprendizaje**: que tiene que aprender para sostener esa decision durante el semestre.

En cada eje escriba **al menos una consecuencia positiva y una negativa**, rotuladas con
`+` y `-`. **Al menos una de las negativas debe hablar de amarre al proveedor o de perdida
de control**: es la contrapartida que casi nunca se escribe y la que la sustentacion de la
Clase 15 va a pedir.

> Una consecuencia no es una ventaja de folleto. «Es mas facil» no es una consecuencia;
> «no voy a poder instalar la libreria de codigos de barras y tendre que buscar una
> alternativa que el proveedor soporte» si lo es, porque describe algo que cambia en su
> trabajo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts los tres ejes presentes y rotulados (operacion, costo, aprendizaje). 2 pts que cada eje traiga al menos una consecuencia positiva y una negativa marcadas con + y -. 1.25 pts que al menos una negativa hable de amarre al proveedor o de perdida de control. Se descuenta por cada consecuencia escrita como ventaja de folleto («es mas facil», «es mas moderno») en vez de como algo que cambia en el trabajo del estudiante.',
                      },
                  ],
     'resumen': '''Las preguntas 5 a 7 de la actividad del Corte 1. El estudiante compara IaaS, PaaS y SaaS sobre las capacidades de su propio dominio, decide un modelo dominante y lo documenta como ADR-001 con sus alternativas descartadas y sus consecuencias.''',
     'titulo': '''Actividad del Corte 1 (preguntas 5 a 7) - Modelos de servicio y ADR-001'''},
 3: {'pasos': [
                  'Paso 1: elija en la pregunta 8 cual servicio de su C4 Context va a contenedorizar y justifiquelo en 2 o 3 frases; escriba a continuacion el Dockerfile completo con la imagen base ligera y con etiqueta fija, el COPY de dependencias antes del COPY del codigo, el EXPOSE y el CMD, verificando que no copie el .env ni ninguna clave.',
                  'Paso 2: explique en la pregunta 9, sobre su propio Dockerfile, la diferencia entre imagen y contenedor, que instrucciones de SU archivo crean capa, por que el orden aprovecha el cache y en que se diferencia su contenedor de una maquina virtual; verifique que no escribio que un contenedor es una VM ligera.',
                  'Paso 3: describa en la pregunta 10 el ciclo completo con los comandos exactos de build y de run, explicando que lado del mapeo de puertos es el anfitrion y que lado el contenedor, y cierre con el contrato del endpoint de salud (ruta, codigo de estado y cuerpo); verifique que el puerto sea el mismo que puso en el EXPOSE.',
                  'Paso 4: ejecute de verdad el ciclo en Killercoda y reporte en la pregunta 11 la tabla de 5 filas con la salida real pegada textualmente, la descripcion de la captura con prompt, docker ps y hora del sistema, y una fila de incidente; recuerde que la sesion caduca a 1 hora, asi que capture la evidencia ANTES de cerrarla.',
              ],
     'preguntas': [
                      {
                          'n_global': 8,
                          'tipo': 'abierta',
                          'puntos': 10.0,
                          'enunciado': '''## El servicio a contenedorizar y su Dockerfile

**Primera parte — la eleccion.** Diga **cual servicio de su C4 Context** va a
contenedorizar: el servicio principal de su dominio, que normalmente es la **API stub** o
el **front estatico**. Justifique la eleccion en 2 o 3 frases: por que ese y no otro, y que
demuestra tener ese servicio corriendo.

**Segunda parte — el Dockerfile.** Escriba el Dockerfile **completo** de ese servicio. Debe
tener, como minimo, estas instrucciones y en un orden que tenga sentido:

- `FROM` con una imagen base **ligera y con etiqueta fija** (por ejemplo `node:20-alpine`,
  `python:3.12-slim`, `nginx:alpine`). Nada de `latest`.
- `WORKDIR`
- `COPY` de las dependencias **antes** que el `COPY` del codigo
- `RUN` de instalacion de dependencias
- `COPY` del codigo
- `EXPOSE` con el puerto
- `CMD` con el proceso principal

**Dos reglas que se califican aparte:**

1. **El puerto de `EXPOSE`, el del `CMD` y el que documenta en la pregunta 10 tienen que ser
   el mismo numero.** Es el error mas comun y el mas facil de evitar.
2. **Prohibido copiar el `.env` o cualquier clave dentro de la imagen.** Si el `COPY` es de
   todo el directorio, se necesita un `.dockerignore`; diga que lleva dentro.

> Un secreto dentro de la imagen queda en el **historial de capas** para siempre: cualquiera
> que tenga la imagen puede leerlo con `docker history` aunque el archivo se borre en una
> capa posterior. Los secretos se inyectan en tiempo de ejecucion, no se construyen dentro.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2 pts la eleccion del servicio con justificacion atada al dominio. 5 pts el Dockerfile completo con las instrucciones minimas y un orden que aproveche el cache (dependencias antes del codigo). 1.5 pts imagen base ligera y con etiqueta fija; se descuenta por usar latest. 1.5 pts coherencia del puerto entre EXPOSE, CMD y lo documentado. Si el Dockerfile copia un .env o una clave, o hace COPY de todo sin .dockerignore ni mencionarlo, se pierden los 5 pts del Dockerfile: es el error que el curso corta el mismo dia.',
                      },
                      {
                          'n_global': 9,
                          'tipo': 'abierta',
                          'puntos': 4.0,
                          'enunciado': '''## Imagen, contenedor y capas, sobre su propio Dockerfile

Explique, **usando el Dockerfile que acaba de escribir**, no la teoria general:

1. **Imagen y contenedor no son lo mismo.** Diga cual es cual en su caso, en una frase. La
   analogia que se espera: la imagen es el molde, el contenedor es la instancia corriendo;
   de una imagen se pueden levantar varios contenedores a la vez.
2. **Que instruccion de SU Dockerfile crea una capa nueva** y por que eso importa. Nombre al
   menos dos instrucciones concretas de su archivo.
3. **Por que puso el `COPY` de dependencias antes que el `COPY` del codigo.** Diga que pasa
   con el cache cuando cambia una linea de codigo, comparado con lo que pasaria en el orden
   inverso.
4. **Una diferencia entre su contenedor y una maquina virtual**, en una frase, en terminos
   de que comparte con la maquina anfitriona.

> Cuidado con dos frases que suenan bien y son falsas: «un contenedor es una VM ligera» (no
> lo es: la VM carga un sistema operativo completo, el contenedor **comparte el kernel** del
> anfitrion) y «la imagen se ejecuta» (se ejecuta el contenedor, que es una instancia de la
> imagen).

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt distinguir imagen de contenedor sin decir que un contenedor es una VM ligera. 1 pt nombrar al menos dos instrucciones de SU propio Dockerfile que crean capa. 1 pt explicar el efecto del orden en el cache, comparando con el orden inverso. 1 pt la diferencia con una VM en terminos de kernel compartido. Una respuesta que explique la teoria sin referirse a su archivo pierde la mitad: la pregunta evalua que entienda lo que escribio.',
                      },
                      {
                          'n_global': 10,
                          'tipo': 'abierta',
                          'puntos': 5.0,
                          'enunciado': '''## Construir, ejecutar y verificar el contenedor

Explique el ciclo completo de su servicio, con los **comandos exactos** que usaria:

1. **Construccion**: el comando de build con el nombre y la etiqueta de su imagen.
2. **Ejecucion**: el comando de run, con el **mapeo de puertos entre el anfitrion y el
   contenedor** explicado. Diga que numero corresponde a cada lado y que pasaria si los
   invierte.
3. **Verificacion**: el **contrato del endpoint de salud** de su stub, con las tres cosas
   que lo definen:
   - la **ruta** (por ejemplo `/health`),
   - el **codigo de estado** esperado,
   - el **cuerpo** de la respuesta, con su formato.

> El endpoint de salud no es un adorno: es la forma en que cualquier orquestador, balanceador
> o pipeline sabra si su servicio esta vivo, y por eso vuelve en la Clase 7 (despliegue) y en
> la Clase 8 (CI). Un endpoint que devuelve 200 con el cuerpo vacio es peor que ninguno,
> porque no distingue «vivo» de «vivo pero roto».

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1.5 pts el comando de build con nombre y etiqueta. 1.5 pts el comando de run con el mapeo de puertos correctamente explicado: que lado es el anfitrion, que lado el contenedor y que pasa si se invierten. 2 pts el contrato de salud completo con ruta, codigo de estado y cuerpo con su formato; se descuenta si falta cualquiera de los tres. El puerto tiene que ser el mismo de la pregunta 8.',
                      },
                      {
                          'n_global': 11,
                          'tipo': 'abierta',
                          'puntos': 6.0,
                          'enunciado': '''## Bitacora del laboratorio: la evidencia de que corrio

Ejecute de verdad el ciclo en **Killercoda** (killercoda.com, cuenta gratuita, escenario
Ubuntu) y reporte lo que paso. Si Killercoda no carga, la alterna es **LabEx Docker
Playground**, que en su plan gratuito da solo **3 sesiones al dia**.

Entregue una tabla de **3 columnas** (`Comando | Que esperaba | Que salio realmente`) con
**una fila por comando**, en este orden:

1. el build de su imagen
2. `docker images` filtrado por su imagen
3. el run de su contenedor
4. `docker ps`
5. la peticion a su endpoint de salud

En la columna de la derecha pegue el **fragmento textual** de la salida real: el numero de
capas, el identificador corto del contenedor, el `200` de la respuesta. No la parafrasee.

Debajo de la tabla:

- **Describa la captura** que adjunta. Debe mostrarse al mismo tiempo el prompt del
  laboratorio, la salida de `docker ps` y la hora del sistema.
- **Una fila de incidente**: un comando que le fallo y como lo resolvio. Si nada fallo,
  escriba el que estuvo a punto de fallar y por que no fallo.

> **La sesion del laboratorio caduca a 1 hora.** El Dockerfile se escribe en la carpeta de
> su PI y se **pega** en el laboratorio, nunca al contrario, y la evidencia se captura
> **antes** de cerrar. Perder el trabajo por no haber guardado es el incidente mas comun del
> dia, y no es excusa aceptable para no entregar esta pregunta.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2.5 pts las cinco filas con la salida real pegada textualmente; una salida parafraseada («salio bien») no suma. 1.5 pts la descripcion de la captura con los tres elementos exigidos (prompt, docker ps y hora del sistema). 1 pt la fila de incidente con el problema y como se resolvio. 1 pt coherencia: el nombre de la imagen, la etiqueta y el puerto son los mismos de las preguntas 8 y 10. Es la pregunta que demuestra que el contenedor existio de verdad y no solo en papel.',
                      },
                  ],
     'resumen': '''Las preguntas 8 a 11 de la actividad del Corte 1. El estudiante elige el servicio a contenedorizar, escribe su Dockerfile, explica capas y cache sobre su propio archivo, documenta el ciclo con el contrato de salud y entrega la bitacora con la evidencia real del contenedor corriendo.''',
     'titulo': '''Actividad del Corte 1 (preguntas 8 a 11) - Contenedor del stub de CloudLite'''},
 4: {'pasos': [
                  'Paso 1: decida en la pregunta 12 si su CloudLite es un monolito modular o microservicios, con los dos criterios aplicados a su caso (tamano del equipo con numero y plazo, y que partes cambian juntas) y lo que gana y pierde; verifique que no escribio «un poco de los dos», porque eso vale cero.',
                  'Paso 2: modele en la pregunta 13 el C4 Container partiendo del C4 Context de la pregunta 3, con entre 2 y 5 contenedores coherentes con la decision anterior, los almacenes de datos como ContainerDb y toda flecha con protocolo y formato; verifique que los nombres de sistema, actores y sistemas externos sean identicos a los del Context.',
                  'Paso 3: liste en la pregunta 14 los 3 contratos con quien llama a quien usando los nombres exactos del diagrama, el verbo y la ruta (o el evento) y el error de negocio con su codigo y su significado en el dominio; verifique que al menos uno sea un 409 de conflicto y que ninguno diga «500 error del servidor».',
                  'Paso 4: analice en la pregunta 15 los tres riesgos de distribucion nombrando una caja concreta que se cae, contando los saltos de red de una operacion de punta a punta y nombrando un dato expuesto a inconsistencia; con esto la actividad del Corte 1 queda completa y se entrega en ExamLab antes del domingo 23:59 de esta semana.',
              ],
     'preguntas': [
                      {
                          'n_global': 12,
                          'tipo': 'abierta',
                          'puntos': 4.0,
                          'enunciado': '''## Monolito modular o microservicios para su CloudLite

Antes de dibujar las cajas hay que decidir si el sistema se parte o no. Escriba su decision
con esta estructura:

1. **La decision**, en una frase: **monolito modular** o **microservicios** para CloudLite.
2. **Dos criterios que la sustentan**, aplicados a su caso concreto:
   - **tamano del equipo**: cuantas personas sostienen el proyecto y durante cuanto tiempo;
   - **acoplamiento**: que partes de su dominio cambian juntas y cuales cambian por separado.
3. **Que gana y que pierde** con la decision: una de cada una, en terminos de su dominio.

> **Regla del curso:** doce microservicios para un equipo de tres es teatro, no
> arquitectura. Partir un sistema tiene un costo real —cada llamada de funcion se convierte
> en una llamada de red, con su latencia y su posibilidad de fallar— y ese costo hay que
> pagarlo con una razon. Un monolito modular bien argumentado vale exactamente lo mismo que
> microservicios bien argumentados; lo que no vale es partir por moda.

Esta decision es la que explica cuantas cajas tendra el diagrama de la pregunta 13: si
elige monolito modular, esas cajas son modulos dentro de un contenedor mas sus almacenes de
datos, no servicios sueltos.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt la decision nombrada en una frase, sin ambiguedad. 2 pts los dos criterios aplicados al caso: 1 pt tamano del equipo con numero y plazo, 1 pt acoplamiento diciendo que partes cambian juntas. 1 pt el que gana y que pierde en terminos del dominio. Cero en la decision si dice «un poco de los dos» o no elige. Elegir monolito modular NO se penaliza: se penaliza no sustentar.',
                      },
                      {
                          'n_global': 13,
                          'tipo': 'diagrama',
                          'puntos': 11.0,
                          'enunciado': '''## C4 Containers de CloudLite App

Modele el diagrama **C4 de nivel Container** de su CloudLite, en Mermaid. La primera linea
debe ser exactamente `C4Container`.

Parta del **C4 Context de la pregunta 3** y **reutilice exactamente los mismos nombres** de
sistema, de actores y de sistemas externos. Es el mismo sistema visto con mas zoom, no otro
sistema.

El diagrama debe tener:

- Entre **2 y 5** contenedores o servicios logicos dentro de la frontera del sistema, cada
  uno con su tecnologia entre parentesis y **coherente con la decision de la pregunta 12**.
- Los **almacenes de datos** como `ContainerDb(...)`.
- Los actores y los sistemas externos que ya estaban en el Context.
- **Cada flecha etiquetada con su protocolo y su formato**: `HTTPS/JSON`, `TCP/SQL`,
  `evento/cola`. Una flecha sin protocolo no cuenta.

> **Justifique cada caja.** Por cada contenedor tiene que poder responder dos preguntas: que
> responsabilidad de negocio propia tiene, y por que se despliega por separado. Si no puede
> responder las dos, esa caja no deberia existir. **Doce microservicios para un equipo de
> tres es teatro, no arquitectura.**

Estos nombres vuelven en el diagrama de despliegue de la Clase 7 y en el checkpoint de la
Clase 11: si aqui llama «api-prestamos» a un servicio, alla tiene que llamarse igual.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts entre 2 y 5 contenedores, cada uno con su tecnologia; se descuenta por cada caja de mas sin justificacion. 2 pts los almacenes de datos declarados como ContainerDb. 3 pts que TODA flecha lleve protocolo y formato. 2 pts que los nombres de sistema, actores y sistemas externos sean identicos a los del C4 Context de la pregunta 3. 1 pt que renderice sin error. Si el numero de cajas contradice la decision de la pregunta 12 (por ejemplo cinco servicios sueltos habiendo elegido monolito modular) se pierden los 3 pts de los contenedores.',
                          'mermaid_esperado': '''C4Container
    title Contenedores de CloudLite App - dominio AgendaU
    Person(estudiante, "Estudiante", "Reserva y cancela citas de asesoria")
    Person(coordinador, "Coordinador academico", "Publica cupos y revisa la ocupacion semanal")
    System_Boundary(cloudlite, "CloudLite App") {
        Container(spa, "Aplicacion web", "React", "Interfaz de reserva y de publicacion de cupos")
        Container(api, "API de agenda", "Node.js", "Reglas de reserva, cancelacion y cupos")
        ContainerDb(db, "Base de datos de agenda", "PostgreSQL", "Cupos, reservas y usuarios")
    }
    System_Ext(idp, "Proveedor de identidad institucional", "Login OIDC de la universidad")
    System_Ext(correo, "Correo transaccional SaaS", "Envio de confirmaciones y recordatorios")
    Rel(estudiante, spa, "Reserva y cancela citas", "HTTPS")
    Rel(coordinador, spa, "Publica cupos y consulta la ocupacion", "HTTPS")
    Rel(spa, api, "Consulta y modifica la agenda", "HTTPS/JSON")
    Rel(api, db, "Lee y escribe reservas y cupos", "TCP/SQL")
    Rel(api, idp, "Valida la identidad institucional", "OIDC sobre HTTPS")
    Rel(api, correo, "Solicita el envio de la confirmacion", "API REST sobre HTTPS")''',
                      },
                      {
                          'n_global': 14,
                          'tipo': 'abierta',
                          'puntos': 7.0,
                          'enunciado': '''## Los tres contratos de CloudLite

Liste **3 contratos** entre las piezas del diagrama de la pregunta 13. Un contrato es el
acuerdo de como se hablan dos partes, y aqui se escribe con **cuatro datos**:

| Contrato | Quien llama a quien | Verbo y ruta | Error de negocio |
|---|---|---|---|

- **Quien llama a quien**: los nombres exactos de las cajas del diagrama.
- **Verbo y ruta**: el verbo HTTP y la ruta (`POST /reservas`), o el **evento** si la
  comunicacion es asincrona (`evento reserva.creada`).
- **Error de negocio**: el codigo y **que significa en su dominio**. No vale «500 error del
  servidor»: eso es una falla, no un contrato. Se espera algo como
  `409 el cupo ya fue tomado por otro estudiante` o `422 la fecha esta fuera del periodo`.

> **Al menos uno de los tres errores debe ser un `409` de conflicto**, porque el conflicto
> es el error que aparece en cuanto dos usuarios hacen lo mismo a la vez, y es el que se
> retoma en la Clase 13 cuando se hable de concurrencia y escalado.

Un contrato sin su error solo describe el camino feliz, y el camino feliz nunca es el que
rompe el sistema.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts los tres contratos con quien llama a quien usando los nombres exactos del diagrama: 1 pt cada uno. 2 pts los verbos y rutas bien formados (o el evento, si es asincrono). 2 pts los errores de negocio con codigo y significado en el dominio; se pierde el punto del error si dice 500 o «error generico», y se pierde 1 pt del total si ninguno de los tres es un 409 de conflicto.',
                      },
                      {
                          'n_global': 15,
                          'tipo': 'abierta',
                          'puntos': 3.0,
                          'enunciado': '''## Riesgos de distribucion de su arquitectura

Toda frontera que dibujo en la pregunta 13 es una llamada de red, y una llamada de red puede
fallar, tardar o dejar los datos a medias. Analice **los tres riesgos** que introdujo su
propia arquitectura logica, en este orden:

1. **Que se rompe cuando una pieza no responde.** Elija **una** caja concreta de su
   diagrama, digala por su nombre, y describa que deja de funcionar y que sigue funcionando
   si esa pieza se cae. La respuesta interesante no es «se cae todo»: es cual capacidad de
   su ficha queda inservible y cual no.
2. **Que latencia agrega cada salto.** Cuente los saltos de red de **una** operacion
   completa de su dominio, de punta a punta, y diga cuantos son. No hace falta medir: hace
   falta contar y darse cuenta de que antes eran cero.
3. **Que datos quedan expuestos a inconsistencia.** Nombre **un** dato que viva en dos
   sitios o que se actualice en dos pasos, y que pasaria si el segundo paso falla.

> Si su decision de la pregunta 12 fue **monolito modular**, esta pregunta sigue aplicando:
> los saltos hacia la base de datos y hacia los sistemas externos son igualmente red, y el
> riesgo 3 existe en cuanto haya dos escrituras que deban ocurrir juntas.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt el riesgo de indisponibilidad nombrando una caja concreta y distinguiendo que deja de funcionar de que sigue funcionando; media respuesta si dice «se cae todo». 1 pt el conteo de saltos de una operacion de punta a punta. 1 pt el dato expuesto a inconsistencia, nombrado, con lo que pasa si falla el segundo paso. Una respuesta generica sobre «los microservicios son mas complejos» no suma en ningun criterio.',
                      },
                  ],
     'resumen': '''Las preguntas 12 a 15 de la actividad del Corte 1, que la cierran. El estudiante decide si parte el sistema, modela el C4 Container reutilizando los nombres del Context, define 3 contratos con su error de negocio y analiza los riesgos que introdujo al distribuir.''',
     'titulo': '''Actividad del Corte 1 (preguntas 12 a 15) - C4 Containers, contratos y riesgos'''},
 6: {'pasos': [
                  'Paso 1: liste en la pregunta 1 cinco amenazas de SU dominio, cada una nombrando el actor o el dato concreto que pone en riesgo y el camino por el que ocurre; use STRIDE como guia de categorias y verifique que ninguna sea una frase de manual que sirva igual para cualquier sistema.',
                  'Paso 2: complete en la pregunta 2 la tabla amenaza-control-donde, senalando para cada control la caja o la flecha concreta del C4 Containers o del Despliegue donde se ve; incluya el principio de menor privilegio aplicado a un componente, diciendo que deja de poder hacer.',
                  'Paso 3: escriba en la pregunta 3 la politica de secretos respondiendo donde viven, quien los rota, cada cuanto y que esta prohibido, y cierre con el procedimiento ante una filtracion; verifique que su politica no admita secretos en el Dockerfile, el README ni el YAML en claro.',
                  'Paso 4: guarde y continue. Esta actividad es una sola para las Clases 6, 7, 8 y 10 y se entrega completa al cierre del Corte 2: hoy resuelve las preguntas 1 a 3 y las 4 a 12 se resuelven en las clases siguientes.',
              ],
     'preguntas': [
                      {
                          'n_global': 1,
                          'tipo': 'abierta',
                          'puntos': 8.75,
                          'enunciado': '''## Cinco amenazas STRIDE-lite de SU dominio

Liste **5 amenazas** aplicadas a su CloudLite. **No una lista generica copiada de
internet**: cada amenaza tiene que nombrar **el actor o el dato concreto de su dominio** que
pone en riesgo.

Use STRIDE como guia de categorias: **S**poofing (suplantacion), **T**ampering (alteracion),
**R**epudiation (negacion), **I**nformation disclosure (fuga), **D**enial of service y
**E**levation of privilege. No hacen falta las seis: hacen falta cinco amenazas reales.

Amenazas tipicas del curso, como referencia de la **forma** esperada, no para copiarlas:

- secretos dentro de la imagen del contenedor
- API sin autenticacion
- registros que guardan tokens
- datos personales viajando sin TLS

> La diferencia entre una amenaza y una frase de manual es el complemento. «Fuga de
> informacion» no es una amenaza; «un estudiante puede consultar por identificador las
> reservas de otro porque el endpoint no valida a quien pertenece» si lo es, porque nombra
> al actor, el dato y el camino.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1.75 pts por amenaza bien formada, hasta 5. Una amenaza suma completo solo si nombra el actor o el dato concreto del dominio y el camino por el que ocurre. Una amenaza generica («podrian hackear la base de datos») vale la mitad. Se descuenta si dos amenazas son la misma con otras palabras.',
                      },
                      {
                          'n_global': 2,
                          'tipo': 'abierta',
                          'puntos': 8.75,
                          'enunciado': '''## El control de cada amenaza y donde se ve

Para **cada una de las 5 amenazas** de la pregunta anterior indique:

1. **El CONTROL que la mitiga.** Concreto y verificable, no «mejorar la seguridad».
2. **DONDE se ve ese control en sus diagramas**: sobre que **caja** o sobre que **flecha**
   del C4 Containers o del diagrama de Despliegue aplica.

Presentelo como tabla: `Amenaza | Control | Donde se ve (caja o flecha)`.

**Debe aparecer el principio de menor privilegio**, aunque sea narrado: que cada componente
y cada rol reciba exactamente los permisos que necesita y ni uno mas. Diga sobre que
componente de SU sistema lo aplica y que deja de poder hacer al aplicarlo.

> Un control que no se puede senalar en un artefacto no existe todavia: es una intencion.
> Por eso la segunda columna vale tanto como la primera. Si no encuentra donde ubicarlo,
> probablemente le falta una caja o una frontera en el diagrama.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt por cada control concreto y verificable, hasta 5. 2.5 pts por senalar correctamente la caja o la flecha de cada uno; se prorratea. 1.25 pts por el principio de menor privilegio aplicado a un componente concreto, diciendo que deja de poder hacer. Un control tipo «usar buenas practicas» no suma.',
                      },
                      {
                          'n_global': 3,
                          'tipo': 'abierta',
                          'puntos': 7.5,
                          'enunciado': '''## Politica de secretos del repositorio y de la CI

Defina la politica de secretos de CloudLite respondiendo estas cuatro preguntas:

1. **Donde viven** los secretos.
2. **Quien los rota**.
3. **Con que frecuencia** se rotan.
4. **Que esta explicitamente prohibido**.

> **Regla del curso:** los secretos van en la **configuracion del repositorio** (los
> `secrets` del proyecto), **nunca** en el `Dockerfile`, en el `README` ni en el YAML en
> claro. Un secreto escrito en el Dockerfile queda en el **historial de capas** de la imagen
> para siempre: cualquiera que tenga la imagen lo lee, aunque el archivo se borre en una
> capa posterior.

Cierre nombrando **que haria si un secreto se filtra**: el primer paso no es borrar el
commit, es **rotar la credencial**, porque el historial ya salio del equipo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1.5 pts cada una de las cuatro preguntas respondida de forma concreta (donde, quien, cada cuanto, que se prohibe): 6 pts. 1.5 pts el procedimiento ante filtracion empezando por rotar la credencial y no por borrar el commit. Cero en la primera pregunta si la respuesta admite guardar secretos en el repositorio en claro.',
                      },
                  ],
     'resumen': '''Las preguntas 1 a 3 de la actividad del Corte 2, que es una sola para las Clases 6, 7, 8 y 10. El estudiante deja el modelo de amenazas de su dominio con sus controles ubicados en los diagramas y la politica de secretos escrita.''',
     'titulo': '''Actividad del Corte 2 (preguntas 1 a 3) - Amenazas, controles y secretos'''},
 7: {'pasos': [
                  'Paso 1: dibuje primero el boceto del despliegue en Excalidraw o draw.io con las tres zonas (publica, privada y de datos), y despues pidale a una IA que lo traduzca a Mermaid; peguelo en la pregunta 4 y verifique en el diagrama ya renderizado que la base de datos NO quede en la zona publica.',
                  'Paso 2: etiquete en ese mismo diagrama el puerto de cada componente y marque las fronteras de confianza, es decir donde termina lo que usted controla; verifique que no aparezcan nombres de subredes ni de servicios de un proveedor concreto.',
                  'Paso 3: justifique en la pregunta 5 el tipo de almacenamiento de cada componente diciendo que caracteristica del dato lo exige; si su dominio no necesita almacenamiento de objetos, declarelo y justifiquelo en vez de agregarlo.',
                  'Paso 4: complete en la pregunta 6 la tabla de correspondencia entre el C4 Containers y el Despliegue, con una fila por componente y su zona, y liste los renombres que aplico; si no hubo ninguno, digalo explicitamente.',
              ],
     'preguntas': [
                      {
                          'n_global': 4,
                          'tipo': 'diagrama',
                          'puntos': 14.0,
                          'enunciado': '''## Diagrama de Despliegue de CloudLite

Modele en Mermaid el diagrama de **Despliegue** de su CloudLite, con sus **tres zonas** y
el flujo completo **Cliente -> edge -> aplicacion -> datos**.

Debe tener:

- Las **tres zonas** como fronteras explicitas: **publica**, **privada** y **de datos**.
- Cada componente **ubicado en su zona**. **La base de datos NO puede quedar en la zona
  publica**: es el error que la pregunta busca detectar.
- Las **fronteras de confianza** marcadas: donde termina lo que usted controla y empieza lo
  que no.
- **El puerto de cada componente** etiquetado.

> **No invente subredes de un proveedor concreto.** Nada de nombres de VPC, de
> disponibilidad ni de servicios de marca: el diagrama es conceptual y tiene que servir
> igual en cualquier proveedor. El curso no abre cuentas de nube de pago.

Reutilice **los mismos nombres** de componentes del C4 Containers del Corte 1: es el mismo
sistema visto desde donde se ejecuta.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '4 pts las tres zonas presentes y rotuladas. 4 pts cada componente en la zona que le corresponde; **se pierden los 4 completos si la base de datos queda en la zona publica**. 2 pts las fronteras de confianza marcadas. 2 pts el puerto de cada componente. 2 pts que renderice sin error. Se descuenta por nombrar subredes o servicios de un proveedor concreto.',
                          'mermaid_esperado': '''flowchart LR
    subgraph publica["Zona publica - internet"]
        cliente["Cliente / navegador"]
        edge["Edge / balanceador<br/>443 HTTPS"]
    end
    subgraph privada["Zona privada - solo alcanzable desde el edge"]
        api["API de agenda<br/>8080 HTTP"]
    end
    subgraph datos["Zona de datos - sin salida a internet"]
        db[("Base de datos<br/>5432 TCP")]
    end
    ext["Correo transaccional SaaS<br/>externo"]
    cliente -->|"HTTPS 443"| edge
    edge -->|"HTTP 8080"| api
    api -->|"TCP 5432"| db
    api -->|"HTTPS 443 - frontera de confianza"| ext''',
                      },
                      {
                          'n_global': 5,
                          'tipo': 'abierta',
                          'puntos': 5.5,
                          'enunciado': '''## Tipo de almacenamiento de cada componente

Justifique **que tipo de almacenamiento** le corresponde a cada componente de su
despliegue, a nivel conceptual:

- **Relacional**: datos con relaciones y consultas que los cruzan.
- **Bloque**: un disco crudo que un solo proceso monta y escribe.
- **Objeto**: archivos completos que se guardan y se recuperan enteros, por su nombre.

Para cada componente diga **que caracteristica del dato lo exige**, no que tipo le gusta
mas. Formato: `Componente | Tipo | Que caracteristica del dato lo exige`.

> **Use almacenamiento de objetos solo si su dominio realmente lo necesita.** Si no maneja
> archivos, imagenes ni documentos adjuntos, no lo incluya: agregar un almacen de objetos
> «porque suena a cloud» es exactamente el tipo de decision que este curso pide justificar.
> Decir «mi dominio no necesita objeto, y por eso no lo tengo» es una respuesta correcta y
> completa.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '3 pts la clasificacion correcta de cada componente del despliegue. 2.5 pts que cada justificacion nombre la caracteristica del dato (se cruza con otros, lo monta un solo proceso, se recupera entero) y no una preferencia. Suma completo quien declare que su dominio no necesita almacenamiento de objetos y lo justifique; se descuenta quien lo incluya sin un dato que lo pida.',
                      },
                      {
                          'n_global': 6,
                          'tipo': 'abierta',
                          'puntos': 5.5,
                          'enunciado': '''## Correspondencia entre el C4 Containers y el Despliegue

Explique **por que** los nombres del diagrama de Despliegue tienen que ser **exactamente los
mismos** del C4 Containers, y demuestrelo con la tabla de correspondencia:

`Componente en el C4 Containers | Componente en el Despliegue | Zona`

Si al dibujar el despliegue **renombro** algo, **liste los renombres** que aplico y diga
cual de los dos diagramas actualizo para que queden iguales.

> Los dos diagramas son **el mismo sistema visto desde angulos distintos**: el C4 Containers
> muestra que piezas hay y el Despliegue donde se ejecutan. Si una pieza se llama
> «api-agenda» en uno y «servidor-backend» en otro, nadie puede saber si son la misma cosa,
> y en la sustentacion de la Clase 15 eso se lee como dos sistemas distintos.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2 pts la explicacion de por que los nombres deben coincidir, en terminos de que son el mismo sistema. 2.5 pts la tabla completa con una fila por componente y su zona. 1 pt listar los renombres aplicados, o declarar explicitamente que no hubo ninguno. Se descuenta si la tabla deja fuera algun componente que si aparece en alguno de los dos diagramas.',
                      },
                  ],
     'resumen': '''Las preguntas 4 a 6 de la actividad del Corte 2. El estudiante deja el diagrama de Despliegue con sus tres zonas, justifica el almacenamiento de cada componente y demuestra que los nombres coinciden con el C4 Containers del Corte 1.''',
     'titulo': '''Actividad del Corte 2 (preguntas 4 a 6) - Despliegue, almacenamiento y nombres'''},
 8: {'pasos': [
                  'Paso 1: escriba en la pregunta 7 el contenido completo del ci.yml con disparadores, entorno y los pasos de construccion, prueba y despliegue simulado, usando la imagen y el puerto del Dockerfile del Corte 1; verifique que ningun secreto quede escrito en claro dentro del YAML.',
                  'Paso 2: explique en la pregunta 8 que se compila o instala, que se ejecuta en la prueba y con que condicion el pipeline debe fallar; hagase la prueba mental de que error tendria que introducir para que el check salga rojo, y si no encuentra ninguno, su pipeline todavia no valida nada.',
                  'Paso 3: distinga en la pregunta 9 que valida CI y que hace CD, ubique cual de los dos construyo y diga que le faltaria para CD real; reconocer que su pipeline llega hasta «listo para desplegar» suma puntos, afirmar que ya tiene CD los resta.',
                  'Paso 4: liste en la pregunta 10 entre 4 y 6 senales con su umbral, atadas a operaciones de su dominio, y verifique que al menos una sea un registro y no una metrica numerica; una senal sin umbral no sirve para operar y no suma.',
              ],
     'preguntas': [
                      {
                          'n_global': 7,
                          'tipo': 'abierta',
                          'puntos': 10.0,
                          'enunciado': '''## El workflow de integracion continua

Escriba el **contenido completo** del archivo `.github/workflows/ci.yml` para el stub de
CloudLite. Debe incluir:

1. **Disparadores** (`on`): cuando corre el pipeline.
2. **Entorno de ejecucion** (`runs-on`).
3. **Pasos** de **construccion**, **prueba** y **despliegue simulado**.

> **Los secretos se referencian desde la configuracion del repositorio**, con la sintaxis de
> *secrets* del proyecto, **nunca escritos en claro dentro del YAML**. Es la misma politica
> que definio en la pregunta 3.

El **despliegue simulado** es deliberado: en este curso el pipeline llega hasta «listo para
desplegar» y no despliega a ningun servidor real, porque no abrimos cuentas de nube de pago.
Dejelo explicito en el nombre del paso para no prometer lo que no hace.

Use la imagen y el puerto **del Dockerfile que escribio en el Corte 1**: es el mismo
servicio.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '2 pts los disparadores declarados. 1.5 pts el entorno de ejecucion. 4 pts los tres pasos presentes y en orden (construccion, prueba, despliegue simulado). 1.5 pts que el despliegue este rotulado como simulado y no prometa un despliegue real. 1 pt coherencia con el Dockerfile del Corte 1 (misma imagen, mismo puerto). **Cero en toda la pregunta si aparece un secreto escrito en claro en el YAML.**',
                      },
                      {
                          'n_global': 8,
                          'tipo': 'abierta',
                          'puntos': 5.0,
                          'enunciado': '''## Que hace realmente su paso de construccion y prueba

Explique, sobre **su propio** `ci.yml`:

1. **Que se compila o se instala** en el paso de construccion.
2. **Que se ejecuta** en el paso de prueba: que comprueba exactamente.
3. **Con que condicion el pipeline debe FALLAR**: que tiene que pasar para que el check
   salga rojo.

> **Un CI que solo imprime un mensaje de exito no es CI.** Si su pipeline no puede fallar
> nunca, no esta validando nada: es una decoracion verde. La pregunta que hay que poder
> responder es «que error tendria que introducir yo en el codigo para que este pipeline lo
> detecte», y su respuesta tiene que decirlo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1.5 pts que se compila o instala. 1.5 pts que se ejecuta en la prueba y que comprueba. 2 pts la condicion de fallo, expresada como algo que el pipeline detectaria. **Cero en la condicion de fallo si el pipeline no puede fallar nunca** (solo `echo`, o pruebas que siempre pasan): es el criterio central de la pregunta.',
                      },
                      {
                          'n_global': 9,
                          'tipo': 'abierta',
                          'puntos': 4.0,
                          'enunciado': '''## Hasta donde llega su pipeline: CI, CD y lo que es realista aqui

Distinga los dos terminos y ubique su propio trabajo:

1. **Que valida la integracion continua (CI)** y en que momento del ciclo actua.
2. **Que hace la entrega o despliegue continuo (CD)**, y en que se diferencia de lo
   anterior.
3. **Cual de los dos construyo usted hoy**, y hasta que punto exacto llega su `ci.yml`.
4. **Que le faltaria** para tener CD de verdad, y **por que este curso no lo pide**.

> La frontera importa mas de lo que parece: decir «ya tenemos CD» porque el YAML tiene un
> paso llamado `deploy` es de las afirmaciones que un evaluador tumba en dos preguntas. En
> este curso el despliegue **se simula**, y decirlo asi no resta puntos: los suma, porque
> demuestra que sabe donde esta el limite de lo que construyo.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt la definicion de CI atada a cuando actua. 1 pt la de CD y su diferencia. 1 pt ubicar correctamente su propio trabajo, reconociendo que llega hasta «listo para desplegar». 1 pt lo que faltaria para CD real y por que el curso no lo exige. Se descuenta la mitad si afirma haber construido CD.',
                      },
                      {
                          'n_global': 10,
                          'tipo': 'abierta',
                          'puntos': 6.0,
                          'enunciado': '''## Metricas y registros de CloudLite en produccion

Liste entre **4 y 6 metricas o registros** que observaria en la produccion hipotetica de su
CloudLite, **cada una con su umbral u objetivo**.

Orientacion: use las **senales doradas** en version reducida, aterrizadas a su dominio:

- **Latencia**: cuanto tarda la operacion que mas se usa.
- **Trafico**: cuantas peticiones u operaciones por unidad de tiempo.
- **Errores**: que proporcion falla, y cuales cuentan como fallo de negocio.
- **Saturacion**: que recurso se agota primero.

Formato: `Senal | Que se mide en MI dominio | Umbral u objetivo`.

> **Una metrica sin umbral no sirve para operar.** «Medimos la latencia» no permite decidir
> nada; «el listado de disponibilidad debe responder en menos de 400 ms y si pasa de 800 ms
> se revisa» si, porque define cuando hay que actuar. El umbral puede ser discutible; lo que
> no puede es faltar.

Al menos una de las senales debe ser un **registro** y no una metrica numerica: algo que se
escribe para poder reconstruir que paso despues.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                          'rubrica': '1 pt por senal bien formada con su umbral, hasta 4 senales; las senales 5 y 6 suman hasta 1 pt adicional entre las dos. 1 pt que al menos una sea un registro y no una metrica numerica. **Una senal sin umbral no suma**, aunque este bien elegida. Se descuenta si las senales no se refieren a operaciones del dominio propio.',
                      },
                  ],
     'resumen': '''Las preguntas 7 a 10 de la actividad del Corte 2. El estudiante escribe el workflow de CI de su stub, explica que valida de verdad, ubica hasta donde llega su pipeline y define las senales con las que operaria CloudLite.''',
     'titulo': '''Actividad del Corte 2 (preguntas 7 a 10) - Integracion continua y monitoreo'''},
 10: {'pasos': [
                   'Paso 1: construya en la pregunta 11 la tabla de costos con una fila por cada componente de su despliegue y las columnas componente, driver, nivel B/M/A y apalancamiento; verifique que cada driver sea una variable contable (horas encendidas, GB de salida, GB almacenados, minutos de CI) y no «el uso».',
                   'Paso 2: fuerce al menos un Alto y un Bajo con su justificacion. Marcar todo como Medio para no decidir es lo que la pregunta busca descartar, y ese criterio vale cero si todas las filas quedan iguales.',
                   'Paso 3: escriba en la pregunta 12 tres acciones de sostenibilidad, cada una con el artefacto donde se comprueba y como se comprueba; aplique la prueba de que otra persona pueda decir en seis meses, mirando el repositorio, si la accion se aplico.',
                   'Paso 4: ate al menos una de las tres acciones a un driver de costo de la pregunta 11 y suba la actividad completa del Corte 2 a ExamLab antes del domingo 23:59. Es una clase autonoma: no hay encuentro sincrono, y las dudas van por el foro.',
               ],
      'preguntas': [
                       {
                           'n_global': 11,
                           'tipo': 'abierta',
                           'puntos': 16.25,
                           'enunciado': '''## Tabla de costos de CloudLite

Construya la tabla de costos con **una fila por componente** —API, base de datos,
almacenamiento de objetos si lo tiene, integracion continua y edge— y **estas cuatro
columnas**:

`Componente | Driver de costo | Nivel B/M/A | Apalancamiento`

- **Driver de costo**: la variable concreta que, si crece, hace crecer la factura de ese
  componente. Drivers a considerar: **tiempo inactivo** (instancias encendidas sin trabajo),
  **transferencia de salida**, **almacenamiento** y **minutos de CI**.
- **Nivel**: **B**ajo, **M**edio o **A**lto. Es una escala **ordinal**: ordena, no mide
  distancias. Decir que la base de datos es Alto y el edge es Bajo afirma que una cuesta mas
  que la otra, no cuantas veces mas.
- **Apalancamiento**: **que palanca concreta baja ese costo**. No «optimizar»: algo que se
  pueda hacer y comprobar.

> **Prohibido inventar precios en dolares o facturas de un proveedor.** La estimacion es
> **cualitativa B/M/A**. Un componente al que no le sabe poner driver es un componente que
> todavia no entiende: vuelva al diagrama antes de escribir la fila.

**Fuerce al menos un Alto y un Bajo.** Marcar todo como «Medio» para no pensar es la
respuesta que esta pregunta busca descartar.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                           'rubrica': '4 pts una fila por cada componente del despliegue, sin dejar ninguno fuera. 5 pts los drivers: cada uno tiene que ser una variable contable (horas encendidas, GB de salida, GB almacenados, minutos de CI) y no «el uso». 3.25 pts los niveles, con al menos un Alto y un Bajo justificados; si todo es Medio, este criterio vale cero. 4 pts los apalancamientos, uno por fila, concretos y comprobables. **Se descuenta fuerte por inventar precios en dolares**: la escala es cualitativa.',
                       },
                       {
                           'n_global': 12,
                           'tipo': 'abierta',
                           'puntos': 8.75,
                           'enunciado': '''## Tres acciones de sostenibilidad tecnica

Proponga **3 acciones de sostenibilidad tecnica** aplicables al diseno de CloudLite. La
condicion que las hace validas es que sean **verificables en el propio diseno**: debe poder
comprobarse **si se aplico o no** mirando los artefactos del sistema.

Para cada accion escriba: `Accion | En que artefacto se comprueba | Como se comprueba`.

Ejemplos de la **forma** esperada, no para copiarlos:

- apagar los laboratorios al terminar la sesion — se comprueba en la bitacora del lab;
- usar imagenes base ligeras — se comprueba en la primera linea del `Dockerfile`;
- no sobredimensionar instancias — se comprueba en la politica de escalado.

> Una accion como «ser mas eficientes» o «concientizar al equipo» no se puede comprobar
> mirando un artefacto, y por eso no cuenta. La prueba: si otra persona abre su repositorio
> dentro de seis meses, ¿puede decir si la accion se aplico? Si la respuesta es no, todavia
> es una intencion.

Ate al menos una de las tres a un **driver de costo** de la tabla anterior: sostenibilidad y
costo suelen apalancarse con la misma decision.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.''',
                           'rubrica': '2.5 pts por accion verificable, hasta 3 acciones: suma completo solo si nombra el artefacto y como se comprueba. 1.25 pts por atar al menos una accion a un driver de costo de la pregunta 11. Una accion que no se pueda comprobar mirando un artefacto vale cero, aunque sea razonable.',
                       },
                   ],
      'resumen': '''Las preguntas 11 y 12 de la actividad del Corte 2, que la cierran. Clase autonoma: el estudiante construye la tabla de costos cualitativa de CloudLite y propone tres acciones de sostenibilidad verificables en sus propios artefactos.''',
      'titulo': '''Actividad del Corte 2 (preguntas 11 y 12) - Costos y sostenibilidad'''},
 11: {'pasos': ['Paso 1: completen el checklist de 10 filas del paquete v1 marcando cada evidencia '
                'como si, no o parcial y pegando la ruta o el enlace exacto de cada una, '
                'verificando que ninguna fila marcada como si quede sin ruta verificable, porque '
                'una fila sin enlace se califica como no.',
                'Paso 2: hagan la reconciliacion de nombres llenando la tabla de 5 filas que '
                'compara como se llama cada elemento en el C4Container, en el C4Deployment, en el '
                'Dockerfile o el ci.yml y en el informe, verificando que la columna de nombre '
                'canonico sea identica en las cuatro y aplicando la correccion en el artefacto que '
                'este desalineado.',
                'Paso 3: escriban en ExamLab el diagrama C4Component del interior de la API con 5 '
                'componentes y sus relaciones hacia la base de datos, la cola y el proveedor de '
                'identidad, verificando al renderizar que ningun componente sea un contenedor de '
                'la Clase 4 disfrazado y que el contenedor contenedor de la frontera se llame '
                'igual que en el C4Container.',
                'Paso 4: escriban el backlog de 5 items priorizados hacia la Clase 12 con hueco '
                'detectado, accion, responsable y fecha, verificando que cada item se pueda cerrar '
                'en una semana y que al menos uno provenga del feedback del docente recibido hoy '
                'en la cola de revision.',
                'Paso 5: empaqueten el ZIP o el repositorio con los diagramas, el Dockerfile, el '
                'ci.yml y el informe al 60 por ciento, y suban las 5 preguntas a ExamLab (modulo '
                'Talleres) antes del domingo 23:59, verificando que el paquete se pueda abrir en '
                'otra maquina y que el informe enlace cada evidencia por su ruta dentro del '
                'paquete.'],
      'preguntas': [{'enunciado': '## Checklist del paquete v1\n'
                                  '\n'
                                  'Construya una tabla de **4 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Evidencia | Estado si/no/parcial | Ruta o enlace exacto | '
                                  'Responsable`\n'
                                  '\n'
                                  'con **exactamente 10 filas**, en este orden:\n'
                                  '\n'
                                  '1. Ficha de dominio con 4 capacidades (Clase 1).\n'
                                  '2. Diagrama C4 Context (Clase 1).\n'
                                  '3. ADR-001 del modelo de servicio (Clase 2).\n'
                                  '4. Dockerfile del stub y evidencia del lab (Clase 3).\n'
                                  '5. Diagrama C4 Container y tabla de 3 contratos (Clase 4).\n'
                                  '6. Modelo de amenazas y politica de secretos (Clase 6).\n'
                                  '7. Diagrama C4 Deployment con zonas y almacenamiento (Clase '
                                  '7).\n'
                                  '8. Workflow ci.yml con enlace al run verde (Clase 8).\n'
                                  '9. Seccion de costos y sostenibilidad (Clase 10).\n'
                                  '10. Informe del PI al 60 por ciento o mas.\n'
                                  '\n'
                                  'Reglas de verificacion:\n'
                                  '- Toda fila marcada `si` **debe** llevar ruta dentro del '
                                  'paquete (`/diagramas/c4-container.png`) o enlace publico. **Una '
                                  'fila `si` sin ruta se califica como `no`.**\n'
                                  '- Toda fila `parcial` o `no` debe indicar en la columna '
                                  '`Responsable` **quien lo cierra y en que fecha**.\n'
                                  '\n'
                                  'Cierre con **una linea**: cuantas filas quedaron en `si` sobre '
                                  '10.',
                     'puntos': 25,
                     'rubrica': '10 pts las 10 filas presentes en el orden pedido. 8 pts que cada '
                                'si tenga ruta o enlace verificable. 5 pts que cada parcial o no '
                                'tenga responsable y fecha de cierre. 2 pts el conteo final. Se '
                                'descuentan 2 pts por cada si sin ruta.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Reconciliacion de nombres entre artefactos\n'
                                  '\n'
                                  'El hueco mas comun del PI: el diagrama llama `Servicio de '
                                  'reservas` a lo que el despliegue llama `api-citas` y el '
                                  'pipeline llama `app`. Corrijalo hoy.\n'
                                  '\n'
                                  'Construya una tabla de **5 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Nombre canonico | Como aparece en el C4 Container | Como '
                                  'aparece en el C4 Deployment | Como aparece en el Dockerfile o '
                                  'ci.yml | Correccion aplicada`\n'
                                  '\n'
                                  'con **exactamente 5 filas**, una por cada elemento de su lista '
                                  'canonica de la Clase 4 (interfaz web, API, procesador '
                                  'asincrono, base de datos, cola).\n'
                                  '\n'
                                  'Reglas:\n'
                                  '- La columna `Nombre canonico` es la que manda y **debe quedar '
                                  'igual en las tres columnas del medio** al terminar el '
                                  'ejercicio.\n'
                                  '- La columna `Correccion aplicada` dice **que archivo edito** '
                                  '(`renombre el servicio en docker-compose.yml y en el ci.yml`) o '
                                  '`sin cambios` si ya coincidia.\n'
                                  '- Si un elemento no aparece en algun artefacto, escriba `no '
                                  'aplica` **y justifique en media linea** por que no aplica.\n'
                                  '\n'
                                  'Cierre con **una linea**: cuantas correcciones aplico en total.',
                     'puntos': 20,
                     'rubrica': '8 pts las 5 filas con las 5 columnas. 6 pts que el nombre '
                                'canonico quede identico en las tres columnas de artefactos al '
                                'final. 4 pts la columna de correccion citando el archivo editado. '
                                '2 pts las justificaciones de no aplica y el conteo final.',
                     'tipo': 'abierta'},
                    {'enunciado': '## C4 Component: por dentro de la API CloudLite\n'
                                  '\n'
                                  'Hasta ahora la API era una caja. Abrala. Escriba en Mermaid un '
                                  'diagrama **C4Component**. La primera linea debe ser exactamente '
                                  '`C4Component`. Debe contener:\n'
                                  '\n'
                                  '- Un `Container_Boundary(...)` con **el mismo nombre y '
                                  'tecnologia** que su API en el C4Container de la Clase 4.\n'
                                  '- **Exactamente 5 `Component(...)`** dentro de la frontera, '
                                  'cada uno con nombre, tecnologia y responsabilidad en una frase. '
                                  'Deben cubrir estas 5 responsabilidades: (1) recibir y validar '
                                  'la peticion HTTP, (2) verificar el token de identidad, (3) '
                                  'aplicar la regla de negocio principal de su dominio, (4) '
                                  'encapsular el acceso a datos, (5) publicar el evento '
                                  'asincrono.\n'
                                  '- Fuera de la frontera: la interfaz web como `Container(...)`, '
                                  'la base de datos como `ContainerDb(...)`, la cola como '
                                  '`ContainerQueue(...)` y el proveedor de identidad como '
                                  '`System_Ext(...)`, todos con **los nombres canonicos** de su '
                                  'tabla de reconciliacion.\n'
                                  '- Exactamente **8 `Rel(...)`**.\n'
                                  '\n'
                                  '**Verificacion:** ninguno de los 5 componentes puede ser un '
                                  'contenedor de la Clase 4 disfrazado (si un componente es la '
                                  'base de datos, esta mal); el flujo debe poder leerse desde la '
                                  'interfaz web hasta la base de datos pasando por los 5 '
                                  'componentes.',
                     'mermaid_esperado': 'C4Component\n'
                                         '    title Componentes internos de la API CloudLite\n'
                                         '    Container(spa, "SPA Web", "HTML y JavaScript", '
                                         '"Cliente de la API de CloudLite")\n'
                                         '    Container_Boundary(api, "API CloudLite - Python '
                                         'FastAPI") {\n'
                                         '        Component(router, "Router HTTP de /citas y '
                                         '/cupos", "FastAPI APIRouter", "Recibe la peticion y '
                                         'valida el esquema de entrada")\n'
                                         '        Component(auth, "Verificador de token", '
                                         '"Libreria de JWT", "Valida la firma y la expiracion del '
                                         'token del proveedor de identidad")\n'
                                         '        Component(reglas, "Servicio de reglas de '
                                         'reserva", "Python", "Evita la doble reserva y aplica el '
                                         'cupo maximo por estudiante")\n'
                                         '        Component(repo, "Repositorio de Citas", '
                                         '"SQLAlchemy", "Encapsula el acceso SQL a la base de '
                                         'datos")\n'
                                         '        Component(pub, "Publicador de eventos", "Cliente '
                                         'de Redis", "Publica el evento cita_confirmada en la '
                                         'cola")\n'
                                         '    }\n'
                                         '    ContainerDb(db, "Base de datos Citas", "PostgreSQL '
                                         '16", "Cupos y citas confirmadas")\n'
                                         '    ContainerQueue(cola, "Cola Notificaciones", "Redis '
                                         'Streams", "Eventos de notificacion")\n'
                                         '    System_Ext(idp, "Proveedor de identidad '
                                         'institucional", "Login OIDC de la universidad")\n'
                                         '    Rel(spa, router, "POST /citas y GET /cupos", "JSON '
                                         'sobre HTTPS")\n'
                                         '    Rel(router, auth, "Delega la validacion del token")\n'
                                         '    Rel(auth, idp, "Descarga las claves publicas de '
                                         'firma", "HTTPS")\n'
                                         '    Rel(router, reglas, "Invoca crear_cita con el id del '
                                         'cupo")\n'
                                         '    Rel(reglas, repo, "Consulta el cupo y guarda la '
                                         'cita")\n'
                                         '    Rel(repo, db, "SQL 5432")\n'
                                         '    Rel(reglas, pub, "Emite el evento cita_confirmada")\n'
                                         '    Rel(pub, cola, "XADD en 6379")',
                     'puntos': 25,
                     'rubrica': '10 pts los 5 componentes dentro de la frontera con nombre '
                                'tecnologia y responsabilidad, cubriendo las 5 responsabilidades '
                                'pedidas. 6 pts los 4 elementos externos con los nombres canonicos '
                                'y los tipos correctos. 6 pts las 8 relaciones formando un flujo '
                                'legible de punta a punta. 3 pts que renderice sin error. Se '
                                'descuentan 10 pts si un componente es en realidad un contenedor '
                                'de la Clase 4.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## Backlog de 5 items hacia la Clase 12\n'
                                  '\n'
                                  'Construya una tabla de **5 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`ID | Hueco detectado | Accion concreta | Responsable | Fecha '
                                  'de cierre`\n'
                                  '\n'
                                  'con **exactamente 5 filas**, con IDs `B-01` a `B-05`, ordenadas '
                                  'de mayor a menor prioridad.\n'
                                  '\n'
                                  'Reglas:\n'
                                  '- Cada `Hueco detectado` debe citar **la evidencia y la clase '
                                  'de origen** (`el ci.yml no tiene pruebas reales - Clase 8`).\n'
                                  '- Cada `Accion concreta` debe poder cerrarse **en una semana** '
                                  'y empezar con un verbo (`agregar`, `renombrar`, `documentar`, '
                                  '`capturar`).\n'
                                  '- Al menos **un item debe provenir del feedback del docente** '
                                  'recibido hoy: marquelo con `[docente]`.\n'
                                  '- Las 5 fechas deben ser **anteriores a la Clase 12** y estar '
                                  'escritas como fecha real.\n'
                                  '\n'
                                  'Cierre con **2 lineas**: cual item bloquea a los demas si no se '
                                  'cierra, y que item decidieron **no** hacer y por que (deuda '
                                  'tecnica aceptada).',
                     'puntos': 20,
                     'rubrica': '8 pts las 5 filas con IDs y las 5 columnas completas. 5 pts que '
                                'cada hueco cite evidencia y clase de origen. 4 pts que al menos '
                                'un item venga del feedback del docente y que las 5 fechas sean '
                                'previas a la Clase 12. 3 pts las 2 lineas de cierre con el '
                                'bloqueante y la deuda aceptada.',
                     'tipo': 'abierta'},
                    {'correctas': [0, 1, 3],
                     'enunciado': '## Huecos tipicos del paquete v1\n'
                                  '\n'
                                  'Seleccione las **3 situaciones que son huecos** que hay que '
                                  'corregir antes de la Clase 12.',
                     'opciones': ['El C4 llama Servicio de reservas a la caja que en el despliegue '
                                  'aparece como api-citas.',
                                  'El ci.yml tiene un unico paso que imprime build ok y ninguna '
                                  'prueba.',
                                  'El Dockerfile fija la imagen base con un tag de version en '
                                  'lugar de usar latest.',
                                  'La seccion de seguridad tiene 5 amenazas pero ninguna se puede '
                                  'senalar en un diagrama.',
                                  'El informe enlaza cada evidencia con su ruta dentro del '
                                  'paquete.',
                                  'El diagrama de despliegue ubica la base de datos en la zona de '
                                  'datos sin IP publica.'],
                     'puntos': 10,
                     'rubrica': '4 pts por cada hueco correctamente identificado hasta un maximo '
                                'de 10; se descuentan 4 pts por cada practica correcta marcada '
                                'como hueco, sin bajar de cero.',
                     'tipo': 'cerrada_multi'}],
      'resumen': 'El estudiante consolida el paquete v1 de CloudLite con checklist enlazado, '
                 'nombres reconciliados entre todos los artefactos, el interior de la API en un '
                 'C4Component y un backlog de 5 items hacia la Clase 12.',
      'titulo': 'Taller Clase 11 en ExamLab - Checkpoint del paquete v1 de CloudLite'},
 12: {'pasos': ['Paso 1: describan el escenario de carga del pico real de su dominio con los 6 '
                'datos obligatorios (evento del pico, usuarios concurrentes, peticiones por '
                'segundo, mezcla de operaciones en porcentajes que sumen 100, duracion de la '
                'ventana y volumen de datos de partida), verificando que la mezcla sume '
                'exactamente 100 por ciento y que el pico corresponda a una fecha real del '
                'calendario de su dominio.',
                'Paso 2: definan las 3 metricas objetivo en una tabla de 4 columnas con numero, '
                'ventana de medicion, forma de medirla y consecuencia de incumplirla, verificando '
                'que cada objetivo tenga un numero y una ventana (por ejemplo p95 por debajo de '
                '800 ms en 5 minutos) y que ninguna diga rapido o aceptable sin cifra.',
                'Paso 3: escriban en ExamLab el sequenceDiagram del camino critico con el '
                'presupuesto de latencia repartido por salto, verificando que la suma de los '
                'tramos sea menor o igual al objetivo de p95 y que la nota final muestre el margen '
                'restante en milisegundos.',
                'Paso 4: ensayen el pitch de 5 a 8 minutos con cronometro y llenen la tabla de '
                'guion de 6 filas con minuto, seccion, quien habla, mensaje clave y evidencia en '
                'pantalla, verificando que la suma de los minutos quede entre 5 y 8, que ninguna seccion pase de 2:00 '
                '(y, si el docente autorizo equipo, que todos los integrantes hablen) y que cada '
                'seccion tenga una evidencia concreta que se pueda '
                'mostrar.',
                'Paso 5: cierren los 5 items del backlog de la Clase 11 dejando registro de los '
                'residuales, dejen el paquete casi final ordenado en el repositorio o el Drive y '
                'suban las 6 preguntas a ExamLab (modulo Talleres) antes del domingo 23:59, '
                'verificando que el cuello de botella declarado en el analisis sea el mismo que '
                'muestra el diagrama de secuencia.'],
      'preguntas': [{'enunciado': '## Escenario de carga del pico de su dominio\n'
                                  '\n'
                                  'Escriba el escenario con **estos 6 datos rotulados**, en este '
                                  'orden:\n'
                                  '\n'
                                  '1. **Evento del pico**: cual dia y por que se concentra la '
                                  'demanda (`primera semana de matricula`, `dia de entrega de '
                                  'notas`, `jornada de vacunacion`). Incluya una fecha real del '
                                  'calendario de su dominio.\n'
                                  '2. **Usuarios concurrentes**: un numero y como lo estimo (`320 '
                                  'estudiantes del programa por 15 por ciento simultaneos`).\n'
                                  '3. **Peticiones por segundo**: un numero y el calculo que lo '
                                  'sustenta.\n'
                                  '4. **Mezcla de operaciones**: porcentajes por operacion (`GET '
                                  '/cupos 70 por ciento`, `POST /citas 25 por ciento`, `DELETE '
                                  '/citas 5 por ciento`). **Deben sumar exactamente 100.**\n'
                                  '5. **Duracion de la ventana**: cuanto dura el pico (`45 '
                                  'minutos`).\n'
                                  '6. **Volumen de datos de partida**: cuantos registros ya '
                                  'existen (`8000 citas historicas y 1200 cupos publicados`).\n'
                                  '\n'
                                  'Cierre con **una frase de honestidad tecnica**: como piensa '
                                  'aproximar este escenario **sin cloud de pago** (medicion en el '
                                  'lab con pocas peticiones, calculo analitico, prueba '
                                  'cualitativa) y cual es el limite de esa aproximacion.',
                     'puntos': 22,
                     'rubrica': '10 pts los 6 datos rotulados y presentes. 5 pts que los usuarios '
                                'concurrentes y las peticiones por segundo tengan el calculo que '
                                'los sustenta. 4 pts que la mezcla de operaciones sume exactamente '
                                '100 por ciento. 3 pts la frase de honestidad tecnica con el '
                                'limite de la aproximacion.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Presupuesto de latencia del camino critico\n'
                                  '\n'
                                  'Escriba un `sequenceDiagram` de la **operacion de escritura '
                                  'principal** de su dominio, con **exactamente 5 participantes** '
                                  '(navegador, edge, API, base de datos y cola), usando los '
                                  'nombres canonicos de su paquete.\n'
                                  '\n'
                                  'Requisitos:\n'
                                  '1. `autonumber`.\n'
                                  '2. Una `Note over` inicial que declare el **objetivo de p95** '
                                  'de la operacion (`p95 de POST /citas igual a 800 ms en el '
                                  'pico`).\n'
                                  '3. Una `Note right of` **por cada salto** con los '
                                  '**milisegundos asignados** a ese salto.\n'
                                  '4. El salto que consume mas tiempo debe estar rotulado como '
                                  '**cuello de botella**.\n'
                                  '5. Una `Note over` final con la **suma de los tramos** y el '
                                  '**margen restante** frente al objetivo.\n'
                                  '\n'
                                  '**Verificacion:** sume a mano los milisegundos de las notas; la '
                                  'suma debe ser **menor o igual** al objetivo declarado y el '
                                  'margen de la nota final debe ser exactamente la diferencia.',
                     'mermaid_esperado': 'sequenceDiagram\n'
                                         '    autonumber\n'
                                         '    participant N as Navegador\n'
                                         '    participant E as Edge TLS\n'
                                         '    participant A as API CloudLite\n'
                                         '    participant D as Base de datos Citas\n'
                                         '    participant Q as Cola Notificaciones\n'
                                         '    Note over N,Q: Objetivo p95 de POST /citas igual a '
                                         '800 ms en el pico de matricula\n'
                                         '    N->>E: POST /citas\n'
                                         '    Note right of E: Terminacion TLS y proxy - 40 ms\n'
                                         '    E->>A: POST /citas interno en 8080\n'
                                         '    Note right of A: Validacion del token con cache - 60 '
                                         'ms\n'
                                         '    A->>D: SELECT del cupo con bloqueo FOR UPDATE\n'
                                         '    D-->>A: Fila bloqueada\n'
                                         '    Note right of D: Lectura con indice por id_cupo - '
                                         '120 ms\n'
                                         '    A->>D: INSERT de la cita y commit\n'
                                         '    D-->>A: Commit confirmado\n'
                                         '    Note right of D: Escritura y commit - 380 ms cuello '
                                         'de botella\n'
                                         '    A->>Q: XADD del evento cita_confirmada\n'
                                         '    Note right of Q: Publicacion asincrona - 20 ms\n'
                                         '    A-->>E: 201 Created\n'
                                         '    E-->>N: 201 Created\n'
                                         '    Note over N,Q: Suma de tramos 620 ms sobre 800 ms - '
                                         'margen de 180 ms',
                     'puntos': 18,
                     'rubrica': '6 pts los 5 participantes con nombres canonicos y el flujo '
                                'completo de la operacion. 6 pts una nota de milisegundos por '
                                'salto. 4 pts que la suma sea menor o igual al objetivo y que el '
                                'margen final sea correcto. 2 pts el cuello de botella rotulado.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## Tres metricas objetivo verificables\n'
                                  '\n'
                                  'Construya una tabla de **4 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Metrica | Objetivo con numero y ventana | Como se mide | Que '
                                  'pasa si no se cumple`\n'
                                  '\n'
                                  'con **exactamente 3 filas**, una por cada tipo: **latencia**, '
                                  '**tasa de error** y **capacidad** (peticiones por segundo '
                                  'sostenidas).\n'
                                  '\n'
                                  'Reglas:\n'
                                  '- El objetivo debe llevar **numero y ventana de medicion**: '
                                  '`p95 por debajo de 800 ms medido en ventanas de 5 minutos`. '
                                  'Palabras como `rapido`, `bueno` o `aceptable` sin cifra '
                                  'invalidan la fila.\n'
                                  '- `Como se mide` nombra la **fuente real** disponible en su '
                                  'proyecto (log del edge, salida de una prueba en el lab, '
                                  'cronometro con 20 peticiones manuales, tiempos del `curl -w`).\n'
                                  '- `Que pasa si no se cumple` es una **decision de '
                                  'arquitectura**, no una queja (`se agrega indice por id_cupo`, '
                                  '`se mueve el envio de correo a la cola`).\n'
                                  '\n'
                                  'Cierre con **una linea**: por que el promedio no sirve como '
                                  'objetivo y el p95 si.',
                     'puntos': 18,
                     'rubrica': '7 pts las 3 filas con los 3 tipos de metrica y las 4 columnas. 5 '
                                'pts que los 3 objetivos tengan numero y ventana de medicion. 4 '
                                'pts que la fuente de medicion exista realmente en el proyecto. 2 '
                                'pts la decision de arquitectura en las 3 filas.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Cuello de botella y mitigaciones\n'
                                  '\n'
                                  '**Parte A.** Nombre **el cuello de botella** de su arquitectura '
                                  'en **una frase** e indique **como lo sabe**: cite el salto '
                                  'exacto del diagrama de la pregunta 2 y su cantidad de '
                                  'milisegundos.\n'
                                  '\n'
                                  '**Parte B.** Proponga **exactamente 2 mitigaciones**, cada una '
                                  'con **4 lineas rotuladas**:\n'
                                  '\n'
                                  '1. **Mitigacion**: que cambia en el diseno.\n'
                                  '2. **Efecto esperado**: cuantos milisegundos o cuanto '
                                  'porcentaje espera recuperar.\n'
                                  '3. **Costo o riesgo**: que empeora (complejidad, consistencia '
                                  'eventual, mas dinero, mas piezas que fallan).\n'
                                  '4. **Trade-off en una frase**: `acepto X para conseguir Y`.\n'
                                  '\n'
                                  'Una de las 2 mitigaciones debe ser **estructural** (indice, '
                                  'cache, mover trabajo a la cola, separar lectura de escritura) y '
                                  'la otra **de capacidad** (mas replicas, nodo mas grande, ajuste '
                                  'del pool de conexiones).\n'
                                  '\n'
                                  '**Parte C.** Una linea: que mitigacion **no** aplicaria y por '
                                  'que romperia el PI.',
                     'puntos': 15,
                     'rubrica': '5 pts el cuello de botella nombrado y respaldado con el salto y '
                                'los milisegundos del diagrama. 6 pts las 2 mitigaciones con sus 4 '
                                'lineas rotuladas. 3 pts que una sea estructural y otra de '
                                'capacidad. 1 pt la parte C.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Guion cronometrado del pitch\n'
                                  '\n'
                                  'Construya una tabla de **5 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Minuto | Seccion | Quien habla | Mensaje clave en una frase | '
                                  'Evidencia en pantalla`\n'
                                  '\n'
                                  'con **exactamente 6 filas**, en este orden de secciones: '
                                  '**problema y dominio**, **arquitectura logica**, **contenedor y '
                                  'pipeline**, **seguridad**, **costos y escalabilidad**, **cierre '
                                  'y preguntas**.\n'
                                  '\n'
                                  'Reglas:\n'
                                  '- La columna `Minuto` usa rangos (`0:00 a 1:00`) y la **suma '
                                  'total debe quedar entre 5 y 8 minutos**.\n'
                                  '- La columna `Quien habla` lleva **su nombre** en modo individual; si el docente '
                                  'autorizo equipo, **deben aparecer todos los integrantes** en la '
                                  'columna y ninguno puede llevar mas de 3 filas. En los dos casos **ninguna seccion '
                                  'puede pasar de 2:00**: el guion se reparte por bloques '
                                  'tematicos, no en un solo tramo largo.\n'
                                  '- `Evidencia en pantalla` cita el **artefacto concreto** que se '
                                  'muestra (`diagrama C4 Container renderizado`, `captura del run '
                                  'verde de Actions`, `tabla STRIDE`).\n'
                                  '\n'
                                  'Debajo de la tabla escriba el **tiempo real cronometrado del '
                                  'ensayo** (`ensayo 1: 9:12`, `ensayo 2: 7:35`) con al menos **2 '
                                  'ensayos**, y **una linea** con lo que recortaron para entrar en '
                                  'el tiempo.',
                     'puntos': 17,
                     'rubrica': '7 pts las 6 filas con las 6 secciones en orden y las 5 columnas. '
                                '4 pts que los minutos sumen entre 5 y 8 y que el guion quede repartido por '
                                'bloques tematicos sin ninguna seccion de mas de 2:00 (en equipo '
                                'autorizado, que ademas hablen todos los '
                                'integrantes). 4 pts que cada fila cite un artefacto '
                                'concreto como evidencia. 2 pts los 2 tiempos de ensayo '
                                'cronometrados y el recorte declarado.',
                     'tipo': 'abierta'},
                    {'correctas': [0, 1, 3],
                     'enunciado': '## Rendimiento: que es cierto\n'
                                  '\n'
                                  'Seleccione las **3 afirmaciones correctas**.',
                     'opciones': ['El promedio puede verse bien mientras el p95 esta muy por '
                                  'encima del objetivo.',
                                  'Un objetivo de rendimiento sin numero ni ventana de medicion no '
                                  'es verificable.',
                                  'Si la API escala a mas replicas, la base de datos primaria '
                                  'escala sola en la misma proporcion.',
                                  'Conviene medir tambien la tasa de error, porque un sistema que '
                                  'devuelve 500 rapido parece rapido.',
                                  'Probar con 3 usuarios en el portatil del equipo demuestra el '
                                  'comportamiento en el pico de matricula.',
                                  'El cuello de botella de una aplicacion web siempre esta en el '
                                  'frontend.'],
                     'puntos': 10,
                     'rubrica': '4 pts por cada correcta marcada hasta un maximo de 10; se '
                                'descuentan 4 pts por cada incorrecta marcada, sin bajar de cero.',
                     'tipo': 'cerrada_multi'}],
      'resumen': 'El estudiante entrega el escenario de carga del pico de su dominio con 3 '
                 'metricas objetivo numericas, el presupuesto de latencia repartido por salto en '
                 'un diagrama de secuencia y el guion cronometrado del pitch de sustentacion.',
      'titulo': 'Taller Clase 12 en ExamLab - Rendimiento y ensayo de sustentacion de CloudLite'},
 13: {'pasos': ['Paso 1: tome los 5 componentes de su C4Deployment de la Clase 7 y clasifique cada '
                'uno como escala horizontal, escala vertical o no escala, verificando que al menos '
                'uno quede en no escala con justificacion tecnica, porque una politica donde todo '
                'escala no es una politica; el resultado abre la seccion Escalabilidad del '
                'informe.',
                'Paso 2: complete la tabla de politica de escalado con 6 columnas y 5 filas '
                '(componente, tipo de escala, disparador de subida, disparador de bajada, minimo y '
                'maximo, tiempo de enfriamiento), verificando que cada disparador tenga metrica, '
                'umbral numerico y ventana de tiempo, y que ningun maximo quede en infinito o sin '
                'definir.',
                'Paso 3: escriba en ExamLab el diagrama Mermaid de la maquina de decision del '
                'autoescalado con el nodo de observacion, los dos rombos de decision, las acciones '
                'de subida y bajada, el enfriamiento y el nodo de lo que no escala, verificando al '
                'renderizar que el ciclo se cierre sobre el nodo de observacion y que los umbrales '
                'del diagrama sean los mismos numeros de la tabla.',
                'Paso 4: escriba los 3 componentes que NO escalan con su justificacion tecnica y '
                'su plan alterno, y la tabla de impacto en costos que enlaza con la Clase 10, '
                'verificando que cada plan alterno sea ejecutable sin cloud de pago y que el '
                'impacto de costo use los mismos niveles bajo, medio o alto de la seccion de '
                'costos.',
                'Paso 5: integre la politica en la seccion Escalabilidad del informe, anote la '
                'marca de replicas en el diagrama de despliegue si aplica y suba las 5 preguntas a '
                'ExamLab (modulo Talleres) antes del domingo 23:59, verificando que la politica no '
                'prometa nada que la arquitectura dibujada no pueda cumplir.'],
      'preguntas': [{'enunciado': '## Politica de autoescalado de CloudLite\n'
                                  '\n'
                                  'Construya una tabla de **6 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Componente | Tipo de escala | Disparador de subida | '
                                  'Disparador de bajada | Minimo y maximo | Enfriamiento`\n'
                                  '\n'
                                  'con **exactamente 5 filas**, una por componente de su '
                                  'C4Deployment: **Edge TLS**, **API CloudLite**, **Worker '
                                  'Notificaciones**, **Base de datos Citas**, **Cola '
                                  'Notificaciones**.\n'
                                  '\n'
                                  'Reglas de verificacion:\n'
                                  '- `Tipo de escala` usa **solo** estos rotulos: `horizontal`, '
                                  '`vertical`, `no escala`. **Al menos una fila debe ser `no '
                                  'escala`.**\n'
                                  '- Cada disparador lleva **metrica + umbral numerico + ventana '
                                  'de tiempo**: `p95 de POST /citas por encima de 800 ms durante 3 '
                                  'minutos`, `longitud de la cola por encima de 500 mensajes '
                                  'durante 2 minutos`. Un disparador sin numero o sin ventana '
                                  'invalida la celda.\n'
                                  '- `Minimo y maximo` con dos numeros concretos (`min 2 y max '
                                  '6`). **Nada de sin limite.**\n'
                                  '- `Enfriamiento` con minutos concretos y **coherente** con el '
                                  'disparador (no puede ser mas corto que la ventana de '
                                  'medicion).\n'
                                  '- Las filas `no escala` llevan en los disparadores la frase `no '
                                  'aplica` y en `Minimo y maximo` la capacidad fija.\n'
                                  '\n'
                                  'Cierre con **una linea**: cual componente escala primero cuando '
                                  'llega el pico y cual es el ultimo.',
                     'puntos': 30,
                     'rubrica': '10 pts las 5 filas con los 5 componentes y los 6 campos. 8 pts '
                                'que los disparadores tengan metrica umbral numerico y ventana en '
                                'todas las filas que escalan. 6 pts los minimos y maximos con '
                                'numeros concretos y sin infinitos. 4 pts el enfriamiento '
                                'coherente con la ventana de medicion. 2 pts la linea de cierre. '
                                'Cero en la fila cuyo disparador no tenga numero.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Maquina de decision del autoescalado\n'
                                  '\n'
                                  'Escriba un `flowchart TD` que represente el ciclo de decision '
                                  'de su politica. Debe contener:\n'
                                  '\n'
                                  '1. Un nodo de **observacion** con el **periodo de evaluacion** '
                                  'y las metricas observadas (`evaluar cada 60 segundos el p95 y '
                                  'la CPU de la API`).\n'
                                  '2. Un **rombo de decision de subida** con **los umbrales '
                                  'exactos de su tabla**.\n'
                                  '3. Un **rombo de decision de bajada** con sus umbrales.\n'
                                  '4. Un nodo de **scale out** y un nodo de **scale in**, ambos '
                                  'con el **limite** correspondiente (`hasta el maximo de 6`, '
                                  '`hasta el minimo de 2`).\n'
                                  '5. Un nodo de **enfriamiento** con los minutos, por el que '
                                  'pasan las dos acciones antes de volver a observar.\n'
                                  '6. Un nodo aparte para **lo que no escala**, unido con **arista '
                                  'punteada** rotulada `limite del diseno`.\n'
                                  '\n'
                                  '**Verificacion:** el ciclo debe cerrarse sobre el nodo de '
                                  'observacion (debe poder recorrerlo con el dedo y volver al '
                                  'inicio), y los numeros del diagrama deben ser identicos a los '
                                  'de la tabla de la pregunta 1.\n'
                                  '\n'
                                  '**Consejo de sintaxis:** escriba los umbrales con palabras '
                                  '(`por encima de`, `por debajo de`) en lugar de los simbolos de '
                                  'mayor y menor.',
                     'mermaid_esperado': 'flowchart TD\n'
                                         '    obs["Observar cada 60 segundos el p95 de POST /citas '
                                         'y la CPU de la API CloudLite"]\n'
                                         '    obs --> up{"p95 por encima de 800 ms o CPU por '
                                         'encima de 70 por ciento durante 3 minutos"}\n'
                                         '    up -->|"Si"| out["Scale out - sumar 1 replica de la '
                                         'API hasta el maximo de 6"]\n'
                                         '    up -->|"No"| down{"p95 por debajo de 300 ms y CPU '
                                         'por debajo de 30 por ciento durante 10 minutos"}\n'
                                         '    down -->|"Si"| inn["Scale in - retirar 1 replica de '
                                         'la API hasta el minimo de 2"]\n'
                                         '    down -->|"No"| obs\n'
                                         '    out --> cool["Enfriamiento de 5 minutos sin nuevas '
                                         'acciones de escalado"]\n'
                                         '    inn --> cool\n'
                                         '    cool --> obs\n'
                                         '    noesc["No escala - Base de datos Citas primaria - '
                                         'solo escala vertical en ventana de mantenimiento"]\n'
                                         '    noesc -.->|"limite del diseno"| obs',
                     'puntos': 25,
                     'rubrica': '8 pts el nodo de observacion con periodo y metricas y los 2 '
                                'rombos con umbrales numericos. 6 pts los nodos de scale out y '
                                'scale in con su limite maximo y minimo. 5 pts el nodo de '
                                'enfriamiento por el que pasan ambas acciones y el cierre del '
                                'ciclo. 4 pts el nodo de lo que no escala con arista punteada. 2 '
                                'pts que renderice sin error.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## Lo que NO escala y por que\n'
                                  '\n'
                                  'Una politica honesta dice que **no** puede escalar. Escriba '
                                  '**exactamente 3 componentes o aspectos** de CloudLite que no '
                                  'escalan horizontalmente, cada uno con **4 lineas rotuladas**:\n'
                                  '\n'
                                  '1. **Componente o aspecto**: nombre canonico de su paquete.\n'
                                  '2. **Por que no escala horizontalmente**: razon **tecnica**, no '
                                  'falta de tiempo (`es la unica instancia que acepta escrituras y '
                                  'dos primarias generarian conflicto de version del cupo`).\n'
                                  '3. **Que pasa si el pico lo desborda**: el sintoma que veria el '
                                  'usuario y en cual metrica de la Clase 8 aparece.\n'
                                  '4. **Plan alterno**: que haria en su lugar (escala vertical en '
                                  'ventana de mantenimiento, replica de solo lectura, cola de '
                                  'amortiguacion, limite de peticiones por usuario), **ejecutable '
                                  'sin cloud de pago**.\n'
                                  '\n'
                                  'Al menos uno de los 3 debe ser la **base de datos primaria de '
                                  'escrituras**, y al menos uno debe ser un aspecto **no de '
                                  'infraestructura** (por ejemplo el estado de sesion, un contador '
                                  'global, un limite de la API de correo externa).',
                     'puntos': 20,
                     'rubrica': '9 pts los 3 componentes con las 4 lineas rotuladas. 5 pts que las '
                                'razones sean tecnicas y no de falta de tiempo. 4 pts que uno sea '
                                'la base de datos primaria y uno un aspecto no de infraestructura. '
                                '2 pts que los planes alternos sean ejecutables sin cloud de pago.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Impacto del autoescalado en costos y sostenibilidad\n'
                                  '\n'
                                  'Enlace esta politica con su seccion de costos de la Clase 10. '
                                  'Construya una tabla de **4 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Escenario | Replicas activas | Costo cualitativo B/M/A | '
                                  'Accion de sostenibilidad`\n'
                                  '\n'
                                  'con **exactamente 3 filas**:\n'
                                  '\n'
                                  '1. **Valle** (madrugada o fin de semana sin trafico).\n'
                                  '2. **Dia normal**.\n'
                                  '3. **Pico** del evento que definio en la Clase 12.\n'
                                  '\n'
                                  'Reglas:\n'
                                  '- `Replicas activas` debe respetar el minimo y el maximo de su '
                                  'tabla de la pregunta 1.\n'
                                  '- `Costo cualitativo B/M/A` debe usar **los mismos niveles** '
                                  'que escribio en la seccion de costos de la Clase 10; si aqui '
                                  'cambia el nivel, explique en media linea por que.\n'
                                  '- `Accion de sostenibilidad` es concreta y verificable (`bajar '
                                  'a 1 replica entre las 22:00 y las 06:00 y dejar registro en la '
                                  'bitacora`).\n'
                                  '\n'
                                  'Cierre con **una frase**: cuanto del costo total del PI viene '
                                  'de capacidad que solo se usa en el pico.',
                     'puntos': 15,
                     'rubrica': '6 pts las 3 filas con las 4 columnas y replicas dentro del rango '
                                'declarado. 5 pts la coherencia de los niveles B/M/A con la '
                                'seccion de costos de la Clase 10. 3 pts las acciones de '
                                'sostenibilidad verificables. 1 pt la frase de cierre.',
                     'tipo': 'abierta'},
                    {'correctas': [0, 1, 3],
                     'enunciado': '## Disparadores de autoescalado\n'
                                  '\n'
                                  'Seleccione las **3 afirmaciones correctas**.',
                     'opciones': ['El p95 de POST /citas por encima de 800 ms sostenido 3 minutos '
                                  'es un disparador valido porque es medible y tiene ventana.',
                                  'La longitud de la cola de notificaciones por encima de 500 '
                                  'mensajes es un disparador valido para el worker.',
                                  'Cuando el sistema se sienta lento es un disparador valido si el '
                                  'equipo lo revisa a diario.',
                                  'Toda politica de autoescalado necesita un maximo de replicas '
                                  'para no escalar sin techo.',
                                  'Un enfriamiento de 10 segundos evita que el sistema suba y baje '
                                  'replicas continuamente.',
                                  'Escalar horizontalmente la base de datos primaria de escrituras '
                                  'es tan simple como sumar replicas.'],
                     'puntos': 10,
                     'rubrica': '4 pts por cada correcta marcada hasta un maximo de 10; se '
                                'descuentan 4 pts por cada incorrecta marcada, sin bajar de cero.',
                     'tipo': 'cerrada_multi'}],
      'resumen': 'El estudiante entrega la politica de autoescalado conceptual de CloudLite con '
                 'disparadores numericos, minimos y maximos, tiempo de enfriamiento, los '
                 'componentes que deliberadamente no escalan y el impacto en costos.',
      'titulo': 'Taller Clase 13 en ExamLab - Politica de autoescalado de CloudLite'},
 15: {'pasos': ['Paso 1: armen el paquete final y llenen el indice de 8 filas con entregable, '
                'nombre de archivo, ruta dentro del paquete y estado, verificando que los 8 '
                'archivos abran desde una maquina distinta a la del autor y que ningun nombre de '
                'archivo tenga espacios ni tildes que rompan la descarga.',
                'Paso 2: escriban en ExamLab la lamina unica de arquitectura en Mermaid con las 3 '
                'zonas, los 5 contenedores, el edge, la cadena de entrega y los sistemas externos, '
                'verificando al renderizar que sea legible en una sola pantalla sin desplazamiento '
                'y que use los mismos nombres canonicos del paquete, porque esta es la lamina que '
                'van a proyectar en la sustentacion.',
                'Paso 3: redacten el Q and A escrito con 3 preguntas duras que el jurado podria '
                'hacer, una de decision de arquitectura, una de seguridad y una de escala o '
                'rendimiento, cada una con respuesta de maximo 4 lineas que cite la evidencia del '
                'paquete, verificando que ninguna respuesta sea no lo alcanzamos a hacer sin '
                'nombrar la decision consciente que tomaron.',
                'Paso 4: ensayen el pitch con cronometro ANTES de la sesion y registren la tabla de '
                'tiempos reales por seccion con quien hablo en cada una, verificando que el tiempo '
                'total quede entre 5 y 8 minutos; la sustentacion se hace EN VIVO en la sesion de '
                'clase, con preguntas del docente al cierre, no con un video grabado.',
                'Paso 5: escriban la reflexion de media pagina sobre el trade-off mas difícil y '
                'suban el paquete final completo mas las 5 preguntas a ExamLab (modulo Proyectos) '
                'ANTES de su turno de sustentacion, verificando que el informe, los diagramas, la evidencia del '
                'lab, el ci.yml y la presentacion esten los cinco dentro del mismo paquete.'],
      'preguntas': [{'enunciado': '## Indice del paquete final\n'
                                  '\n'
                                  'Construya una tabla de **4 columnas** con encabezados exactos:\n'
                                  '\n'
                                  '`Entregable | Nombre del archivo | Ruta dentro del paquete o '
                                  'enlace | Estado`\n'
                                  '\n'
                                  'con **exactamente 8 filas**, en este orden:\n'
                                  '\n'
                                  '1. Informe de arquitectura completo (PDF o DOCX).\n'
                                  '2. Diagrama C4 Context y C4 Container.\n'
                                  '3. Diagrama C4 Deployment.\n'
                                  '4. Dockerfile y evidencia del lab de contenedores.\n'
                                  '5. Workflow `ci.yml` y enlace al run verde.\n'
                                  '6. Seccion de seguridad con tabla STRIDE y politica de '
                                  'secretos.\n'
                                  '7. Secciones de costos, sostenibilidad y escalabilidad.\n'
                                  '8. Presentacion de sustentacion (diapositivas o guion del pitch '
                                  'que va a defender en vivo).\n'
                                  '\n'
                                  'Reglas de verificacion:\n'
                                  '- `Estado` usa **solo** `completo` o `parcial`; si es '
                                  '`parcial`, agregue entre parentesis **que falta**.\n'
                                  '- Los nombres de archivo **no llevan espacios ni tildes** (use '
                                  'guiones).\n'
                                  '- **Verificacion obligatoria antes de enviar:** abra los 8 '
                                  'archivos **desde otra maquina o desde una ventana privada del '
                                  'navegador** y confirme que ninguno pide permisos; escriba '
                                  'debajo de la tabla la linea `verificado desde otra maquina el '
                                  '<fecha>`.\n'
                                  '\n'
                                  'Cierre con **una linea**: cuantas filas quedaron en `completo` '
                                  'sobre 8.',
                     'puntos': 25,
                     'rubrica': '10 pts las 8 filas en el orden pedido con las 4 columnas. 6 pts '
                                'las rutas o enlaces reales y nombres de archivo sin espacios ni '
                                'tildes. 6 pts la linea de verificacion desde otra maquina. 3 pts '
                                'el estado de cada fila con el faltante entre parentesis en las '
                                'parciales. Cada archivo que no abra descuenta 3 pts.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Lamina unica de arquitectura para la sustentacion\n'
                                  '\n'
                                  'Esta es **la lamina que va a proyectar** cuando le pidan '
                                  'explicar CloudLite en 60 segundos. Escriba un `flowchart LR` '
                                  'que consolide todo el semestre en un solo diagrama legible:\n'
                                  '\n'
                                  '1. **3 subgrafos de zona** con su subred: `Zona publica`, `Zona '
                                  'privada`, `Zona de datos`.\n'
                                  '2. Los **5 contenedores canonicos** mas el **edge**, cada uno '
                                  'en su zona, con **el puerto** en la etiqueta.\n'
                                  '3. La **API con su rango de replicas** de la Clase 13 (`2 a 6 '
                                  'replicas`).\n'
                                  '4. Un **subgrafo de cadena de entrega** con el workflow y la '
                                  'imagen etiquetada, unido a la API por una **arista punteada** '
                                  'rotulada `despliegue simulado`.\n'
                                  '5. Los **2 sistemas externos** (identidad y correo) fuera de '
                                  'las zonas.\n'
                                  '6. El **actor principal** entrando por HTTPS 443 al edge.\n'
                                  '\n'
                                  'Reglas de verificacion:\n'
                                  '- Todos los nombres deben ser **los canonicos** de su tabla de '
                                  'reconciliacion de la Clase 11.\n'
                                  '- Debe entenderse **sin leer el informe**: si un jurado no '
                                  'puede seguir el camino del usuario hasta la base de datos, '
                                  'simplifique.\n'
                                  '- Debe caber en una pantalla: **maximo 14 nodos** contando los '
                                  'de los subgrafos.',
                     'mermaid_esperado': 'flowchart LR\n'
                                         '    est["Estudiante"]\n'
                                         '    subgraph zpub["Zona publica 10.10.1.0/24"]\n'
                                         '        edge["Edge TLS y proxy reverso - 443"]\n'
                                         '        spa["SPA Web - contenido estatico"]\n'
                                         '    end\n'
                                         '    subgraph zpriv["Zona privada 10.10.2.0/24"]\n'
                                         '        api["API CloudLite - 8080 - de 2 a 6 replicas"]\n'
                                         '        worker["Worker Notificaciones"]\n'
                                         '    end\n'
                                         '    subgraph zdat["Zona de datos 10.10.3.0/24"]\n'
                                         '        db[("Base de datos Citas - 5432")]\n'
                                         '        cola[("Cola Notificaciones - 6379")]\n'
                                         '        obj[("Almacen Adjuntos - objetos")]\n'
                                         '    end\n'
                                         '    subgraph entrega["Cadena de entrega"]\n'
                                         '        gh["GitHub Actions ci.yml - build test y '
                                         'artefacto"]\n'
                                         '        img["Imagen cloudlite-api:v1"]\n'
                                         '    end\n'
                                         '    idp["Proveedor de identidad institucional"]\n'
                                         '    correo["Correo transaccional SaaS"]\n'
                                         '    est -->|"HTTPS 443"| edge\n'
                                         '    edge --> spa\n'
                                         '    edge -->|"8080 interno"| api\n'
                                         '    api -->|"SQL 5432"| db\n'
                                         '    api -->|"XADD 6379"| cola\n'
                                         '    worker -->|"XREAD 6379"| cola\n'
                                         '    api -->|"HTTPS objetos"| obj\n'
                                         '    api -->|"OIDC"| idp\n'
                                         '    worker -->|"API REST"| correo\n'
                                         '    gh --> img\n'
                                         '    img -.->|"despliegue simulado"| api',
                     'puntos': 25,
                     'rubrica': '10 pts las 3 zonas con sus subredes y los 6 elementos ubicados '
                                'correctamente con puerto. 6 pts el rango de replicas de la API y '
                                'la cadena de entrega con arista punteada de despliegue simulado. '
                                '5 pts los 2 sistemas externos y el actor entrando por 443. 4 pts '
                                'legibilidad: maximo 14 nodos y nombres canonicos coherentes con '
                                'el resto del paquete.',
                     'tipo': 'diagrama'},
                    {'enunciado': '## Q and A escrito: las 3 preguntas que teme\n'
                                  '\n'
                                  'Escriba **exactamente 3 preguntas** que un jurado podria '
                                  'hacerle y respondalas usted mismo. Una de cada tipo, en este '
                                  'orden:\n'
                                  '\n'
                                  '1. **Decision de arquitectura**: por que eligio el modelo de '
                                  'servicio o por que 5 contenedores y no otro numero.\n'
                                  '2. **Seguridad**: como protege el activo mas sensible de su '
                                  'dominio.\n'
                                  '3. **Escala o rendimiento**: que pasa el dia del pico y que no '
                                  'escala.\n'
                                  '\n'
                                  'Cada respuesta:\n'
                                  '- **Maximo 4 lineas.**\n'
                                  '- Debe **citar la evidencia** del paquete que la respalda '
                                  '(`ADR-001`, `tabla STRIDE fila 3`, `politica de escalado fila '
                                  'API`, `diagrama de secuencia con el presupuesto de 800 ms`).\n'
                                  '- Debe nombrar **el trade-off aceptado**, no solo la virtud.\n'
                                  '\n'
                                  '**Prohibido** responder `no lo alcanzamos a hacer` sin '
                                  'convertirlo en una decision: si algo quedo fuera, escriba `lo '
                                  'dejamos fuera a proposito porque ...` y diga que gano el '
                                  'proyecto con eso.',
                     'puntos': 20,
                     'rubrica': '9 pts las 3 preguntas de los 3 tipos exigidos con respuesta de '
                                'maximo 4 lineas. 6 pts que cada respuesta cite una evidencia '
                                'concreta del paquete. 5 pts que cada una nombre el trade-off '
                                'aceptado. Cero en la respuesta que se limite a decir que no '
                                'alcanzo el tiempo.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Reflexion: el trade-off mas dificil\n'
                                  '\n'
                                  'Escriba media pagina (entre 200 y 300 palabras) con **estos 5 '
                                  'bloques rotulados**:\n'
                                  '\n'
                                  '1. **La decision**: cual fue el trade-off mas dificil del '
                                  'semestre, en una frase.\n'
                                  '2. **La alternativa que descarto**: que era y quien la defendia (usted mismo al principio, '
                                  'o un companero si trabajo en equipo).\n'
                                  '3. **Que sacrifico**: lo concreto que se perdio al decidir asi '
                                  '(velocidad, simplicidad, seguridad, costo, aprendizaje).\n'
                                  '4. **Como se ve hoy en el paquete**: en cual artefacto quedo '
                                  'escrita esa decision (ADR, diagrama, seccion del informe).\n'
                                  '5. **Que haria distinto**: una accion concreta si volviera a '
                                  'empezar CloudLite manana.\n'
                                  '\n'
                                  'Es una reflexion tecnica, no una carta de agradecimiento: cada '
                                  'bloque debe poder discutirse con argumentos.',
                     'puntos': 15,
                     'rubrica': '8 pts los 5 bloques rotulados y desarrollados dentro de las 200 a '
                                '300 palabras. 4 pts que el sacrificio y la alternativa descartada '
                                'sean concretos y no genericos. 3 pts que el bloque 4 cite el '
                                'artefacto real donde quedo la decision.',
                     'tipo': 'abierta'},
                    {'enunciado': '## Evidencia del pitch y tiempos reales\n'
                                  '\n'
                                  '**Parte A.** Escriba la **fecha y hora de su turno de '
                                  'sustentacion en vivo** (la sesion de cierre del curso) y '
                                  'confirme en una linea que el paquete final ya quedo subido '
                                  '**antes** de ese turno: `paquete subido el <fecha>, verificado '
                                  'en ventana privada`.\n'
                                  '\n'
                                  '**Parte B.** Construya una tabla de **4 columnas** con '
                                  'encabezados exactos:\n'
                                  '\n'
                                  '`Seccion | Tiempo real | Quien hablo | Evidencia '
                                  'mostrada`\n'
                                  '\n'
                                  'con **exactamente 6 filas**, las mismas 6 secciones del guion '
                                  'de la Clase 12 (problema y dominio, arquitectura logica, '
                                  'contenedor y pipeline, seguridad, costos y escalabilidad, '
                                  'cierre y preguntas).\n'
                                  '\n'
                                  'Escriba debajo el **total real en minutos y segundos** y '
                                  'verifique que quede **entre 5:00 y 8:00**; si se paso, agregue '
                                  'una linea de que recortaria.\n'
                                  '\n'
                                  '**Parte C.** Una linea de autoevaluacion de **su propio trabajo** en CloudLite: '
                                  'nota de 1 '
                                  'a 5 y **el hecho concreto** que la '
                                  'sustenta (no una intencion). Si el docente autorizo equipo, agregue una '
                                  'segunda linea con la nota al trabajo del equipo y su hecho '
                                  'concreto.',
                     'puntos': 15,
                     'rubrica': '5 pts la fecha y hora del turno de sustentacion con la '
                                'confirmacion de paquete subido antes. 6 pts la tabla de 6 '
                                'secciones con tiempo real, quien hablo '
                                'y evidencia. 3 pts el total entre 5:00 y 8:00 o el recorte '
                                'propuesto si se paso. 1 pt la autoevaluacion con hecho concreto.',
                     'tipo': 'abierta'}],
      'resumen': 'El estudiante entrega el paquete final de CloudLite indexado y verificado, la '
                 'lamina unica de arquitectura que proyecta en la sustentacion, el Q and A '
                 'escrito, los tiempos reales del pitch y la reflexion del trade-off mas difícil.',
      'titulo': 'Taller Clase 15 en ExamLab - Entrega final y sustentacion de CloudLite'}}
