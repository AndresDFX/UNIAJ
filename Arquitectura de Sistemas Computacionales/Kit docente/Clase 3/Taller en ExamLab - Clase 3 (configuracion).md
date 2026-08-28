# Taller de la Clase 3 en ExamLab - configuracion

- **Curso:** Arquitectura de Sistemas Computacionales (FI303380)
- **Taller:** Actividad del Corte 1 (preguntas 8 a 11) - Contenedor del stub de CloudLite
- **Preguntas:** 4 · **Total:** 25 puntos
- **Plataforma:** ExamLab (https://uniaj.examlab.workers.dev/) · modulo Talleres
- **Hito del PI:** Contenerizar un stub del servicio principal de CloudLite
- **Entregable de la clase:** Dockerfile del stub + bitácora de 5 comandos con la salida real + captura del lab

> ExamLab no importa preguntas desde archivo: el alta se hace en la UI del
> docente (o con la pestana de IA). Este documento trae el texto exacto de cada
> campo para copiar y pegar, incluidos el SQL de partida y el codigo base.

**Que produce el estudiante:** Las preguntas 8 a 11 de la actividad del Corte 1. El estudiante elige el servicio a contenedorizar, escribe su Dockerfile, explica capas y cache sobre su propio archivo, documenta el ciclo con el contrato de salud y entrega la bitacora con la evidencia real del contenedor corriendo.

---

## Pregunta 8 - Respuesta escrita · 10.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## El servicio a contenedorizar y su Dockerfile

**Primera parte — la eleccion.** Diga **cual servicio de su C4 Context** va a
contenedorizar: el servicio principal de su dominio, que normalmente es la **API stub** o
el **front estatico**. Justifique la eleccion en 2 o 3 frases: por que ese y no otro, y que
demuestra tener ese servicio corriendo.

**Segunda parte — el Dockerfile.** Escriba el Dockerfile **completo** de ese servicio. Debe
tener, como minimo, estas instrucciones y en un orden que tenga sentido:

- `FROM` con una imagen base **ligera y con etiqueta fija** (por ejemplo `node:20-alpine`,
  `python:3.12-slim`, `nginx:alpine`). Nada de `latest`.
- `WORKDIR`
- `COPY` de las dependencias **antes** que el `COPY` del codigo
- `RUN` de instalacion de dependencias
- `COPY` del codigo
- `EXPOSE` con el puerto
- `CMD` con el proceso principal

**Dos reglas que se califican aparte:**

1. **El puerto de `EXPOSE`, el del `CMD` y el que documenta en la pregunta 10 tienen que ser
   el mismo numero.** Es el error mas comun y el mas facil de evitar.
2. **Prohibido copiar el `.env` o cualquier clave dentro de la imagen.** Si el `COPY` es de
   todo el directorio, se necesita un `.dockerignore`; diga que lleva dentro.

> Un secreto dentro de la imagen queda en el **historial de capas** para siempre: cualquiera
> que tenga la imagen puede leerlo con `docker history` aunque el archivo se borre en una
> capa posterior. Los secretos se inyectan en tiempo de ejecucion, no se construyen dentro.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2 pts la eleccion del servicio con justificacion atada al dominio. 5 pts el Dockerfile completo con las instrucciones minimas y un orden que aproveche el cache (dependencias antes del codigo). 1.5 pts imagen base ligera y con etiqueta fija; se descuenta por usar latest. 1.5 pts coherencia del puerto entre EXPOSE, CMD y lo documentado. Si el Dockerfile copia un .env o una clave, o hace COPY de todo sin .dockerignore ni mencionarlo, se pierden los 5 pts del Dockerfile: es el error que el curso corta el mismo dia.

---

## Pregunta 9 - Respuesta escrita · 4.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Imagen, contenedor y capas, sobre su propio Dockerfile

Explique, **usando el Dockerfile que acaba de escribir**, no la teoria general:

1. **Imagen y contenedor no son lo mismo.** Diga cual es cual en su caso, en una frase. La
   analogia que se espera: la imagen es el molde, el contenedor es la instancia corriendo;
   de una imagen se pueden levantar varios contenedores a la vez.
2. **Que instruccion de SU Dockerfile crea una capa nueva** y por que eso importa. Nombre al
   menos dos instrucciones concretas de su archivo.
3. **Por que puso el `COPY` de dependencias antes que el `COPY` del codigo.** Diga que pasa
   con el cache cuando cambia una linea de codigo, comparado con lo que pasaria en el orden
   inverso.
4. **Una diferencia entre su contenedor y una maquina virtual**, en una frase, en terminos
   de que comparte con la maquina anfitriona.

> Cuidado con dos frases que suenan bien y son falsas: «un contenedor es una VM ligera» (no
> lo es: la VM carga un sistema operativo completo, el contenedor **comparte el kernel** del
> anfitrion) y «la imagen se ejecuta» (se ejecuta el contenedor, que es una instancia de la
> imagen).

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1 pt distinguir imagen de contenedor sin decir que un contenedor es una VM ligera. 1 pt nombrar al menos dos instrucciones de SU propio Dockerfile que crean capa. 1 pt explicar el efecto del orden en el cache, comparando con el orden inverso. 1 pt la diferencia con una VM en terminos de kernel compartido. Una respuesta que explique la teoria sin referirse a su archivo pierde la mitad: la pregunta evalua que entienda lo que escribio.

---

## Pregunta 10 - Respuesta escrita · 5.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Construir, ejecutar y verificar el contenedor

Explique el ciclo completo de su servicio, con los **comandos exactos** que usaria:

1. **Construccion**: el comando de build con el nombre y la etiqueta de su imagen.
2. **Ejecucion**: el comando de run, con el **mapeo de puertos entre el anfitrion y el
   contenedor** explicado. Diga que numero corresponde a cada lado y que pasaria si los
   invierte.
3. **Verificacion**: el **contrato del endpoint de salud** de su stub, con las tres cosas
   que lo definen:
   - la **ruta** (por ejemplo `/health`),
   - el **codigo de estado** esperado,
   - el **cuerpo** de la respuesta, con su formato.

> El endpoint de salud no es un adorno: es la forma en que cualquier orquestador, balanceador
> o pipeline sabra si su servicio esta vivo, y por eso vuelve en la Clase 7 (despliegue) y en
> la Clase 8 (CI). Un endpoint que devuelve 200 con el cuerpo vacio es peor que ninguno,
> porque no distingue «vivo» de «vivo pero roto».

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

1.5 pts el comando de build con nombre y etiqueta. 1.5 pts el comando de run con el mapeo de puertos correctamente explicado: que lado es el anfitrion, que lado el contenedor y que pasa si se invierten. 2 pts el contrato de salud completo con ruta, codigo de estado y cuerpo con su formato; se descuenta si falta cualquiera de los tres. El puerto tiene que ser el mismo de la pregunta 8.

---

## Pregunta 11 - Respuesta escrita · 6.0 pts

**Tipo en la plataforma:** `abierta`

**Enunciado (campo Contenido):**

## Bitacora del laboratorio: la evidencia de que corrio

Ejecute de verdad el ciclo en **Killercoda** (killercoda.com, cuenta gratuita, escenario
Ubuntu) y reporte lo que paso. Si Killercoda no carga, la alterna es **LabEx Docker
Playground**, que en su plan gratuito da solo **3 sesiones al dia**.

Entregue una tabla de **3 columnas** (`Comando | Que esperaba | Que salio realmente`) con
**una fila por comando**, en este orden:

1. el build de su imagen
2. `docker images` filtrado por su imagen
3. el run de su contenedor
4. `docker ps`
5. la peticion a su endpoint de salud

En la columna de la derecha pegue el **fragmento textual** de la salida real: el numero de
capas, el identificador corto del contenedor, el `200` de la respuesta. No la parafrasee.

Debajo de la tabla:

- **Describa la captura** que adjunta. Debe mostrarse al mismo tiempo el prompt del
  laboratorio, la salida de `docker ps` y la hora del sistema.
- **Una fila de incidente**: un comando que le fallo y como lo resolvio. Si nada fallo,
  escriba el que estuvo a punto de fallar y por que no fallo.

> **La sesion del laboratorio caduca a 1 hora.** El Dockerfile se escribe en la carpeta de
> su PI y se **pega** en el laboratorio, nunca al contrario, y la evidencia se captura
> **antes** de cerrar. Perder el trabajo por no haber guardado es el incidente mas comun del
> dia, y no es excusa aceptable para no entregar esta pregunta.

> La entrega oficial es esta respuesta dentro de ExamLab. El documento en Word o Google Docs es opcional y solo sirve para conservar sus respuestas.

**Rubrica esperada (campo Rubrica):**

2.5 pts las cinco filas con la salida real pegada textualmente; una salida parafraseada («salio bien») no suma. 1.5 pts la descripcion de la captura con los tres elementos exigidos (prompt, docker ps y hora del sistema). 1 pt la fila de incidente con el problema y como se resolvio. 1 pt coherencia: el nombre de la imagen, la etiqueta y el puerto son los mismos de las preguntas 8 y 10. Es la pregunta que demuestra que el contenedor existio de verdad y no solo en papel.

---

## Al terminar de crearlo

- Verifique que la suma de puntos sea la esperada: **25**.
- Publique el taller y confirme la fecha limite (domingo 23:59 segun el Acuerdo).
- Las preguntas con SQL o codigo: ejecutelas una vez usted mismo antes de publicar,
  para confirmar que el SQL de partida corre y que el starter compila.
