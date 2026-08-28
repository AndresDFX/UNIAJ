# Solucion — Actividad del Corte 2, preguntas 1 a 3 (amenazas STRIDE, controles y politica de secretos)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las tres primeras preguntas del Corte 2, resueltas sobre **BiblioLite** y sobre los diagramas que ya existen del Corte 1. La clave de estas tres es que **no se puede responder sin abrir el C4 Container de la Clase 4**: la pregunta 2 exige senalar caja o flecha, y quien no tenga diagrama solo puede escribir intenciones. Si algun estudiante no entrego el diagrama, ese es el problema a resolver antes del taller, no durante.

> Estas 3 preguntas valen **25 de los 100 puntos** de la actividad del Corte 2, que es una sola actividad de 12 preguntas para las Clases 6, 7, 8 y 10. La pregunta 2 depende de la 1: si las amenazas de la 1 son genericas, la 2 no tiene nada donde aterrizar. Conviene calificar las dos seguidas y de la misma sentada.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 6 - Seguridad en la nube/`
- Configuracion en la plataforma: `Kit docente/Clase 6/Taller en ExamLab - Clase 6 (configuracion).md`
- Hito del PI: Modelo de amenazas mínimo + controles para CloudLite
- Entregable: Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI
- **Estas preguntas: 25.0 puntos** en 3 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 1 | Cinco amenazas STRIDE-lite de BiblioLite | `abierta` | 8.75 |
| 2 | El control de cada amenaza y donde se ve en el diagrama | `abierta` | 8.75 |
| 3 | Politica de secretos del repositorio y de la CI | `abierta` | 7.5 |

---

## Pregunta 1 · Cinco amenazas STRIDE-lite de BiblioLite · 8.75 pts

### Respuesta esperada

| # | Categoria | Amenaza (actor o dato + camino) |
|---|---|---|
| 1 | **S** — Suplantacion | Un estudiante puede reservar un ejemplar **en nombre de otro** porque `POST /titulos/{isbn}/reservas` toma el `id_estudiante` del cuerpo de la peticion en vez de tomarlo del token que valido el proveedor de identidad. Basta con cambiar un numero en el JSON. |
| 2 | **E** — Elevacion de privilegio | Cualquier estudiante autenticado puede llamar `POST /prestamos`, que es la operacion de mostrador del **auxiliar de biblioteca**, porque la API verifica que el token sea valido pero **no verifica el rol**. Un estudiante podria registrarse a si mismo un prestamo sin pasar por el mostrador. |
| 3 | **I** — Fuga de informacion | Un estudiante consulta `GET /prestamos/17`, `/18`, `/19` con identificadores consecutivos y lee **que libros pidio prestados otro companero**, porque el endpoint valida que haya sesion pero no que el prestamo le pertenezca. El historial de lectura es dato personal. |
| 4 | **I** — Fuga de informacion (secretos) | La cadena de conexion de PostgreSQL y la clave del correo transaccional quedaron dentro de la imagen `bibliolite-api:0.1.0` por un `COPY . .` que arrastro el `.env`. Cualquiera que descargue la imagen del registro las lee con `docker history`, incluso si una capa posterior borro el archivo. |
| 5 | **R** — Repudiacion | El auxiliar puede **modificar la fecha de devolucion** de un prestamo vencido con un `UPDATE` directo y despues negar haberlo hecho, porque la tabla `prestamos` guarda solo el estado actual y no existe ninguna bitacora de quien cambio que y cuando. |

**Por que estas cinco y no una lista de manual.** Las cinco nombran una ruta concreta (`POST /titulos/{isbn}/reservas`, `GET /prestamos/17`), un actor de la ficha (estudiante, auxiliar de biblioteca) o un dato del dominio (historial de prestamos, cadena de conexion), y el camino por el que la amenaza ocurre. Esa es la diferencia que el enunciado exige: «fuga de informacion» es una categoria; la fila 3 es una amenaza.

**Dos amenazas comparten la letra I y eso esta bien.** La 3 y la 4 son ambas fuga, pero una ocurre en tiempo de ejecucion por una autorizacion incompleta y la otra en tiempo de construccion por un archivo que no debia entrar en la imagen. Los controles son distintos y los momentos son distintos, asi que no son la misma amenaza con otras palabras. STRIDE es una guia de categorias, no una cuota de una por letra.

**Una sexta que quedo fuera, para tenerla en el bolsillo:** **D** — un script sin autenticacion golpea `GET /titulos?disponible=true` mil veces por minuto en semana de parciales y la base se queda sin conexiones libres. No entro en las cinco porque el impacto academico es menor que los otros, pero si un estudiante la elige, es perfectamente valida y conecta con el escalado de la Clase 13.

### Como calificar

- 1.75 pts por amenaza bien formada, hasta 5. Una amenaza suma completo **solo si nombra el actor o el dato concreto del dominio y el camino por el que ocurre**. Los tres elementos: quien, sobre que, y como.
- Una amenaza generica vale **la mitad**: «podrian hackear la base de datos», «hay riesgo de fuga de informacion», «un atacante puede entrar». La prueba rapida es preguntarse si esa frase se podria copiar sin cambiar una letra al proyecto de otro estudiante. Si se puede, es de manual.
- Se descuenta si **dos amenazas son la misma con otras palabras**: «no hay autenticacion» y «cualquiera puede entrar a la API» son una sola. Dos amenazas de la misma letra de STRIDE **si** se aceptan cuando el camino y el control son distintos.
- No se exige una amenaza por cada letra, y no se premia cubrir las seis. Cinco amenazas reales de tres letras valen mas que seis frases vacias que completan el acronimo.
- Que la amenaza pueda ubicarse en el diagrama del Corte 1 es senal de que esta bien formada. Si al leerla no se sabe sobre que caja cae, la pregunta 2 va a fallar tambien: dígalo en la retroalimentacion de esta.

### Errores frecuentes y que hacer

- Pegar la lista de las cuatro amenazas de ejemplo del enunciado. Estan puestas como referencia de **forma**, no como respuesta, y el enunciado lo dice. Anunciarlo al abrir el taller ahorra la mitad de las correcciones.
- Listar controles en vez de amenazas: «falta HTTPS», «no hay validacion». Eso es la pregunta 2. La amenaza describe **que puede pasar y quien lo hace**; el control describe como se evita.
- Amenazas de un sistema que no es el suyo: pagos, tarjetas, transferencias. Casi siempre viene de un ejemplo de internet. Devuelvala con la pregunta «¿su dominio cobra algo?».
- Confundir repudiacion con negacion de servicio por la letra. Repudiacion es «puedo negar que lo hice» y se combate con bitacora; DoS es «te dejo sin servicio». Es la confusion mas comun de STRIDE.
- Cinco amenazas que caen todas sobre la base de datos. Si ninguna toca el front, la API, el proveedor de identidad ni la imagen del contenedor, es que no se recorrio el diagrama pieza por pieza.
- Escribir la amenaza en futuro condicional infinito («podria eventualmente llegar a pasar que alguien...»). Pida presente y concreto: «un estudiante cambia el numero y lee el prestamo de otro».

---

## Pregunta 2 · El control de cada amenaza y donde se ve en el diagrama · 8.75 pts

### Respuesta esperada

| Amenaza | Control | Donde se ve (caja o flecha) |
|---|---|---|
| 1. Reservar en nombre de otro | El `id_estudiante` se ignora si viene en el cuerpo: se toma del `sub` del token verificado contra el `idp`. Verificable con una prueba que manda un id ajeno y espera `403`. | **Flecha** `API de prestamos -> Proveedor de identidad institucional` (validacion del token) y **caja** `API de prestamos` (la regla que ignora el cuerpo). |
| 2. Estudiante ejecutando la operacion del auxiliar | Autorizacion por rol en el propio endpoint: `POST /prestamos` exige el rol `auxiliar` presente en el token. Verificable con dos tokens de prueba, uno de cada rol. | **Caja** `API de prestamos`, en el modulo `prestamos`. No es del front: un control en la `Aplicacion web` solo esconde el boton. |
| 3. Leer el prestamo de otro por identificador | La consulta filtra siempre por el dueno: `WHERE id = $1 AND id_estudiante = $2`, con el segundo parametro tomado del token. Verificable pidiendo un id ajeno y esperando `404`. | **Caja** `API de prestamos` y **flecha** `API de prestamos -> Base de datos de prestamos`, que es donde el filtro se aplica de verdad. |
| 4. Secretos dentro de la imagen | `.dockerignore` con `.env` y `.env.*`, secretos inyectados como variables de entorno al ejecutar, y una verificacion en la CI que falla si `docker history` menciona `.env`. Verificable: el pipeline se pone rojo. | **Caja** `API de prestamos` (su imagen) y la frontera de construccion: el pipeline de la Clase 8, que es donde el control se ejecuta solo. |
| 5. Cambiar la fecha y negarlo | Tabla `auditoria` con `quien`, `que`, `antes`, `despues` y `cuando`, escrita en la misma transaccion del cambio, y sin permiso de `UPDATE` ni `DELETE` sobre ella para el usuario de la aplicacion. Verificable: se cambia una fecha y aparece la fila. | **Caja** `Base de datos de prestamos` (la tabla y sus permisos) y **flecha** `API de prestamos -> Base de datos de prestamos`. |

**Principio de menor privilegio, aplicado a un componente concreto**

Lo aplico sobre la **conexion de la `API de prestamos` a la `Base de datos de prestamos`**. La API no se conecta como superusuario: usa el rol `bibliolite_api`, al que le concedo exactamente `SELECT`, `INSERT` y `UPDATE` sobre `titulos`, `ejemplares`, `reservas` y `prestamos`, mas `INSERT` — solo `INSERT` — sobre `auditoria`.

**Que deja de poder hacer al aplicarlo:** ese rol **no puede** borrar filas (`DELETE`), no puede alterar la estructura (`DROP`, `ALTER`), no puede leer ningun otro esquema de la misma instancia, y **no puede modificar ni borrar la bitacora de auditoria** que el mismo escribe. Eso ultimo es lo importante: si manana aparece una inyeccion de SQL en la API — la amenaza que Bases de Datos II trabaja con parametros —, el atacante hereda estos permisos y **no** los del dueno de la base. Puede hacer dano, pero no puede borrar la evidencia de haberlo hecho ni tumbar el esquema.

**Nota sobre la segunda columna.** Tres de los cinco controles caen en la caja `API de prestamos`. No es un defecto: es la consecuencia de que casi toda la autorizacion vive donde estan las reglas de negocio. Lo que si seria defecto es que un control cayera en la `Aplicacion web`: ocultar un boton no es un control, porque la peticion se puede enviar sin pasar por la interfaz.

### Como calificar

- 1 pt por cada control **concreto y verificable**, hasta 5. La prueba de «verificable» es poder decir en una frase que se hace para comprobar que el control esta puesto. «Usar buenas practicas», «mejorar la seguridad» o «validar los datos» **no suman nada**.
- 2.5 pts por senalar correctamente la **caja o la flecha** de cada control, prorrateado: 0.5 pts por fila. Se acepta «caja X» o «flecha X -> Y» siempre que el nombre exista en el C4 Container de la Clase 4 o en el diagrama de despliegue de la Clase 7.
- 1.25 pts el **principio de menor privilegio aplicado a un componente concreto, diciendo que deja de poder hacer**. Las dos mitades pesan igual: definirlo sin aplicarlo vale 0.6, y aplicarlo sin decir que se pierde tambien.
- Un control ubicado en la caja equivocada se corrige y se descuenta solo esa fila. El caso tipico es poner en la `Aplicacion web` un control de autorizacion: comente por que no sirve (la peticion se puede enviar sin el front) en vez de solo tachar.
- Que varios controles caigan en la misma caja **no se penaliza**. La API concentra la autorizacion y eso es normal. Lo que se revisa es que la caja senalada sea la correcta, no que esten repartidos.
- Si un control no se puede ubicar en ninguna caja ni flecha del diagrama, el enunciado da la lectura correcta: probablemente falta una pieza en el diagrama. Escribalo asi en la retroalimentacion — es un hallazgo util para el checkpoint de la Clase 11, no solo un descuento.

### Errores frecuentes y que hacer

- «Usar HTTPS» como control de todo. HTTPS protege el dato en transito y no resuelve ninguna de las cinco amenazas de arriba: ni la suplantacion, ni el rol, ni el IDOR, ni el secreto en la imagen, ni el repudio. Es el control comodin y hay que cortarlo.
- Dejar la tercera columna en blanco o poner «en todo el sistema». Es la mitad de la nota y el enunciado explica por que: un control que no se puede senalar en un artefacto todavia es una intencion.
- Definir menor privilegio con la definicion del libro y no aplicarlo. Pida las dos frases: sobre que componente, y que deja de poder hacer.
- Controles de front para amenazas de API: «deshabilito el boton», «oculto el campo». La correccion en clase es una linea de `curl` que manda la peticion sin abrir el navegador.
- Confundir autenticacion con autorizacion. La amenaza 2 no se resuelve pidiendo login: el estudiante **ya** tiene login. Se resuelve verificando el rol. Es la distincion que mas se falla en esta pregunta.
- Un control por amenaza pero sin correspondencia con las amenazas de la pregunta 1 — cinco controles para cinco amenazas distintas de las que listo. Califique la coherencia entre las dos preguntas; se ve en treinta segundos poniendolas al lado.

---

## Pregunta 3 · Politica de secretos del repositorio y de la CI · 7.5 pts

### Respuesta esperada

**1. Donde viven los secretos**
- En la **configuracion del repositorio**: los `secrets` del proyecto en GitHub, que se inyectan como variables de entorno solo durante la ejecucion del pipeline y que no se pueden volver a leer desde la interfaz una vez guardados.
- En **las variables de entorno del proveedor de PaaS** para el servicio en ejecucion, que es coherente con el ADR-001 de la Clase 2.
- En **local**, en un archivo `.env` que esta en `.gitignore` y en `.dockerignore`. Lo que si se versiona es `.env.example`, con los nombres de las variables y **sin un solo valor real**, para que otra persona sepa que necesita sin recibir nada.

Los tres secretos de BiblioLite son: `DATABASE_URL`, `CORREO_API_KEY` y el secreto de cliente del proveedor de identidad.

**2. Quien los rota** El **dueno del repositorio**, que en este proyecto soy yo y es la unica persona con permiso de administracion. Queda escrito en el `README` para que no dependa de la memoria: si manana el proyecto pasa a dos personas, el responsable sigue siendo un rol, no un nombre.

**3. Con que frecuencia**
- Rotacion programada: **al cierre de cada corte**, es decir cada cinco semanas, y en la entrega final antes de la sustentacion de la Clase 15.
- Rotacion inmediata, sin esperar el calendario: si el secreto aparece en un log, en una captura de pantalla, en un `docker history`, en el chat del grupo, o si alguien con acceso deja el proyecto.

**4. Que esta explicitamente prohibido**
- Escribir un secreto en el `Dockerfile`, en el `README`, en el YAML del pipeline en claro o en cualquier archivo que entre a git.
- Hacer `COPY . .` sin `.dockerignore`, que es la via por la que el `.env` entra a la imagen sin que nadie lo escriba a proposito.
- Imprimir variables de entorno en el pipeline (`env`, `printenv`, `echo $DATABASE_URL`): el log de la CI es publico en un repositorio publico.
- Pegar secretos en capturas de pantalla, en la bitacora del laboratorio o en el chat del grupo.
- Commits «temporales» con la clave «que borro despues». No existe el despues: el commit ya esta en el historial.

**5. Que hago si un secreto se filtra**
1. **Rotar la credencial**, primero y ya: generar una nueva en el proveedor e invalidar la anterior. El historial ya salio del equipo y no se puede recuperar; lo unico que esta bajo mi control es que la clave filtrada deje de servir.
2. Actualizar el secreto en la configuracion del repositorio y en el PaaS, y volver a despuegar.
3. Revisar los registros de acceso del proveedor por el periodo en que la clave estuvo expuesta, para saber si alguien la uso.
4. **Solo despues**, limpiar el historial de git — y sabiendo que es cosmetico: si el repositorio es publico, cualquier clon o cualquier indexador ya tiene la copia.

Borrar el commit primero es el orden equivocado: da la sensacion de haber resuelto el problema mientras la credencial sigue siendo valida.

### Como calificar

- 1.5 pts cada una de las cuatro preguntas respondida **de forma concreta**: donde viven, quien rota, cada cuanto, que se prohibe. Son 6 pts en total y se califican una por una.
- **Cero en la primera pregunta si la respuesta admite guardar secretos en el repositorio en claro**, en cualquier forma: en el YAML, en un archivo de configuracion versionado, «comentado» o «solo mientras desarrollo».
- 1.5 pts el procedimiento ante filtracion **empezando por rotar la credencial y no por borrar el commit**. Si el primer paso es limpiar el historial, este criterio es cero aunque el resto de los pasos esten bien: el orden ES la respuesta.
- «Quien los rota» exige un **responsable**, no un mecanismo. «Se rotan automaticamente» no responde la pregunta: alguien tiene que ser el responsable de que ocurra, incluso si la ejecucion es automatica.
- «Con que frecuencia» exige un **numero o un evento del calendario**. «De vez en cuando» o «periodicamente» no suman. Se acepta atarla a los cortes del curso, que es lo mas realista para un proyecto de doce semanas.
- Mencionar el `.env.example` versionado sin valores reales no es obligatorio, pero es la senal de que el estudiante entendio la diferencia entre **el nombre** de un secreto (publico) y **su valor** (privado). Vale un comentario positivo.

### Errores frecuentes y que hacer

- «Los guardo en un archivo de configuracion que no subo». Suena bien hasta que se pregunta que impide subirlo. La respuesta completa nombra el `.gitignore` **y** el `.dockerignore`: sin el segundo, el secreto no entra a git pero si a la imagen.
- Creer que borrar el commit resuelve la filtracion. Es el error central que la pregunta esta diseñada para detectar. La frase para el tablero: «el historial ya salio del equipo; lo unico que usted controla es que la clave deje de servir».
- Poner el secreto en el `Dockerfile` «porque es privado el repositorio». El secreto queda en el historial de capas de la imagen, que viaja al registro y se lee con `docker history` aunque el repo sea privado. Son dos cosas distintas.
- Imprimir el secreto en el pipeline para «verificar que llego». Es la forma mas comun de filtrar una clave en un repositorio publico, y se hace con buena intencion. La alternativa es verificar la **longitud** del valor, no el valor.
- Confundir secreto con variable de configuracion. La URL publica de la API no es un secreto; la cadena de conexion si. Si la politica trata todo como secreto, en la practica no se aplica ninguna.
- Politica escrita en tercera persona y sin responsable («deberian rotarse»). Una politica sin dueno no se ejecuta. Pida el nombre del rol.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Cuantas amenazas por cada letra de STRIDE?**

Ninguna cuota. Se piden cinco amenazas reales, no seis casillas llenas. Dos amenazas de la misma letra son validas si el camino y el control son distintos, y es lo que suele pasar con la fuga de informacion.

**¿La amenaza tiene que ser posible en mi codigo actual?**

No necesariamente: se modela sobre el diseño, y a estas alturas casi nadie tiene el sistema completo. Lo que si tiene que ser es posible **en su arquitectura**, es decir, apoyada en una caja o una flecha que usted dibujo.

**¿Que hago si un control no lo puedo ubicar en ninguna caja?**

Es informacion, no un problema: significa que al diagrama le falta una pieza o una frontera. Escribalo asi en la respuesta y anotelo para el checkpoint de la Clase 11. Vale mas que inventar una ubicacion.

**¿HTTPS no cuenta como control?**

Cuenta, pero solo para la amenaza que de verdad mitiga: dato personal viajando en claro. Lo que no vale es usarlo como respuesta para las cinco filas. Cada amenaza tiene su control propio.

**¿Menor privilegio va sobre la base de datos obligatoriamente?**

No. Puede ir sobre el token del correo transaccional que solo puede enviar y no leer la bandeja, o sobre el usuario del pipeline. Lo obligatorio es que sea un componente concreto y que diga **que deja de poder hacer**.

**¿Donde pongo los secretos si todavia no tengo pipeline?**

En los `secrets` del repositorio igual: se configuran hoy y el pipeline de la Clase 8 los consume sin cambiar nada. Lo que no se hace nunca es dejarlos en un archivo «mientras tanto».

**¿Tengo que rotar los secretos de verdad durante el semestre?**

Al menos una vez, al cierre de un corte, y quedar la evidencia de que se hizo. Es la unica forma de descubrir que el sistema tenia la clave escrita en dos sitios que nadie recordaba.

**Se me filtro una clave en un commit, ¿reprueba la actividad?**

No. Lo que se califica es el procedimiento: si rota primero y documenta, la respuesta esta completa. Este es exactamente el incidente que la pregunta entrena, y es mejor que ocurra en un proyecto de clase.

---

## Cierre de la clase

Lo que se llevan de hoy es que la seguridad se escribe sobre un diagrama, no sobre una lista de buenas intenciones: cinco amenazas con nombre propio, cinco controles ubicados en una caja o en una flecha, y una politica de secretos con responsable y frecuencia. Deje dicho el enlace hacia adelante: el control 4 se vuelve automatico en el pipeline de la Clase 8, la tabla de amenazas se revisa en el checkpoint de la Clase 11 contra el diagrama actualizado, y en la sustentacion de la Clase 15 la pregunta de seguridad es literalmente «¿donde se ve ese control en su diagrama?».

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. Gratis + navegador; sin cuentas cloud de pago ni tarjeta.
