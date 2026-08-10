# Guion docente · Clase 9 · Casos de uso

- **Curso:** Seminario de Sistemas (FI303301) · 120 min
- **Hilo:** Proyecto Integrador **VetCare** — planos del sistema de la clinica «Huellitas»
- **Hoy avanzamos el PI en:** Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente.
- **Entregable de hoy:** Un PDF con el diagrama de casos de uso, la matriz de trazabilidad RF a CU y las dos especificaciones textuales completas (precondiciones, postcondiciones, flujo principal y minimo dos flujos alternos cada una), subido a ExamLab.
- **Herramienta:** draw.io · Google Docs
- **Slides:** `Clases/Clase 9 - Casos de uso/Presentacion.pptx`

> Sin mapa del curso, sin bio del docente, sin fechas de periodo: eso vive en la Sesion 0.

## Fundamento teorico para el docente

Un caso de uso es la descripcion de una interaccion completa entre un actor y el sistema que termina entregando un resultado con valor observable para ese actor. La palabra clave es completa: no es una pantalla, no es un boton, no es una tabla de la base de datos y no es un paso intermedio. La prueba practica que usamos en clase es la del almuerzo: si el actor puede levantarse de la silla e irse a almorzar satisfecho porque ya logro lo que queria, entonces eso es un caso de uso. En VetCare, Registrar mascota pasa la prueba, porque la recepcionista de Huellitas termina con la ficha creada y el codigo asignado; en cambio Validar la fecha de nacimiento no la pasa, porque nadie llega a la clinica con el objetivo de validar una fecha. Esa distincion parece un detalle de nombres, pero define el tamaño de todo el modelo: si se confunde, un sistema pequeño como VetCare termina con cuarenta casos de uso inutiles en vez de seis u ocho casos de uso reales. La regla de redaccion es simple y no se negocia: verbo en infinitivo mas objeto del dominio, escrito con las palabras de la clinica y no con palabras de programador.

El actor es un rol, no una persona ni un cargo del organigrama. Doña Marta, la recepcionista de Huellitas, no es un actor: el actor es Recepcionista, y si mañana la reemplazan el modelo no cambia. Una misma persona puede encarnar dos actores, por ejemplo el veterinario dueño de la clinica que a veces atiende y a veces revisa las metricas: alli actua como Veterinario y como Administrador, y por eso aparecen dos monigotes. Ademas existen actores que no son humanos: un sistema externo que enviaria los recordatorios por mensajeria seria un actor secundario de VetCare, porque participaria en el caso de uso pero no es quien lo inicia. Todo esto se ordena con el limite del sistema, ese rectangulo que muchos omiten y que en realidad es la decision de arquitectura mas importante del diagrama: adentro va lo que nosotros vamos a construir y por lo tanto especificar, y afuera queda lo que solo vamos a consumir o a recibir. Si en VetCare dibujamos adentro del rectangulo un caso de uso llamado Enviar mensaje de WhatsApp, estamos diciendo que nosotros construimos la mensajeria, y eso probablemente sea falso y encarezca el proyecto por escrito.

Las relaciones entre casos de uso son tres y se abusa de ellas. Include significa que el caso base siempre ejecuta el caso incluido, y se usa cuando un comportamiento se repite en varios casos y vale la pena escribirlo una sola vez: en VetCare, CU-03 Registrar consulta medica y CU-04 Agendar cita incluyen ambos a Verificar existencia de la mascota, siempre, sin condicion. Extend es lo contrario: comportamiento opcional que se dispara solo si se cumple una condicion en un punto de extension del caso base; en VetCare, CU-02 Buscar expediente puede extenderse con CU-06 Exportar expediente a PDF, que ocurre unicamente cuando el veterinario lo pide. La generalizacion, mucho menos frecuente, sirve cuando un actor especializa a otro, por ejemplo Veterinario especialista como especializacion de Veterinario. El peligro real no es equivocarse en la flecha sino usar include para descomponer funcionalmente: si el diagrama muestra Registrar mascota incluyendo Abrir formulario, incluyendo Digitar datos, incluyendo Guardar en base de datos, ya no es un modelo de casos de uso sino un diagrama de flujo disfrazado, y ese error contagia despues al diagrama de clases.

La especificacion textual es donde vive el noventa por ciento del valor y donde casi nadie invierte tiempo. Un caso de uso especificado tiene ficha de identificacion (ID, nombre, actor primario, requisitos que cubre, prioridad y frecuencia), precondiciones, postcondiciones, flujo principal y flujos alternos, y las reglas de negocio asociadas. El flujo principal se escribe en pares de responsabilidad: una columna dice que hace el actor y la otra que hace el sistema, alternandose, en pasos numerados y sin adjetivos. Por ejemplo, en Buscar expediente el paso 1 es que el veterinario digita el codigo o el nombre de la mascota y el paso 2 es que el sistema devuelve la lista de coincidencias; nunca se escribe el sistema es rapido y amigable, porque eso no es un paso sino un requisito no funcional que ya vive en otro documento, el RNF-02, que exige mostrar el resultado en menos de tres segundos. Los flujos alternos se numeran respecto al paso donde se desvian: 2a cuando no hay coincidencias, 2b cuando hay demasiadas, 4a cuando la mascota esta inactiva. Ese numerito es lo que permite que el compañero de Programacion II sepa exactamente en que punto del comportamiento hay que preguntar algo, y es tambien la razon por la cual la clinica Huellitas deja de perder tiempo buscando historiales.

Precondiciones y postcondiciones son un contrato, no un adorno. La precondicion es aquello que debe ser verdadero antes de empezar y que el caso de uso no vuelve a verificar dentro del flujo: si escribimos que el usuario esta autenticado como precondicion de Registrar mascota, entonces el flujo principal no puede tener un paso que diga el sistema pide usuario y contraseña, porque eso ya ocurrio. La postcondicion describe el estado en que queda el sistema cuando el caso termina, y debe ser verificable mirando los datos: en VetCare la postcondicion de exito de Registrar mascota es que existe una ficha con codigo unico asociada a un propietario y que quedo bitacora de quien la creo y cuando; la postcondicion de fracaso es que no queda ningun registro a medias. Escribirlas asi tiene dos consecuencias practicas enormes. Primero, cada postcondicion se convierte casi automaticamente en un caso de prueba, porque describe algo que se puede ir a comprobar. Segundo, resuelve la discusion entre los tres casos de matricula: el estudiante que solo cursa Seminario cierra con este documento y su prototipo navegable y ya entrego un producto completo, mientras que el que solo cursa Programacion II recibe estas postcondiciones y sabe exactamente que debe dejar guardado su codigo, sin tener que adivinar ni volver a entrevistar a la clinica.

Error tipico del docente que no domina el tema: dibujar los monigotes, las elipses y el rectangulo, sentirse satisfecho y dar por terminado el tema de casos de uso, cuando en realidad apenas hizo la portada. De ese error nacen los otros cuatro que veremos en los talleres. Uno, convertir cada operacion CRUD y cada boton en un caso de uso, de modo que VetCare aparece con Ingresar usuario, Validar contraseña, Mostrar mensaje de error y Cerrar ventana como si fueran objetivos de negocio. Dos, usar include como si fuera una flecha de orden de pantallas, cuando include no dice nada sobre el orden en el tiempo, para eso existe el diagrama de secuencia que veremos en la clase doce. Tres, dejar las precondiciones en blanco o llenarlas con frases vacias como el sistema debe estar funcionando, que no restringe nada. Y cuatro, no escribir flujos alternos, que es el mas caro de todos, porque los flujos alternos son precisamente lo que la clinica Huellitas vive a diario: el propietario que no esta registrado, la mascota que aparece dos veces, la busqueda que no devuelve nada. Si el docente no exige alternos, el estudiante entrega un sistema que solo funciona el dia perfecto que nunca existe.

**Demo que usted debe poder repetir:** El docente proyecta como un caso de uso mal escrito (Dar clic en guardar) se transforma en uno correcto (Registrar mascota) y luego llena en vivo, delante del grupo, la plantilla de especificacion de Buscar expediente.

## Plan minuto a minuto (120 min)

### 0-10 · Encuadre
**Decir:** «Hoy avanzamos VetCare en: Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente. La teoria es corta; el peso esta en
el taller del proyecto.»
Pasar asistencia. Recordar donde quedo el avance de la clase pasada.

### 10-40 · Teoria Core
Cubrir el fundamento de arriba apoyandose en la slide «Teoria Core» y en la de codigo
proyectable. Cada 8-10 min, amarrar al producto: «esto es lo que van a dejar hoy en VetCare».
Pregunta al aire (2 min): ¿donde encaja esto en el VetCare de su equipo?

### 40-60 · Demo en vivo
**Decir:** «Miren mi pantalla. Dominio VetCare — no otro ejemplo.»
Demo: El docente proyecta como un caso de uso mal escrito (Dar clic en guardar) se transforma en uno correcto (Registrar mascota) y luego llena en vivo, delante del grupo, la plantilla de especificacion de Buscar expediente.
Escribir el codigo en vivo (no copiar-pegar). Codigo de apoyo:
`Kit docente/Clase 9/Plantillas/CU-VetCare-Especificacion.md`

### 60-105 · Taller guiado = avance del PI
**Decir:** «Equipos: abran su proyecto VetCare. Esto suma a la rubrica del PI.»
Actividades:
1. En draw.io, dibujar el limite del sistema rotulado VetCare y ubicar afuera los actores como roles (Recepcionista, Veterinario, Administrador y el servicio externo de mensajeria como actor secundario candidato, que hoy todavia no se conecta a ningun caso de uso); ningun actor puede llamarse con nombre propio ni con cargo inventado.
2. Colocar dentro del limite entre seis y ocho casos de uso derivados del catalogo de RF ya construido, todos redactados como verbo en infinitivo mas objeto del dominio, y borrar de inmediato cualquier elipse que se llame Guardar, Validar, Mostrar o Iniciar pantalla.
3. Construir en Google Docs la matriz de trazabilidad RF a CU: cada requisito funcional debe apuntar al menos a un caso de uso y cada caso de uso debe nacer de al menos un requisito; marcar en rojo los huerfanos que aparezcan y anotar por escrito la decision que se tomara con cada uno.
4. Modelar exactamente una relacion include y una relacion extend en el diagrama, y escribir al lado, en una nota de draw.io, una frase que justifique por que una es obligatoria y la otra condicional; si no se puede justificar, se elimina la flecha.
5. Diligenciar la plantilla completa de especificacion para CU-01 Registrar mascota y CU-02 Buscar expediente, con precondiciones, postcondiciones de exito y de fracaso, flujo principal en pares actor-sistema y minimo dos flujos alternos cada uno; exportar todo a PDF y subirlo a ExamLab.
Circular por los equipos. Empujar evidencia funcionando, no perfeccionismo.
Entregable: Un PDF con el diagrama de casos de uso, la matriz de trazabilidad RF a CU y las dos especificaciones textuales completas (precondiciones, postcondiciones, flujo principal y minimo dos flujos alternos cada una), subido a ExamLab.

### 105-120 · Criterios de exito y cierre
Repasar el checklist de la slide de criterios.
Aplicar el quiz corto de `Kit docente/Clase 9/Quiz Clase 9 - VetCare.docx`
(la clave va aparte y **no se proyecta**).
**Decir:** «Queda avanzado: Queda listo el diagrama de casos de uso de VetCare con su limite de sistema y la especificacion textual completa de Registrar mascota y Buscar expediente.. Entrega en ExamLab, domingo 23:59.»

## Solucion del taller (privada)
`Kit docente/Clase 9/Solucion Taller Clase 9 - VetCare.docx` — no proyectar completa.
