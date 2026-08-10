# Guion docente · Clase 6 · Requerimientos de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.
- **Entregable de hoy:** Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 6 - Requerimientos de software/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un requerimiento no es lo que el cliente dijo, es lo que el sistema debe hacer para que el problema del cliente desaparezca; entre esas dos cosas hay un trabajo de traduccion que se llama elicitacion, palabra que viene de sacar a la luz algo que estaba implicito. Las tres tecnicas que caben en este curso son baratas y no necesitan software especializado: la entrevista, donde se arranca con preguntas abiertas (cuenteme como es un dia normal en la clinica) y solo al final se cierran con preguntas de si o no; la observacion, donde uno se para media hora en la recepcion un sabado y cronometra cuanto tarda la auxiliar en encontrar una carpeta; y el prototipo desechable, donde uno dibuja una pantalla fea a mano o en draw.io y la pone frente al veterinario, porque la gente no sabe decir lo que quiere pero sabe perfectamente decir lo que NO quiere cuando lo ve. En VetCare la entrevista al Dr. Ramirez dejo cinco frases crudas: que las fichas no se pierdan, ver de una lo que le han hecho antes al paciente, que la auxiliar agende sin llamarlo, que el sistema sea rapido, y saber cuantas consultas se hicieron en el mes. Ninguna de esas cinco frases es todavia un requisito: son necesidades, y confundirlas es el primer error del analista novato.

Con las necesidades en la mano se separan dos familias. Un requisito funcional (RF) describe una capacidad observable del sistema, algo que alguien puede hacer con el, y se escribe con la plantilla el sistema debe permitir a <actor> <accion> <objeto> [bajo <condicion>]; el truco practico es que si al leerlo usted puede imaginar un boton, un formulario o una pantalla, es funcional. Un requisito no funcional (RNF) no describe QUE hace el sistema sino QUE TAN BIEN lo hace, y se agrupa en categorias conocidas: desempeno, seguridad y control de acceso, usabilidad, disponibilidad, respaldo, mantenibilidad y portabilidad. En VetCare, la frase que la auxiliar pueda agendar sin llamarme se convierte en dos cosas distintas al mismo tiempo: RF-05 el sistema debe permitir a la auxiliar registrar una cita seleccionando mascota, veterinario, fecha y hora; y RNF-02 el sistema debe manejar dos perfiles de acceso, auxiliar y veterinario, donde la auxiliar puede crear citas pero no puede editar ni ver el diagnostico clinico. Esa separacion importa porque el RF se prueba haciendo clic y el RNF se prueba midiendo o intentando lo prohibido.

La regla de oro del oficio es dura y se enuncia asi: si no se puede verificar, no es un requisito, es un deseo. Hay una lista negra de palabras que suenan a compromiso pero no comprometen a nada: rapido, amigable, facil, intuitivo, robusto, moderno, optimo, eficiente, seguro. Cada vez que aparece una de esas palabras hay que preguntar cuanto, en que condiciones y como lo mediriamos delante del cliente. La frase 4 del Dr. Ramirez, el sistema tiene que ser rapido, no se puede calificar ni aprobar ni rechazar; convertida queda RNF-01: la busqueda de historial por documento del dueno debe devolver resultados en maximo 3 segundos, con 5.000 fichas cargadas y 10 usuarios trabajando al mismo tiempo. Ahora si existe una prueba: se carga la base de ejemplo, se cronometra y el requisito pasa o no pasa. Lo mismo con la frase 1: que las fichas no se pierdan no es requisito, pero RF-01 registrar una ficha con codigo unico e irrepetible mas RNF-04 respaldo automatico diario con restauracion probada una vez al mes, si lo son.

Priorizar no es ordenar por gusto sino decidir con el cliente que pasa si algo no esta el dia de la entrega, y para eso se usa MoSCoW: Must es lo que sin ello el sistema no sirve y no se sale a produccion; Should es importante pero existe un plan B manual mientras tanto; Could es lo que se hace si sobra tiempo; y Won't es lo que se declara explicitamente fuera de ESTA version, que es la categoria mas valiosa de las cuatro porque es la unica que le pone freno al alcance infinito. La regla practica es que los Must no deberian superar el 60% del esfuerzo estimado, porque si todo es Must nada es Must. En VetCare: registrar dueno y mascota, consultar historial y agendar cita son Must, porque atacan los tres dolores de Huellitas; el reporte mensual de consultas es Should, porque hoy el Dr. Ramirez lo hace contando a mano y puede sobrevivir un mes mas; el envio de recordatorios por WhatsApp y la facturacion electronica son Won't de esta version, y se escriben en el documento con esa etiqueta para que nadie los reclame despues como si hubieran sido prometidos.

El ultimo pedazo es la trazabilidad, que es poder seguir cada requisito hacia atras y hacia adelante. Hacia atras: de donde salio este RF, quien lo pidio, en que frase de la entrevista, en que fecha; asi cuando alguien pregunte y esto por que esta aqui hay respuesta y no cara de sorpresa. Hacia adelante: en que caso de uso se desarrolla, en que pantalla del mockup se ve, en que clase del diagrama UML aparece y con que prueba se acepta. Se lleva en una matriz simple de cuatro columnas y se actualiza cada clase. Esto no es burocracia: es lo que permite que cuando el cliente cambie de opinion, usted sepa en dos minutos que se rompe y cuanto cuesta; y en el Proyecto Integrador es lo que hace posible que el companero que solo cursa Programacion II reciba estos planos y sepa exactamente que implementar y por que, sin tener que volver a entrevistar al veterinario. Quien solo cursa Seminario cierra el ciclo distinto pero completo: su matriz termina en el prototipo navegable y en el documento de diseno, y eso es una entrega profesional valida, no una version reducida.

Error tipico del docente que no domina el tema: creer que levantar requisitos es transcribir lo que dijo el cliente y calificar la lista por cantidad de vinetas. El docente que no domina esto acepta como RNF valido el sistema debe ser amigable e intuitivo, deja pasar RF que en realidad son tres requisitos pegados con la palabra y (el sistema debe registrar mascotas y generar reportes y enviar correos), no exige criterio de verificacion porque le parece que alarga el documento, y pone MoSCoW como adorno permitiendo que el 90% de la lista quede en Must. El resultado es un documento que se ve gordo y bonito y que en la siguiente clase no sirve para dibujar ni un caso de uso. El antidoto es sencillo y hay que aplicarlo en voz alta requisito por requisito: con que prueba concreta sabriamos, delante del Dr. Ramirez, que esto se cumplio. Si el estudiante no lo responde en una sola frase con un numero o un si/no, el requisito se devuelve; y si el requisito tiene una y en la mitad, se parte en dos antes de seguir.

**Demo que usted debe poder repetir:** El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 6/Plantillas/RF-RNF-VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Paso 1: copie en la plantilla las cinco frases crudas de la entrevista al Dr. Ramirez y marque cada una como NECESIDAD, anotando al lado quien la dijo y en que contexto; esa columna es el origen y no se puede dejar vacia.
2. Paso 2: traduzca las necesidades a requisitos funcionales usando la plantilla el sistema debe permitir a <actor> <accion> <objeto>, hasta llegar a minimo 8 RF numerados de RF-01 a RF-08; ningun RF puede contener la palabra y uniendo dos capacidades distintas.
3. Paso 3: derive 4 RNF, uno por categoria (desempeno, control de acceso, usabilidad y respaldo), y escriba en cada uno al menos un numero: segundos, cantidad de registros, frecuencia o porcentaje.
4. Paso 4: asigne prioridad MoSCoW a los 12 requisitos, verifique que los Must no pasen de seis y justifique en una linea por que los dos Won't quedan fuera de esta version de VetCare.
5. Paso 5: complete la matriz de trazabilidad con las columnas Necesidad, RF/RNF, Pantalla prevista y Prueba de aceptacion, exporte el documento a PDF y subalo a ExamLab con el nombre RF-RNF-VetCare-<sus apellidos>.pdf.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 6/Quiz Clase 6 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 6/Solucion Taller Clase 6 - VetCare.docx` — no proyectar completa.
