# Guion docente · Clase 1 · Conceptos iniciales de ingenieria de software

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Equipo conformado y dominio del proyecto acotado
- **Entregable de hoy:** Ficha del equipo: problema en 2-3 frases, 3-5 capacidades, 2-3 actores y lo que queda fuera de alcance
- **Herramienta:** Google Docs · draw.io
- **Slides:** `Clases/Clase 1 - Conceptos iniciales/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Programar es escribir codigo que funcione hoy. La ingenieria de software es el conjunto de practicas que hacen que ese codigo siga funcionando cuando el sistema crece, cuando lo mantiene otra persona y cuando los requisitos cambian. La diferencia no es filosofica sino economica: un error detectado al analizar requisitos cuesta corregirlo una fraccion de lo que cuesta corregirlo en produccion, cuando ya hay usuarios reales dependiendo del sistema. Esa curva de costo es la justificacion de todo lo que se vera en este curso; sin ella, las metodologias suenan a burocracia arbitraria.

Conviene separar dos palabras que se usan como sinonimos y no lo son. El producto es el software y su documentacion: lo que queda cuando todos se van. El proyecto es el esfuerzo acotado en tiempo y recursos para construirlo. Un proyecto termina; un producto puede seguir vivo diez años. Confundirlos lleva al equipo a pensar «ya entregamos, ya terminamos» y a no dejar nada escrito para quien venga despues. En VetCare, el proyecto es el semestre; el producto es el sistema que la clinica Huellitas usaria todos los dias.

Un requisito funcional dice QUE debe hacer el sistema: «registrar una mascota con ID, nombre y especie». Un requisito no funcional dice COMO debe comportarse: «la busqueda de un expediente responde en menos de dos segundos», «la informacion no se pierde ante un corte de energia». Los no funcionales son los que mas se olvidan y, paradojicamente, los que mas condicionan la arquitectura. La regla practica que el estudiante debe interiorizar desde hoy es: si no se puede verificar, no es un requisito, es un deseo. «El sistema debe ser rapido» no sirve; «responde en menos de 2 s con 50 usuarios simultaneos» si, porque alguien puede sentarse a comprobarlo.

Los interesados no son solo quien paga. En la clinica Huellitas hay al menos tres con intereses distintos: el dueño de la clinica quiere metricas del negocio, la recepcionista quiere agendar rapido y con pocos clics, y el veterinario quiere el historial del paciente a la mano durante la consulta. Esos intereses entran en conflicto: pedir mas datos da mejores metricas al dueño pero vuelve mas lento el registro para la recepcionista. Resolver ese conflicto, decidiendo que se prioriza y documentando por que, es trabajo de analisis, no de programacion.

Todo desarrollo pasa por las mismas fases —requisitos, diseño, construccion, pruebas, mantenimiento— y lo que cambia entre metodologias no son las fases sino COMO se recorren: una sola vez y en orden (cascada) o en ciclos cortos que repiten todas las fases (iterativo y agil). Hoy solo se nombran; se comparan a fondo en las Clases 2, 3 y 4. Lo importante del primer dia es que el estudiante entienda su rol en esta asignatura: aqui no se construye la casa, se dibujan los planos para que cualquier equipo pueda construirla. Decirlo explicitamente evita que quien esperaba programar se frustre a mitad de semestre.

Queda una pregunta que el estudiante hace el primer dia y conviene responder sin rodeos: para que sirve documentar si al final lo que se usa es el codigo. La respuesta esta en quien lee. El codigo lo lee la maquina y quien ya conoce el sistema; los planos los lee quien todavia no lo conoce: el companero que entra a mitad de semestre, el docente que califica, el equipo de Programacion II que va a construir VetCare a partir de estos documentos, y usted mismo dentro de seis semanas cuando ya no recuerde por que decidio lo que decidio. Documentar no es escribir bonito ni llenar plantillas: es dejar por escrito las decisiones y su justificacion, de modo que otro pueda continuar sin volver a entrevistar al cliente. Por eso en este curso cada entregable tiene un lector concreto, y la pregunta que se hace al calificar no es cuantas paginas tiene sino si ese lector podria trabajar con el sin preguntarle nada al autor.

Conviene tambien aclarar el mapa del semestre en una sola frase, porque de eso depende que el estudiante sepa donde esta parado en cada clase. Las primeras cuatro clases responden como se organiza el trabajo (ciclos de vida, metodologias tradicionales y agiles); de la sexta a la novena, que debe hacer el sistema (requisitos, historias de usuario, UML y casos de uso); de la once a la catorce, como se ve y como se sustenta (auditoria del avance, diagramas dinamicos, interfaces y sustentacion). Las clases 5, 10 y 15 son de parcial. Todo lo que se produzca en el camino se acumula en un unico paquete de diseno del proyecto VetCare, que es el entregable real de la asignatura; no hay trabajos sueltos que se boten al terminar la clase. Decir esto el primer dia evita la sensacion de estar haciendo tareas desconectadas.

Error tipico del docente que no domina el tema: empezar por las metodologias (cascada, Scrum) antes de que el estudiante entienda que problema resuelven. Sin la nocion de que el costo del error crece con el tiempo, Scrum se percibe como una serie de reuniones sin sentido y la documentacion como relleno para la nota. El segundo tropiezo es aceptar requisitos no verificables en la primera entrega («el sistema debe ser amigable»): si no se corrige el primer dia, ese vicio contamina los casos de uso, las pruebas y la sustentacion final.

**Demo que usted debe poder repetir:** Convertir en vivo la frase cruda «necesito buscar rapido el expediente de un animal» en un requisito funcional y uno no funcional bien escritos

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Equipo conformado y dominio del proyecto acotado. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: Convertir en vivo la frase cruda «necesito buscar rapido el expediente de un animal» en un requisito funcional y uno no funcional bien escritos
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 1/Plantillas/Ficha de dominio - VetCare.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. Formen equipo de 2-3 personas y definan quien sera el vocero tecnico del grupo ante el docente.
2. Escriban el problema en 2-3 frases: quien sufre que, y como se nota hoy ese dolor en la operacion diaria de la clinica.
3. Listen 3-5 capacidades del sistema, escritas como verbos de negocio (registrar, agendar, consultar), no como pantallas.
4. Identifiquen 2-3 actores y, para cada uno, que espera obtener del sistema.
5. Escriban explicitamente que NO hara el sistema este semestre (fuera de alcance): sin esa lista, el proyecto crece sin control.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Ficha del equipo: problema en 2-3 frases, 3-5 capacidades, 2-3 actores y lo que queda fuera de alcance

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 1/Quiz Clase 1 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Equipo conformado y dominio del proyecto acotado. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 1/Solucion Taller Clase 1 - VetCare.docx` — no proyectar completa.
