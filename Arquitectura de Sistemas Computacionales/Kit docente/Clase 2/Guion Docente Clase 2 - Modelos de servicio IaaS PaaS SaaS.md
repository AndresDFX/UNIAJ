# Guion docente — Clase 2: Modelos de servicio: IaaS, PaaS, SaaS

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Comparar IaaS, PaaS y SaaS con criterios de control, operación y velocidad.
- Elegir el modelo dominante de CloudLite con justificación.
- Documentar la decisión como ADR reutilizable en el informe PI.

## Hoy avanzamos el PI en…
**Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**

**Entregable concreto:** ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio

**Herramienta:** Google Docs · draw.io (opcional)

## Fundamento teórico para el docente
### De que se parte y que se decide hoy - diapositiva 4
Esta clase se dicta en sesion virtual sincrona, en el mismo bloque de 120 minutos de siempre: hay explicacion en vivo, taller acompanado y tiempo para preguntar, asi que este fundamento es material del docente para dictar y no una lectura que reemplace la clase. El punto de partida es lo definido en la Clase 1: cada estudiante ya tiene un dominio para CloudLite App, tres a cinco capacidades, sus actores y un diagrama de contexto. La pregunta de hoy es la siguiente en orden logico: si ese sistema va a vivir en la nube, quien administra cada capa de la maquinaria que lo sostiene. No hay una sola respuesta, hay tres respuestas estandar que la industria llama IaaS, PaaS y SaaS, y elegir entre ellas es una decision de arquitectura con consecuencias medibles en costo, velocidad de entrega, seguridad y libertad futura.
### La pila de responsabilidades: donde se corta la linea - diapositiva 5
Para entender los tres modelos hay que ver primero la pila completa de responsabilidades que existe debajo de cualquier aplicacion, de abajo hacia arriba: el edificio y la energia electrica, el hardware fisico (servidores, discos, cableado de red), la capa de virtualizacion que parte ese hardware en maquinas logicas, el sistema operativo de cada maquina, el runtime o entorno de ejecucion (por ejemplo Node.js, Python o la maquina virtual de Java) junto con servicios de apoyo como la base de datos, y finalmente el codigo de la aplicacion, sus datos y la administracion de usuarios y permisos. Son ocho o nueve capas segun como se cuente. En el modelo tradicional, llamado on-premise porque los equipos son propios y estan en las instalaciones de la organizacion, todas son responsabilidad del cliente. Los tres modelos de servicio se distinguen exactamente por donde se traza la linea que separa lo que administra el proveedor de lo que administra el cliente. Nada mas y nada menos: si el estudiante entiende esa frase, entendio la clase.
### IaaS, PaaS y SaaS: los tres cortes, uno por uno - diapositiva 5
IaaS, infraestructura como servicio, corta la linea justo encima de la virtualizacion: el proveedor entrega maquinas virtuales, redes y discos, y el cliente recibe una maquina practicamente vacia con un sistema operativo que debe actualizar, endurecer, monitorear y respaldar el mismo. Lo que gana es control total, porque puede instalar cualquier version de cualquier cosa, abrir los puertos que quiera y afinar el sistema. Lo que paga es trabajo operativo permanente, que en la practica se mide en horas de persona por semana dedicadas a aplicar parches de seguridad, rotar certificados y vigilar el espacio en disco. Para CloudLite Turnos, el ejemplo de la barberia con agendamiento de citas, elegir IaaS significaria que el estudiante se compromete a administrar el sistema operativo donde corren la API y la base de datos; en un curso de doce semanas, y trabajando solo o con dos companeros, eso consume justamente el tiempo que deberia dedicarse a disenar la arquitectura y a sustentarla.

PaaS, plataforma como servicio, sube la linea dos escalones: el proveedor administra tambien el sistema operativo y el runtime, y el cliente entrega su codigo mas un archivo de configuracion; la plataforma lo construye, lo empaqueta y lo pone a correr. El cliente pierde el acceso a la maquina, porque ya no hay un servidor donde entrar por consola, y gana velocidad: un despliegue que en IaaS implica preparar una imagen, configurar el servicio y probar la red, en PaaS se reduce a subir el codigo al repositorio. Los niveles gratuitos tipicos de este modelo ofrecen del orden de 512 MB de memoria por instancia, una cantidad limitada de horas de ejecucion al mes y suspension automatica del servicio tras unos 15 minutos sin trafico, lo que produce el efecto conocido como arranque en frio: la primera peticion despues de la inactividad puede tardar varios segundos en lugar de milisegundos. Esos numeros son ordenes de magnitud tipicos que varian entre proveedores, no constantes; lo estructural es el patron, porque gratis siempre implica limites de memoria, de horas y de latencia en frio, y el estudiante debe anticiparlo en su diseno en vez de descubrirlo la noche antes de la sustentacion.

SaaS, software como servicio, lleva la linea hasta arriba: el proveedor administra la aplicacion completa y el cliente solo la configura y la usa, sin desplegar nada. El correo corporativo, un servicio de envio de mensajes transaccionales, un proveedor de identidad que resuelve el inicio de sesion o un servicio de almacenamiento y transformacion de imagenes son SaaS desde la perspectiva de quien construye CloudLite. Y aqui esta el punto que casi siempre se pierde: los tres modelos no son excluyentes y un sistema real los combina. La arquitectura probable de CloudLite Turnos es hibrida: la API desplegada como PaaS, la base de datos como servicio gestionado (que es PaaS en su variante de datos), el envio de recordatorios delegado a un SaaS de correo y el almacenamiento de fotos de perfil a un SaaS de archivos. El entregable de hoy no pide elegir un modelo unico para todo el sistema; pide elegir por componente y justificar cada eleccion, que es exactamente como se decide en la industria.
### Responsabilidad compartida: quien responde por que - diapositiva 6
El concepto que unifica todo esto se llama modelo de responsabilidad compartida y se resume en una frase que conviene memorizar: el proveedor es responsable de la seguridad DE la nube y el cliente de la seguridad EN la nube. El proveedor garantiza que el centro de datos no se incendie, que la capa de virtualizacion este parcheada y que los discos esten cifrados en reposo; el cliente sigue siendo responsable de sus contrasenas, sus permisos, sus datos y su configuracion. Importa porque la causa dominante de los incidentes de seguridad en la nube no son fallas del proveedor sino configuraciones erradas del cliente: un almacenamiento de archivos dejado publico, una credencial subida al repositorio en texto plano, un puerto de base de datos expuesto a internet. Subir de IaaS a PaaS reduce la superficie de responsabilidad del cliente, pero nunca la elimina, y esa idea es el punto de partida literal de la Clase 6. De ahi sale el trade-off central, que se escribe como regla practica: a mas abstraccion, menos control y menos trabajo operativo. Pero hay un tercer eje que el estudiante no ve solo, el amarre al proveedor o vendor lock-in, que es el costo de mudarse a otro proveedor mas adelante: bajo en IaaS, porque una maquina virtual con Linux se parece a cualquier otra; medio en PaaS, porque el archivo de configuracion y algunos servicios son propietarios; potencialmente alto en SaaS, porque los datos y parte de la logica viven dentro de un producto ajeno. Para CloudLite la mitigacion no es evitar SaaS sino acotarlo: si el envio de correos se encapsula detras de una interfaz propia, por ejemplo un modulo Notificador con un solo metodo enviar, cambiar de proveedor toca un archivo y no cuarenta.
### El ADR-001: seis secciones rotuladas y una sola decision - diapositiva 7
El entregable concreto es el ADR-001. Un ADR (Architecture Decision Record, registro de decision arquitectonica) es un documento corto, de media pagina a una pagina, que registra UNA sola decision. En este curso tiene SEIS secciones rotuladas, siempre las mismas y en este orden, y hay que dictarlas tal cual porque son las que la actividad califica: 1) Titulo, con el numero consecutivo del ADR; 2) Estado, que hoy es «Aceptado» mas la fecha de la sesion; 3) Contexto, o sea las restricciones bajo las que se decide; 4) Decision, en una sola frase y con un unico modelo dominante; 5) Alternativas descartadas, exactamente dos y con el motivo atado al dominio; 6) Consecuencias, con lo bueno y lo malo que se acepta. El reparto en la plataforma es que las cinco primeras van en la pregunta 6 y la sexta en la pregunta 7, pero es UN solo documento, y conviene decirlo en voz alta porque el estudiante que lo entienda como dos ejercicios sueltos repite la decision en las consecuencias y pierde puntos. No hay seccion de «opciones consideradas»: ese analisis es la matriz de la pregunta 5, y en el ADR solo quedan las dos alternativas que se descartaron. La regla de una decision por documento no es burocracia: es lo que permite que meses despues alguien lea por que se eligio algo sin depender de la memoria de nadie.

Conviene mostrar la diferencia entre contexto y analisis con el ejemplo, porque es donde se pierde la seccion 3 completa. Un ADR-001 aceptable para CloudLite Turnos diria en CONTEXTO: la barberia agenda por mensajeria y pierde alrededor de tres turnos diarios por doble reserva; el proyecto lo sostiene un desarrollador (o un equipo de dos o tres, si el docente lo autorizo) durante doce semanas, sin presupuesto ni tarjeta de credito, y el sistema tiene que estar disponible el dia de la sustentacion. Eso es contexto: son restricciones, no teoria. «Existen tres modelos de servicio y hay que elegir uno» NO es contexto, es el apunte de clase, y esa confusion es el error dominante de la pregunta 6. La prueba que el docente puede aplicar en voz alta mientras pasa por los grupos es una sola: si del contexto no se puede deducir por que se descarta IaaS, todavia no es contexto. En DECISION va una frase: la aplicacion de CloudLite Turnos se despliega sobre PaaS. En ALTERNATIVAS DESCARTADAS van dos y solo dos: IaaS con maquina virtual propia, descartada porque habria que asumir parches y respaldos del sistema operativo sin tiempo para ello; y SaaS de agendamiento ya existente, descartada porque el proyecto perderia su objeto, ya que no habria arquitectura que disenar sino solo configuracion. Que identidad y correo se consuman como SaaS satelite se aclara aqui y no en la decision, porque el modelo dominante se refiere a la aplicacion propia. Y en CONSECUENCIAS, que es la seccion que los estudiantes dejan a medias, deben aparecer tambien las malas: se acepta un arranque en frio de varios segundos tras inactividad, se acepta no poder afinar el sistema operativo y se acepta un amarre medio al proveedor, mitigado con contenedores.
### Preguntas frecuentes y cierre conceptual (de la diapositiva 5 a la diapositiva 8)
Tres preguntas salen en voz alta en esta clase casi sin falta y conviene tener la respuesta lista, porque las tres se contestan en treinta segundos y desbloquean el taller. Cual de los tres modelos es el mejor: ninguno; la pregunta correcta es cual conviene para este componente, con este equipo y en este plazo, y responder que PaaS es mejor sin decir para que es la senal de que el ADR sera de relleno. Donde encaja serverless o las funciones como servicio: es una variante extrema de PaaS en la que no se administra ninguna instancia siempre encendida, se paga por invocacion y el codigo debe tolerar arrancar en frio; para efectos del curso se clasifica como PaaS anotando la diferencia. Y la mas comun: si elegimos PaaS, para que aprendemos Docker en la Clase 3 si la plataforma se encarga de todo. Respuesta: porque la plataforma construye internamente una imagen de contenedor con el codigo entregado, de modo que entender contenedores es entender que hace la plataforma por debajo, y porque el contenedor es precisamente el artefacto que vuelve reversible la decision de hoy. La Clase 4 usara este mismo ADR para justificar cuantas piezas tendra el sistema, y el Parcial 1 de la Clase 5 evalua la capacidad de ubicar la linea de responsabilidad en cada modelo.

Error tipico del docente que no domina el tema: presentar IaaS, PaaS y SaaS como catalogos de marcas y no como un modelo conceptual de responsabilidad, con lo cual el estudiante memoriza nombres de productos que cambiaran en dos periodos y no aprende a preguntar quien administra que capa; aguas abajo, en la Clase 6 sera incapaz de decir de que es responsable el en materia de seguridad, y en la Clase 10 no podra explicar por que su factura hipotetica sube o baja. El segundo error es dejar pasar ADR sin consecuencias negativas, y como esta clase tiene encuentro sincronico no hay excusa para no corregirlo en el momento: al pasar por los grupos en el tramo de taller, pregunte «que perdieron al elegir eso» antes de que el documento se suba. Un ADR que solo lista beneficios no es una decision, es una justificacion escrita despues de los hechos, y quien lo entrega asi llegara a la Clase 11 sin poder explicar ningun trade-off de su arquitectura, que es justamente lo que se le exigira sustentar en la Clase 15.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 2 - Modelos de servicio IaaS PaaS SaaS/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 2 · Modelos de servicio: IaaS, PaaS, SaaS
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. IaaS · PaaS · SaaS (sin cloud de pago)
6. Cómo decidir para CloudLite
7. Plantilla ADR-001
8. ADR-001 — las 6 secciones caben en una pagina
9. Herramientas de hoy
10. Taller PI (paso a paso)
11. Para continuar (PI)
12. Clase 2 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 4]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve**.
Entregable concreto: ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~10 min cada uno, con su diapositiva:
- **IaaS · PaaS · SaaS (sin cloud de pago)** · [Slide 5]
- **Cómo decidir para CloudLite** · [Slide 6]
- **Plantilla ADR-001** · [Slide 7]

**Ninguna se salta**: cada una de esas diapositivas es el mecanismo con que se resuelve
al menos una pregunta de la actividad calificada de hoy.
El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 8]
Herramienta del día: **Google Docs · draw.io (opcional)**.
**Demo que usted debe poder repetir:** Llenar un ADR-001 delante del grupo, con sus 6 secciones rotuladas

1. Abra un Google Doc y escriba los 6 encabezados en orden: 1. Titulo · 2. Estado · 3. Contexto · 4. Decision · 5. Alternativas descartadas · 6. Consecuencias.
2. Titulo: «ADR-001 Modelo de servicio dominante de CloudLite App». Estado: «Aceptado» y la fecha de hoy. Diga en voz alta: «estos dos rotulos valen 1.5 puntos y son los que se citan en la sustentacion».
3. Contexto: «lo desarrolla una persona en doce semanas, sin presupuesto ni tarjeta, y tiene que estar en linea el dia de la sustentacion». Subraye que son RESTRICCIONES: «existen tres modelos y hay que elegir uno» no es contexto, es el apunte de clase.
4. Decision, en una sola frase: «la aplicacion de CloudLite se despliega sobre PaaS». Tache en vivo un segundo modelo si alguien lo propone: «esta seccion vale cero si nombra dos».
5. Alternativas descartadas, exactamente dos: IaaS, porque habria que operar el sistema operativo sin tiempo para ello; SaaS como nucleo, porque no quedaria arquitectura que disenar. Aclare aqui —y no en la decision— que identidad y correo siguen siendo SaaS satelite.
6. Consecuencias: escriba UN eje (operacion) con su + y su -, y deje los otros dos al grupo. Diga: «un ADR de una pagina que se entiende vale mas que 5 paginas que nadie lee».

Narra los clics en voz alta. Si falla la red, proyecta la [Slide 8], que ya trae el resultado de la demo, y recórrela rótulo por rótulo.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 10]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 12]
Di: «Queda avanzado: Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: relea su ficha y su C4 Context de la Clase 1. No cambie de dominio: las preguntas 5 a 7 se califican sobre el mismo sistema, y el ADR que redacte hoy se reutiliza en el informe del PI y en la sustentacion de la Clase 15.
2. Paso 2: construya en la pregunta 5 la matriz «Criterio | IaaS | PaaS | SaaS» con las cuatro filas en orden (control, costo cualitativo, operacion, time-to-demo) y maximo 2 lineas por celda; verifique que cada celda nombre una capacidad o una restriccion de SU dominio, y que la fila de operacion no afirme que en PaaS o SaaS usted deja de responder por su propia aplicacion.
3. Paso 3: redacte en la pregunta 6 el ADR-001 con las cinco secciones rotuladas —titulo, estado con fecha, contexto con sus restricciones reales, la decision en UNA sola frase con UN modelo dominante, y exactamente 2 alternativas descartadas con el motivo atado a su dominio—; verifique que la seccion de decision no nombre dos modelos, porque en ese caso vale cero.
4. Paso 4: escriba en la pregunta 7 la seccion 6 del mismo ADR, las consecuencias en los tres ejes (operacion, costo y aprendizaje), con al menos una positiva y una negativa por eje marcadas con + y -, y verifique que al menos una negativa hable de amarre al proveedor o de perdida de control; guarde y continue, que la actividad se entrega completa al cierre del corte.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Elegir el modelo de servicio por moda y no por trade-off. Pida la frase «aceptamos perder X para ganar Y» escrita en el ADR.
- ADR sin alternativas descartadas: un ADR con una sola opcion no documenta una decision, documenta un hecho.
- Nombrar productos de marca en vez del modelo conceptual; el modelo aplica a cualquier proveedor.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Quien administra el sistema operativo en IaaS, en PaaS y en SaaS?
1. Que perdieron y que ganaron con el modelo que eligieron?
1. Por que un ADR necesita las alternativas que descartaron?

## Solución del taller (privada)
`Kit docente/Clase 2/Solucion Taller Clase 2 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 2/Quiz Clase 2 - Modelos de servicio IaaS PaaS SaaS.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 2/Quiz Clase 2 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase02.png | receta: 1) Abre Google Docs · draw.io (opcional) y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 2/Capturas/demo-clase02.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase02.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 2/Capturas/evidencia-clase02.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
