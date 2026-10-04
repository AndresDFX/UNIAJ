# -*- coding: utf-8 -*-
"""BD II · Clase 13 · Análisis de casos reales (autónoma): ideas proyectadas y GUION por lámina.

Formato: `notas_guion.py` (se fusiona en `bd2_contenido_data.CONTENIDO`). Las animaciones están en
`config/animaciones/bd2/clase13/`: «Al entrar» es su primer paso y cada «Clic» el siguiente. En las
láminas de código y de ilustración no hay clics: los pasos van rotulados por líneas o por zona.

La clase cae en festivo (lunes 2 de noviembre) y es AUTÓNOMA: el grupo la trabaja solo con estas
láminas. Las notas sirven para grabar una explicación corta, para responder por el canal del
curso o para retomarla; los minutos son los de una explicación completa.

Salidas verificadas en PGlite (PostgreSQL 18) con los datos de ejemplo del curso: 6 dueños
(Ana Gomez … Andres Vallejo) y la tabla propia `tarifa` (CANINO, FELINO, OTRA) de las láminas
del trigger de archivo y de la restauración, que corren en orden sobre la base de la clase.
"""

CONTENIDO = {
    13: {
        "Encuadre de hoy": {
            "ideas": [
                "Hoy la clase es **autónoma**: no hay encuentro en vivo y estas láminas son la guía "
                "completa.",
                "El tema es el **análisis de casos reales**: cómo falla una base en producción y qué "
                "se cambia para que no se repita.",
                "Seis casos públicos, una forma de analizarlos (**causa raíz** y **lección "
                "accionable**) y dos mejoras en SQL.",
                "Cada lámina se sostiene sola: sirve para repasar aunque no hayas visto las "
                "anteriores.",
            ],
            "notas": {
                "min": 3,
                "explica": "Hoy no hay técnica nueva: se usa lo del semestre para entender fallos "
                           "reales. La pregunta de la clase es una sola: cuando una base falla en "
                           "producción, ¿qué falló de verdad y qué se cambia para que no vuelva a "
                           "pasar?",
                "pasos": [
                    "La clase cae en festivo (2 de noviembre) y no hay encuentro en vivo. Si grabas "
                    "una explicación corta, abre con la pregunta de la clase y avisa que las "
                    "láminas se leen en orden y que cada una se entiende sola.",
                    ("Antes de empezar",
                     "Recuerda al grupo que el Parcial 3 (Clase 14, 9 de noviembre) incluye esta "
                     "clase autónoma: es la que más se olvida al estudiar."),
                ],
                "cuidado": "No la presentes como «clase de relleno»: el análisis de incidentes es "
                           "una práctica profesional con nombre propio, el post-mortem.",
                "puente": "Empezamos por ese documento: el post-mortem.",
            },
        },
        "Mapa del bloque": {
            "notas": {
                "min": 1,
                "explica": "El reparto orientativo de las dos horas de trabajo autónomo: teoría con "
                           "una lámina por concepto, un análisis guiado completo y la práctica "
                           "opcional de la carpeta.",
                "pasos": [
                    "Señala los tramos sin detenerte. La teoría, leída con calma, toma unos 50 "
                    "minutos (más que el tramo 10-35); el «demo» de hoy es el análisis guiado de "
                    "la lámina «Demo del día», y la práctica empieza hacia el minuto 65.",
                ],
                "puente": "Primer concepto: qué es un post-mortem.",
            },
        },
        "El post-mortem analiza el fallo": {
            "ideas": [
                "Un **post-mortem** es el documento breve que se escribe después de un fallo en "
                "producción.",
                "Responde cuatro preguntas: qué pasó, con qué **impacto**, por qué fue posible y "
                "qué se cambia.",
                "Es **sin culpables** (blameless): se analiza el sistema, no a la persona que se "
                "equivocó.",
                "Si el informe castiga, nadie vuelve a reportar los errores pequeños que avisan "
                "de los grandes.",
            ],
            "notas": {
                "min": 4,
                "explica": "Cuando un sistema falla en producción, los equipos serios no se quedan "
                           "en «se cayó»: escriben un post-mortem, un documento corto que "
                           "reconstruye el fallo y decide qué cambiar. La regla del oficio es que no "
                           "se buscan culpables: se busca la condición del sistema que dejó que un "
                           "error común se volviera un problema grande.",
                "pasos": [
                    "La falla en producción y, a la derecha, el documento que se escribe después. "
                    "«Post-mortem» es literalmente «después de la muerte» del servicio; es breve, "
                    "no un libro.",
                    "Las cuatro preguntas, en orden. Subraya la 3, en otro color: «por qué fue "
                    "posible» es la causa raíz, el tema de la lámina siguiente. El impacto se mide: "
                    "datos, horas, dinero o personas afectadas.",
                    "La banda verde: sin culpables. Explica el porqué práctico: si el documento "
                    "sirve para castigar, la gente esconde los errores pequeños y la organización "
                    "se queda sin aviso de los grandes.",
                ],
                "ejemplo": "Un post-mortem de cuatro líneas en la clínica: «A las 9:10 se borraron "
                           "las citas del día; a las 9:40 se restauraron desde el respaldo de la "
                           "noche y se perdieron las creadas en esa media hora; fue posible porque "
                           "el usuario de la aplicación podía hacer DELETE sin WHERE; se cambia: la "
                           "aplicación pierde el permiso DELETE sobre cita».",
                "preguntas": [
                    ("¿Y si alguien lo hizo mal a propósito?",
                     "Eso ya no es un incidente sino un asunto de seguridad o disciplinario, y va "
                     "por otro camino. El post-mortem trata los errores honestos, que son casi "
                     "todos."),
                    ("¿Hace falta post-mortem si el fallo no llegó al usuario?",
                     "Sí: el que se detuvo a tiempo es el más barato de estudiar. Incidente es "
                     "todo evento que degrada el servicio o pone en riesgo los datos."),
                ],
                "cuidado": "«Sin culpables» no es «sin responsables»: cada acción de mejora tiene "
                           "un responsable y una fecha. Lo que no hay es castigo por el error "
                           "honesto.",
                "puente": "Para responder la tercera pregunta hay que separar dos causas: la "
                          "próxima y la raíz.",
            },
        },
        "Causa proxima y causa raiz": {
            "ideas": [
                "La **causa próxima** es el último evento de la cadena, el que se ve: el disco que "
                "falla.",
                "La **causa raíz** es la condición que le dio consecuencias: un respaldo que nadie "
                "había probado.",
                "Se llega preguntando **¿por qué?** varias veces, hasta nombrar algo que se pueda "
                "cambiar.",
                "Si la respuesta nombra a una persona, todavía no es la raíz.",
            ],
            "notas": {
                "min": 4,
                "explica": "Todo fallo tiene una causa que se ve y otra que lo permitió. La que se "
                           "ve, la próxima, casi nunca se puede eliminar: los discos fallan y la "
                           "gente se equivoca. La raíz sí se cambia, y se encuentra preguntando "
                           "por qué hasta llegar a un procedimiento, un permiso, una restricción o "
                           "una alarma.",
                "pasos": [
                    "Arriba, lo que se ve: el disco falla un viernes y se pierden tres semanas de "
                    "historias clínicas. La etiqueta roja dice «causa próxima». Pregunta: «¿la "
                    "solución es comprar discos que no fallen?».",
                    "Tres «¿por qué?» bajan a la caja azul: había un respaldo que nadie había "
                    "restaurado nunca, y nadie vigilaba si el del día se ejecutaba. Esa es la "
                    "causa raíz, y esa sí se puede cambiar.",
                    "La regla para saber cuándo parar: si la respuesta nombra a una persona "
                    "(«Pedro borró»), sigue preguntando; si nombra algo que se cambia (un permiso, "
                    "una restricción, una alarma), llegaste.",
                ],
                "ejemplo": "«Se borró la agenda» → ¿por qué? «Alguien corrió DELETE sin WHERE» "
                           "(nombra una persona: seguir) → ¿por qué pudo? «El usuario de la "
                           "aplicación tiene DELETE sobre cita» (un permiso: raíz). La mejora es "
                           "quitar ese permiso.",
                "preguntas": [
                    ("¿Siempre son cinco «por qué»?",
                     "No: cinco es una guía. Se para cuando la respuesta es algo que se puede "
                     "cambiar; a veces son tres y a veces seis."),
                    ("¿Y que fuera de noche o que quien sabía restaurar estuviera de vacaciones?",
                     "Son factores contribuyentes: empeoraron el resultado sin causarlo. Se anotan "
                     "aparte; no son la raíz."),
                ],
                "cuidado": "No aceptes «error humano» como causa raíz: es la causa próxima de casi "
                           "todo. La pregunta correcta es por qué el sistema dejó que ese error "
                           "tuviera consecuencias.",
                "puente": "Con esta herramienta vamos al primer caso real, el mejor documentado.",
            },
        },
        "Caso uno: el respaldo": {
            "ideas": [
                "En enero de 2017, un **borrado** en el servidor equivocado eliminó unos 300 GB de "
                "datos.",
                "Al recuperar, ninguno de sus **cinco mecanismos de respaldo** funcionó como se "
                "esperaba.",
                "Se restauró una copia de unas **seis horas** antes: lo creado en esa ventana se "
                "perdió.",
                "Un respaldo que nunca se restauró de prueba **no es un respaldo**.",
            ],
            "notas": {
                "min": 4,
                "explica": "GitLab, un servicio en la nube para guardar código, perdió datos en 2017. "
                           "El error humano fue corriente; lo que lo volvió histórico fue descubrir, "
                           "en plena emergencia, que ninguno de sus respaldos servía como se creía.",
                "pasos": [
                    "La causa próxima: atendiendo un problema de replicación, un ingeniero ejecutó "
                    "un borrado recursivo del directorio de datos en el servidor equivocado. Unos "
                    "300 GB.",
                    "La causa raíz: al intentar recuperar, los cinco mecanismos de respaldo y "
                    "replicación fallaban. Dos ejemplos: el volcado lógico fallaba en silencio por "
                    "una diferencia de versión entre cliente y servidor, y las copias remotas "
                    "estaban vacías.",
                    "El desenlace: se restauró una copia de unas seis horas antes; lo creado en "
                    "esa ventana se perdió para siempre (miles de proyectos y comentarios).",
                    "Las dos lecciones: un respaldo nunca restaurado no es un respaldo, y el RPO "
                    "(Clase 4: cuántos datos se acepta perder, medido en tiempo) no se declara: se "
                    "demuestra restaurando.",
                ],
                "ejemplo": "En la clínica: si el respaldo de la noche nunca se ha restaurado en una "
                           "base de prueba, nadie sabe si el RPO real es de 24 horas o de tres "
                           "semanas.",
                "preguntas": [
                    ("¿Por qué el volcado fallaba en silencio?",
                     "Por una diferencia de versión entre el programa que hacía la copia y el "
                     "servidor: daba error y nadie revisaba ese error. Un proceso que puede fallar "
                     "sin avisar da una confianza que no existe."),
                    ("¿Qué es el RPO?",
                     "Recovery Point Objective: cuántos datos acepta perder la organización, "
                     "medido en tiempo. Si el último respaldo bueno era de seis horas antes, el RPO "
                     "real fue de seis horas."),
                ],
                "cuidado": "No lo cuentes como «un ingeniero borró la base»: esa es la causa "
                           "próxima, justo el error de análisis de la lámina anterior. El caso "
                           "enseña que cinco respaldos sin probar equivalen a ninguno.",
                "puente": "Segundo caso: no se perdió nada; se leyó lo que no se debía, por un "
                          "permiso de más.",
            },
        },
        "Caso dos: permisos excesivos": {
            "ideas": [
                "En 2019, un **cortafuegos mal configurado** dejó obtener las credenciales de un "
                "rol de servicio.",
                "Ese rol podía leer **todos** los buckets de almacenamiento, muchos más de los que "
                "necesitaba.",
                "Se expusieron datos de unos **100 millones** de personas; la multa fue de 80 "
                "millones de dólares.",
                "La lección es el **privilegio mínimo**: cada rol, solo lo que su tarea necesita.",
            ],
            "notas": {
                "min": 3,
                "explica": "Capital One, un banco de Estados Unidos, tuvo en 2019 una fuga de datos "
                           "sin ninguna hazaña técnica: una configuración incorrecta abrió la "
                           "puerta, y un permiso de más hizo que detrás de esa puerta estuviera "
                           "todo.",
                "pasos": [
                    "La cadena, de arriba abajo: cortafuegos mal configurado (causa próxima) → el "
                    "servidor hace peticiones internas a pedido del atacante → entrega credenciales "
                    "temporales de un rol de servicio.",
                    "Lo que ese rol podía leer. Los 12 recuadros son un esquema, no a escala: "
                    "verde, lo que su función necesitaba; rojo, todo lo demás que también podía "
                    "listar y leer.",
                    "La causa raíz: un privilegio mucho mayor que su función. La lección, con el "
                    "vocabulario de la Clase 2: privilegio mínimo.",
                ],
                "ejemplo": "En la clínica, una aplicación que entra con el usuario dueño de todas "
                           "las tablas repite el error: si alguien abusa de ella, tiene todo. Con "
                           "un rol que solo puede ejecutar los procedimientos, el daño queda "
                           "acotado.",
                "preguntas": [
                    ("¿El problema no fue el cortafuegos?",
                     "Esa es la causa próxima. Con un rol de privilegio mínimo, la misma falla "
                     "habría expuesto una fracción de los datos."),
                    ("¿Por qué los proyectos de curso repiten este error?",
                     "Porque conectarse con un usuario que tiene todo hace que nunca aparezca un "
                     "error de permisos: es más rápido hoy y es la puerta abierta mañana."),
                ],
                "cuidado": "Usa las cifras publicadas: unos 100 millones de personas en EE. UU. y "
                           "varios millones en Canadá, y una multa de 80 millones de dólares en "
                           "2020. No las redondees hacia arriba para dramatizar.",
                "puente": "Tercer caso: ni ataque ni comando equivocado; una migración sin camino "
                          "de vuelta.",
            },
        },
        "Caso tres: perdida de datos": {
            "ideas": [
                "En 2019, MySpace reconoció haber perdido la **música** subida entre 2003 y 2015 en "
                "una migración de servidores.",
                "No hubo ataque: la migración no tenía **copia verificada** ni camino de vuelta.",
                "Faltaban tres prácticas: **expandir, migrar y contraer**, comparar conteos y "
                "probar el retorno antes.",
                "Una migración sin retorno probado es una **apuesta**.",
            ],
            "notas": {
                "min": 3,
                "explica": "Migrar es mover datos de un sistema a otro. MySpace lo hizo sin una "
                           "copia verificada y sin poder volver atrás, y perdió doce años de música "
                           "de sus usuarios. El mismo patrón aparece en la banca.",
                "pasos": [
                    "Los archivos viajan de los servidores viejos a los nuevos; los rojos se "
                    "pierden en el camino. No había copia verificada: la franja roja son doce años "
                    "de música, del orden de 50 millones de archivos.",
                    "Lo que faltaba, en tres cajas: expandir, migrar y contraer (las dos versiones "
                    "conviven mientras se migra), conteos que coincidan entre origen y destino "
                    "antes de borrar nada, y un plan de retorno probado antes del día del cambio.",
                    "La lección y el caso paralelo: TSB, un banco del Reino Unido, dejó en 2018 a "
                    "millones de clientes sin acceso confiable durante semanas por una migración "
                    "probada de forma insuficiente.",
                ],
                "ejemplo": "En la clínica, al mover las citas antiguas a una tabla histórica: se "
                           "crea la tabla nueva, se copian las filas, se compara SELECT COUNT(*) en "
                           "las dos y solo entonces se borran del origen.",
                "preguntas": [
                    ("¿Qué es expandir, migrar y contraer?",
                     "Primero se agrega lo nuevo sin quitar lo viejo (expandir), luego se mueven "
                     "los datos y la aplicación (migrar) y solo al final se retira lo viejo "
                     "(contraer). Mientras tanto siempre hay a dónde volver."),
                ],
                "cuidado": "La causa raíz no es «el servidor nuevo falló»: es que se dio por "
                           "terminada la migración sin haber comprobado el destino.",
                "puente": "Cuarto caso: el fallo que no da ningún mensaje de error.",
            },
        },
        "Caso cuatro: concurrencia": {
            "ideas": [
                "Dos procesos leen el mismo stock (5), cada uno resta 3 y los dos escriben 2: es la "
                "**actualización perdida**.",
                "Salieron 6 unidades y el sistema dice que quedan 2, **sin ningún mensaje de "
                "error**.",
                "Siguen el mismo patrón la **doble reserva** de una franja y el **bloqueo mutuo** "
                "(deadlock).",
                "La defensa vive en la base: **UPDATE condicional**, FOR UPDATE o UNIQUE.",
            ],
            "notas": {
                "min": 4,
                "explica": "La concurrencia es lo que pasa cuando dos usuarios trabajan sobre el "
                           "mismo dato al mismo tiempo. Sus fallos no producen errores: el sistema "
                           "queda mal en silencio y se descubre semanas después, cuando el "
                           "inventario físico no cuadra o dos personas reclaman el mismo cupo.",
                "pasos": [
                    "El stock del insumo vale 5. Los dos procesos lo leen y los dos ven 5.",
                    "Cada uno resta 3 y escribe 2. El número del centro pasa a 2 en rojo: la "
                    "segunda escritura pisó a la primera.",
                    "El resultado: salieron 6 unidades y el sistema dice 2, sin mensaje de error. "
                    "Nombra los otros dos patrones de la Clase 10: la doble reserva de la misma "
                    "franja y el bloqueo mutuo, en el que el motor aborta una de las dos "
                    "transacciones.",
                    "La defensa vive en la base: UPDATE condicional (stock = stock - 3 WHERE stock "
                    ">= 3) o SELECT … FOR UPDATE al leer, y UNIQUE para la doble reserva. Validar "
                    "antes en la aplicación no basta: entre leer y escribir hay una ventana.",
                ],
                "ejemplo": "UPDATE insumo SET stock = stock - 3 WHERE id_insumo = 2 AND stock >= 3; "
                           "— si otro proceso ya descontó, esta sentencia actualiza 0 filas en vez "
                           "de dejar un dato falso.",
                "preguntas": [
                    ("¿Por qué no lo vi al probar?",
                     "Porque estos defectos solo aparecen con dos sesiones a la vez. Si se probó "
                     "desde una sola máquina, no se probó."),
                    ("¿Qué hace exactamente FOR UPDATE?",
                     "Bloquea la fila leída hasta el COMMIT: la segunda sesión espera en vez de "
                     "decidir con un dato que ya cambió."),
                ],
                "cuidado": "El título dice que este caso no llega a los titulares: no le inventes "
                           "un nombre propio. Es un patrón, no una noticia.",
                "puente": "Quinto caso: el fallo de seguridad más documentado de la web.",
            },
        },
        "Caso cinco: inyeccion de SQL": {
            "ideas": [
                "La **inyección de SQL** ocurre cuando la aplicación pega en la sentencia el texto "
                "que escribió el usuario.",
                "Con x' OR '1'='1 el WHERE se vuelve siempre verdadero y la consulta devuelve **toda "
                "la tabla**.",
                "Escapar comillas a mano no basta: la defensa es el **parámetro ligado** (EXECUTE … "
                "USING).",
                "Con el parámetro, el mismo texto se compara como un valor y devuelve **0 filas**.",
            ],
            "notas": {
                "min": 4,
                "explica": "Inyectar SQL es colar código dentro de un dato. Pasa cuando la "
                           "aplicación arma la consulta pegando lo que el usuario escribió: el "
                           "texto deja de ser un dato y pasa a ser parte de la sentencia. La "
                           "defensa es que el dato viaje aparte, como parámetro.",
                "pasos": [
                    "Recorre la ilustración de arriba abajo. Primero, lo que escribe el usuario: "
                    "x' OR '1'='1.",
                    ("Camino 1",
                     "Pegado dentro de la sentencia: la comilla del texto cierra la cadena y el OR "
                     "queda como código. La condición es siempre verdadera y salen todos los "
                     "dueños."),
                    ("Camino 2",
                     "Ligado como parámetro: la sentencia lleva $1 y USING entrega el valor aparte. "
                     "El texto completo se compara como un nombre y salen 0 filas: nadie se llama "
                     "así."),
                    ("Banda final",
                     "Escapar comillas a mano no equivale: basta olvidarlo en un sitio. La regla: "
                     "el dato nunca viaja como código."),
                ],
                "ejemplo": "TalkTalk, Reino Unido, octubre de 2015: una inyección de SQL en páginas "
                           "web heredadas que nadie había actualizado expuso datos personales de "
                           "unos 157.000 clientes; el regulador de protección de datos la multó con "
                           "400.000 libras en 2016.",
                "preguntas": [
                    ("¿Y si le quito las comillas a lo que escribe el usuario?",
                     "Rompe nombres legítimos como O'Brien y basta olvidarlo en un solo sitio. El "
                     "parámetro ligado lo resuelve siempre, porque el dato nunca se interpreta."),
                    ("¿El PREPARE de la Clase 12 es lo mismo?",
                     "Es el mismo principio: la sentencia con huecos y los valores aparte. EXECUTE "
                     "… USING es su forma dentro de PL/pgSQL."),
                ],
                "cuidado": "No digas que la inyección «borra la base» siempre: el ataque típico lee "
                           "datos, como aquí. Lo que puede hacer depende del rol con que entra la "
                           "aplicación: otra vez, privilegio mínimo.",
                "puente": "Veámoslo en código: la misma búsqueda, insegura y segura.",
            },
        },
        "SQL dinamico: concatenar el texto": {
            "notas": {
                "min": 4,
                "explica": "Dos funciones que buscan un dueño por nombre con SQL dinámico: la "
                           "sentencia se arma como texto y se ejecuta con EXECUTE. La única "
                           "diferencia es cómo entra el nombre: pegado al texto o ligado como "
                           "parámetro.",
                "pasos": [
                    "Presenta la lámina como «la misma función dos veces»; señala las dos "
                    "cabeceras, MAL y BIEN.",
                    ("Líneas 1-7",
                     "La versión insegura: RETURN QUERY EXECUTE ejecuta un texto armado con || "
                     "(concatenar). Cada '' dentro de la cadena es UNA comilla escrita: el nombre "
                     "queda entre comillas dentro de la sentencia."),
                    ("Líneas 9-15",
                     "La versión segura: el texto lleva $1 donde va el dato y USING p_nombre "
                     "entrega el valor por separado. El motor nunca lo lee como SQL."),
                    ("Líneas 17-18",
                     "La prueba: el mismo texto de ataque contra las dos. La insegura devuelve "
                     "todos los dueños; la segura, 0."),
                ],
                "ejemplo": "Con los 6 dueños de ejemplo: el COUNT(*) del ataque contra "
                           "buscar_dueno_inseguro da 6 y contra buscar_dueno_seguro da 0; "
                           "buscar_dueno_inseguro('Ana Gomez') devuelve una fila (id 1), así que el "
                           "uso normal funciona igual en las dos.",
                "preguntas": [
                    ("¿Por qué no WHERE nombre = p_nombre, sin EXECUTE?",
                     "Es todavía mejor cuando la consulta es fija: una consulta estática usa el "
                     "parámetro siempre como valor. EXECUTE solo hace falta si la sentencia cambia, "
                     "por ejemplo la tabla o la columna."),
                    ("¿Qué pasa si alguien busca O'Brien en la insegura?",
                     "Falla con «syntax error at or near \"Brien\"»: la comilla del nombre cierra la "
                     "cadena. Es la misma grieta por la que entra el ataque."),
                ],
                "cuidado": "Las dos comillas seguidas ('') dentro de una cadena SQL son una sola "
                           "comilla escrita, no una cadena vacía; si las confundes al dictar, nadie "
                           "entiende por qué funciona el ataque.",
                "puente": "Sexto caso: no es de seguridad ni de pérdida, sino de rendimiento.",
            },
        },
        "Caso seis: el reporte que tumba": {
            "ideas": [
                "Un panel refresca **cada minuto** un reporte con SELECT * sobre una tabla enorme, "
                "sin índice para su filtro.",
                "Si cada ejecución tarda más de un minuto, **se apilan** y ocupan las conexiones "
                "del servidor.",
                "En hora pico la aplicación se queda **sin conexiones** y deja de responder.",
                "El **plan de ejecución** lo delata: un Seq Scan que lee toda la tabla para quedarse "
                "con pocas filas.",
            ],
            "notas": {
                "min": 4,
                "explica": "No todos los incidentes son pérdidas o ataques: muchos son una consulta "
                           "lenta que se ejecuta demasiado seguido. Ninguna ejecución falla; el "
                           "servicio cae porque se queda sin recursos. Es el caso que más se repite "
                           "y menos se cuenta.",
                "pasos": [
                    "Recorre la ilustración en tres franjas, de arriba abajo.",
                    ("Arriba",
                     "Un reporte programado cada minuto (min 0 a 5) en el que cada ejecución tarda "
                     "más que un minuto y más que la anterior, porque compiten entre sí: la "
                     "siguiente empieza antes de que termine la anterior y se apilan."),
                    ("Centro",
                     "En el minuto 5 hay tres reportes a la vez y, en hora pico, la aplicación usa "
                     "el resto: las 10 conexiones del esquema quedan ocupadas y la siguiente "
                     "petición de recepción no consigue ninguna."),
                    ("Abajo",
                     "Lo que dice el plan: Seq Scan sobre la tabla grande, que recorre todo para "
                     "quedarse con pocas filas, es la firma de un índice que falta. La lección "
                     "accionable: solo las columnas que se muestran e índice en el filtro, medido "
                     "con EXPLAIN ANALYZE antes y después."),
                ],
                "ejemplo": "En la clínica: un tablero que cada minuto cuenta las citas del día "
                           "leyendo toda la tabla de citas, con años de historia, en lugar de usar "
                           "un índice por fecha.",
                "preguntas": [
                    ("¿Por qué el SELECT * es parte del problema?",
                     "Trae columnas que nadie mira: más datos leídos, más memoria y más red por "
                     "ejecución. El reporte pide solo lo que muestra."),
                    ("¿Cómo sé que el índice sirvió?",
                     "Con EXPLAIN ANALYZE antes y después: el Seq Scan cambia por un Index Scan y "
                     "el tiempo real baja. Si no se midió, no se sabe."),
                ],
                "cuidado": "No afirmes que un índice lo arregla siempre: si el filtro devuelve casi "
                           "toda la tabla, el planeador hace bien en recorrerla. El índice ayuda "
                           "cuando el filtro deja pocas filas.",
                "puente": "Cómo se lee el plan de una consulta que no escribiste tú.",
            },
        },
        "Leer un plan de ejecucion ajeno": {
            "notas": {
                "min": 3,
                "explica": "EXPLAIN (ANALYZE, BUFFERS) ejecuta la consulta y muestra el plan que "
                           "eligió el motor, con filas y tiempos reales. Los cuatro comentarios son "
                           "el orden en que se lee un plan ajeno, el de un sistema que falla.",
                "pasos": [
                    "Primero la consulta y después los comentarios: son una lista de revisión.",
                    ("Líneas 1-8",
                     "La consulta: dueños con más de 5 citas desde el 1 de enero de 2026. EXPLAIN "
                     "(ANALYZE, BUFFERS) delante la ejecuta de verdad y añade tiempos y páginas "
                     "leídas."),
                    ("Comentario 1",
                     "Se busca el nodo con el costo más alto, no el primero de arriba: el plan es un "
                     "árbol y se lee de adentro hacia afuera."),
                    ("Comentarios 2 y 3",
                     "Seq Scan sobre tabla grande con un filtro que deja pocas filas: falta un "
                     "índice. Filas estimadas contra reales diez veces distintas: estadísticas "
                     "viejas, ANALYZE."),
                    ("Comentario 4",
                     "Un Nested Loop con muchas filas suele indicar estimaciones malas; con "
                     "estadísticas al día el planeador tiende a elegir Hash Join."),
                ],
                "ejemplo": "Con los datos de ejemplo (10 citas) el plan muestra Seq Scan on cita c "
                           "con Filter: (fecha_hora >= '2026-01-01'::date), dos Hash Join y un "
                           "HashAggregate que descarta a los 4 dueños con citas porque ninguno pasa "
                           "de 5: devuelve 0 filas.",
                "preguntas": [
                    ("¿EXPLAIN ANALYZE es seguro en producción?",
                     "Ejecuta la sentencia de verdad: con un SELECT solo cuesta su tiempo, pero con "
                     "un UPDATE o un DELETE los cambios se aplican. A esos se les envuelve en "
                     "BEGIN … ROLLBACK."),
                    ("¿Qué agrega BUFFERS?",
                     "Cuántas páginas se leyeron de memoria (shared hit) y cuántas de disco (read). "
                     "Muchas lecturas de disco son la señal de una consulta cara."),
                ],
                "cuidado": "Con tablas pequeñas el Seq Scan es la decisión correcta: no lo presentes "
                           "como error en la base de ejemplo de 10 citas. La alarma es con millones "
                           "de filas.",
                "puente": "Ya hay seis casos. ¿Cómo se convierte un caso en una lección que sirva?",
            },
        },
        "Lecciones accionables": {
            "ideas": [
                "Una lección es un **lugar común** si se pudo escribir antes del caso: «hay que "
                "probar los respaldos».",
                "Es **accionable** si tiene verbo concreto, artefacto, frecuencia o umbral, y forma "
                "de comprobarla.",
                "Ejemplo: el primer lunes de cada mes se restaura el respaldo en una base de prueba "
                "y se comparan conteos.",
                "La segunda se puede **auditar**: sin registro del mes, no hay respaldo.",
            ],
            "notas": {
                "min": 4,
                "explica": "La parte difícil del análisis no es contar el caso sino sacar una "
                           "lección que alguien pueda cumplir y otro pueda verificar. La prueba es "
                           "simple: si la lección se pudo escribir antes de conocer el caso, es un "
                           "lugar común.",
                "pasos": [
                    "La versión inútil, tachada: «hay que probar los respaldos». Pregunta: "
                    "¿quién la cumple, cuándo, y cómo sabemos que la cumplió? Nadie puede "
                    "responder.",
                    "La misma lección con sus cuatro partes: verbo (se restaura), artefacto (el "
                    "respaldo más reciente, en una base de prueba), frecuencia (el primer lunes de "
                    "cada mes) y comprobación (conteos de filas contra producción y bitácora con "
                    "fecha y resultado).",
                    "Por qué vale: se puede auditar. Si no hay registro del mes, se declara que no "
                    "hay respaldo.",
                ],
                "ejemplo": "Del caso de permisos: crear rol_clinica_app con GRANT EXECUTE sobre los "
                           "procedimientos y sin SELECT, INSERT, UPDATE ni DELETE directos, "
                           "verificado consultando las vistas de privilegios. Del de concurrencia: "
                           "ALTER TABLE cita ADD CONSTRAINT uq_cita_vet_franja UNIQUE "
                           "(id_veterinario, fecha_hora).",
                "preguntas": [
                    ("¿Puedo inventar un caso?",
                     "No. Cada caso tiene que poder verificarse con una fuente pública o "
                     "declararse expresamente como hipotético."),
                    ("¿Y si el caso no tiene detalle técnico publicado?",
                     "Se escribe solo lo documentado y se marca aparte lo que es inferencia "
                     "propia: separar hecho de suposición es parte del análisis."),
                ],
                "cuidado": "No aceptes lecciones en infinitivo vago («mejorar la seguridad», "
                           "«optimizar»): sin artefacto y sin comprobación no son lecciones.",
                "puente": "Ahora, la lección del caso del respaldo convertida en dos objetos de la "
                          "base.",
            },
        },
        "Del caso a la mejora": {
            "ideas": [
                "Un **trigger BEFORE DELETE** copia cada fila (OLD) a una tabla de archivo antes de "
                "que se borre.",
                "No evita el error humano, pero lo vuelve **recuperable**: desde el archivo se "
                "puede volver.",
                "Una **consulta de verificación** compara las filas esperadas con las restauradas y "
                "da un veredicto.",
                "Son **controles distintos**: uno permite volver y el otro demuestra que se volvió "
                "completo.",
            ],
            "notas": {
                "min": 3,
                "explica": "Del caso GitLab salen dos mejoras que se confunden pero hacen cosas "
                           "distintas. El archivo de borrados permite recuperar lo que se borró por "
                           "error; la verificación demuestra que lo recuperado está completo. Sin "
                           "la segunda, nadie sabe si la primera funcionó.",
                "pasos": [
                    "Presenta las dos columnas como dos controles distintos.",
                    ("Columna izquierda",
                     "El DELETE sigue siendo posible (el error humano no desaparece); el trigger "
                     "BEFORE DELETE copia OLD a tarifa_borrada y devuelve OLD para que el borrado "
                     "siga. Resultado: se puede volver."),
                    ("Columna derecha",
                     "El registro del respaldo guarda cuántas filas había (3); después de restaurar "
                     "se cuenta otra vez y el CASE compara: 3 = 3, RESTAURACION OK. Resultado: se "
                     "demuestra que se volvió completo."),
                    ("Abajo",
                     "Lo que le faltó a GitLab: tenía respaldos, pero ninguno se había comprobado "
                     "restaurando."),
                ],
                "ejemplo": "Con la tabla tarifa de tres especies (CANINO 45000, FELINO 40000, OTRA "
                           "35000), un DELETE FROM tarifa sin WHERE deja 3 filas en tarifa_borrada; "
                           "tras restaurar, registro 3, conteo 3, RESTAURACION OK. Si solo volvieran "
                           "2, el veredicto sería REVISAR.",
                "preguntas": [
                    ("¿El trigger no impide el borrado?",
                     "No: devuelve OLD y el borrado sigue. Impedirlo sería otra decisión (quitar el "
                     "permiso o un BEFORE con RAISE EXCEPTION). Este control acepta el error y "
                     "prepara la vuelta."),
                    ("¿Por qué no basta con el respaldo de la noche?",
                     "Porque no tiene lo creado durante el día; el archivo guarda la fila exacta en "
                     "el momento en que se borró."),
                ],
                "cuidado": "El conteo esperado se calcula con COUNT(*) al respaldar, no se escribe a "
                           "mano: un número escrito a mano verifica contra lo que alguien creyó, no "
                           "contra lo que había.",
                "puente": "Primero, el trigger en código.",
            },
        },
        "El borrado con rastro": {
            "notas": {
                "min": 3,
                "explica": "Un trigger de archivo completo sobre una tabla pequeña y sin "
                           "dependencias, la de tarifas por especie: la tabla donde se guarda lo "
                           "borrado, la función que copia la fila y la asociación que la dispara "
                           "antes de cada DELETE.",
                "pasos": [
                    "Recorre las piezas de arriba abajo.",
                    ("Líneas 1-2",
                     "La tabla de ejemplo, tarifa, con tres especies. Nadie apunta a ella con una "
                     "clave foránea, así que se puede borrar sin tropezar con otras tablas."),
                    ("Líneas 4-9",
                     "La tabla tarifa_borrada: las columnas de tarifa más dos que se llenan solas, "
                     "borrado_en (DEFAULT now()) y usuario_bd (DEFAULT current_user)."),
                    ("Líneas 11-17",
                     "La función RETURNS TRIGGER: inserta los valores de OLD, que en un DELETE es la "
                     "fila que se va, y termina en RETURN OLD."),
                    ("Líneas 19-21",
                     "La asociación: BEFORE DELETE ON tarifa, FOR EACH ROW. Corre una vez por cada "
                     "fila borrada."),
                ],
                "ejemplo": "DELETE FROM tarifa WHERE especie = 'OTRA'; deja en tarifa_borrada la "
                           "fila OTRA · 35000.00, con la fecha y el usuario de la base.",
                "preguntas": [
                    ("¿Por qué RETURN OLD y no RETURN NEW?",
                     "En un DELETE no hay fila nueva: NEW es NULL. En un BEFORE, devolver NULL "
                     "cancela la operación en silencio; devolver OLD la deja seguir."),
                    ("¿Y si el borrado falla por una clave foránea?",
                     "Se deshace toda la sentencia, incluida la copia que hizo el trigger: el "
                     "archivo no queda con filas que en realidad no se borraron."),
                ],
                "cuidado": "Haz el ejemplo sobre tarifa y no sobre una tabla con dependencias: "
                           "borrar un veterinario que tiene citas falla por la clave foránea "
                           "(«update or delete on table \"veterinario\" violates foreign key "
                           "constraint»), y la tabla cita es la de la práctica.",
                "puente": "La segunda mejora: comprobar que la restauración quedó completa.",
            },
        },
        "La restauracion comprobada": {
            "notas": {
                "min": 3,
                "explica": "El ciclo completo en tres bloques: respaldar y anotar cuántas filas "
                           "había, sufrir el accidente y volver desde el archivo, y una consulta que "
                           "compara y dicta un veredicto.",
                "pasos": [
                    "Señala los tres comentarios numerados: son los tres momentos.",
                    ("Líneas 1-6",
                     "CREATE TABLE … AS SELECT copia la tabla tarifa; registro_respaldo guarda el "
                     "conteo calculado con COUNT(*), no escrito a mano."),
                    ("Líneas 8-11",
                     "El accidente: DELETE sin WHERE. El trigger de la lámina anterior ya archivó "
                     "cada fila; el INSERT … SELECT con columnas explícitas las devuelve."),
                    ("Líneas 13-20",
                     "La comprobación: una fila con las filas esperadas, las actuales y el veredicto "
                     "del CASE. ORDER BY hecho_en DESC LIMIT 1 toma el respaldo más reciente si hubo "
                     "varios."),
                ],
                "ejemplo": "Ejecutada después de la lámina anterior, la consulta final devuelve "
                           "esperadas 3 · actuales 3 · RESTAURACION OK, y la tabla cita de la base "
                           "sigue intacta. Si faltara una fila, devolvería 3 · 2 · REVISAR.",
                "preguntas": [
                    ("¿Por qué columnas explícitas en el INSERT?",
                     "Porque tarifa_borrada tiene dos columnas más (borrado_en y usuario_bd): con "
                     "SELECT * no coincidirían. Nombrarlas además protege si cambia el orden de "
                     "las columnas."),
                    ("¿Basta con comparar el conteo?",
                     "Es el mínimo. Una verificación más fuerte compara también rangos o sumas, "
                     "por ejemplo el MIN y el MAX de una fecha o la suma de los valores."),
                ],
                "cuidado": "Si una tabla con SERIAL se restaura con su id explícito en una tabla "
                           "recién creada, la secuencia no avanza y el siguiente INSERT sin id choca "
                           "con la llave primaria; se ajusta con setval. Aquí no pasa: la llave de "
                           "tarifa es la especie.",
                "puente": "Con todo esto, el análisis guiado de un caso completo.",
            },
        },
        "Demo del dia": {
            "ideas": [
                "Un caso se recorre en seis pasos: contexto, qué falló, **causa raíz**, impacto, "
                "lección y cambio.",
                "La causa raíz es un **control ausente**, no una persona.",
                "La lección lleva verbo, artefacto, frecuencia y **comprobación**.",
                "El cambio nombra un **objeto real** de la base: una tabla, un trigger, un rol o un "
                "índice.",
            ],
            "notas": {
                "min": 15,
                "explica": "Como hoy no hay encuentro en vivo, la «demo» es un análisis completo "
                           "hecho sobre un caso que no es el de la práctica: Capital One. Muestra la "
                           "forma que debe tener cualquier análisis, de punta a punta.",
                "pasos": [
                    "Recorre las seis filas de la ilustración de arriba abajo, leyendo cada una en "
                    "voz alta como una frase del informe.",
                    ("Filas 2 y 3",
                     "Qué falló y causa raíz por separado: el cortafuegos es la causa próxima; la "
                     "raíz es el rol que podía leerlo todo."),
                    ("Filas 5 y 6",
                     "La lección tiene comprobación (revisión mensual contra la matriz) y el cambio "
                     "nombra un objeto de la base: la aplicación entra con su propio rol, con "
                     "GRANT EXECUTE y sin SELECT directo."),
                    ("Si tienes una base a mano",
                     "Ejecuta en orden las tres láminas de código (SQL dinámico, trigger de archivo "
                     "y restauración comprobada) y muestra cada salida: 6 contra 0, las 3 filas en "
                     "tarifa_borrada y el RESTAURACION OK."),
                ],
                "ejemplo": "Cambio en la base, escrito para la clínica: «la aplicación se conecta "
                           "como rol_clinica_app, que tiene GRANT EXECUTE sobre los procedimientos y "
                           "ningún privilegio directo sobre las tablas; se verifica en las vistas "
                           "de privilegios».",
                "preguntas": [
                    ("¿Cuánto debe medir el análisis?",
                     "Media página: lo que cabe en seis secciones breves."),
                    ("¿Puedo usar uno de los casos de las láminas?",
                     "Sí, o uno propio documentado con su fuente. Lo que no vale es inventarlo."),
                ],
                "cuidado": "Que el análisis no se quede en la noticia: la fila 6, el cambio en la "
                           "base propia, es la que conecta el caso con el proyecto y la que más se "
                           "olvida.",
                "puente": "Cierre de la clase.",
            },
        },
        "Clase 13 ·": {
            "notas": {
                "min": 3,
                "explica": "Cierre: un fallo real casi nunca es mala suerte. Es una causa raíz que "
                           "se puede nombrar y una lección que se convierte en un objeto de la "
                           "base.",
                "pasos": [
                    "Pregunta de salida, por el canal del curso: «elige un caso de hoy y escribe su "
                    "causa raíz en una frase que no nombre a una persona». Responde dos o tres "
                    "corrigiendo las que se quedan en la causa próxima.",
                    ("Antes de despedir",
                     "Recuerda que la próxima sesión es el Parcial 3 (9 de noviembre) y que esta "
                     "clase entra."),
                ],
            },
        },
    },
}
