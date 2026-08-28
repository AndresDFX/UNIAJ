# Solucion — Actividad del Corte 2, preguntas 7 a 10 (pipeline de CI, condicion de fallo, frontera CI/CD y senales)

> **DOCUMENTO DOCENTE — PRIVADO.** No publicar en `Clases/` ni en ExamLab antes del cierre de la entrega.

**Resumen:** Las cuatro preguntas de la Clase 8 sobre **BiblioLite**, con el pipeline escrito completo y ejecutable. Las tres primeras son **la misma pregunta con tres profundidades**: el YAML (7), que hace de verdad (8) y hasta donde llega (9); y las tres se derrumban si el pipeline no puede fallar nunca. La pregunta 7 tiene **cero automatico si aparece un secreto en claro**, y es la unica penalizacion total de la actividad.

> Estas 4 preguntas valen **25 de los 100 puntos** de la actividad del Corte 2 (Clases 6, 7, 8 y 10). Se califican en orden y comparandolas: un `ci.yml` correcto con una explicacion en la 8 que no corresponde a ese archivo es la senal mas clara de que el YAML se copio de internet.

## Alineacion con el taller

- Taller del estudiante: `Clases/Clase 8 - Monitoreo optimizacion y CI-CD/`
- Configuracion en la plataforma: `Kit docente/Clase 8/Taller en ExamLab - Clase 8 (configuracion).md`
- Hito del PI: Workflow Actions (build/test/simulate) + métricas de monitoreo del PI
- Entregable: .github/workflows/ci.yml + sección Monitoreo/CI del informe
- **Estas preguntas: 25.0 puntos** en 4 preguntas.

| # | Pregunta | Tipo | Puntos |
|---|---|---|---|
| 7 | El workflow de integracion continua de BiblioLite | `abierta` | 10.0 |
| 8 | Que hace realmente el paso de construccion y prueba | `abierta` | 5.0 |
| 9 | Hasta donde llega el pipeline: CI, CD y lo realista aqui | `abierta` | 4.0 |
| 10 | Metricas y registros de BiblioLite en produccion | `abierta` | 6.0 |

---

## Pregunta 7 · El workflow de integracion continua de BiblioLite · 10.0 pts

### Respuesta esperada

```yaml
name: CI BiblioLite API

# 1. DISPARADORES
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:        # para poder correrlo a mano el dia de la sustentacion

jobs:
  construir-probar:
    # 2. ENTORNO DE EJECUCION
    runs-on: ubuntu-latest

    steps:
      - name: Traer el codigo
        uses: actions/checkout@v4

      - name: Preparar Node 20
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      # 3a. CONSTRUCCION
      - name: Instalar dependencias exactas
        run: npm ci

      - name: Construir la imagen del servicio
        run: docker build -t bibliolite-api:0.1.0 .

      # 3b. PRUEBA
      - name: Pruebas de las reglas de prestamo
        run: npm test

      - name: Verificar que la imagen no lleva secretos
        run: |
          if docker history --no-trunc bibliolite-api:0.1.0 | grep -q '[.]env'; then
            echo "La imagen menciona .env: se detiene el pipeline"
            exit 1
          fi

      - name: Levantar el contenedor y verificar el endpoint de salud
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          CORREO_API_KEY: ${{ secrets.CORREO_API_KEY }}
        run: |
          docker run -d --name api -p 8080:3000 \
            -e DATABASE_URL="$DATABASE_URL" \
            -e CORREO_API_KEY="$CORREO_API_KEY" \
            bibliolite-api:0.1.0
          for i in $(seq 1 15); do
            if curl -fsS http://localhost:8080/health | grep -q '"estado":"ok"'; then
              echo "Endpoint de salud OK"
              exit 0
            fi
            sleep 2
          done
          echo "El endpoint /health no respondio 200 con estado ok"
          docker logs api
          exit 1

      # 3c. DESPLIEGUE SIMULADO
      - name: Despliegue SIMULADO (no despliega a ningun servidor real)
        run: |
          echo "Imagen bibliolite-api:0.1.0 construida verificada y lista para desplegar."
          echo "En este curso el despliegue se SIMULA: no se abren cuentas de nube de pago."
```

**Coherencia con el Corte 1.** La imagen es `bibliolite-api:0.1.0` y el puerto del contenedor es el **3000**, exactamente los del Dockerfile de la Clase 3 y del diagrama de despliegue de la Clase 7. El `-p 8080:3000` publica el 3000 del contenedor en el 8080 del ejecutor, que es donde el `curl` entra.

**Secretos.** Los dos que el servicio necesita se referencian con `${{ secrets.NOMBRE }}` desde la configuracion del repositorio, se pasan al paso como variables de entorno y de ahi al contenedor con `-e`. **Ninguno aparece escrito en el YAML**, y el paso «Verificar que la imagen no lleva secretos» convierte en automatica la politica que la pregunta 3 dejo escrita: si manana alguien hace un `COPY . .`, el pipeline se pone rojo antes de que la imagen salga del equipo.

**Por que el despliegue dice SIMULADO en el nombre.** Porque no despliega. Rotularlo asi no resta: evita prometer lo que el pipeline no hace, que es exactamente lo que la pregunta 9 pregunta despues.

### Como calificar

- 2 pts los **disparadores declarados**. Se espera al menos `push` a la rama principal; `pull_request` y `workflow_dispatch` son deseables y no obligatorios. Un `on:` vacio o ausente es cero en este criterio.
- 1.5 pts el **entorno de ejecucion** (`runs-on`). Basta con `ubuntu-latest`; no se exige justificarlo.
- 4 pts los **tres pasos presentes y en orden**: construccion, prueba, despliegue simulado. Aproximadamente 1.3 pts cada uno. Si el orden esta invertido (prueba antes de construir) se descuenta 1 pt: es una senal de que el YAML no se ejecuto nunca.
- 1.5 pts que el **despliegue este rotulado como simulado** y no prometa un despliegue real. El rotulo va en el nombre del paso, no solo en un comentario.
- 1 pt **coherencia con el Dockerfile del Corte 1**: misma imagen, mismo puerto. Se verifica abriendo la pregunta 8 del Corte 1 al lado.
- **CERO EN TODA LA PREGUNTA si aparece un secreto escrito en claro en el YAML.** Es la unica penalizacion total del corte y hay que anunciarla al abrir el taller. Un valor de ejemplo evidente (`DATABASE_URL: postgres://usuario:CAMBIAR@...`) no cuenta como secreto en claro, pero comentelo: es una costumbre que termina en filtracion.
- Que el pipeline incluya una verificacion automatica de la politica de secretos de la pregunta 3 no es obligatorio y merece comentario positivo: es el paso de una politica escrita a una politica que se cumple sola.

### Errores frecuentes y que hacer

- Escribir la cadena de conexion o la clave del correo en el YAML «para probar». Cero en la pregunta, 10 puntos. Y el log de la CI es publico si el repositorio lo es: ademas de perder la nota, hay que rotar la clave.
- Un `ci.yml` con tres pasos que solo hacen `echo`. Formalmente cumple la estructura y se derrumba en la pregunta 8, donde la condicion de fallo es cero. Califique las dos juntas para que la nota sea coherente.
- Copiar un workflow de internet con acciones que no aplican: despliegues a proveedores de nube, publicacion en registros de paquetes, matrices de cinco versiones de Node. Se detecta porque menciona pasos que el proyecto no tiene.
- Imagen o puerto distintos de los del Corte 1, casi siempre `8080:8080` copiado del ejemplo de la diapositiva. Cuesta el punto de coherencia y hace que el paso del `curl` no pueda funcionar.
- `npm install` en vez de `npm ci` en el pipeline. Aqui si vale corregirlo con firmeza: en CI el objetivo es reproducir, y `ci` es el que respeta el `package-lock.json`.
- Olvidar el `actions/checkout`. El pipeline arranca sin codigo y falla en el primer paso con un error que no dice nada. Es el olvido mas comun de quien escribe el YAML de memoria.
- Un paso llamado `deploy` sin la palabra simulado. Cuesta 1.5 pts aqui y medio criterio en la pregunta 9, donde afirmar haber construido CD descuenta la mitad.

---

## Pregunta 8 · Que hace realmente el paso de construccion y prueba · 5.0 pts

### Respuesta esperada

**1. Que se instala y se construye** `npm ci` instala las dependencias **exactas** del `package-lock.json` — no las compatibles, las exactas — en el ejecutor limpio de GitHub. Despues `docker build` construye la imagen `bibliolite-api:0.1.0` con el mismo Dockerfile del Corte 1, asi que el pipeline valida tambien que el Dockerfile siga siendo valido, no solo que el codigo compile. No hay compilacion en el sentido estricto porque es JavaScript, y conviene decirlo asi en vez de inventar un paso de compilacion que no existe.

**2. Que se ejecuta en la prueba y que comprueba exactamente** Tres cosas, en orden de menos a mas costoso:

- `npm test` corre las pruebas de las reglas de prestamo. La que importa: **no se puede reservar el ultimo ejemplar disponible si ya tiene una reserva vigente**. Es la regla que justifica que BiblioLite exista, asi que es la que se prueba.
- La verificacion de que `docker history` **no menciona `.env`**: comprueba la politica de secretos de la pregunta 3 sobre la imagen que se acaba de construir.
- El contenedor se levanta de verdad y se consulta `GET /health` esperando `200` con `"estado":"ok"`: comprueba que la imagen **arranca**, que el proceso escucha en el 3000 y que el contrato de salud de la Clase 3 se sigue cumpliendo.

**3. Con que condicion el pipeline DEBE fallar** Cuatro condiciones, y todas se pueden provocar a proposito:

| Si introduzco... | el pipeline lo detecta en... |
|---|---|
| una regla que permite reservar un ejemplar ya reservado | `npm test`, la prueba falla |
| un `COPY . .` que arrastra el `.env` | la verificacion de `docker history` |
| un puerto distinto en el `EXPOSE` o en el `CMD` | el `curl` a `/health`, que agota los 30 s |
| una dependencia que no esta en el `package-lock.json` | `npm ci`, que se niega a instalarla |

**La prueba de que no es decoracion verde:** si cambio la comparacion de la regla de reserva de `>=` a `>`, el `npm test` se pone rojo y el pipeline se detiene antes del despliegue simulado. Ese es el error concreto que introduciria para demostrar que el pipeline sirve, y es el que conviene provocar una vez a proposito para ver el check rojo con los propios ojos.

### Salida esperada

```
== RUN VERDE - el pipeline de arriba cuando pasa ==

CI BiblioLite API  #7  [OK] construir-probar (ubuntu-latest)        1m 48s
  [OK] Traer el codigo                                                 3s
  [OK] Preparar Node 20                                                7s
  [OK] Instalar dependencias exactas       npm ci                     22s
  [OK] Construir la imagen del servicio    docker build ... 0.1.0     41s
  [OK] Pruebas de las reglas de prestamo   npm test                    6s
         3 passing  (reserva del ultimo ejemplar ya reservado: rechazada con 409)
  [OK] Verificar que la imagen no lleva secretos                       4s
  [OK] Levantar el contenedor y verificar el endpoint de salud        14s
         Endpoint de salud OK
  [OK] Despliegue SIMULADO (no despliega a ningun servidor real)       2s
         Imagen bibliolite-api:0.1.0 construida verificada y lista para desplegar.

== RUN ROJO - el mismo pipeline con la regla de reserva rota (>= cambiado por >) ==

CI BiblioLite API  #8  [FALLA] construir-probar (ubuntu-latest)        52s
  [OK]    Traer el codigo / Preparar Node 20 / Instalar dependencias exactas
  [OK]    Construir la imagen del servicio
  [FALLA] Pruebas de las reglas de prestamo   npm test                  5s
            1 failing - reserva del ultimo ejemplar ya reservado:
                        se esperaba 409 y devolvio 201
            Error: Process completed with exit code 1
  [-]     Verificar que la imagen no lleva secretos                omitido
  [-]     Levantar el contenedor y verificar el endpoint de salud  omitido
  [-]     Despliegue SIMULADO                                     omitido
```

Los segundos varian con el ejecutor y no significan nada: lo que se compara son **los nombres de los pasos, su orden y donde se detiene**. Si el estudiante describe un run que no se parece a ninguno de los dos, la diferencia esta en su `ci.yml` y ahi es donde hay que mirar. Los tres `omitido` del run rojo son el argumento entero de la pregunta: **el pipeline no publica un artefacto que no paso las pruebas.** Un run que se pone verde con la regla rota es la decoracion verde que este criterio califica con cero.

### Como calificar

- 1.5 pts **que se compila o instala**, dicho sobre su propio archivo. Si el proyecto es JavaScript y no hay compilacion, decirlo explicitamente es la respuesta correcta y suma completo: inventar un paso de compilacion es peor.
- 1.5 pts **que se ejecuta en la prueba y que comprueba**. Las dos mitades: el comando **y** la afirmacion que verifica. «Corre `npm test`» sin decir que comprueba vale la mitad.
- 2 pts la **condicion de fallo expresada como algo que el pipeline detectaria**. La forma que vale es «si introduzco X, falla en Y». Basta una condicion bien formada; dos o mas es lo esperado en una buena respuesta.
- **CERO en la condicion de fallo si el pipeline no puede fallar nunca**: solo `echo`, o pruebas que siempre pasan, o un `|| true` al final de cada paso. Es el criterio central de la pregunta y no admite matices.
- Un `continue-on-error: true` o un `|| true` escondido en el YAML de la pregunta 7 anula esta pregunta aunque la prosa diga lo contrario. Vale la pena buscarlo: es la forma sofisticada de la decoracion verde.
- Que el estudiante nombre **el error concreto que introduciria** para ver el check rojo es la mejor version de esta respuesta. Si lo hizo de verdad y lo cuenta, comentelo: es la diferencia entre entender el CI y describirlo.

### Errores frecuentes y que hacer

- «El pipeline falla si hay un error». Circular y vacio. La correccion es una pregunta: «¿que error, exactamente, y en que paso lo veria?».
- Explicar un `ci.yml` que no es el suyo. Se detecta comparando: la prosa menciona pruebas de integracion y el YAML solo tiene un `echo`. Cuando pasa, califique sobre el YAML entregado y comentelo sin acusar.
- Confundir «no hay compilacion» con «no hay construccion». La construccion existe: es el `npm ci` y el `docker build`. Lo que no existe en JavaScript es un paso de compilacion a binario.
- Pruebas que solo verifican que el archivo existe o que la funcion devuelve algo. No comprueban ninguna regla del dominio y por eso no pueden fallar por un error de negocio. Pida una prueba sobre la regla que justifica el sistema.
- Poner `|| true` o `continue-on-error` para que el pipeline «se vea verde». Es exactamente lo contrario del objetivo: un check que nunca falla no informa nada y da una falsa seguridad que en un proyecto real es peor que no tener CI.
- Decir que el pipeline fallaria si el servidor de produccion esta caido. No hay servidor de produccion: el despliegue se simula. Confundir eso indica que la pregunta 9 tambien va a fallar.

---

## Pregunta 9 · Hasta donde llega el pipeline: CI, CD y lo realista aqui · 4.0 pts

### Respuesta esperada

**1. Que valida la integracion continua (CI) y cuando actua** La CI valida que **el codigo de todos integrado sigue funcionando**, y actua en el momento en que el codigo entra al repositorio compartido: en cada `push` a `main` y en cada solicitud de cambios. Su pregunta es «¿esto rompe algo?», y su respuesta es un check verde o rojo en minutos, no en la semana de la entrega.

**2. Que hace la entrega o el despliegue continuo (CD) y en que se diferencia** La CD toma el artefacto que la CI verifico y lo **lleva a un entorno**. La sigla es ambigua a proposito y conviene separar las dos lecturas:

- **Entrega continua**: el artefacto queda siempre listo para desplegar y el despliegue lo dispara una persona con un boton.
- **Despliegue continuo**: no hay boton; todo lo que pasa la CI llega automaticamente al entorno.

La diferencia con la CI es el objeto: **la CI valida, la CD entrega**. Una responde si el codigo esta sano; la otra lo pone donde los usuarios lo alcanzan.

**3. Cual construi yo y hasta que punto exacto llega** Construi **integracion continua**, no CD. Mi `ci.yml` llega hasta **«listo para desplegar»**: instala dependencias exactas, construye la imagen `bibliolite-api:0.1.0`, corre las pruebas de la regla de prestamo, verifica que la imagen no lleva secretos y comprueba que el contenedor arranca y responde `200` en `/health`. El ultimo paso se llama «Despliegue SIMULADO» y lo unico que hace es imprimir que la imagen quedo verificada. **No hay ningun servidor recibiendo esa imagen**, y el nombre del paso lo dice para no prometerlo.

**4. Que me faltaria para CD de verdad, y por que el curso no lo pide** Me faltarian cuatro cosas concretas: un **entorno destino** con su URL, un **registro de imagenes** donde publicar `bibliolite-api:0.1.0`, **credenciales de despliegue** guardadas como secretos del repositorio, y una **estrategia de reversion** para volver a la version anterior cuando el despliegue salga mal —porque va a salir mal alguna vez—. Ademas, una verificacion posterior al despliegue contra el `/health` del entorno real, no del contenedor local.

El curso no lo pide porque las cuatro exigen una **cuenta de nube de pago con tarjeta de credito**, y la politica del curso —la misma que sostiene el ADR-001— es que todo se hace con herramientas gratuitas o en el navegador. La consecuencia pedagogica es honesta: se aprende a construir el pipeline y a saber donde termina, que es mas util que tener un `deploy` que nadie puede verificar.

### Como calificar

- 1 pt la definicion de CI **atada a cuando actua**. «Integrar el codigo» sin el momento vale la mitad: el «cuando» (al entrar el codigo al repositorio) es lo que la distingue de cualquier otra cosa.
- 1 pt la de CD **y su diferencia**. Distinguir entrega de despliegue continuo no es obligatorio, pero es la respuesta que demuestra que el estudiante entendio por que la sigla es ambigua.
- 1 pt **ubicar correctamente su propio trabajo**, reconociendo que llega hasta «listo para desplegar». Se espera que nombre el punto exacto donde se detiene, no solo la etiqueta.
- 1 pt **lo que faltaria para CD real y por que el curso no lo exige**. Las dos mitades: la lista de lo que falta (entorno, registro, credenciales, reversion) y el motivo (no se abren cuentas de pago).
- **Se descuenta la mitad del total si afirma haber construido CD.** No es una trampa: el enunciado avisa que decirlo suma en vez de restar, y aun asi cada semestre alguien escribe «ya tengo CD porque tengo un paso deploy».
- Reconocer que el despliegue es simulado **no resta nada** y hay que decirlo en la retroalimentacion, porque el estudiante suele creer que admitirlo lo perjudica. Saber donde termina lo que construyo es precisamente lo que se califica.

### Errores frecuentes y que hacer

- «Ya tengo CD porque el YAML tiene un paso deploy». Cuesta la mitad de la pregunta. La frase para el tablero: el nombre del paso no despliega nada; lo que despliega es que haya un servidor al otro lado.
- Definir CI como «usar GitHub Actions». La herramienta no es la practica: se puede tener Actions y no tener integracion continua, y se puede tener integracion continua con otra herramienta.
- Usar CI y CD como si fueran una sola palabra («el cicd»). La pregunta existe porque la frontera importa; si el estudiante no la puede trazar, tampoco puede decir hasta donde llega su trabajo.
- Decir que falta «configurar el servidor» sin nombrar nada mas. Se espera una lista de piezas concretas: entorno, registro de imagenes, credenciales, reversion.
- Justificar la ausencia de CD por falta de tiempo o de conocimiento. El motivo real y suficiente es la politica del curso: no se abren cuentas de nube de pago. Es mejor argumento y ademas es verdad.
- Prometer en la sustentacion de la Clase 15 un despliegue automatico que no existe. Es la afirmacion que un evaluador tumba en dos preguntas, y aqui se esta entrenando justo lo contrario.

---

## Pregunta 10 · Metricas y registros de BiblioLite en produccion · 6.0 pts

### Respuesta esperada

| Senal | Que se mide en BiblioLite | Umbral u objetivo |
|---|---|---|
| **Latencia** | Tiempo de respuesta de `GET /titulos?disponible=true`, la consulta de disponibilidad, que es la operacion mas usada del sistema. | p95 **menor a 400 ms**. Si el p95 pasa de **800 ms** durante 5 minutos, se revisa el plan de la consulta antes de agregar capacidad. |
| **Trafico** | Reservas creadas por hora: respuestas `2xx` de `POST /titulos/{isbn}/reservas`. | Base esperada **20/hora**, pico de **150/hora** en semana de parciales. Por encima de **300/hora** se revisa capacidad, porque es el doble del pico previsto. |
| **Errores** | Proporcion de respuestas `5xx` sobre el total de peticiones. Aparte y como error **de negocio**: proporcion de `409` sobre las reservas intentadas. | `5xx` **por debajo de 0.5%** en ventanas de 5 minutos. Los `409` no son fallas, pero si pasan del **5%** de los intentos hay que revisar la interfaz: significa que muestra disponibilidad vencida. |
| **Saturacion** | Conexiones activas del pool de PostgreSQL sobre el maximo configurado (20). Es el recurso que se agota primero, antes que la CPU o la memoria. | Alerta al **80%** (16 conexiones sostenidas 2 minutos). Al 100% las peticiones no fallan: se encolan, y el sintoma aparece como latencia. |
| **Registro** (no numerico) | Bitacora de auditoria: una fila por cambio de estado de un prestamo con `quien`, `id_ejemplar`, `antes`, `despues` y `cuando`. Es el control de la amenaza 5 de la pregunta 1. | Objetivo: **100%** de los cambios de fecha de devolucion con fila, verificado por muestreo mensual. Retencion **1 ano**. |
| **Registro** (no numerico) | Log de fallos de envio del `Correo transaccional SaaS`, con el motivo que devolvio el proveedor y el `id_prestamo` afectado. | Objetivo **0 fallos en 24 h**. Con **mas de 3 en un dia** se revisa la cuota del plan gratuito y las direcciones invalidas. |

**Por que estas seis y en este orden.** Las cuatro primeras son las senales doradas aterrizadas: cada una responde una pregunta distinta que las otras no pueden responder. La latencia dice si duele, el trafico dice si es por volumen, los errores dicen si se rompe, y la saturacion dice **que recurso** se agota. Sin la cuarta, un pico de latencia no tiene explicacion; con ella, la explicacion suele ser el pool.

**Las dos que son registro y no metrica.** Un numero dice **que** algo paso; un registro permite reconstruir **por que**. La bitacora de auditoria existe para poder responder «¿quien movio esa fecha?» tres semanas despues, y el log de fallos de correo para poder decirle a un estudiante por que no recibio el aviso. Ninguna de las dos se puede graficar como una linea, y las dos son las que salvan una revision.

**Nota sobre los umbrales.** Los numeros de la tercera columna son discutibles y estan puestos para poder discutirlos: 400 ms sale del umbral de percepcion de «instantaneo» que la Clase 12 trabaja, 20 conexiones es el maximo por defecto de PostgreSQL, y el pico de 150 reservas/hora sale de la aritmetica de servilleta —unos 900 estudiantes activos, cada uno con una reserva cada dos semanas, concentradas en la semana de parciales—. Lo que no es discutible es que la columna exista: sin umbral no se puede decidir cuando actuar, y una senal que no lleva a una decision no se mira nunca.

### Como calificar

- 1 pt por senal bien formada **con su umbral**, hasta 4 senales. Las senales 5 y 6 suman hasta **1 pt adicional entre las dos**: no se premia listar mas, se premia que las adicionales aporten algo distinto.
- 1 pt que **al menos una sea un registro y no una metrica numerica**: algo que se escribe para poder reconstruir que paso despues. Una metrica disfrazada de registro («cantidad de errores en el log») no cuenta: sigue siendo un numero.
- **Una senal sin umbral no suma, aunque este bien elegida.** Es la regla mas mecanica de la pregunta y la que mas se pierde: «medimos la latencia» es cero en esa fila.
- Se descuenta si las senales **no se refieren a operaciones del dominio propio**. «Latencia de la API» es generico; «latencia de la consulta de disponibilidad, que es la mas usada» esta aterrizado. La segunda columna es la que se revisa para decidirlo.
- Un umbral que sea claramente irreal (latencia menor a 1 ms, cero errores siempre) se corrige pero **no se anula**: el criterio pide que el umbral exista y sea discutible. Comente el numero y de el suyo como referencia.
- Distinguir el error de plataforma (`5xx`) del error de negocio esperado (`409`) no es obligatorio y es la mejor senal de madurez de esta pregunta: significa que el estudiante no va a alertar por algo que funciona como debe.

### Errores frecuentes y que hacer

- Metricas sin umbral. Es el error numero uno y el enunciado lo dice con todas sus letras. Anunciar antes del taller: «una fila sin tercera columna vale cero, aunque la senal sea perfecta».
- Copiar las cuatro senales doradas con su definicion de manual y sin aterrizarlas: «latencia: cuanto tarda una peticion». ¿Cual peticion? La segunda columna pide la operacion concreta del dominio.
- Medir el uso de CPU como saturacion sin haber pensado que recurso se agota primero. En un servicio como BiblioLite casi nunca es la CPU: son las conexiones a la base. Vale preguntarlo en voz alta durante el taller.
- Poner como registro «los logs de la aplicacion». Demasiado vago. Se pide que diga que se escribe en cada linea y para responder que pregunta futura.
- Alertar por los `409`. Son el comportamiento correcto del sistema cuando dos personas reservan a la vez; alertar por ellos entrena al equipo a ignorar las alertas. Lo que se vigila es su **proporcion**, no su existencia.
- Seis metricas que son variantes de la misma («tiempo de respuesta», «velocidad», «demora»). El limite de 6 no es una meta: cuatro senales distintas valen mas que seis parecidas.

---

## Lo que van a preguntar (respuestas listas)

Estas son las dudas que aparecen todos los semestres. Tenerlas resueltas por escrito es lo que evita responder la misma cosa quince veces durante el taller.

**¿El pipeline tiene que correr de verdad en GitHub?**

Si, y es gratis: el nivel gratuito da 2000 minutos al mes en repositorios privados e ilimitado en publicos. No se pide tarjeta en ningun momento. Un `ci.yml` que nunca se ejecuto se nota en la pregunta 8.

**¿Que pongo si no tengo pruebas escritas?**

Escriba una, la de la regla que justifica su sistema. Con una prueba real que puede fallar, la pregunta 8 suma completo; con tres `echo` no suma nada. Media hora de trabajo vale 5 puntos.

**¿Puedo poner el secreto en el YAML si el repositorio es privado?**

No. Cero en la pregunta 7, y por una razon de fondo: el log de la CI, los forks y cualquier colaborador futuro lo ven. La sintaxis de secrets del repositorio es exactamente igual de facil de escribir.

**¿Por que el despliegue tiene que decir «simulado»?**

Porque no despliega. Rotularlo no resta: suma en la pregunta 9, donde se califica que sepa donde termina lo que construyo. Afirmar tener CD descuenta la mitad de esa pregunta.

**¿Cuantas metricas exactamente, cuatro o seis?**

Cuatro bien formadas ya suman los 4 pts principales; la quinta y la sexta suman 1 pt entre las dos y solo si aportan algo distinto. Es mejor entregar cuatro aterrizadas que seis genericas.

**¿Un registro cuenta como metrica?**

No, y por eso hay 1 pt aparte: al menos una senal debe ser un registro. La diferencia es la pregunta que responde: la metrica dice que paso, el registro permite reconstruir por que.

**¿De donde saco los umbrales si no tengo usuarios?**

De la aritmetica de servilleta y de los umbrales de percepcion, que es lo que la Clase 12 formaliza. El umbral puede ser discutible; lo que no puede es faltar.

**¿Y si mi pipeline falla y no lo puedo arreglar antes de la entrega?**

Entregue el `ci.yml` y explique en la pregunta 8 en que paso falla y por que. Un pipeline rojo con diagnostico correcto vale mas que uno verde que no valida nada, y es lo que la rubrica premia.

---

## Cierre de la clase

Hoy la politica de secretos de la Clase 6 dejo de ser un documento y se volvio un paso que se pone rojo solo, y el contrato de salud de la Clase 3 dejo de ser una promesa y se volvio una verificacion automatica. Deje dicho el enlace hacia adelante: los minutos de CI son un **driver de costo** de la tabla de la Clase 10, el cache del pipeline es una de las **acciones de sostenibilidad** de esa misma clase, los umbrales de latencia de hoy son los que la Clase 12 va a medir con percentiles, y las senales de saturacion son las que la Clase 13 usa para decidir la metrica de autoescalado. Y provoque una vez el check rojo delante del grupo: es el minuto que convierte el CI de decoracion en herramienta.

---

## Politica de entrega

La entrega que se califica es la respuesta dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento en Word o Google Docs es opcional y solo sirve para que el estudiante conserve sus respuestas. Gratis + navegador; sin cuentas cloud de pago ni tarjeta.
