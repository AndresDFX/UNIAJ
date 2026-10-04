# -*- coding: utf-8 -*-
"""Material operativo proyectado de Arquitectura: Dockerfile, CLI, Mermaid, YAML.

Por que existe
--------------
Arquitectura proyectaba 7 laminas de codigo sobre 391: el 1%. Y sus entregables son casi
todos artefactos con FORMA: un Dockerfile, un `docker build`, un diagrama C4 en Mermaid, un
workflow de GitHub Actions. El estudiante que no ha visto la forma proyectada la adivina, y
pierde puntos por el formato, no por el criterio.

La regla que gobierna lo que se escribe aqui
--------------------------------------------
CLAUDE.md §0: se ensena el MECANISMO que la actividad evalua, no su respuesta. Cada actividad
de ARQ pide el artefacto **para el dominio que el estudiante eligio**, asi que aqui se
proyecta la forma sobre el ejemplo comun de las laminas —la app de turnos de una barberia,
`cloudlite-api`— y no sobre el dominio de la solucion docente.

Cada lamina es un archivo COMPLETO que corre o renderiza tal cual, no un fragmento: el
build las pone detras del concepto que ilustran (`_secuencia`). Y es COHERENTE con las
laminas curadas de su clase: el mismo puerto (`EXPOSE 8080`, `-p 8081:8080`), el mismo
nombre de contenedor y de imagen, la misma sintaxis que la actividad exige en la primera
linea (`C4Context`, `C4Container`, `C4Component`, `sequenceDiagram`, `flowchart TD`).
Antes la Clase 3 proyectaba dos Dockerfiles con puertos distintos, y las Clases 4 y 11
proyectaban un `flowchart` donde la actividad cobra `C4Container` / `C4Component`.

Que cubre cada clase, contra lo que su actividad evalua:
  C1  C4 Context en Mermaid                                  -> diagrama de la Clase 1
  C3  el ciclo build/run/verify, imagen vs contenedor, estado -> Clase 3
  C4  las tres reglas del C4 Container                       -> Clase 4
  C6  la politica de secretos en comandos                    -> Clase 6
  C7  que almacenamiento pide cada componente                -> Clase 7
  C8  secretos en el workflow y CD simulado                  -> Clase 8
  C11 C4 Component en Mermaid                                -> Clase 11
  C12 sequenceDiagram con presupuesto de latencia            -> Clase 12
  C13 la regla de autoescalado y su maquina de decision      -> Clase 13
(El Dockerfile, el C4 Container, el Despliegue, el ci.yml y el ADR van en
`CODIGO_SLIDE` del builder: una sola version de cada artefacto.)

Verificacion: los YAML se cargan con PyYAML; Dockerfile, comandos y Mermaid se revisaron por
lectura contra la sintaxis de cada herramienta (no hay Docker ni runner de Actions aqui).
"""

#: `{clase: [(titulo, [lineas]), ...]}`. Cada entrada es una lamina de codigo.
OPERATIVO = {

    # ── Clase 1 · C4 Context en Mermaid ─────────────────────────────────────
    1: [
        ("El C4 Context en Mermaid: el sistema es una sola caja", [
            "C4Context",
            "title Contexto - CloudLite Turnos",
            'Person(cliente, "Cliente", "Reserva turnos")',
            'Person(barbero, "Barbero", "Ve su agenda")',
            'System(app, "CloudLite Turnos", "Agenda turnos")',
            'System_Ext(idp, "Proveedor de identidad", "Login")',
            'System_Ext(correo, "Correo transaccional", "Envia correos")',
            'Rel(cliente, app, "Reserva un turno", "HTTPS")',
            'Rel(barbero, app, "Consulta su agenda", "HTTPS")',
            'Rel(app, idp, "Valida identidad", "OIDC/HTTPS")',
            'Rel(app, correo, "Pide recordatorio", "REST/HTTPS")',
            'Rel(correo, cliente, "Entrega el recordatorio", "SMTP")',
        ]),
    ],

    # ── Clase 3 · Contenedores: el ciclo y lo que demuestra ─────────────────
    3: [
        ("El ciclo completo: construir, ejecutar, verificar", [
            "# 1. construir la imagen con nombre Y etiqueta",
            "$ docker build -t cloudlite-api:0.1.0 .",
            "",
            "# 2. ejecutarla publicando el puerto  (anfitrion:contenedor)",
            "$ docker run -d --name api -p 8081:8080 cloudlite-api:0.1.0",
            "",
            "# 3. verificar que responde DE VERDAD, no solo que el contenedor existe",
            "$ curl -i http://localhost:8081/health",
            "HTTP/1.1 200 OK",
            "Content-Type: application/json",
            "",
            '{"estado":"ok","version":"0.1.0","dependencias":{"bd":"ok"}}',
            "",
            "# 4. si no responde, el log es el primer sitio, no el ultimo",
            "$ docker logs api --tail 20",
        ]),
        ("Imagen, contenedor y capas: los comandos que lo demuestran", [
            "# La IMAGEN es la plantilla; el CONTENEDOR, una instancia en ejecucion.",
            '$ docker images cloudlite-api --format "table {{.Repository}}\\t{{.Tag}}\\t{{.Size}}"',
            "REPOSITORY      TAG     SIZE",
            "cloudlite-api   0.1.0   142MB",
            "",
            '$ docker ps --format "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}"',
            "NAMES   STATUS         PORTS",
            "api     Up 2 minutes   0.0.0.0:8081->8080/tcp",
            "",
            "# De una imagen salen N contenedores: eso es lo que hace escalar barato.",
            "$ docker run -d --name api2 -p 8082:8080 cloudlite-api:0.1.0",
            "$ docker run -d --name api3 -p 8083:8080 cloudlite-api:0.1.0",
        ]),
        ("Limpiar, y la prueba de que el contenedor no guarda estado", [
            "$ docker rm -f api api2 api3",
            "",
            "# Lo escrito DENTRO del contenedor se va con el:",
            "$ docker run -d --name c1 cloudlite-api:0.1.0",
            "$ docker exec c1 sh -c 'echo hola > /tmp/dato.txt'",
            "$ docker rm -f c1",
            "$ docker run --rm cloudlite-api:0.1.0 cat /tmp/dato.txt",
            "cat: can't open '/tmp/dato.txt': No such file or directory",
            "",
            "# Por eso el estado vive fuera: un volumen o una base de datos.",
            "$ docker run -d --name api -p 8081:8080 \\",
            "    -v cloudlite_datos:/app/data cloudlite-api:0.1.0",
        ]),
    ],

    # ── Clase 4 · las reglas del C4 Container ───────────────────────────────
    4: [
        ("Las tres reglas del C4 Container, en codigo", [
            "C4Container",
            "title Tres reglas que el visor no revisa por ti",
            "%% 1. Cada contenedor con TECNOLOGIA.  Mal: Container(api, \"API\")",
            'Container(api, "API de turnos", "Node.js", "Valida la franja y registra el turno")',
            "%% 2. Lo que guarda datos es ContainerDb, no un Container mas",
            'ContainerDb(db, "Base de turnos", "PostgreSQL", "Turnos y horarios")',
            "%% 3. Cada Rel con verbo, protocolo Y formato.  Mal: Rel(api, db, \"usa\")",
            'Rel(api, db, "INSERT y SELECT de turnos", "TCP/SQL")',
            "%% Y los nombres se repiten IGUALES en el Despliegue y en el Component.",
        ]),
    ],

    # ── Clase 6 · Secretos ──────────────────────────────────────────────────
    6: [
        ("La politica de secretos, en comandos", [
            "# 1. lo que NUNCA entra al repositorio ni a la imagen",
            "$ cat .gitignore .dockerignore",
            ".env",
            "*.pem",
            ".env",
            "node_modules",
            "",
            "# 2. el ejemplo SI entra: los NOMBRES de las variables, ningun valor",
            "$ cat .env.example",
            "DATABASE_URL=",
            "JWT_SECRET=",
            "",
            "# 3. un secreto que ya se subio sigue en el historial aunque se borre:",
            "$ git log --all --oneline -- .env",
            "#    por eso el primer paso es ROTARLO; limpiar el historial va despues.",
        ]),
    ],

    # ── Clase 7 · almacenamiento ────────────────────────────────────────────
    7: [
        ("Que tipo de almacenamiento pide cada componente", [
            "flowchart LR",
            "  %% La pregunta que decide: si esta instancia desaparece ahora, que dato se pierde?",
            '  api["API - instancia"]',
            '  api -->|"cache y temporales"| bloque[("Disco de bloque<br/>se va con la instancia")]',
            '  api -->|"HTTPS"| objetos[("Almacenamiento de objetos<br/>fotos, adjuntos, respaldos")]',
            '  api -->|"TCP 5432"| bd[("Base relacional gestionada<br/>turnos, con respaldo")]',
        ]),
    ],

    # ── Clase 8 · CI/CD ─────────────────────────────────────────────────────
    8: [
        ("Secretos en el workflow, y hasta donde llega el pipeline", [
            "# .github/workflows/cd.yml",
            "name: CD simulado",
            "on:",
            "  push:",
            "    branches: [main]",
            "jobs:",
            "  desplegar:",
            "    runs-on: ubuntu-latest",
            "    steps:",
            "      - uses: actions/checkout@v4",
            "      - name: Despliegue SIMULADO",
            "        env:",
            "          TOKEN: ${{ secrets.DEPLOY_TOKEN }}   # del almacen, nunca en claro",
            '        run: echo "token recibido con ${#TOKEN} caracteres; no se despliega"',
            "# CI = construir y probar en cada push: realista aqui.",
            "# CD = desplegar a produccion: necesita un proveedor con credenciales,",
            "#      asi que se declara SIMULADO y el paso lo dice en su nombre.",
        ]),
    ],

    # ── Clase 11 · C4 Component ─────────────────────────────────────────────
    11: [
        ("El C4 Component: por dentro de la API", [
            "C4Component",
            "title Componentes de la API de turnos",
            'Container(spa, "App web", "React", "Muestra franjas y crea la reserva")',
            'Container_Boundary(api, "API de turnos - Node.js") {',
            '  Component(rutas, "Rutas de /turnos", "Express Router", "Recibe y valida la peticion")',
            '  Component(token, "Verificador de token", "Libreria JWT", "Valida firma y expiracion")',
            '  Component(reglas, "Reglas de reserva", "Node.js", "Impide dos turnos en una franja")',
            '  Component(repo, "Repositorio de turnos", "node-postgres", "Encapsula el SQL")',
            '  Component(pub, "Publicador de avisos", "Cliente AMQP", "Publica aviso-de-turno")',
            "}",
            'ContainerDb(db, "Base de turnos", "PostgreSQL", "Turnos y horarios")',
            'ContainerQueue(cola, "Cola de avisos", "RabbitMQ", "Avisos pendientes")',
            'System_Ext(idp, "Proveedor de identidad", "Emite los tokens")',
            'Rel(spa, rutas, "POST /turnos", "HTTPS/JSON")',
            'Rel(rutas, token, "Verifica el token")',
            'Rel(token, idp, "Obtiene las llaves publicas", "HTTPS")',
            'Rel(rutas, reglas, "Pide reservar la franja")',
            'Rel(reglas, repo, "Guarda el turno")',
            'Rel(repo, db, "INSERT del turno", "TCP/SQL")',
            'Rel(reglas, pub, "Pide avisar al cliente")',
            'Rel(pub, cola, "Publica aviso-de-turno", "AMQP")',
        ]),
    ],

    # ── Clase 12 · Presupuesto de latencia ──────────────────────────────────
    12: [
        ("El presupuesto de latencia del camino critico", [
            "sequenceDiagram",
            "  autonumber",
            "  participant N as Navegador",
            "  participant E as Edge TLS",
            "  participant A as API de turnos",
            "  participant D as Base de turnos",
            "  participant Q as Cola de avisos",
            "  Note over N,Q: Objetivo p95 de POST /turnos igual a 300 ms en el pico",
            "  N->>E: POST /turnos",
            "  Note right of E: TLS y proxy - 20 ms",
            "  E->>A: POST /turnos interno en 8080",
            "  Note right of A: Validar token y franja - 30 ms",
            "  A->>D: SELECT de la franja",
            "  Note right of D: Lectura por indice - 40 ms",
            "  A->>D: INSERT del turno y commit",
            "  Note right of D: Escritura y commit - 150 ms - cuello de botella",
            "  A->>Q: Publica aviso-de-turno",
            "  Note right of Q: Publicacion asincrona - 10 ms",
            "  A-->>N: 201 Created",
            "  Note over N,Q: Suma 250 ms - margen 50 ms frente al objetivo",
        ]),
        ("Las metricas objetivo, escritas como se verifican", [
            "| Metrica                | Objetivo | Como se mide              | Si falla                     |",
            "|------------------------|----------|---------------------------|------------------------------|",
            "| p95 de POST /turnos    | < 300 ms | percentil del log del API | revisar el indice            |",
            "| tasa de errores 5xx    | < 1 %    | conteo por minuto         | abrir el log del paso        |",
            "| CPU de la API          | < 70 %   | metrica del proveedor     | escalar horizontal (Clase 13)|",
            "",
            "El PROMEDIO no sirve: con 99 respuestas de 10 ms y una de 5 s",
            "da 60 ms, y el usuario que espero 5 s existe. Por eso p95.",
        ]),
    ],

    # ── Clase 13 · Escalabilidad automatica ─────────────────────────────────
    13: [
        ("La regla de autoescalado, escrita como configuracion", [
            "# Lo que un autoescalador necesita para no oscilar:",
            "autoescalado:",
            "  servicio: cloudlite-api",
            "  minimo: 2                       # 1 no da tolerancia a fallo",
            "  maximo: 6                       # tope que el presupuesto aguanta",
            "  metrica: cpu_promedio",
            "  subir_si: '> 70% durante 5 min'",
            "  bajar_si: '< 30% durante 10 min'  # bajar mas lento que subir",
            "  enfriamiento: 5 min             # sin esto, arranques en cadena",
            "",
            "# Y el limite honesto: escalar la API no escala la BASE. Si el cuello",
            "# de botella es PostgreSQL, seis instancias lo empeoran.",
        ]),
        ("La maquina de decision del autoescalado", [
            "flowchart TD",
            '  obs["Observar CPU cada 60 s"] --> up{"CPU sobre 70 por ciento 5 min?"}',
            '  up -->|"Si"| out["Scale out: +1, max 6"]',
            '  up -->|"No"| down{"CPU bajo 30 por ciento 10 min?"}',
            '  down -->|"Si"| inn["Scale in: -1, min 2"]',
            '  down -->|"No"| obs',
            '  out --> cool["Enfriamiento 5 min"]',
            "  inn --> cool",
            "  cool --> obs",
            '  bd["No escala: base primaria"] -.->|"limite del diseno"| obs',
        ]),
    ],
}
