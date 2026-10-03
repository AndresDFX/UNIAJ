# -*- coding: utf-8 -*-
"""Ejemplos resueltos de Introduccion a la Ingenieria: el concepto, aplicado a un caso.

Por que existe
--------------
El docente reviso el curso y el diagnostico fue: «todavia es demasiado general y no se
entiende; es para primer semestre». Las laminas de concepto estan bien escritas, pero dicen
el concepto en abstracto —«ENTRADAS: lo que llega: datos, dinero, personas»— y un estudiante
que nunca analizo un sistema no sabe que hacer con eso. Lo que le falta es VER el concepto
aplicado, paso a paso, sobre algo que reconoce.

Esos recorridos ya existian: estaban dentro del fundamento, escritos AL DOCENTE («el ejemplo
de las citas medicas conviene desarrollarlo hasta el final»). Aqui se reescriben PARA EL
ESTUDIANTE, en lenguaje llano y con casos de su entorno: la fila de la EPS, el semaforo de
una esquina, el MIO, la tienda del barrio, la matricula de la UNIAJC.

Como se usa
-----------
`EJEMPLOS[n]` es una lista de `(despues_de, spec)`:
  - `despues_de` es un fragmento del titulo de la lamina de concepto que el ejemplo sigue;
  - `spec` tiene la MISMA forma que las laminas de `teoria` (`tipo` content, steps, cards,
    before_after o tabla), asi que se pinta con el mismo motor y con la misma variedad visual;
  - `nota` (opcional) va a las NOTAS DEL PRESENTADOR: como recorrerlo en clase.

La regla que no se rompe
------------------------
CLAUDE.md §0: el ejemplo ensena el MECANISMO, no la respuesta del taller. El taller de cada
clase lo resuelve cada equipo sobre SU problema; aqui se usan casos distintos.
"""

EJEMPLOS = {

    # ── Clase 2 · Historia y evolucion de la Ingenieria ──────────────────────
    2: [
        ("Cómo se cuenta la historia", {
            "tipo": "tabla",
            "titulo": "Ejemplo: el mismo proyecto atrasado, en 1964 y en 2026",
            "headers": ["", "OS/360 de IBM (1964)", "Una app de hoy (2026)"],
            "rows": [
                ["Qué se quería", "Un sistema operativo para toda una familia de computadores", "Una app de pedidos para una cadena de tiendas"],
                ["Cuánta gente", "Más de 1.000 personas", "15 personas en tres equipos"],
                ["Qué pasó", "Se entregó tarde y costó mucho más de lo planeado", "Se entregó tarde y costó más de lo planeado"],
                ["Por qué", "Nadie sabía coordinar a tanta gente construyendo una sola cosa", "Los requisitos cambiaron a mitad de camino"],
                ["¿Era culpa de la máquina?", "No", "No"],
            ],
            "note": "Sesenta años de diferencia y el mismo síntoma: el problema nunca fue la máquina, fue organizar el trabajo.",
            "nota": "Recorra la tabla fila por fila y pregunte en cada una si cambió algo entre 1964 y 2026. La única fila que cambia de verdad es «cuánta gente». El resto es idéntico, y esa es la idea de la clase.",
        }),
        ("Seis hitos", {
            "tipo": "steps",
            "titulo": "Ejemplo: la ley de Brooks, con números",
            "sub": "Agregar gente a un proyecto atrasado lo atrasa más. ¿Por qué? Cuente las conversaciones.",
            "steps": [
                ("2 personas", "1 conversación posible: A con B."),
                ("5 personas", "10 parejas que se tienen que poner de acuerdo."),
                ("10 personas", "45 parejas. Se duplicó la gente y se multiplicaron por 4,5 las conversaciones."),
                ("La fórmula", "n × (n − 1) ÷ 2. Con 20 personas: 190 parejas."),
                ("La conclusión", "Cada persona nueva hay que ponerla al día. Ese tiempo sale del trabajo de los que ya estaban."),
            ],
            "nota": "Haga la cuenta en voz alta con el grupo antes de mostrar los números: pregunte cuántas parejas hay con 5 personas y deje que la calculen. Es aritmética de bachillerato y es lo que hace que la idea se quede.",
        }),
        ("Cómo se lee un hito", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: el hito de 1975, con las cuatro preguntas",
            "sub": "Así se ve un hito leído completo. En el taller hacen lo mismo con los de su periodo.",
            "steps": [
                ("¿Qué dolía?", "Proyectos grandes que iban atrasados. La reacción de los jefes era contratar más programadores."),
                ("¿Qué propuso?", "Fred Brooks mostró que meter más gente a un proyecto atrasado lo atrasa más."),
                ("¿Qué resolvió?", "Explicó por qué pasaba: la comunicación crece más rápido que el equipo. No dio una solución mágica."),
                ("¿Qué sigue vivo?", "Hoy mismo: cuando un equipo del curso se atrasa y pide ayuda a otro, gasta 20 minutos explicando el contexto."),
            ],
            "nota": "Insista en que la cuarta pregunta es la que se califica: «Brooks dijo que agregar gente atrasa» está bien pero no muestra que lo entendieron. La cuarta obliga a conectarlo con algo que les pasó a ellos.",
        }),
    ],

    # ── Clase 3 · Fundamentos basicos de la Ingenieria de Sistemas ───────────
    3: [
        ("Los cinco elementos", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: el sistema de citas de un consultorio",
            "sub": "Los cinco elementos, uno por uno, sobre un caso que todos conocen.",
            "steps": [
                ("Entradas", "Las solicitudes de cita, la agenda disponible del médico y los datos del paciente."),
                ("Proceso", "Asignar la cita, confirmarla y recordarla. Aquí está el software, si hay."),
                ("Salidas", "La cita asignada, el paciente atendido y el registro de lo que pasó."),
                ("Retroalimentación", "Si un paciente no llega, ese cupo se libera y debería cambiar cómo se asignan las próximas citas."),
                ("Frontera", "¿El transporte del paciente es parte del sistema? Si el 30 % pierde la cita por no poder llegar, dejarlo fuera hace que el sistema funcione solo en el papel."),
            ],
            "nota": "Deténgase en la frontera y pregunte: ¿el bus que toma el paciente es parte del sistema de citas? No hay respuesta única, y esa es la lección: la frontera la decide el ingeniero y la tiene que poder defender.",
        }),
        ("Mirar el software o mirar el sistema", {
            "tipo": "content",
            "titulo": "Ejemplo: la app que funcionó y la fila que no se movió",
            "items": [
                "Un equipo construye una **app de citas impecable**: rápida, bonita y sin errores.",
                "A las 5 de la mañana **la fila de la EPS sigue igual**. ¿Por qué?",
                "Las personas de la fila **no tienen datos en el celular**, o no confían en la app.",
                "La secretaria **sigue anotando en el cuaderno**, porque el sistema nuevo le duplica el trabajo.",
                "**El software funcionó y el problema siguió.** En este curso, ese proyecto fracasó.",
                "Un proyecto se juzga por **si el problema del entorno se redujo y se puede medir**, no por si la app funciona.",
            ],
            "nota": "Este es el caso más importante de la clase: deje que el grupo diga por qué creen que la fila no se movió antes de mostrar las razones. Casi siempre aparecen solas.",
        }),
        ("Cuatro conceptos", {
            "tipo": "cards",
            "titulo": "Ejemplo: todos los actores del sistema de citas",
            "columns": 3,
            "cards": [
                ("El paciente", "Pide la cita. Es el actor que todos ven."),
                ("La secretaria", "Asigna y confirma. Si el sistema le complica el trabajo, vuelve al cuaderno."),
                ("El médico", "Su agenda se llena distinto según cómo se asignen las citas."),
                ("Quien paga", "La EPS o el consultorio: quiere menos cupos perdidos."),
                ("El vecino que madrugaba", "Antes conseguía cita llegando temprano. Con el sistema nuevo, ya no. **Nadie le preguntó.**"),
                ("La pregunta clave", "¿Quién más se ve afectado aunque nunca abra la pantalla?"),
            ],
            "nota": "El vecino que madrugaba es el actor que siempre se olvida y el que más importa: el sistema le empeoró la vida sin consultarlo. La Clase 13, sobre impacto social, es una hora entera buscando a ese actor.",
        }),
        ("Cómo se descompone un sistema", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: el semáforo de una esquina, en cinco pasos",
            "sub": "El mismo método del taller, sobre un sistema que ven todos los días.",
            "steps": [
                ("1 · Propósito", "Que carros y peatones crucen la esquina sin chocar y sin esperar de más."),
                ("2 · Frontera", "Dentro: el semáforo, la esquina y quienes la cruzan. Fuera: el resto de la ciudad. Pero si el semáforo de al lado está mal sincronizado, el trancón llega igual."),
                ("3 · Actores", "Conductores, peatones, el agente de tránsito y el vecino que vive en la esquina y aguanta el ruido."),
                ("4 · Seguir una entrada", "Un peatón llega a las 6 p. m. Espera 90 segundos. ¿Es mucho? Depende de cuántos carros pasan."),
                ("5 · Retroalimentación", "¿Cómo se entera el semáforo de que hay trancón? Casi nunca se entera: repite el mismo ciclo todo el día."),
            ],
            "nota": "El paso 5 es el hallazgo: la mayoría de los sistemas del entorno no se enteran de que les salió mal. Encontrar eso en su propio proyecto suele ser la mejor oportunidad de mejora, porque casi siempre es barata.",
        }),
    ],

    # ── Clase 4 · Principios eticos en la Ingenieria ────────────────────────
    4: [
        ("Tres cosas que se confunden", {
            "tipo": "before_after",
            "titulo": "Ejemplo: el mismo pedido, decidido de dos maneras",
            "sub": "El jefe pide: «guarden la cédula y el celular de todos los clientes, por si acaso».",
            "before_title": "Decisión que no se defiende",
            "before": [
                "«Lo pidió el jefe, entonces se hace».",
                "«Es legal: nadie ha dicho que no».",
                "«Cada uno opina distinto sobre los datos».",
                "Se guarda todo y nadie sabe para qué.",
            ],
            "after_title": "Decisión que sí se defiende",
            "after": [
                "Se pregunta **para qué** se va a usar cada dato.",
                "Se guarda **solo lo que se usa**, y el cliente lo sabe.",
                "Se cita la **Ley 1581 de 2012**, no una opinión.",
                "Queda escrito **quién lo decidió y por qué**.",
            ],
            "nota": "Pregunte al grupo qué harían ellos antes de mostrar la columna derecha. La mayoría dirá «lo pidió el jefe»: esa es la idea que la clase viene a cambiar.",
        }),
        ("Los principios que sí están escritos", {
            "tipo": "before_after",
            "titulo": "Ejemplo: opinar o citar un principio",
            "sub": "La misma objeción, dicha de dos formas. Solo una se puede sostener en una reunión.",
            "before_title": "Una opinión",
            "before": [
                "«A mí no me parece bien guardar esos datos».",
                "Se puede responder con otra opinión.",
                "Pesa según quién la diga.",
            ],
            "after_title": "Un principio citado",
            "after": [
                "«La **Ley 1581 de 2012** exige finalidad y consentimiento».",
                "«No podemos guardar datos que no usamos sin decirle al cliente para qué».",
                "Pesa lo mismo la diga quien la diga.",
            ],
            "nota": "La diferencia práctica es enorme para un recién graduado: una opinión de un practicante se ignora; un numeral de una ley no. Insista en que citar no es ser pedante, es protegerse.",
        }),
        ("Cuatro casos donde el software funcionó", {
            "tipo": "steps",
            "titulo": "Ejemplo: qué falló en el Therac-25, paso a paso",
            "sub": "Una máquina de radioterapia que dio sobredosis. Cada paso parecía razonable.",
            "steps": [
                ("1 · Se quitaron los seguros", "Los modelos viejos tenían frenos físicos. En el nuevo se quitaron: «el software lo evita»."),
                ("2 · Se reutilizó el código", "El software venía de los modelos viejos, con errores que antes tapaban esos frenos."),
                ("3 · Apareció la falla", "Si la operadora corregía la pantalla muy rápido, la máquina quedaba mal configurada."),
                ("4 · Los errores no se entendían", "La pantalla decía un código sin explicación. Las operadoras lo ignoraban y seguían."),
                ("El resultado", "Sobredosis masivas y muertes. El software hacía lo que estaba programado."),
            ],
            "nota": "La pregunta para el grupo es: ¿en qué paso se pudo haber parado? Casi siempre responden el 4, y la respuesta más barata era el 1: no quitar los seguros físicos.",
        }),
        ("Yo solo programé", {
            "tipo": "content",
            "titulo": "Ejemplo: el correo que deja rastro",
            "items": [
                "@@Asunto:@@ Riesgo en la función de exportar clientes",
                "@@Lo que me piden:@@ exportar la lista de clientes con cédula y celular a un archivo compartido.",
                "@@El riesgo:@@ si el archivo se filtra, quedan expuestos los datos de unas 2.000 personas.",
                "@@Lo que propongo:@@ exportar solo nombre y ciudad, que es lo que el reporte necesita.",
                "@@Quedo atento@@ a su decisión. — Firmado, con fecha.",
                "**Cinco líneas.** Si el jefe insiste, la decisión ya no es suya, y queda escrito que avisó.",
            ],
            "nota": "Este es el contenido más útil de la clase para su vida laboral: no es heroísmo, es un correo de cinco líneas. Pídales que escriban uno para su propio proyecto antes de terminar.",
        }),
        ("Cinco preguntas para decidir", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: la app que vende la ubicación",
            "sub": "Una app de domicilios quiere vender a anunciantes por dónde se mueven sus usuarios.",
            "steps": [
                ("1 · ¿Quién se daña?", "Los usuarios: un tercero sabe dónde viven, trabajan y estudian."),
                ("2 · ¿Lo saben?", "No. Aceptaron unos términos que nadie lee. No es consentimiento informado."),
                ("3 · ¿Aguanta que se sepa?", "Si mañana sale en el noticiero, la empresa no lo defiende."),
                ("4 · ¿Qué dice la norma?", "La Ley 1581 de 2012: el dato se usa para lo que se pidió, no para venderlo."),
                ("5 · ¿Cuándo se para?", "Ahora, en el diseño. Después de vender los datos ya no se pueden recoger."),
            ],
            "nota": "Hágalo con el grupo pregunta por pregunta, dejando que respondan antes de mostrar cada paso. Es el mismo método que usan en el taller sobre su caso.",
        }),
    ],

    # ── Clase 5 · El rol del ingeniero en el contexto ambiental ─────────────
    5: [
        ("Las cuatro etapas de la huella", {
            "tipo": "steps",
            "titulo": "Ejemplo: la huella de una app de citas en el celular",
            "sub": "Las cuatro etapas, sobre algo que todos tienen en el bolsillo.",
            "steps": [
                ("Fabricación", "El celular ya gastó la mayor parte de su huella antes de encenderse: minería, ensamblaje, transporte."),
                ("Uso", "Cada vez que se abre la app gasta batería, y el servidor que responde gasta electricidad."),
                ("Red", "Cada foto y cada consulta viaja por antenas y cables que también consumen."),
                ("Fin de vida", "Si la app deja de funcionar en celulares viejos, empuja a cambiar de celular: más residuo."),
            ],
            "nota": "La sorpresa es la fabricación: la mayor parte de la huella de un celular está gastada el día que se compra. Por eso la decisión ambiental más fuerte de software es que el celular dure más años.",
        }),
        ("Cuatro conceptos con nombre propio", {
            "tipo": "content",
            "titulo": "Ejemplo: el PUE de un centro de datos, con números",
            "items": [
                "Un centro de datos consume **1.600 kWh** en un día.",
                "De esos, a los servidores —los que computan— llegan **1.000 kWh**.",
                "**PUE = 1.600 ÷ 1.000 = 1,6**",
                "Los otros **600 kWh** se van en enfriar, iluminar y en pérdidas. **No computan nada.**",
                "Un PUE de **1,0** sería perfecto. Uno de **2,0** gasta la mitad de la energía en no computar.",
                "Sirve para comparar: entre dos proveedores, el de PUE más bajo desperdicia menos.",
            ],
            "nota": "No hace falta que memoricen el número. Lo que tiene que quedar es que una parte grande de la energía de un centro de datos no computa, y que hay una métrica con nombre para medirlo.",
        }),
        ("La misma función, dos decisiones", {
            "tipo": "tabla",
            "titulo": "Ejemplo: cuánto ahorra una sola decisión",
            "headers": ["", "Cada 5 segundos", "Cada 5 minutos"],
            "rows": [
                ["Pedidos de ubicación al día, por usuario", "17.280", "288"],
                ["Con 1.000 usuarios", "17.280.000", "288.000"],
                ["¿Cumple la función?", "Sí", "Sí"],
                ["Batería y red", "Mucho más gasto", "60 veces menos"],
            ],
            "note": "Un día tiene 86.400 segundos. 86.400 ÷ 5 = 17.280. 86.400 ÷ 300 = 288. La misma app, la misma función, 60 veces menos pedidos.",
            "nota": "Haga la cuenta con ellos: un día tiene 86.400 segundos. Es la forma más rápida de que entiendan que una decisión de diseño pequeña se multiplica por todos los usuarios y todos los días.",
        }),
        ("Cómo se estima una huella", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: el reporte diario de una tienda",
            "sub": "Los cinco pasos sobre un caso pequeño, sin un solo cálculo difícil.",
            "steps": [
                ("1 · El recorrido", "Computador de la tienda → internet → servidor → base de datos."),
                ("2 · Lo que se repite", "El reporte se genera completo cada vez que alguien lo abre: 40 veces al día."),
                ("3 · La etapa más pesada", "El servidor: recalcula todo el mes, 40 veces, aunque nada cambió."),
                ("4 · Dos decisiones", "Guardar el resultado y recalcular solo si hay ventas nuevas. Abrir solo el día, no el mes."),
                ("5 · Un indicador", "Veces que se recalcula el reporte al día: de 40 a 1."),
            ],
            "nota": "El paso 5 es el que convierte la conciencia en ingeniería: un indicador que se puede medir al final del semestre. Sin indicador, la mejora es una opinión.",
        }),
    ],

    # ── Clase 6 · Analisis de problemas tecnologicos del entorno ────────────
    6: [
        ("Síntoma, problema y solución disfrazada", {
            "tipo": "steps",
            "titulo": "Ejemplo: de la queja al problema, en cuatro pasos",
            "sub": "Todo empieza con algo que dice la gente. El trabajo es llegar al problema de verdad.",
            "steps": [
                ("La queja", "«La gente se queja de la biblioteca del barrio». Es un síntoma."),
                ("¿Se queja de qué?", "«No encuentran los libros». Sigue siendo vago."),
                ("¿A quién le pasa qué?", "Los estudiantes de colegio pierden tiempo buscando un libro porque el catálogo es un cuaderno."),
                ("Con su consecuencia", "Muchos se van sin el libro y no vuelven. **Ese** es el problema."),
            ],
            "nota": "Fíjese que en ningún paso aparece «hacer una app». Si un equipo llega al problema con la solución ya puesta, devuélvalo al primer paso.",
        }),
        ("El árbol del problema", {
            "tipo": "steps",
            "titulo": "Ejemplo resuelto: el árbol de la fila en la tienda",
            "sub": "Se lee de abajo hacia arriba: las raíces producen el tronco, y el tronco las ramas.",
            "steps": [
                ("Efectos (ramas)", "Clientes que se van sin comprar. Ventas perdidas en la hora pico."),
                ("Problema (tronco)", "En la hora pico, los clientes esperan unos 15 minutos para pagar."),
                ("Causas directas", "Hay una sola caja. Cada fiado se anota a mano en un cuaderno."),
                ("Causas de fondo", "Para cobrar un fiado hay que buscar el nombre página por página."),
            ],
            "nota": "Lo valioso está en las causas de fondo: buscar el fiado página por página es algo que sí se puede cambiar en un semestre. Comprar otra caja no.",
        }),
        ("La línea base", {
            "tipo": "content",
            "titulo": "Ejemplo: cómo se saca una línea base con el celular",
            "items": [
                "Ir a la tienda el **viernes de 6 a 7 p. m.**, que es la hora pico.",
                "Contar **10 clientes** y medir con el cronómetro del celular cuánto espera cada uno.",
                "Sumar y dividir: el promedio da **14 minutos**.",
                "Escribirlo completo: **«14 min de espera promedio · 10 clientes · viernes 6-7 p. m. · medido el 12/09»**.",
                "Al final del semestre se mide **igual** y se compara. Así se sabe si el proyecto sirvió.",
                "Sin esa cifra, «mejoramos la atención» no se puede comprobar.",
            ],
            "nota": "La regla de honestidad: toda cifra lleva cómo se obtuvo y cuándo. Un «14 min» suelto no vale; «14 min, 10 clientes, viernes en la noche» sí.",
        }),
        ("Cuándo un problema cabe en un semestre", {
            "tipo": "before_after",
            "titulo": "Ejemplo: el mismo problema, grande y del tamaño justo",
            "before_title": "No cabe en un semestre",
            "before": [
                "«La movilidad en Cali es mala».",
                "No hay una sola persona a quien preguntarle.",
                "No se puede medir con un cronómetro.",
                "Ningún equipo de 5 lo mueve en 11 semanas.",
            ],
            "after_title": "Cabe en un semestre",
            "after": [
                "«En el paradero del colegio, los estudiantes no saben si el MIO ya pasó».",
                "Se puede hablar con los estudiantes y con el celador.",
                "Se mide: cuántos esperan más de 20 minutos.",
                "Un equipo de 5 sí lo puede trabajar.",
            ],
            "nota": "Si un equipo no puede ponerle una cifra a su problema, casi siempre es porque es demasiado grande. La salida es bajarlo hasta un lugar y un grupo de personas concretos.",
        }),
    ],

    # ── Clase 7 · Ciclo de vida ─────────────────────────────────────────────
    7: [
        ("Las seis fases del ciclo de vida", {
            "tipo": "steps",
            "titulo": "Ejemplo: las seis fases en la app de turnos de la tienda",
            "sub": "Un solo proyecto pequeño, recorrido de punta a punta.",
            "steps": [
                ("DEFINICIÓN", "Los clientes esperan de pie 25 minutos sin saber cuántos van antes."),
                ("REQUISITOS", "El cliente ve su turno en el celular. Criterio: lo encuentra en menos de 1 minuto."),
                ("DISEÑO", "Tres pantallas: pedir turno, ver turno, aviso de «ya casi»."),
                ("CONSTRUCCIÓN", "Se arma la versión mínima con un formulario y una hoja de cálculo."),
                ("VALIDACIÓN", "Cinco clientes reales la prueban un sábado; se mide el tiempo."),
                ("OPERACIÓN Y RETIRO", "La tienda la usa; si se apaga, se borran los celulares guardados."),
            ],
            "nota": "Pida al grupo que diga en qué fase está hoy su propio proyecto. La respuesta correcta es: terminando la primera (la ficha de la Clase 6) y entrando en requisitos.",
        }),
        ("Lo que cuesta cambiar en cada fase", {
            "tipo": "tabla",
            "titulo": "Ejemplo: el mismo error, descubierto en tres momentos",
            "sub": "Error: la app pedía correo, y la mayoría de clientes de la tienda no lo usa.",
            "headers": ["Cuándo se descubre", "Qué hay que hacer", "Cuánto cuesta"],
            "rows": [
                ["En requisitos", "Cambiar «correo» por «celular» en una línea.", "Cinco minutos"],
                ["En construcción", "Rehacer el formulario, la hoja y los avisos.", "Una semana del equipo"],
                ["Ya en uso", "Todo lo anterior, más los clientes que no pudieron pedir turno.", "Clientes perdidos"],
            ],
            "nota": "Es la curva del costo del cambio con un caso que cualquiera entiende. Subraye que el error es el mismo; lo único que cambia es cuándo se encuentra.",
        }),
        ("Cuatro cosas que se entregan y no son código", {
            "tipo": "before_after",
            "titulo": "Ejemplo: requisitos mal y bien escritos",
            "before_title": "Mal escrito",
            "before": [
                "«El sistema tendrá una base de datos MySQL».",
                "«La app será rápida y fácil».",
                "«Ir avanzando con el diseño».",
            ],
            "after_title": "Bien escrito",
            "after": [
                "**Funcional:** «El cliente puede ver cuántos turnos van antes del suyo».",
                "**Criterio:** «Una persona que no conoce la app lo ve en menos de 1 minuto».",
                "**Hito:** «En la Clase 10 está el prototipo de las 3 pantallas».",
            ],
            "nota": "El primero de la izquierda no es un requisito: es una decisión de diseño disfrazada. El segundo no se puede comprobar. El tercero no tiene fecha ni resultado. La derecha se puede verificar con un sí o un no.",
        }),
    ],

    # ── Clase 8 · Taller del ciclo de vida ──────────────────────────────────
    8: [
        ("Cómo se decide entre dos alternativas", {
            "tipo": "tabla",
            "titulo": "Ejemplo: matriz de decisión resuelta",
            "sub": "¿Turnos por WhatsApp o por una página web? Pesos decididos antes de calificar (escala 1-3).",
            "headers": ["Criterio (peso)", "WhatsApp", "Página web"],
            "rows": [
                ["Los clientes ya lo usan (3)", "3 · todos lo tienen", "1 · hay que abrir enlace"],
                ["El equipo lo puede construir (2)", "2 · necesita un bot simple", "3 · formulario gratuito"],
                ["Se puede medir el tiempo (2)", "1 · difícil de registrar", "3 · queda en la hoja"],
                ["**Total ponderado**", "3·3 + 2·2 + 1·2 = **15**", "1·3 + 3·2 + 3·2 = **15**"],
            ],
            "nota": "El empate es a propósito: la matriz no decide sola. Ahí entra el paso 5: elegir y escribir qué se pierde. Si eligen la web, pierden comodidad del cliente; si eligen WhatsApp, pierden la medición. Ninguna respuesta es incorrecta si se justifica.",
        }),
        ("Alcance mínimo: qué entra y qué no", {
            "tipo": "before_after",
            "titulo": "Ejemplo: alcance soñado y alcance mínimo",
            "before_title": "Lo que el equipo soñaba",
            "before": [
                "Registro de usuarios con contraseña.",
                "Turnos, pagos, domicilios y promociones.",
                "App para Android y para iPhone.",
                "Nada se puede probar antes de la Clase 15.",
            ],
            "after_title": "Alcance mínimo",
            "after": [
                "**Solo** pedir turno y ver cuántos van antes.",
                "Sin registro: se entra con el celular.",
                "Se prueba con 5 clientes en la Clase 11.",
                "**Queda fuera:** pagos, domicilios, promociones.",
            ],
            "nota": "La prueba del alcance mínimo: si se construye solo esto y se pone delante del cliente, ¿le sirve? Aquí sí: deja de esperar de pie. La lista de lo que queda fuera se muestra en la exposición final.",
        }),
        ("El plan de validación, y dos trampas", {
            "tipo": "cards",
            "titulo": "Ejemplo: un plan de validación de tres líneas",
            "cards": [
                ("Con quién", "Cinco clientes de la tienda que **no** conocen al equipo, un sábado en la mañana."),
                ("Qué tarea", "«Pida un turno y dígame cuántas personas van antes que usted». Sin ayuda."),
                ("Qué se mide", "Cuántos lo logran y en cuánto tiempo. **Éxito:** 4 de 5 en menos de 1 minuto."),
                ("Lo que NO se pregunta", "«¿Le gusta la app?». Todos dicen que sí por cortesía y no se aprende nada."),
            ],
            "nota": "Muestre que cada línea responde a una trampa: ajenos al equipo (trampa 1) y una tarea en lugar de una opinión (trampa 2).",
        }),
    ],

    # ── Clase 9 · Innovación ────────────────────────────────────────────────
    9: [
        ("Qué es innovación y qué no", {
            "tipo": "before_after",
            "titulo": "Ejemplo: tecnología nueva o innovación",
            "before_title": "Tecnología nueva, sin innovación",
            "before": [
                "La tienda pone una pantalla táctil para pedir turno.",
                "Los clientes mayores no la saben usar.",
                "Siguen haciendo la fila de siempre.",
                "No cambió nada en la práctica.",
            ],
            "after_title": "Innovación, sin tecnología nueva",
            "after": [
                "La tienda reparte fichas de papel numeradas.",
                "Escribe en un tablero el número que va.",
                "Los clientes se sientan o salen y vuelven.",
                "Todos la adoptaron: **eso es innovar**.",
            ],
            "nota": "La palabra clave es adopta. La pantalla es más nueva y fracasó; la ficha es vieja y cambió la experiencia. Es una innovación de proceso, no de producto.",
        }),
        ("Cuatro maneras de generar una mejora", {
            "tipo": "tabla",
            "titulo": "Ejemplo: las cuatro operaciones sobre la fila de la tienda",
            "sub": "Antecedente: la fila con fichas de papel. Cada operación produce una idea distinta.",
            "headers": ["Operación", "Idea que sale"],
            "rows": [
                ["QUITAR", "Quitar la fila: el turno se pide desde la casa."],
                ["COMBINAR", "Ficha de papel + un mensaje de texto cuando faltan 3 turnos."],
                ["INVERTIR", "En vez de que el cliente pregunte «¿cuánto falta?», la tienda le avisa."],
                ["ADAPTAR", "Traer el sistema de turnos de los bancos y las EPS a una tienda de barrio."],
            ],
            "nota": "Subraye que todas parten de algo que ya existe. Sin el antecedente de la fila con fichas, ninguna de las cuatro ideas aparece.",
        }),
        ("Cómo se busca un antecedente en cinco pasos", {
            "tipo": "steps",
            "titulo": "Ejemplo: la búsqueda del antecedente, hecha",
            "steps": [
                ("1 · Pregunta", "¿Cómo manejan los turnos los negocios pequeños que no tienen sistema?"),
                ("2 · Términos", "«turnos virtuales», «gestión de filas», «queue management small business»."),
                ("3 · Sitios", "Google Scholar, el repositorio de una universidad, y apps de turnos que ya existen."),
                ("4 · Filtro", "Se descarta un blog sin autor; se queda una tesis de 2021 sobre filas en droguerías."),
                ("5 · Ficha", "Autor, año, enlace, qué hace y qué le falta: «exige que el cliente instale una app»."),
            ],
            "nota": "Lo que le falta al antecedente es la oportunidad del equipo: aquí, una solución que no obligue a instalar nada.",
        }),
    ],

    # ── Clase 10 · Herramientas y prototipo ─────────────────────────────────
    10: [
        ("Qué es un prototipo y qué no", {
            "tipo": "before_after",
            "titulo": "Ejemplo: maqueta decorativa y prototipo",
            "before_title": "Maqueta decorativa",
            "before": [
                "Diez pantallas bonitas en Canva.",
                "Nadie escribió qué se quería averiguar.",
                "Solo la vio el equipo.",
                "Al final: «quedó lindo».",
            ],
            "after_title": "Prototipo",
            "after": [
                "**Pregunta:** ¿el cliente entiende cuántos turnos van antes?",
                "Tres pantallas dibujadas en papel.",
                "Se las muestran a 3 clientes de la tienda.",
                "Al final: «2 de 3 no vieron el número; hay que agrandarlo».",
            ],
            "nota": "La derecha aprendió algo con una hora de trabajo; la izquierda gastó una tarde y no aprendió nada. Pida a cada equipo que escriba la pregunta de su prototipo antes de dibujar.",
        }),
        ("Cómo se dibuja una pantalla que sirve", {
            "tipo": "steps",
            "titulo": "Ejemplo: la pantalla «ver mi turno», en cinco pasos",
            "steps": [
                ("1 · Para qué existe", "«Aquí el cliente sabe cuántas personas van antes que él»."),
                ("2 · Camino principal", "Un número grande al centro: **«Van 4 antes que usted»**."),
                ("3 · Textos reales", "«Su turno: 27» y no «texto aquí»."),
                ("4 · Vacío y error", "«Aún no tiene turno → Pedir turno» · «Sin conexión: intente de nuevo»."),
                ("5 · Qué pasa al tocar", "«Cancelar turno» → pantalla de confirmación."),
            ],
            "nota": "El paso 4 es el que casi nadie dibuja, y es donde el usuario real se pierde. Exíjalo en el taller.",
        }),
    ],

    # ── Clase 11 · Prototipado con IA ───────────────────────────────────────
    11: [
        ("Cómo se le pide algo a la IA en este curso", {
            "tipo": "before_after",
            "titulo": "Ejemplo: la misma petición, mal y bien hecha",
            "before_title": "Petición sin contexto",
            "before": [
                "«Hazme una app de turnos».",
                "La IA no sabe para quién ni con qué límites.",
                "Devuelve registro, pagos y notificaciones.",
                "El equipo la copia tal cual.",
            ],
            "after_title": "Petición del curso",
            "after": [
                "«Tienda de barrio; clientes mayores; sin computador en el mostrador».",
                "«Dame **tres** maneras distintas de mostrar el turno».",
                "«**Sin** cuentas, **sin** pedir datos personales».",
                "El equipo anota qué corrigió y lo declara.",
            ],
            "nota": "La petición de la derecha usa los pasos 1, 2, 3 y 4. Haga que cada equipo reescriba su primera petición con esta forma antes de abrir el asistente.",
        }),
    ],

    # ── Clase 12 · Avances ──────────────────────────────────────────────────
    12: [
        ("Cómo se lee una prueba con una persona real", {
            "tipo": "tabla",
            "titulo": "Ejemplo: tres pruebas leídas y clasificadas",
            "sub": "Tarea: «pida un turno y diga cuántos van antes». Tres clientes de la tienda.",
            "headers": ["Lo que hizo", "Tipo", "¿Patrón?"],
            "rows": [
                ["Preguntó qué significa «en cola».", "Lenguaje", "2 de 3 · se cambia por «antes que usted»"],
                ["Buscó volver arriba a la izquierda.", "Flujo", "1 de 3 · se anota y se observa"],
                ["Preguntó si podía pagar ahí.", "Expectativa", "Fuera del alcance · se escribe y no se arregla"],
            ],
            "nota": "Muestre que la columna de la izquierda describe lo que la persona hizo, no lo que el equipo opina. Solo el primero es patrón, y es el arreglo más barato: un texto.",
        }),
        ("Cómo se da retroalimentación que sirve", {
            "tipo": "before_after",
            "titulo": "Ejemplo: retroalimentación que no sirve y que sí",
            "before_title": "No sirve",
            "before": [
                "«Está muy bien, me gustó».",
                "«La navegación es mala».",
                "«Yo lo haría con una app».",
            ],
            "after_title": "Sí sirve",
            "after": [
                "«¿Por qué el número de turno va abajo?»",
                "«Cuando lo mostraron, no encontré cómo cancelar».",
                "«Yo esperaba ver cuánto tiempo falta, no solo cuántos van».",
            ],
            "nota": "Cada línea de la derecha corresponde a un paso: pregunta, observación, expectativa. Ninguna rediseña el proyecto ajeno.",
        }),
    ],

    # ── Clase 13 · Impacto ──────────────────────────────────────────────────
    13: [
        ("Cómo se encuentra a los afectados que no son usuarios", {
            "tipo": "cards",
            "titulo": "Ejemplo: afectados de la app de turnos que nunca la usan",
            "cards": [
                ("El cajero", "Ahora además debe actualizar el turno en el celular: **más trabajo** (paso 2)."),
                ("Doña Rosa, 74 años", "No tiene datos móviles: **queda fuera** si la fila desaparece (paso 3)."),
                ("El vendedor de fichas", "La tienda le compraba los talonarios de papel: **lo desplaza** (paso 5)."),
                ("El plan de datos", "Cada consulta gasta datos que paga el cliente: **consumo** (paso 4)."),
            ],
            "nota": "Ninguno de los cuatro abre la app y a todos les cambia algo. Pida a cada equipo que encuentre al menos dos así en su proyecto.",
        }),
        ("Cómo se califica un impacto, sin fingir precisión", {
            "tipo": "tabla",
            "titulo": "Ejemplo: un impacto negativo calificado",
            "sub": "«Doña Rosa y los clientes sin datos quedan fuera si se elimina la fila física».",
            "headers": ["Criterio", "Calificación", "Por qué"],
            "rows": [
                ["Carácter", "Negativo", "Pierden el servicio que tenían"],
                ["Magnitud", "Alta", "Para ellos, no poder comprar es grave"],
                ["Extensión", "Un grupo", "Cerca de 1 de cada 5 clientes"],
                ["Reversibilidad", "Reversible", "**Mitigación:** se mantienen fichas de papel"],
            ],
            "nota": "La mitigación sale de la misma calificación: como es reversible, se mantiene la ficha de papel junto a la app. Eso es lo que se espera en la matriz.",
        }),
    ],

    # ── Clase 14 · Presentación final ───────────────────────────────────────
    14: [
        ("Los cinco tramos de nueve minutos", {
            "tipo": "steps",
            "titulo": "Ejemplo: los cinco tramos de la app de turnos, dichos",
            "steps": [
                ("1 · 1 min", "«En la tienda de don Jaime, los clientes esperan **25 minutos de pie**»."),
                ("2 · 2 min", "«Afecta también al cajero. Elegimos web y no WhatsApp: **perdimos comodidad**»."),
                ("3 · 3 min", "Se pide un turno en vivo y se ve «Van 4 antes que usted»."),
                ("4 · 2 min", "«2 de 3 no entendieron «en cola»; lo cambiamos. Pagos: decidimos no hacerlo»."),
                ("5 · 1 min", "«Ahorra 20 minutos de pie. Deja fuera a quien no tiene datos: **mantenemos fichas**»."),
            ],
            "nota": "Cronometre leyéndolo en voz alta frente al grupo: dura menos de nueve minutos porque cada tramo trae una sola idea y un número.",
        }),
    ],

    # ── Clase 15 · Exposición final ─────────────────────────────────────────
    15: [
        ("Los tres minutos de preguntas también son exposición", {
            "tipo": "before_after",
            "titulo": "Ejemplo: la misma pregunta, dos respuestas",
            "sub": "Pregunta del curso: «¿Por qué la app no deja pagar?»",
            "before_title": "Excusa",
            "before": [
                "«No alcanzamos el tiempo».",
                "«Lo íbamos a hacer pero el profe dijo que no».",
                "Responde quien no hizo esa parte, y duda.",
            ],
            "after_title": "Decisión",
            "after": [
                "«**Decidimos** dejarlo fuera del alcance mínimo en la sesión 8».",
                "«Pagar exige guardar datos que no necesitamos para el turno».",
                "Responde quien hizo la matriz, en 30 segundos.",
            ],
            "nota": "La respuesta de la derecha cita una decisión documentada y su razón. Es la que se califica alto, aunque la función no exista.",
        }),
    ],

    # ── Clase 16 · Informe final ────────────────────────────────────────────
    16: [
        ("Cuatro errores frecuentes del informe", {
            "tipo": "before_after",
            "titulo": "Ejemplo: la sección 10 del informe, vacía y bien hecha",
            "before_title": "Sección 10 vacía",
            "before": [
                "«Limitaciones: ninguna».",
                "«Trabajo futuro: mejorar la app».",
            ],
            "after_title": "Sección 10 que suma",
            "after": [
                "«No se arregló el botón de volver: 1 de 3 lo buscó (Clase 12)».",
                "«Queda fuera quien no tiene datos; se mitiga con fichas (Clase 13)».",
                "«Siguiente paso: probar con 10 clientes un sábado completo».",
            ],
            "nota": "Cada línea de la derecha cita la sesión de donde sale. Un informe así se arma con lo que ya hicieron; no hay que inventar nada.",
        }),
    ],
}
