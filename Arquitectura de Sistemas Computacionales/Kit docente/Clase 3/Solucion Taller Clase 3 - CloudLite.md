# Solucion — Actividad del Corte 1, preguntas 8 a 11 (contenedor del stub de CloudLite)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las cuatro preguntas de la Clase 3, resueltas sobre **BiblioLite** y sobre la decision de PaaS del ADR-001. El servicio contenedorizado es la **API de prestamos**, con imagen `bibliolite-api:0.1.0` y puerto **3000**. Ese numero y ese nombre se repiten en las preguntas 8, 10 y 11: la coherencia entre las tres es criterio de nota, asi que conviene calificarlas juntas y no una por una.

> Estas 4 preguntas valen **25 de los 100 puntos** de la actividad del Corte 1. La pregunta 11 exige haber ejecutado el ciclo **de verdad** en Killercoda: es la unica de todo el corte que no se puede responder de memoria, y es la que hay que anunciar al empezar el taller para que nadie deje el laboratorio para el final.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 3 - Virtualizacion y contenedores/`
- Configuracion en la plataforma: `Kit docente/Clase 3/Taller en ExamLab - Clase 3 (configuracion).md`
- Hito del PI: Contenerizar un stub del servicio principal de CloudLite
- Entregable: Dockerfile (+ compose opcional) + captura/enlace lab navegador
- **Estas preguntas: 25.0 puntos** en 4 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 8 | El servicio a contenedorizar y su Dockerfile | `abierta` | 10.0 |
| 9 | Imagen, contenedor y capas, sobre su propio Dockerfile | `abierta` | 4.0 |
| 10 | Construir, ejecutar y verificar el contenedor | `abierta` | 5.0 |
| 11 | Bitacora del laboratorio: la evidencia de que corrio | `abierta` | 6.0 |

---

## Pregunta 8 · El servicio a contenedorizar y su Dockerfile · 10.0 pts

### Respuesta esperada

**Primera parte — la eleccion**
Contenedorizo la **API de prestamos**, que es la caja `api-prestamos` del C4 Context. Elijo
esa y no el front porque es la que tiene la regla de negocio del dominio: decide si un
ejemplar esta disponible y si una renovacion es valida. Tener esa API corriendo en un
contenedor demuestra que la logica de BiblioLite se ejecuta de forma reproducible en
cualquier maquina, que es lo que el front por si solo no demostraria: un front estatico
corriendo solo prueba que se sirven archivos.

**Segunda parte — el Dockerfile**

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY src ./src
EXPOSE 3000
CMD ["node", "src/server.js"]
```

**Puerto** — `EXPOSE 3000`, el servidor de `src/server.js` escucha en `3000`, y `3000` es el
puerto del contenedor que se documenta en la pregunta 10. Un solo numero en los tres sitios.

**Secretos** — no hay `COPY .` de todo el directorio: se copian `package.json`,
`package-lock.json` y la carpeta `src`, y nada mas. Aun asi existe `.dockerignore` como
segunda barrera, con:

```text
node_modules
.env
.env.*
.git
capturas/
*.md
```

Ni `.env` ni ninguna clave entra en la imagen. La cadena de conexion a la base y la clave del
proveedor de correo se inyectan al ejecutar, con `-e` o con las variables de entorno del
proveedor de PaaS, que es coherente con el ADR-001.

### Como calificar

- 2 pts la eleccion del servicio **con justificacion atada al dominio**: por que ese y que demuestra tenerlo corriendo. «Porque es el principal» no es justificacion; «porque tiene la regla que decide si el ejemplar esta disponible» si.
- 5 pts el Dockerfile completo con las **siete instrucciones minimas** (`FROM`, `WORKDIR`, `COPY` de dependencias, `RUN` de instalacion, `COPY` del codigo, `EXPOSE`, `CMD`) **y** en un orden que aproveche el cache: las dependencias antes del codigo. Si el orden esta invertido se descuenta 1.5 de estos 5 pts, porque es justo lo que la pregunta 9 pide explicar.
- 1.5 pts imagen base **ligera y con etiqueta fija**. Se descuenta completo por `latest`, y la mitad por una imagen completa sin variante ligera (`node:20` en vez de `node:20-alpine`) cuando el servicio no necesita nada que justifique el peso.
- 1.5 pts **coherencia del puerto** entre `EXPOSE`, el proceso del `CMD` y lo documentado en la pregunta 10. Se verifica leyendo las dos preguntas seguidas.
- **Si el Dockerfile copia un `.env` o una clave**, o hace `COPY . .` sin `.dockerignore` ni mencionarlo, **se pierden los 5 pts del Dockerfile**. No es una penalizacion desproporcionada: un secreto queda en el historial de capas para siempre y se lee con `docker history` aunque una capa posterior borre el archivo. Es el error que el curso corta el mismo dia en que aparece.
- Un `CMD` en forma de shell (`CMD node src/server.js`) no se penaliza en esta clase, aunque la forma de lista sea la correcta. Si la respuesta lo usa, valga la nota completa y comente por que la lista es mejor: el proceso recibe las señales de parada directamente.

### Errores frecuentes y que hacer

- `FROM node:latest`. Rompe la reproducibilidad, que es el argumento entero de la clase: la imagen que hoy funciona manana puede traer otra version mayor de Node. Se corrige en diez segundos y hay que exigirlo.
- `COPY . .` antes del `RUN npm ci`. Con eso cada cambio de una linea de codigo invalida la capa de dependencias y el build vuelve a descargar todo. Es el error que la pregunta 9 hace visible, asi que si aparece aqui, revise si en la 9 el estudiante explico lo contrario de lo que escribio.
- `.env` dentro de la imagen, casi siempre por `COPY . .`. Pida el `.dockerignore` en el momento; es la unica correccion del dia que no admite «lo arreglo despues».
- `EXPOSE 3000` con el servidor escuchando en `8080`, o al reves. Es el error mas comun y el mas facil de evitar: el contenedor arranca, `docker ps` lo muestra vivo y la peticion nunca responde.
- Dockerfile de una imagen que no corresponde al servicio elegido: elige el front y escribe un `FROM node` con `npm ci`. Suele ser copiar el ejemplo de la diapositiva sin adaptarlo.
- `RUN npm install` en vez de `npm ci`. No se penaliza, pero vale explicarlo: `ci` respeta el `package-lock.json` y por eso es el que produce la misma imagen dos veces.

---

## Pregunta 9 · Imagen, contenedor y capas, sobre su propio Dockerfile · 4.0 pts

### Respuesta esperada

**1. Imagen y contenedor**
La imagen es `bibliolite-api:0.1.0`, el molde: un paquete inmutable con Alpine, Node 20, mis
dependencias y mi carpeta `src`. El contenedor es la instancia que corre de ese molde; de esa
misma imagen puedo levantar dos contenedores a la vez, uno en el puerto 8080 y otro en el
8081 del anfitrion, y cada uno tiene su propio sistema de archivos escribible y su propio
proceso.

**2. Que instrucciones de mi Dockerfile crean capa**
`RUN npm ci --omit=dev` crea una capa con los `node_modules` instalados, y `COPY src ./src`
crea otra con mi codigo. Tambien crean capa los dos `COPY` y el `FROM` trae las capas de la
imagen base. Importa porque cada capa se cachea por separado y se identifica por su
contenido: si la capa no cambio, el build la reutiliza y no la vuelve a construir.

**3. Por que el `COPY` de dependencias va antes**
Porque cambio `src/server.js` muchas veces al dia y el `package.json` casi nunca. Con este
orden, al cambiar una linea de codigo el build reutiliza la capa del `npm ci` — que es la
lenta, la que descarga paquetes — e invalida solo la capa del codigo: el rebuild tarda
segundos. En el orden inverso, con `COPY . .` antes del `RUN`, cualquier cambio de una linea
invalida la capa que contiene el `package.json` y todas las siguientes, asi que el `npm ci`
se vuelve a ejecutar completo cada vez.

**4. Una diferencia con una maquina virtual**
Mi contenedor **comparte el kernel** del anfitrion: dentro solo esta Alpine como sistema de
archivos y mi proceso de Node, no hay otro sistema operativo arrancando. Una maquina virtual
carga su propio kernel y su propio sistema operativo completo sobre un hipervisor, y por eso
arranca en decenas de segundos y ocupa gigas, mientras mi contenedor arranca en menos de un
segundo.

### Como calificar

- 1 pt distinguir imagen de contenedor **sin decir que un contenedor es una VM ligera** y sin decir que «la imagen se ejecuta». Se espera la idea del molde y la instancia, con el detalle de que de una imagen salen varios contenedores.
- 1 pt nombrar **al menos dos instrucciones de SU propio Dockerfile** que crean capa. Nombrar `RUN` y `COPY` en abstracto vale la mitad: la pregunta pide las de su archivo.
- 1 pt explicar el efecto del orden en el cache **comparando con el orden inverso**. Sin la comparacion no hay explicacion, solo la receta.
- 1 pt la diferencia con una VM **en terminos de kernel compartido**. «Es mas ligero» o «arranca mas rapido» son consecuencias, no la diferencia: valen la mitad si no nombran el kernel.
- Una respuesta que explique la teoria correctamente **sin referirse a su archivo pierde la mitad del total**. La pregunta no evalua si sabe la definicion: evalua si entiende lo que escribio en la pregunta 8.

### Errores frecuentes y que hacer

- «Un contenedor es una maquina virtual ligera». Suena bien y es falso. El enunciado lo advierte y aun asi aparece: es la frase que hay que corregir en voz alta ante todo el grupo.
- «La imagen se ejecuta». Se ejecuta el contenedor. Parece un detalle de lenguaje y no lo es: quien lo dice suele no entender por que puede levantar dos contenedores del mismo molde.
- Explicar el cache al reves: decir que el orden correcto es el codigo primero. Verifique contra el Dockerfile de la pregunta 8; a veces el archivo esta bien y la explicacion mal, y a veces al contrario.
- Enumerar teoria de capas sin abrir su archivo. Es la mitad de la nota. La correccion es literal: «vuelva a responder citando las lineas que usted escribio».
- Confundir capa con contenedor: decir que cada capa es un contenedor. Las capas son de la imagen y son de solo lectura; el contenedor agrega encima una unica capa escribible.

---

## Pregunta 10 · Construir, ejecutar y verificar el contenedor · 5.0 pts

### Respuesta esperada

**1. Construccion**
```bash
docker build -t bibliolite-api:0.1.0 .
```
Nombre `bibliolite-api` y etiqueta `0.1.0`. La etiqueta es una version, no `latest`: asi
puedo tener dos versiones a la vez y saber cual estoy ejecutando.

**2. Ejecucion**
```bash
docker run -d --name bibliolite-api -p 8080:3000 \
  -e DATABASE_URL="postgres://..." bibliolite-api:0.1.0
```
En `-p 8080:3000`, el numero de la **izquierda es el del anfitrion** (la maquina de
Killercoda, donde entro yo con el navegador o con `curl`) y el de la **derecha es el del
contenedor** (donde escucha Node, el mismo del `EXPOSE`). Si los invierto y escribo
`-p 3000:8080`, Docker publica el 3000 del anfitrion hacia el 8080 del contenedor, donde no
hay nada escuchando: el contenedor aparece vivo en `docker ps` y la peticion muere con
`Connection reset by peer` o se queda colgada. El sintoma no dice cual es la causa, y por eso
este es el error que mas tiempo hace perder.

La clave de la base y la del correo entran aqui, con `-e`, en tiempo de ejecucion: no estan
en la imagen.

**3. Verificacion — contrato del endpoint de salud**
- **Ruta**: `GET /health`
- **Codigo de estado**: `200` cuando el servicio esta vivo **y** alcanza la base de datos;
  `503` cuando el proceso responde pero la base no contesta.
- **Cuerpo**: JSON, con esta forma exacta:

```json
{
  "estado": "ok",
  "version": "0.1.0",
  "dependencias": { "bd": "ok" }
}
```

Se verifica con:
```bash
curl -i http://localhost:8080/health
```

El cuerpo lleva las dependencias a proposito: un `200` con el cuerpo vacio no distingue «vivo»
de «vivo pero roto», y es justo lo que la Clase 7 va a consultar desde el balanceador y la
Clase 8 desde el pipeline.

### Como calificar

- 1.5 pts el comando de **build con nombre y etiqueta**. Sin etiqueta, o con `latest`, vale la mitad.
- 1.5 pts el comando de **run con el mapeo de puertos correctamente explicado**: que lado es el anfitrion, que lado el contenedor y **que pasa si se invierten**. La explicacion de la inversion es la mitad de este criterio; sin ella se queda en 0.75.
- 2 pts el **contrato de salud completo**: ruta, codigo de estado y cuerpo con su formato. Se descuenta si falta **cualquiera** de los tres, y los tres pesan igual.
- El **puerto del contenedor tiene que ser el mismo de la pregunta 8**. Si no coincide, se descuenta de los 1.5 pts del run, y ademas revise la pregunta 11: el error se propaga hasta la bitacora.
- Distinguir `200` de `503` segun el estado de las dependencias **no es obligatorio** pero es la respuesta que merece la nota completa del criterio de codigo de estado. Un `200` unico, bien documentado, tambien la merece si el cuerpo dice algo verificable.

### Errores frecuentes y que hacer

- Invertir el mapeo de puertos y no notarlo, porque `docker ps` muestra el contenedor arriba. Enseñe el sintoma: contenedor `Up`, peticion sin respuesta. Es la leccion mas util del dia.
- Endpoint de salud que devuelve `200` con cuerpo vacio. El enunciado dice por que es peor que ninguno: no distingue vivo de roto. Pida al menos un campo verificable.
- `docker build` sin `-t`. La imagen queda sin nombre, la pregunta 11 no puede filtrarla en `docker images` y se pierde el punto de coherencia alla tambien.
- Poner la clave de la base dentro del Dockerfile «para que el run sea mas corto». Es el mismo error de la pregunta 8 disfrazado de comodidad, y cuesta los 5 pts de aquella.
- Describir el contrato de salud en prosa sin decir el formato del cuerpo. Un contrato sin forma no es un contrato: la Clase 8 va a escribir una verificacion automatica contra el.
- Confundir `-p` con `-e`, o usar `--port`. No es conceptual pero se corrige rapido y evita media hora de frustracion en el laboratorio.

---

## Pregunta 11 · Bitacora del laboratorio: la evidencia de que corrio · 6.0 pts

### Respuesta esperada

| Comando | Que esperaba | Que salio realmente |
|---|---|---|
| `docker build -t bibliolite-api:0.1.0 .` | Que construya sin error y que se vean las capas de cada paso. | `=> [4/6] RUN npm ci --omit=dev` ... `Successfully tagged bibliolite-api:0.1.0`. **7 pasos**, el mas lento el `npm ci` con 21.4s. |
| `docker images | grep bibliolite` | Una fila con mi imagen, etiqueta 0.1.0. | `bibliolite-api   0.1.0   9f2c1a4be7d3   58 seconds ago   142MB` |
| `docker run -d --name bibliolite-api -p 8080:3000 bibliolite-api:0.1.0` | Que imprima el identificador largo del contenedor. | `9d41c7e8b2a5f0c3...` (64 caracteres). Sin salida de error. |
| `docker ps` | Una fila, estado Up, puertos 0.0.0.0:8080->3000/tcp. | `9d41c7e8b2a5   bibliolite-api:0.1.0   "node src/server.js"   12 seconds ago   Up 11 seconds   0.0.0.0:8080->3000/tcp   bibliolite-api` |
| `curl -i http://localhost:8080/health` | 200 y el JSON con estado, version y dependencias. | `HTTP/1.1 200 OK` · `content-type: application/json` · `{"estado":"ok","version":"0.1.0","dependencias":{"bd":"ok"}}` |

**Descripcion de la captura**
La captura es una sola imagen de la ventana del escenario Ubuntu de Killercoda en la que se
ven al mismo tiempo las tres cosas exigidas: el **prompt del laboratorio**
(`controlplane $`), la **salida completa de `docker ps`** con la fila del contenedor
`bibliolite-api` y el mapeo `0.0.0.0:8080->3000/tcp`, y la **hora del sistema** que imprimi
con `date` en la linea inmediatamente anterior (`Mon Sep  7 14:22:10 UTC 2026`). No es un
recorte: se ve la terminal completa, para que se pueda verificar que las tres cosas son de la
misma sesion.

**Fila de incidente**
El primer `docker run` fallo con
`docker: Error response from daemon: driver failed programming external connectivity on
endpoint bibliolite-api: Bind for 0.0.0.0:8080 failed: port is already allocated`. Causa: en
un intento anterior habia dejado un contenedor con el mismo puerto publicado, detenido pero
no eliminado. Lo resolvi con `docker rm -f bibliolite-api` y volvi a ejecutar el `run`.
Verifique antes con `docker ps -a`, que es donde aparecen los detenidos y donde no habia
mirado.

### Como calificar

- 2.5 pts las **cinco filas** con la salida real pegada **textualmente**. Una salida parafraseada («salio bien», «funciono correctamente») no suma nada en esa fila. Lo que se busca son marcas que no se pueden inventar sin haber corrido el ciclo: el numero de pasos del build, el identificador corto, el tamano de la imagen, el `Up N seconds`.
- 1.5 pts la descripcion de la captura con los **tres elementos** exigidos: prompt del laboratorio, salida de `docker ps` y hora del sistema. 0.5 pts cada uno.
- 1 pt la fila de incidente con el problema **y** como se resolvio. Si nada fallo, se acepta el que estuvo a punto de fallar y por que no fallo; lo que no se acepta es dejarla vacia.
- 1 pt **coherencia**: nombre de imagen, etiqueta y puerto identicos a los de las preguntas 8 y 10. Este punto se pone comparando las tres respuestas, no leyendo esta sola.
- Si la bitacora esta hecha con LabEx en vez de Killercoda, **no se descuenta**: la alterna esta autorizada en el enunciado. Solo verifique que la captura corresponda al entorno que dice usar.
- **Senal de bitacora inventada**: las cinco filas con salidas redondas y sin ningun incidente, identificadores de contenedor demasiado regulares, tamano de imagen ausente. Cuando aparece, pida la captura y la hora del sistema antes de poner nota.

### Errores frecuentes y que hacer

- Columna derecha parafraseada. Es el error que vacia la pregunta: sin salida textual no hay evidencia de que el contenedor existio. Se avisa al abrir el taller, no al calificar.
- Perder el trabajo porque la sesion caduco a la hora. El enunciado lo advierte: el Dockerfile se escribe en la carpeta del PI y se **pega** en el laboratorio, nunca al contrario, y la evidencia se captura antes de cerrar. No es excusa aceptable para no entregar.
- Captura recortada que solo muestra la salida de `docker ps`, sin prompt ni hora. Se pierde 1 de los 1.5 pts de la captura y no se puede verificar que sea de la sesion propia.
- Fila de incidente en blanco «porque todo funciono». Siempre hay algo: el puerto ocupado, el `npm ci` sin `package-lock.json`, el `curl` a `localhost` desde la pestaña equivocada. Pida el que estuvo cerca.
- Puerto distinto del de las preguntas 8 y 10, casi siempre porque en el laboratorio lo cambio para que funcionara y no volvio a corregir el Dockerfile. Cuesta el punto de coherencia y, si el Dockerfile quedo mal, tambien en la pregunta 8.
- Pegar la salida como imagen dentro de la respuesta abierta. La columna pide texto: una imagen no se puede leer ni comparar con las otras preguntas.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿Hay que instalar Docker en el computador?**

No, y no conviene. El laboratorio es Killercoda en el navegador, con cuenta gratuita y escenario Ubuntu; si no carga, la alterna es LabEx Docker Playground, que da solo 3 sesiones al dia en el plan gratuito. Nadie necesita permisos de administrador en su maquina para esta actividad.

**¿Que hago si la sesion del laboratorio se cierra a la hora?**

Volver a abrir el escenario y pegar de nuevo el Dockerfile, que debe estar guardado en la carpeta del PI. El laboratorio es desechable a proposito: la fuente de verdad es el repositorio, no la sesion.

**¿Puedo contenedorizar el front en vez de la API?**

Si, esta autorizado por el enunciado, pero entonces la justificacion tiene que sostenerlo: que demuestra tener el front corriendo. Con `nginx:alpine`, el `RUN` de instalacion no aplica y hay que decirlo en vez de inventarse uno.

**¿Por que no puedo usar `FROM node:latest`?**

Porque `latest` cambia sin avisar y la imagen que hoy funciona manana puede traer otra version mayor de Node. La reproducibilidad es el argumento entero de la clase: si la etiqueta no fija la version, no hay reproducibilidad.

**¿El `.env` no queda protegido si lo borro en una capa posterior?**

No. Las capas son acumulativas y quedan en el historial: `docker history` y cualquiera que tenga la imagen pueden recuperar el archivo aunque una capa posterior lo borre. Los secretos se inyectan al ejecutar.

**¿La captura tiene que mostrar la hora?**

Si, y es medio punto. La forma mas simple es ejecutar `date` justo antes de `docker ps`, para que la hora quede en la misma pantalla que la evidencia.

**¿Que pongo en la fila de incidente si de verdad no fallo nada?**

El que estuvo a punto de fallar y por que no fallo. Sirve igual: el objetivo es que quede escrito un sintoma con su causa, que es lo que se va a necesitar en la Clase 8 cuando el pipeline falle sin explicacion.

**¿Se puede usar Docker Compose?**

No hace falta y hoy suma ruido: la pregunta pide un servicio, un Dockerfile y un `docker run`. Compose entra cuando haya mas de un contenedor, que es a partir del diagrama de la Clase 4.

---

## Cierre de la clase

Lo que sale de hoy no es «saber Docker»: es una unidad de despliegue con nombre, version y puerto, y un contrato de salud escrito. Esas cuatro cosas son las que la Clase 4 va a dibujar como caja `Container`, las que la Clase 7 va a colocar en el diagrama de despliegue con su puerto real y las que la Clase 8 va a verificar desde el pipeline. Cierre insistiendo en la coherencia del puerto entre las tres preguntas: es el detalle que separa una entrega que se sostiene de una que se cae en la primera revision.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. Gratis + navegador; sin cuentas cloud de pago ni tarjeta.
