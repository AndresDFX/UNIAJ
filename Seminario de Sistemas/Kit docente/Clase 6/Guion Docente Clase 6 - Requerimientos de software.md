# Guion docente · Clase 6 · Requerimientos de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Avance del PI (si se hace la practica):** Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.
- **Practica (opcional):** `Clases/Clase 6 - Requerimientos de software/Taller PI - Clase 6 - VetCare.docx` — no esta en el deck
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 6 - Requerimientos de software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

## Apoyo por diapositiva

Todo lo que hay que decir **esta proyectado**. Esta seccion dice que subrayar en cada lamina, no repite su contenido.

**[Slide 4] Elicitación: de lo que dijo a lo que necesita** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un requerimiento no es lo que el cliente dijo, es lo que el sistema debe hacer para que el problema del cliente desaparezca
  - Entre esas dos cosas hay un trabajo de traduccion que se llama elicitacion, palabra que viene de sacar a la luz algo que estaba implicito.
  - Las tres tecnicas que caben en este curso son baratas y no necesitan software especializado: la entrevista, donde se arranca con preguntas abiertas (cuenteme como es un dia normal en la clinica) y solo al final se cierran con preguntas de si o no
  - La observacion, donde uno se para media hora en la recepcion un sabado y cronometra cuanto tarda la auxiliar en encontrar una carpeta; y el prototipo desechable, donde uno dibuja una pantalla fea a mano o en draw.io y la pone frente al veterinario
  - Porque la gente no sabe decir lo que quiere pero sabe perfectamente decir lo que NO quiere cuando lo ve.
  - En la clinica la entrevista al Dr. Ramirez dejo cinco frases crudas: que las fichas no se pierdan, ver de una lo que le han hecho antes al paciente
  - Que la auxiliar agende sin llamarlo, que el sistema sea rapido, y saber cuantas consultas se hicieron en el mes.
  - Ninguna de esas cinco frases es todavia un requisito: son necesidades, y confundirlas es el primer error del analista novato.

**[Slide 5] Dos familias: RF y RNF** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Un requisito funcional (RF) describe una capacidad observable del sistema, algo que alguien puede hacer con el
  - Y se escribe con la plantilla el sistema debe permitir a <actor> <accion> <objeto> [bajo <condicion>]; el truco practico es que si al leerlo usted puede imaginar un boton, un formulario o una pantalla, es funcional.
  - Un requisito no funcional (RNF) no describe QUE hace el sistema sino QUE TAN BIEN lo hace, y se agrupa en categorias conocidas: desempeno, seguridad y control de acceso, usabilidad, disponibilidad, respaldo, mantenibilidad y portabilidad.
  - En la clinica, la frase que la auxiliar pueda agendar sin llamarme se convierte en dos cosas distintas al mismo tiempo: RF-05 el sistema debe permitir a la auxiliar registrar una cita seleccionando mascota, veterinario, fecha y hora
  - Y RNF-02 el sistema debe manejar dos perfiles de acceso, auxiliar y veterinario, donde la auxiliar puede crear citas pero no puede editar ni ver el diagnostico clinico.
  - NOTAS:
  - Con las necesidades en la mano se separan dos familias.
  - Esa separacion importa porque el RF se prueba haciendo clic y el RNF se prueba midiendo o intentando lo prohibido.

**[Slide 6] El RNF cuantificado: la diferencia esta en el numero** — 13 vinetas.

**[Slide 7] Si no se puede verificar, es un deseo** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - La regla de oro del oficio es dura y se enuncia asi: si no se puede verificar, no es un requisito, es un deseo.
  - Hay una lista negra de palabras que suenan a compromiso pero no comprometen a nada: rapido, amigable, facil, intuitivo, robusto, moderno, optimo, eficiente, seguro.
  - Cada vez que aparece una de esas palabras hay que preguntar cuanto, en que condiciones y como lo mediriamos delante del cliente.
  - La frase 4 del Dr. Ramirez, el sistema tiene que ser rapido, no se puede calificar ni aprobar ni rechazar
  - Convertida queda RNF-01: la busqueda de historial por documento del dueno debe devolver resultados en maximo 3 segundos, con 5.000 fichas cargadas y 10 usuarios trabajando al mismo tiempo.
  - Ahora si existe una prueba: se carga la base de ejemplo, se cronometra y el requisito pasa o no pasa.
  - Lo mismo con la frase 1: que las fichas no se pierdan no es requisito, pero RF-01 registrar una ficha con codigo unico e irrepetible mas RNF-04 respaldo automatico diario con restauracion probada una vez al mes, si lo son.

**[Slide 8] Priorizar con MoSCoW** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - Priorizar no es ordenar por gusto sino decidir con el cliente que pasa si algo no esta el dia de la entrega, y para eso se usa MoSCoW: Must es lo que sin ello el sistema no sirve y no se sale a produccion
  - Should es importante pero existe un plan B manual mientras tanto
  - Could es lo que se hace si sobra tiempo; y Won't es lo que se declara explicitamente fuera de ESTA version, que es la categoria mas valiosa de las cuatro porque es la unica que le pone freno al alcance infinito.
  - La regla practica es que los Must no deberian superar el 60% del esfuerzo estimado, porque si todo es Must nada es Must.
  - En la clinica: registrar dueno y mascota, consultar historial y agendar cita son Must, porque atacan los tres dolores de la clinica; el reporte mensual de consultas es Should
  - Porque hoy el Dr. Ramirez lo hace contando a mano y puede sobrevivir un mes mas; el envio de recordatorios por WhatsApp y la facturacion electronica son Won't de esta version
  - Y se escriben en el documento con esa etiqueta para que nadie los reclame despues como si hubieran sido prometidos.

**[Slide 9] La priorizacion MoSCoW en Mermaid** — 17 vinetas.

**[Slide 10] Trazabilidad hacia atrás y hacia adelante** — 4 vinetas.
  - DESARROLLO (para explicarlo, no se proyecta):
  - El ultimo pedazo es la trazabilidad, que es poder seguir cada requisito hacia atras y hacia adelante.
  - Hacia atras: de donde salio este RF, quien lo pidio, en que frase de la entrevista, en que fecha; asi cuando alguien pregunte y esto por que esta aqui hay respuesta y no cara de sorpresa.
  - Hacia adelante: en que caso de uso se desarrolla, en que pantalla del mockup se ve, en que clase del diagrama UML aparece y con que prueba se acepta.
  - Quien solo cursa Seminario cierra el ciclo distinto pero completo: su matriz termina en el prototipo navegable y en el documento de diseno, y eso es una entrega profesional valida, no una version reducida.
  - NOTAS:
  - Se lleva en una matriz simple de cuatro columnas y se actualiza cada clase.
  - Esto no es burocracia: es lo que permite que cuando el cliente cambie de opinion, usted sepa en dos minutos que se rompe y cuanto cuesta; y en el proyecto de diseño es lo que hace posible que el companero que solo cursa Programacion II reciba estos planos y sepa exactamente que implementar y por que, sin tener que volver a entrevistar al veterinario.

**[Slide 11] Ficha completa del requisito RF-03** — 12 vinetas.


**Demo que usted debe poder repetir:** El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy el tema es: Requerimientos de software. Todo lo que vamos a ver esta en las laminas.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en las laminas de teoria (una por concepto)
y en las de codigo proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en su VetCare?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 6/Plantillas/RF-RNF-VetCare.md`

### 60-105 · Practica guiada (OPCIONAL) = avance del PI
No hay laminas para esta franja: la guia es el archivo
`Clases/Clase 6 - Requerimientos de software/Taller PI - Clase 6 - VetCare.docx` (compartirlo, no proyectarlo).
Si hoy no se hace, usar el tiempo para profundizar la teoria y la demo.
**Decir (si se hace):** «Abran su proyecto VetCare. Trabajo individual por defecto; si autorice equipo, el archivo puede ser compartido pero cada uno entrega en ExamLab. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: copie en la plantilla las cinco frases crudas de la entrevista al Dr. Ramirez y marque cada una como NECESIDAD, anotando al lado quien la dijo y en que contexto; esa columna es el origen y no se puede dejar vacia.
2. Paso 2: traduzca las necesidades a requisitos funcionales usando la plantilla el sistema debe permitir a <actor> <accion> <objeto>, hasta llegar a minimo 8 RF numerados de RF-01 a RF-08; ningun RF puede contener la palabra y uniendo dos capacidades distintas.
3. Paso 3: derive 4 RNF, uno por categoria (desempeno, control de acceso, usabilidad y respaldo), y escriba en cada uno al menos un numero: segundos, cantidad de registros, frecuencia o porcentaje.
4. Paso 4: asigne prioridad MoSCoW a los 12 requisitos, verifique que los Must no pasen de seis y justifique en una linea por que los dos Won't quedan fuera de esta version de VetCare.
5. Paso 5: complete la matriz de trazabilidad con las columnas Necesidad, RF/RNF, Pantalla prevista y Prueba de aceptacion, exporte el documento a PDF y subalo a ExamLab con el nombre RF-RNF-VetCare-<sus apellidos>.pdf.
Circular por los puestos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.

### 105-120 · Sintesis y cierre
Si hubo practica, repasar los criterios de exito del archivo del taller (no estan en el deck).
Aplicar el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir (si hubo practica):** «Queda avanzado: Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx` — no proyectar completa.
