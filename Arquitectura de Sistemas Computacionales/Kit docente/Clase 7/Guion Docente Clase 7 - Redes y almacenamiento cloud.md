# Guion docente — Clase 7: Redes y almacenamiento cloud

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: Clase regular (teoría + taller PI) · encuentro síncrono
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
- Modelar red lógica (cliente, edge, app, datos) sin VPC de pago.
- Elegir tipo de almacenamiento según el caso de uso CloudLite.
- Completar el diagrama de despliegue del PI.

## Hoy avanzamos el PI en…
**Diagrama de despliegue: red, zonas, almacenamiento**

**Entregable concreto:** Diagrama Deployment (draw.io) + elección de storage (objeto/bloque/relacional conceptual)

**Herramienta:** draw.io

## Fundamento teórico para el docente
### El tercer angulo: que responde el diagrama de despliegue - diapositiva 4
El diagrama de despliegue responde una pregunta que los anteriores no responden: donde corre cada pieza y por que camino de red se hablan entre si. Conviene tener claro el mapa de los tres diagramas del curso, porque el estudiante cree que dibuja lo mismo tres veces. En la Clase 1 se hizo C4 Context: el sistema como una caja, quien lo usa y con que sistemas externos habla; responde QUIEN. En la Clase 4 se hizo C4 Containers: que aplicaciones, servicios y bases de datos lo componen por dentro y con que contratos se comunican; responde QUE. Hoy se hace el despliegue: en que nodos se ejecutan esos contenedores, en que zona de red esta cada nodo, por que puerto y protocolo pasa cada flecha, y donde quedan los datos; responde DONDE. Un nodo es cualquier lugar de ejecucion: una maquina virtual, un host de contenedores, un servicio gestionado. Es el mismo sistema desde un tercer angulo, no un sistema nuevo, y por eso los nombres deben coincidir con los de la Clase 4.
### IP, puerto y protocolo: las tres etiquetas de cada flecha - diapositiva 5
Para etiquetar ese diagrama hacen falta tres conceptos de red que el docente debe definir en una frase. Una direccion IP identifica una maquina dentro de una red. Un puerto es un numero entre 1 y 65535 que identifica a que proceso de esa maquina se entrega el trafico: la direccion lleva el paquete al edificio, el puerto lo lleva a la oficina. Un protocolo es el idioma de esa conexion: HTTP o HTTPS para la API, el protocolo propio del motor para la base de datos. Hay puertos fijados por convencion registrada, no por ley fisica: 80 para HTTP, 443 para HTTPS, 5432 para PostgreSQL, 3306 para MySQL, 8080 para desarrollo. Nada impide correr una base de datos en el 9999, pero cambiar la convencion confunde a quien opera. Esto conecta con la Clase 3: cuando en Killercoda se ejecuta un contenedor publicando un puerto, esa linea es la decision de que superficie queda expuesta, tema de la Clase 6.
### Subred publica y privada: lo definen las rutas, no el nombre - diapositiva 5
Una subred es una subdivision de una red, y lo que la hace publica o privada no es su nombre sino sus rutas. Una subred publica tiene camino de entrada desde internet: alguien de afuera puede iniciar una conexion hacia lo que vive ahi. Una privada no lo tiene; solo se alcanza desde dentro, aunque normalmente si puede salir para descargar actualizaciones. Sobre esa distincion se construye la regla que se evalua hoy: en la zona publica va unicamente el punto de entrada, el balanceador o proxy inverso; la aplicacion va en la zona privada; los datos van en una tercera zona que solo acepta conexiones desde la aplicacion. Llega la primera pregunta previsible: «si la base de datos es privada, como se conecta la API?». Privado significa inalcanzable desde internet, no inalcanzable en absoluto: la API esta en la misma red y llega por el nombre interno y el puerto del motor; quien no puede llegar es el usuario final ni un atacante externo. Si un desarrollador necesita entrar, se hace por un unico host intermedio controlado, llamado bastion.
### DNS y balanceador de carga - diapositiva 5
Dos piezas mas hay que explicar sin titubear. El DNS es el directorio distribuido que traduce un nombre legible, como cloudlite.example, en la direccion IP donde atiende el servicio; el registro tipo A apunta un nombre a una IP y el CNAME apunta un nombre a otro nombre. Cada registro tiene un TTL, los segundos que los demas guardan la respuesta en cache; tipicamente de 300 a 3600, asi que un cambio de direccion no es instantaneo para todos. El balanceador de carga recibe todas las peticiones y las reparte entre varias instancias iguales del mismo servicio, con algoritmos como round robin o menor numero de conexiones activas. Su funcion menos obvia y mas importante es el chequeo de salud: consulta un endpoint como /health, por convencion cada 10 a 30 segundos, y si falla dos o tres veces seguidas retira esa instancia de la rotacion hasta que responda. Es tambien donde termina el TLS, es decir donde se descifra HTTPS.
### Primer ejemplo: una peticion de CloudLite de punta a punta - diapositiva 8
Primer ejemplo concreto, y la mejor forma de dictar la clase: seguir una peticion de CloudLite de punta a punta. Un usuario final abre cloudlite.example en su telefono; el DNS resuelve el nombre a la IP publica del balanceador; el navegador abre una conexion HTTPS al puerto 443 de ese balanceador, que vive en la zona publica; el balanceador elige una de las dos instancias del contenedor de la API, en la zona privada, y le reenvia la peticion por HTTP al puerto 8080; la API consulta el motor de base de datos en la zona de datos por el puerto 5432 y devuelve JSON por el mismo camino. Ese recorrido dibujado en draw.io, con cada flecha etiquetada con protocolo y puerto y cada caja dentro de su zona, ES el entregable. Sirve para citar numeros: una consulta simple bien indexada responde entre 1 y 20 milisegundos, y el objetivo que se formalizara en la Clase 12 suele fijarse por convencion en menos de 300 milisegundos para el 95 por ciento de las peticiones. Con eso el grupo ve que si una pantalla dispara veinte consultas encadenadas el problema es de diseno.
### Los cuatro tipos de almacenamiento y como se decide - diapositiva 6
El almacenamiento se decide por tipo de dato, y hay cuatro categorias que el docente debe distinguir. El de bloque es un disco crudo que el sistema operativo formatea y monta; se conecta a una sola instancia a la vez, es lo que hay debajo del volumen de un contenedor, y se mide en gigabytes y en IOPS, operaciones de lectura y escritura por segundo. El de archivos es un sistema de archivos compartido que varias instancias montan por red. El de objetos no tiene carpetas reales: es un espacio plano de contenedores llamados buckets donde cada objeto se guarda bajo una clave, se lee y escribe por HTTP y se reemplaza completo en vez de editarse por partes; es practicamente ilimitado, barato y accesible por URL. Y el de la base de datos guarda registros estructurados con consultas y transacciones. El numero que ordena la decision es el precio relativo: un gigabyte al mes en objetos cuesta del orden de dos a tres centavos de dolar, en disco de bloque cerca de cuatro veces mas, y en base de datos gestionada aun mas porque se paga computo. Son referencias de mercado, no reglas fijas, y aqui no se aprovisiona nada de pago: el valor esta en justificar la eleccion.
### Segundo ejemplo: la foto de perfil y el error de diseno que conviene provocar - diapositiva 6
Segundo ejemplo concreto, y el error de diseno que conviene provocar: CloudLite permite subir una foto de perfil o adjuntar un PDF. La solucion ingenua es guardar el archivo en una columna binaria de la base de datos. Hay que dejar que el estudiante la proponga y luego cuantificarla: dos megabytes por usuario y cinco mil usuarios son diez gigabytes de binarios dentro de una base cuyos datos utiles podrian ser doscientos megabytes; cada respaldo arrastra esos diez gigabytes y la cache del motor se llena de bytes que ninguna consulta filtra. El diseno correcto separa: el archivo va a almacenamiento de objetos y la base guarda una fila con la clave del objeto, el dueno, el tamano, el tipo de contenido y la fecha. Eso es el almacenamiento primario mas secundario que pide el entregable. Hay una razon adicional: un contenedor es efimero, lo que se escriba en su sistema de archivos desaparece cuando se reemplaza, y con dos instancias detras del balanceador el archivo subido a una no existe en la otra. Mantener los contenedores sin estado es la condicion del escalado horizontal de la Clase 13.
### Trazabilidad: los nombres deben coincidir con la Clase 4 - diapositiva 7
Queda la trazabilidad, donde mas puntos se pierden: los nombres de las cajas del despliegue deben ser los mismos que los contenedores del C4 Containers de la Clase 4. Si alli el servicio se llamaba api-citas, hoy no puede aparecer como backend, ni puede aparecer una caja nueva que nadie declaro. Segunda pregunta previsible: «esto no esta mal por no ser una VPC real de un proveedor?». Lo que se evalua es el razonamiento sobre zonas, puertos y ubicacion de los datos, no la sintaxis de una marca; el curso usa herramientas gratis en navegador y no pide cuenta de pago ni tarjeta, y por eso las slides indican zonas Publica, Privada y Datos. La Clase 6 identifico amenazas y fronteras de confianza en texto y hoy esas fronteras se vuelven zonas dibujadas; la Clase 8 tomara cada flecha para definir que se mide en ella, porque no se puede monitorear un camino que no esta dibujado; la Clase 10 costeara estas mismas cajas, asi que la eleccion de almacenamiento es tambien decision de costo; y la Clase 13 discutira cual caja se replica y cual no. Todo el bloque se evalua en el Parcial 2 de la Clase 9.
### Cierre conceptual y error tipico del docente (de la diapositiva 5 a la diapositiva 7)
Error tipico del docente que no domina el tema: dejar pasar el dibujo de la nube como una caja difusa con flechas sin etiqueta, donde no se distingue zona publica de privada, no hay puertos y no se sabe donde viven los datos. La consecuencia aguas abajo es acumulativa: sin zonas, los controles de red de la Clase 6 no tienen donde mostrarse; sin flechas etiquetadas, la Clase 8 no tiene sobre que definir latencia ni saturacion; y en la sustentacion de la Clase 15 el estudiante describe su sistema con gestos en vez de senalar componentes. El segundo tropiezo es permitir que el despliegue introduzca nombres y servicios que no existian en el C4 Containers, o dejar la eleccion de almacenamiento sin justificar («usamos base de datos porque es lo normal»). Cuando eso ocurre, el informe describe dos sistemas distintos que se contradicen entre secciones y se pierde la trazabilidad, que es el criterio con el que se calificara el paquete integrado de la Clase 11.

## Referencias a diapositivas
Numeración real del deck `Clases/Clase 7 - Redes y almacenamiento cloud/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

1. Portada · Clase 7 · Redes y almacenamiento cloud
2. Agenda de hoy (120 min)
3. Objetivos de la clase
4. PI CloudLite — entregable de hoy
5. Red lógica para el diagrama
6. Almacenamiento
7. Checklist del diagrama Deployment
8. Ejemplo de diagrama de despliegue (Deployment)
9. Herramientas de hoy
10. Del boceto a ExamLab (diagrama)
11. Taller PI (paso a paso)
12. Para continuar (PI)
13. Clase 7 · PI en movimiento

## Plan de clase minuto a minuto (120 min)

### 0–10 · Encuadre PI · [Slide 2][Slide 3][Slide 4]
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **Diagrama de despliegue: red, zonas, almacenamiento**.
Entregable concreto: Diagrama Deployment (draw.io) + elección de storage (objeto/bloque/relacional conceptual).
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «¿En qué quedó tu CloudLite la clase pasada?» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde [Slide 5]
Cubre estos conceptos, en este orden, ~10 min cada uno (son los títulos de las diapositivas de teoría):
- Red lógica para el diagrama
- Almacenamiento
- Checklist del diagrama Deployment

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un estudiante voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · [Slide 10]
Herramienta del día: **draw.io**.
**Demo que usted debe poder repetir:** Dibujar zonas de confianza sobre el diagrama de despliegue

1. En draw.io dibuje dos rectangulos grandes rotulados «Subred publica» y «Subred privada».
2. Ponga el balanceador en la publica y la base de datos en la privada; dibuje la flecha API -> BD cruzando de una a otra.
3. Pregunte: «si un atacante llega desde internet, con que se topa primero?» — eso es superficie de exposicion.
4. Verifique en voz alta que los nombres de los servicios son LOS MISMOS del C4 Containers de la Clase 4.

Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase 7/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»

**Cierra la demo dentro de ExamLab** [Slide 10] — es el paso que el estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, pegalo en la pregunta de diagrama y muestralo renderizado.

**Del boceto al codigo Mermaid.** No subas una imagen: la respuesta de esta pregunta es texto Mermaid.

- **1. Disena visual** Dibuja el diagrama como quieras en Excalidraw o draw.io: es mas rapido arrastrar cajas que escribir codigo, y ahi es donde piensas el modelo.
- **2. Traduce con IA** Copia o describe tu boceto a una IA y pidele el codigo Mermaid: «convierte este diagrama a Mermaid usando `flowchart`». Revisa el resultado: la IA acierta la sintaxis, no tu modelo.
- **3. Pega y renderiza en ExamLab** Pega ese codigo en la caja de texto de la pregunta y mira como lo dibuja la plataforma. Si no renderiza, corrige ahi mismo: lo que se califica es el diagrama renderizado dentro de ExamLab.
- **4. Guarda el PNG para tu PI** Exporta tambien la imagen a la carpeta de tu Proyecto Integrador. Esa copia es para tu informe; no reemplaza la respuesta en la plataforma.


### 55–100 · Taller guiado PI (individual · equipos de 2–3 solo si tú los autorizaste) · [Slide 11]
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase 7/Quiz Clase 7 - Redes y almacenamiento cloud.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 estudiantes en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · [Slide 13]
Di: «Queda avanzado: Diagrama de despliegue: red, zonas, almacenamiento.
Criterio de éxito: el estudiante explica su artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»


## Actividad / taller (detalle)
1. Paso 1: dibuje primero el boceto del despliegue en Excalidraw o draw.io con las tres zonas (publica, privada y de datos), y despues pidale a una IA que lo traduzca a Mermaid; peguelo en la pregunta 4 y verifique en el diagrama ya renderizado que la base de datos NO quede en la zona publica.
2. Paso 2: etiquete en ese mismo diagrama el puerto de cada componente y marque las fronteras de confianza, es decir donde termina lo que usted controla; verifique que no aparezcan nombres de subredes ni de servicios de un proveedor concreto.
3. Paso 3: justifique en la pregunta 5 el tipo de almacenamiento de cada componente diciendo que caracteristica del dato lo exige; si su dominio no necesita almacenamiento de objetos, declarelo y justifiquelo en vez de agregarlo.
4. Paso 4: complete en la pregunta 6 la tabla de correspondencia entre el C4 Containers y el Despliegue, con una fila por componente y su zona, y liste los renombres que aplico; si no hubo ninguno, digalo explicitamente.

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, pregunta a cualquier integrante).

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
- Dibujar «la nube» como una caja difusa. Exija las dos zonas, publica y privada, explicitas.
- Poner la base de datos en la subred publica «para que sea mas facil probar». Es exactamente lo que la Clase 6 acaba de prohibir.
- Renombrar servicios respecto al C4 Containers, con lo que los dos diagramas dejan de ser el mismo sistema.

## Preguntas de comprobación oral (no son del quiz)
Úsalas en el tramo 100–115, a personas distintas y al azar.
1. Que va en la subred publica y que en la privada, y por que?
1. Que hace un balanceador de carga en una frase?
1. Cuando conviene object storage y cuando la base de datos?

## Solución del taller (privada)
`Kit docente/Clase 7/Solucion Taller Clase 7 - CloudLite.docx` — es la referencia con la que
comparas lo que entregan los estudiantes. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase 7/Quiz Clase 7 - Redes y almacenamiento cloud.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase 7/Quiz Clase 7 - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase07.png | receta: 1) Abre draw.io y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase 7/Capturas/demo-clase07.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase07.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase 7/Capturas/evidencia-clase07.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
