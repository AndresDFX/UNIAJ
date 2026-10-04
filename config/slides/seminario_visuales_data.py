# -*- coding: utf-8 -*-
"""Lamina de cada concepto de Seminario de Sistemas: su titulo, sus ideas y su visual.

Por que existe
--------------
En Seminario la teoria no viene en secciones `###` sino en parrafos (`teoria` + `fundamento`
de `seminario_clases_data.py`), y `teoria_a_slides` titula cada lamina con la frase que abre
el parrafo, cortada a 72 caracteres: «Vale la pena decir con precision que produce cada
fase, porque ahi se...». Eso no es un titulo. Y las ideas que extrae en modo concepto son la
primera clausula de cada frase, que en parrafos con enumeraciones deja fragmentos sueltos
(«Cuando el sistema es critico o esta regulado (equipos medicos.»).

Aqui se fija, por concepto, lo que se PROYECTA: un titulo que dice lo que es y 3-4 ideas
completas, fieles al parrafo. El parrafo entero sigue yendo a las notas del presentador
(«DESARROLLO»), asi que nada se pierde: solo deja de proyectarse cortado.

Clave: el comienzo del titulo que `teoria_a_slides` le da al parrafo (su primera frase, ya
filtrada por `_deck`), comparado sin tildes ni mayusculas por `visuales.spec_de`.

- ``LAMINAS[n][clave]`` = ``{"titulo": ..., "ideas": [...]}``.
- ``VISUALES[n][clave]`` = ``{"anim": "seminario/claseN/<huella>"}`` (las fotos se retiraron: solo animaciones e ilustraciones generadas):
  la animacion se renderiza con `config/animaciones/renderizar.py seminario/claseN` y sus pasos
  aparecen uno por clic; la foto (Pexels) va donde el concepto es contexto y no proceso.

Ninguna idea nombra el proyecto del curso ni la actividad evaluada: el ejemplo es «la clinica».
"""

LAMINAS = {
    1: {
        "Programar es escribir codigo": {
            "titulo": "Programar no es lo mismo que hacer ingeniería de software",
            "ideas": [
                "Programar es escribir código que funcione hoy.",
                "La ingeniería de software son las prácticas que lo mantienen funcionando cuando "
                "el sistema crece, cambia de manos o cambian los requisitos.",
                "La razón es económica: un error hallado al analizar requisitos cuesta una fracción "
                "de lo que cuesta en producción, con usuarios reales encima.",
                "Esa curva de costo es la que justifica todas las metodologías del curso.",
            ]},
        "Proyecto y producto": {
            "titulo": "Proyecto y producto",
            "ideas": [
                "El producto es el software y su documentación: lo que queda cuando todos se van.",
                "El proyecto es el esfuerzo acotado en tiempo y recursos para construirlo.",
                "Un proyecto termina; un producto puede seguir vivo diez años.",
                "En la clínica, el proyecto es el semestre; el producto es el sistema que usaría todos los días.",
            ]},
        "Un requisito funcional dice": {
            "titulo": "Requisito funcional y no funcional",
            "ideas": [
                "Funcional: QUÉ hace el sistema. «Registrar una mascota con ID, nombre y especie».",
                "No funcional: CÓMO se comporta. «La búsqueda responde en menos de 2 s».",
                "Los no funcionales son los que más se olvidan y los que más condicionan la arquitectura.",
                "Si no se puede verificar, no es un requisito: es un deseo.",
            ]},
        "Los interesados no son solo": {
            "titulo": "Los interesados y sus conflictos",
            "ideas": [
                "Los interesados no son solo quien paga.",
                "En la clínica: el dueño quiere métricas, la recepcionista agendar rápido, "
                "el veterinario el historial a la mano.",
                "Chocan: más datos dan mejores métricas pero hacen más lento el registro.",
                "Decidir qué se prioriza y dejar escrito por qué es trabajo de análisis, no de programación.",
            ]},
        "Todo desarrollo pasa por las mismas fases": {
            "titulo": "Las mismas fases, distinto recorrido",
            "ideas": [
                "Todo desarrollo pasa por requisitos, diseño, construcción, pruebas y mantenimiento.",
                "Entre metodologías no cambian las fases: cambia cómo se recorren, una vez en orden "
                "o en ciclos cortos.",
                "En esta asignatura no se construye la casa: se dibujan los planos para que cualquier "
                "equipo pueda construirla.",
                "Los recorridos se comparan a fondo en las clases 2, 3 y 4.",
            ]},
        "Para que sirve documentar": {
            "titulo": "Para qué documentar: depende de quién lee",
            "ideas": [
                "El código lo lee la máquina y quien ya conoce el sistema.",
                "Los planos los lee quien todavía no lo conoce: el compañero nuevo, quien revisa, "
                "el equipo que va a construir, y usted mismo en seis semanas.",
                "Documentar es dejar escritas las decisiones y su justificación, para que otro "
                "continúe sin volver a entrevistar al cliente.",
                "Cada artefacto tiene un lector concreto que debe poder trabajar con él sin preguntar.",
            ]},
        "El mapa del semestre": {
            "titulo": "El mapa del semestre",
            "ideas": [
                "Clases 1 a 4: cómo se organiza el trabajo (ciclos de vida, metodologías tradicionales y ágiles).",
                "Clases 6 a 9: qué debe hacer el sistema (requisitos, historias de usuario, UML y casos de uso).",
                "Clases 11 a 14: cómo se ve y cómo se sustenta (auditoría, diagramas dinámicos, interfaces).",
                "Todo se acumula en un único paquete de diseño: nada se bota al terminar la clase.",
            ]},
        "Hay un concepto que explica": {
            "titulo": "La deuda técnica",
            "ideas": [
                "Elegir la salida rápida es pedir prestado tiempo al futuro, y se paga con intereses en cada cambio.",
                "La metáfora es de Ward Cunningham (1992), sobre código; vale igual para el diseño.",
                "Caso típico: nadie decide si una Mascota puede existir sin Dueño; tres semanas después "
                "hay dos documentos que se contradicen.",
                "Los equipos maduros reservan del 10 al 20 % de cada iteración para pagar deuda.",
            ]},
        "En un curso de diseno la deuda": {
            "titulo": "El artefacto desactualizado",
            "ideas": [
                "Un diagrama que ya no corresponde a la decisión vigente es peor que no tener "
                "diagrama: el que falta obliga a preguntar, el equivocado convence.",
                "Regla 1: cada artefacto lleva fecha y versión visibles.",
                "Regla 2: si una decisión cambia, el artefacto se actualiza esa semana y el cambio "
                "queda anotado con fecha y motivo.",
                "Cambiar de opinión es normal; tener dos verdades circulando es el error.",
            ]},
        "El segundo concepto de fondo": {
            "titulo": "Qué es un modelo",
            "ideas": [
                "Un modelo es una representación simplificada de algo real, hecha para responder "
                "preguntas acotadas.",
                "Un modelo útil es incompleto a propósito: el mapa no es el territorio.",
                "Para cada diagrama hay que poder nombrar qué pregunta responde y quién la hace; "
                "si no, el diagrama no va.",
                "Casos de uso responde quién hace qué; no cuánto tarda una búsqueda.",
            ]},
        "De ahi se sigue": {
            "titulo": "Dos maneras de que un modelo falle",
            "ideas": [
                "Incompleto donde no debía: omite lo que importaba para su pregunta.",
                "Ruido con apariencia de rigor: tanto detalle que nadie lo lee. Es la falla más común.",
                "Referencias del curso: un diagrama de casos de uso legible rara vez pasa de 15 a 20 "
                "casos; una historia cabe en dos o tres líneas.",
                "Prueba: un compañero ajeno lo explica en tres minutos. Lo que no pueda explicar, no comunica.",
            ]},
        "Lo anterior conduce al criterio": {
            "titulo": "Cinco rasgos de un documento usable",
            "ideas": [
                "Tiene lector y pregunta · es verificable · es trazable · está fechado y versionado · "
                "es accionable.",
                "De relleno: «el sistema debe ser amigable e intuitivo». Nadie puede construirlo "
                "ni decir si se cumplió.",
                "Usable: RF-012 registrar mascota con cinco datos y dueño asociado, con criterio de "
                "aceptación, origen y prioridad.",
                "Fuera: la definición copiada, la historia de la disciplina y las promesas sin sujeto.",
            ]},
        "El rasgo tres merece": {
            "titulo": "Trazabilidad: el hilo del semestre",
            "ideas": [
                "Seguir un requisito desde quien lo pidió hasta el artefacto que lo resuelve y el "
                "criterio que lo verifica.",
                "La cadena: entrevista → requisito (clase 6) → historia (7) → caso de uso (9) → "
                "pantalla (13) → criterio de aceptación.",
                "Dos controles: todo RF aparece en algún caso de uso, y todo caso de uso señala su RF.",
                "Un requisito huérfano es algo que nadie necesita o un hueco que nadie notó.",
            ]},
    },
    2: {
        "Un ciclo de vida del software": {
            "titulo": "Qué es un ciclo de vida",
            "ideas": [
                "El orden en que se recorren las etapas, desde «necesito un sistema» hasta que el "
                "sistema se apaga.",
                "Cinco etapas clásicas: requisitos, diseño, construcción, pruebas y mantenimiento.",
                "Cada fase tiene una entrada, un artefacto de salida y un criterio para decir «esto ya quedó».",
                "Si una fase no produce un artefacto verificable, no existe: existe una conversación.",
            ]},
        "Vale la pena decir con precision": {
            "titulo": "Qué produce cada fase",
            "ideas": [
                "Requisitos (QUÉ): RF y RNF, glosario y reglas de negocio.",
                "Diseño (CÓMO): casos de uso, clases, modelo de datos, wireframes y mockups.",
                "Construcción: el ejecutable. Pruebas: casos de prueba y evidencias. "
                "Mantenimiento: el sistema en uso, que se ajusta y evoluciona.",
                "Esta asignatura vive en requisitos y diseño: los planos, no la obra.",
            ]},
        "La gran decision no es": {
            "titulo": "Una vuelta o varias vueltas",
            "ideas": [
                "La decisión no es qué fases hacer, sino cuántas veces recorrerlas y con cuánto sistema.",
                "Una vuelta: requisitos de TODO, diseño de TODO, construcción de TODO.",
                "En ciclos: un pedazo útil pasa por las cinco fases; vuelta 1 la ficha del paciente, "
                "vuelta 2 el historial, vuelta 3 los reportes.",
                "En una vuelta, un malentendido de la semana 2 aparece en la 15; en ciclos se corrige barato.",
            ]},
        "Hay que separar dos palabras": {
            "titulo": "Proyecto, producto y la segunda vida del sistema",
            "ideas": [
                "Proyecto: esfuerzo temporal, con inicio, fin, alcance y presupuesto; se cierra.",
                "Producto: el sistema vivo, con versiones (1.0, 1.1, 2.0), que sigue cuando el proyecto cerró.",
                "El mantenimiento se lleva entre el 60 y el 80 % del costo total de un sistema.",
                "Error común: dar todo por cerrado con la versión 1.0 y no dejar nada escrito para la segunda vida.",
            ]},
        "Como se elige el recorrido": {
            "titulo": "Cómo se elige el recorrido",
            "ideas": [
                "Requisitos estables, contrato cerrado y sistema crítico: recorrido lineal con aprobaciones formales.",
                "Dominio nuevo y un cliente que descubre lo que quiere al verlo: recorrido en ciclos.",
                "En la clínica conviven los dos: los datos del paciente son estables; el tablero de "
                "métricas es incierto.",
                "Se elige por la estabilidad de los requisitos, no por costumbre del equipo.",
            ]},
    },
    3: {
        "El modelo en cascada": {
            "titulo": "La cascada y la línea base",
            "ideas": [
                "Las fases van una detrás de otra y cada una termina con un documento que alguien firma.",
                "Sin documento aprobado no se avanza: corregir un plano cuesta una borrada; un muro, demoler.",
                "El documento de requisitos aprobado es la línea base: la versión oficial contra la que se mide todo.",
                "La cascada sí admite cambios: entran por una solicitud que estima costo y tiempo, y suben la versión.",
            ]},
        "El modelo en V": {
            "titulo": "El modelo en V",
            "ideas": [
                "Dobla la cascada en una V: cada fase de diseño tiene enfrente su nivel de prueba.",
                "Requisitos ↔ aceptación · arquitectura ↔ integración · diseño detallado ↔ unitarias.",
                "La prueba se diseña al mismo tiempo que el requisito: con RF-03 nace CP-ACEP-07.",
                "Verificar: ¿se construyó bien según el documento? Validar: ¿se construyó lo correcto?",
            ]},
        "Cuando SI tienen sentido": {
            "titulo": "Cuándo sí conviene el enfoque tradicional",
            "ideas": [
                "Requisitos estables y conocidos desde el principio.",
                "Contrato a precio fijo o licitación pública: el alcance debe estar cerrado para cotizar.",
                "Sistemas críticos o regulados: equipos médicos, aviación, banca, datos personales.",
                "Varios proveedores que necesitan un documento común. Ahí el detalle previo no es "
                "burocracia: es la única forma de estimar.",
            ]},
        "Cuando NO tienen sentido": {
            "titulo": "Cuándo no conviene",
            "ideas": [
                "Cuando el cliente no sabe lo que quiere hasta que lo ve, o el dominio es nuevo para el equipo.",
                "Cuando la primera entrega visible tarda tanto que el negocio cambia antes.",
                "Integrar todo al final concentra el riesgo en el peor momento.",
                "Cambiar una frase en requisitos cuesta casi nada; con diseño, código y datos, semanas.",
            ]},
        "En el mundo tradicional": {
            "titulo": "La documentación como producto",
            "ideas": [
                "En el enfoque tradicional la documentación es buena parte del producto contratado.",
                "Artefactos típicos: ERS (IEEE 830 / ISO 29148), documento de diseño, matriz de "
                "trazabilidad y acta de aprobación.",
                "Cada documento lleva versión, fecha, autor y aprobador; todo cambio entra por solicitud formal.",
                "Un documento de diseño con prototipo navegable es justo el tipo de producto que se factura.",
            ]},
    },
    4: {
        "El manifiesto agil": {
            "titulo": "El manifiesto ágil",
            "ideas": [
                "Firmado en 2001 por diecisiete personas cansadas de documentos perfectos y sistemas inservibles.",
                "Cuatro valores unidos por «sobre»: individuos sobre procesos, software funcionando "
                "sobre documentación exhaustiva, colaboración sobre contrato, respuesta al cambio sobre plan.",
                "«Sobre» no es «en vez de»: lo de la derecha sigue valiendo.",
                "Mejor un mockup imperfecto en la semana 3 que ochenta páginas en la 15.",
            ]},
        "Scrum es un marco de trabajo": {
            "titulo": "Scrum: roles, eventos y artefactos",
            "ideas": [
                "Un marco, no una metodología completa: define lo mínimo.",
                "Roles: Product Owner (QUÉ y en qué orden), Scrum Master (facilita, no es el jefe) "
                "y equipo de desarrollo (CÓMO).",
                "Eventos: Sprint de 1 a 4 semanas, Planificación, Diaria de 15 min, Revisión y Retrospectiva.",
                "Artefactos: Product Backlog, Sprint Backlog e Incremento, con su Definición de Terminado.",
            ]},
        "Kanban viene de otra tradicion": {
            "titulo": "Kanban y el límite de trabajo en curso",
            "ideas": [
                "No impone iteraciones ni roles: hace visible el flujo del trabajo.",
                "Prácticas: visualizar en un tablero, limitar el trabajo en curso, gestionar el flujo, "
                "políticas explícitas y mejora continua.",
                "Con límite 2 en «Modelando», nadie empieza una tercera tarea sin terminar otra.",
                "Abrir cinco diagramas y no terminar ninguno es el problema que el límite resuelve.",
            ]},
        "Hay dos palabras que se usan": {
            "titulo": "Iteración e incremento",
            "ideas": [
                "Incremento: agregar un pedazo nuevo y utilizable al sistema.",
                "Iteración: volver sobre lo que ya existe y mejorarlo con la retroalimentación.",
                "Mockup de la ficha (incremento); la veterinaria pide alergias y foto, sale la versión 2 (iteración).",
                "Cada entrega es una rebanada vertical que el cliente puede ver, no una capa invisible.",
            ]},
        "Agil no significa trabajar sin": {
            "titulo": "Ágil no es trabajar sin documentación",
            "ideas": [
                "Lo que el manifiesto rechaza es el documento inflado que nadie lee, no el documento útil.",
                "Un equipo ágil documenta historias con criterios, Definición de Terminado, decisiones, "
                "diccionario de datos y diagramas.",
                "Los escribe justo a tiempo y los mantiene vivos.",
                "Un producto que ES documentación de diseño también se puede hacer ágil: por incrementos, "
                "revisado con el cliente.",
            ]},
    },
    6: {
        "Un requerimiento no es lo que": {
            "titulo": "Elicitación: de lo que dijo a lo que necesita",
            "ideas": [
                "Un requerimiento es lo que el sistema debe hacer para que el problema desaparezca, "
                "no lo que el cliente dijo.",
                "Entrevista: preguntas abiertas primero, las de sí o no al final.",
                "Observación: media hora en recepción, cronometrando. Prototipo desechable: la gente "
                "sabe decir lo que NO quiere cuando lo ve.",
                "Las frases crudas son necesidades, todavía no requisitos.",
            ]},
        "Con las necesidades en la mano": {
            "titulo": "Dos familias: RF y RNF",
            "ideas": [
                "RF: una capacidad observable. «El sistema debe permitir a <actor> <acción> <objeto> [bajo <condición>]».",
                "Si al leerlo se imagina un botón o una pantalla, es funcional.",
                "RNF: QUÉ TAN BIEN lo hace: desempeño, seguridad, usabilidad, disponibilidad, respaldo, mantenibilidad.",
                "El RF se prueba haciendo clic; el RNF, midiendo o intentando lo prohibido.",
            ]},
        "La regla de oro del oficio": {
            "titulo": "Si no se puede verificar, es un deseo",
            "ideas": [
                "Lista negra: rápido, amigable, fácil, intuitivo, robusto, moderno, óptimo, eficiente, seguro.",
                "Ante cada una: ¿cuánto?, ¿en qué condiciones?, ¿cómo lo mediríamos delante del cliente?",
                "«Que sea rápido» → RNF-01: búsqueda en máximo 3 s, con 5.000 fichas y 10 usuarios a la vez.",
                "Con número, el requisito pasa o no pasa.",
            ]},
        "Priorizar no es ordenar": {
            "titulo": "Priorizar con MoSCoW",
            "ideas": [
                "Must: sin ello no se sale a producción. Should: importante, con plan B manual.",
                "Could: si sobra tiempo. Won't: fuera de ESTA versión, y escrito.",
                "Won't es la categoría más valiosa: es la única que frena el alcance infinito.",
                "Los Must no deberían pasar del 60 % del esfuerzo: si todo es Must, nada es Must.",
            ]},
        "El ultimo pedazo es la trazabilidad": {
            "titulo": "Trazabilidad hacia atrás y hacia adelante",
            "ideas": [
                "Hacia atrás: de dónde salió el RF, quién lo pidió, en qué frase y en qué fecha.",
                "Hacia adelante: en qué caso de uso, pantalla, clase y prueba termina.",
                "Se lleva en una matriz simple y se actualiza cada clase.",
                "Cuando el cliente cambia de opinión, dice en dos minutos qué se rompe y cuánto cuesta.",
            ]},
    },
    7: {
        "Una historia de usuario no es": {
            "titulo": "La historia de usuario",
            "ideas": [
                "El recordatorio corto de una conversación pendiente entre quien necesita y quien construye.",
                "Como <rol> quiero <acción> para <beneficio>: un rol concreto, no «el usuario».",
                "El «para» es lo que más se borra y lo más valioso: dice por qué vale la pena.",
                "Las tres C: Card (la tarjeta), Conversation (la charla) y Confirmation (los criterios).",
            ]},
        "Los criterios de aceptacion son": {
            "titulo": "Criterios de aceptación: Dado, Cuando, Entonces",
            "ideas": [
                "Convierten una historia bonita en una verificable.",
                "Dado <contexto> Cuando <acción> Entonces <resultado observable>.",
                "Cada criterio se responde con sí o no mirando la pantalla, nunca con «depende».",
                "El que siempre falta es el camino alterno: el caso feo, el error.",
            ]},
        "INVEST es la lista de chequeo": {
            "titulo": "INVEST: una historia bien cortada",
            "ideas": [
                "Independiente · Negociable · Valiosa · Estimable · Small (pequeña) · Testeable.",
                "Negociable: describe la necesidad, no la solución técnica.",
                "Small: cabe en una iteración; si toma tres semanas es una épica disfrazada.",
                "Si falla dos letras, no se planea: se vuelve a partir.",
            ]},
        "Una epica es una historia grande": {
            "titulo": "Épicas y corte vertical",
            "ideas": [
                "Una épica es una historia que todavía no cabe en una iteración.",
                "Corte vertical, como una rebanada de pastel: cada historia atraviesa pantalla, lógica "
                "y datos, y deja algo usable.",
                "Corte horizontal por capas: ninguna sirve sola y el cliente no ve nada.",
                "Otros ejes: por tipo de dato, por regla de negocio, por camino (primero el feliz).",
            ]},
        "Estimar en agil no es adivinar": {
            "titulo": "Puntos de historia y planning poker",
            "ideas": [
                "Estimar es comparar tamaños, no adivinar horas: los puntos mezclan esfuerzo, complejidad e incertidumbre.",
                "Una historia de referencia (registrar un dueño = 3) y la escala 1, 2, 3, 5, 8, 13.",
                "Con 13 o más, la señal es partirla.",
                "Planning poker: todos muestran a la vez; lo que vale es la discusión cuando uno dice 2 y otro 8.",
            ]},
    },
    8: {
        "UML significa Lenguaje Unificado": {
            "titulo": "Qué es UML",
            "ideas": [
                "Lenguaje Unificado de Modelado: gráfico y estandarizado, ni de programación ni una herramienta.",
                "Lo normalizado es el significado de cajas, líneas y números, no el programa donde se pintan.",
                "Tiene catorce diagramas; un analista usa cuatro o cinco.",
                "«Un dueño puede tener varias mascotas» deja preguntas que el diagrama contesta con dos números y una línea.",
            ]},
        "Los diagramas se agrupan": {
            "titulo": "Vista estructural y vista de comportamiento",
            "ideas": [
                "Estructural: de qué está hecho el sistema (clases, objetos, componentes, despliegue).",
                "Comportamiento: qué pasa y en qué orden (casos de uso, actividades, secuencia, estados).",
                "Un sistema necesita las dos, como una casa el plano de plantas y el de instalaciones.",
                "Los diagramas no reemplazan los requisitos: los dibujan.",
            ]},
        "El diagrama de clases se dibuja": {
            "titulo": "La clase: tres compartimentos",
            "ideas": [
                "Arriba el nombre en singular (Mascota), en medio los atributos, abajo los métodos.",
                "Atributo: visibilidad, nombre y tipo: -nombre: String (- privado, + público).",
                "Método: firma y retorno: +calcularEdad(): int.",
                "Modelo de dominio: solo conceptos del negocio; nada de MascotaDAO ni ConexionBD.",
            ]},
        "Las lineas entre clases son": {
            "titulo": "Asociaciones y multiplicidades",
            "ideas": [
                "Asociación: línea con un nombre que se lee como frase y una multiplicidad en cada extremo.",
                "1 exactamente uno · 0..1 opcional · 1..* uno o más · 0..* cero o más.",
                "Dueño 1 — 0..* Mascota: el 1 es una decisión de negocio que se confirma con el cliente.",
                "Composición (rombo relleno), agregación (rombo vacío) y herencia (triángulo), solo si hay un es-un.",
            ]},
        "El diagrama que dibujamos hoy": {
            "titulo": "Del diagrama de clases a la base de datos",
            "ideas": [
                "De cada clase salen los campos del diccionario de datos y después las tablas.",
                "La clase Mascota → la tabla mascota; la asociación 1 a 0..* → una llave foránea.",
                "Muchos a muchos → una tabla intermedia.",
                "Por eso va limpio: nombres en singular, sin atributos repetidos, sin cajas sin requisito.",
            ]},
    },
    9: {
        "Un caso de uso es la descripcion": {
            "titulo": "Qué es un caso de uso",
            "ideas": [
                "Una interacción completa entre un actor y el sistema que entrega un resultado con valor para ese actor.",
                "No es una pantalla, ni un botón, ni una tabla, ni un paso intermedio.",
                "Prueba del almuerzo: ¿el actor se puede ir satisfecho? Registrar mascota sí; validar la fecha no.",
                "Se nombra con verbo en infinitivo y objeto del dominio, con palabras de la clínica.",
            ]},
        "El actor es un rol": {
            "titulo": "El actor es un rol, y el límite del sistema",
            "ideas": [
                "Doña Marta no es un actor: el actor es Recepcionista.",
                "Una persona puede ser dos actores; un sistema externo puede ser actor secundario.",
                "El rectángulo del límite es una decisión: adentro, lo que se construye; afuera, lo que se consume.",
                "Dibujar «Enviar WhatsApp» adentro es prometer que se construye la mensajería.",
            ]},
        "Las relaciones entre casos de uso": {
            "titulo": "Include, extend y generalización",
            "ideas": [
                "Include: el caso base SIEMPRE ejecuta el incluido (agendar y registrar consulta verifican la mascota).",
                "Extend: opcional, solo si se cumple una condición (exportar el expediente a PDF).",
                "Generalización: un actor especializa a otro.",
                "Usar include para partir en pasos convierte el diagrama en un flujo disfrazado.",
            ]},
        "La especificacion textual es donde": {
            "titulo": "La especificación textual",
            "ideas": [
                "Ahí vive el noventa por ciento del valor: ficha, pre y postcondiciones, flujo principal y alternos.",
                "El flujo principal va en pares: lo que hace el actor y lo que responde el sistema, sin adjetivos.",
                "«Rápido y amigable» no es un paso: es un RNF que vive en otro documento.",
                "Los alternos se numeran por el paso donde se desvían: 2a sin coincidencias, 2b demasiadas.",
            ]},
        "Precondiciones y postcondiciones": {
            "titulo": "Precondiciones y postcondiciones",
            "ideas": [
                "Precondición: lo que es verdad antes de empezar; el flujo no la vuelve a verificar.",
                "Si «autenticado» es precondición, ningún paso pide usuario y contraseña.",
                "Postcondición: el estado en que queda el sistema, verificable mirando los datos.",
                "Cada postcondición se convierte casi sola en un caso de prueba.",
            ]},
    },
    11: {
        "Un paquete de diseño no es": {
            "titulo": "El paquete de diseño es un sistema de documentos",
            "ideas": [
                "Todos deben decir lo mismo con las mismas palabras, aunque se escribieron en semanas distintas.",
                "RF-07 promete recordatorios; ningún caso de uso los tiene; ninguna clase los soporta.",
                "Ninguno está mal por sí solo: lo que está mal es el conjunto.",
                "Corregirlo hoy cuesta una hoja; cuando ya hay pantallas y código, carísimo.",
            ]},
        "La herramienta central para eso": {
            "titulo": "Requisitos huérfanos y elementos viudos",
            "ideas": [
                "Hacia adelante: ¿todo RF llega a un caso de uso y a una clase que lo soporte?",
                "Un RF que no llega a nada es huérfano: se prometió algo que el diseño no cumple.",
                "Hacia atrás: ¿todo elemento del diseño nace de un requisito? Si no, es viudo.",
                "La matriz de trazabilidad es la única prueba objetiva de que el paquete es coherente.",
            ]},
        "El segundo eje de la auditoria": {
            "titulo": "El glosario canónico",
            "ideas": [
                "Dueño, Propietario, Cliente y Responsable no son cuatro sinónimos: son cuatro tablas en potencia.",
                "Cada concepto: un nombre único, una definición de una línea y sus sinónimos prohibidos.",
                "El glosario manda sobre todos los artefactos, sin excepciones.",
                "Separa parejas peligrosas: Cita es la reserva futura; Consulta, la atención ya realizada.",
            ]},
        "La revision entre pares se hace": {
            "titulo": "Revisión entre pares con reglas",
            "ideas": [
                "Se revisa el artefacto, nunca a la persona.",
                "Roles: autor (en silencio), revisor (hechos observables) y moderador (tiempo y registro).",
                "Cada hallazgo: ubicación exacta, inconsistencia y severidad: bloqueante, mayor o menor.",
                "«No me gusta» no es un hallazgo: es una opinión.",
            ]},
        "Todo lo que se encuentra se convierte": {
            "titulo": "Del hallazgo al backlog de deuda de diseño",
            "ideas": [
                "Cada hallazgo es un ítem con responsable, severidad, criterio de cierre y estado.",
                "Estados: aceptado, rechazado con justificación escrita, o aplazado por acuerdo.",
                "Rechazar un hallazgo es legítimo si se argumenta.",
                "Definición de terminado: RF y RNF sin huérfanos, casos de uso, clases con multiplicidades, "
                "mockups y diccionario de datos.",
            ]},
    },
    12: {
        "Hasta ahora todos los modelos": {
            "titulo": "El diagrama de secuencia",
            "ideas": [
                "Clases y casos de uso son estáticos; la secuencia es un modelo del tiempo.",
                "Participantes arriba, una línea de vida por cada uno, y el tiempo corre hacia abajo.",
                "Flecha llena: mensaje síncrono. Punteada: el retorno. Barra: el objeto está trabajando.",
                "Agendar: recepcionista → pantalla → control → repositorio, y vuelve la confirmación.",
            ]},
        "El diagrama de actividad responde": {
            "titulo": "El diagrama de actividad y sus calles",
            "ideas": [
                "Responde en qué orden ocurre el trabajo y quién hace cada paso, también fuera del computador.",
                "Inicio, acciones, decisiones con condición entre corchetes, bifurcación y unión, final.",
                "Las calles: una franja por rol, para ver de un vistazo quién hace qué.",
                "Revela lo que ni casos de uso ni clases muestran: los cuellos de botella.",
            ]},
        "La pregunta practica es cuando": {
            "titulo": "¿Secuencia o actividad?",
            "ideas": [
                "Duda de responsabilidades (¿quién se encarga y con quién habla?): secuencia.",
                "Duda de proceso (¿en qué orden, dónde se decide, qué va en paralelo?): actividad.",
                "La secuencia se dibuja para un caso de uso; la actividad, para un proceso que cruza varios.",
                "Agendar cita: secuencia. La atención completa, de la puerta a la factura: actividad.",
            ]},
        "Estos diagramas no se inventan": {
            "titulo": "Del paso del caso de uso al mensaje y la operación",
            "ideas": [
                "Cada paso del flujo principal se vuelve uno o más mensajes, en el mismo orden y con los nombres del glosario.",
                "«Verifica la disponibilidad» → mensaje consultarDisponibilidad a un participante.",
                "Ese participante es una clase del diagrama de clases, con esa operación.",
                "Si la clase o la operación no existen, el modelo estático estaba incompleto: el hallazgo más valioso.",
            ]},
        "Los flujos alternos tambien se modelan": {
            "titulo": "Fragmentos combinados: alt, opt y loop",
            "ideas": [
                "alt: caminos excluyentes con su condición entre corchetes (hay horario / no hay).",
                "opt: un camino que puede ocurrir o no (recordatorio si el propietario lo autorizó).",
                "loop: un bloque que se repite (agregar varias vacunas).",
                "El camino feliz completo y una o dos decisiones críticas; el resto, en la especificación.",
            ]},
    },
    13: {
        "Un wireframe, un mockup y un prototipo": {
            "titulo": "Wireframe, mockup y prototipo",
            "ideas": [
                "Wireframe: esqueleto en gris. ¿Qué información va y en qué orden se lee?",
                "Mockup: la foto fija de cómo se verá: tipografía, color, iconos. ¿Cómo se ve?",
                "Prototipo: el mockup con clic. ¿Cómo se siente usarlo?",
                "Mover una caja en un wireframe cuesta treinta segundos; ya programada, dos sesiones.",
            ]},
        "Los principios de usabilidad no son": {
            "titulo": "Cuatro principios de usabilidad",
            "ideas": [
                "Visibilidad del estado: «Ficha guardada, código M-0421» y el botón deshabilitado mientras guarda.",
                "Prevención de errores: calendario en vez de teclear, especie de una lista cerrada.",
                "Consistencia: la misma acción con el mismo nombre y en el mismo lugar.",
                "Reconocer antes que recordar: elegir de una lista, no memorizar códigos.",
            ]},
        "Una pantalla suelta no sirve": {
            "titulo": "El flujo de tarea y sus caminos alternos",
            "ideas": [
                "Se diseña el recorrido completo, de la intención a la tarea cumplida.",
                "Camino feliz: buscar al dueño, encontrarlo, registrar la mascota y recibir el código.",
                "Alternos: dueño no registrado, mascota ya existente, dueño sin documento.",
                "Doce mascotas llamadas Firulais: mostrar especie, edad y dueño para desambiguar.",
            ]},
        "La interfaz no se inventa": {
            "titulo": "La interfaz se deriva de los artefactos",
            "ideas": [
                "Cada pantalla señala el RF que la origina.",
                "Cada campo existe en el diccionario de datos con su tipo y longitud.",
                "Cada botón corresponde a una operación del caso de uso o de la secuencia.",
                "Un campo sin respaldo en el diccionario: o falta un requisito o sobra el campo.",
            ]},
        "Una interfaz se puede evaluar": {
            "titulo": "Evaluar una interfaz sin programarla",
            "ideas": [
                "Recorrido cognitivo: alguien ajeno al diseño intenta una tarea concreta sin ayuda; se cuentan clics, dudas y errores.",
                "Prueba de pasillo: tres personas de otro grupo, y se anota sin defenderse.",
                "Se evalúa con la usuaria real: escribe lento, la interrumpen, el monitor está lejos.",
                "Mensajes de la clínica: «Esta mascota ya tiene ficha», no «violación de unicidad».",
            ]},
    },
    14: {
        "Sustentar un paquete de diseño": {
            "titulo": "Sustentar es defender decisiones",
            "ideas": [
                "No es leer diapositivas ni narrar lo hecho cada semana.",
                "El jurado mira tres cosas: si el diseño resuelve el problema, si las piezas son coherentes "
                "y si el autor entiende lo que entregó.",
                "Narrar: «hicimos casos de uso, luego clases». Sustentar: «la clínica pierde fichas, y esto lo resuelve así».",
                "Se ordena por problema resuelto, no por documento.",
            ]},
        "El orden de la sustentacion": {
            "titulo": "El orden en embudo",
            "ideas": [
                "1 Problema · 2 Requisitos · 3 Modelo · 4 Interfaz · 5 Decisiones.",
                "El problema primero: sin saber qué duele, nada de lo que sigue tiene sentido.",
                "Empezar por las pantallas bonitas es el error más común.",
                "En doce minutos: problema y alcance 3, requisitos 2, modelo 2, interfaz 2, decisiones 2, "
                "riesgos y cierre 1.",
            ]},
        "Defender una decision de diseño": {
            "titulo": "Cómo se defiende una decisión",
            "ideas": [
                "Decisión · alternativas consideradas · criterio de elección · consecuencia asumida.",
                "Decisión: separar Historia_Clinica de Mascota. Alternativa: campos dentro de Mascota.",
                "Criterio: una mascota tiene muchas consultas en su vida. Consecuencia: una entidad más, "
                "aceptada porque el RNF de 3 s se sostiene.",
                "Así el jurado ya sabe que se pensó en la alternativa.",
            ]},
        "Las preguntas del jurado son": {
            "titulo": "Las preguntas previsibles del jurado",
            "ideas": [
                "¿Por qué es necesario este requisito? ¿Qué pasa si dos registran la misma mascota a la vez?",
                "¿Por qué esto es una clase y no un atributo? ¿Cómo se mide el RNF? ¿Qué quedó fuera?",
                "Cada respuesta en dos frases, sin discursos.",
                "Si no se sabe, no se inventa: se reconoce el vacío y se propone cómo se resolvería.",
            ]},
        "El reparto del guion en bloques": {
            "titulo": "El guion en bloques con tiempos",
            "ideas": [
                "Cada bloque con su rango de minutos y su evidencia en pantalla.",
                "Problema y alcance → requisitos y trazabilidad → modelos UML → prototipo en vivo → decisiones y riesgos.",
                "Se ensaya cronometrado dos veces, en voz alta: leído en silencio dura la mitad.",
                "Plan B: capturas del prototipo, PDF descargado y diagramas en imagen.",
            ]},
    },
}


VISUALES = {
    1: {
        "Programar es escribir codigo": {"anim": "seminario/clase1/costo-del-error"},
        "Proyecto y producto": {"anim": "seminario/clase1/proyecto-producto"},
        "Un requisito funcional dice": {"anim": "seminario/clase1/deseo-o-requisito"},
        "Los interesados no son solo": {"anim": "seminario/clase1/interesados"},
        "Todo desarrollo pasa por las mismas fases": {"anim": "seminario/clase1/fases-planos"},
        "El mapa del semestre": {"anim": "seminario/clase1/mapa-semestre"},
        "Hay un concepto que explica": {"anim": "seminario/clase1/deuda-intereses"},
        "En un curso de diseno la deuda": {"anim": "seminario/clase1/artefacto-version"},
        "De ahi se sigue": {"anim": "seminario/clase1/modelo-dos-fallas"},
        "Lo anterior conduce al criterio": {"anim": "seminario/clase1/cinco-rasgos"},
        "El rasgo tres merece": {"anim": "seminario/clase1/cadena-trazabilidad"},
    },
    2: {
        "Un ciclo de vida del software": {"anim": "seminario/clase2/fase-entrada-salida"},
        "Vale la pena decir con precision": {"anim": "seminario/clase2/artefactos-por-fase"},
        "La gran decision no es": {"anim": "seminario/clase2/una-o-tres-vueltas"},
        "Hay que separar dos palabras": {"anim": "seminario/clase2/costo-mantenimiento"},
        "Como se elige el recorrido": {"anim": "seminario/clase2/elegir-recorrido"},
    },
    3: {
        "El modelo en cascada": {"anim": "seminario/clase3/cascada-linea-base"},
        "El modelo en V": {"anim": "seminario/clase3/modelo-v"},
        "Cuando NO tienen sentido": {"anim": "seminario/clase3/costo-del-cambio"},
        "En el mundo tradicional": {"anim": "seminario/clase3/paquete-tradicional"},
    },
    4: {
        "El manifiesto agil": {"anim": "seminario/clase4/manifiesto-sobre"},
        "Scrum es un marco de trabajo": {"anim": "seminario/clase4/ciclo-scrum"},
        "Kanban viene de otra tradicion": {"anim": "seminario/clase4/kanban-wip"},
        "Hay dos palabras que se usan": {"anim": "seminario/clase4/iteracion-incremento"},
    },
    6: {
        "Un requerimiento no es lo que": {"anim": "seminario/clase6/elicitacion"},
        "Con las necesidades en la mano": {"anim": "seminario/clase6/rf-rnf"},
        "La regla de oro del oficio": {"anim": "seminario/clase6/lista-negra"},
        "Priorizar no es ordenar": {"anim": "seminario/clase6/moscow"},
        "El ultimo pedazo es la trazabilidad": {"anim": "seminario/clase6/traza-atras-adelante"},
    },
    7: {
        "Una historia de usuario no es": {"anim": "seminario/clase7/tres-c"},
        "Los criterios de aceptacion son": {"anim": "seminario/clase7/dado-cuando-entonces"},
        "INVEST es la lista de chequeo": {"anim": "seminario/clase7/invest"},
        "Una epica es una historia grande": {"anim": "seminario/clase7/corte-vertical"},
        "Estimar en agil no es adivinar": {"anim": "seminario/clase7/planning-poker"},
    },
    8: {
        "UML significa Lenguaje Unificado": {"anim": "seminario/clase8/uml-pregunta"},
        "Los diagramas se agrupan": {"anim": "seminario/clase8/dos-vistas"},
        "El diagrama de clases se dibuja": {"anim": "seminario/clase8/clase-compartimentos"},
        "Las lineas entre clases son": {"anim": "seminario/clase8/relaciones-uml"},
        "El diagrama que dibujamos hoy": {"anim": "seminario/clase8/clase-a-tabla"},
    },
    9: {
        "Un caso de uso es la descripcion": {"anim": "seminario/clase9/prueba-almuerzo"},
        "El actor es un rol": {"anim": "seminario/clase9/actor-limite"},
        "Las relaciones entre casos de uso": {"anim": "seminario/clase9/include-extend"},
        "La especificacion textual es donde": {"anim": "seminario/clase9/pares-responsabilidad"},
        "Precondiciones y postcondiciones": {"anim": "seminario/clase9/pre-post"},
    },
    11: {
        "Un paquete de diseño no es": {"anim": "seminario/clase11/paquete-inconsistente"},
        "La herramienta central para eso": {"anim": "seminario/clase11/huerfano-viudo"},
        "El segundo eje de la auditoria": {"anim": "seminario/clase11/glosario"},
        "La revision entre pares se hace": {"anim": "seminario/clase11/revision-roles"},
        "Todo lo que se encuentra se convierte": {"anim": "seminario/clase11/backlog-deuda"},
    },
    12: {
        "Hasta ahora todos los modelos": {"anim": "seminario/clase12/secuencia"},
        "El diagrama de actividad responde": {"anim": "seminario/clase12/actividad-calles"},
        "La pregunta practica es cuando": {"anim": "seminario/clase12/secuencia-o-actividad"},
        "Estos diagramas no se inventan": {"anim": "seminario/clase12/paso-mensaje-operacion"},
        "Los flujos alternos tambien se modelan": {"anim": "seminario/clase12/fragmentos"},
    },
    13: {
        "Un wireframe, un mockup y un prototipo": {"anim": "seminario/clase13/wire-mock-proto"},
        "Los principios de usabilidad no son": {"anim": "seminario/clase13/usabilidad"},
        "Una pantalla suelta no sirve": {"anim": "seminario/clase13/flujo-tarea"},
        "La interfaz no se inventa": {"anim": "seminario/clase13/wireframe-anotado"},
    },
    14: {
        "Sustentar un paquete de diseño": {"anim": "seminario/clase14/narrar-sustentar"},
        "El orden de la sustentacion": {"anim": "seminario/clase14/embudo"},
        "Defender una decision de diseño": {"anim": "seminario/clase14/defender-decision"},
    },
}


#: Detras de que concepto va cada lamina de codigo cuando el vocabulario compartido engana a
#: `teoria_a_slides.intercalar` (el «mapa de dominio» no va detras del «mapa del semestre»).
#: `{n: {comienzo del titulo del codigo: clave del concepto en LAMINAS}}`. El resto, automatico.
CODIGO_TRAS = {
    1: {"El mapa de dominio": "Los interesados no son solo",
        "La ficha de requisito": "Un requisito funcional dice",
        "De frase cruda": "Un requisito funcional dice"},
    2: {"El recorrido lineal": "Un ciclo de vida del software",
        "El mismo ciclo en tres vueltas": "La gran decision no es",
        "El ciclo de vida de": "La gran decision no es"},
    4: {"El plan de sprints": "Scrum es un marco de trabajo",
        "Historia de usuario de": "Agil no significa trabajar sin"},
    8: {"Lo que NO es una clase": "El diagrama de clases se dibuja",
        "El diagrama de clases en Mermaid": "El diagrama de clases se dibuja",
        "Modelo de dominio de": "Las lineas entre clases son"},
    11: {"Auditoria cruzada": "La herramienta central para eso"},
    13: {"El mapa de navegacion": "Una pantalla suelta no sirve",
         "La tabla de anotaciones": "La interfaz no se inventa"},
}
