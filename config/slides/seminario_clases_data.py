# -*- coding: utf-8 -*-
"""Contenido pedagogico de Seminario de Sistemas 2026-2 (PI VetCare, diseño).

Fuente unica de la que `build_uniajc_seminario_all.py` genera slides, guiones,
talleres, quices, soluciones y plantillas de artefactos. Esta asignatura entrega
PLANOS (requisitos, UML, wireframes), no codigo: el mismo producto se programa en
Programacion II. Las clases 5, 10 y 15 son de parcial (solo evaluacion).
"""

CLASES = [
    {
        "n": 1,
        "slug": "Conceptos iniciales",
        "titulo": "Conceptos iniciales de ingenieria de software",
        "subtitulo": "Que es diseñar software y por que no es programar",
        "herramienta": "Google Docs · draw.io",
        "hito_pi": "Dominio del proyecto acotado (trabajo individual por defecto)",
        "entregable": "Ficha de dominio: problema en 2-3 frases, 3-5 capacidades, 2-3 actores y lo que queda fuera de alcance",
        "demo": "Convertir en vivo la frase cruda «necesito buscar rapido el expediente de un animal» en un requisito funcional y uno no funcional bien escritos",
        "teoria": [
            "Programar es escribir codigo que funcione hoy. La ingenieria de software es el conjunto de practicas que hacen que ese codigo siga funcionando cuando el sistema crece, cuando lo mantiene otra persona y cuando los requisitos cambian. La diferencia no es filosofica sino economica: un error detectado al analizar requisitos cuesta corregirlo una fraccion de lo que cuesta corregirlo en produccion, cuando ya hay usuarios reales dependiendo del sistema. Esa curva de costo es la justificacion de todo lo que se vera en este curso; sin ella, las metodologias suenan a burocracia arbitraria.",
            "Conviene separar dos palabras que se usan como sinonimos y no lo son. El producto es el software y su documentacion: lo que queda cuando todos se van. El proyecto es el esfuerzo acotado en tiempo y recursos para construirlo. Un proyecto termina; un producto puede seguir vivo diez años. Confundirlos lleva al equipo a pensar «ya entregamos, ya terminamos» y a no dejar nada escrito para quien venga despues. En VetCare, el proyecto es el semestre; el producto es el sistema que la clinica Huellitas usaria todos los dias.",
            "Un requisito funcional dice QUE debe hacer el sistema: «registrar una mascota con ID, nombre y especie». Un requisito no funcional dice COMO debe comportarse: «la busqueda de un expediente responde en menos de dos segundos», «la informacion no se pierde ante un corte de energia». Los no funcionales son los que mas se olvidan y, paradojicamente, los que mas condicionan la arquitectura. La regla practica que el estudiante debe interiorizar desde hoy es: si no se puede verificar, no es un requisito, es un deseo. «El sistema debe ser rapido» no sirve; «responde en menos de 2 s con 50 usuarios simultaneos» si, porque alguien puede sentarse a comprobarlo.",
            "Los interesados no son solo quien paga. En la clinica Huellitas hay al menos tres con intereses distintos: el dueño de la clinica quiere metricas del negocio, la recepcionista quiere agendar rapido y con pocos clics, y el veterinario quiere el historial del paciente a la mano durante la consulta. Esos intereses entran en conflicto: pedir mas datos da mejores metricas al dueño pero vuelve mas lento el registro para la recepcionista. Resolver ese conflicto, decidiendo que se prioriza y documentando por que, es trabajo de analisis, no de programacion.",
            "Todo desarrollo pasa por las mismas fases —requisitos, diseño, construccion, pruebas, mantenimiento— y lo que cambia entre metodologias no son las fases sino COMO se recorren: una sola vez y en orden (cascada) o en ciclos cortos que repiten todas las fases (iterativo y agil). Hoy solo se nombran; se comparan a fondo en las Clases 2, 3 y 4. Lo importante del primer dia es que el estudiante entienda su rol en esta asignatura: aqui no se construye la casa, se dibujan los planos para que cualquier equipo pueda construirla. Decirlo explicitamente evita que quien esperaba programar se frustre a mitad de semestre.",
            "Queda una pregunta que el estudiante hace el primer dia y conviene responder sin rodeos: para que sirve documentar si al final lo que se usa es el codigo. La respuesta esta en quien lee. El codigo lo lee la maquina y quien ya conoce el sistema; los planos los lee quien todavia no lo conoce: el companero que entra a mitad de semestre, el docente que califica, el equipo de Programacion II que va a construir VetCare a partir de estos documentos, y usted mismo dentro de seis semanas cuando ya no recuerde por que decidio lo que decidio. Documentar no es escribir bonito ni llenar plantillas: es dejar por escrito las decisiones y su justificacion, de modo que otro pueda continuar sin volver a entrevistar al cliente. Por eso en este curso cada entregable tiene un lector concreto, y la pregunta que se hace al calificar no es cuantas paginas tiene sino si ese lector podria trabajar con el sin preguntarle nada al autor.",
            "Conviene tambien aclarar el mapa del semestre en una sola frase, porque de eso depende que el estudiante sepa donde esta parado en cada clase. Las primeras cuatro clases responden como se organiza el trabajo (ciclos de vida, metodologias tradicionales y agiles); de la sexta a la novena, que debe hacer el sistema (requisitos, historias de usuario, UML y casos de uso); de la once a la catorce, como se ve y como se sustenta (auditoria del avance, diagramas dinamicos, interfaces y sustentacion). Las clases 5, 10 y 15 son de parcial. Todo lo que se produzca en el camino se acumula en un unico paquete de diseno del proyecto VetCare, que es el entregable real de la asignatura; no hay trabajos sueltos que se boten al terminar la clase. Decir esto el primer dia evita la sensacion de estar haciendo tareas desconectadas.",
            "Error tipico del docente que no domina el tema: empezar por las metodologias (cascada, Scrum) antes de que el estudiante entienda que problema resuelven. Sin la nocion de que el costo del error crece con el tiempo, Scrum se percibe como una serie de reuniones sin sentido y la documentacion como relleno para la nota. El segundo tropiezo es aceptar requisitos no verificables en la primera entrega («el sistema debe ser amigable»): si no se corrige el primer dia, ese vicio contamina los casos de uso, las pruebas y la sustentacion final."
        ],
        "taller": [
            "Modalidad de trabajo: individual por defecto. Abra su ficha de dominio y escriba su nombre. Si el docente autoriza equipos de 2 o 3 integrantes, la ficha puede ser compartida, pero la entrega en ExamLab siempre es individual y con sus propias palabras.",
            "Escriban el problema en 2-3 frases: quien sufre que, y como se nota hoy ese dolor en la operacion diaria de la clinica.",
            "Listen 3-5 capacidades del sistema, escritas como verbos de negocio (registrar, agendar, consultar), no como pantallas.",
            "Identifiquen 2-3 actores y, para cada uno, que espera obtener del sistema.",
            "Escriban explicitamente que NO hara el sistema este semestre (fuera de alcance): sin esa lista, el proyecto crece sin control."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ la ficha de hoy es la base de todo el paquete de diseño; si el dominio queda vago, los requisitos y los diagramas tambien.",
            "En esta asignatura el entregable son los planos, no el codigo: conviene decirlo desde el primer dia.",
            "El diagnostico de hoy no tiene nota: sirve para calibrar el ritmo de las proximas clases."
        ],
        "escenario": [
            "Dominio por defecto: la clinica veterinaria Huellitas del Proyecto Integrador.",
            "Herramientas: Google Docs para la ficha y draw.io o Excalidraw para el boceto.",
            "Se parte de cero: no hay documentacion previa del sistema."
        ],
        "criterios": [
            "El problema nombra un actor concreto y un dolor observable, no una generalidad.",
            "Las capacidades estan escritas como verbos de negocio y son entre 3 y 5.",
            "Los actores identificados tienen un interes explicito, no solo un nombre.",
            "La lista de fuera de alcance existe y es especifica."
        ],
        "pistas": [
            "¿Quien sufre el problema y como se mide hoy ese sufrimiento?",
            "¿Otro compañero entenderia mi sistema en 30 segundos, sin que se lo explique?",
            "¿Escribimos que NO hara el sistema, o dejamos la puerta abierta a que crezca sin control?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. El trabajo es individual por defecto: cada estudiante tiene su propia ficha y responde por todo el diseño, que es exactamente lo que se evalua en la sustentacion, donde se pregunta al azar. Si el docente autoriza un equipo, el maximo es tres personas —con mas, alguien queda sin trabajo real— y aun asi la entrega en ExamLab es individual: cada integrante redacta sus respuestas abiertas y debe poder explicar cualquier parte de la ficha en 60 segundos.",
            "Paso 2 resuelto. Un problema bien escrito para VetCare: «La clinica Huellitas atiende un alto volumen de pacientes y lleva su gestion en carpetas de papel. Se extravian fichas de pacientes y buscar un historial durante la consulta toma varios minutos, lo que genera filas en la sala de espera. Ademas la administracion no sabe cuantas especies distintas atiende al mes». Note que hay actor, dolor y consecuencia observable.",
            "Paso 3 resuelto. Capacidades como verbos de negocio: registrar dueños y sus mascotas; agendar citas medicas; consultar el historial clinico de una mascota; buscar un expediente por identificador; generar un conteo de atenciones por especie. Lo que NO es una capacidad: «tener una pantalla azul con botones», porque eso es una decision de interfaz, no una capacidad del sistema.",
            "Paso 4 resuelto. Actores con interes explicito: Recepcionista, que necesita registrar y agendar rapido porque tiene fila esperando; Veterinario, que necesita ver el historial completo durante la consulta; Administrador de la clinica, que necesita metricas mensuales para decidir compras e horarios. Escribir el interes al lado del actor es lo que despues permite priorizar requisitos en conflicto.",
            "Paso 5 resuelto. Fuera de alcance, escrito para que nadie lo discuta despues: no habra cobro ni facturacion electronica; no habra aplicacion movil; no habra acceso desde internet (el sistema es de escritorio, en la clinica); no habra historia clinica con imagenes ni radiografias. Cada linea de esta lista es una discusion que el equipo se ahorra en la Clase 11."
        ],
        "solucion_rubrica": [
            "Problema con actor y dolor observable (3)",
            "3-5 capacidades como verbos de negocio (3)",
            "Actores con interes explicito (2)",
            "Fuera de alcance especifico (2)"
        ],
        "solucion_errores": [
            "Dominio vago tipo «una app para la universidad»: sin problema concreto, todo el semestre se vuelve humo.",
            "Confundir capacidad con pantalla: «tener un formulario» no es una capacidad, «registrar una mascota» si.",
            "Omitir el fuera de alcance: el proyecto crece cada semana y el equipo no alcanza a cerrar nada."
        ],
        "codigo_slide_titulo": "De frase cruda a requisito verificable",
        "codigo_slide_lineas": [
            "FRASE DEL CLIENTE (entrevista):",
            "  \"Necesito buscar rapido el expediente de un animal usando solo su ID.\"",
            "",
            "RF-01  Buscar expediente por identificador",
            "  El sistema permite consultar la ficha completa de una mascota",
            "  a partir de su identificador unico.",
            "  Actor: Recepcionista, Veterinario",
            "",
            "RNF-01 Tiempo de respuesta de la busqueda",
            "  La consulta del RF-01 devuelve el resultado en menos de 2 segundos",
            "  con hasta 500 mascotas registradas.",
            "  Verificacion: medir con cronometro sobre el juego de datos de prueba."
        ],
        "codigo_slide_caption": "Si no se puede verificar, no es un requisito: es un deseo.",
        "artefacto_archivo": "Ficha de dominio - VetCare.md",
        "artefacto_contenido": "# Ficha de dominio del Proyecto Integrador — VetCare\n\n> Plantilla de la Clase 1. Trabajo **individual por defecto**: un archivo por estudiante. Se completa en clase y se sube a ExamLab.\n\n## Autor\nNombre: ______________________\n\n> Si el docente autorizo trabajo en equipo (2 o 3 integrantes), liste abajo a los demas\n> integrantes. La ficha puede ser compartida, pero la entrega en ExamLab es individual y\n> cada integrante debe poder explicar cualquier parte de este documento en 60 segundos.\n\n| Otros integrantes (opcional) |\n|---|\n|  |\n|  |\n\n## 1. Problema (2-3 frases)\nQuien sufre que, y como se nota hoy ese dolor en la operacion diaria.\n\n> _Escriba aqui._\n\n## 2. Capacidades del sistema (3 a 5)\nVerbos de negocio, no pantallas.\n\n1.\n2.\n3.\n4.\n5.\n\n## 3. Actores y su interes\n| Actor | Que espera obtener del sistema |\n|---|---|\n|  |  |\n|  |  |\n|  |  |\n\n## 4. Fuera de alcance (que NO hara el sistema este semestre)\nCada linea aqui es una discusion que se ahorran mas adelante.\n\n-\n-\n-\n\n## 5. Boceto de contexto\nAdjunte el PNG o el enlace del diagrama: el sistema como una caja, los actores\nalrededor y los sistemas externos con los que se conecta.\n\nEnlace / archivo: ______________________\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "¿Cual es la diferencia entre programar y hacer ingenieria de software?",
                "opciones": [
                    "A) Ninguna, son sinonimos",
                    "B) Programar es escribir codigo que funcione hoy; la ingenieria busca que siga funcionando al crecer, cambiar de manos y cambiar los requisitos",
                    "C) La ingenieria de software solo aplica a proyectos grandes de mas de 10 personas",
                    "D) Programar requiere titulo profesional y la ingenieria no"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "«La informacion no se pierde ante un corte de energia» es un requisito:",
                "opciones": [
                    "A) Funcional",
                    "B) No funcional",
                    "C) No es un requisito",
                    "D) De negocio"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "«El sistema debe ser rapido» es un requisito bien escrito.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "El producto y el proyecto son la misma cosa.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "En la clinica Huellitas, ¿cual de estos NO es un interesado del sistema?",
                "opciones": [
                    "A) La recepcionista que agenda las citas",
                    "B) El veterinario que consulta el historial",
                    "C) El proveedor de papeleria de la clinica",
                    "D) El administrador que necesita metricas mensuales"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Lo que cambia entre metodologias no son las fases del ciclo de vida, sino la forma de recorrerlas.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Convierta en un requisito funcional verificable la frase: «quiero ver una lista de quienes estan en la sala de espera».",
                "clave": "Ej: RF-0X Consultar sala de espera. El sistema muestra la lista de mascotas con cita registrada para el dia actual que aun no han sido atendidas, en orden de llegada. Actor: Recepcionista. Debe ser comprobable: alguien puede sentarse a verificar que la lista aparece y que respeta el orden."
            },
            {
                "tipo": "abierta",
                "q": "¿Por que se escribe explicitamente lo que el sistema NO hara?",
                "clave": "Porque acota el alcance y evita que el proyecto crezca sin control (scope creep). Cada linea de fuera de alcance es una discusion evitada mas adelante y protege al equipo de comprometerse a algo que no alcanza a entregar."
            }
        ],
        "fundamento": "Hay un concepto que explica por que este curso existe y que conviene instalar el primer dia sin jerga: la deuda tecnica. Cada vez que un equipo elige la salida rapida en lugar de la correcta, esta pidiendo prestado tiempo al futuro. El prestamo puede ser razonable, igual que un credito, pero se paga con intereses, y los intereses se cobran en forma de tiempo adicional en cada cambio posterior. La metafora la propuso Ward Cunningham en 1992 hablando de codigo, y funciona igual de bien para el diseno, que es lo que se hace aqui. Un caso de VetCare que ocurre todos los semestres: el equipo no decide si una Mascota puede existir sin un Dueno registrado, porque en la primera semana parece un detalle. Tres semanas despues, dos integrantes han asumido cosas distintas; uno diseno la pantalla de registro pidiendo el dueno primero y el otro escribio un caso de uso donde la mascota se registra sola y el dueno se asocia despues. Ahora hay que decidir, ajustar dos documentos, avisar al equipo y probablemente rehacer un wireframe. El trabajo extra es el interes de una decision que costaba dos minutos en la Clase 1. Como convencion practica, los equipos maduros reservan entre el diez y el veinte por ciento de cada iteracion para pagar deuda; no es una regla dura, es una forma de reconocer que la deuda no desaparece sola. Y hay una deuda que nunca conviene tomar: la que se contrae por no saber que se estaba decidiendo algo.\n\nEn un curso de diseno la deuda toma una forma particular y peligrosa: el artefacto desactualizado. Un diagrama que ya no corresponde a la decision vigente es peor que no tener diagrama, porque un documento que no existe obliga a preguntar, mientras que un documento equivocado convence. Quien lo lea tomara decisiones a partir de informacion falsa y descubrira el problema tarde. De ahi salen dos reglas que este curso aplica a todos los entregables. La primera: cada artefacto lleva fecha y version visibles, de modo que cualquiera pueda saber si esta mirando lo ultimo. La segunda: si una decision cambia, el artefacto se actualiza en la misma semana y el cambio queda anotado en una linea, con la fecha y el motivo; ese registro es lo que en la sustentacion de la Clase 14 distingue a un equipo que diseno de un equipo que improviso y despues escribio el documento hacia atras. Vale decirlo explicitamente porque contradice el habito escolar: aqui no se penaliza cambiar de opinion, se penaliza tener dos verdades circulando al mismo tiempo. Un equipo que cambio tres veces el alcance y lo registro esta mejor evaluado que uno que entrega un documento perfecto que nadie uso.\n\nEl segundo concepto de fondo es la palabra modelo, que se usa todo el semestre sin definirla. Un modelo es una representacion simplificada de algo real, construida para responder un conjunto acotado de preguntas. La parte que sorprende al estudiante es que un modelo util es necesariamente incompleto, y la razon es aritmetica y no filosofica: un modelo que incluyera todo seria del tamano del territorio que representa y por lo tanto no serviria para nada, porque un mapa a escala uno a uno pesa lo mismo que la ciudad y no cabe en el bolsillo. La formula que se cita habitualmente es que el mapa no es el territorio. Consecuencia operativa, y este es el criterio que el estudiante debe llevarse: para cada diagrama que va a dibujar hay que poder nombrar dos cosas, cual pregunta responde y quien es la persona que la hace. Si no se pueden nombrar, el diagrama no va. En VetCare, un diagrama de casos de uso responde quien hace que y con que finalidad, y le sirve al dueno de la clinica para confirmar que no falta ningun tramite; no responde en cuanto tiempo se busca un expediente ni como se guardan los datos, y quien busque eso ahi va a leer mal. Esas otras preguntas tienen sus propios modelos, y el curso los introduce en las Clases 8, 9 y 12. Reconocer que cada diagrama es parcial es lo que permite tener varios sin contradecirse.\n\nDe ahi se sigue que un modelo puede estar mal de dos maneras opuestas, y conviene decirlas juntas porque los equipos suelen corregir una cayendo en la otra. Puede omitir algo que si importaba para la pregunta que promete responder, y entonces es incompleto donde no debia. O puede incluir tanto detalle que nadie lo lee, y entonces es ruido con apariencia de rigor. La segunda falla es la mas comun en trabajos de curso, porque el estudiante asume que mas paginas equivalen a mas nota. Sirven algunas magnitudes de referencia, todas convenciones de este curso y no reglas del lenguaje: un diagrama de casos de uso legible rara vez pasa de quince o veinte casos; un diagrama con cuarenta elementos ya no se puede discutir en una reunion; una historia de usuario cabe en dos o tres lineas. Y hay una prueba empirica que reemplaza cualquier lista de verificacion: entregue el artefacto a un compañero que no haya trabajado en su documento, sin explicarle nada, y pidale que lo explique en tres minutos. Lo que no pueda explicar, no comunica, y hay que arreglarlo. La pregunta previsible aqui es cuantos diagramas hay que hacer entonces, y la respuesta que hay que sostener todo el semestre es que se hacen los que responden preguntas que alguien tiene, y que un diagrama sin lector es trabajo perdido aunque este perfecto.\n\nLo anterior conduce al criterio que gobierna todas las entregas de este curso: la diferencia entre un documento que alguien puede usar y uno que solo existe para la nota. Son cinco rasgos y todos son verificables desde afuera. Uno, tiene un lector nombrado y una pregunta que responde. Dos, es verificable: sus afirmaciones se pueden confirmar o refutar, lo que en requisitos significa criterios de aceptacion. Tres, es trazable: cada requisito tiene identificador y se puede seguir hasta el artefacto donde se resuelve. Cuatro, esta fechado y versionado. Cinco, es accionable: alguien puede tomar una decision o construir algo con el. Comparemos en VetCare. Version para la nota: el sistema debe ser amigable e intuitivo y permitir gestionar la informacion de las mascotas de manera eficiente. Nadie puede construir eso ni puede decir si se cumplio. Version usable: RF-012, el sistema permite registrar una mascota con identificador, nombre, especie, fecha de nacimiento y dueno asociado; criterio de aceptacion, dado un dueno ya registrado, cuando la recepcionista guarda la mascota con esos cinco datos, entonces la mascota aparece en el listado de ese dueno, y si el dueno no existe el registro se rechaza con un mensaje; origen, entrevista con la recepcionista; prioridad, alta. La segunda version se puede programar, se puede probar y se puede discutir con el dueno de la clinica. Los tres rellenos que hay que prohibir desde hoy son la definicion copiada de un libro, la historia del origen de la ingenieria de software y las promesas sin sujeto del tipo se garantizara la calidad.\n\nEl rasgo tres merece su propio parrafo porque es el hilo que amarra el semestre: la trazabilidad. Trazabilidad es poder seguir un requisito desde su origen, es decir quien lo pidio, hasta el artefacto que lo resuelve y el criterio que lo verifica. En este curso la cadena es concreta y siempre la misma: un interesado dice algo en una entrevista, eso se convierte en un requisito con identificador en la Clase 6, se expresa como historia de usuario en la Clase 7, aparece como caso de uso en la Clase 9, se dibuja como pantalla en la Clase 13 y se cierra con un criterio de aceptacion que permite decir si quedo hecho. Dos controles simples permiten auditar esa cadena sin herramientas: todo requisito funcional debe aparecer al menos una vez en algun caso de uso, y todo caso de uso debe poder senalar el requisito que lo origina. Un requisito huerfano, que no aparece en ningun sitio, es una de dos cosas: algo que nadie necesita y hay que eliminar, o un hueco de diseno que nadie noto; ambas conclusiones son valiosas y ambas se pierden si el equipo escribe cada documento como si fuera independiente. Esta es tambien la razon por la que en la Clase 11 se revisa el avance mirando la coherencia entre artefactos y no la cantidad de paginas.\n\nHay un asunto de organizacion que el docente debe resolver el primer dia porque afecta la calificacion: los estudiantes llegan en tres situaciones de matricula distintas y cada una cierra su entregable de manera diferente. Primera situacion, quien cursa Seminario y Programacion II al mismo tiempo. Este es el caso ideal y hay que aprovecharlo: se acota el dominio de VetCare una sola vez y el entregable de diseno de este curso se convierte en el insumo real del codigo del otro. El riesgo es conocido, y consiste en que el estudiante se entusiasme programando y descuide el documento; la regla de cierre es que aqui se califica el plano y no la demostracion, y que si el codigo se desvio del plano lo correcto es actualizar el plano y anotar por que, nunca esconder la diferencia. Segunda situacion, quien cursa solo Programacion II: no entrega en este curso, pero importa porque los equipos son mixtos y puede haber companeros de proyecto que no esten en esta aula. De ahi sale una exigencia concreta para el documento: debe ser autosuficiente, entendible por alguien que no estuvo en las conversaciones del equipo; si el artefacto solo se entiende cuando su autor lo explica de viva voz, no sirve para ese companero y por lo tanto no sirve. Tercera situacion, quien cursa solo Seminario: cierra el semestre con el juego completo de planos y la sustentacion, y no se le exige ni una linea de codigo ni una demostracion funcionando; su nota no depende de que exista implementacion. Su prueba de calidad es otra y hay que decirsela en estos terminos: que un tercero pueda construir el producto leyendo su documento. En su caso el wireframe de la Clase 13 cumple el papel que en el otro curso cumple la pantalla.\n\nQueda la trampa pedagogica de este primer dia, y es la mas seria del curso: el estudiante que se matriculo esperando programar y descubre que va a escribir documentos. Si no se encuadra hoy, ese estudiante pasa quince semanas convencido de que el curso es trabajo administrativo, y el sintoma aparece en la primera entrega en forma de documentos hechos en la ultima hora. El encuadre tiene cuatro movimientos y conviene hacerlos en este orden. Primero, reconocerlo en voz alta, porque negarlo lo confirma: aqui varios querian programar, y programar es legitimo y necesario. Segundo, dar el argumento del costo con numeros aunque sean gruesos: borrar una caja de un diagrama toma diez segundos, mientras que eliminar un modulo ya programado, probado e integrado toma dias y arrastra todo lo que dependia de el; ese es el orden de magnitud que justifica dibujar antes. Tercero, mostrar que las decisiones que el programador ya no podra cambiar se toman aqui, con ejemplos que se sienten reales: si una Mascota puede existir sin Dueno, o si reagendar una cita es modificarla o es cancelarla y crear otra, que es una decision de diseno con consecuencias en el historial clinico durante anos. Cuarto, dar salidas legitimas al deseo de construir: en la Clase 13 hay trabajo visual concreto con interfaces, en la Clase 11 se compara el diseno con lo que se esta construyendo, y en la Clase 12 los diagramas avanzados exigen precision tecnica. Conviene tambien nombrar el perfil profesional, porque el estudiante rara vez lo tiene claro: analista, arquitecto y product owner son cargos que existen y que se pagan bien precisamente por traducir entre el negocio y la tecnica. Y hay que anticipar la pregunta textual, porque va a llegar: profesor, para que dibujo esto si lo voy a cambiar cuando programe. La respuesta es que el diagrama es justamente lo que hace barato ese cambio, y que cuando cambie, se actualiza y se anota el motivo, y ese registro es parte de lo que se evalua.\n\nError tipico del docente que no domina el tema: el primero es tratar el curso como una lista de artefactos por producir, es decir pedir los requisitos, despues las historias, despues los casos de uso y despues los wireframes, sin conectarlos nunca entre si. El estudiante aprende a llenar plantillas y produce un paquete donde el caso de uso no corresponde al requisito ni el wireframe al caso de uso; el problema estalla en la Clase 11 y en la sustentacion final, cuando una sola pregunta de trazabilidad, de donde salio este requisito y donde se resuelve, deja sin respuesta a todo el equipo. El segundo es no encuadrar el primer dia la naturaleza de la materia, o encuadrarla con la frase suelta de que aqui no se programa. Dicha asi suena a advertencia disciplinaria y el estudiante concluye que el curso es teoria; hay que decirlo con el argumento del costo y con la fase del proyecto en la mano. Sin ese encuadre, la Clase 6 de requerimientos se recibe como un tramite, y los documentos que lleguen no seran usables por nadie, lo que arruina justamente al estudiante que si cursa Programacion II y esperaba construir con esos planos."
    },
    {
        "n": 2,
        "slug": "Ciclos de vida del software",
        "titulo": "Ciclos de vida del software",
        "subtitulo": "Las mismas fases, recorridas de distinta forma",
        "herramienta": "draw.io · Google Docs",
        "hito_pi": "Queda listo el mapa de fases de VetCare con el artefacto concreto que produce cada fase y la marca de en cual esta parado el equipo hoy.",
        "entregable": "Un documento de una pagina en Google Docs con la tabla Fase / Pregunta que responde / Artefacto de VetCare / Quien lo aprueba, mas dos diagramas en draw.io (recorrido lineal y recorrido en tres vueltas) exportados a PDF y subidos a ExamLab.",
        "demo": "El docente arma en vivo en draw.io el ciclo de VetCare en dos versiones, una sola pasada y tres vueltas, y muestra que las cajas son identicas y lo unico que cambia es el recorrido.",
        "teoria": [
            "Un ciclo de vida del software es el orden en que se recorren las etapas que van desde que alguien dice 'necesito un sistema' hasta que ese sistema se apaga definitivamente. Las etapas clasicas son cinco: requisitos, diseño, construccion, pruebas y mantenimiento. Lo importante no es memorizar los nombres sino entender que cada fase tiene tres cosas: una entrada (lo que recibe de la fase anterior), una salida tangible llamada artefacto (un documento, un diagrama, un programa) y un criterio para decir 'esto ya quedo'. Si una fase no produce un artefacto verificable, esa fase no existe, existe una conversacion. En VetCare la fase de requisitos no termina cuando el equipo 'ya entendio' el problema de Huellitas: termina cuando existe una lista numerada de requisitos funcionales y no funcionales que la clinica leyo y aprobo.",
            "Vale la pena decir con precision que produce cada fase, porque ahi se cae la mitad de los equipos. Requisitos responde la pregunta QUE debe hacer el sistema y produce la lista de RF y RNF, el glosario y las reglas de negocio. Diseño responde COMO se va a lograr y produce casos de uso, diagramas de clases, modelo de datos, wireframes y mockups. Construccion es escribir el codigo y produce el ejecutable. Pruebas verifica que lo construido corresponde a lo pedido y produce casos de prueba y evidencias. Mantenimiento arregla, ajusta y evoluciona el sistema ya en uso. En nuestro Proyecto Integrador esto se reparte: Seminario de Sistemas vive en requisitos y diseño (los planos), y Programacion II vive en construccion y pruebas (la obra). Por eso aqui nunca se califica codigo: se califica que los planos esten completos, coherentes y sean construibles.",
            "La gran decision no es cuales fases hacer, sino cuantas veces recorrerlas y con cuanto sistema a la vez. Recorrerlas una sola vez y en orden significa cerrar requisitos de TODO VetCare, luego diseñar TODO VetCare, luego construir TODO. Recorrerlas en ciclos significa tomar un pedazo util del sistema y pasarlo por las cinco fases en una vuelta corta, y despues repetir con el siguiente pedazo. En VetCare la vuelta 1 podria ser solo la ficha del paciente (requisitos de la ficha, diseño de la ficha, mockup de la ficha, revision con la clinica); la vuelta 2, la historia clinica y la busqueda; la vuelta 3, los reportes y metricas. La diferencia practica es brutal: en el recorrido unico la clinica ve algo hasta el final y un malentendido de la semana 2 se descubre en la semana 15; en el recorrido en ciclos la clinica opina cada dos o tres semanas y el error se corrige cuando todavia es barato corregirlo.",
            "Hay que separar dos palabras que los equipos usan como sinonimos y no lo son: proyecto y producto. Un proyecto es un esfuerzo temporal, con inicio, fin, alcance, presupuesto y responsables; se acaba y se cierra. Un producto es el sistema vivo, que la gente usa, que tiene versiones y que sigue existiendo cuando el proyecto ya se cerro. En VetCare el proyecto es 'entregar los planos y el prototipo de VetCare en este semestre'; el producto es el sistema que Huellitas usaria durante los proximos años, con su version 1.0, su 1.1 cuando pidan vacunacion a domicilio y su 2.0 cuando quieran facturacion electronica. Esta distincion tiene una consecuencia dura: la fase mas larga y mas costosa de la vida de un sistema no es construirlo, es mantenerlo, y por eso el diseño y la documentacion que hacemos aqui no son un tramite, son lo que permite que otro entienda el sistema dentro de dos años.",
            "Como se elige el recorrido? Con criterios, no con moda. Si los requisitos son estables, el contrato es cerrado y el sistema es critico, conviene un recorrido lineal con aprobaciones formales. Si el dominio es nuevo, el cliente descubre lo que quiere cuando lo ve, y hay margen para ajustar, conviene un recorrido en ciclos. En VetCare aplican los dos matices: los datos basicos de un paciente (nombre, especie, raza, propietario) son estables y se pueden cerrar temprano; el tablero de metricas es incierto porque la clinica nunca ha visto uno y va a cambiar de opinion apenas lo vea. Ademas, el ciclo elegido debe caber en la realidad del curso: el estudiante que solo cursa Seminario cierra con documento de diseño y prototipo navegable, y esa es una ruta completa, porque el ciclo de vida del software incluye fases donde no se escribe una sola linea de codigo y aun asi se produce valor.",
            "Error tipico del docente que no domina el tema: confundir ciclo de vida con metodologia y decir que 'cascada es malo y agil es bueno'. Ciclo de vida es el conjunto de fases; metodologia es la forma organizada de recorrerlas. Agil no elimina el analisis ni el diseño, los distribuye en vueltas cortas. El segundo error, mas fino, es llamar iterativo a algo que solo es incremental: si el equipo entrega el modulo de pacientes, luego el de citas y luego el de reportes, y nunca vuelve a tocar lo entregado, eso es incremental pero no iterativo; iterar es volver sobre lo mismo y mejorarlo tras la retroalimentacion del cliente. El tercer error es proyectar el diagrama de cascada con flechitas hacia atras y decir 'ven, es iterativo': esas flechas son retrabajo por errores detectados, no vueltas planificadas de mejora."
        ],
        "taller": [
            "En Google Docs cree la tabla de cuatro columnas (Fase / Pregunta que responde / Artefacto concreto de VetCare / Quien lo aprueba) y llenela con las cinco fases; en la columna del artefacto esta prohibido escribir generalidades: debe decir cosas como 'Lista RF-01 a RF-12 de Huellitas' o 'Mockup de la ficha del paciente'.",
            "Marque con relleno amarillo la fila de la fase donde esta el equipo hoy y escriba debajo dos evidencias verificables que lo demuestren (por ejemplo: 'existe la entrevista transcrita' y 'no existe ningun diagrama aprobado').",
            "En draw.io dibuje el recorrido lineal de VetCare: cinco cajas en fila, y sobre cada flecha escriba el artefacto que se entrega para poder pasar a la siguiente fase.",
            "Duplique la pagina en draw.io y dibuje el recorrido en tres vueltas: las mismas cinco cajas, pero con las vueltas rotuladas Incremento 1 (ficha del paciente), Incremento 2 (historia clinica y busqueda) e Incremento 3 (reportes y metricas), y una flecha de retroalimentacion desde la clinica hacia requisitos.",
            "Escriba al final del documento un parrafo de tres renglones titulado 'Producto vs proyecto en VetCare' que responda: cuando termina el proyecto, cuando terminaria el producto y un ejemplo concreto de una solicitud de mantenimiento; exporte a PDF y suba el archivo a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ VetCare no se dibuja de una sola sentada, y hoy definimos el mapa de fases que vamos a recorrer todo el semestre y en cual de ellas se califica cada entrega.",
            "En la clase anterior quedo claro el dolor de Huellitas (fichas que se extravian, busquedas eternas y cero metricas); hoy ese dolor se ubica dentro de un ciclo de vida y se le pone nombre a lo que sale de cada etapa.",
            "Los tres casos de matricula se entienden mejor con el ciclo en la mano: aqui vivimos en requisitos y diseño, Programacion II vive en construccion y pruebas, y quien solo cursa Seminario cierra con documento de diseño y prototipo navegable."
        ],
        "escenario": [
            "Huellitas guarda hoy 5.000 fichas en carpetas de carton dentro de un archivador metalico, y las citas del dia se anotan a mano en una libreta que se lleva la auxiliar.",
            "El equipo tiene una lista cruda de necesidades salida de la entrevista, pero nadie ha definido que documento sale de cada etapa ni quien lo firma como aprobado.",
            "No existe ni una linea de codigo ni un diagrama formal: se parte de cero y el unico insumo real es lo que dijo la clinica."
        ],
        "criterios": [
            "La tabla tiene las cinco fases y en cada una un artefacto concreto de VetCare escrito con nombre propio, no una definicion generica de libro.",
            "El diagrama lineal y el diagrama en vueltas usan exactamente las mismas cinco cajas; lo unico distinto entre ellos es el recorrido.",
            "La fase actual del equipo esta marcada y sustentada con dos evidencias verificables del estado real de VetCare.",
            "El parrafo final distingue con hechos concretos cuando termina el proyecto y cuando terminaria el producto, e incluye un ejemplo de mantenimiento."
        ],
        "pistas": [
            "Si borro la palabra VetCare de su tabla, esa tabla serviria igual para un cajero automatico o para una tienda de ropa? Si la respuesta es si, todavia no aterrizo nada.",
            "En su diagrama de vueltas, cada vuelta termina en algo que la veterinaria podria mirar y opinar, o termina en trabajo interno que solo entiende el equipo?",
            "Que documento exacto tendria que mostrar hoy, en pantalla, para demostrarle a la clinica que la fase de requisitos ya quedo cerrada?"
        ],
        "solucion_pasos": [
            "Tabla resuelta: Requisitos responde QUE debe hacer VetCare y produce la lista RF-01 registrar paciente, RF-02 registrar consulta, RF-03 buscar historial, RNF-01 tiempo de respuesta menor a 3 segundos, aprobada por la administradora de Huellitas. Diseño responde COMO y produce el diagrama de casos de uso, el diagrama de clases, el modelo entidad-relacion y los mockups de la ficha, aprobados por el docente en rol de arquitecto. Construccion produce el codigo del modulo de pacientes y se aprueba en Programacion II. Pruebas produce los casos de prueba de aceptacion y sus evidencias, aprobados por la veterinaria. Mantenimiento produce las solicitudes de cambio y las versiones 1.1 y 1.2, aprobadas por la clinica.",
            "Fase actual resuelta: el equipo esta cerrando REQUISITOS. Evidencia 1: existe la entrevista con Huellitas transcrita y una lista cruda de necesidades. Evidencia 2: no existe ningun diagrama UML ni mockup aprobado, luego la fase de diseño no ha empezado formalmente. Conclusion escrita: no se puede diseñar la pantalla de busqueda mientras no este claro por cuales campos se busca.",
            "Diagrama lineal resuelto en draw.io: Requisitos -> Diseño con la flecha rotulada 'Documento RF/RNF aprobado'; Diseño -> Construccion rotulada 'Casos de uso, clases, modelo de datos y mockups'; Construccion -> Pruebas rotulada 'Modulo de pacientes ejecutable'; Pruebas -> Mantenimiento rotulada 'Acta de aceptacion firmada'. Una nota al pie aclara que si la clinica cambia de opinion en la ultima flecha, hay que devolverse hasta requisitos y rehacer todo lo intermedio.",
            "Diagrama en vueltas resuelto: tres ciclos con las mismas cinco cajas. Vuelta 1 Incremento 1 'Ficha del paciente' entrega el mockup navegable de la ficha; Vuelta 2 Incremento 2 'Historia clinica y busqueda' entrega el caso de uso y el prototipo de busqueda; Vuelta 3 Incremento 3 'Reportes y metricas' entrega el tablero de indicadores. Desde la caja de pruebas de cada vuelta sale una flecha punteada rotulada 'Retroalimentacion de Huellitas' que regresa a requisitos de la vuelta siguiente.",
            "Parrafo resuelto: 'El proyecto VetCare termina cuando se entregan y aprueban los planos, el prototipo navegable y el documento de diseño al cierre del semestre. El producto VetCare no termina ahi: sigue vivo mientras Huellitas lo use, con su version 1.0 en operacion. Ejemplo de mantenimiento: tres meses despues la clinica pide registrar vacunacion a domicilio con la direccion del cliente, lo cual obliga a volver a requisitos, ajustar el modelo de datos y liberar la version 1.1.'"
        ],
        "solucion_rubrica": [
            "Tabla de fases con artefactos propios de VetCare y responsable de aprobacion (3)",
            "Diagrama lineal en draw.io con artefacto rotulado en cada flecha (2)",
            "Diagrama en tres vueltas con incrementos nombrados y flecha de retroalimentacion (3)",
            "Parrafo producto vs proyecto con ejemplo concreto de mantenimiento (2)"
        ],
        "solucion_errores": [
            "Copiar la definicion de las fases de internet y dejar la columna del artefacto en abstracto ('documentacion', 'analisis'), sin nombrar un solo entregable real de Huellitas.",
            "Dibujar el diagrama iterativo con cajas distintas a las del lineal, como si iterar cambiara las fases; iterar cambia el recorrido, no las fases.",
            "Confundir incremento con iteracion: entregar modulo tras modulo sin volver nunca sobre lo ya entregado, y llamar a eso 'trabajo iterativo'."
        ],
        "codigo_slide_titulo": "El ciclo de vida de VetCare en Mermaid: mismas cajas, dos recorridos",
        "codigo_slide_lineas": [
            "flowchart LR",
            "  A[Requisitos] -->|RF-01 a RF-12 aprobados| B[Diseno]",
            "  B -->|Casos de uso + clases + mockups| C[Construccion]",
            "  C -->|Modulo ficha del paciente| D[Pruebas]",
            "  D -->|Acta de aceptacion| E[Operacion y mantenimiento]",
            "  E -.->|Solicitud: vacunacion a domicilio| A",
            "%% Recorrido lineal  = UNA sola pasada por A..E",
            "%% Recorrido en ciclos = TRES pasadas por A..E",
            "%%   Vuelta 1: ficha del paciente",
            "%%   Vuelta 2: historia clinica y busqueda",
            "%%   Vuelta 3: reportes y metricas",
            "%% Las cajas nunca cambian; lo que cambia es cuantas veces se recorren"
        ],
        "codigo_slide_caption": "Las fases son las mismas en cualquier metodologia; lo unico que se negocia es cuantas vueltas se dan y cuanto sistema entra en cada vuelta.",
        "artefacto_archivo": "Mapa-Ciclo-de-Vida-VetCare.md",
        "artefacto_contenido": "# Mapa de ciclo de vida - Proyecto Integrador VetCare\n**Clinica Veterinaria Huellitas** | Seminario de Sistemas | Estudiante: ______________\n\n> Recuerde: en esta asignatura se dibujan los planos. Nada de codigo.\n\n---\n\n## 1. Las cinco fases y lo que produce cada una\n\n| Fase | Pregunta que responde | Artefacto concreto de VetCare | Quien lo aprueba | Listo? |\n|---|---|---|---|---|\n| Requisitos | Que debe hacer el sistema? | Lista RF-01..RF-12 y RNF-01..RNF-05 de Huellitas | Administradora de la clinica | [ ] |\n| Diseno | Como lo va a lograr? | Casos de uso, diagrama de clases, modelo de datos, mockups | Docente en rol de arquitecto | [ ] |\n| Construccion | Con que se arma? | Codigo del modulo (se hace en Programacion II) | Docente de Programacion II | [ ] |\n| Pruebas | Hace lo que se pidio? | Casos de prueba de aceptacion + evidencias | Veterinaria de Huellitas | [ ] |\n| Mantenimiento | Que cambia ahora? | Solicitudes de cambio, version 1.1, 1.2 | Comite de la clinica | [ ] |\n\n---\n\n## 2. En que fase estamos hoy?\n\nMarque con X: [ ] Requisitos  [ ] Diseno  [ ] Construccion  [ ] Pruebas  [ ] Mantenimiento\n\n- Evidencia 1 que lo demuestra: ______________________________________\n- Evidencia 2 que lo demuestra: ______________________________________\n- Que artefacto falta para cerrar esta fase: ___________________________\n\n---\n\n## 3. Recorrido A - una sola pasada (lineal)\n\n```\nRequisitos --[doc RF/RNF aprobado]--> Diseno --[UML + mockups]--> Construccion\n   --[modulo ejecutable]--> Pruebas --[acta de aceptacion]--> Mantenimiento\n```\nRiesgo escrito por el equipo: __________________________________________\n\n---\n\n## 4. Recorrido B - tres vueltas (iterativo e incremental)\n\n| Vuelta | Incremento | Que ve la clinica al final de la vuelta | Semana estimada |\n|---|---|---|---|\n| 1 | Ficha del paciente | Mockup navegable de la ficha | |\n| 2 | Historia clinica y busqueda | Prototipo de busqueda por nombre y documento | |\n| 3 | Reportes y metricas | Tablero de indicadores de la clinica | |\n\nDespues de cada vuelta: **retroalimentacion de Huellitas -> vuelve a Requisitos.**\n\n---\n\n## 5. Producto vs proyecto\n\n- El **proyecto** VetCare termina cuando: ________________________________\n- El **producto** VetCare terminaria cuando: _____________________________\n- Ejemplo real de mantenimiento que ya podemos anticipar: ________________\n\n---\n\n## 6. Checklist antes de subir a ExamLab\n\n- [ ] La tabla nombra artefactos de VetCare, no definiciones genericas.\n- [ ] Los dos diagramas usan las mismas cinco cajas.\n- [ ] La fase actual esta marcada y sustentada con dos evidencias.\n- [ ] El PDF exportado abre correctamente y lleva el nombre del equipo.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare, cual es el artefacto que debe producir la fase de requisitos para poder decir que la fase quedo cerrada?",
                "opciones": [
                    "A) El diagrama de clases del sistema",
                    "B) La lista numerada de RF y RNF revisada y aprobada por Huellitas",
                    "C) La base de datos creada con las tablas de pacientes",
                    "D) El manual de usuario del modulo de citas"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "El equipo entrega el modulo de pacientes, luego el de citas y luego el de reportes, y nunca vuelve a tocar lo ya entregado. Como se llama eso?",
                "opciones": [
                    "A) Iterativo puro, porque hay varias entregas",
                    "B) Incremental, pero no iterativo",
                    "C) Cascada pura",
                    "D) Mantenimiento evolutivo"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual afirmacion describe correctamente la diferencia entre proyecto y producto en VetCare?",
                "opciones": [
                    "A) Son sinonimos: cuando se entrega el sistema terminan los dos",
                    "B) El producto es el cronograma y el proyecto es el software",
                    "C) El proyecto es el esfuerzo temporal que se cierra al entregar; el producto es el sistema que sigue vivo y evolucionando en Huellitas",
                    "D) El proyecto solo existe si hay contrato firmado; si no, solo hay producto"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Huellitas pide un tablero de metricas que nunca ha visto y sobre el cual no sabe que indicadores quiere. Que recorrido conviene para esa parte del sistema?",
                "opciones": [
                    "A) Una sola pasada lineal, cerrando requisitos al inicio",
                    "B) Ciclos cortos con prototipos que la clinica pueda ver y corregir",
                    "C) Saltarse el diseno y construir directamente",
                    "D) Dejarlo para mantenimiento y no analizarlo"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Un ciclo de vida iterativo elimina la fase de requisitos, porque los requisitos se van descubriendo mientras se programa.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "En un recorrido lineal y en uno en ciclos las fases del ciclo de vida son basicamente las mismas; lo que cambia es cuantas veces se recorren y cuanto sistema entra en cada vuelta.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Diga en que fases del ciclo de vida se ubica Seminario de Sistemas y en cuales Programacion II, y nombre un artefacto concreto de VetCare que entrega cada una.",
                "clave": "Seminario vive en requisitos y diseno y entrega la lista RF/RNF, los casos de uso, el diagrama de clases, el modelo de datos y los mockups; Programacion II vive en construccion y pruebas y entrega el modulo ejecutable y los casos de prueba con sus evidencias."
            },
            {
                "tipo": "abierta",
                "q": "Tres meses despues de entregado VetCare, Huellitas pide registrar vacunacion a domicilio. En que fase del ciclo de vida cae esa solicitud y que se debe hacer antes de tocar el sistema?",
                "clave": "Cae en mantenimiento (evolutivo). Antes de tocar el sistema hay que volver a requisitos: documentar el nuevo RF, evaluar el impacto en el modelo de datos y en las pantallas, y liberar una nueva version (1.1) con su aprobacion; no es un proyecto nuevo mientras el cambio quepa en el producto existente."
            }
        ]
    },
    {
        "n": 3,
        "slug": "Metodologias tradicionales",
        "titulo": "Metodologias tradicionales",
        "subtitulo": "Cascada y modelo en V: cuando el plano se firma antes de levantar el muro",
        "herramienta": "draw.io · Google Docs",
        "hito_pi": "Queda listo el indice del documento formal de diseño de VetCare y la matriz en V que amarra cada requisito con la prueba que lo va a verificar.",
        "entregable": "Un documento en Google Docs con el indice del ERS de VetCare, cuatro requisitos escritos en formato de ficha con version y linea base, la matriz en V (requisito - nivel de prueba - criterio de aceptacion) y un formato de solicitud de cambio diligenciado; mas el diagrama en V dibujado en draw.io y subido a ExamLab.",
        "demo": "El docente dibuja en draw.io el modelo en V de VetCare y traza en vivo la linea punteada que conecta el requisito RF-03 'buscar historial' con su prueba de aceptacion CP-ACEP-07.",
        "teoria": [
            "El modelo en cascada es el recorrido lineal llevado a su version formal: las fases van una detras de otra y cada una termina con un documento que alguien firma. Ese documento es la puerta de entrada a la siguiente fase; si no esta aprobado, no se avanza. Cuando el documento de requisitos se aprueba, se convierte en linea base, es decir, la version oficial contra la cual se va a medir todo lo demas. La idea de fondo es sencilla y muy usada en ingenieria civil: corregir un plano cuesta una borrada, corregir un muro construido cuesta demoler. Trasladado a VetCare: si Huellitas aprueba que la busqueda se hace por nombre de la mascota y por documento del propietario, ese acuerdo queda escrito, fechado y versionado, y a partir de ahi el equipo diseña con la tranquilidad de que el piso no se le va a mover.",
            "El modelo en V toma la cascada y la dobla en forma de letra V para dejar visible algo que la cascada esconde: cada fase de la izquierda tiene su prueba correspondiente a la derecha. Los requisitos se emparejan con las pruebas de aceptacion, el diseño de la arquitectura con las pruebas de integracion y el diseño detallado con las pruebas unitarias. La consecuencia practica es enorme: la prueba se diseña al mismo tiempo que el requisito, no al final. En VetCare, cuando se escribe el requisito RF-03 'la veterinaria busca la historia clinica por nombre o por documento', en ese mismo momento se escribe el caso de prueba CP-ACEP-07: con 5.000 fichas cargadas, escribir Rocky y obtener la ficha en menos de tres segundos y en maximo tres clics. Aqui aparecen dos palabras que hay que distinguir: verificar es preguntarse si construimos el sistema correctamente segun el documento; validar es preguntarse si construimos el sistema correcto para la clinica.",
            "Cuando SI tienen sentido estos modelos? Cuando los requisitos son estables y se conocen desde el principio, cuando el contrato es a precio fijo o viene de una licitacion publica y el alcance debe estar cerrado para poder cotizar, cuando el sistema es critico o esta regulado (equipos medicos, aviacion, banca, manejo de historia clinica con normativa de proteccion de datos) y cuando hay varios proveedores que necesitan un documento comun para poder trabajar en paralelo. En VetCare hay partes que caben perfecto en este enfoque: los datos basicos de un paciente casi no cambian, y si mañana la clinica conecta facturacion electronica, las reglas de esa parte vienen impuestas por la norma y no se negocian con el cliente. En esos casos escribir todo el detalle antes no es burocracia, es la unica forma de estimar y de cumplir.",
            "Cuando NO tienen sentido? Cuando el cliente no sabe lo que quiere hasta que lo ve, cuando el dominio es nuevo para el equipo, cuando el tiempo hasta la primera entrega visible es tan largo que el negocio cambia antes de recibir nada, y cuando integrar todo de un solo golpe al final concentra el riesgo en el peor momento. El costo de corregir crece de forma brutal a medida que se avanza: cambiar una frase en el documento de requisitos vale casi nada; cambiar la misma idea cuando ya hay diseño, codigo y datos migrados puede costar semanas. En VetCare esto se ve clarito con el tablero de metricas: la administradora dice 'quiero ver cuantos pacientes atendemos', pero cuando vea el primer grafico va a pedir por especie, por veterinario y por mes. Congelar ese requisito en la semana dos es congelar una suposicion.",
            "En el mundo tradicional la documentacion no acompaña al producto: en buena parte ES el producto contratado. Los entregables tipicos son la Especificacion de Requisitos de Software (ERS o SRS, con estructura tipo IEEE 830 / ISO 29148), el Documento de Diseño (SDD), la matriz de trazabilidad que muestra que cada requisito tiene diseño y prueba, y el acta de aprobacion. Cada documento tiene numero de version, fecha, autor y aprobador, y todo cambio entra por una solicitud formal donde se evalua impacto en alcance, tiempo y costo antes de aceptarla. Para el estudiante que solo cursa Seminario de Sistemas esto es una gran noticia: su entregable final -documento de diseño mas prototipo navegable- es exactamente el tipo de producto que se factura en un proyecto tradicional, y por eso su ruta es completa y no una version reducida del curso.",
            "Error tipico del docente que no domina el tema: presentar la cascada como un modelo torpe inventado por gente que no sabia trabajar, y de paso repetir que 'Royce la propuso' cuando en realidad el articulo de 1970 la describia y advertia sus riesgos. El segundo error es decir que el modelo en V es 'la cascada con un dibujito mas bonito': lo que agrega es la planeacion de las pruebas desde el inicio y la trazabilidad requisito-prueba, que es justamente lo que salva proyectos. El tercero, el mas costoso en el aula, es enseñar que congelar requisitos significa que ya no se admiten cambios: los cambios siempre llegan; lo que hace el enfoque tradicional es obligarlos a pasar por un control de cambios donde se dice cuanto cuestan y cuanto atrasan, en vez de aceptarlos de palabra en un pasillo."
        ],
        "taller": [
            "En Google Docs escriba el indice del ERS de VetCare con al menos estas secciones numeradas: 1. Proposito y alcance, 2. Glosario del dominio veterinario, 3. Requisitos funcionales, 4. Requisitos no funcionales, 5. Reglas de negocio, 6. Matriz de trazabilidad, 7. Control de versiones y aprobaciones.",
            "Escriba cuatro requisitos de VetCare en formato de ficha completa (ID, nombre, fuente, prioridad, estabilidad, descripcion, precondicion, criterio de aceptacion, version y estado); al menos uno debe ser no funcional y al menos uno debe declarar dependencia de otro.",
            "Construya la matriz en V en una tabla de cuatro columnas: Fase de la izquierda / Artefacto / Nivel de prueba emparejado / Caso de prueba de VetCare que lo verifica, y asegurese de que cada uno de sus cuatro requisitos aparezca con su codigo de prueba.",
            "En draw.io dibuje el modelo en V de VetCare con las fases de bajada y de subida, y trace lineas punteadas horizontales que unan cada fase con su nivel de prueba; rotule al menos dos de esas lineas con el ID del requisito y el ID del caso de prueba.",
            "Diligencie el formato de solicitud de cambio con este caso real: la clinica pide, ya aprobada la linea base, que la busqueda tambien funcione por numero de microchip; describa el requisito afectado, el impacto en diseño y pruebas, y la decision (aprobar, aplazar o rechazar) con su justificacion. Exporte todo a PDF y suba a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ si Huellitas exige aprobar todo el diseño antes de que Programacion II escriba una linea, este es exactamente el paquete de documentos que el equipo tendria que entregar y defender.",
            "La clase pasada quedo el mapa de fases; hoy se aprende a cerrar una fase de manera formal, con version, aprobacion y trazabilidad hacia las pruebas.",
            "Este es el enfoque que sostiene la ruta del estudiante que solo cursa Seminario: su producto final es un documento de diseño formal, que es lo que en la industria se contrata y se factura."
        ],
        "escenario": [
            "El equipo ya tiene una lista cruda de necesidades de Huellitas, pero escrita en frases sueltas tipo 'que sea rapido' y 'que no se pierdan las fichas', sin ID, sin version y sin quien lo pidio.",
            "La administradora de la clinica avisa que solo dispone de dos reuniones en todo el semestre, asi que no habra a quien preguntarle cada semana.",
            "Nadie ha escrito todavia una sola prueba, y la idea instalada en el grupo es que las pruebas se piensan al final, cuando ya haya algo que probar."
        ],
        "criterios": [
            "Cada requisito tiene ID unico, fuente identificada, version, estado y un criterio de aceptacion medible (con numero, tiempo o cantidad), no una opinion.",
            "La matriz en V empareja cada fase de la izquierda con su nivel de prueba a la derecha y no deja ningun requisito sin su caso de prueba asociado.",
            "El diagrama en draw.io muestra las dos ramas de la V y al menos dos lineas de trazabilidad rotuladas con IDs reales de VetCare.",
            "La solicitud de cambio identifica el requisito afectado, el impacto en diseño y pruebas y una decision justificada, no un simple 'si, se agrega'."
        ],
        "pistas": [
            "Su criterio de aceptacion se puede medir con un cronometro, un contador o un si/no, o depende de que la veterinaria este de buen genio ese dia?",
            "Si mañana entra un estudiante nuevo al equipo, podria saber solo leyendo el documento quien pidio cada requisito y en que version se aprobo?",
            "Hay algun requisito en su lista que no tenga ninguna prueba asociada? Si lo hay, como pensaba demostrarle a la clinica que ese requisito quedo cumplido?"
        ],
        "solucion_pasos": [
            "Indice del ERS resuelto: 1. Proposito y alcance (VetCare digitaliza el registro de pacientes, consultas e historia clinica de la clinica Huellitas; queda fuera del alcance la facturacion y el inventario de medicamentos). 2. Glosario (paciente = animal atendido; propietario = persona responsable; ficha = historia clinica del paciente; consulta = atencion medica registrada). 3. Requisitos funcionales RF-01 a RF-12. 4. Requisitos no funcionales RNF-01 a RNF-05. 5. Reglas de negocio (RN-01 un paciente pertenece a un unico propietario; RN-02 no se elimina una consulta, se anula con motivo). 6. Matriz de trazabilidad. 7. Control de versiones y aprobaciones.",
            "Requisitos resueltos en ficha: RF-01 Registrar paciente, fuente auxiliar de recepcion, prioridad alta, estabilidad alta, criterio de aceptacion: se guarda con nombre, especie, raza, fecha de nacimiento y propietario, y el sistema rechaza el registro si falta el propietario. RF-03 Buscar historial, fuente Dra. Rios, criterio: con 5.000 fichas el resultado aparece en menos de 3 segundos y en maximo 3 clics. RF-08 Anular consulta con motivo, depende de RF-02. RNF-02 Disponibilidad: el sistema opera en horario de atencion de 7:00 a 19:00 con caida maxima de 30 minutos al mes. Todos en version 1.0, estado Aprobado, linea base con fecha.",
            "Matriz en V resuelta: Requisitos / ERS aprobado / Pruebas de aceptacion / CP-ACEP-07 verifica RF-03 y CP-ACEP-02 verifica RF-01. Diseño de arquitectura / Diagrama de componentes y modelo de datos / Pruebas de integracion / CP-INT-03 verifica que el modulo de consultas guarde contra la ficha correcta. Diseño detallado / Diagrama de clases y contratos de metodos / Pruebas unitarias / CP-UNI-11 verifica la regla RN-01. Construccion (Programacion II) / Modulo ejecutable / se prueba de abajo hacia arriba.",
            "Diagrama en V resuelto en draw.io: rama izquierda descendente con Requisitos, Diseño de arquitectura, Diseño detallado y en el vertice Construccion; rama derecha ascendente con Pruebas unitarias, Pruebas de integracion y Pruebas de aceptacion. Lineas punteadas horizontales: Requisitos <--> Pruebas de aceptacion rotulada 'RF-03 <-> CP-ACEP-07'; Diseño detallado <--> Pruebas unitarias rotulada 'RN-01 <-> CP-UNI-11'. Nota al margen: la prueba se escribe cuando se escribe el requisito, no al final.",
            "Solicitud de cambio resuelta: SC-004, solicitada por la administradora, descripcion 'buscar tambien por numero de microchip'. Requisito afectado RF-03 (pasa a version 1.1). Impacto: el modelo de datos requiere el campo microchip en la entidad Paciente, el mockup de busqueda necesita un filtro adicional, y CP-ACEP-07 debe ampliarse con un tercer escenario. Estimacion: 6 horas de rediseño de planos. Decision: aprobada con nueva linea base fechada, porque el cambio se detecto antes de construir; si hubiera llegado despues de la construccion, se habria aplazado a la version 1.1 del producto."
        ],
        "solucion_rubrica": [
            "Indice del ERS completo y con glosario del dominio veterinario (2)",
            "Cuatro requisitos en ficha con ID, version, estado y criterio de aceptacion medible (3)",
            "Matriz en V con todos los requisitos emparejados a su nivel de prueba y codigo de caso (3)",
            "Solicitud de cambio con impacto y decision justificada (2)"
        ],
        "solucion_errores": [
            "Escribir criterios de aceptacion no medibles como 'la busqueda debe ser rapida' o 'la pantalla debe ser amigable', que nadie puede aprobar ni rechazar objetivamente.",
            "Dibujar la V con las mismas fases en los dos lados (requisitos abajo y requisitos arriba), perdiendo el sentido del modelo, que es emparejar cada fase con su NIVEL de prueba.",
            "Poner requisitos sin fuente ni version y luego cambiarlos en el documento sin dejar rastro, con lo cual la linea base deja de existir y ya no se puede demostrar que fue lo acordado."
        ],
        "codigo_slide_titulo": "Ficha formal de requisito de VetCare (asi se ve un requisito con linea base)",
        "codigo_slide_lineas": [
            "ID: RF-03            Version: 1.2      Estado: Aprobado (linea base 27/08)",
            "Nombre: Buscar la historia clinica de un paciente",
            "Fuente: Dra. Marcela Rios, medica veterinaria de Huellitas",
            "Prioridad: Alta      Estabilidad: Alta      Modulo: Historia clinica",
            "Descripcion: El sistema debe permitir buscar la historia clinica de un",
            "  paciente por nombre de la mascota, por documento del propietario o por",
            "  codigo de ficha, mostrando las ultimas tres consultas registradas.",
            "Precondicion: el paciente esta registrado y el usuario tiene rol Veterinario.",
            "Criterio de aceptacion: con 5.000 fichas cargadas el resultado se muestra",
            "  en menos de 3 segundos y en maximo 3 clics desde el tablero principal.",
            "Depende de: RF-01 (registrar paciente), RNF-02 (tiempo de respuesta)",
            "Verificado por: CP-ACEP-07 (prueba de aceptacion)",
            "Historial: v1.1 se agrega busqueda por documento (SC-002)",
            "           v1.2 se agrega busqueda por microchip (SC-004, aprobada)"
        ],
        "codigo_slide_caption": "En el enfoque tradicional un requisito no es una frase suelta: es una ficha con ID, version, criterio medible y la prueba que lo verifica.",
        "artefacto_archivo": "ERS-y-Matriz-en-V-VetCare.md",
        "artefacto_contenido": "# ERS + Matriz en V - Proyecto Integrador VetCare\n**Clinica Veterinaria Huellitas** | Enfoque tradicional (cascada / modelo en V)\nEstudiante: ______________  Version del documento: 1.0  Fecha: __________\n\n---\n\n## 1. Indice del ERS (estructura minima exigida)\n\n1. Proposito y alcance (que entra y que NO entra)\n2. Glosario del dominio veterinario\n3. Requisitos funcionales (RF-01 ...)\n4. Requisitos no funcionales (RNF-01 ...)\n5. Reglas de negocio (RN-01 ...)\n6. Matriz de trazabilidad requisito - diseno - prueba\n7. Control de versiones y aprobaciones\n\n---\n\n## 2. Ficha de requisito (copie una por cada requisito)\n\n```\nID: RF-__            Version: ___     Estado: [Borrador|Revision|Aprobado]\nNombre:\nFuente (quien lo pidio):\nPrioridad: [Alta|Media|Baja]     Estabilidad: [Alta|Media|Baja]\nDescripcion:\nPrecondicion:\nCriterio de aceptacion (MEDIBLE: tiempo, cantidad, si/no):\nDepende de:\nVerificado por (ID del caso de prueba):\nHistorial de cambios:\n```\n\n---\n\n## 3. Matriz en V (trazabilidad requisito <-> prueba)\n\n| Fase (bajada) | Artefacto que produce | Nivel de prueba (subida) | Caso de prueba VetCare | Requisito que verifica |\n|---|---|---|---|---|\n| Requisitos | ERS aprobado | Pruebas de aceptacion | CP-ACEP-07 | RF-03 |\n| Diseno de arquitectura | Componentes + modelo de datos | Pruebas de integracion | CP-INT-03 | RF-02 |\n| Diseno detallado | Diagrama de clases | Pruebas unitarias | CP-UNI-11 | RN-01 |\n| Construccion (Prog. II) | Modulo ejecutable | -- | -- | -- |\n\n**Regla de oro:** ningun requisito puede quedar sin fila. Si no tiene prueba, no se puede demostrar cumplido.\n\n---\n\n## 4. Formato de solicitud de cambio (control de cambios)\n\n| Campo | Contenido |\n|---|---|\n| Codigo | SC-___ |\n| Fecha / solicitante | |\n| Descripcion del cambio | |\n| Requisito(s) afectado(s) | |\n| Impacto en diseno | |\n| Impacto en pruebas | |\n| Esfuerzo estimado (horas de rediseno) | |\n| Decision | [ ] Aprobada  [ ] Aplazada  [ ] Rechazada |\n| Justificacion de la decision | |\n| Nueva linea base | version ___ del ___ |\n\n---\n\n## 5. Control de versiones y aprobaciones\n\n| Version | Fecha | Cambio | Autor | Aprobado por |\n|---|---|---|---|---|\n| 1.0 | | Version inicial | | Administradora de Huellitas |\n\n---\n\n## 6. Checklist antes de subir a ExamLab\n\n- [ ] Todos los requisitos tienen ID, version, estado y criterio MEDIBLE.\n- [ ] Ningun requisito quedo sin caso de prueba en la matriz.\n- [ ] El diagrama en V muestra las dos ramas y dos lineas de trazabilidad rotuladas.\n- [ ] La solicitud de cambio esta diligenciada con impacto y decision justificada.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "En el modelo en V, con que nivel de prueba se empareja la fase de requisitos?",
                "opciones": [
                    "A) Pruebas unitarias",
                    "B) Pruebas de integracion",
                    "C) Pruebas de aceptacion",
                    "D) Pruebas de humo"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual de estos escenarios justifica MEJOR usar un enfoque tipo cascada en una parte de VetCare?",
                "opciones": [
                    "A) El tablero de metricas, porque la clinica nunca ha visto uno",
                    "B) El modulo de facturacion electronica, con reglas fijas impuestas por la norma y contrato cerrado",
                    "C) Los mockups, porque cambian mucho con la retroalimentacion",
                    "D) Cualquier modulo, porque cascada siempre es mas seguro"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Que significa que el documento de requisitos de VetCare quede como linea base?",
                "opciones": [
                    "A) Que ya no se puede modificar nunca mas bajo ninguna circunstancia",
                    "B) Que es la version oficial y fechada contra la cual se mide todo lo demas, y los cambios entran por control de cambios",
                    "C) Que se subio a ExamLab",
                    "D) Que la clinica lo leyo aunque no lo haya aprobado"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual de estos criterios de aceptacion sirve en un enfoque tradicional?",
                "opciones": [
                    "A) La busqueda debe ser rapida y comoda",
                    "B) La pantalla debe verse profesional",
                    "C) Con 5.000 fichas cargadas el resultado se muestra en menos de 3 segundos y en maximo 3 clics",
                    "D) El sistema debe gustarle a la veterinaria"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Congelar los requisitos en un proyecto en cascada significa que ya no se admite ningun cambio durante el proyecto.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "El aporte principal del modelo en V frente a la cascada es emparejar cada fase de desarrollo con un nivel de prueba y planear esas pruebas desde el inicio.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Si Huellitas exigiera aprobar TODO el diseño de VetCare antes de que se programe una sola linea, mencione un beneficio concreto y un riesgo concreto de esa decision.",
                "clave": "Beneficio: el alcance queda cerrado y se puede estimar costo y tiempo con precision, ademas el equipo de Programacion II recibe planos completos y estables para construir sin ambiguedades. Riesgo: la clinica no sabe que metricas quiere hasta ver el primer tablero, asi que se congelaria una suposicion y el cambio llegaria tarde, cuando corregirlo ya cuesta rediseno, recodificacion y repruebas."
            },
            {
                "tipo": "abierta",
                "q": "Explique la diferencia entre verificacion y validacion usando un ejemplo de VetCare.",
                "clave": "Verificar es comprobar que se construyo segun el documento: la pantalla de busqueda tiene los tres campos que decia el RF-03. Validar es comprobar que se construyo lo correcto para el cliente: la veterinaria usa la pantalla y confirma que asi si encuentra la ficha en la consulta real. Se puede verificar bien un requisito equivocado."
            }
        ]
    },
    {
        "n": 4,
        "slug": "Metodologias agiles",
        "titulo": "Metodologias agiles",
        "subtitulo": "Iterar e incrementar sin dejar de documentar",
        "herramienta": "draw.io · Excalidraw · Google Docs",
        "hito_pi": "Queda listo el backlog priorizado de VetCare repartido en sprints del semestre, con las primeras historias de usuario escritas con criterios de aceptacion.",
        "entregable": "Un tablero en draw.io o Excalidraw con el Product Backlog priorizado de VetCare y las columnas de flujo con limite de trabajo en curso, mas un documento con el plan de tres sprints (objetivo y entregable de diseño de cada uno), la Definicion de Terminado y tres historias de usuario con criterios en formato Dado/Cuando/Entonces.",
        "demo": "El docente arma en pantalla el tablero de VetCare, arrastra una tarjeta de 'Por hacer' a 'En revision del cliente' y muestra que pasa cuando se rompe el limite de trabajo en curso.",
        "teoria": [
            "El manifiesto agil se firmo en 2001 por diecisiete personas cansadas de proyectos que entregaban documentos perfectos y sistemas inservibles. Tiene cuatro valores y la clave esta en la palabra que los une: 'sobre'. Individuos e interacciones SOBRE procesos y herramientas; software funcionando SOBRE documentacion exhaustiva; colaboracion con el cliente SOBRE negociacion contractual; respuesta ante el cambio SOBRE seguir un plan. Dice sobre, no 'en vez de': lo de la derecha sigue teniendo valor, solo que lo de la izquierda tiene mas. Ademas hay doce principios, y tres son muy utiles aqui: entregar valor pronto y con frecuencia, aceptar el cambio incluso tarde, y mantener un ritmo sostenible. En VetCare esto se traduce en algo muy concreto: es mejor mostrarle a Huellitas un mockup imperfecto de la ficha en la semana tres que un documento de ochenta paginas en la semana quince.",
            "Scrum es un marco de trabajo, no una metodologia completa: define lo minimo y deja que cada equipo llene el resto. Tiene tres roles: el Product Owner, que decide QUE se hace y en que orden, y es el dueño del Product Backlog; el Scrum Master, que facilita, protege al equipo y quita impedimentos, y que no es el jefe; y el equipo de desarrollo, que decide COMO hacerlo y se autoorganiza. Tiene cinco eventos: el Sprint, que es el contenedor de duracion fija (una a cuatro semanas), la Planificacion, la Reunion diaria de quince minutos para sincronizarse, la Revision donde se le muestra el incremento al cliente, y la Retrospectiva donde se mejora la forma de trabajar. Y tiene tres artefactos: Product Backlog, Sprint Backlog e Incremento, este ultimo gobernado por la Definicion de Terminado. En VetCare el docente actua como vocero de Huellitas en el rol de Product Owner, y cada estudiante -o cada equipo, si el docente lo autoriza- hace de equipo de desarrollo que se compromete con un objetivo de sprint.",
            "Kanban viene de otra tradicion y su promesa es distinta: no impone iteraciones ni roles, sino que hace visible el flujo del trabajo. Sus practicas centrales son visualizar el trabajo en un tablero, limitar el trabajo en curso, gestionar el flujo detectando donde se acumulan las tarjetas, hacer explicitas las politicas de cada columna y mejorar de forma continua. El limite de trabajo en curso es la parte que mas cuesta y la que mas sirve: si el equipo pone limite dos en la columna 'Modelando', nadie puede empezar una tercera tarea sin terminar alguna. En VetCare el tablero seria Por hacer / Modelando / En revision del cliente / Aprobado, y la politica de la ultima columna podria ser 'solo pasa a Aprobado si tiene diagrama, mockup y visto bueno de la clinica'. El estudiante que abre cinco diagramas al tiempo y no termina ninguno es exactamente el problema que el limite de trabajo en curso resuelve.",
            "Hay dos palabras que se usan como sinonimos y significan cosas distintas: iteracion e incremento. Incremento es agregar un pedazo nuevo y utilizable al sistema; iteracion es volver sobre algo que ya existe y mejorarlo con base en la retroalimentacion. Agil hace las dos cosas al mismo tiempo. En VetCare el incremento 1 es el mockup de la ficha del paciente; cuando la veterinaria lo mira y dice 'me falta el campo de alergias y la foto de la mascota', y el equipo produce la version 2 de ese mismo mockup, eso es iteracion. Y aqui aparece una regla practica que salva proyectos: cada entrega debe ser una rebanada vertical, algo que el cliente pueda ver y opinar, no una capa horizontal invisible. Entregar 'todas las tablas de la base de datos' no es un incremento util para Huellitas; entregar 'registrar y consultar una ficha completa de principio a fin' si lo es.",
            "Agil no significa trabajar sin documentacion, y este es el malentendido que mas daño hace. El manifiesto dice software funcionando sobre documentacion exhaustiva: lo que se rechaza es el documento inflado que nadie lee, no el documento util. Un equipo agil documenta historias de usuario con criterios de aceptacion, la Definicion de Terminado, las decisiones de arquitectura, el diccionario de datos y los diagramas que hagan falta, pero los escribe justo a tiempo y los mantiene vivos. Para nuestro Proyecto Integrador esto es central: en Seminario de Sistemas el entregable ES documentacion de diseño, y aun asi el trabajo puede ser perfectamente agil, porque se produce por incrementos, se revisa con el cliente y se corrige. El estudiante que solo cursa esta materia trabaja con sprints igual que los demas: sus incrementos son mockups, casos de uso y diccionario de datos, y cierra con un prototipo navegable que se puede recorrer y criticar.",
            "Error tipico del docente que no domina el tema: enseñar que agil es 'sin plan, sin documentos y sin fechas', cuando en realidad agil planifica mas seguido, solo que en horizontes cortos. El segundo error es volver la reunion diaria un informe de avance al profesor, con cada estudiante rindiendo cuentas: la diaria es del equipo para el equipo, quince minutos, para detectar bloqueos, no para calificar. El tercero es partir el semestre en sprint uno de analisis, sprint dos de diseño y sprint tres de construccion, y creer que eso es Scrum: eso es una cascada disfrazada con vocabulario nuevo, porque ningun sprint termina en algo que el cliente pueda ver y opinar. Se agrega un cuarto, muy frecuente: confundir al Scrum Master con el jefe de proyecto, o medir productividad por velocidad, cuando la velocidad solo sirve para que el propio equipo planee."
        ],
        "taller": [
            "En Google Docs escriba el Product Backlog de VetCare con al menos ocho items redactados como historias de usuario cortas, cada uno con prioridad (Alta/Media/Baja) y una justificacion de valor para Huellitas en una linea.",
            "Priorice el backlog en orden de arriba hacia abajo y explique por escrito, en dos renglones, por que el primer item es el primero (pista: resuelve uno de los tres dolores de la clinica).",
            "Escriba tres historias completas con criterios de aceptacion en formato Dado/Cuando/Entonces, y asegurese de que cada historia tenga al menos un escenario alternativo o de error, no solo el camino feliz.",
            "Redacte la Definicion de Terminado para artefactos de diseño (por ejemplo: tiene diagrama en draw.io, tiene mockup, esta revisado por un compañero y tiene el visto bueno del cliente) y escribala en la cabecera del tablero.",
            "En draw.io o Excalidraw arme el tablero con las columnas Por hacer / Modelando / En revision del cliente / Aprobado, ponga el limite de trabajo en curso en dos para las columnas del medio, distribuya las tarjetas en tres sprints con su objetivo y entregable de diseño, exporte a PDF y suba a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el semestre completo de VetCare se va a organizar como sprints, y lo que se defina hoy en el backlog es literalmente el orden en que se van a producir los planos.",
            "Ya vimos el enfoque tradicional y su documentacion formal; hoy se ve el otro extremo del espectro y se aprende a decidir cual parte de VetCare conviene tratar de cada forma.",
            "Aqui se aclara de una vez el malentendido mas costoso del curso: agil no es la excusa para no documentar, y en esta asignatura la documentacion de diseño es justamente el incremento entregable."
        ],
        "escenario": [
            "El equipo tiene requisitos escritos y un mapa de fases, pero no tiene ningun orden de trabajo: todos quieren empezar por la pantalla que les parece mas bonita.",
            "La administradora de Huellitas puede dar retroalimentacion corta cada dos o tres semanas, pero no puede sentarse a leer un documento de ochenta paginas.",
            "En el grupo circula la idea de que agil significa no escribir nada y que 'ya lo iremos viendo sobre la marcha'."
        ],
        "criterios": [
            "El backlog esta priorizado con un orden explicito y cada item tiene una justificacion de valor para la clinica, no un orden arbitrario.",
            "Las tres historias siguen la estructura Como / quiero / para y cada una tiene al menos dos escenarios en Dado/Cuando/Entonces, incluido uno alternativo o de error.",
            "Cada sprint del plan termina en un incremento que la clinica podria ver y opinar (mockup, prototipo, diagrama revisado), no en trabajo interno invisible.",
            "El tablero declara la Definicion de Terminado y el limite de trabajo en curso, y ninguna columna del medio tiene mas tarjetas que su limite."
        ],
        "pistas": [
            "Si su sprint 1 se llama 'analisis' y el sprint 2 'diseño', que le va a mostrar a la veterinaria al terminar el sprint 1 que ella pueda entender y criticar?",
            "Sus criterios de aceptacion describen solo el camino feliz? Que pasa si la mascota no existe, si el nombre esta repetido o si la conexion se cae?",
            "Su Definicion de Terminado se puede verificar mirando el tablero, o incluye frases como 'que quede bien hecho' que nadie puede comprobar?"
        ],
        "solucion_pasos": [
            "Backlog priorizado resuelto (primeros cinco): 1) Registrar paciente con sus datos basicos y su propietario, prioridad Alta, porque sin ficha digital se siguen extraviando las fichas de papel. 2) Buscar historial por nombre o documento, Alta, porque ataca directo el dolor de la busqueda lenta. 3) Registrar consulta con motivo, diagnostico y tratamiento, Alta. 4) Ver historia clinica completa del paciente, Media. 5) Reporte de consultas por mes y por especie, Media, porque es el dolor de las metricas pero solo tiene sentido cuando ya hay datos. Justificacion del primer item: sin registro de pacientes ninguna otra historia se puede usar, es la base de todo el flujo.",
            "Historia resuelta con criterios: 'Como veterinaria de Huellitas quiero buscar la historia clinica de una mascota por nombre o por documento del dueño para atender la consulta sin ir al archivador'. Escenario feliz: Dado que Rocky esta registrado con el dueño CC 1.144.556, Cuando escribo Rocky y presiono Enter, Entonces veo la ficha con nombre, especie, edad y las ultimas tres consultas en menos de 3 segundos. Escenario alternativo: Dado que escribo un nombre que no existe, Cuando presiono Enter, Entonces veo el mensaje 'No se encontro el paciente' y el boton 'Registrar nuevo'. Escenario de ambiguedad: Dado que hay tres mascotas llamadas Rocky, Cuando busco por ese nombre, Entonces veo una lista con nombre del propietario para poder distinguirlas.",
            "Definicion de Terminado resuelta para artefactos de diseño: 1) El diagrama esta hecho en draw.io y exportado a PDF. 2) Existe el mockup de la pantalla asociada en Figma o Penpot. 3) Los nombres de campos coinciden con el diccionario de datos. 4) Un compañero distinto al autor lo reviso y dejo comentario. 5) El cliente (docente en rol de Huellitas) dio visto bueno en la revision de sprint. Si falta uno solo de los cinco, la tarjeta NO pasa a Aprobado.",
            "Plan de sprints resuelto: Sprint 1 (tres semanas) objetivo 'que la clinica pueda ver como se registra y se consulta una ficha', entregable: casos de uso de registro y consulta mas mockup navegable de la ficha del paciente. Sprint 2 objetivo 'que la busqueda quede resuelta de punta a punta', entregable: historias con criterios, diagrama de clases del modulo de historia clinica y prototipo de busqueda. Sprint 3 objetivo 'que la clinica vea sus numeros', entregable: diccionario de datos completo, modelo entidad-relacion y mockup del tablero de metricas. Cada sprint cierra con revision frente al cliente y retrospectiva escrita de tres lineas.",
            "Tablero resuelto: columnas Por hacer / Modelando (limite 2) / En revision del cliente (limite 2) / Aprobado, con la Definicion de Terminado escrita en la cabecera. Al arrastrar la tercera tarjeta a Modelando el tablero queda en rojo y la politica dice: nadie empieza algo nuevo, se ayuda a terminar lo que esta atascado. En la retrospectiva del sprint 1 el equipo anota: 'las tarjetas se acumulan en revision del cliente porque solo pedimos retroalimentacion el ultimo dia; en el sprint 2 pedimos revision a mitad de sprint'."
        ],
        "solucion_rubrica": [
            "Product Backlog priorizado con justificacion de valor por item (2)",
            "Tres historias con estructura completa y escenarios Dado/Cuando/Entonces incluyendo casos alternativos (3)",
            "Plan de tres sprints con objetivo e incremento visible para el cliente en cada uno (3)",
            "Tablero con Definicion de Terminado explicita y limite de trabajo en curso respetado (2)"
        ],
        "solucion_errores": [
            "Organizar los sprints por fases (sprint 1 analisis, sprint 2 diseño, sprint 3 construccion), con lo cual ningun sprint termina en algo que la clinica pueda ver: es cascada con nombre nuevo.",
            "Escribir historias que en realidad son tareas tecnicas ('crear la tabla paciente', 'instalar la herramienta'), sin decir quien las necesita ni para que sirven al negocio.",
            "Dejar criterios de aceptacion solo con el camino feliz, sin definir que pasa cuando el paciente no existe, cuando hay nombres repetidos o cuando falta un dato obligatorio."
        ],
        "codigo_slide_titulo": "Historia de usuario de VetCare con criterios de aceptacion",
        "codigo_slide_lineas": [
            "HU-07  Buscar historia clinica",
            "  Como veterinaria de la clinica Huellitas",
            "  quiero buscar la historia clinica de una mascota por nombre o documento",
            "  para atender la consulta sin ir al archivador de papel.",
            "",
            "Criterios de aceptacion",
            "  Dado que la mascota Rocky esta registrada con el dueño CC 1.144.556",
            "  Cuando escribo Rocky en el buscador y presiono Enter",
            "  Entonces veo la ficha con especie, edad y las ultimas 3 consultas en <= 3 s",
            "",
            "  Dado que escribo un nombre que no existe en el sistema",
            "  Cuando presiono Enter",
            "  Entonces veo 'No se encontro el paciente' y el boton Registrar nuevo",
            "Terminado = caso de uso + mockup + revision de un compañero + visto bueno del cliente"
        ],
        "codigo_slide_caption": "La historia dice quien la necesita y para que; los criterios dicen como se demuestra que quedo lista, incluido el camino que sale mal.",
        "artefacto_archivo": "Backlog-y-Sprints-VetCare.md",
        "artefacto_contenido": "# Backlog agil y plan de sprints - Proyecto Integrador VetCare\n**Clinica Veterinaria Huellitas** | Estudiante: ______________\n\n> Agil NO es trabajar sin documentacion. Aqui el incremento de cada sprint ES un artefacto de diseno.\n\n---\n\n## 1. Product Backlog priorizado\n\n| # | Historia (Como / quiero / para) | Prioridad | Valor para Huellitas | Sprint |\n|---|---|---|---|---|\n| 1 | Como auxiliar quiero registrar un paciente con su propietario para no perder la ficha | Alta | Ataca el dolor de fichas extraviadas | 1 |\n| 2 | Como veterinaria quiero buscar la historia por nombre o documento para no ir al archivador | Alta | Ataca el dolor de busqueda lenta | 1 |\n| 3 | Como veterinaria quiero registrar la consulta con diagnostico y tratamiento | Alta | Historia clinica completa | 2 |\n| 4 | Como veterinaria quiero ver la historia clinica completa del paciente | Media | Contexto para la atencion | 2 |\n| 5 | Como administradora quiero ver consultas por mes y por especie | Media | Ataca el dolor de cero metricas | 3 |\n| 6 | | | | |\n| 7 | | | | |\n| 8 | | | | |\n\n---\n\n## 2. Plantilla de historia con criterios de aceptacion\n\n```\nHU-__  Titulo\n  Como  <rol en la clinica>\n  quiero <lo que necesita hacer>\n  para  <el beneficio de negocio>\n\nCriterio 1 (camino feliz)\n  Dado que ...\n  Cuando ...\n  Entonces ...\n\nCriterio 2 (camino alternativo o de error)\n  Dado que ...\n  Cuando ...\n  Entonces ...\n```\nRegla: si no hay al menos un criterio de error, la historia esta incompleta.\n\n---\n\n## 3. Definicion de Terminado (DoD)\n\nUna tarjeta pasa a **Aprobado** solo si cumple TODO:\n\n- [ ] Diagrama hecho en draw.io y exportado a PDF\n- [ ] Mockup de la pantalla asociada (Figma o Penpot)\n- [ ] Nombres de campos coinciden con el diccionario de datos\n- [ ] Revisado por un companero distinto al autor\n- [ ] Visto bueno del cliente en la revision de sprint\n\n---\n\n## 4. Plan de sprints del semestre\n\n| Sprint | Objetivo (en una frase, en lenguaje de la clinica) | Incremento que la clinica puede VER | Fecha de revision |\n|---|---|---|---|\n| 1 | | Mockup navegable de la ficha del paciente | |\n| 2 | | Prototipo de busqueda + diagrama de clases | |\n| 3 | | Diccionario de datos + mockup del tablero de metricas | |\n\n**Prohibido:** sprint 1 = analisis, sprint 2 = diseno, sprint 3 = construccion. Eso es cascada disfrazada.\n\n---\n\n## 5. Tablero de flujo (Kanban)\n\n```\n| Por hacer | Modelando (WIP 2) | En revision del cliente (WIP 2) | Aprobado |\n|-----------|-------------------|---------------------------------|----------|\n|           |                   |                                 |          |\n```\nPolitica de columna: nadie empieza una tarjeta nueva si la columna ya llego a su limite; se ayuda a destrabar la que esta atascada.\n\n---\n\n## 6. Retrospectiva (3 lineas al cierre de cada sprint)\n\n- Que funciono: ______________________________________\n- Que no funciono: ___________________________________\n- Que cambiamos el proximo sprint: ___________________\n\n---\n\n## 7. Checklist antes de subir a ExamLab\n\n- [ ] Backlog priorizado con justificacion de valor.\n- [ ] Tres historias con criterios Dado/Cuando/Entonces y camino de error.\n- [ ] Cada sprint termina en algo visible para el cliente.\n- [ ] El tablero declara DoD y limites de trabajo en curso.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cual de estos es un valor del manifiesto agil, redactado correctamente?",
                "opciones": [
                    "A) Software funcionando EN VEZ DE documentacion",
                    "B) Software funcionando SOBRE documentacion exhaustiva",
                    "C) Documentacion exhaustiva SOBRE software funcionando",
                    "D) Herramientas SOBRE individuos e interacciones"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "En Scrum, quien decide el orden de prioridad del Product Backlog?",
                "opciones": [
                    "A) El Scrum Master",
                    "B) El equipo de desarrollo por votacion",
                    "C) El Product Owner",
                    "D) El cliente final directamente en la reunion diaria"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual es la practica central de Kanban que evita que el equipo tenga cinco diagramas empezados y ninguno terminado?",
                "opciones": [
                    "A) La reunion diaria de 15 minutos",
                    "B) Limitar el trabajo en curso (WIP) por columna",
                    "C) Estimar en puntos de historia",
                    "D) Hacer sprints de dos semanas"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "En que evento de Scrum el equipo revisa e intenta mejorar su propia forma de trabajar?",
                "opciones": [
                    "A) Sprint Planning",
                    "B) Daily",
                    "C) Sprint Review",
                    "D) Retrospectiva"
                ],
                "clave": "D"
            },
            {
                "tipo": "vf",
                "q": "Trabajar de forma agil significa no producir documentacion.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "La reunion diaria es una sincronizacion corta del equipo para detectar bloqueos, no un informe de avance para el jefe o el docente.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Explique la diferencia entre iteracion e incremento con un ejemplo concreto de VetCare.",
                "clave": "Incremento es agregar un pedazo nuevo y utilizable: entregar el mockup de la ficha del paciente que antes no existia. Iteracion es volver sobre lo que ya existe y mejorarlo con la retroalimentacion: la veterinaria pide campo de alergias y foto de la mascota, y el equipo produce la version 2 del mismo mockup. Agil hace las dos cosas."
            },
            {
                "tipo": "abierta",
                "q": "Por que organizar el semestre como sprint 1 = analisis, sprint 2 = diseño y sprint 3 = construccion NO es trabajo agil? Proponga una organizacion correcta para VetCare.",
                "clave": "Porque ningun sprint termina en algo que la clinica pueda ver y opinar: son fases de cascada con nombre nuevo y la retroalimentacion sigue llegando al final. La organizacion correcta reparte por rebanadas verticales de valor: sprint 1 ficha del paciente completa (caso de uso + mockup navegable), sprint 2 busqueda e historia clinica de punta a punta, sprint 3 reportes y metricas; cada sprint cierra con revision frente al cliente y retrospectiva."
            }
        ]
    },
    {
        "n": 5,
        "slug": "Parcial 1",
        "titulo": "Parcial 1",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    },
    {
        "n": 6,
        "slug": "Requerimientos de software",
        "titulo": "Requerimientos de software",
        "subtitulo": "De la frase del veterinario al requisito verificable",
        "herramienta": "Google Docs · draw.io",
        "hito_pi": "Queda listo el catalogo de requisitos de VetCare: 8 RF y 4 RNF con criterio de verificacion y prioridad MoSCoW.",
        "entregable": "Documento de requisitos de VetCare en PDF, con minimo 8 RF, 4 RNF cuantificados, priorizacion MoSCoW y matriz de trazabilidad, subido a ExamLab.",
        "demo": "El docente toma en vivo dos frases crudas de la entrevista al Dr. Ramirez y las convierte, frente al grupo, en un RF y un RNF usando la plantilla.",
        "teoria": [
            "Un requerimiento no es lo que el cliente dijo, es lo que el sistema debe hacer para que el problema del cliente desaparezca; entre esas dos cosas hay un trabajo de traduccion que se llama elicitacion, palabra que viene de sacar a la luz algo que estaba implicito. Las tres tecnicas que caben en este curso son baratas y no necesitan software especializado: la entrevista, donde se arranca con preguntas abiertas (cuenteme como es un dia normal en la clinica) y solo al final se cierran con preguntas de si o no; la observacion, donde uno se para media hora en la recepcion un sabado y cronometra cuanto tarda la auxiliar en encontrar una carpeta; y el prototipo desechable, donde uno dibuja una pantalla fea a mano o en draw.io y la pone frente al veterinario, porque la gente no sabe decir lo que quiere pero sabe perfectamente decir lo que NO quiere cuando lo ve. En VetCare la entrevista al Dr. Ramirez dejo cinco frases crudas: que las fichas no se pierdan, ver de una lo que le han hecho antes al paciente, que la auxiliar agende sin llamarlo, que el sistema sea rapido, y saber cuantas consultas se hicieron en el mes. Ninguna de esas cinco frases es todavia un requisito: son necesidades, y confundirlas es el primer error del analista novato.",
            "Con las necesidades en la mano se separan dos familias. Un requisito funcional (RF) describe una capacidad observable del sistema, algo que alguien puede hacer con el, y se escribe con la plantilla el sistema debe permitir a <actor> <accion> <objeto> [bajo <condicion>]; el truco practico es que si al leerlo usted puede imaginar un boton, un formulario o una pantalla, es funcional. Un requisito no funcional (RNF) no describe QUE hace el sistema sino QUE TAN BIEN lo hace, y se agrupa en categorias conocidas: desempeno, seguridad y control de acceso, usabilidad, disponibilidad, respaldo, mantenibilidad y portabilidad. En VetCare, la frase que la auxiliar pueda agendar sin llamarme se convierte en dos cosas distintas al mismo tiempo: RF-05 el sistema debe permitir a la auxiliar registrar una cita seleccionando mascota, veterinario, fecha y hora; y RNF-02 el sistema debe manejar dos perfiles de acceso, auxiliar y veterinario, donde la auxiliar puede crear citas pero no puede editar ni ver el diagnostico clinico. Esa separacion importa porque el RF se prueba haciendo clic y el RNF se prueba midiendo o intentando lo prohibido.",
            "La regla de oro del oficio es dura y se enuncia asi: si no se puede verificar, no es un requisito, es un deseo. Hay una lista negra de palabras que suenan a compromiso pero no comprometen a nada: rapido, amigable, facil, intuitivo, robusto, moderno, optimo, eficiente, seguro. Cada vez que aparece una de esas palabras hay que preguntar cuanto, en que condiciones y como lo mediriamos delante del cliente. La frase 4 del Dr. Ramirez, el sistema tiene que ser rapido, no se puede calificar ni aprobar ni rechazar; convertida queda RNF-01: la busqueda de historial por documento del dueno debe devolver resultados en maximo 3 segundos, con 5.000 fichas cargadas y 10 usuarios trabajando al mismo tiempo. Ahora si existe una prueba: se carga la base de ejemplo, se cronometra y el requisito pasa o no pasa. Lo mismo con la frase 1: que las fichas no se pierdan no es requisito, pero RF-01 registrar una ficha con codigo unico e irrepetible mas RNF-04 respaldo automatico diario con restauracion probada una vez al mes, si lo son.",
            "Priorizar no es ordenar por gusto sino decidir con el cliente que pasa si algo no esta el dia de la entrega, y para eso se usa MoSCoW: Must es lo que sin ello el sistema no sirve y no se sale a produccion; Should es importante pero existe un plan B manual mientras tanto; Could es lo que se hace si sobra tiempo; y Won't es lo que se declara explicitamente fuera de ESTA version, que es la categoria mas valiosa de las cuatro porque es la unica que le pone freno al alcance infinito. La regla practica es que los Must no deberian superar el 60% del esfuerzo estimado, porque si todo es Must nada es Must. En VetCare: registrar dueno y mascota, consultar historial y agendar cita son Must, porque atacan los tres dolores de Huellitas; el reporte mensual de consultas es Should, porque hoy el Dr. Ramirez lo hace contando a mano y puede sobrevivir un mes mas; el envio de recordatorios por WhatsApp y la facturacion electronica son Won't de esta version, y se escriben en el documento con esa etiqueta para que nadie los reclame despues como si hubieran sido prometidos.",
            "El ultimo pedazo es la trazabilidad, que es poder seguir cada requisito hacia atras y hacia adelante. Hacia atras: de donde salio este RF, quien lo pidio, en que frase de la entrevista, en que fecha; asi cuando alguien pregunte y esto por que esta aqui hay respuesta y no cara de sorpresa. Hacia adelante: en que caso de uso se desarrolla, en que pantalla del mockup se ve, en que clase del diagrama UML aparece y con que prueba se acepta. Se lleva en una matriz simple de cuatro columnas y se actualiza cada clase. Esto no es burocracia: es lo que permite que cuando el cliente cambie de opinion, usted sepa en dos minutos que se rompe y cuanto cuesta; y en el Proyecto Integrador es lo que hace posible que el companero que solo cursa Programacion II reciba estos planos y sepa exactamente que implementar y por que, sin tener que volver a entrevistar al veterinario. Quien solo cursa Seminario cierra el ciclo distinto pero completo: su matriz termina en el prototipo navegable y en el documento de diseno, y eso es una entrega profesional valida, no una version reducida.",
            "Error tipico del docente que no domina el tema: creer que levantar requisitos es transcribir lo que dijo el cliente y calificar la lista por cantidad de vinetas. El docente que no domina esto acepta como RNF valido el sistema debe ser amigable e intuitivo, deja pasar RF que en realidad son tres requisitos pegados con la palabra y (el sistema debe registrar mascotas y generar reportes y enviar correos), no exige criterio de verificacion porque le parece que alarga el documento, y pone MoSCoW como adorno permitiendo que el 90% de la lista quede en Must. El resultado es un documento que se ve gordo y bonito y que en la siguiente clase no sirve para dibujar ni un caso de uso. El antidoto es sencillo y hay que aplicarlo en voz alta requisito por requisito: con que prueba concreta sabriamos, delante del Dr. Ramirez, que esto se cumplio. Si el estudiante no lo responde en una sola frase con un numero o un si/no, el requisito se devuelve; y si el requisito tiene una y en la mitad, se parte en dos antes de seguir."
        ],
        "taller": [
            "Paso 1: copie en la plantilla las cinco frases crudas de la entrevista al Dr. Ramirez y marque cada una como NECESIDAD, anotando al lado quien la dijo y en que contexto; esa columna es el origen y no se puede dejar vacia.",
            "Paso 2: traduzca las necesidades a requisitos funcionales usando la plantilla el sistema debe permitir a <actor> <accion> <objeto>, hasta llegar a minimo 8 RF numerados de RF-01 a RF-08; ningun RF puede contener la palabra y uniendo dos capacidades distintas.",
            "Paso 3: derive 4 RNF, uno por categoria (desempeno, control de acceso, usabilidad y respaldo), y escriba en cada uno al menos un numero: segundos, cantidad de registros, frecuencia o porcentaje.",
            "Paso 4: asigne prioridad MoSCoW a los 12 requisitos, verifique que los Must no pasen de seis y justifique en una linea por que los dos Won't quedan fuera de esta version de VetCare.",
            "Paso 5: complete la matriz de trazabilidad con las columnas Necesidad, RF/RNF, Pantalla prevista y Prueba de aceptacion, exporte el documento a PDF y subalo a ExamLab con el nombre RF-RNF-VetCare-<sus apellidos>.pdf."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ este catalogo es el contrato del Proyecto Integrador; todo lo que se dibuje en las clases siguientes (casos de uso, clases, mockups, diccionario de datos) debe poder rastrearse hasta un requisito de esta lista.",
            "Si un requisito no queda hoy en el documento, sencillamente no existe para VetCare: no se disena, no se dibuja y no se programa en Programacion II.",
            "Es tambien la primera entrega que se defiende hablando: usted debe poder explicarle al Dr. Ramirez, en dos minutos, que se le va a construir y que no."
        ],
        "escenario": [
            "Hoy solo existe la transcripcion de la entrevista al Dr. Ramirez: cinco frases sueltas, dichas en lenguaje de veterinario y no de analista.",
            "La clinica Huellitas sigue en papel: fichas que se extravian, busquedas de historial que toman varios minutos con el paciente esperando y cero metricas mensuales.",
            "No hay documento de requisitos, no hay prioridades acordadas y nadie sabe todavia que queda dentro y que queda fuera de la primera version de VetCare."
        ],
        "criterios": [
            "El documento tiene minimo 8 RF y 4 RNF, todos con ID unico, actor explicito y redaccion en plantilla.",
            "Cada RNF trae al menos un valor medible (segundos, cantidad, frecuencia o porcentaje) y su forma de verificacion.",
            "Ningun requisito usa las palabras rapido, amigable, facil, intuitivo, robusto u optimo sin cuantificarlas.",
            "La matriz de trazabilidad conecta las cinco frases de la entrevista con al menos un requisito cada una, y ningun requisito queda huerfano de origen."
        ],
        "pistas": [
            "Con que prueba concreta, hecha en menos de dos minutos delante del Dr. Ramirez, demostraria que este requisito quedo cumplido?",
            "Si borro este requisito de la lista, VetCare deja de resolver alguno de los tres dolores de Huellitas o solamente queda menos vistoso?",
            "Esta frase describe una sola accion de un solo actor, o estoy escondiendo dos o tres requisitos detras de una y?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: las cinco necesidades quedan etiquetadas asi. NEC-01 'necesito que las fichas no se me pierdan mas' (origen: entrevista Dr. Ramirez, frase 1, dolor de extravio); NEC-02 'cuando llega un perro quiero ver de una lo que le hemos hecho antes' (frase 2, busqueda lenta del historial); NEC-03 'que la auxiliar pueda agendar sin llamarme a mi' (frase 3, cuello de botella en la agenda); NEC-04 'el sistema tiene que ser rapido' (frase 4, desempeno sin cuantificar); NEC-05 'quiero saber cuantas consultas hicimos en el mes' (frase 5, ausencia de metricas). Ninguna se copia al catalogo tal cual: todas se traducen.",
            "Paso 2 resuelto: RF-01 el sistema debe permitir a la auxiliar registrar un dueno con documento, nombre, telefono y direccion, sin permitir dos duenos con el mismo documento; RF-02 el sistema debe permitir a la auxiliar registrar una mascota asociada a un dueno, con codigo unico, nombre, especie, raza y fecha de nacimiento; RF-03 el sistema debe permitir al veterinario consultar el historial de atenciones de una mascota buscando por el documento del dueno; RF-04 el sistema debe permitir al veterinario registrar una atencion con fecha, motivo, diagnostico y tratamiento; RF-05 el sistema debe permitir a la auxiliar agendar una cita seleccionando mascota, veterinario, fecha y hora; RF-06 el sistema debe permitir a la auxiliar cancelar o reprogramar una cita registrando el motivo del cambio; RF-07 el sistema debe permitir al administrador generar el reporte mensual de consultas atendidas por veterinario; RF-08 el sistema debe permitir a la auxiliar listar las citas del dia ordenadas por hora. Ninguno lleva una 'y' que una dos capacidades distintas.",
            "Paso 3 resuelto: RNF-01 (desempeno) la consulta de historial por documento del dueno responde en maximo 3 segundos, con 5.000 fichas cargadas y 10 usuarios concurrentes, y se verifica con cronometro sobre la base de prueba; RNF-02 (control de acceso) el sistema maneja dos perfiles, auxiliar y veterinario, donde la auxiliar registra duenos, mascotas y citas pero no puede ver ni editar el diagnostico clinico, y se verifica intentando abrir el diagnostico con sesion de auxiliar y comprobando que el sistema lo niega; RNF-03 (usabilidad) un usuario nuevo agenda una cita en maximo 4 clics y despues de no mas de 10 minutos de induccion, y se verifica con tres personas ajenas al diseño contando clics y tiempo; RNF-04 (respaldo) el sistema genera copia automatica diaria a las 11:00 p.m. y una vez al mes se ejecuta una restauracion de prueba exitosa, verificada con la evidencia del archivo restaurado.",
            "Paso 4 resuelto: Must (6 de 12, 50% de la lista) RF-01, RF-02, RF-03, RF-04, RF-05 y RNF-01, porque atacan directamente los tres dolores de Huellitas; Should RF-07, RF-08 y RNF-04, porque hoy existe plan B manual (el conteo a mano y la agenda en cuaderno) que aguanta unas semanas mas; Could RF-06 y RNF-03; Won't de esta version el recordatorio automatico por WhatsApp y la facturacion electronica, justificados asi: no atacan ninguno de los tres dolores declarados por la clinica y exigen integraciones externas que el alcance del semestre no cubre; quedan escritos en el documento con la etiqueta Won't para que nadie los reclame despues.",
            "Paso 5 resuelto: la matriz queda con las cinco necesidades cubiertas. NEC-01 -> RF-01 y RF-02 -> pantalla P-01 Registro de dueno y mascota -> PR-01 crear un dueno, intentar repetir el documento y verificar que el sistema lo rechaza; NEC-02 -> RF-03 -> pantalla P-02 Historial de mascota -> PR-07 cronometrar la busqueda con la base de 5.000 fichas; NEC-03 -> RF-05 y RF-08 -> pantalla P-03 Agenda -> PR-09 la auxiliar agenda una cita sin intervencion del veterinario y la cita aparece en el listado del dia; NEC-04 -> RNF-01 -> aplica a P-02 -> PR-07 con 10 usuarios concurrentes; NEC-05 -> RF-07 -> pantalla P-05 Reporte mensual -> PR-12 comparar el total del sistema contra el conteo manual de un mes. Ningun requisito queda sin origen y ninguna necesidad queda suelta."
        ],
        "solucion_rubrica": [
            "Requisitos funcionales bien formulados, minimo 8, con actor y accion unica (4)",
            "Requisitos no funcionales cuantificados y verificables, minimo 4 categorias (3)",
            "Priorizacion MoSCoW coherente con los tres dolores de Huellitas y Won't justificados (2)",
            "Matriz de trazabilidad completa, sin necesidades sueltas ni requisitos huerfanos (1)"
        ],
        "solucion_errores": [
            "Escribir RF-09 el sistema debe registrar mascotas y generar reportes y enviar correos: son tres requisitos disfrazados de uno, y ninguno se puede probar por separado.",
            "Poner como RNF el sistema debe ser seguro y confiable sin definir perfiles, sin tiempo maximo de sesion y sin politica de respaldo: suena bien y no obliga a nada.",
            "Marcar 11 de los 12 requisitos como Must y dejar un solo Should: eso no es priorizar, es aplazar la decision para el dia en que ya no haya tiempo."
        ],
        "codigo_slide_titulo": "Ficha de requisito RF-03 (plantilla proyectable)",
        "codigo_slide_lineas": [
            "ID: RF-03",
            "Nombre: Consultar historial clinico de una mascota",
            "Actor: Veterinario (consulta completa) / Auxiliar (consulta sin diagnostico)",
            "Descripcion: El sistema debe permitir consultar el historial de atenciones de una mascota a partir del documento del dueno.",
            "Entrada: documento del dueno o codigo de la mascota",
            "Salida: lista de atenciones con fecha, motivo, diagnostico y veterinario, ordenada de la mas reciente a la mas antigua",
            "Regla de negocio: RN-02 una mascota siempre pertenece a un unico dueno registrado",
            "Criterio de verificacion: dado un dueno con 12 atenciones, la busqueda por documento devuelve las 12 en 3 segundos o menos",
            "Prioridad MoSCoW: Must",
            "Origen: entrevista Dr. Ramirez, frase 2 (necesidad NEC-02)",
            "Trazabilidad: NEC-02 -> RF-03 -> CU-04 -> Pantalla P-02 -> Prueba PR-07",
            "Estado: aprobado por el cliente"
        ],
        "codigo_slide_caption": "Un requisito sin criterio de verificacion y sin origen es una opinion con numero de identificacion.",
        "artefacto_archivo": "RF-RNF-VetCare.md",
        "artefacto_contenido": "# VetCare - Catalogo de requisitos (plantilla de trabajo)\n\nProyecto Integrador: sistema VetCare para la Clinica Veterinaria Huellitas.\nAsignatura: Seminario de Sistemas. Entrega: ExamLab, formato PDF.\n\n---\n\n## 1. Fuente de la elicitacion\n\nEntrevista al Dr. Ramirez, medico veterinario y dueno de la clinica Huellitas.\nFrases crudas registradas (necesidades, NO requisitos):\n\n| ID | Frase textual del cliente | Dolor que revela |\n|---|---|---|\n| NEC-01 | 'Necesito que las fichas no se me pierdan mas.' | Extravio de fichas |\n| NEC-02 | 'Cuando llega un perro quiero ver de una lo que le hemos hecho antes.' | Busqueda lenta del historial |\n| NEC-03 | 'Que la auxiliar pueda agendar sin llamarme a mi.' | Cuello de botella en agenda |\n| NEC-04 | 'El sistema tiene que ser rapido, aqui no hay tiempo de esperar.' | Desempeno (sin cuantificar) |\n| NEC-05 | 'Quiero saber cuantas consultas hicimos en el mes.' | Ausencia de metricas |\n\n---\n\n## 2. Ficha de requisito funcional (copie una por cada RF)\n\n| Campo | Contenido |\n|---|---|\n| ID | RF-00 |\n| Nombre | |\n| Actor | |\n| Descripcion | El sistema debe permitir a <actor> <accion> <objeto> [bajo <condicion>] |\n| Entrada | |\n| Salida | |\n| Regla de negocio | |\n| Criterio de verificacion | (debe tener un numero o un si/no) |\n| Prioridad MoSCoW | Must / Should / Could / Won't |\n| Origen | NEC-00, frase del cliente |\n| Estado | propuesto / aprobado / descartado |\n\n---\n\n## 3. Catalogo de requisitos funcionales\n\n| ID | Requisito (plantilla) | Actor | MoSCoW | Verificacion |\n|---|---|---|---|---|\n| RF-01 | El sistema debe permitir registrar un dueno con documento, nombre, telefono y direccion | Auxiliar | Must | Se crea el dueno y el documento no se puede repetir |\n| RF-02 | | | | |\n| RF-03 | | | | |\n| RF-04 | | | | |\n| RF-05 | | | | |\n| RF-06 | | | | |\n| RF-07 | | | | |\n| RF-08 | | | | |\n\n---\n\n## 4. Catalogo de requisitos no funcionales\n\n| ID | Categoria | Requisito CUANTIFICADO | Como se mide |\n|---|---|---|---|\n| RNF-01 | Desempeno | La consulta de historial responde en maximo 3 s con 5.000 fichas y 10 usuarios concurrentes | Cronometro sobre base de prueba |\n| RNF-02 | Control de acceso | | |\n| RNF-03 | Usabilidad | | |\n| RNF-04 | Respaldo | | |\n\n---\n\n## 5. Matriz de trazabilidad\n\n| Necesidad | Requisito | Pantalla prevista | Prueba de aceptacion |\n|---|---|---|---|\n| NEC-02 | RF-03 | P-02 Historial de mascota | PR-07 cronometrar busqueda |\n| | | | |\n| | | | |\n\n---\n\n## 6. Lista negra de palabras (si aparecen, el requisito se devuelve)\n\nrapido, amigable, facil, intuitivo, robusto, moderno, optimo, eficiente, seguro (sin metrica), sencillo, agil, de ultima tecnologia.\n\n---\n\n## 7. Checklist antes de subir a ExamLab\n\n- [ ] Hay minimo 8 RF y 4 RNF.\n- [ ] Ningun RF tiene una 'y' uniendo dos capacidades distintas.\n- [ ] Todos los RNF tienen por lo menos un numero.\n- [ ] Los Must no superan el 60% de la lista.\n- [ ] Los Won't estan escritos y justificados (protegen el alcance).\n- [ ] Cada necesidad NEC-01 a NEC-05 aparece al menos una vez en la matriz.\n- [ ] El archivo se llama RF-RNF-VetCare-<apellidos>.pdf\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cual de las siguientes frases es un requisito NO funcional correctamente formulado para VetCare?",
                "opciones": [
                    "A) El sistema debe permitir agendar una cita seleccionando mascota, veterinario, fecha y hora",
                    "B) El sistema debe ser rapido y facil de usar para la auxiliar",
                    "C) La consulta de historial por documento debe responder en maximo 3 segundos con 5.000 fichas y 10 usuarios concurrentes",
                    "D) El sistema debe generar el reporte mensual de consultas"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "En MoSCoW, que significa exactamente que un requisito quede clasificado como Won't?",
                "opciones": [
                    "A) Que el equipo no sabe todavia como hacerlo",
                    "B) Que queda declarado explicitamente fuera de esta version, para proteger el alcance",
                    "C) Que se hara solo si sobra tiempo al final",
                    "D) Que el cliente lo rechazo por costoso y no se volvera a considerar nunca"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "El Dr. Ramirez no logra explicar como hace hoy para ubicar una ficha, pero lo hace veinte veces al dia. Cual tecnica de elicitacion es la mas adecuada?",
                "opciones": [
                    "A) Entrevista estructurada con preguntas cerradas",
                    "B) Encuesta enviada a todo el personal",
                    "C) Observacion directa del proceso en la recepcion",
                    "D) Revision del manual de funciones de la clinica"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual de estos requisitos esta MAL formulado y debe partirse antes de aprobarse?",
                "opciones": [
                    "A) El sistema debe permitir a la auxiliar registrar una mascota asociada a un dueno",
                    "B) El sistema debe permitir registrar mascotas y generar reportes y enviar correos de recordatorio",
                    "C) El sistema debe permitir al veterinario registrar el diagnostico de una atencion",
                    "D) El sistema debe permitir consultar las citas del dia ordenadas por hora"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "La trazabilidad hacia atras permite saber de que necesidad o frase del cliente nacio cada requisito.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Como las frases del cliente ya expresan lo que necesita, transcribirlas tal cual al documento es suficiente para tener requisitos validos.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Convierta la frase cruda 'el sistema tiene que ser rapido' en un RNF verificable para VetCare e indique como se probaria.",
                "clave": "RNF-01: la busqueda de historial por documento del dueno debe devolver resultados en maximo 3 segundos, con 5.000 fichas cargadas y 10 usuarios concurrentes. Se prueba cargando la base de datos de ejemplo y cronometrando la consulta; si supera los 3 segundos el requisito no pasa."
            },
            {
                "tipo": "abierta",
                "q": "Explique con sus palabras por que se dice que 'si no se puede verificar, no es un requisito' y de un ejemplo de VetCare.",
                "clave": "Porque un enunciado que no se puede medir ni comprobar no permite decir si el sistema quedo bien o mal, con lo cual no se puede aceptar ni rechazar la entrega y el cliente y el equipo terminan discutiendo por opiniones. Ejemplo: 'el sistema debe ser amigable' no se puede verificar; en cambio 'un usuario nuevo agenda una cita en maximo 4 clics y sin capacitacion mayor a 10 minutos' si se puede comprobar con una prueba con usuarios."
            }
        ]
    },
    {
        "n": 7,
        "slug": "Historias de usuario",
        "titulo": "Historias de usuario",
        "subtitulo": "El requisito contado por quien lo necesita y con criterios que se pueden cobrar",
        "herramienta": "Google Docs · Excalidraw",
        "hito_pi": "Queda listo el backlog inicial de VetCare: dos epicas descompuestas en ocho historias priorizadas, con criterios de aceptacion y talla en puntos.",
        "entregable": "Tablero de backlog con 8 historias en formato Como/quiero/para, cada una con 2 o 3 criterios de aceptacion en Dado-Cuando-Entonces, estimacion en puntos y trazabilidad al RF de la clase 6, subido a ExamLab.",
        "demo": "El docente toma el RF-03 del catalogo, lo convierte en vivo en historia con criterios y luego muestra una historia partida por capas para tumbarla con INVEST.",
        "teoria": [
            "Una historia de usuario no es un requisito abreviado ni una moda de las metodologias agiles: es el recordatorio corto de una conversacion pendiente entre quien necesita el sistema y quien lo va a construir. Su formato canonico tiene tres partes: Como <rol> quiero <accion> para <beneficio>. El rol obliga a nombrar a alguien concreto (la auxiliar Marcela, el veterinario de turno, el dueno de la mascota) y no al generico usuario, que no existe en ninguna clinica del mundo; la accion describe algo que esa persona hace, no algo que hace la base de datos por dentro; y el para es la parte que casi todo el mundo borra por afan y es la mas valiosa, porque es la unica que explica por que vale la pena gastar tiempo y plata en eso. En VetCare, Como auxiliar quiero buscar la ficha de una mascota por el documento del dueno para no revolver la carpeta fisica mientras el paciente espera en el meson se entiende sin traduccion; en cambio El sistema debe tener un buscador no dice a quien le sirve ni que dolor cura. Ron Jeffries lo resumio en tres C: Card, la tarjeta corta; Conversation, la charla que aclara los detalles; y Confirmation, los criterios de aceptacion. La tarjeta sin conversacion es un titulo huerfano, y la conversacion sin criterios es un acuerdo que nadie puede cobrar. Frente al requisito tradicional de la clase pasada, la historia no lo reemplaza: el requisito es el contrato formal y la historia es la unidad de trabajo con la que se planea la entrega.",
            "Los criterios de aceptacion son la parte que convierte una historia bonita en una historia entregable, y se escriben en el patron Dado <contexto inicial> Cuando <accion del usuario> Entonces <resultado observable>. Cada criterio debe poder responderse con un si o un no mirando la pantalla, nunca con un depende. Para la historia de buscar el historial en VetCare los criterios serian: Dado un dueno con tres mascotas registradas, cuando busco por su documento, entonces el sistema lista las tres mascotas con nombre y especie; Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo sus atenciones de la mas reciente a la mas antigua; Dado un documento que no existe, cuando busco, entonces el sistema muestra un mensaje claro y ofrece crear el dueno. Fijense que el tercer criterio es el que casi siempre falta: el camino alterno, el caso feo, el error. Una historia con solo criterios felices es una historia a medio pensar. Ademas, los criterios de aceptacion son el puente directo con el prototipo navegable y con las pruebas que hara el companero de Programacion II, porque son literalmente el guion de lo que se va a revisar.",
            "INVEST es la lista de chequeo para saber si una historia esta bien cortada, y conviene revisarla letra por letra con VetCare en la mano. Independiente: se puede hacer sin esperar a otra; si la historia de agendar cita necesita obligatoriamente que exista la de registrar mascota, hay dependencia y toca ordenarlas. Negociable: la historia describe la necesidad, no la solucion tecnica; decir quiero un combo desplegable con autocompletar en JavaScript ya no es historia, es diseno impuesto. Valiosa: alguien de la clinica gana algo real; si nadie de Huellitas nota la diferencia, no es historia sino tarea interna. Estimable: el equipo entiende lo suficiente para tallarla; si nadie sabe cuanto pesa, falta conversacion o hace falta investigar aparte. Small o pequena: cabe en una iteracion; si toma tres semanas es una epica disfrazada. Testeable: tiene criterios verificables, que es exactamente la misma regla de oro de la clase pasada aplicada en formato agil. Una historia que falla dos letras de INVEST no se planea todavia, se vuelve a partir.",
            "Una epica es una historia grande que todavia no cabe en una iteracion, y descomponerla es una habilidad que se aprende cortando mal varias veces. El corte correcto es vertical, como una rebanada de pastel que trae bizcocho, crema y cubierta: cada historia atraviesa pantalla, logica y datos y deja algo que el usuario puede usar. El corte equivocado es horizontal, por capas: una historia para la pantalla, otra para la logica y otra para la base de datos; asi ninguna de las tres sirve sola y el cliente no ve nada hasta que estan las tres. En VetCare la epica Historial clinico se parte en: consultar historial por documento del dueno, registrar una atencion nueva, adjuntar resultados de laboratorio y filtrar el historial por rango de fechas; cada una entregable y demostrable por separado. Otros ejes utiles para cortar son por tipo de dato (primero solo perros y gatos, despues otras especies), por regla de negocio (primero sin control de acceso, luego con perfiles) y por camino (primero el flujo feliz, luego los errores). El nombre de la epica se conserva como etiqueta en cada historia para no perder el hilo.",
            "Estimar en agil no es adivinar horas sino comparar tamanos, y esa es la razon de los puntos de historia: son una medida relativa que mezcla esfuerzo, complejidad e incertidumbre. Se toma una historia mediana y conocida como referencia (por ejemplo registrar un dueno vale 3 puntos) y todas las demas se comparan contra ella usando una escala tipo Fibonacci 1, 2, 3, 5, 8, 13, donde el salto grande refleja que entre mas grande la historia, menos confiable la estimacion; si algo llega a 13 o mas, la senal no es de dificultad sino de que hay que partirla. La tecnica de sala es el planning poker: todos muestran su carta al tiempo y lo importante no es el numero sino la discusion cuando alguien dice 2 y otro dice 8, porque ahi aparece el requisito que unos entendieron y otros no. Con dos o tres iteraciones se conoce la velocidad del equipo y recien ahi se puede prometer fechas. En el Proyecto Integrador este backlog es la lista de trabajo que se le entrega al companero de Programacion II para que sepa por donde empezar; y quien solo cursa Seminario usa el mismo backlog para ordenar las pantallas de su prototipo navegable, en el mismo orden de prioridad.",
            "Error tipico del docente que no domina el tema: pensar que la historia de usuario es simplemente el mismo requisito escrito con la formula Como/quiero/para y calificar que la formula este completa. Con ese criterio pasan barbaridades como Como usuario quiero un boton de guardar para guardar, que cumple la plantilla y no dice absolutamente nada: el rol es generico, la accion es una solucion tecnica y el beneficio es una repeticion circular de la accion. Tambien es tipico aceptar historias sin criterios de aceptacion porque parece que alargan la tarea, permitir el corte horizontal por capas porque a los estudiantes les suena logico, y pedir estimacion en horas porque el docente no entiende para que sirven los puntos, con lo cual el ejercicio se vuelve un cronograma falso. El antidoto es revisar cada historia con tres preguntas en voz alta: quien es esta persona con nombre y cargo en la clinica Huellitas, que gana ella cuando esto exista, y con que prueba concreta se acepta. Si la respuesta al beneficio repite la accion, la historia se devuelve sin negociar."
        ],
        "taller": [
            "Paso 1: agrupe los RF del catalogo de la clase 6 en dos epicas de VetCare (por ejemplo Gestion de pacientes e Historial y agenda) y escriba el nombre y el objetivo de cada epica en una linea.",
            "Paso 2: descomponga las dos epicas en 8 historias con el formato Como <rol de la clinica Huellitas> quiero <accion> para <beneficio>, usando roles concretos (auxiliar, veterinario, administrador) y nunca la palabra usuario.",
            "Paso 3: escriba 2 o 3 criterios de aceptacion por historia en Dado-Cuando-Entonces, e incluya obligatoriamente un criterio de camino alterno o de error en al menos cuatro de las ocho historias.",
            "Paso 4: revise cada historia contra INVEST marcando las seis letras con si o no; toda historia que falle dos o mas letras debe reescribirse o partirse antes de continuar.",
            "Paso 5: estime en puntos con la escala 1, 2, 3, 5, 8 tomando 'registrar un dueno = 3' como referencia, ordene el backlog de mayor a menor prioridad, agregue la columna de trazabilidad al RF de origen y suba el tablero a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el backlog es la version ejecutable del catalogo de requisitos; es la lista con la que se decide que se disena primero y, en Programacion II, que se codifica primero.",
            "Los criterios de aceptacion que escriba hoy se vuelven literalmente el guion de revision del prototipo navegable y de las pruebas del sistema.",
            "Una historia sin beneficio claro es una funcionalidad que nadie va a extranar si no se hace: aqui es donde se justifica cada pantalla de VetCare."
        ],
        "escenario": [
            "Ya existe el catalogo de requisitos de VetCare con RF, RNF, prioridades MoSCoW y matriz de trazabilidad aprobados en la clase anterior.",
            "Ese catalogo esta escrito en lenguaje formal de analista y todavia no permite decidir por donde arrancar ni cuanto pesa cada pieza.",
            "El equipo del Proyecto Integrador necesita una lista ordenada de trabajo para poder repartirse las siguientes semanas entre diseno y construccion."
        ],
        "criterios": [
            "Las 8 historias usan roles concretos de la clinica Huellitas y ninguna emplea el rol generico usuario.",
            "Cada historia tiene minimo 2 criterios de aceptacion en Dado-Cuando-Entonces y al menos cuatro incluyen un camino alterno o de error.",
            "Todas las historias pasan INVEST con al menos cinco de las seis letras en si, y ninguna esta cortada por capas tecnicas.",
            "Cada historia trae estimacion en puntos, prioridad y el RF de origen; ninguna historia supera los 8 puntos sin partirse."
        ],
        "pistas": [
            "Si le leo esta historia al Dr. Ramirez sin explicarle nada, entiende quien gana algo y que gana, o solo entiende que hay una pantalla nueva?",
            "El 'para' de mi historia esta repitiendo la accion con otras palabras, o dice de verdad el beneficio para la clinica?",
            "Si esta historia se entregara sola, sin ninguna otra, el usuario podria hacer algo completo de principio a fin?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: quedan dos epicas. E-01 Gestion de pacientes, cuyo objetivo es que ninguna ficha se pierda y cada mascota tenga un dueno identificado (agrupa RF-01 y RF-02); y E-02 Historial y agenda, cuyo objetivo es que el historial se consulte en segundos y la agenda no dependa del veterinario (agrupa RF-03 a RF-08).",
            "Paso 2 resuelto: las ocho historias quedan escritas asi. HU-01 (E-01, RF-01) Como auxiliar de Huellitas quiero registrar un dueno con su documento, nombre y telefono para no volver a abrir una carpeta duplicada del mismo cliente. HU-02 (E-01, RF-02) Como auxiliar quiero registrar una mascota asociada a su dueno con codigo unico, especie, raza y fecha de nacimiento para que su ficha no se confunda con la de otro paciente. HU-03 (E-02, RF-08) Como auxiliar quiero ver las citas del dia ordenadas por hora para saber a quien sigue atender sin preguntarle al doctor. HU-04 (E-02, RF-03) Como veterinario quiero consultar el historial de una mascota por el documento del dueno para decidir el tratamiento sin depender de la carpeta fisica. HU-05 (E-02, RF-04) Como veterinario quiero registrar la atencion de una mascota con motivo, diagnostico y tratamiento para que quede en el historial de ese paciente. HU-06 (E-02, RF-05) Como auxiliar quiero agendar una cita seleccionando mascota, veterinario, fecha y hora para no tener que llamar al doctor cada vez. HU-07 (E-02, RF-06) Como auxiliar quiero cancelar o reprogramar una cita registrando el motivo para que la agenda del dia refleje lo que de verdad va a pasar. HU-08 (E-02, RF-07) Como administrador quiero ver el total de consultas del mes por veterinario para saber si la clinica esta creciendo.",
            "Paso 3 resuelto: para HU-04 los criterios quedan CA-1 Dado un dueno con tres mascotas registradas, cuando busco por su documento, entonces el sistema lista las tres mascotas con nombre y especie; CA-2 Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo las atenciones ordenadas de la mas reciente a la mas antigua; CA-3 (alterno) Dado un documento no registrado, cuando busco, entonces el sistema muestra el mensaje 'No hay duenos con ese documento' y ofrece crear uno nuevo. Para HU-06 quedan CA-1 Dado el veterinario Perez con la agenda libre el martes a las 10:00 a.m., cuando la auxiliar agenda a Rocky en ese espacio, entonces la cita aparece en la agenda del martes con estado Programada; CA-2 (alterno) Dado que ese mismo espacio ya esta ocupado, cuando la auxiliar intenta agendar otra cita ahi, entonces el sistema bloquea el guardado y muestra 'El veterinario ya tiene una cita a esa hora'; CA-3 (alterno) Dado un intento de agendar en una fecha anterior a hoy, cuando se guarda, entonces el sistema lo rechaza y explica el motivo.",
            "Paso 4 resuelto: la historia 'Como veterinario quiero la tabla de la base de datos de atenciones para guardar los diagnosticos' se rechaza porque falla Valiosa (nadie en la clinica percibe valor), falla Negociable (impone la solucion tecnica) y esta cortada por capas; se reemplaza por HU-05 Como veterinario quiero registrar la atencion de una mascota con motivo, diagnostico y tratamiento para que quede en el historial de ese paciente. HU-06 pasa las seis letras pero queda en el limite de la S (8 puntos), asi que se marca como candidata a partirse en 'agendar cita' y 'validar choque de horario' si el equipo se queda corto de tiempo.",
            "Paso 5 resuelto: con la referencia registrar un dueno = 3 puntos, el backlog ordenado por prioridad queda HU-01 (3, Must, RF-01), HU-02 (3, Must, RF-02), HU-04 (5, Must, RF-03), HU-05 (5, Must, RF-04), HU-06 (8, Must, RF-05), HU-03 (2, Should, RF-08), HU-07 (3, Should, RF-06) y HU-08 (5, Should, RF-07); suma 34 puntos, ninguna historia pasa de 8 y HU-06 queda senalada para revisar en la proxima sesion porque 8 puntos es la frontera antes de partir."
        ],
        "solucion_rubrica": [
            "Ocho historias bien formuladas con rol concreto, accion y beneficio real (4)",
            "Criterios de aceptacion en Dado-Cuando-Entonces, incluyendo caminos alternos (3)",
            "Aplicacion de INVEST y descomposicion vertical de las epicas (2)",
            "Estimacion relativa coherente, priorizacion y trazabilidad al RF de origen (1)"
        ],
        "solucion_errores": [
            "Escribir Como usuario quiero un boton de guardar para guardar los datos: rol generico, accion que es solucion tecnica y beneficio que repite la accion; no dice nada y aun asi cumple la plantilla.",
            "Partir la epica en tres historias llamadas pantalla de historial, logica de historial y tabla de historial: corte horizontal por capas, ninguna se puede entregar ni demostrar sola.",
            "Estimar en horas (esta historia son 6 horas) en lugar de puntos, y ademas dejar historias de 13 y 21 puntos sin partir, con lo cual el backlog no sirve para planear nada."
        ],
        "codigo_slide_titulo": "Historia HU-04 con criterios de aceptacion (artefacto proyectable)",
        "codigo_slide_lineas": [
            "HU-04  [Epica: E-02 Historial y agenda]",
            "Como veterinario de la clinica Huellitas",
            "quiero consultar el historial de atenciones de una mascota por el documento del dueno",
            "para decidir el tratamiento sin depender de la carpeta fisica.",
            "",
            "Criterios de aceptacion",
            "CA-1  Dado un dueno con 3 mascotas registradas, cuando busco por su documento, entonces el sistema lista las 3 mascotas con nombre y especie.",
            "CA-2  Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo sus atenciones de la mas reciente a la mas antigua.",
            "CA-3  Dado un documento no registrado, cuando busco, entonces el sistema muestra 'No hay duenos con ese documento' y ofrece crear uno.",
            "",
            "Estimacion: 5 puntos   |   Prioridad: Must   |   Origen: RF-03 / NEC-02",
            "Definicion de terminado: mockup aprobado + los 3 criterios verificados en el prototipo navegable"
        ],
        "codigo_slide_caption": "La historia dice a quien le sirve y para que; los criterios de aceptacion son la unica parte que se puede cobrar.",
        "artefacto_archivo": "Backlog-Historias-VetCare.md",
        "artefacto_contenido": "# VetCare - Backlog inicial de historias de usuario\n\nProyecto Integrador: Clinica Veterinaria Huellitas.\nAsignatura: Seminario de Sistemas. Entrega: ExamLab.\n\n---\n\n## 1. Epicas\n\n| ID | Epica | Objetivo en una linea | RF que agrupa |\n|---|---|---|---|\n| E-01 | Gestion de pacientes | Que ninguna ficha se pierda y cada mascota tenga un dueno identificado | RF-01, RF-02 |\n| E-02 | Historial y agenda | Que el historial se consulte en segundos y la agenda no dependa del veterinario | RF-03 a RF-08 |\n\n---\n\n## 2. Plantilla de historia (copie una por cada HU)\n\n**HU-00**  [Epica: ]\n\nComo <rol concreto de Huellitas: auxiliar / veterinario / administrador>\nquiero <accion que hace esa persona>\npara <beneficio real para la clinica>.\n\n**Criterios de aceptacion**\n\n- CA-1  Dado <contexto>, cuando <accion>, entonces <resultado observable>.\n- CA-2  Dado <contexto>, cuando <accion>, entonces <resultado observable>.\n- CA-3  (camino alterno o error) Dado <contexto>, cuando <accion>, entonces <resultado observable>.\n\n**Estimacion:** ___ puntos  |  **Prioridad:** Must/Should/Could  |  **Origen:** RF-__\n\n---\n\n## 3. Ejemplo resuelto\n\n**HU-04**  [Epica: E-02]\n\nComo veterinario de la clinica Huellitas\nquiero consultar el historial de atenciones de una mascota por el documento del dueno\npara decidir el tratamiento sin depender de la carpeta fisica.\n\n- CA-1  Dado un dueno con 3 mascotas registradas, cuando busco por su documento, entonces el sistema lista las 3 mascotas con nombre y especie.\n- CA-2  Dado que selecciono la mascota Rocky, cuando abro su historial, entonces veo sus atenciones de la mas reciente a la mas antigua.\n- CA-3  Dado un documento no registrado, cuando busco, entonces el sistema muestra 'No hay duenos con ese documento' y ofrece crear uno.\n\n**Estimacion:** 5 puntos  |  **Prioridad:** Must  |  **Origen:** RF-03\n\n---\n\n## 4. Tablero del backlog\n\n| ID | Epica | Historia (resumen) | Puntos | Prioridad | RF origen | INVEST ok |\n|---|---|---|---|---|---|---|\n| HU-01 | E-01 | Registrar dueno | 3 | Must | RF-01 | si |\n| HU-02 | | | | | | |\n| HU-03 | | | | | | |\n| HU-04 | E-02 | Consultar historial | 5 | Must | RF-03 | si |\n| HU-05 | | | | | | |\n| HU-06 | | | | | | |\n| HU-07 | | | | | | |\n| HU-08 | | | | | | |\n\n---\n\n## 5. Chequeo INVEST (marque si / no por historia)\n\n| Letra | Pregunta de control |\n|---|---|\n| I - Independiente | Se puede entregar sin esperar otra historia? |\n| N - Negociable | Describe la necesidad y no la solucion tecnica? |\n| V - Valiosa | Alguien de Huellitas gana algo concreto? |\n| E - Estimable | El equipo entiende lo suficiente para tallarla? |\n| S - Pequena | Cabe en una iteracion (8 puntos o menos)? |\n| T - Testeable | Tiene criterios verificables con si/no? |\n\n---\n\n## 6. Escala de estimacion\n\nReferencia: **registrar un dueno = 3 puntos**.\nEscala permitida: 1, 2, 3, 5, 8. Todo lo que llegue a 13 se parte.\n\n---\n\n## 7. Checklist antes de subir a ExamLab\n\n- [ ] 8 historias, ninguna con el rol 'usuario'.\n- [ ] Ningun 'para' repite la accion.\n- [ ] Minimo 2 criterios por historia y 4 historias con camino alterno.\n- [ ] Cortes verticales (nada de pantalla / logica / base de datos por separado).\n- [ ] Todas estimadas y ordenadas por prioridad.\n- [ ] Archivo: Backlog-VetCare-<apellidos>.pdf\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cual de estas historias esta correctamente formulada para VetCare?",
                "opciones": [
                    "A) Como usuario quiero un boton de guardar para guardar los datos",
                    "B) Como auxiliar quiero agendar una cita seleccionando mascota, veterinario, fecha y hora para no tener que llamar al doctor cada vez",
                    "C) Como sistema quiero almacenar las atenciones en la tabla ATENCION para tener persistencia",
                    "D) Como veterinario quiero una interfaz moderna y agradable para trabajar mejor"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Que letra de INVEST se incumple cuando una historia dice 'quiero un combo desplegable con autocompletar en JavaScript'?",
                "opciones": [
                    "A) Independiente",
                    "B) Negociable",
                    "C) Estimable",
                    "D) Testeable"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual es la forma correcta de descomponer la epica 'Historial clinico'?",
                "opciones": [
                    "A) Una historia para la pantalla, otra para la logica y otra para la base de datos",
                    "B) Una historia por cada desarrollador disponible en el equipo",
                    "C) Consultar historial, registrar atencion, adjuntar resultados de laboratorio y filtrar por fechas",
                    "D) Una sola historia grande de 21 puntos que se trabaja durante todo el semestre"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Para que sirve principalmente estimar en puntos de historia en lugar de horas?",
                "opciones": [
                    "A) Para que el cliente no sepa cuanto se demora el equipo",
                    "B) Para comparar tamanos relativos y hacer visible la incertidumbre, y luego calcular velocidad",
                    "C) Porque los puntos son mas exactos que las horas",
                    "D) Porque las horas no se pueden sumar entre varias personas"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Los criterios de aceptacion se escriben en el patron Dado-Cuando-Entonces y deben poder responderse con un si o un no mirando la pantalla.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Una historia de usuario reemplaza por completo al catalogo de requisitos, por eso despues de escribir el backlog el documento de RF y RNF se descarta.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Escriba una historia de usuario para el reporte mensual de VetCare y dos criterios de aceptacion, uno de ellos de camino alterno.",
                "clave": "Como administrador de la clinica Huellitas quiero ver el total de consultas atendidas en el mes por veterinario para saber si la clinica esta creciendo. CA-1: Dado el mes de septiembre con 120 atenciones registradas, cuando genero el reporte de ese mes, entonces el sistema muestra el total 120 desglosado por veterinario. CA-2 (alterno): Dado un mes sin atenciones registradas, cuando genero el reporte, entonces el sistema muestra el mensaje 'No hay atenciones en el periodo seleccionado' y no una tabla vacia sin explicacion."
            },
            {
                "tipo": "abierta",
                "q": "Cual es la diferencia de fondo entre un requisito tradicional y una historia de usuario, y por que en el Proyecto Integrador se usan los dos?",
                "clave": "El requisito tradicional es el enunciado formal y contractual de lo que el sistema debe hacer, redactado en lenguaje de analista y pensado para ser completo y verificable; la historia de usuario es una unidad corta de trabajo escrita desde la perspectiva de quien la necesita, que sirve para conversar, priorizar y estimar. En el PI se usan los dos porque el catalogo de RF/RNF fija el alcance y la trazabilidad de VetCare, mientras el backlog de historias ordena por donde se empieza a disenar y a construir."
            }
        ]
    },
    {
        "n": 8,
        "slug": "Introduccion a UML",
        "titulo": "Introduccion a UML",
        "subtitulo": "El idioma comun para dibujar los planos de VetCare",
        "herramienta": "draw.io · Mermaid",
        "hito_pi": "Queda listo el modelo de dominio de VetCare: el diagrama de clases con Dueno, Mascota, Cita, Veterinario y Atencion.",
        "entregable": "Diagrama de clases de VetCare hecho en draw.io, exportado a PNG y al archivo .drawio, con 5 clases, atributos tipados, metodos propios y 4 asociaciones con multiplicidad y nombre de rol, subido a ExamLab.",
        "demo": "El docente dibuja en vivo Dueno, Mascota y Cita en draw.io y borra tres atributos mal ubicados explicando a que clase pertenecen de verdad.",
        "teoria": [
            "UML significa Lenguaje Unificado de Modelado y nacio en los anos noventa para resolver un problema muy concreto: tres personas leian la misma frase en espanol y entendian tres sistemas distintos. Es un lenguaje grafico estandarizado, no un lenguaje de programacion y no una herramienta; usted puede dibujar UML valido en draw.io, en Mermaid o en el tablero con marcador, porque lo que esta normalizado es el significado de las cajas, las lineas y los numeros, no el programa donde se pintan. La especificacion tiene catorce tipos de diagrama, pero en la vida real de un analista se usan cuatro o cinco de forma constante y los demas se consultan cuando se necesitan; querer aprender los catorce es la manera mas rapida de no aprender ninguno. En VetCare, la frase un dueno puede tener varias mascotas parece clarisima hasta que alguien pregunta si una mascota puede tener dos duenos, si el dueno existe antes de registrar la mascota o si al borrar el dueno desaparece la mascota; el diagrama contesta esas tres preguntas con dos numeros y una linea, y ahi es donde UML se gana el sueldo.",
            "Los diagramas se agrupan en dos grandes vistas. La vista estructural muestra de que esta hecho el sistema y no cambia con el tiempo: diagrama de clases, de objetos, de componentes y de despliegue. La vista de comportamiento muestra que pasa y en que orden: casos de uso, actividades, secuencia y maquina de estados. Un mismo sistema necesita las dos, igual que una casa necesita el plano de plantas y tambien el plano de instalaciones. En la practica profesional los que sobreviven son cinco: casos de uso para acordar el alcance con el cliente, clases para el modelo del dominio, secuencia para entender un flujo complicado paso a paso, actividades para procesos de negocio con decisiones, y despliegue cuando hay que explicar donde vive cada cosa. En VetCare vamos a usar clases hoy, casos de uso y secuencia mas adelante, y el resto se menciona para que sepan que existen. Aclaracion importante: los diagramas no reemplazan el documento de requisitos, lo dibujan; cada clase que aparezca hoy debe poder rastrearse a un RF o a una historia del backlog.",
            "El diagrama de clases se dibuja con una caja de tres compartimentos: arriba el nombre de la clase en singular y con mayuscula inicial (Mascota, no mascotas), en el medio los atributos y abajo los metodos. Un atributo se escribe con visibilidad, nombre y tipo, por ejemplo -nombre: String o -fechaNacimiento: Date, donde el guion significa privado y el mas significa publico. Un metodo se escribe con su firma y su tipo de retorno, por ejemplo +calcularEdad(): int. Aqui hay que distinguir dos cosas que los estudiantes mezclan: el modelo de dominio, que solo tiene los conceptos del negocio y sus datos, y el modelo de diseno, que ya incluye clases tecnicas como controladores o repositorios. Hoy hacemos modelo de dominio, asi que en VetCare no aparece ninguna clase llamada MascotaDAO ni ConexionBD: aparecen Dueno, Mascota, Cita, Veterinario y Atencion, que son las cosas de las que habla el Dr. Ramirez cuando cuenta como funciona la clinica. Los metodos, en el modelo de dominio, son solo los que pertenecen naturalmente al concepto, como calcularEdad en Mascota.",
            "Las lineas entre clases son la mitad del valor del diagrama. Una asociacion es una relacion estable entre dos conceptos y se dibuja con una linea recta, un nombre que se lee como frase (Dueno tiene Mascota) y, en cada extremo, una multiplicidad que responde cuantos: 1 exactamente uno, 0..1 opcional, 1..* uno o mas, 0..* cero o mas. En VetCare, Dueno 1 --- 0..* Mascota se lee un dueno puede tener cero o mas mascotas y una mascota pertenece a exactamente un dueno; ese 1 del lado del dueno es una decision de negocio que hay que confirmar con el cliente, no una suposicion. Cita relaciona a Mascota y a Veterinario, cada cita con exactamente una mascota y un veterinario, y cada veterinario con muchas citas. La composicion (rombo relleno) se usa cuando la parte no vive sin el todo: en VetCare las Atenciones de una Mascota son parte de su historia clinica y no tienen sentido si se elimina la ficha de la mascota. La agregacion (rombo vacio) se usa cuando la parte sobrevive por su cuenta, como un Veterinario que pertenece a una Sede pero sigue existiendo si la sede cierra. La herencia (triangulo) solo cuando hay un es-un verdadero, por ejemplo Persona con Dueno y Veterinario como especializaciones, decision que solo vale la pena si comparten varios atributos.",
            "El diagrama que dibujamos hoy no se queda en la clase: es la pieza que viaja mas lejos del Proyecto Integrador. De cada clase salen los campos del diccionario de datos y, mas adelante, las tablas de la base de datos: la clase Mascota con sus atributos se convierte en la tabla mascota, la asociacion 1 a 0..* se convierte en una llave foranea, y las multiplicidades muchos a muchos se convierten en una tabla intermedia. Para quien cursa tambien Programacion II, este diagrama es el mapa que le dice que clases crear y que atributos poner; para quien solo cursa Programacion II, es lo que recibe ya hecho y debe respetar; y para quien solo cursa Seminario, es el corazon del documento de diseno que se entrega al final junto con el prototipo navegable, una ruta completa y perfectamente valida donde el entregable profesional es el plano, no el ladrillo. Por eso el diagrama debe estar limpio: nombres en singular, sin atributos repetidos en dos clases, sin lineas sueltas y sin cajas que no correspondan a ningun requisito.",
            "Error tipico del docente que no domina el tema: calificar el diagrama de clases por lo bonito y por el numero de cajas, sin leer una sola linea en voz alta. El docente que no domina UML deja pasar clases en plural o con nombres de tabla (tbl_mascotas), acepta atributos sin tipo, permite que la fecha de la cita este como atributo dentro de Mascota (con lo cual cada mascota solo podria tener una cita en toda su vida), no exige multiplicidades porque le parecen un detalle, y confunde asociacion con herencia poniendo un triangulo entre Dueno y Mascota como si una mascota fuera un tipo de dueno. Tambien es comun que llene el modelo de dominio de clases tecnicas como Login, Menu o Conexion, que no son conceptos del negocio de la clinica. El antidoto es una regla de sala: cada relacion se lee en voz alta como frase completa con sus dos multiplicidades, un dueno tiene cero o mas mascotas y una mascota pertenece a un dueno; si la frase suena absurda en la clinica Huellitas, el diagrama esta mal, por mas ordenado que se vea."
        ],
        "taller": [
            "Paso 1: subraye en el catalogo de requisitos y en el backlog los sustantivos del negocio de VetCare y arme la lista de clases candidatas, descartando las que sean pantallas, reportes o cosas tecnicas.",
            "Paso 2: dibuje en draw.io las cinco clases Dueno, Mascota, Cita, Veterinario y Atencion con la caja de tres compartimentos, en singular y con mayuscula inicial.",
            "Paso 3: coloque minimo cuatro atributos por clase con visibilidad y tipo (por ejemplo -documento: String, -fechaNacimiento: Date) verificando que ningun atributo este repetido en dos clases distintas.",
            "Paso 4: agregue al menos un metodo propio del dominio por clase (por ejemplo +calcularEdad(): int en Mascota, +reprogramar(nuevaFecha: Date) en Cita) y descarte metodos tecnicos como conectarBD o guardarEnDisco.",
            "Paso 5: trace las cuatro asociaciones con nombre de relacion y multiplicidad en ambos extremos, leala cada una en voz alta como frase completa, exporte a PNG y .drawio y suba ambos archivos a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ este diagrama de clases es el plano maestro de VetCare: de el salen el diccionario de datos, las tablas de la base de datos y las clases que se programan en Programacion II.",
            "Es el primer artefacto del curso que se lee igual en Cali, en Bogota o en Berlin, porque UML es un estandar y no una convencion del salon.",
            "Si una clase no puede rastrearse a un requisito o a una historia del backlog, sobra; y si un requisito no tiene donde vivir en el diagrama, falta una clase."
        ],
        "escenario": [
            "Ya existen el catalogo de RF/RNF y el backlog de historias de VetCare, ambos escritos en texto y sin ninguna representacion grafica.",
            "Nadie ha definido todavia que conceptos del negocio existen, que datos guarda cada uno ni como se relacionan entre si.",
            "El equipo discute en palabras si una mascota puede tener dos duenos y si la cita pertenece a la mascota o al veterinario, y esa discusion no se cierra hablando."
        ],
        "criterios": [
            "El diagrama tiene las 5 clases del dominio en singular, con mayuscula inicial y sin clases tecnicas (nada de DAO, Conexion, Login o Menu).",
            "Cada clase tiene minimo 4 atributos con visibilidad y tipo, y ningun atributo aparece duplicado en dos clases.",
            "Las 4 asociaciones tienen nombre de relacion y multiplicidad explicita en ambos extremos.",
            "Cada relacion se puede leer en voz alta como una frase verdadera del negocio de la clinica Huellitas, y cada clase se rastrea a un RF o a una historia."
        ],
        "pistas": [
            "Si leo esta relacion en voz alta con sus dos multiplicidades, la frase resultante es cierta en la clinica Huellitas o suena absurda?",
            "Este atributo pertenece de verdad al concepto donde lo puse, o lo puse ahi solo porque en la pantalla aparecen juntos?",
            "Esta caja es un concepto del negocio del que habla el veterinario, o es una pantalla, un reporte o algo tecnico que se me colo?"
        ],
        "solucion_pasos": [
            "Paso 1 resuelto: los sustantivos que sobreviven son dueno, mascota, cita, veterinario y atencion; se descartan reporte mensual (es una salida, no un concepto), login y buscador (son pantallas) y base de datos (es tecnologia).",
            "Paso 2 resuelto: quedan cinco cajas de tres compartimentos, todas en singular y con mayuscula inicial: Dueno, Mascota, Veterinario, Cita y Atencion. Se corrigen en el tablero los nombres Mascotas, tbl_duenos y CitaForm que siempre aparecen en los primeros intentos.",
            "Paso 3 resuelto: Dueno con -documento: String, -nombre: String, -telefono: String, -direccion: String; Mascota con -codigo: String, -nombre: String, -especie: String, -raza: String, -fechaNacimiento: Date; Veterinario con -tarjetaProfesional: String, -nombre: String, -especialidad: String, -telefono: String; Cita con -numero: int, -fechaHora: DateTime, -motivo: String, -estado: String; Atencion con -fecha: Date, -diagnostico: String, -tratamiento: String, -observaciones: String. Se verifica que el nombre del dueno no se repita dentro de Mascota y que la especialidad no aparezca en Cita.",
            "Paso 4 resuelto: Mascota +calcularEdad(): int; Cita +reprogramar(nuevaFecha: DateTime): void y +cancelar(motivo: String): void; Dueno +registrarMascota(m: Mascota): void; Veterinario +agendaDelDia(f: Date): List; Atencion +resumen(): String. Se eliminan del tablero los metodos conectarBD, guardar y abrirVentana que proponen siempre los estudiantes, porque no son responsabilidades del concepto sino de la tecnologia.",
            "Paso 5 resuelto: las asociaciones quedan Dueno 1 --- 0..* Mascota (es dueno de), Mascota 1 --- 0..* Cita (tiene agendada), Veterinario 1 --- 0..* Cita (atiende) y Cita 1 --- 0..1 Atencion (genera, porque una cita cancelada no genera atencion). Cada una se lee en voz alta antes de exportar: 'un dueno puede tener cero o mas mascotas y una mascota pertenece a un unico dueno'. Verificacion final con el cliente: se confirma con el Dr. Ramirez que en esta version una mascota pertenece a un solo dueno (regla de negocio RN-02), lo cual justifica el 1 en ese extremo y evita la tabla intermedia que si tocaria si fuera 0..* en ambos lados."
        ],
        "solucion_rubrica": [
            "Clases del dominio correctas, en singular y sin clases tecnicas (3)",
            "Atributos con visibilidad y tipo, sin duplicados entre clases (3)",
            "Asociaciones con multiplicidad y nombre de relacion en las cuatro lineas (3)",
            "Metodos propios del dominio y trazabilidad de cada clase a un RF o historia (1)"
        ],
        "solucion_errores": [
            "Poner fechaCita como atributo dentro de Mascota: con eso cada mascota tendria una sola cita en toda su vida; la cita es una clase aparte relacionada 1 a muchos.",
            "Nombrar las clases en plural o como tablas (Mascotas, tbl_duenos) y dejar atributos sin tipo, con lo cual el diagrama deja de servir para derivar el diccionario de datos.",
            "Usar el triangulo de herencia entre Dueno y Mascota o entre Cita y Veterinario, cuando ahi no hay ningun es-un sino una simple asociacion."
        ],
        "codigo_slide_titulo": "Modelo de dominio de VetCare en sintaxis Mermaid (diagrama, no codigo)",
        "codigo_slide_lineas": [
            "classDiagram",
            "  class Dueno {",
            "    -documento: String",
            "    -nombre: String",
            "    +registrarMascota(m: Mascota): void",
            "  }",
            "  class Mascota {",
            "    -codigo: String",
            "    -especie: String",
            "    -fechaNacimiento: Date",
            "    +calcularEdad(): int",
            "  }",
            "  class Veterinario {",
            "    -tarjetaProfesional: String",
            "    -especialidad: String",
            "  }",
            "  class Cita {",
            "    -fechaHora: DateTime",
            "    -estado: String",
            "    +reprogramar(nuevaFecha: DateTime): void",
            "  }",
            "  class Atencion {",
            "    -diagnostico: String",
            "    -tratamiento: String",
            "  }",
            "  Dueno \"1\" --> \"0..*\" Mascota : es dueno de",
            "  Mascota \"1\" --> \"0..*\" Cita : tiene agendada",
            "  Veterinario \"1\" --> \"0..*\" Cita : atiende",
            "  Cita \"1\" --> \"0..1\" Atencion : genera"
        ],
        "codigo_slide_caption": "Las multiplicidades son las que contestan las preguntas que el espanol deja abiertas: un dueno, muchas mascotas.",
        "artefacto_archivo": "Diagrama-Clases-VetCare.md",
        "artefacto_contenido": "# VetCare - Modelo de dominio (diagrama de clases)\n\nProyecto Integrador: Clinica Veterinaria Huellitas.\nAsignatura: Seminario de Sistemas. Herramientas: draw.io o Mermaid. Entrega: ExamLab.\n\n---\n\n## 1. Notacion minima que se exige\n\n| Elemento | Como se escribe | Ejemplo VetCare |\n|---|---|---|\n| Clase | Sustantivo en singular, mayuscula inicial | Mascota |\n| Atributo | visibilidad nombre: Tipo | -fechaNacimiento: Date |\n| Metodo | visibilidad nombre(param): Retorno | +calcularEdad(): int |\n| Visibilidad | - privado, + publico, # protegido | -documento: String |\n| Asociacion | linea con nombre de relacion | Dueno es dueno de Mascota |\n| Multiplicidad | 1 / 0..1 / 1..* / 0..* | Dueno 1 --- 0..* Mascota |\n| Composicion | rombo relleno (la parte no vive sin el todo) | Mascota contiene sus Atenciones (historia clinica) |\n| Agregacion | rombo vacio (la parte sobrevive sola) | Sede agrupa Veterinarios |\n| Herencia | triangulo (solo si hay un 'es-un' real) | Persona <|-- Veterinario |\n\n---\n\n## 2. Clases del dominio VetCare\n\n### Dueno\n- -documento: String\n- -nombre: String\n- -telefono: String\n- -direccion: String\n- +registrarMascota(m: Mascota): void\n\n### Mascota\n- -codigo: String\n- -nombre: String\n- -especie: String\n- -raza: String\n- -fechaNacimiento: Date\n- +calcularEdad(): int\n\n### Veterinario\n- -tarjetaProfesional: String\n- -nombre: String\n- -especialidad: String\n- +agendaDelDia(f: Date): List\n\n### Cita\n- -numero: int\n- -fechaHora: DateTime\n- -motivo: String\n- -estado: String\n- +reprogramar(nuevaFecha: DateTime): void\n- +cancelar(motivo: String): void\n\n### Atencion\n- -fecha: Date\n- -diagnostico: String\n- -tratamiento: String\n- -observaciones: String\n- +resumen(): String\n\n---\n\n## 3. Relaciones (leer en voz alta antes de aprobar)\n\n| Origen | Mult. | Destino | Mult. | Se lee |\n|---|---|---|---|---|\n| Dueno | 1 | Mascota | 0..* | Un dueno puede tener cero o mas mascotas; una mascota pertenece a un unico dueno |\n| Mascota | 1 | Cita | 0..* | Una mascota puede tener muchas citas; cada cita es de una sola mascota |\n| Veterinario | 1 | Cita | 0..* | Un veterinario atiende muchas citas; cada cita la atiende un veterinario |\n| Cita | 1 | Atencion | 0..1 | Una cita genera a lo sumo una atencion (si se cancela, ninguna) |\n\n---\n\n## 4. Version en Mermaid (para pegar en el documento)\n\n```mermaid\nclassDiagram\n  class Dueno {\n    -documento: String\n    -nombre: String\n    -telefono: String\n    +registrarMascota(m: Mascota): void\n  }\n  class Mascota {\n    -codigo: String\n    -nombre: String\n    -especie: String\n    -fechaNacimiento: Date\n    +calcularEdad(): int\n  }\n  class Veterinario {\n    -tarjetaProfesional: String\n    -especialidad: String\n    +agendaDelDia(f: Date): List\n  }\n  class Cita {\n    -numero: int\n    -fechaHora: DateTime\n    -estado: String\n    +reprogramar(nuevaFecha: DateTime): void\n  }\n  class Atencion {\n    -fecha: Date\n    -diagnostico: String\n    -tratamiento: String\n  }\n  Dueno \"1\" --> \"0..*\" Mascota : es dueno de\n  Mascota \"1\" --> \"0..*\" Cita : tiene agendada\n  Veterinario \"1\" --> \"0..*\" Cita : atiende\n  Cita \"1\" --> \"0..1\" Atencion : genera\n```\n\n---\n\n## 5. Del diagrama al diccionario de datos (adelanto de la proxima clase)\n\n| Clase | Tabla prevista | Campo | Tipo | Observacion |\n|---|---|---|---|---|\n| Dueno | dueno | documento | VARCHAR(15) | Llave primaria |\n| Mascota | mascota | codigo | VARCHAR(10) | Llave primaria |\n| Mascota | mascota | documento_dueno | VARCHAR(15) | Llave foranea (viene del 1 --- 0..*) |\n| Cita | cita | fecha_hora | DATETIME | No se permiten dos citas del mismo veterinario a la misma hora |\n\n---\n\n## 6. Trazabilidad clase - requisito\n\n| Clase | RF / Historia que la justifica |\n|---|---|\n| Dueno | RF-01 / HU-01 |\n| Mascota | RF-02 / HU-02 |\n| Cita | RF-05 / HU-06 |\n| Atencion | RF-04 / HU-05 |\n| Veterinario | RF-07 / HU-08 |\n\n---\n\n## 7. Checklist antes de subir a ExamLab\n\n- [ ] Clases en singular y sin nombres de tabla ni de pantalla.\n- [ ] Ninguna clase tecnica (DAO, Conexion, Login, Menu, Reporte).\n- [ ] Todos los atributos tienen visibilidad y tipo.\n- [ ] Ningun atributo repetido en dos clases.\n- [ ] Las 4 relaciones tienen nombre y multiplicidad en los dos extremos.\n- [ ] Cada relacion se leyo en voz alta y la frase es verdadera en Huellitas.\n- [ ] Se suben los dos archivos: Diagrama-Clases-VetCare-<apellidos>.png y .drawio\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "Que problema resuelve principalmente UML en un proyecto como VetCare?",
                "opciones": [
                    "A) Permite generar el codigo Java automaticamente sin programar",
                    "B) Da un lenguaje grafico estandar para que todos entiendan lo mismo y elimina la ambiguedad del lenguaje natural",
                    "C) Reemplaza el documento de requisitos y las historias de usuario",
                    "D) Sirve para escoger la base de datos que se va a usar"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Como se lee la relacion Dueno \"1\" --- \"0..*\" Mascota?",
                "opciones": [
                    "A) Una mascota puede tener varios duenos y un dueno tiene una sola mascota",
                    "B) Un dueno puede tener cero o mas mascotas y cada mascota pertenece a un unico dueno",
                    "C) Dueno y Mascota son la misma clase con distinto nombre",
                    "D) Una mascota hereda de dueno"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Cual de estas clases NO pertenece al modelo de dominio de VetCare?",
                "opciones": [
                    "A) Atencion",
                    "B) Veterinario",
                    "C) MascotaDAO",
                    "D) Cita"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Cual de estos diagramas pertenece a la vista de comportamiento?",
                "opciones": [
                    "A) Diagrama de clases",
                    "B) Diagrama de componentes",
                    "C) Diagrama de despliegue",
                    "D) Diagrama de secuencia"
                ],
                "clave": "D"
            },
            {
                "tipo": "vf",
                "q": "En el diagrama de clases, la caja se divide en tres compartimentos: nombre, atributos y metodos.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Poner el atributo fechaCita dentro de la clase Mascota es correcto, porque la cita siempre es de una mascota.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Explique por que la Cita debe modelarse como clase propia en VetCare y no como un atributo de Mascota.",
                "clave": "Porque una mascota puede tener muchas citas a lo largo del tiempo, cada una con su fecha, hora, motivo, estado y veterinario asignado. Si la cita fuera un atributo de Mascota solo se podria guardar una y se perderia el historial de agenda; ademas la cita relaciona a la mascota con un veterinario, y una relacion entre dos conceptos con datos propios exige una clase con sus propias asociaciones y multiplicidades."
            },
            {
                "tipo": "abierta",
                "q": "Como se traduce despues el diagrama de clases al diccionario de datos y a la base de datos de VetCare?",
                "clave": "Cada clase del dominio se convierte en una tabla y cada atributo en un campo con su tipo y su longitud, que es justamente lo que registra el diccionario de datos. Las asociaciones uno a muchos se convierten en llaves foraneas (por ejemplo el documento del dueno viaja como llave foranea a la tabla mascota) y una asociacion muchos a muchos obliga a crear una tabla intermedia. Por eso los tipos y las multiplicidades del diagrama deben quedar bien desde ahora."
            }
        ]
    },
    {
        "n": 9,
        "slug": "Casos de uso",
        "titulo": "Casos de uso",
        "subtitulo": "El diagrama se dibuja en cinco minutos; el valor esta en la especificacion",
        "herramienta": "draw.io · Google Docs",
        "hito_pi": "Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente.",
        "entregable": "Un PDF con el diagrama de casos de uso, la matriz de trazabilidad RF a CU y las dos especificaciones textuales completas (precondiciones, postcondiciones, flujo principal y minimo dos flujos alternos cada una), subido a ExamLab.",
        "demo": "El docente proyecta como un caso de uso mal escrito (Dar clic en guardar) se transforma en uno correcto (Registrar mascota) y luego llena en vivo, delante del grupo, la plantilla de especificacion de Buscar expediente.",
        "teoria": [
            "Un caso de uso es la descripcion de una interaccion completa entre un actor y el sistema que termina entregando un resultado con valor observable para ese actor. La palabra clave es completa: no es una pantalla, no es un boton, no es una tabla de la base de datos y no es un paso intermedio. La prueba practica que usamos en clase es la del almuerzo: si el actor puede levantarse de la silla e irse a almorzar satisfecho porque ya logro lo que queria, entonces eso es un caso de uso. En VetCare, Registrar mascota pasa la prueba, porque la recepcionista de Huellitas termina con la ficha creada y el codigo asignado; en cambio Validar la fecha de nacimiento no la pasa, porque nadie llega a la clinica con el objetivo de validar una fecha. Esa distincion parece un detalle de nombres, pero define el tamaño de todo el modelo: si se confunde, un sistema pequeño como VetCare termina con cuarenta casos de uso inutiles en vez de seis u ocho casos de uso reales. La regla de redaccion es simple y no se negocia: verbo en infinitivo mas objeto del dominio, escrito con las palabras de la clinica y no con palabras de programador.",
            "El actor es un rol, no una persona ni un cargo del organigrama. Doña Marta, la recepcionista de Huellitas, no es un actor: el actor es Recepcionista, y si mañana la reemplazan el modelo no cambia. Una misma persona puede encarnar dos actores, por ejemplo el veterinario dueño de la clinica que a veces atiende y a veces revisa las metricas: alli actua como Veterinario y como Administrador, y por eso aparecen dos monigotes. Ademas existen actores que no son humanos: un sistema externo que enviaria los recordatorios por mensajeria seria un actor secundario de VetCare, porque participaria en el caso de uso pero no es quien lo inicia. Todo esto se ordena con el limite del sistema, ese rectangulo que muchos omiten y que en realidad es la decision de arquitectura mas importante del diagrama: adentro va lo que nosotros vamos a construir y por lo tanto especificar, y afuera queda lo que solo vamos a consumir o a recibir. Si en VetCare dibujamos adentro del rectangulo un caso de uso llamado Enviar mensaje de WhatsApp, estamos diciendo que nosotros construimos la mensajeria, y eso probablemente sea falso y encarezca el proyecto por escrito.",
            "Las relaciones entre casos de uso son tres y se abusa de ellas. Include significa que el caso base siempre ejecuta el caso incluido, y se usa cuando un comportamiento se repite en varios casos y vale la pena escribirlo una sola vez: en VetCare, CU-03 Registrar consulta medica y CU-04 Agendar cita incluyen ambos a Verificar existencia de la mascota, siempre, sin condicion. Extend es lo contrario: comportamiento opcional que se dispara solo si se cumple una condicion en un punto de extension del caso base; en VetCare, CU-02 Buscar expediente puede extenderse con CU-06 Exportar expediente a PDF, que ocurre unicamente cuando el veterinario lo pide. La generalizacion, mucho menos frecuente, sirve cuando un actor especializa a otro, por ejemplo Veterinario especialista como especializacion de Veterinario. El peligro real no es equivocarse en la flecha sino usar include para descomponer funcionalmente: si el diagrama muestra Registrar mascota incluyendo Abrir formulario, incluyendo Digitar datos, incluyendo Guardar en base de datos, ya no es un modelo de casos de uso sino un diagrama de flujo disfrazado, y ese error contagia despues al diagrama de clases.",
            "La especificacion textual es donde vive el noventa por ciento del valor y donde casi nadie invierte tiempo. Un caso de uso especificado tiene ficha de identificacion (ID, nombre, actor primario, requisitos que cubre, prioridad y frecuencia), precondiciones, postcondiciones, flujo principal y flujos alternos, y las reglas de negocio asociadas. El flujo principal se escribe en pares de responsabilidad: una columna dice que hace el actor y la otra que hace el sistema, alternandose, en pasos numerados y sin adjetivos. Por ejemplo, en Buscar expediente el paso 1 es que el veterinario digita el codigo o el nombre de la mascota y el paso 2 es que el sistema devuelve la lista de coincidencias; nunca se escribe el sistema es rapido y amigable, porque eso no es un paso sino un requisito no funcional que ya vive en otro documento, el RNF-02, que exige mostrar el resultado en menos de tres segundos. Los flujos alternos se numeran respecto al paso donde se desvian: 2a cuando no hay coincidencias, 2b cuando hay demasiadas, 4a cuando la mascota esta inactiva. Ese numerito es lo que permite que el compañero de Programacion II sepa exactamente en que punto del comportamiento hay que preguntar algo, y es tambien la razon por la cual la clinica Huellitas deja de perder tiempo buscando historiales.",
            "Precondiciones y postcondiciones son un contrato, no un adorno. La precondicion es aquello que debe ser verdadero antes de empezar y que el caso de uso no vuelve a verificar dentro del flujo: si escribimos que el usuario esta autenticado como precondicion de Registrar mascota, entonces el flujo principal no puede tener un paso que diga el sistema pide usuario y contraseña, porque eso ya ocurrio. La postcondicion describe el estado en que queda el sistema cuando el caso termina, y debe ser verificable mirando los datos: en VetCare la postcondicion de exito de Registrar mascota es que existe una ficha con codigo unico asociada a un propietario y que quedo bitacora de quien la creo y cuando; la postcondicion de fracaso es que no queda ningun registro a medias. Escribirlas asi tiene dos consecuencias practicas enormes. Primero, cada postcondicion se convierte casi automaticamente en un caso de prueba, porque describe algo que se puede ir a comprobar. Segundo, resuelve la discusion entre los tres casos de matricula: el estudiante que solo cursa Seminario cierra con este documento y su prototipo navegable y ya entrego un producto completo, mientras que el que solo cursa Programacion II recibe estas postcondiciones y sabe exactamente que debe dejar guardado su codigo, sin tener que adivinar ni volver a entrevistar a la clinica.",
            "Error tipico del docente que no domina el tema: dibujar los monigotes, las elipses y el rectangulo, sentirse satisfecho y dar por terminado el tema de casos de uso, cuando en realidad apenas hizo la portada. De ese error nacen los otros cuatro que veremos en los talleres. Uno, convertir cada operacion CRUD y cada boton en un caso de uso, de modo que VetCare aparece con Ingresar usuario, Validar contraseña, Mostrar mensaje de error y Cerrar ventana como si fueran objetivos de negocio. Dos, usar include como si fuera una flecha de orden de pantallas, cuando include no dice nada sobre el orden en el tiempo, para eso existe el diagrama de secuencia que veremos en la clase doce. Tres, dejar las precondiciones en blanco o llenarlas con frases vacias como el sistema debe estar funcionando, que no restringe nada. Y cuatro, no escribir flujos alternos, que es el mas caro de todos, porque los flujos alternos son precisamente lo que la clinica Huellitas vive a diario: el propietario que no esta registrado, la mascota que aparece dos veces, la busqueda que no devuelve nada. Si el docente no exige alternos, el estudiante entrega un sistema que solo funciona el dia perfecto que nunca existe."
        ],
        "taller": [
            "En draw.io, dibujar el limite del sistema rotulado VetCare y ubicar afuera los actores como roles (Recepcionista, Veterinario, Administrador y el servicio externo de mensajeria como actor secundario candidato, que hoy todavia no se conecta a ningun caso de uso); ningun actor puede llamarse con nombre propio ni con cargo inventado.",
            "Colocar dentro del limite entre seis y ocho casos de uso derivados del catalogo de RF ya construido, todos redactados como verbo en infinitivo mas objeto del dominio, y borrar de inmediato cualquier elipse que se llame Guardar, Validar, Mostrar o Iniciar pantalla.",
            "Construir en Google Docs la matriz de trazabilidad RF a CU: cada requisito funcional debe apuntar al menos a un caso de uso y cada caso de uso debe nacer de al menos un requisito; marcar en rojo los huerfanos que aparezcan y anotar por escrito la decision que se tomara con cada uno.",
            "Modelar exactamente una relacion include y una relacion extend en el diagrama, y escribir al lado, en una nota de draw.io, una frase que justifique por que una es obligatoria y la otra condicional; si no se puede justificar, se elimina la flecha.",
            "Diligenciar la plantilla completa de especificacion para CU-01 Registrar mascota y CU-02 Buscar expediente, con precondiciones, postcondiciones de exito y de fracaso, flujo principal en pares actor-sistema y minimo dos flujos alternos cada uno; exportar todo a PDF y subirlo a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ los casos de uso son el puente entre lo que pidio la clinica Huellitas y lo que despues alguien va a programar; sin ellos, el equipo de Programacion II tiene que adivinar el comportamiento del sistema y siempre adivina distinto.",
            "El estudiante que solo cursa Seminario cierra el semestre con este paquete de especificaciones como pieza central de su documento de diseño, y por eso hoy se califica la escritura y no el dibujo.",
            "Toda especificacion escrita hoy se convierte mañana en un caso de prueba: si una postcondicion no se puede ir a verificar en los datos, esta mal redactada."
        ],
        "escenario": [
            "Ya existe el catalogo de RF y RNF de VetCare, pero esta redactado como lista de deseos y nadie sabe en que orden ocurren las cosas ni que pasa cuando algo sale mal.",
            "La recepcionista de Huellitas describe su trabajo con frases sueltas: busco la carpeta, si no aparece le pregunto al veterinario, si el propietario es nuevo lleno una hoja aparte y la engrapo.",
            "El equipo tiene draw.io abierto y la tentacion de dibujar veinte monigotes antes de escribir una sola linea de comportamiento."
        ],
        "criterios": [
            "El diagrama tiene limite de sistema rotulado, actores como roles y ningun caso de uso con nombre de boton, pantalla u operacion tecnica.",
            "La matriz de trazabilidad no tiene huerfanos sin decision escrita: todo RF llega al menos a un CU o queda documentado como pendiente, y todo CU nace al menos de un RF.",
            "Las dos especificaciones tienen precondicion, postcondicion de exito, postcondicion de fracaso y flujo principal numerado en pares actor-sistema.",
            "Cada especificacion incluye minimo dos flujos alternos numerados respecto al paso del flujo principal donde se desvian."
        ],
        "pistas": [
            "Si un actor se fuera a almorzar justo despues de ejecutar su caso de uso, quedaria satisfecho o le faltaria algo por hacer?",
            "Su flujo principal describe pasos del negocio o describe clics sobre una interfaz que todavia no existe?",
            "Que pasa en Huellitas cuando el propietario no esta registrado, cuando la busqueda no devuelve nada y cuando hay dos mascotas con el mismo nombre? Aparece eso escrito en algun flujo alterno?"
        ],
        "solucion_pasos": [
            "Actores y limite del sistema tal como deben quedar: dentro del rectangulo rotulado VetCare quedan unicamente los casos de uso que el equipo se compromete a especificar. Afuera quedan Recepcionista (actor primario de CU-00 Registrar propietario, CU-01 Registrar mascota y CU-04 Agendar cita), Veterinario (actor primario de CU-02 Buscar expediente y CU-03 Registrar consulta medica), Administrador (actor primario de CU-05 Consultar indicadores de atencion) y el servicio externo de mensajeria, dibujado como actor secundario candidato que hoy no se conecta a ningun caso de uso, porque el RF-07 de recordatorio todavia no tiene comportamiento especificado. Esa deuda se anota al pie del diagrama con una nota que dice: RF-07 sin caso de uso, pendiente de decision. Nombrar la mensajeria como actor externo, y no como caso de uso interno, evita que el equipo se comprometa a construir un servicio de envio de mensajes.",
            "Catalogo de casos de uso y matriz de trazabilidad RF a CU, fila por fila: RF-02 Registrar propietario origina CU-00 Registrar propietario; RF-03 Registrar la ficha de la mascota y RF-04 Registrar los datos basicos de la mascota (especie, raza, fecha de nacimiento y sexo) originan ambos a CU-01 Registrar mascota; RF-05 Consultar el expediente de una mascota, con el RNF-02 de tres segundos asociado, origina CU-02 Buscar expediente; RF-06 Registrar la consulta medica origina CU-03 Registrar consulta medica; RF-08 Agendar cita con un veterinario origina CU-04 Agendar cita; RF-09 Reporte mensual de atenciones origina CU-05 Consultar indicadores de atencion. RF-07 Recordatorio de cita por mensajeria queda marcado en rojo porque no llega a ningun caso de uso: se documenta como huerfano pendiente de decision (construirlo en un CU-07 con la mensajeria como actor secundario, o declararlo fuera del alcance del periodo). Seis filas completas y un huerfano confesado valen mas que ocho filas inventadas.",
            "Relaciones justificadas, exactamente una de cada una: CU-03 Registrar consulta medica y CU-04 Agendar cita incluyen ambos a Verificar existencia de la mascota, porque ninguno de los dos puede ejecutarse sin esa verificacion, siempre, sin condicion; la nota al lado dice: obligatoria, ocurre en el cien por ciento de las ejecuciones. CU-02 Buscar expediente se extiende con CU-06 Exportar expediente a PDF, porque el veterinario a veces lo pide y a veces no; el punto de extension se marca despues del paso 4 del flujo principal, cuando el expediente ya esta desplegado en pantalla, y la nota dice: condicional, solo si el veterinario solicita la exportacion.",
            "Especificacion completa de CU-01 Registrar mascota, tal como debe entregarse. Ficha: ID CU-01, actor primario Recepcionista, actores secundarios ninguno, cubre RF-03 y RF-04, prioridad alta, frecuencia estimada 15 veces al dia. Precondiciones: 1) la recepcionista inicio sesion con su rol; 2) el propietario existe en el sistema o se crea dentro del flujo alterno 2a. Flujo principal: 1) la recepcionista selecciona la opcion Registrar mascota y el sistema muestra el formulario con los campos obligatorios marcados; 2) digita el documento del propietario y el sistema recupera y muestra su nombre y telefono; 3) digita nombre, especie, raza, fecha de nacimiento y sexo y el sistema valida el formato y habilita la accion Guardar; 4) confirma el registro y el sistema genera el codigo unico con formato VC-0000 (por ejemplo VC-0001), guarda la ficha y muestra la confirmacion con el codigo. Flujos alternos: 2a el propietario no existe, el sistema ofrece registrarlo pidiendo documento, nombre, telefono y direccion, y el flujo continua en el paso 3; 3a la fecha de nacimiento es posterior a hoy, el sistema rechaza el dato, marca el campo y no permite continuar hasta corregirlo; 4a ya existe una mascota con el mismo nombre para ese propietario, el sistema advierte y exige confirmacion explicita antes de guardar. Excepcion E1: falla de conexion al guardar, el sistema informa el error, no crea la ficha y conserva el formulario diligenciado. Postcondicion de exito: existe una ficha de mascota con codigo unico asociada a exactamente un propietario y queda bitacora de quien la creo y en que momento. Postcondicion de fracaso: no queda ningun registro parcial y el formulario conserva lo digitado. Reglas de negocio: RN-01 toda mascota tiene exactamente un propietario responsable; RN-02 el codigo de mascota nunca se reutiliza, ni siquiera si la ficha se inactiva.",
            "Especificacion completa de CU-02 Buscar expediente, tal como debe entregarse. Ficha: ID CU-02, actor primario Veterinario, cubre RF-05 y se apoya en RNF-02, prioridad alta, frecuencia estimada 40 veces al dia. Precondiciones: 1) el veterinario esta autenticado; 2) la mascota existe en el sistema. Flujo principal: 1) el veterinario digita el codigo de la mascota, su nombre o el documento del propietario; 2) el sistema devuelve la lista de coincidencias en menos de tres segundos, cumpliendo el RNF-02; 3) el veterinario selecciona una mascota de la lista; 4) el sistema despliega la ficha, el historial de consultas y las vacunas en orden cronologico descendente. Flujos alternos: 2a no hay coincidencias, el sistema informa y ofrece registrar la mascota, pasando a CU-01; 2b hay mas de cincuenta coincidencias, el sistema pagina el resultado y sugiere afinar el filtro con el documento del propietario; 4a la mascota esta inactiva, el sistema despliega el expediente en modo solo lectura y muestra la fecha de inactivacion. Punto de extension: despues del paso 4 puede ejecutarse CU-06 Exportar expediente a PDF. Postcondicion de exito: el expediente queda desplegado, la consulta queda registrada en la bitacora y no se modifica ningun dato clinico. Postcondicion de fracaso: no se despliega ningun expediente y el criterio de busqueda queda disponible para corregirlo."
        ],
        "solucion_rubrica": [
            "Diagrama con limite de sistema, actores como roles y casos de uso bien nombrados (2)",
            "Matriz de trazabilidad RF a CU sin huerfanos ocultos ni casos de uso inventados (2)",
            "Especificacion completa de CU-01 Registrar mascota con pre, post y flujo principal (3)",
            "Especificacion de CU-02 Buscar expediente con minimo dos flujos alternos bien numerados (3)"
        ],
        "solucion_errores": [
            "Convertir el CRUD en casos de uso: entregar Crear mascota, Leer mascota, Actualizar mascota y Eliminar mascota como cuatro elipses, cuando el objetivo real del negocio es Registrar mascota y Actualizar ficha; el resultado es un diagrama de doce elipses que no dice nada del trabajo de la clinica.",
            "Escribir el flujo principal como secuencia de clics (el usuario da clic en el boton azul, luego da clic en Aceptar), lo cual amarra el diseño a una interfaz que todavia no existe y obliga a reescribir la especificacion apenas cambie el mockup.",
            "Dejar los flujos alternos vacios o con una sola linea del tipo si hay error el sistema avisa; en VetCare eso significa que nadie definio que pasa cuando el propietario es nuevo, cuando hay homonimos o cuando la busqueda no devuelve resultados, que es exactamente el problema que hoy tiene Huellitas en papel."
        ],
        "codigo_slide_titulo": "CU-02 Buscar expediente: la especificacion que el diagrama no muestra",
        "codigo_slide_lineas": [
            "CU-02  Buscar expediente",
            "Actor primario: Veterinario  |  Prioridad: Alta  |  Cubre: RF-05, RNF-02",
            "Precondicion: el veterinario esta autenticado y la mascota existe en el sistema.",
            "Postcondicion (exito): el expediente queda desplegado y la consulta queda en bitacora; no se modifica ningun dato clinico.",
            "Flujo principal:",
            "  1. El veterinario digita codigo, nombre de mascota o documento del propietario.",
            "  2. El sistema devuelve la lista de coincidencias en menos de 3 segundos (RNF-02).",
            "  3. El veterinario selecciona una mascota de la lista.",
            "  4. El sistema muestra ficha, historial de consultas y vacunas en orden cronologico.",
            "Flujos alternos:",
            "  2a. Sin coincidencias: el sistema informa y ofrece registrar la mascota (pasa a CU-01).",
            "  2b. Mas de 50 coincidencias: el sistema pagina el resultado y sugiere afinar el filtro.",
            "  4a. La mascota esta inactiva: el sistema muestra el expediente en modo solo lectura.",
            "Punto de extension: despues del paso 4 puede ejecutarse CU-06 Exportar expediente a PDF."
        ],
        "codigo_slide_caption": "El diagrama solo dice que existe Buscar expediente; unicamente la especificacion dice que hace el sistema cuando no hay coincidencias.",
        "artefacto_archivo": "CU-VetCare-Especificacion.md",
        "artefacto_contenido": "# Plantilla de especificacion de casos de uso - VetCare (Clinica Huellitas)\n\n> Regla de oro: el diagrama muestra QUE hace el sistema; esta plantilla explica COMO se comporta paso a paso. Sin la plantilla diligenciada, el caso de uso NO esta hecho.\n\n## 1. Ficha de identificacion\n\n| Campo | Contenido |\n|---|---|\n| ID | CU-01 |\n| Nombre | Registrar mascota |\n| Actor primario | Recepcionista |\n| Actores secundarios | Ninguno |\n| Requisitos que cubre | RF-03, RF-04 |\n| Frecuencia estimada | 15 veces al dia |\n| Prioridad | Alta |\n\n## 2. Precondiciones\n\n1. El usuario inicio sesion con rol Recepcionista.\n2. El propietario ya existe en el sistema, o se registra dentro del flujo alterno 2a.\n\n## 3. Postcondiciones\n\n- Exito: queda creada una ficha de mascota con codigo unico de formato VC-0000 (por ejemplo VC-0001) asociada a un propietario, y queda registrado en la bitacora quien la creo y en que momento.\n- Fracaso: no se crea ningun registro parcial; el sistema conserva los datos digitados para que el usuario corrija.\n\n## 4. Flujo principal (camino feliz)\n\n| Paso | Actor | Sistema |\n|---|---|---|\n| 1 | Selecciona la opcion Registrar mascota | Muestra el formulario con los campos obligatorios marcados |\n| 2 | Digita el documento del propietario | Busca y muestra nombre y telefono del propietario |\n| 3 | Digita nombre, especie, raza, fecha de nacimiento y sexo | Valida formato y habilita la accion Guardar |\n| 4 | Confirma el registro | Genera el codigo de mascota, guarda la ficha y muestra la confirmacion con el codigo |\n\n## 5. Flujos alternos\n\n- 2a. El propietario no existe: el sistema ofrece registrarlo; se capturan documento, nombre, telefono y direccion; el flujo continua en el paso 3.\n- 3a. La fecha de nacimiento es posterior a hoy: el sistema rechaza el dato, marca el campo y no permite continuar hasta corregirlo.\n- 4a. Ya existe una mascota con el mismo nombre para ese propietario: el sistema advierte y exige confirmacion explicita antes de guardar.\n\n## 6. Excepciones\n\n- E1. Falla de conexion al guardar: el sistema informa el error, no crea la ficha y conserva el formulario diligenciado.\n\n## 7. Reglas de negocio asociadas\n\n- RN-01: toda mascota debe tener exactamente un propietario responsable.\n- RN-02: el codigo de mascota nunca se reutiliza, ni siquiera si la ficha se inactiva.\n\n## 8. Matriz de trazabilidad\n\n| RF | Caso de uso | Mockup | Clases implicadas |\n|---|---|---|---|\n| RF-02 | CU-00 Registrar propietario | M-01 Formulario de propietario | Propietario |\n| RF-03, RF-04 | CU-01 Registrar mascota | M-02 Formulario de mascota | Mascota, Propietario |\n| RF-05 | CU-02 Buscar expediente | M-03 Buscador de expedientes | Mascota, Consulta |\n| RF-06 | CU-03 Registrar consulta medica | M-05 Ficha de consulta | Consulta, Veterinario |\n| RF-08 | CU-04 Agendar cita | M-04 Agenda | Cita, Veterinario |\n| RF-07 | (todavia sin caso de uso: HUERFANO) | -- | -- |\n\n## 9. Checklist antes de entregar en ExamLab\n\n- [ ] Cada caso de uso se llama verbo en infinitivo + objeto del dominio.\n- [ ] Ningun caso de uso se llama Guardar, Validar, Mostrar pantalla o Dar clic.\n- [ ] Todo caso de uso del diagrama tiene al menos un RF que lo origina.\n- [ ] Todo RF llega a un caso de uso o queda registrado por escrito como huerfano pendiente de decision.\n- [ ] Cada especificacion tiene minimo dos flujos alternos numerados.\n- [ ] Las postcondiciones se pueden verificar mirando el estado del sistema.\n- [ ] El limite del sistema esta dibujado y rotulado VetCare.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "Cual de los siguientes es un caso de uso valido para VetCare?",
                "opciones": [
                    "A) Validar el campo especie",
                    "B) Registrar mascota",
                    "C) Tabla mascota",
                    "D) Dar clic en el boton Guardar"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Para que sirve el limite del sistema (el rectangulo) en un diagrama de casos de uso?",
                "opciones": [
                    "A) Para decorar el diagrama y que se vea ordenado",
                    "B) Para separar lo que el equipo va a construir de lo que solo se consume desde afuera",
                    "C) Para indicar el orden en que ocurren los casos de uso",
                    "D) Para agrupar las clases del diagrama de clases"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "En VetCare, despues de mostrar el expediente el veterinario a veces pide exportarlo a PDF y a veces no. Que relacion corresponde entre Buscar expediente y Exportar expediente a PDF?",
                "opciones": [
                    "A) include, porque la exportacion forma parte de la busqueda",
                    "B) extend, porque la exportacion es opcional y depende de una condicion",
                    "C) generalizacion, porque exportar es un tipo de busqueda",
                    "D) asociacion entre actores, porque intervienen dos roles"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Que parte de la especificacion describe el estado en que queda el sistema cuando el caso de uso termina bien?",
                "opciones": [
                    "A) La precondicion, porque describe el estado inicial requerido",
                    "B) La postcondicion de exito, porque describe el estado final verificable",
                    "C) El flujo alterno, porque describe las desviaciones del camino feliz",
                    "D) La regla de negocio, porque restringe los datos del dominio"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Un actor siempre representa a una persona concreta de la clinica Huellitas.",
                "clave": "F"
            },
            {
                "tipo": "vf",
                "q": "Los flujos alternos se numeran respecto al paso del flujo principal en el que se produce la desviacion, por ejemplo 2a o 4a.",
                "clave": "V"
            },
            {
                "tipo": "abierta",
                "q": "Escriba la precondicion y la postcondicion de exito del caso de uso CU-02 Buscar expediente de VetCare.",
                "clave": "Precondicion: el veterinario esta autenticado y la mascota existe en el sistema. Postcondicion de exito: el expediente queda desplegado con ficha, historial de consultas y vacunas en orden cronologico, la consulta queda registrada en la bitacora y no se modifica ningun dato clinico."
            },
            {
                "tipo": "abierta",
                "q": "Un compañero afirma que con el diagrama de monigotes y elipses ya quedo documentado el sistema VetCare. Que le responde usted y que le hace falta?",
                "clave": "Que el diagrama es apenas el indice: muestra que casos de uso existen pero no como se comportan. Falta la especificacion textual de cada uno con ficha de identificacion, precondiciones, postcondiciones de exito y de fracaso, flujo principal en pares actor-sistema, flujos alternos numerados y reglas de negocio; sin eso quien programe en Programacion II tiene que adivinar que pasa cuando el propietario no existe, cuando hay homonimos o cuando la busqueda no devuelve resultados. Ademas falta la matriz de trazabilidad que demuestre que cada caso de uso nace de un requisito de la clinica Huellitas."
            }
        ]
    },
    {
        "n": 10,
        "slug": "Parcial 2",
        "titulo": "Parcial 2",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    },
    {
        "n": 11,
        "slug": "Avance del proyecto integrador",
        "titulo": "Avance del proyecto integrador",
        "subtitulo": "Hoy no se agrega nada nuevo: se verifica que todos los documentos hablen del mismo sistema",
        "herramienta": "Google Docs · draw.io",
        "hito_pi": "El paquete de diseño de VetCare queda auditado y consistente: requisitos, casos de uso y diagrama de clases usan los mismos nombres y no se contradicen entre si.",
        "entregable": "Un documento con la matriz de trazabilidad RF a CU a Clase, el glosario de nombres canonicos, el acta de revision entre pares con hallazgos clasificados por severidad y el backlog priorizado de correcciones, subido a ExamLab.",
        "demo": "El docente proyecta el paquete de un equipo ficticio de VetCare y encuentra en vivo tres inconsistencias: un RF sin caso de uso, una clase llamada Dueño que en el catalogo de requisitos se llama Propietario, y un caso de uso que ninguna clase puede soportar.",
        "teoria": [
            "Un paquete de diseño no es una carpeta de archivos sueltos: es un sistema de documentos que deben decir lo mismo con las mismas palabras. El problema es que esos documentos se escribieron en semanas distintas, muchas veces por personas distintas del equipo, y cada semana el entendimiento del dominio cambio un poquito. Asi es como en VetCare aparece un requisito RF-07 que promete recordatorio de cita por mensajeria, un diagrama de casos de uso donde no existe ningun caso de uso de recordatorio, y un diagrama de clases donde no hay nada parecido a una clase Notificacion. Ninguno de los tres documentos esta mal por si solo; lo que esta mal es el conjunto. Un defecto de consistencia cuesta poco corregirlo hoy, en una hoja, y cuesta carisimo corregirlo cuando ya se construyo sobre el, porque para entonces hay pantallas, tablas y codigo apoyados en la contradiccion. Por eso esta sesion no agrega tema nuevo: agrega confianza en lo que ya existe, que es un trabajo de arquitecto tan legitimo como dibujar.",
            "La herramienta central para eso es la trazabilidad, y se verifica en dos direcciones. Hacia adelante se pregunta si todo requisito funcional llega a algun caso de uso y si ese caso de uso llega a alguna clase, atributo u operacion que lo soporte; si un RF no llega a nada, es un requisito huerfano y significa que el equipo prometio algo que el diseño no cumple. Hacia atras se pregunta si todo elemento del diseño nace de algun requisito; si un caso de uso o una clase no viene de ningun RF, es un elemento viudo y casi siempre significa que alguien agrego funcionalidad por gusto propio o que la fila de la matriz quedo sin diligenciar. En VetCare esto se vuelve concreto rapidisimo: RF-05, consultar el expediente de una mascota, junto con el RNF-02 que exige que el resultado aparezca en menos de tres segundos, debe llegar a CU-02 Buscar expediente y de ahi a las clases Mascota y Consulta, con una operacion de busqueda por codigo o por nombre; si ese camino se rompe en cualquier punto, el problema numero dos de la clinica Huellitas sigue sin resolverse aunque el equipo tenga veinte paginas escritas. La matriz de trazabilidad es apenas una tabla de cuatro columnas, pero es la unica prueba objetiva de que el paquete es coherente.",
            "El segundo eje de la auditoria es el lenguaje. Un sistema se diseña bien cuando existe un solo nombre para cada concepto y todos lo usan, desde la entrevista con la clinica hasta el nombre de la clase. Cuando en un documento se lee Dueño, en otro Propietario, en otro Cliente y en el mockup Responsable, no hay cuatro sinonimos: hay cuatro oportunidades de que alguien crea que son cuatro cosas distintas y termine con cuatro tablas. La solucion es un glosario canonico donde cada concepto de VetCare tiene un nombre unico, una definicion de una linea y una lista explicita de sinonimos prohibidos. Ese glosario manda sobre todos los artefactos: si el nombre canonico es Propietario, entonces el requisito, el caso de uso, el mockup, el diccionario de datos y la clase se llaman Propietario, sin excepciones y sin diminutivos. El glosario tambien separa parejas peligrosas: en Huellitas, Cita es la reserva de un horario futuro y Consulta es el registro de una atencion ya realizada, y confundirlas produce un modelo donde nadie sabe si se esta agendando o atendiendo. La ganancia es inmediata para el compañero que solo cursa Programacion II, porque puede buscar una palabra en el documento y encontrarla en todos lados; y tambien para el que solo cursa Seminario, porque su documento de diseño se lee como un texto y no como un rompecabezas.",
            "La revision entre pares se hace con reglas o no sirve. Se revisa el artefacto, nunca a la persona, y para eso se asignan tres roles: el autor, que entrega su paquete y permanece en silencio mientras lo revisan; el revisor, que recorre la rubrica punto por punto y solo reporta hechos observables; y el moderador, que controla el tiempo y escribe los hallazgos. Cada hallazgo se anota con ubicacion exacta, descripcion de la inconsistencia y severidad: bloqueante cuando impide construir el sistema, mayor cuando obliga a rehacer un artefacto completo, menor cuando es cosmetico. Prohibido discutir la solucion durante la revision, porque ahi es donde se van los cuarenta minutos y no se revisa nada. En VetCare, un hallazgo bien escrito se ve asi: en el diagrama de clases, la clase Consulta no tiene relacion con Veterinario, pero el flujo principal de CU-03 dice que toda consulta queda a nombre del veterinario que atendio; severidad mayor. Eso es util. En cambio esta mal hecho, no me gusta o le falta orden no es un hallazgo, es una opinion.",
            "Todo lo que se encuentra se convierte en backlog de deuda de diseño, no en angustia. Cada hallazgo pasa a ser un item con responsable, severidad, criterio de cierre verificable y un estado que puede ser aceptado, rechazado con justificacion escrita o aplazado por acuerdo. Rechazar un hallazgo es legitimo si se argumenta, y aprender a hacerlo es parte del oficio del analista. Sobre ese backlog se define lo que en la industria se llama definicion de terminado del paquete de diseño de VetCare: catalogo de RF y RNF numerado y sin huerfanos, diagrama y especificaciones de casos de uso, diagrama de clases con multiplicidades, mockups de las pantallas criticas y diccionario de datos. Aqui es donde los tres casos de matricula se hacen visibles y conviene decirlo en voz alta en el aula: el que cursa las dos materias entrega estos planos aca y el codigo alla; el que solo cursa Programacion II recibe este paquete y todo lo que hoy quede ambiguo lo va a pagar en horas de reproceso; y el que solo cursa Seminario cierra con este mismo documento mas el prototipo navegable, que es una ruta completa y valida, no una version reducida del curso.",
            "Error tipico del docente que no domina el tema: usar la sesion de avance como una hora libre para que los equipos adelanten lo que les falta, sin producto propio y sin evidencia. Cuando eso pasa, la clase se convierte en un salon de gente escribiendo en silencio y el docente pasando por los puestos preguntando como van, que es exactamente lo que no se debe hacer, porque el checkpoint tambien tiene entregable. El segundo error es pedir a los equipos que se revisen entre si sin rubrica: sin criterios escritos, la revision se vuelve un intercambio de cortesias donde todos dicen que el trabajo del otro esta muy bien y nadie encuentra nada. El tercero es confundir consistencia con completitud y celebrar que el paquete este completo cuando en realidad esta completo pero se contradice: veinte requisitos, ocho casos de uso, quince clases y ninguna trazabilidad entre ellos. Y el cuarto, el mas silencioso, es no exigir que los hallazgos queden por escrito con severidad y responsable; si los hallazgos se dicen de palabra, en la siguiente sesion nadie recuerda ninguno y la auditoria no cambia nada del proyecto."
        ],
        "taller": [
            "Construir en Google Docs la matriz de trazabilidad de VetCare con las columnas RF, Caso de uso, Clase o clases implicadas y Mockup, incluyendo todos los requisitos del catalogo, y marcar en rojo cada fila incompleta.",
            "Levantar el glosario de nombres canonicos con minimo ocho conceptos del dominio (Propietario, Mascota, Consulta, Cita, Veterinario, Vacuna, Expediente, Bitacora), cada uno con definicion de una linea y sinonimos prohibidos, y renombrar en los artefactos todo lo que no coincida.",
            "Intercambiar el paquete completo con otro estudiante (o con otro equipo, si el docente autorizo trabajo en equipo) y aplicar la rubrica de auditoria de seis puntos durante veinte minutos cronometrados, registrando cada hallazgo con ubicacion exacta, descripcion y severidad bloqueante, mayor o menor; queda prohibido proponer soluciones durante la revision.",
            "Recibir los hallazgos propios y clasificarlos en aceptado, rechazado con justificacion escrita o aplazado por acuerdo, sin borrar ninguno del acta, de modo que quede evidencia de la decision tomada.",
            "Armar el backlog priorizado de correcciones con responsable y criterio de cierre verificable para cada item, ordenado por severidad, y aplicar en clase al menos las dos correcciones bloqueantes antes de subir el paquete corregido a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ el paquete de VetCare ya tiene requisitos, casos de uso y clases, pero nadie ha verificado que los tres describan el mismo sistema; sin esa verificacion los planos se contradicen y quien construya va a escoger al azar cual documento obedecer.",
            "Esta sesion produce evidencia propia: matriz, glosario, acta de revision y backlog, y por eso se califica igual que cualquier otra entrega.",
            "Lo que hoy quede ambiguo lo paga el compañero que solo cursa Programacion II, que recibira estos planos sin poder preguntarle nada a la clinica Huellitas."
        ],
        "escenario": [
            "Cada estudiante llega con tres artefactos de VetCare escritos en semanas distintas: el catalogo de RF y RNF, el diagrama con las especificaciones de casos de uso y el diagrama de clases con sus multiplicidades.",
            "Nadie ha vuelto a abrir el catalogo de requisitos desde que se dibujaron las clases, y los nombres empezaron a moverse: donde el requisito dice Propietario, la clase dice Dueño y el mockup dice Cliente.",
            "Hay al menos un requisito que suena bonito en el papel, el RF-07 de recordatorio de cita, y no aparece en ningun caso de uso ni en ninguna clase del modelo."
        ],
        "criterios": [
            "La matriz de trazabilidad cubre el cien por ciento de los RF y no deja casos de uso ni clases sin origen en algun requisito.",
            "El glosario tiene minimo ocho conceptos con nombre canonico, definicion de una linea y sinonimos prohibidos, y los artefactos ya fueron renombrados en consecuencia.",
            "El acta de revision entre pares registra minimo seis hallazgos con ubicacion exacta, descripcion objetiva y severidad asignada.",
            "El backlog tiene responsable y criterio de cierre verificable por item, y las correcciones de severidad bloqueante quedaron aplicadas en el paquete entregado."
        ],
        "pistas": [
            "Si toma el requisito mas ambicioso de su catalogo y lo persigue hasta el diagrama de clases, en que punto exacto se le pierde el rastro?",
            "Cuantos nombres distintos esta usando su paquete para referirse a la misma persona que lleva la mascota a la clinica?",
            "Si usted desapareciera y solo quedara el paquete escrito, alguien podria construir VetCare sin hacer una sola pregunta?"
        ],
        "solucion_pasos": [
            "Matriz de trazabilidad de VetCare diligenciada, fila por fila: RF-02 Registrar propietario lleva a CU-00, a la clase Propietario y al mockup M-01; RF-03 y RF-04 Registrar ficha y datos de la mascota llevan a CU-01 Registrar mascota, a las clases Mascota y Propietario y al mockup M-02; RF-05 Consultar el expediente de una mascota, con el RNF-02 de tres segundos asociado, lleva a CU-02 Buscar expediente, a las clases Mascota y Consulta y al mockup M-03; RF-06 Registrar la consulta medica lleva a CU-03, a las clases Consulta y Veterinario y al mockup M-05; RF-08 Agendar cita lleva a CU-04, a las clases Cita y Veterinario y al mockup M-04; RF-09 Reporte mensual de atenciones lleva a CU-05 Consultar indicadores, a las clases Consulta y Veterinario y al mockup M-06. Al llenarla aparecen las dos filas defectuosas del dia: RF-07 Recordatorio de cita no tiene caso de uso ni clase (huerfano), y la fila de CU-04 quedo sin RF diligenciado en el paquete revisado, de modo que el caso de uso parece viudo aunque el RF-08 exista en el catalogo.",
            "Resolucion del huerfano RF-07, escrita como decision y no como intencion: el equipo elige entre dos caminos y lo deja firmado en el acta. Camino uno, crear CU-07 Enviar recordatorio de cita con el servicio de mensajeria como actor secundario, agregar la clase Notificacion con los atributos destinatario, canal, fechaEnvio y estado, y agregar la asociacion Cita uno a muchos Notificacion. Camino dos, declarar RF-07 fuera del alcance de este periodo y moverlo a la seccion de requisitos aplazados con la justificacion escrita: no hay proveedor de mensajeria definido ni presupuesto para el periodo. Lo inaceptable es dejarlo flotando en el catalogo como promesa sin respaldo, porque la clinica Huellitas ya lo leyo y cuenta con el.",
            "Glosario canonico aplicado, con las filas exactas que deben quedar: Propietario, persona responsable de una o mas mascotas ante la clinica, sinonimos prohibidos Dueño, Cliente y Responsable; Mascota, animal atendido en la clinica identificado con codigo unico, prohibidos Paciente y Animalito; Cita, reserva de un horario futuro con un veterinario, prohibidos Turno y Agendamiento; Consulta, registro de una atencion medica ya realizada, prohibidos Visita y Atencion; Expediente, vista consolidada de ficha mas consultas mas vacunas de una mascota, con la aclaracion explicita de que no es una clase sino una vista, para que nadie cree una tabla Expediente en el diagrama de clases. Tras el renombramiento se corrigen tres artefactos concretos: la clase Dueño pasa a llamarse Propietario en el diagrama de clases, el rotulo Cliente del mockup M-02 pasa a Propietario, y el flujo alterno 2a de CU-01 deja de decir se crea el dueño y dice se registra el propietario.",
            "Acta de revision entre pares con hallazgos escritos como hechos, no como opiniones. H-01, ubicacion diagrama de clases: la clase Consulta no tiene relacion con Veterinario, pero el flujo principal de CU-03 exige registrar quien atendio; severidad mayor. H-02, ubicacion matriz de trazabilidad fila 6: CU-04 Agendar cita aparece sin RF de origen, aunque el catalogo tiene el RF-08 Agendar cita sin enlazar; severidad mayor. H-03, ubicacion diagrama de clases, clase Mascota: guarda el atributo dueño en minuscula y de tipo texto, cuando debe ser una asociacion con la clase Propietario; severidad bloqueante. H-04, ubicacion especificacion de CU-02: el RNF-02 de tres segundos no esta referenciado en ninguna postcondicion; severidad menor. H-05, ubicacion catalogo de requisitos: RF-07 sin caso de uso ni clase; severidad mayor. H-06, ubicacion mockup M-02: el campo que la especificacion llama especie aparece rotulado como tipo de animal; severidad menor.",
            "Backlog priorizado resultante, con responsable y criterio de cierre verificable: primero H-03, responsable el encargado del modelo estatico, cierra cuando la asociacion Propietario uno a muchos Mascota este dibujada con multiplicidad y el atributo de texto haya desaparecido; segundo H-01, mismo responsable, cierra cuando exista la asociacion entre Consulta y Veterinario con multiplicidad y el nombre del veterinario ya no se guarde como texto; tercero H-05, responsable el encargado de requisitos, cierra cuando RF-07 quede ligado a un CU-07 con su clase Notificacion o movido a la seccion de aplazados con justificacion escrita; cuarto H-02, mismo responsable, cierra cuando la fila de CU-04 en la matriz quede ligada a RF-08 Agendar cita; quinto H-04, cierra cuando la postcondicion de CU-02 mencione explicitamente el tiempo maximo de respuesta; sexto H-06, cierra cuando el mockup use el nombre canonico especie. Las dos primeras se aplican en la misma sesion y solo entonces el paquete se marca como consistente."
        ],
        "solucion_rubrica": [
            "Matriz de trazabilidad RF a CU a Clase completa y sin huerfanos (3)",
            "Glosario de nombres canonicos aplicado efectivamente a los artefactos (2)",
            "Acta de revision entre pares con hallazgos objetivos y severidad (3)",
            "Backlog con responsable, criterio de cierre y bloqueantes ya corregidos (2)"
        ],
        "solucion_errores": [
            "Usar la sesion para seguir produciendo artefactos nuevos en lugar de auditar los existentes, de modo que el equipo termina con mas paginas y la misma cantidad de contradicciones.",
            "Escribir hallazgos que son opiniones y no hechos, del estilo el diagrama esta desordenado o falta mas detalle, en vez de señalar la ubicacion exacta y la inconsistencia concreta entre dos artefactos.",
            "Aceptar sinonimos por costumbre, dejando Dueño en el diagrama de clases porque asi se dibujo desde el principio, con lo cual el diccionario de datos y el trabajo de Programacion II terminan con dos conceptos donde solo debia haber uno."
        ],
        "codigo_slide_titulo": "Auditoria cruzada de VetCare: la matriz que delata las contradicciones",
        "codigo_slide_lineas": [
            "| RF     | Caso de uso                  | Clases implicadas      | Mockup | Estado      |",
            "|--------|------------------------------|------------------------|--------|-------------|",
            "| RF-02  | CU-00 Registrar propietario  | Propietario            | M-01   | OK          |",
            "| RF-03  | CU-01 Registrar mascota      | Mascota, Propietario   | M-02   | OK          |",
            "| RF-05  | CU-02 Buscar expediente      | Mascota, Consulta      | M-03   | OK          |",
            "| RF-06  | CU-03 Registrar consulta     | Consulta, ???          | M-05   | HALLAZGO    |",
            "| RF-07  | (no existe)                  | (no existe)            | --     | HUERFANO    |",
            "| (sin)  | CU-04 Agendar cita           | Cita, Veterinario      | M-04   | SIN ORIGEN  |",
            "",
            "H-01 (mayor)     : CU-03 exige registrar quien atendio, pero Consulta no se relaciona con Veterinario.",
            "H-02 (mayor)     : la fila de CU-04 quedo sin RF; debe ligarse a RF-08 Agendar cita o eliminarse el CU.",
            "H-03 (bloqueante): la clase Mascota guarda dueño como texto en lugar de asociarse a Propietario.",
            "H-04 (menor)     : el RNF-02 de 3 segundos no aparece en ninguna postcondicion de CU-02.",
            "Glosario canonico: Propietario (prohibido Dueño, Cliente, Responsable) | Cita != Consulta."
        ],
        "codigo_slide_caption": "Una tabla de cuatro columnas encuentra en veinte minutos las contradicciones que un equipo no ve en tres semanas.",
        "artefacto_archivo": "Auditoria-Cruzada-VetCare.md",
        "artefacto_contenido": "# Auditoria cruzada del paquete de diseño - VetCare (Clinica Huellitas)\n\n> Hoy no se agrega tema nuevo. Se verifica que requisitos, casos de uso, clases y mockups describan el MISMO sistema y usen los MISMOS nombres.\n\n## 1. Matriz de trazabilidad\n\nRegla: toda fila debe estar completa. Fila incompleta = hallazgo.\n\n| RF | Caso de uso | Clases implicadas | Mockup | Estado |\n|---|---|---|---|---|\n| RF-02 | CU-00 Registrar propietario | Propietario | M-01 | |\n| RF-03, RF-04 | CU-01 Registrar mascota | Mascota, Propietario | M-02 | |\n| RF-05 | CU-02 Buscar expediente | Mascota, Consulta | M-03 | |\n| RF-06 | CU-03 Registrar consulta medica | Consulta, Veterinario | M-05 | |\n| RF-07 | | | | |\n| RF-08 | CU-04 Agendar cita | Cita, Veterinario | M-04 | |\n| RF-09 | CU-05 Consultar indicadores | Consulta, Veterinario | M-06 | |\n\n- HUERFANO: requisito que no llega a ningun caso de uso ni clase.\n- VIUDO: caso de uso o clase que no nace de ningun requisito.\n\n## 2. Glosario de nombres canonicos\n\n| Nombre canonico | Definicion en una linea | Sinonimos prohibidos |\n|---|---|---|\n| Propietario | Persona responsable de una o mas mascotas ante la clinica | Dueño, Cliente, Responsable |\n| Mascota | Animal atendido en la clinica, identificado con codigo unico | Paciente, Animalito |\n| Cita | Reserva de un horario con un veterinario para una fecha futura | Turno, Agendamiento |\n| Consulta | Registro de una atencion medica ya realizada | Visita, Atencion |\n| Expediente | Vista consolidada de ficha, consultas y vacunas de una mascota (NO es una clase) | Historia, Carpeta |\n| Veterinario | Profesional que atiende consultas y firma el registro clinico | Doctor, Medico |\n| Vacuna | Aplicacion registrada de un biologico con fecha y refuerzo | Inyeccion |\n| Bitacora | Registro de quien hizo que y cuando dentro del sistema | Log, Auditoria |\n\n## 3. Rubrica de revision entre pares (20 minutos por paquete)\n\nRoles: el AUTOR permanece en silencio, el REVISOR recorre la rubrica, el MODERADOR toma el tiempo y escribe.\nProhibido proponer soluciones durante la revision: solo se reportan hechos.\n\n| # | Punto a verificar | Cumple | Observacion |\n|---|---|---|---|\n| 1 | Todo RF llega a un caso de uso y a una clase | | |\n| 2 | Todo caso de uso nace de al menos un RF | | |\n| 3 | Los nombres coinciden con el glosario canonico | | |\n| 4 | Cada caso de uso tiene pre, post y minimo dos alternos | | |\n| 5 | El diagrama de clases tiene multiplicidades en todas las asociaciones | | |\n| 6 | Los mockups muestran los campos que exige la especificacion | | |\n\n## 4. Acta de hallazgos\n\nSeveridad: BLOQUEANTE (impide construir) / MAYOR (obliga a rehacer un artefacto) / MENOR (cosmetico).\n\n| ID | Ubicacion exacta | Descripcion objetiva del hallazgo | Severidad | Decision |\n|---|---|---|---|---|\n| H-01 | Diagrama de clases, clase Consulta | No existe relacion con Veterinario y CU-03 exige registrar quien atendio | Mayor | Aceptado / Rechazado / Aplazado |\n| H-02 | Matriz de trazabilidad, fila de CU-04 | El caso de uso aparece sin RF de origen pese a que existe RF-08 | Mayor | |\n| H-03 | Diagrama de clases, clase Mascota | Guarda dueño como atributo de texto en vez de asociarse con Propietario | Bloqueante | |\n\n## 5. Backlog de deuda de diseño\n\n| Prioridad | Item | Responsable | Criterio de cierre verificable |\n|---|---|---|---|\n| 1 | H-03 | Modelo estatico | Existe asociacion Propietario 1..* Mascota con multiplicidad y el atributo texto fue eliminado |\n| 2 | H-01 | Modelo estatico | Existe asociacion Consulta - Veterinario con multiplicidad dibujada |\n| 3 | H-02 | Requisitos | La fila de CU-04 en la matriz queda ligada a RF-08 |\n\n## 6. Definicion de terminado del paquete VetCare\n\n- [ ] Catalogo de RF y RNF numerado, sin huerfanos.\n- [ ] Diagrama de casos de uso con limite de sistema y actores como roles.\n- [ ] Especificacion textual de los casos de uso criticos con flujos alternos.\n- [ ] Diagrama de clases con atributos, operaciones y multiplicidades.\n- [ ] Mockups de las pantallas criticas coherentes con las especificaciones.\n- [ ] Diccionario de datos alineado con los nombres canonicos.\n- [ ] Matriz de trazabilidad completa y acta de revision firmada por el equipo revisor.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare, el RF-07 promete recordatorio de cita pero no aparece en ningun caso de uso ni en ninguna clase. Como se llama ese defecto?",
                "opciones": [
                    "A) Requisito huerfano",
                    "B) Requisito no funcional",
                    "C) Caso de uso viudo",
                    "D) Regla de negocio implicita"
                ],
                "clave": "A"
            },
            {
                "tipo": "om",
                "q": "Cual de estos es un hallazgo bien redactado en una revision entre pares?",
                "opciones": [
                    "A) El diagrama de clases esta desordenado y cuesta leerlo",
                    "B) Al equipo le falto dedicarle mas tiempo al modelo",
                    "C) En el diagrama de clases, Consulta no se relaciona con Veterinario aunque CU-03 exige registrar quien atendio",
                    "D) Deberian usar otra herramienta de modelado para dibujar mejor"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Que severidad corresponde a un hallazgo que impide construir el sistema mientras no se corrija, como guardar el propietario en un atributo de texto?",
                "opciones": [
                    "A) Menor, porque es un detalle de nombres",
                    "B) Mayor, porque obliga a rehacer un artefacto",
                    "C) Bloqueante, porque impide construir el sistema",
                    "D) Informativo, porque solo es una sugerencia de estilo"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Para que sirve el glosario de nombres canonicos en el paquete de VetCare?",
                "opciones": [
                    "A) Para tener un anexo bonito al final del documento",
                    "B) Para que cada concepto tenga un solo nombre en requisitos, casos de uso, mockups y clases",
                    "C) Para traducir los terminos tecnicos al ingles",
                    "D) Para reemplazar el diccionario de datos"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Un paquete de diseño puede estar completo y aun asi ser inconsistente, porque completitud y consistencia no son lo mismo.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Durante la revision entre pares el autor debe defender su trabajo y discutir cada hallazgo en el momento, para no perder tiempo despues.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Explique la diferencia entre trazabilidad hacia adelante y trazabilidad hacia atras, con un ejemplo de VetCare para cada una.",
                "clave": "Hacia adelante se verifica que todo requisito llegue a un caso de uso y a una clase: RF-05, consultar el expediente de una mascota, debe llegar a CU-02 Buscar expediente y a las clases Mascota y Consulta; si se pierde en el camino, el problema de Huellitas queda sin resolver. Hacia atras se verifica que todo elemento del diseño nazca de un requisito: si en la matriz CU-04 Agendar cita aparece sin RF de origen, hay que ligarlo al RF-08 del catalogo o eliminarlo del diagrama, porque nadie construye lo que nadie pidio."
            },
            {
                "tipo": "abierta",
                "q": "Su equipo detecta que la clase Mascota guarda el dueño como un atributo de texto, mientras el requisito habla de Propietario como una entidad con documento y telefono. Redacte el hallazgo con severidad y su criterio de cierre.",
                "clave": "Hallazgo de severidad bloqueante: en el diagrama de clases, Mascota almacena dueño como atributo de texto en lugar de asociarse con la clase Propietario, lo que impide cumplir RF-02 y duplica informacion cada vez que un propietario tiene varias mascotas. Criterio de cierre verificable: existe la asociacion Propietario uno a muchos Mascota con multiplicidad dibujada, el atributo de texto fue eliminado y el nombre Propietario reemplaza a Dueño en todos los artefactos segun el glosario canonico."
            }
        ]
    },
    {
        "n": 12,
        "slug": "Diagramas UML avanzados",
        "titulo": "Diagramas UML avanzados",
        "subtitulo": "Secuencia: quien le habla a quien. Actividad: en que orden ocurre el trabajo",
        "herramienta": "draw.io · Mermaid Live Editor",
        "hito_pi": "Queda modelada la dinamica de VetCare: el diagrama de secuencia del caso de uso Agendar cita y el diagrama de actividad del proceso de atencion en el consultorio.",
        "entregable": "Un PDF con el diagrama de secuencia de Agendar cita incluyendo el fragmento alt para horario ocupado, el diagrama de actividad del proceso de atencion con calles por rol, y la tabla que mapea cada mensaje del diagrama de secuencia a una operacion del diagrama de clases, subido a ExamLab.",
        "demo": "El docente toma el flujo principal ya escrito de CU-04 Agendar cita y lo convierte linea por linea en mensajes de un diagrama de secuencia en Mermaid, mostrando en vivo que cada mensaje necesita una clase dueña que lo pueda responder.",
        "teoria": [
            "Hasta ahora todos los modelos de VetCare han sido estaticos: el diagrama de clases dice que existe una clase Cita con sus atributos, y la especificacion de caso de uso dice que la recepcionista agenda. Lo que ninguno de los dos muestra es la conversacion interna del sistema en el momento exacto en que eso ocurre. Para eso existe el diagrama de secuencia, que es un modelo del tiempo: arriba se dibujan los participantes, de cada uno baja una linea de vida y el tiempo transcurre hacia abajo, de modo que el orden vertical de las flechas es el orden real de los eventos. Cada flecha es un mensaje, es decir, la peticion de un objeto a otro para que haga algo; la flecha llena representa una llamada sincrona, donde quien pide se queda esperando la respuesta, y la flecha punteada representa el retorno con el resultado. Sobre la linea de vida se dibujan barras de activacion que muestran durante cuanto tiempo ese objeto esta trabajando. En VetCare, agendar una cita se ve como una cadena corta y clara: la recepcionista le habla a la pantalla de agenda, la pantalla le habla al control de agenda, el control verifica la mascota, le pregunta al repositorio de citas por la disponibilidad y devuelve una confirmacion con el identificador de la cita.",
            "El diagrama de actividad responde a otra pregunta completamente distinta: no quien le habla a quien, sino en que orden ocurre el trabajo y quien es responsable de cada paso, incluyendo pasos que suceden fuera del computador. Sus elementos son nodo inicial, acciones, nodos de decision con condiciones escritas entre corchetes, nodos de union, barras de bifurcacion y sincronizacion para el trabajo que ocurre en paralelo, y nodo final. La herramienta que lo vuelve realmente util en un proyecto como VetCare son las particiones o calles: una franja por cada rol, de modo que al mirar el dibujo se sabe de un vistazo que hace el Propietario, que hace la Recepcionista, que hace el Veterinario y que hace el sistema. Eso permite modelar el proceso completo de atencion en Huellitas: el propietario llega y pregunta, la recepcionista verifica la cita, si no la tiene se decide entre esperar o reagendar, el veterinario atiende, registra la consulta y si formula medicamentos el flujo se abre en dos ramas paralelas, una de facturacion y otra de programacion del control. Ese dibujo revela algo que ni los casos de uso ni las clases muestran: donde estan los cuellos de botella del proceso real de la clinica.",
            "La pregunta practica es cuando usar cada uno, y la respuesta se decide por el tipo de duda que se quiere resolver. Si la duda es de responsabilidades, es decir, cual objeto deberia encargarse de esto y con quien tiene que hablar para lograrlo, el diagrama correcto es el de secuencia, porque obliga a que cada mensaje tenga un destinatario concreto y por lo tanto una clase que lo sepa atender. Si la duda es de proceso, es decir, en que orden hace la gente las cosas, donde se decide algo y que pasa en paralelo, el diagrama correcto es el de actividad, porque admite pasos manuales, decisiones del negocio y actores humanos que no son objetos de software. Una regla practica para el aula: el diagrama de secuencia se dibuja para un caso de uso y suele cubrir su flujo principal; el diagrama de actividad se dibuja para un proceso de negocio que puede atravesar varios casos de uso. En VetCare, CU-04 Agendar cita se modela con secuencia; la atencion completa desde que el propietario entra por la puerta hasta que sale con la factura se modela con actividad, porque incluye conversaciones y esperas que ningun objeto del sistema ejecuta.",
            "Estos diagramas no se inventan desde cero: se derivan de lo que ya esta escrito, y ahi esta la parte que separa a un estudiante que entendio de uno que solo dibujo. Cada paso del flujo principal del caso de uso se convierte en uno o varios mensajes del diagrama de secuencia, en el mismo orden y con los mismos nombres del glosario canonico que se fijo en la auditoria de la clase once. Si el paso 2 de CU-04 dice que el sistema verifica la disponibilidad del veterinario para esa fecha, entonces debe existir un mensaje llamado consultarDisponibilidad dirigido a algun participante, y ese participante debe ser una clase que exista en el diagrama de clases. Aqui aparece el hallazgo tipico y valiosisimo: al dibujar la secuencia el equipo descubre que envio un mensaje a una clase que no tiene esa operacion, o peor, a una clase que no existe. Eso no es un fracaso del diagrama de secuencia, es su mayor utilidad, porque es la unica manera barata de detectar que el modelo estatico estaba incompleto. Por eso el entregable de hoy incluye la tabla de mapeo mensaje a operacion: obliga a cerrar el circulo entre lo dinamico y lo estatico.",
            "Los flujos alternos tambien se modelan, y para eso existen los fragmentos combinados, que son esos recuadros con una etiqueta en la esquina. El fragmento alt representa caminos excluyentes con sus condiciones de guarda escritas entre corchetes, y es el que usamos en VetCare para el horario ocupado: si hay disponibilidad se guarda la cita y se confirma, si no la hay el sistema ofrece alternativas del dia siguiente. El fragmento opt es un camino opcional que puede ocurrir o no, como enviar el recordatorio si el propietario autorizo mensajeria. El fragmento loop repite un bloque, por ejemplo mientras el veterinario agrega varias vacunas al expediente. La disciplina que hay que enseñar aqui es de alcance: un diagrama de secuencia no debe intentar mostrar los quince alternos posibles, porque se vuelve ilegible y nadie lo lee. La practica sana es dibujar el camino feliz completo mas uno o dos fragmentos que representen las decisiones criticas del negocio, y dejar el resto documentado en el texto de la especificacion, que para eso existe.",
            "Error tipico del docente que no domina el tema: confundir el diagrama de secuencia con un diagrama de flujo y poner rombos de decision colgando de las lineas de vida, cuando las decisiones en secuencia se representan con fragmentos alt y no con rombos. El segundo error es dibujar la secuencia con participantes que no son objetos, como Base de datos, Internet, Usuario final o incluso Sistema, a secas: si el participante no corresponde a una clase del modelo o a un actor legitimo, el diagrama no sirve para verificar responsabilidades y se vuelve un adorno. El tercero es olvidar las flechas de retorno y quedarse solo con las flechas de ida, con lo cual nunca se ve que informacion devuelve cada llamada, que es justamente lo que despues define el resultado esperado de cada operacion en Programacion II. El cuarto es usar diagrama de actividad sin calles, dibujando quince cajitas seguidas donde no se sabe quien hace que, con lo cual se pierde precisamente la ventaja del diagrama. Y el quinto, el mas grave para el proyecto integrador, es dibujar una secuencia que contradice el caso de uso ya especificado: el texto dice que primero se verifica la existencia de la mascota y el dibujo empieza guardando la cita, y como nadie compara los dos artefactos, la contradiccion viaja intacta hasta la construccion."
        ],
        "taller": [
            "Tomar el flujo principal escrito de CU-04 Agendar cita, y si todavia no esta especificado diligenciar primero la plantilla de la clase nueve, para luego numerar en el documento cual paso genera cual mensaje, de manera que quede una lista de entre seis y ocho mensajes antes de dibujar cualquier cosa.",
            "Dibujar el diagrama de secuencia en Mermaid Live Editor o draw.io con la recepcionista como actor y minimo tres participantes que correspondan a clases reales del diagrama de clases de VetCare, incluyendo las flechas de retorno con el dato que devuelven.",
            "Agregar un fragmento alt que modele el horario ocupado con sus dos condiciones de guarda escritas, y verificar que el camino del else corresponda a un flujo alterno documentado en la especificacion del caso de uso.",
            "Construir la tabla de mapeo mensaje a operacion con tres columnas, mensaje, clase destinataria y operacion que debe existir, y agregar al diagrama de clases toda operacion que hoy falte; ninguna fila puede quedar con la clase en blanco.",
            "Dibujar el diagrama de actividad del proceso de atencion en el consultorio con cuatro calles (Propietario, Recepcionista, Veterinario y Sistema VetCare), con minimo dos nodos de decision y una bifurcacion en paralelo, y exportar todo a PDF para subirlo a ExamLab."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ los casos de uso dicen que hace VetCare y el diagrama de clases dice de que esta hecho, pero solo los diagramas de secuencia y actividad muestran como colaboran las piezas en el tiempo, que es lo que necesita quien vaya a construirlo.",
            "Dibujar la secuencia es la forma mas barata de descubrir que al diagrama de clases le faltan operaciones, porque cada flecha exige un dueño que la pueda responder.",
            "El diagrama de actividad es el unico artefacto del paquete que muestra el trabajo humano de la clinica Huellitas, incluidas las esperas y las decisiones que ocurren fuera del computador."
        ],
        "escenario": [
            "VetCare ya tiene casos de uso especificados y un diagrama de clases con multiplicidades, pero ningun documento explica el orden en que los objetos se comunican para cumplir un caso de uso.",
            "En Huellitas, agendar una cita depende de la disponibilidad del veterinario y hoy eso se resuelve preguntando en voz alta al fondo del consultorio, sin ninguna regla escrita.",
            "El equipo tiende a dibujar cajas y flechas por intuicion, sin volver a mirar el flujo principal que ya habia escrito hace tres sesiones."
        ],
        "criterios": [
            "El diagrama de secuencia reproduce el orden exacto del flujo principal de CU-04 y no inventa pasos que no esten en la especificacion.",
            "Todos los participantes del diagrama corresponden a actores legitimos o a clases existentes en el diagrama de clases, y aparecen las flechas de retorno con el dato que devuelven.",
            "Existe al menos un fragmento alt con sus dos condiciones de guarda escritas, coherente con un flujo alterno ya documentado.",
            "El diagrama de actividad tiene calles por rol, minimo dos decisiones con condiciones entre corchetes y una bifurcacion en paralelo, y la tabla de mapeo mensaje a operacion no tiene filas incompletas."
        ],
        "pistas": [
            "Si sigue las flechas de su diagrama de arriba hacia abajo, obtiene exactamente el mismo relato que ya escribio en el flujo principal del caso de uso?",
            "Cada participante de su diagrama existe como clase en el modelo, o dibujo cajas como Base de datos y Sistema que nadie puede implementar?",
            "En su diagrama de actividad se puede saber, mirando solo la calle, quien es responsable de cada paso y cual de esos pasos ocurre sin tocar el computador?"
        ],
        "solucion_pasos": [
            "Derivacion desde el caso de uso, que es el paso que casi nadie hace. El flujo principal de CU-04 Agendar cita, que nace del RF-08, queda escrito asi: 1) la recepcionista selecciona Agendar cita, indica el codigo de la mascota, el veterinario y la fecha deseada; 2) el sistema verifica que la mascota exista; 3) el sistema consulta la disponibilidad del veterinario para esa fecha; 4) el sistema muestra los horarios libres y la recepcionista escoge uno; 5) el sistema registra la cita y confirma mostrando el identificador. El alterno 3a dice que si el veterinario no tiene disponibilidad el sistema ofrece los horarios del dia siguiente. De ese texto salen exactamente cinco mensajes de ida y tres retornos, y esa lista se escribe en el documento antes de dibujar; si al terminar el dibujo aparecen flechas que no corresponden a ningun paso del texto, sobran.",
            "Diagrama de secuencia resuelto: actor Recepcionista; participantes :PantallaAgenda, :ControlAgenda, :RepositorioMascotas y :RepositorioCitas. Mensajes en orden: solicitarAgendamiento(codigoMascota, fecha) de la recepcionista a PantallaAgenda; agendarCita(codigoMascota, fecha, idVeterinario) de PantallaAgenda a ControlAgenda; existePorCodigo(codigoMascota) de ControlAgenda a RepositorioMascotas con retorno punteado mascota; consultarDisponibilidad(idVeterinario, fecha) de ControlAgenda a RepositorioCitas con retorno punteado horariosLibres; dentro del fragmento alt, si hay horario libre, guardarCita(cita) hacia RepositorioCitas con retorno idCita y luego confirmacion(idCita) hacia PantallaAgenda; si no lo hay, el retorno es alternativas(dia siguiente). Todas las flechas de ida son llenas y todos los retornos son punteados, y cada linea de vida lleva su barra de activacion mientras trabaja.",
            "Tabla de mapeo mensaje a operacion, que es donde aparecen los hallazgos: existePorCodigo(codigoMascota) va a RepositorioMascotas y exige la operacion existePorCodigo(codigo) que devuelve booleano o la mascota; consultarDisponibilidad(idVeterinario, fecha) va a RepositorioCitas y exige consultarDisponibilidad(idVeterinario, fecha) que devuelve una lista de horarios libres; guardarCita(cita) va a RepositorioCitas y exige guardarCita(cita) que devuelve el identificador de la cita. Al llenar la tabla el equipo descubre que el diagrama de clases no tenia la operacion consultarDisponibilidad en ninguna clase, la agrega a RepositorioCitas y anota el cambio en el acta; ese es el resultado mas valioso del ejercicio y se reporta como hallazgo de severidad mayor sobre el modelo estatico.",
            "Fragmento alt coherente con la especificacion: la condicion de guarda del camino principal se escribe hay horario libre y la del camino alterno no hay horario libre. Ambas deben existir como flujos en el texto de CU-04, donde el alterno 3a dice que si el veterinario no tiene disponibilidad el sistema ofrece los horarios del dia siguiente. Si el dibujo tiene un camino que el texto no contempla, se corrige el texto o se borra el camino, pero nunca se dejan los dos artefactos diciendo cosas distintas. Los demas alternos de CU-04, como fecha en el pasado o mascota inactiva, se quedan documentados en el texto y no se dibujan, para que el diagrama siga siendo legible.",
            "Diagrama de actividad del proceso de atencion, con cuatro calles y contenido concreto: en la calle Propietario, llegar a la clinica y entregar la mascota, mas esperar el turno, ambos marcados como trabajo manual; en la calle Recepcionista, verificar si tiene cita, con un nodo de decision de dos salidas etiquetadas [tiene cita] que va a registrar la llegada y [no tiene cita] que lleva a un segundo nodo de decision entre [hay disponibilidad ahora] y [no hay disponibilidad], que termina en reagendar la cita y en el nodo final; en la calle Veterinario, atender la consulta y registrar el diagnostico; en la calle Sistema VetCare, actualizar el expediente y, a partir de ahi, una barra de bifurcacion que abre dos ramas paralelas, generar la orden de facturacion y programar la cita de control, con una barra de sincronizacion antes del nodo final. El dibujo deja ver el cuello de botella real de Huellitas: la espera del propietario cuando llega sin cita."
        ],
        "solucion_rubrica": [
            "Diagrama de secuencia derivado fielmente del flujo principal de CU-04 (3)",
            "Participantes validos con flechas de retorno y datos devueltos (2)",
            "Fragmento alt coherente con un flujo alterno documentado (2)",
            "Diagrama de actividad con calles, decisiones y paralelismo, mas tabla de mapeo mensaje a operacion completa (3)"
        ],
        "solucion_errores": [
            "Poner rombos de decision colgando de las lineas de vida del diagrama de secuencia, cuando las decisiones se representan con fragmentos alt; el resultado es un hibrido que no es ni secuencia ni actividad y que ninguna herramienta de modelado acepta.",
            "Usar participantes que no son clases del modelo, como Base de datos, Sistema o Internet, con lo cual el diagrama deja de servir para verificar responsabilidades y no permite descubrir operaciones faltantes en el diagrama de clases.",
            "Dibujar el diagrama de actividad como una tira de cajas sin calles, de manera que no se distingue que hace el propietario, que hace la recepcionista y que hace el sistema, que era precisamente la informacion que se buscaba al modelar el proceso de Huellitas."
        ],
        "codigo_slide_titulo": "Secuencia de CU-04 Agendar cita en sintaxis Mermaid",
        "codigo_slide_lineas": [
            "sequenceDiagram",
            "    actor Recepcionista",
            "    participant UI as :PantallaAgenda",
            "    participant CTRL as :ControlAgenda",
            "    participant REPM as :RepositorioMascotas",
            "    participant REPC as :RepositorioCitas",
            "    Recepcionista->>UI: solicitarAgendamiento(codigoMascota, fecha)",
            "    UI->>CTRL: agendarCita(codigoMascota, fecha, idVeterinario)",
            "    CTRL->>REPM: existePorCodigo(codigoMascota)",
            "    REPM-->>CTRL: mascota",
            "    CTRL->>REPC: consultarDisponibilidad(idVeterinario, fecha)",
            "    REPC-->>CTRL: horariosLibres",
            "    alt hay horario libre",
            "        CTRL->>REPC: guardarCita(cita)",
            "        REPC-->>CTRL: idCita",
            "        CTRL-->>UI: confirmacion(idCita)",
            "    else no hay horario libre",
            "        CTRL-->>UI: alternativas(dia siguiente)",
            "    end"
        ],
        "codigo_slide_caption": "Cada flecha tiene que corresponder a una operacion existente en el diagrama de clases: si no existe, o falta la operacion o sobra la flecha.",
        "artefacto_archivo": "Secuencia-Actividad-VetCare.md",
        "artefacto_contenido": "# Diagramas dinamicos de VetCare - secuencia y actividad\n\n> Regla: estos diagramas NO se inventan. Se derivan del flujo principal ya escrito en la especificacion del caso de uso y de las clases ya definidas.\n\n## 1. Cuando usar cada uno\n\n| Pregunta que quiero responder | Diagrama correcto |\n|---|---|\n| Quien le habla a quien y en que orden para cumplir un caso de uso | Secuencia |\n| Que objeto deberia ser responsable de esta tarea | Secuencia |\n| En que orden hace el trabajo la gente de la clinica, incluyendo pasos manuales | Actividad |\n| Donde se decide algo y que ocurre en paralelo | Actividad |\n\n## 2. Punto de partida: flujo principal de CU-04 Agendar cita (RF-08)\n\n| Paso | Actor | Sistema |\n|---|---|---|\n| 1 | Selecciona Agendar cita e indica codigo de mascota, veterinario y fecha | Muestra el formulario de agendamiento |\n| 2 | -- | Verifica que la mascota exista |\n| 3 | -- | Consulta la disponibilidad del veterinario para esa fecha |\n| 4 | Escoge uno de los horarios libres | Muestra los horarios libres |\n| 5 | Confirma | Registra la cita y muestra el identificador |\n\n- Alterno 3a: el veterinario no tiene disponibilidad; el sistema ofrece los horarios del dia siguiente.\n\n## 3. Diagrama de secuencia - CU-04 Agendar cita\n\n```mermaid\nsequenceDiagram\n    actor Recepcionista\n    participant UI as :PantallaAgenda\n    participant CTRL as :ControlAgenda\n    participant REPM as :RepositorioMascotas\n    participant REPC as :RepositorioCitas\n    Recepcionista->>UI: solicitarAgendamiento(codigoMascota, fecha)\n    UI->>CTRL: agendarCita(codigoMascota, fecha, idVeterinario)\n    CTRL->>REPM: existePorCodigo(codigoMascota)\n    REPM-->>CTRL: mascota\n    CTRL->>REPC: consultarDisponibilidad(idVeterinario, fecha)\n    REPC-->>CTRL: horariosLibres\n    alt hay horario libre\n        CTRL->>REPC: guardarCita(cita)\n        REPC-->>CTRL: idCita\n        CTRL-->>UI: confirmacion(idCita)\n    else no hay horario libre\n        CTRL-->>UI: alternativas(dia siguiente)\n    end\n```\n\n## 4. Tabla de mapeo mensaje a operacion (obligatoria)\n\n| Mensaje del diagrama | Clase destinataria | Operacion que debe existir | Ya existe? |\n|---|---|---|---|\n| existePorCodigo(codigoMascota) | RepositorioMascotas | existePorCodigo(codigo): booleano | |\n| consultarDisponibilidad(idVeterinario, fecha) | RepositorioCitas | consultarDisponibilidad(idVeterinario, fecha): lista de horarios | |\n| guardarCita(cita) | RepositorioCitas | guardarCita(cita): idCita | |\n\n> Si una fila queda sin clase destinataria, el diagrama de clases esta incompleto. Ese es el hallazgo mas valioso del ejercicio.\n\n## 5. Diagrama de actividad - proceso de atencion en Huellitas\n\n```mermaid\nflowchart TD\n    A([Inicio]) --> B[Propietario llega con la mascota]\n    B --> C{Tiene cita agendada?}\n    C -- Si --> D[Recepcionista registra la llegada]\n    C -- No --> E{Hay disponibilidad ahora?}\n    E -- Si --> D\n    E -- No --> F[Recepcionista reagenda la cita]\n    F --> Z([Fin])\n    D --> G[Veterinario atiende la consulta]\n    G --> H[Sistema registra diagnostico en el expediente]\n    H --> I[Generar orden de facturacion]\n    H --> J[Programar cita de control]\n    I --> K([Fin])\n    J --> K\n```\n\n> En draw.io este mismo flujo se dibuja con calles: Propietario, Recepcionista, Veterinario y Sistema VetCare, para que se vea de un golpe quien es responsable de cada paso y cual ocurre sin tocar el computador.\n\n## 6. Checklist antes de entregar en ExamLab\n\n- [ ] El orden de los mensajes coincide paso por paso con el flujo principal del caso de uso.\n- [ ] Todos los participantes son actores legitimos o clases del diagrama de clases.\n- [ ] Aparecen las flechas de retorno indicando que informacion devuelven.\n- [ ] Hay al menos un fragmento alt con sus dos condiciones de guarda escritas.\n- [ ] El fragmento alt corresponde a un flujo alterno ya documentado en el texto.\n- [ ] El diagrama de actividad tiene calles, minimo dos decisiones y una bifurcacion en paralelo.\n- [ ] La tabla de mapeo mensaje a operacion no tiene filas incompletas.\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "En un diagrama de secuencia, que representa el eje vertical?",
                "opciones": [
                    "A) La jerarquia de herencia entre clases",
                    "B) El paso del tiempo, de arriba hacia abajo",
                    "C) La cantidad de objetos creados",
                    "D) La prioridad de los requisitos"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "El equipo quiere modelar el proceso completo de atencion en Huellitas, incluyendo la espera del propietario en la sala y la decision de reagendar. Que diagrama corresponde?",
                "opciones": [
                    "A) Diagrama de secuencia, porque muestra el orden en el tiempo",
                    "B) Diagrama de clases, porque muestra las entidades del dominio",
                    "C) Diagrama de actividad con calles por rol, porque admite pasos manuales y decisiones del negocio",
                    "D) Diagrama de casos de uso, porque muestra a los actores"
                ],
                "clave": "C"
            },
            {
                "tipo": "om",
                "q": "Como se representan en un diagrama de secuencia los dos caminos de VetCare cuando hay o no hay horario disponible?",
                "opciones": [
                    "A) Con un rombo de decision colgando de la linea de vida",
                    "B) Con un fragmento combinado alt y sus condiciones de guarda",
                    "C) Con dos diagramas separados obligatoriamente",
                    "D) Con una nota al pie del diagrama"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Al dibujar la secuencia de Agendar cita, el equipo envia el mensaje consultarDisponibilidad a una clase que no tiene esa operacion. Que significa ese hallazgo?",
                "opciones": [
                    "A) Que el diagrama de secuencia esta mal y hay que borrar el mensaje",
                    "B) Que el diagrama de clases esta incompleto y debe agregarse la operacion o reasignarse la responsabilidad",
                    "C) Que hay que cambiar de herramienta de modelado",
                    "D) Que el caso de uso sobra y debe eliminarse del diagrama"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Las flechas punteadas en un diagrama de secuencia representan los mensajes de retorno con el resultado de la llamada.",
                "clave": "V"
            },
            {
                "tipo": "vf",
                "q": "Un diagrama de secuencia debe incluir todos los flujos alternos documentados en la especificacion del caso de uso, sin excepcion.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Explique con un ejemplo de VetCare la diferencia entre lo que muestra un diagrama de secuencia y lo que muestra un diagrama de actividad.",
                "clave": "El diagrama de secuencia muestra la colaboracion interna entre objetos en el tiempo para cumplir un caso de uso: en CU-04 Agendar cita, PantallaAgenda le pide a ControlAgenda que agende, este verifica la mascota en RepositorioMascotas, consulta la disponibilidad en RepositorioCitas y devuelve la confirmacion con el idCita. El diagrama de actividad muestra el flujo de trabajo del negocio con decisiones y responsables por calle, incluidos pasos manuales: el propietario llega, la recepcionista verifica si hay cita, si no hay se decide entre esperar o reagendar, el veterinario atiende y en paralelo se genera la facturacion y se programa el control."
            },
            {
                "tipo": "abierta",
                "q": "Un equipo entrega un diagrama de secuencia cuyos participantes son Usuario, Sistema e Internet. Que le señala usted y como se corrige?",
                "clave": "Que esos participantes no son objetos del modelo: Usuario debe ser el actor Recepcionista o Veterinario segun el caso de uso, Sistema debe descomponerse en las clases reales que colaboran, como PantallaAgenda, ControlAgenda, RepositorioMascotas y RepositorioCitas, e Internet no participa porque es infraestructura y no una responsabilidad del diseño. Se corrige reemplazando cada participante por una clase existente en el diagrama de clases y verificando con la tabla de mapeo que cada mensaje tenga una operacion que lo atienda; si alguna no existe, se agrega al modelo estatico."
            }
        ]
    },
    {
        "n": 13,
        "slug": "Diseño de interfaces",
        "titulo": "Diseño de interfaces",
        "subtitulo": "Del boceto en gris al prototipo que se puede recorrer",
        "herramienta": "Figma o Penpot · Excalidraw · Google Docs",
        "hito_pi": "Quedan listas las pantallas de Registrar mascota y Buscar expediente de VetCare, anotadas y conectadas en un prototipo navegable.",
        "entregable": "Un archivo de Figma o Penpot con las dos pantallas anotadas y minimo tres transiciones navegables, mas la hoja de anotaciones que amarra cada campo a un RF y a un atributo del diccionario de datos, subido a ExamLab.",
        "demo": "El docente dibuja en vivo el wireframe de Registrar mascota en Penpot, le pone tres anotaciones numeradas y lo conecta con Buscar expediente para que la clase vea en la misma pantalla la diferencia entre wireframe, mockup y prototipo.",
        "teoria": [
            "Un wireframe, un mockup y un prototipo no son tres nombres elegantes para lo mismo: son tres momentos distintos del diseño y cada uno responde una pregunta diferente. El wireframe es el esqueleto en gris, cajas, lineas y etiquetas, sin colores ni logos, y responde a la pregunta que informacion va en esta pantalla y en que orden la va a leer la persona. El mockup ya es la foto fija de como se vera: tipografia, color, iconos, el logo de la clinica Huellitas, los espacios reales entre elementos; responde a la pregunta como se ve. El prototipo es el mockup con clic, es decir uno oprime Guardar y la herramienta lo lleva a otra pantalla; responde a la pregunta como se siente usarlo. En VetCare esto se traduce asi: el wireframe de Registrar mascota se hace en diez minutos en Excalidraw y solo dice que arriba va la busqueda del dueño, en el centro los datos de la mascota y abajo el boton Guardar; el mockup de esa misma pantalla ya usa el verde de la clinica y una tipografia grande porque la recepcionista tiene el monitor lejos; y el prototipo permite que el docente, en la sustentacion, oprima Guardar y aterrice en la ficha del paciente recien creado. La razon de hacerlo en ese orden es puramente economica: mover una caja en un wireframe cuesta treinta segundos, mover esa misma caja cuando ya esta programada en Programacion II cuesta dos sesiones de trabajo. Diseñar es equivocarse barato.",
            "Los principios de usabilidad no son gusto ni estetica, son reglas observables que se pueden verificar sobre el papel. Visibilidad del estado del sistema significa que la persona siempre sepa que esta pasando: si la recepcionista oprime Guardar y la pantalla no dice nada, ella va a oprimir Guardar otra vez y VetCare va a terminar con la mascota registrada dos veces; por eso el diseño debe incluir el mensaje concreto Ficha guardada, codigo M-0421, y el boton debe quedar deshabilitado mientras se guarda. Prevencion de errores significa que es mejor impedir el error que ponerle un mensaje bonito despues: la fecha de nacimiento se escoge en un calendario y no se teclea, la especie se elige de una lista cerrada con Canino, Felino y Otro, y el sistema pide confirmacion antes de eliminar una historia clinica. Consistencia significa que la misma accion se llame igual y viva en el mismo lugar en todas las pantallas: si en Registrar mascota el boton principal se llama Guardar y esta abajo a la derecha, en Registrar dueño no puede llamarse Aceptar ni estar arriba a la izquierda. Reconocer antes que recordar significa que la persona escoja de una lista en vez de acordarse de un codigo: la recepcionista no tiene por que memorizar que el codigo de raza mestiza es 07, se lo mostramos. Cada uno de estos cuatro principios se puede auditar sobre un wireframe impreso, sin una sola linea de codigo, y esa auditoria es exactamente lo que se evalua en esta asignatura.",
            "Una pantalla suelta no sirve para nada; lo que se diseña es un flujo de tarea completo, es decir el recorrido que hace una persona real desde que tiene una intencion hasta que la cumple. El flujo tiene un camino feliz y tiene caminos alternos, y los caminos alternos son donde se cae el diseño de los principiantes. En VetCare el camino feliz de registrar una mascota es: llega el dueño, la recepcionista lo busca, lo encuentra, registra la mascota y el sistema devuelve el codigo. Pero los caminos alternos son igual de reales: el dueño no esta registrado y hay que crearlo sin perder lo que ya se habia escrito de la mascota; la mascota ya existe porque otro turno la registro ayer y hay que avisarlo en vez de duplicarla; el dueño no trae documento y hay que permitir el registro con telefono como identificador temporal. En Buscar expediente pasa lo mismo: el camino feliz es buscar por documento del dueño y encontrar una sola ficha, pero hay que diseñar que ocurre cuando la busqueda por nombre devuelve doce mascotas llamadas Firulais, y ahi la respuesta de diseño es mostrar en la lista de resultados la especie, la edad y el nombre del dueño para poder desambiguar de un vistazo. Un flujo que solo dibuja el camino feliz no es un diseño, es una postal.",
            "La interfaz no se inventa: se deriva de los artefactos que el equipo ya construyo en las clases anteriores. Cada pantalla debe poder señalar el requisito funcional que la origina, cada campo debe existir en el diccionario de datos con su tipo y su longitud, y cada boton debe corresponder a una operacion que aparece en el diagrama de casos de uso o en el de secuencia. Por eso los wireframes se entregan anotados: se ponen numeritos sobre el dibujo y al lado una tabla que dice, por ejemplo, el numero uno es el campo Nombre de la mascota que sale del atributo Mascota.nombre, texto de sesenta caracteres, obligatorio, exigido por RF-03; el numero cuatro es el mensaje de confirmacion que cumple el RNF-02 de respuesta menor a tres segundos. Esa anotacion tiene un efecto secundario muy util: si aparece un campo en la pantalla que no esta en el diccionario de datos, entonces o falta un requisito o sobra el campo, y ambas cosas hay que resolverlas hoy y no cuando el compañero de Programacion II ya escribio la tabla. La trazabilidad no es burocracia, es el mecanismo que hace que los planos y la casa coincidan.",
            "Una interfaz se puede evaluar sin programarla, y esa es una de las habilidades mas valiosas que se lleva un analista. El metodo mas barato es el recorrido cognitivo: se toma una tarea concreta, por ejemplo registrar la mascota Luna de la señora Perez, y una persona que no participo en el diseño intenta hacerla sobre el prototipo sin que nadie le explique nada, mientras usted cuenta cuantos clics necesito, donde dudo y donde se equivoco. La variante de bolsillo es la prueba de pasillo: se le pide a tres compañeros de otro grupo que lo intenten y se anota, sin defenderse ni explicar. Para VetCare hay que evaluar pensando en la usuaria real, que es la recepcionista de Huellitas: no es experta en computadores, escribe lento, contesta el telefono mientras registra y tiene un perro ladrando al lado. Eso obliga a decisiones de diseño concretas: letra grande, pocos campos obligatorios, nada de scroll interminable, tolerancia a la interrupcion para que si la llaman y vuelve en tres minutos no haya perdido lo escrito, y mensajes en lenguaje de clinica y no de sistemas, es decir Esta mascota ya tiene ficha en la clinica y no Violacion de restriccion de unicidad.",
            "Error tipico del docente que no domina el tema: creer que diseñar interfaces es escoger colores y decir que quede bonito, y por lo tanto calificar el mockup mas vistoso. Eso produce tres daños. Primero, se premian pantallas lindas que no se pueden usar: fondos oscuros con letra delgada que la recepcionista no alcanza a leer, iconos sin texto que nadie entiende, animaciones que estorban. Segundo, se acepta un conjunto de pantallas sueltas sin flujo, sin caminos alternos y sin un solo mensaje de error diseñado, lo cual garantiza que en Programacion II el equipo va a improvisar la mitad del comportamiento. Tercero, se pierde la trazabilidad: aparecen campos que nadie pidio, como el correo de la mascota o el numero de chip cuando el diccionario de datos ni lo contempla, y desaparecen campos obligatorios del requisito. El antidoto es sencillo y verificable: exigir siempre wireframe antes que mockup, exigir anotaciones que citen el RF y el atributo del diccionario, exigir al menos dos caminos alternos por flujo y hacer la prueba de pasillo en clase con un otro compañero. Si el docente no se siente seguro juzgando estetica, no importa; lo que debe evaluar es si la tarea se completa sin ayuda y si cada elemento dibujado tiene un requisito que lo respalde."
        ],
        "taller": [
            "Paso 1. En Excalidraw o en papel, dibujen el wireframe en gris de la pantalla Registrar mascota de VetCare, sin colores ni logos, ubicando bloque de dueño, bloque de datos de la mascota y zona de accion; el wireframe debe caber en una sola vista sin scroll y no puede tener mas de nueve campos.",
            "Paso 2. Numeren de uno a seis los elementos criticos del wireframe y llenen la tabla de anotaciones indicando para cada numero el atributo del diccionario de datos que lo respalda, el RF que lo exige y si es obligatorio u opcional; si un elemento no tiene RF, borrenlo o creen el requisito y dejenlo escrito.",
            "Paso 3. Diseñen la pantalla Buscar expediente resolviendo explicitamente el caso de resultados multiples: definan los tres criterios de busqueda, las columnas de la lista de resultados que permiten desambiguar y el mensaje exacto que se muestra cuando no hay ningun resultado.",
            "Paso 4. Pasen las dos pantallas a Figma o Penpot como mockup y conecten minimo tres transiciones navegables: Registrar mascota hacia la confirmacion con codigo, confirmacion hacia Buscar expediente, y un resultado de la lista hacia la ficha del paciente; escriban al lado de cada transicion que principio de usabilidad estan cumpliendo.",
            "Paso 5. Hagan prueba de pasillo con otro compañero, denle la tarea registrar la mascota Luna de la señora Perez y encontrar su ficha, no le expliquen nada, cronometren, cuenten clics y anoten los dos puntos donde dudo; escriban abajo los dos cambios concretos que haran al diseño por lo observado."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ la interfaz es la cara visible del paquete de diseño de VetCare y es lo unico del PI que la clinica Huellitas entiende sin traduccion; ademas es el insumo directo con el que Programacion II construye las pantallas reales.",
            "Es la ultima clase con tema nuevo del curso: lo que se produzca hoy entra tal cual al documento final y a la sustentacion de la clase 14.",
            "Quien va solo por la ruta C cierra su PI con este prototipo navegable, que es entregable completo y valido por si mismo, no una version recortada del proyecto."
        ],
        "escenario": [
            "El equipo ya tiene aprobados los RF y RNF, el diagrama de casos de uso, el de clases con Mascota, Dueño, Historia_Clinica y Cita, y el diccionario de datos con tipos y longitudes.",
            "Hasta hoy VetCare existe solo como texto y diagramas: nadie ha visto todavia como se veria la pantalla que va a usar la recepcionista de Huellitas.",
            "La usuaria de referencia esta descrita asi: recepcionista con experiencia clinica alta y experiencia informatica baja, atiende telefono mientras registra y necesita terminar el registro de un paciente nuevo en menos de dos minutos."
        ],
        "criterios": [
            "Las dos pantallas se entregan primero como wireframe en gris y luego como mockup, y ambas versiones estan en el archivo entregado.",
            "Cada campo dibujado aparece en la tabla de anotaciones con su atributo del diccionario de datos y el RF que lo exige, sin campos huerfanos.",
            "El prototipo tiene al menos tres transiciones que funcionan al hacer clic y cubre minimo dos caminos alternos, entre ellos resultados multiples o dueño no registrado.",
            "El diseño evidencia por escrito los cuatro principios trabajados: hay mensaje de estado tras guardar, hay al menos dos mecanismos de prevencion de errores, los botones principales son consistentes entre pantallas y las listas cerradas reemplazan los campos de memoria."
        ],
        "pistas": [
            "Si la recepcionista oprime Guardar y se va al telefono treinta segundos, cuando vuelva a mirar la pantalla sabe con certeza si el registro quedo o no quedo, y por que lo sabe.",
            "De los campos que dibujaron, cuantos podria llenar mal una persona apurada, y cual de esos errores se puede volver imposible en vez de corregible.",
            "Si la busqueda por nombre devuelve doce mascotas llamadas Firulais, que dato adicional muestra la lista para que la recepcionista escoja la correcta sin abrir ninguna ficha."
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. El wireframe de Registrar mascota queda en tres bloques verticales. Bloque uno, Dueño, con un campo de busqueda por documento o telefono y un enlace secundario Registrar dueño nuevo. Bloque dos, Datos de la mascota, con Nombre, Especie como lista cerrada de Canino, Felino y Otro, Raza como lista con opcion Mestizo, Fecha de nacimiento con selector de calendario, Sexo con dos opciones visibles y Peso con la unidad kg escrita al lado del campo. Bloque tres, zona de accion abajo a la derecha con boton primario Guardar y enlace discreto Cancelar. Total nueve campos y cero scroll.",
            "Paso 2 resuelto. La tabla de anotaciones queda asi. Uno, Nombre, viene de Mascota.nombre, texto de sesenta, obligatorio, exigido por RF-03. Dos, Especie, viene de Mascota.especie, lista cerrada, obligatorio, RF-03. Tres, Fecha de nacimiento, viene de Mascota.fecha_nacimiento, tipo fecha, opcional porque muchos dueños no la saben, RF-03. Cuatro, buscador de dueño, viene de Dueño.documento, texto de quince, obligatorio antes de guardar, exigido por RF-02 y por la regla toda mascota debe tener un dueño registrado. Cinco, mensaje Ficha guardada, codigo M-0421, cumple visibilidad del estado y el RNF-02 de respuesta en menos de tres segundos. Seis, boton Guardar deshabilitado mientras falten obligatorios, cumple prevencion de errores.",
            "Paso 3 resuelto. Buscar expediente ofrece tres criterios en una sola barra con selector: documento del dueño, nombre de la mascota y codigo de ficha. La lista de resultados muestra cinco columnas, codigo, nombre de la mascota, especie, edad calculada y nombre del dueño, que es justo lo que permite desambiguar doce Firulais. Cuando no hay resultados el mensaje es No encontramos ninguna ficha con ese dato, con dos acciones sugeridas debajo, Buscar por otro criterio y Registrar mascota nueva, en vez de dejar la pantalla en blanco.",
            "Paso 4 resuelto. En Penpot se crean tres frames y se conectan. Guardar de Registrar mascota lleva al frame Confirmacion con el codigo visible, que cumple visibilidad del estado. Ver ficha de la confirmacion lleva a Buscar expediente con el codigo ya cargado, que cumple reconocer antes que recordar. Un clic sobre una fila de resultados lleva a la Ficha del paciente. Ademas se modela el camino alterno: el enlace Registrar dueño nuevo abre un frame de dueño y regresa al formulario de mascota conservando lo ya escrito.",
            "Paso 5 resuelto. La prueba de pasillo con un otro compañero arroja tipicamente que la persona duda en el buscador de dueño porque no sabe si buscar o registrar primero, y que no encuentra el boton Guardar por estar muy abajo. Los dos cambios concretos que se documentan son: poner un texto de ayuda bajo el buscador que diga Escriba el documento del dueño; si no aparece, registrelo aqui, y anclar la barra de accion al pie de la pantalla para que Guardar sea siempre visible. Se anota el tiempo antes y despues, por ejemplo dos minutos cuarenta y luego un minuto cincuenta."
        ],
        "solucion_rubrica": [
            "Wireframes en gris de las dos pantallas, con jerarquia clara y sin scroll (2)",
            "Tabla de anotaciones con trazabilidad campo a RF y a diccionario de datos (3)",
            "Prototipo navegable con tres transiciones y dos caminos alternos resueltos (3)",
            "Evidencia escrita de los cuatro principios de usabilidad y bitacora de la prueba de pasillo (2)"
        ],
        "solucion_errores": [
            "Entregar directamente el mockup bonito sin wireframe previo, lo que hace que el equipo discuta colores durante media hora y llegue a la clase 14 sin haber resuelto el flujo ni los mensajes de error.",
            "Dibujar campos que no existen en el diccionario de datos, como correo de la mascota o numero de chip, y al mismo tiempo olvidar el campo obligatorio de dueño, con lo cual la pantalla contradice el modelo de clases entregado en clases anteriores.",
            "Diseñar solo el camino feliz: no hay pantalla de resultados multiples, no hay mensaje de busqueda sin resultados y no hay confirmacion tras guardar, de modo que el prototipo se cae en la sustentacion apenas el jurado hace clic en algo distinto de lo ensayado."
        ],
        "codigo_slide_titulo": "Flujo de tarea de VetCare en Mermaid: registrar mascota y buscar expediente con caminos alternos",
        "codigo_slide_lineas": [
            "flowchart TD",
            "  A[Recepcion: llega el dueño con su mascota] --> B{Dueño ya registrado?}",
            "  B -- No --> C[Pantalla Registrar dueño]",
            "  B -- Si --> D[Pantalla Registrar mascota]",
            "  C --> D",
            "  D --> E{Campos obligatorios completos?}",
            "  E -- No --> F[Guardar deshabilitado + ayuda en el campo faltante]",
            "  F --> D",
            "  E -- Si --> G[Confirmacion: Ficha guardada, codigo M-0421]",
            "  G --> H[Pantalla Buscar expediente]",
            "  H --> I{Cuantos resultados?}",
            "  I -- Cero --> J[Mensaje sin resultados + Buscar por otro criterio]",
            "  I -- Varios --> K[Lista con especie, edad y dueño para desambiguar]",
            "  I -- Uno --> L[Ficha del paciente]"
        ],
        "codigo_slide_caption": "La interfaz no son pantallas sueltas: es un camino con desvios, y los desvios son los que hay que diseñar.",
        "artefacto_archivo": "Wireframes-Anotados-VetCare.md",
        "artefacto_contenido": "# Wireframes anotados y prototipo navegable - VetCare\n**Clinica Veterinaria Huellitas | Clase 13 - Diseño de interfaces**\n\nEstudiante: ______________________  Fecha: ____________  Version: 1.0\n\n---\n\n## 1. Usuaria de referencia\n\n| Aspecto | Descripcion |\n|---|---|\n| Rol | Recepcionista de Huellitas |\n| Experiencia clinica | Alta |\n| Experiencia informatica | Baja: escribe lento, no usa atajos |\n| Contexto de uso | Atiende telefono mientras registra, interrupciones cada 2-3 minutos |\n| Meta de tiempo | Registrar un paciente nuevo en menos de 2 minutos |\n\n---\n\n## 2. Los tres niveles (marcar lo entregado)\n\n- [ ] **Wireframe** (gris, sin color, sin logo): responde QUE informacion va y en que orden.\n- [ ] **Mockup** (color, tipografia, iconos): responde COMO SE VE.\n- [ ] **Prototipo** (con clic y transiciones): responde COMO SE SIENTE usarlo.\n\n> Regla: no se pasa a mockup hasta que el wireframe tenga anotaciones completas.\n\n---\n\n## 3. Pantalla 1: Registrar mascota\n\nPegar aqui la imagen del wireframe con numeros de 1 a N.\n\n### Tabla de anotaciones\n\n| # | Elemento en pantalla | Atributo del diccionario | Tipo / Longitud | Oblig. | RF que lo exige |\n|---|---|---|---|---|---|\n| 1 | Campo Nombre de la mascota | Mascota.nombre | Texto(60) | Si | RF-03 |\n| 2 | Lista Especie | Mascota.especie | Lista cerrada | Si | RF-03 |\n| 3 | Lista Raza | Mascota.raza | Lista(40) | No | RF-03 |\n| 4 | Selector Fecha de nacimiento | Mascota.fecha_nacimiento | Fecha | No | RF-03 |\n| 5 | Buscador de dueño | Dueño.documento | Texto(15) | Si | RF-02 |\n| 6 | Boton Guardar | operacion registrarMascota | - | - | RF-03 |\n| 7 | Mensaje de confirmacion con codigo | Mascota.codigo | Texto(8) | - | RNF-02 |\n| 8 |  |  |  |  |  |\n| 9 |  |  |  |  |  |\n\n> Si una fila no tiene RF, se borra el elemento o se crea el requisito. No hay campos huerfanos.\n\n---\n\n## 4. Pantalla 2: Buscar expediente\n\n| Decision de diseño | Su definicion |\n|---|---|\n| Criterios de busqueda | Documento del dueño / Nombre de la mascota / Codigo de ficha |\n| Columnas de la lista de resultados | Codigo, Nombre, Especie, Edad, Dueño |\n| Mensaje si hay 0 resultados | `No encontramos ninguna ficha con ese dato.` mas las acciones Buscar por otro criterio y Registrar mascota nueva |\n| Que pasa con 12 resultados iguales | Se desambigua por especie, edad y nombre del dueño sin abrir la ficha |\n| Tiempo maximo de respuesta | 3 segundos (RNF-02) |\n\n---\n\n## 5. Auditoria de los 4 principios de usabilidad\n\n| Principio | Evidencia concreta en nuestro diseño | Pantalla |\n|---|---|---|\n| Visibilidad del estado | Ej: mensaje `Ficha guardada, codigo M-0421` y boton bloqueado mientras guarda |  |\n| Prevencion de errores | Ej: calendario en vez de fecha tecleada; confirmacion antes de eliminar |  |\n| Consistencia | Ej: el boton primario siempre se llama Guardar y va abajo a la derecha |  |\n| Reconocer antes que recordar | Ej: lista cerrada de especies en vez de escribir el codigo de memoria |  |\n\n---\n\n## 6. Caminos alternos diseñados (minimo 2)\n\n| # | Camino alterno | Que hace la interfaz |\n|---|---|---|\n| A | El dueño no esta registrado | Abre Registrar dueño y regresa conservando lo escrito de la mascota |\n| B | La mascota ya tiene ficha | Avisa `Esta mascota ya tiene ficha en la clinica` y ofrece abrirla |\n| C |  |  |\n\n---\n\n## 7. Prototipo navegable\n\n| Transicion | Desde | Hacia | Principio que cumple |\n|---|---|---|---|\n| 1 | Registrar mascota (Guardar) | Confirmacion con codigo | Visibilidad del estado |\n| 2 | Confirmacion (Ver ficha) | Buscar expediente precargado | Reconocer antes que recordar |\n| 3 | Fila de resultados | Ficha del paciente | Consistencia |\n\nEnlace del prototipo (Figma o Penpot, con permiso de lectura): ______________________\n\n---\n\n## 8. Bitacora de prueba de pasillo\n\n| Probador (otro compañero) | Tarea asignada | Tiempo | Clics | Donde dudo | Donde se equivoco |\n|---|---|---|---|---|---|\n| 1 | Registrar a Luna de la señora Perez y hallar su ficha |  |  |  |  |\n| 2 |  |  |  |  |  |\n| 3 |  |  |  |  |  |\n\n**Dos cambios que haremos por lo observado:**\n1. ______________________________________________\n2. ______________________________________________\n\n---\n\n## 9. Checklist antes de subir a ExamLab\n\n- [ ] Wireframe en gris de las 2 pantallas\n- [ ] Mockup de las 2 pantallas\n- [ ] Tabla de anotaciones sin campos huerfanos\n- [ ] Minimo 3 transiciones navegables funcionando\n- [ ] Minimo 2 caminos alternos diseñados\n- [ ] Auditoria de los 4 principios diligenciada\n- [ ] Bitacora de prueba de pasillo con 3 personas\n- [ ] Enlace del prototipo con permiso de lectura, verificado desde otro navegador\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "En VetCare se dibuja en gris la pantalla Registrar mascota, sin logo ni colores, solo cajas y etiquetas, para decidir que informacion va y en que orden. Ese artefacto es:",
                "opciones": [
                    "A) Un mockup",
                    "B) Un wireframe",
                    "C) Un prototipo navegable",
                    "D) Un diagrama de secuencia"
                ],
                "clave": "B"
            },
            {
                "tipo": "om",
                "q": "Poner una lista cerrada con Canino, Felino y Otro en vez de un campo libre donde la recepcionista teclee la especie responde principalmente al principio de:",
                "opciones": [
                    "A) Visibilidad del estado del sistema",
                    "B) Estetica minimalista",
                    "C) Reconocer antes que recordar",
                    "D) Control y libertad del usuario"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Para entregar un prototipo navegable de VetCare en Figma o Penpot es necesario escribir codigo.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Despues de oprimir Guardar, la pantalla muestra el mensaje Ficha guardada, codigo M-0421 y deshabilita el boton. Esa decision cumple sobre todo:",
                "opciones": [
                    "A) Visibilidad del estado del sistema",
                    "B) Consistencia entre pantallas",
                    "C) Flexibilidad para usuarios expertos",
                    "D) Ayuda y documentacion"
                ],
                "clave": "A"
            },
            {
                "tipo": "vf",
                "q": "Todo campo dibujado en un wireframe de VetCare debe existir en el diccionario de datos y poder citar el RF que lo exige.",
                "clave": "V"
            },
            {
                "tipo": "om",
                "q": "La busqueda por nombre devuelve doce mascotas llamadas Firulais. La mejor decision de diseño es:",
                "opciones": [
                    "A) Mostrar solo el primer resultado para no confundir",
                    "B) Obligar a buscar siempre por codigo de ficha",
                    "C) Mostrar la lista con especie, edad y nombre del dueño para desambiguar",
                    "D) Mostrar un mensaje de error por busqueda ambigua"
                ],
                "clave": "C"
            },
            {
                "tipo": "abierta",
                "q": "Mencione dos mecanismos de prevencion de errores que aplicaria en la pantalla Registrar mascota de VetCare, sabiendo que la recepcionista trabaja con interrupciones.",
                "clave": "Se esperan dos de estos: selector de calendario en vez de fecha tecleada; listas cerradas para especie y raza; boton Guardar deshabilitado hasta que los obligatorios esten completos; validacion de mascota duplicada por dueño mas nombre con aviso antes de guardar; confirmacion explicita antes de eliminar o de salir sin guardar; conservacion de lo escrito al ir a registrar el dueño."
            },
            {
                "tipo": "abierta",
                "q": "Explique en que consiste una prueba de pasillo y que se debe medir en ella para el prototipo de VetCare.",
                "clave": "Consiste en pedirle a dos o tres personas ajenas al documento que ejecuten una tarea concreta sobre el prototipo sin ninguna explicacion previa, mientras el equipo observa en silencio. Se mide el tiempo para completar la tarea, la cantidad de clics, los puntos donde la persona dudo y los errores cometidos; el resultado se convierte en cambios concretos al diseño, no en explicaciones al probador."
            }
        ]
    },
    {
        "n": 14,
        "slug": "Preparacion de la sustentacion y cierre",
        "titulo": "Preparacion de la sustentacion y cierre",
        "subtitulo": "Como se defiende un paquete de planos frente a un jurado",
        "herramienta": "Google Docs · draw.io · Figma o Penpot",
        "hito_pi": "Queda armado el guion cronometrado de sustentacion de VetCare y consolidado el documento final de diseño en una sola pieza coherente.",
        "entregable": "Un documento en Google Docs con el guion minuto a minuto repartido en bloques con tiempos y evidencia (con responsable nominal solo si el docente autorizo equipo), la tabla de tres decisiones de diseño defendidas y el banco de diez preguntas con su respuesta, mas el indice del documento final consolidado, subido a ExamLab.",
        "demo": "El docente proyecta una sustentacion mal hecha y una bien hecha del mismo paquete VetCare, y luego arma en vivo la tabla de decisiones para justificar por que Historia_Clinica es una clase aparte de Mascota.",
        "teoria": [
            "Sustentar un paquete de diseño no es leer diapositivas ni narrar lo que el equipo hizo cada semana: es demostrar que las decisiones tomadas son defendibles. El jurado, sea el docente o un cliente simulado de la clinica Huellitas, no esta evaluando cuanto trabajaron sino tres cosas concretas: si el diseño resuelve el problema declarado, si las piezas son coherentes entre si y si el equipo entiende lo que entrego. Por eso una sustentacion es un argumento con evidencia, no un recuento cronologico. La diferencia se nota en la primera frase: quien dice hicimos casos de uso, luego clases, luego pantallas, esta narrando; quien dice Huellitas pierde fichas y tarda ocho minutos en encontrar un historial, y este paquete de diseño ataca esos tres problemas asi, esta sustentando. En VetCare la evidencia esta toda disponible: la tabla de RF y RNF, los diagramas UML, el diccionario de datos y el prototipo navegable. El trabajo de hoy es ordenar esa evidencia para que cuente una sola historia.",
            "El orden de la sustentacion no es libre, es un embudo y tiene una razon logica. Primero el problema, porque nada de lo que sigue tiene sentido si el jurado no sabe que duele en Huellitas. Segundo los requisitos, porque son la promesa concreta: que va a hacer el sistema y con que restricciones. Tercero el modelo, casos de uso y clases, porque muestra como se organiza la solucion. Cuarto la interfaz, porque es donde el jurado por fin ve y toca. Y quinto las decisiones, que es la parte que separa a un equipo que entendio de uno que copio plantillas. Invertir ese orden es el error mas comun: los equipos empiezan mostrando pantallas bonitas, el jurado pregunta que problema resuelve eso y ahi la sustentacion se desarma. Para VetCare doce minutos alcanzan de sobra si se respetan las proporciones: uno y medio para el problema, tres para requisitos, dos para modelo, dos para interfaz en vivo, dos para decisiones y el resto para riesgos y cierre.",
            "Defender una decision de diseño tiene una estructura fija que conviene memorizar: decision, alternativas consideradas, criterio de eleccion y consecuencia asumida. No basta decir que se hizo, hay que decir contra que se comparo y por que gano. Ejemplo concreto de VetCare: decidimos separar Historia_Clinica de Mascota como clases distintas; la alternativa era guardar diagnosticos y tratamientos como campos dentro de Mascota; el criterio fue que una mascota tiene muchas consultas a lo largo de su vida y una relacion uno a muchos no cabe en campos fijos; la consecuencia es que hay una entidad mas y una consulta adicional al mostrar la ficha, lo cual se acepta porque el RNF de busqueda menor a tres segundos se sostiene con un indice. Otro ejemplo: decidimos que la fecha de nacimiento sea opcional; la alternativa era hacerla obligatoria; el criterio fue que en Huellitas muchos dueños de mascotas rescatadas no la conocen y un campo obligatorio los llevaria a inventar datos; la consecuencia es que la edad se muestra como aproximada cuando el dato falta. Una decision defendida asi resiste cualquier pregunta, porque el jurado ya sabe que el equipo penso en la alternativa.",
            "Las preguntas del jurado son bastante predecibles y por eso se preparan. Las mas frecuentes en un proyecto como VetCare son: como sabe usted que este requisito es realmente necesario; que pasa si dos recepcionistas registran la misma mascota al mismo tiempo; por que esta clase existe y no es un atributo de otra; como se cumple el requisito no funcional que usted escribio y como se mediria; que pasa si el sistema se cae a mitad de un registro; que dejaron por fuera del alcance y por que; y quien de ustedes hizo esta parte. Hay que preparar la respuesta de cada una en dos frases, sin discursos. Y hay una regla de oro para cuando no se sabe: no se inventa. La respuesta correcta es reconocer el vacio y proponer como se resolveria, por ejemplo no lo modelamos, lo registramos como riesgo abierto y se resolveria agregando una validacion de unicidad por dueño mas nombre en el diccionario de datos. Un jurado castiga mucho mas la improvisacion detectada que la honestidad tecnica.",
            "El reparto del guion en bloques con tiempos es criterio de evaluacion, no un detalle logistico. La sustentacion es individual por defecto: el estudiante expone los cinco bloques y responde por todos, y lo que se califica es que cada bloque tenga su rango de minutos y su evidencia en pantalla, no quien lo dice. El orden que funciona para VetCare es: abrir con problema y alcance, seguir con requisitos y trazabilidad, luego los modelos UML, despues el prototipo en vivo y cerrar con decisiones, riesgos y siguiente paso hacia Programacion II. Si el docente autorizo equipo de 2 o 3, se agrega el nombre del responsable a cada bloque, todos los integrantes deben hablar al menos dos minutos y ninguno puede hablar solo de lo suyo: cada persona domina una pieza pero debe conocer el todo, porque el jurado tiene derecho a preguntarle a cualquiera sobre cualquier parte. Se ensaya cronometrado al menos dos veces, en voz alta y de pie, porque el tiempo estimado leyendo en silencio siempre es la mitad del real. Ademas se prepara el plan B tecnico: capturas del prototipo por si falla el internet, el documento en PDF descargado y los diagramas exportados a imagen. Y algo que parece obvio pero se olvida siempre: quien maneja el prototipo debe haberlo recorrido antes haciendo clic en cosas que no estaban en el guion, porque el jurado va a hacer exactamente eso.",
            "Error tipico del docente que no domina el tema: tratar la sustentacion como un tramite y evaluarla por la calidad de las diapositivas o por la fluidez del que mas habla. Eso produce tres distorsiones. Primera, se premia a quien mejor habla aunque su diseño sea inconsistente, y se castiga al estudiante timido cuyo paquete es impecable. Segunda, al no preguntar por trazabilidad, el docente no detecta que el prototipo muestra campos que no estan en el diccionario de datos o que hay un RF que ningun diagrama cubre, que es justo lo que va a explotar en Programacion II. Tercera, al no exigir decisiones justificadas, se acepta el como sin el por que y el estudiante nunca desarrolla el criterio profesional, que es el objetivo real de la asignatura. El antidoto es tener una lista fija de preguntas de trazabilidad y hacerlas siempre: señale en el diagrama de clases donde vive el RF-04; muestre el campo de esta pantalla en el diccionario de datos; digame que alternativa descartaron aqui y con que criterio; y dirigirlas a cualquier parte del paquete, no solo a la que el estudiante acaba de exponer (si hay equipo, a un integrante distinto del que expuso esa parte)."
        ],
        "taller": [
            "Paso 1. Arme en Google Docs el guion cronometrado de doce minutos con las cinco secciones obligatorias en orden problema, requisitos, modelo, interfaz y decisiones, asignando a cada bloque su rango de minutos exacto y la evidencia que se muestra en pantalla en ese bloque; ningun bloque puede quedar sin rango de minutos ni sin evidencia asociada. Si el docente autorizo equipo, escriba ademas el nombre del responsable de cada bloque y reparta de modo que ningun integrante quede con menos de dos minutos.",
            "Paso 2. Llenen la tabla de tres decisiones de diseño de VetCare con las cuatro columnas decision, alternativa descartada, criterio y consecuencia asumida; una de las tres decisiones debe ser sobre el modelo de clases y otra sobre un requisito no funcional.",
            "Paso 3. Construyan el banco de diez preguntas del jurado con su respuesta en maximo dos frases, incluyendo obligatoriamente que pasa si dos recepcionistas registran la misma mascota, como se mide su RNF de tiempo de respuesta y que quedo fuera del alcance.",
            "Paso 4. Haga un ensayo cronometrado de pie, con el prototipo abierto, y registre el tiempo real de cada bloque; recorte lo que se paso y anote los dos puntos donde se enredo al hablar (si trabaja en equipo, donde se enredo la transicion entre un expositor y el siguiente).",
            "Paso 5. Consoliden el documento final armando el indice completo desde problema hasta trazabilidad, verifiquen que los nombres de las clases, los campos del diccionario y los campos de las pantallas coinciden exactamente, y corrijan al menos una inconsistencia encontrada dejando constancia de cual era."
        ],
        "contexto": [
            "@@Por que importa al PI:@@ hoy se convierte el monton de artefactos de VetCare en un solo paquete defendible, y se ensaya la unica ocasion en que el equipo tiene que demostrar que entiende lo que entrego.",
            "No hay tema nuevo: todo el trabajo es de consolidacion, coherencia y argumentacion sobre lo ya producido.",
            "Las inconsistencias que se detecten hoy son baratas de arreglar; las mismas inconsistencias detectadas por el jurado o por el equipo de Programacion II salen carisimas."
        ],
        "escenario": [
            "El equipo tiene todos los artefactos de VetCare producidos, pero dispersos en varios archivos y con pequeñas contradicciones entre ellos.",
            "Nadie ha dicho todavia en voz alta la historia completa del proyecto de principio a fin, y el reparto de quien expone que no esta definido.",
            "El prototipo navegable existe y funciona, pero solo lo ha manejado la persona que lo dibujo."
        ],
        "criterios": [
            "El guion tiene las cinco secciones en el orden problema, requisitos, modelo, interfaz y decisiones, con minutos asignados que suman doce, cada bloque con su evidencia en pantalla y, si el docente autorizo equipo, todos los integrantes hablando al menos dos minutos.",
            "Las tres decisiones de diseño estan escritas con las cuatro columnas completas, incluida la consecuencia asumida, y ninguna se justifica por gusto o por costumbre.",
            "El banco tiene diez preguntas con respuesta de maximo dos frases y contempla al menos un caso de concurrencia, uno de medicion de RNF y uno de alcance excluido.",
            "El documento final consolidado tiene indice, version y al menos una inconsistencia entre artefactos detectada y corregida, dejando registro de cual era."
        ],
        "pistas": [
            "Si el jurado le pregunta por una parte que no alcanzo a mostrar, puede responderla sin buscar ayuda (y si hay equipo autorizado, cualquier integrante puede responder por cualquier bloque).",
            "De sus tres decisiones de diseño, cual podria haberse tomado al reves sin que el proyecto se cayera, y que perderia la clinica si se hubiera tomado asi.",
            "Si el internet falla justo antes de mostrar el prototipo, que hace el equipo en los siguientes quince segundos para no perder el bloque de interfaz."
        ],
        "solucion_pasos": [
            "Paso 1 resuelto. El guion queda repartido en bloques tematicos asi, y esto es identico para quien sustenta solo y para un equipo autorizado. Minuto 0 a 1:30, Problema, con la frase de apertura Huellitas extravia fichas, tarda ocho minutos en hallar un historial y no tiene una sola metrica de atencion. Minuto 1:30 a 5:00, Alcance y requisitos, mostrando la tabla RF-01 a RF-08 con prioridad y los dos RNF que si se van a demostrar. Minuto 5:00 a 7:00, Modelos, con casos de uso y clases. Minuto 7:00 a 9:00, Interfaz en vivo, recorriendo registrar mascota y buscar expediente. Minuto 9:00 a 11:30, Decisiones y riesgos. Minuto 11:30 a 12:00, cierre con la frase de valor para la clinica. En modo individual el estudiante expone los seis bloques y el puntaje se gana por tener los rangos de minutos escritos y la evidencia asignada a cada bloque, no por repartir nombres. Si el docente autorizo equipo, se escribe al lado de cada bloque el nombre del responsable y ningun integrante queda con menos de dos minutos.",
            "Paso 2 resuelto. La tabla de decisiones queda asi. Decision uno, separar Historia_Clinica de Mascota; alternativa, guardar diagnosticos como campos dentro de Mascota; criterio, una mascota tiene muchas consultas y la relacion es uno a muchos; consecuencia, una entidad mas y una consulta adicional al abrir la ficha. Decision dos, RNF-02 de busqueda de expediente en menos de tres segundos con hasta cinco mil fichas; alternativa, no fijar tiempo; criterio, el dolor declarado por la clinica es la demora, asi que sin numero no hay como demostrar mejora; consecuencia, obliga a definir indice por documento del dueño y por codigo. Decision tres, fecha de nacimiento opcional; alternativa, obligatoria; criterio, muchos dueños de mascotas rescatadas no la conocen y la obligatoriedad genera datos inventados; consecuencia, la edad se muestra como aproximada cuando el dato falta.",
            "Paso 3 resuelto. Entre las diez preguntas quedan resueltas al menos estas tres. Que pasa si dos recepcionistas registran la misma mascota al tiempo: se define regla de unicidad por documento del dueño mas nombre de la mascota y la interfaz avisa Esta mascota ya tiene ficha en la clinica antes de guardar. Como mide su RNF de tiempo: se cronometra la busqueda por documento con una base de prueba de cinco mil fichas y se exige que el promedio de diez intentos sea menor a tres segundos. Que quedo fuera del alcance: facturacion, inventario de medicamentos y agenda automatica de vacunacion, porque los tres problemas declarados por Huellitas son extravio, demora y falta de metricas.",
            "Paso 4 resuelto. El primer ensayo tipicamente da diecisiete minutos en vez de doce, con el bloque de requisitos desbordado porque el expositor lee toda la tabla. La correccion documentada es no leer la tabla completa sino mostrar solo los tres RF criticos y decir que los demas estan en el documento, y practicar la transicion entre modelo e interfaz, que es donde el equipo suele quedarse callado buscando la pestaña del prototipo. Se anota el tiempo antes y despues por bloque.",
            "Paso 5 resuelto. Al consolidar aparece al menos una inconsistencia clasica, por ejemplo que en el diagrama de clases el atributo se llama fechaNacimiento, en el diccionario de datos aparece como fecha_nac y en la pantalla el rotulo dice Fecha de nacimiento aproximada. Se unifica a fecha_nacimiento en modelo y diccionario, se deja el rotulo humano en la pantalla y se anota la correccion en la bitacora de la version 1.0. El indice del documento final queda con nueve secciones, desde problema y alcance hasta acta de entrega."
        ],
        "solucion_rubrica": [
            "Guion cronometrado en el orden correcto, con los 5 bloques con minutos y evidencia y sin bloques huerfanos (si hay equipo autorizado, todos los integrantes con minimo 2 minutos) (3)",
            "Tabla de tres decisiones con alternativa, criterio y consecuencia (3)",
            "Banco de diez preguntas con respuestas de dos frases, incluyendo concurrencia, RNF y alcance (2)",
            "Documento final consolidado con indice, version e inconsistencia corregida documentada (2)"
        ],
        "solucion_errores": [
            "Contar la historia al reves, empezando por las pantallas bonitas, de modo que el jurado interrumpe preguntando que problema resuelve eso y el equipo pierde el hilo y el tiempo.",
            "Justificar decisiones con frases vacias como asi lo vimos en clase o porque quedaba mas ordenado, sin alternativa descartada ni criterio, lo cual delata que el equipo copio una plantilla en vez de diseñar.",
            "Que un solo integrante hable el ochenta por ciento del tiempo y los demas digan una frase, con el agravante de que ninguno puede responder preguntas fuera de su parte porque nunca leyeron el paquete completo."
        ],
        "codigo_slide_titulo": "Guion de sustentacion VetCare: doce minutos cronometrados y quien dice que",
        "codigo_slide_lineas": [
            "00:00-01:30 | PROBLEMA    | Huellitas: fichas extraviadas, 8 min por historial, cero metricas",
            "01:30-03:00 | ALCANCE     | Lo que si entra y lo que quedo por fuera, con la razon",
            "03:00-05:00 | REQUISITOS  | Solo los 3 RF criticos y 2 RNF medibles; el resto en el documento",
            "05:00-07:00 | MODELO      | Casos de uso y clases: Mascota, Dueño, Historia_Clinica, Cita",
            "07:00-09:00 | INTERFAZ    | Prototipo en vivo: registrar mascota -> confirmacion -> buscar",
            "09:00-11:00 | DECISIONES  | 3 decisiones con alternativa descartada, criterio y consecuencia",
            "11:00-11:30 | RIESGOS     | Que queda abierto y que recibe Programacion II",
            "11:30-12:00 | CIERRE      | Una frase de valor para la clinica, no un resumen",
            "--- Reparto: todos hablan minimo 2 minutos y todos responden minimo 1 pregunta",
            "--- Regla: nadie lee la diapositiva; la diapositiva es el plano, la voz es el argumento",
            "--- Cada pantalla proyectada debe poder señalar el RF que la origina",
            "--- Plan B: capturas del prototipo, PDF descargado y diagramas exportados a imagen"
        ],
        "codigo_slide_caption": "Un paquete de diseño no se narra en orden cronologico: se defiende en orden de embudo, del dolor a la decision.",
        "artefacto_archivo": "Guion-y-Decisiones-Sustentacion-VetCare.md",
        "artefacto_contenido": "# Guion de sustentacion y decisiones de diseño - VetCare\n**Clinica Veterinaria Huellitas | Clase 14 - Preparacion de la sustentacion**\n\nEstudiante: ______________________  Fecha: ____________  Duracion objetivo: 12 minutos\n\n---\n\n## 1. Frase de apertura (se aprende de memoria, maximo 25 palabras)\n\n> _Ejemplo:_ En Huellitas se extravian fichas, encontrar un historial toma ocho minutos y no existe una sola metrica de atencion. Estos son los planos que lo resuelven.\n\nNuestra frase: ______________________________________________\n\n---\n\n## 2. Guion cronometrado y reparto\n\n| Bloque | Minutos | Contenido exacto que se muestra | Evidencia en pantalla | Responsable (solo si hay equipo) |\n|---|---|---|---|---|\n| Problema | 00:00-01:30 | Los 3 dolores de Huellitas |  |  |\n| Alcance | 01:30-03:00 | Que entra y que NO entra, con razon |  |  |\n| Requisitos | 03:00-05:00 | 3 RF criticos y 2 RNF medibles |  |  |\n| Modelo | 05:00-07:00 | Casos de uso y diagrama de clases |  |  |\n| Interfaz | 07:00-09:00 | Prototipo en vivo, 1 flujo completo |  |  |\n| Decisiones | 09:00-11:00 | Tabla de 3 decisiones |  |  |\n| Riesgos y siguiente paso | 11:00-11:30 | Lo abierto y el handoff |  |  |\n| Cierre | 11:30-12:00 | Frase de valor |  |  |\n\n> Regla: todos los bloques llevan su rango de minutos y su evidencia en pantalla, y quien sustenta debe poder responder sobre cualquier parte. Si el docente autorizo equipo, ademas ningun integrante habla menos de 2 minutos.\n\n---\n\n## 3. Tabla de decisiones de diseño (minimo 3)\n\n| # | Decision tomada | Alternativa descartada | Criterio de eleccion | Consecuencia asumida |\n|---|---|---|---|---|\n| 1 | Historia_Clinica es clase aparte de Mascota | Guardar diagnosticos como campos de Mascota | Una mascota tiene muchas consultas: relacion 1 a N | Una entidad mas y una consulta extra al abrir la ficha |\n| 2 | RNF-02: buscar expediente en menos de 3 s con 5.000 fichas | No fijar tiempo | El dolor declarado es la demora; sin numero no hay mejora demostrable | Obliga a indice por documento del dueño y por codigo |\n| 3 | Fecha de nacimiento opcional | Campo obligatorio | Muchos dueños de rescatados no la saben; obligar genera datos inventados | La edad se muestra como aproximada cuando falta |\n| 4 |  |  |  |  |\n\n> Una decision sin alternativa descartada NO es una decision, es una costumbre.\n\n---\n\n## 4. Banco de preguntas del jurado (minimo 10)\n\n| # | Pregunta esperada | Respuesta en maximo 2 frases | Quien responde |\n|---|---|---|---|\n| 1 | Como saben que este requisito es necesario? |  |  |\n| 2 | Que pasa si dos recepcionistas registran la misma mascota al tiempo? |  |  |\n| 3 | Por que esta clase existe y no es un atributo de otra? |  |  |\n| 4 | Como mediria usted su RNF de tiempo de respuesta? |  |  |\n| 5 | Que pasa si el sistema se cae a mitad de un registro? |  |  |\n| 6 | Que dejaron fuera del alcance y por que? |  |  |\n| 7 | Donde vive el RF-04 en el diagrama de clases? |  |  |\n| 8 | Este campo de la pantalla, en que parte del diccionario esta? |  |  |\n| 9 | Que cambiarian si Huellitas abre una segunda sede? |  |  |\n| 10 | Quien hizo esta parte y por que la hizo asi? |  |  |\n\n**Regla de oro:** si no lo sabe, no lo invente. Diga: `no lo modelamos, lo registramos como riesgo abierto y se resolveria asi...`\n\n---\n\n## 5. Checklist de consolidacion del documento final\n\n- [ ] Portada con nombre del proyecto, autor o autores y version\n- [ ] Indice con numeracion\n- [ ] Problema y alcance (que entra / que no entra)\n- [ ] Tabla RF y RNF con prioridad\n- [ ] Diagrama de casos de uso\n- [ ] Diagrama de clases\n- [ ] Diagrama de secuencia del flujo critico\n- [ ] Wireframes anotados y enlace al prototipo\n- [ ] Diccionario de datos\n- [ ] Tabla de decisiones de diseño\n- [ ] Matriz de trazabilidad RF -> pantalla -> clase\n- [ ] **Verificacion de nombres**: los atributos se llaman IGUAL en clases, diccionario y anotaciones de pantalla\n\n**Inconsistencia encontrada y corregida hoy:** ______________________________________________\n\n---\n\n## 6. Ensayo cronometrado\n\n| Ensayo | Tiempo real total | Bloque que se paso | Correccion aplicada |\n|---|---|---|---|\n| 1 |  |  |  |\n| 2 |  |  |  |\n\n**Plan B tecnico:** [ ] capturas del prototipo  [ ] documento en PDF descargado  [ ] diagramas exportados a imagen  [ ] alguien mas sabe manejar el prototipo\n",
        "quiz": [
            {
                "tipo": "om",
                "q": "El orden recomendado para sustentar el paquete de diseño de VetCare es:",
                "opciones": [
                    "A) Interfaz, modelo, requisitos, problema, decisiones",
                    "B) Problema, requisitos, modelo, interfaz, decisiones",
                    "C) Cronologia del trabajo semana a semana",
                    "D) Decisiones, problema, interfaz, requisitos, modelo"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Una decision de diseño queda bien defendida diciendo que asi se hizo porque quedaba mas ordenado.",
                "clave": "F"
            },
            {
                "tipo": "om",
                "q": "Los cuatro elementos que debe tener una decision de diseño bien sustentada son:",
                "opciones": [
                    "A) Autor, fecha, herramienta y version",
                    "B) Decision, alternativa descartada, criterio y consecuencia asumida",
                    "C) Requisito, clase, pantalla y prueba",
                    "D) Problema, solucion, presupuesto y cronograma"
                ],
                "clave": "B"
            },
            {
                "tipo": "vf",
                "q": "Si el docente autoriza trabajo en equipo, en la sustentacion todos los integrantes deben hablar y cualquiera puede recibir preguntas sobre partes que no expuso.",
                "clave": "V"
            },
            {
                "tipo": "om",
                "q": "El jurado pregunta algo que el equipo no modelo. La conducta correcta es:",
                "opciones": [
                    "A) Improvisar una respuesta tecnica que suene convincente",
                    "B) Decir que eso lo hace Programacion II y seguir",
                    "C) Reconocer el vacio, registrarlo como riesgo abierto y proponer como se resolveria",
                    "D) Pedir que la pregunta se haga al final por falta de tiempo"
                ],
                "clave": "C"
            },
            {
                "tipo": "vf",
                "q": "Leer en voz alta el contenido de la diapositiva es una practica aceptable si el texto es correcto.",
                "clave": "F"
            },
            {
                "tipo": "abierta",
                "q": "Defienda con el formato completo la decision de separar Historia_Clinica de Mascota en el modelo de VetCare.",
                "clave": "Decision: Historia_Clinica se modela como clase independiente asociada a Mascota. Alternativa descartada: guardar diagnosticos y tratamientos como campos dentro de Mascota. Criterio: una mascota tiene muchas consultas a lo largo de su vida, es una relacion uno a muchos que no cabe en campos fijos y ademas se necesita el historial ordenado por fecha para las metricas. Consecuencia asumida: una entidad adicional y una consulta extra al abrir la ficha, aceptable porque el RNF de busqueda menor a tres segundos se sostiene con indice."
            },
            {
                "tipo": "abierta",
                "q": "Escriba una pregunta frecuente del jurado sobre requisitos no funcionales en VetCare y su respuesta en maximo dos frases.",
                "clave": "Pregunta esperada: como mide usted que la busqueda de expediente tarda menos de tres segundos. Respuesta: se cronometra la busqueda por documento del dueño sobre una base de prueba de cinco mil fichas y se exige que el promedio de diez intentos sea menor a tres segundos; si no se cumple, se agrega indice por documento y por codigo de ficha."
            }
        ]
    },
    {
        "n": 15,
        "slug": "Parcial 3",
        "titulo": "Parcial 3",
        "subtitulo": "Solo evaluacion",
        "herramienta": "—",
        "hito_pi": "No avanza el PI (dia de evaluacion)",
        "entregable": "—",
        "demo": "—",
        "teoria": [],
        "taller": [],
        "quiz": []
    }
]
