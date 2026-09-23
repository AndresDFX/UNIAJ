# -*- coding: utf-8 -*-
"""Material operativo proyectado de Arquitectura: Dockerfile, CLI, Mermaid, YAML, ADR.

Por que existe
--------------
Arquitectura proyectaba 7 laminas de codigo sobre 391: el 1%. Y sus entregables son casi
todos artefactos con FORMA: un Dockerfile, un `docker build`, un diagrama C4 en Mermaid, un
workflow de GitHub Actions, un ADR. El estudiante que no ha visto la forma proyectada la
adivina, y pierde puntos por el formato, no por el criterio.

La regla que gobierna lo que se escribe aqui
--------------------------------------------
CLAUDE.md §0: se ensena el MECANISMO que la actividad evalua, no su respuesta. Cada actividad
de ARQ pide el artefacto **para el dominio que el estudiante eligio**, asi que aqui se
proyecta la forma sobre el artefacto comun del curso —`cloudlite-api`, que es el nombre que
ya usa el material— con los huecos del dominio marcados como `<...>`. La forma se ve
completa; la decision sigue siendo del estudiante.

Que cubre cada clase, contra lo que su actividad evalua:
  C3  Dockerfile + el ciclo build/run/verify en Killercoda  -> P1..P4 de la Clase 3
  C4  C4 Container en Mermaid                               -> P2 de la Clase 4
  C7  Diagrama de Despliegue en Mermaid                      -> P1 de la Clase 7
  C8  Workflow de CI en YAML + politica de secretos          -> P1 y P3 de la Clase 8
  C11 C4 Component en Mermaid                                -> P3 de la Clase 11
  C12 sequenceDiagram con presupuesto de latencia            -> P2 de la Clase 12
  C2  Plantilla de ADR                                       -> P2 y P3 de la Clase 2

Limite declarado (CLAUDE.md): **nada de esto se ejecuto.** No hay Docker ni un runner de
Actions en el entorno de generacion. Esta verificado por lectura contra la sintaxis de cada
herramienta; la comprobacion real es el laboratorio de la clase.
"""

#: `{clase: [(titulo, [lineas]), ...]}`. Cada entrada es una lamina de codigo.
OPERATIVO = {

    # ── Clase 2 · ADR: la decision escrita ──────────────────────────────────
    2: [
        ("La plantilla de ADR: los seis apartados que se califican", [
            "# ADR-001 · Modelo de servicio dominante de CloudLite",
            "",
            "## 1. Estado",
            "Aceptada · 2026-09-01 · decide: <su nombre>",
            "",
            "## 2. Contexto",
            "<que problema del dominio obliga a decidir esto, en 3 o 4 lineas>",
            "",
            "## 3. Alternativas consideradas",
            "- IaaS  — <que ganaria y que costaria en SU dominio>",
            "- PaaS  — <idem>",
            "- SaaS  — <idem>",
            "",
            "## 4. Decision",
            "Se adopta <IaaS|PaaS|SaaS> como modelo dominante porque <criterio>.",
            "",
            "## 5. Justificacion contra los atributos de calidad",
            "<el atributo de la Clase 1 que esta decision favorece, y el que sacrifica>",
            "",
            "## 6. Consecuencias",
            "Positivas: <...>   Negativas: <...>   A revisar si: <condicion>",
        ]),
    ],

    # ── Clase 3 · Contenedores: el artefacto y el ciclo ─────────────────────
    3: [
        ("El Dockerfile minimo, capa por capa", [
            "# Cada instruccion es UNA CAPA. El orden decide que se reconstruye.",
            "FROM node:20-alpine",
            "",
            "WORKDIR /app",
            "",
            "# Primero las dependencias: si el codigo cambia y package.json no,",
            "# esta capa se reutiliza de la cache y el build tarda segundos.",
            "COPY package*.json ./",
            "RUN npm ci --omit=dev",
            "",
            "# Despues el codigo, que es lo que cambia en cada commit.",
            "COPY . .",
            "",
            "EXPOSE 3000",
            "CMD [\"node\", \"server.js\"]",
        ]),
        ("El ciclo completo: construir, ejecutar, verificar", [
            "# 1. construir la imagen y etiquetarla con version",
            "$ docker build -t cloudlite-api:0.1.0 .",
            "",
            "# 2. ejecutarla publicando el puerto (host:contenedor)",
            "$ docker run -d --name cloudlite -p 8080:3000 cloudlite-api:0.1.0",
            "",
            "# 3. verificar que responde DE VERDAD, no que el contenedor existe",
            "$ curl -i http://localhost:8080/health",
            "HTTP/1.1 200 OK",
            "",
            "# 4. si no responde, el log es el primer sitio, no el ultimo",
            "$ docker logs cloudlite --tail 20",
        ]),
        ("Imagen, contenedor y capas: los comandos que lo demuestran", [
            "# La IMAGEN es la plantilla; el CONTENEDOR es una instancia en ejecucion.",
            "$ docker images cloudlite-api",
            "REPOSITORY      TAG     IMAGE ID       SIZE",
            "cloudlite-api   0.1.0   a1b2c3d4e5f6   142MB",
            "",
            "$ docker ps",
            "CONTAINER ID   IMAGE                 STATUS         PORTS",
            "9f8e7d6c5b4a   cloudlite-api:0.1.0   Up 2 minutes   0.0.0.0:8080->3000/tcp",
            "",
            "# De una imagen salen N contenedores: eso es lo que hace escalar barato.",
            "$ docker run -d -p 8081:3000 cloudlite-api:0.1.0",
            "$ docker run -d -p 8082:3000 cloudlite-api:0.1.0",
        ]),
        ("Limpiar, y la prueba de que el contenedor no guarda estado", [
            "$ docker stop cloudlite && docker rm cloudlite",
            "",
            "# Lo escrito DENTRO del contenedor se va con el:",
            "$ docker run -d --name c1 cloudlite-api:0.1.0",
            "$ docker exec c1 sh -c 'echo hola > /tmp/dato.txt'",
            "$ docker rm -f c1",
            "$ docker run --rm cloudlite-api:0.1.0 cat /tmp/dato.txt",
            "cat: can't open '/tmp/dato.txt': No such file or directory",
            "",
            "# Por eso el estado vive fuera: volumen o base de datos gestionada.",
            "$ docker run -d -v cloudlite_datos:/app/data cloudlite-api:0.1.0",
        ]),
    ],

    # ── Clase 4 · C4 Container en Mermaid ───────────────────────────────────
    4: [
        ("El C4 Container en Mermaid: la forma que la plataforma del curso renderiza", [
            "flowchart TB",
            "  usuario([Usuario <rol de su dominio>])",
            "",
            "  subgraph cloudlite[CloudLite App]",
            "    web[Web SPA<br/>React]",
            "    api[API REST<br/>Node + Express]",
            "    db[(Base de datos<br/>PostgreSQL)]",
            "    cola[[Cola de trabajos<br/>Redis]]",
            "  end",
            "",
            "  correo[Servicio de correo<br/>externo]",
            "",
            "  usuario -->|HTTPS| web",
            "  web -->|JSON/HTTPS| api",
            "  api -->|SQL| db",
            "  api -->|encola| cola",
            "  cola -->|SMTP| correo",
        ]),
        ("Lo que se califica del diagrama, y no es el dibujo", [
            "%% Cada caja lleva TECNOLOGIA, no solo nombre:",
            "%%   mal:  api[API]",
            "%%   bien: api[API REST<br/>Node + Express]",
            "",
            "%% Cada flecha lleva PROTOCOLO y sentido:",
            "%%   mal:  web --- api",
            "%%   bien: web -->|JSON/HTTPS| api",
            "",
            "%% Lo externo va FUERA del subgraph del sistema: es la frontera",
            "%% que define de que se es responsable.",
            "",
            "%% Y los nombres tienen que ser LOS MISMOS en el C4, en el Despliegue",
            "%% (Clase 7) y en el Component (Clase 11). Reconciliarlos es la P2 del hito.",
        ]),
    ],

    # ── Clase 6 · Secretos ──────────────────────────────────────────────────
    6: [
        ("La politica de secretos, en comandos", [
            "# 1. lo que NUNCA entra al repositorio",
            "$ cat .gitignore",
            ".env",
            "*.pem",
            "credenciales*.json",
            "",
            "# 2. el ejemplo SI entra, para que otro pueda arrancar",
            "$ cat .env.example",
            "DATABASE_URL=postgres://usuario:clave@host:5432/cloudlite",
            "JWT_SECRET=cambiar_en_produccion",
            "",
            "# 3. si un secreto ya se subio, rotarlo NO es opcional:",
            "#    el historial de git lo conserva aunque se borre el archivo.",
            "$ git log --all --full-history -- .env",
        ]),
    ],

    # ── Clase 7 · Despliegue en Mermaid ─────────────────────────────────────
    7: [
        ("El diagrama de Despliegue: donde corre cada cosa", [
            "flowchart TB",
            "  subgraph internet[Internet]",
            "    nav([Navegador del usuario])",
            "  end",
            "",
            "  subgraph nube[Proveedor cloud - region <su region>]",
            "    subgraph edge[CDN / Edge]",
            "      estatico[/Archivos estaticos<br/>build de la SPA/]",
            "    end",
            "    subgraph app[Servicio de aplicacion]",
            "      api1[Instancia API 1]",
            "      api2[Instancia API 2]",
            "    end",
            "    subgraph datos[Servicio gestionado]",
            "      pg[(PostgreSQL<br/>con respaldo diario)]",
            "      obj[(Almacenamiento de objetos<br/>adjuntos)]",
            "    end",
            "  end",
            "",
            "  nav --> estatico",
            "  nav --> api1 & api2",
            "  api1 & api2 --> pg",
            "  api1 & api2 --> obj",
        ]),
        ("Que tipo de almacenamiento pide cada componente", [
            "%% BLOQUE (disco de la instancia): rapido, se va con la instancia.",
            "%%   -> cache local, archivos temporales. NUNCA el dato que importa.",
            "",
            "%% OBJETOS (S3 y equivalentes): barato, por HTTP, no se monta como disco.",
            "%%   -> adjuntos, imagenes, respaldos, el build de la SPA.",
            "",
            "%% BASE RELACIONAL GESTIONADA: transaccional, con respaldo y replica.",
            "%%   -> lo que necesita integridad y consultas.",
            "",
            "%% La pregunta que decide: si esta instancia desaparece ahora mismo,",
            "%% que dato se pierde? Si la respuesta no es «ninguno», esta mal ubicado.",
        ]),
    ],

    # ── Clase 8 · CI/CD ─────────────────────────────────────────────────────
    8: [
        ("El workflow de CI: el archivo completo", [
            "# .github/workflows/ci.yml",
            "name: CI",
            "",
            "on:",
            "  push:",
            "    branches: [main]",
            "  pull_request:",
            "",
            "jobs:",
            "  construir-y-probar:",
            "    runs-on: ubuntu-latest",
            "    steps:",
            "      - uses: actions/checkout@v4",
            "",
            "      - uses: actions/setup-node@v4",
            "        with:",
            "          node-version: '20'",
            "          cache: 'npm'",
            "",
            "      - run: npm ci",
            "      - run: npm test -- --ci",
            "      - run: docker build -t cloudlite-api:${{ github.sha }} .",
        ]),
        ("Secretos en el workflow, y hasta donde llega el pipeline", [
            "      - name: Desplegar",
            "        env:",
            "          TOKEN: ${{ secrets.DEPLOY_TOKEN }}   # del almacen, nunca en claro",
            "        run: ./deploy.sh",
            "",
            "# CI  = construir y probar en cada push. Esto SI es realista aqui.",
            "# CD  = desplegar automaticamente a produccion. Necesita un proveedor",
            "#       con credenciales, asi que en el PI se declara como SIMULADO",
            "#       y el ultimo paso se rotula como tal. Decirlo vale puntos;",
            "#       fingirlo los quita.",
        ]),
    ],

    # ── Clase 11 · C4 Component ─────────────────────────────────────────────
    11: [
        ("El C4 Component: por dentro de la API", [
            "flowchart TB",
            "  subgraph api[API REST de CloudLite - Node + Express]",
            "    rutas[Capa de rutas<br/>valida entrada y responde HTTP]",
            "    servicio[Servicio de dominio<br/>reglas de <su dominio>]",
            "    repo[Repositorio<br/>consultas SQL]",
            "    auth[Autenticacion<br/>verifica el token]",
            "  end",
            "",
            "  web[Web SPA] -->|JSON/HTTPS| rutas",
            "  rutas --> auth",
            "  rutas --> servicio",
            "  servicio --> repo",
            "  repo -->|SQL| db[(PostgreSQL)]",
            "",
            "%% La regla del nivel Component: las cajas son piezas de CODIGO dentro",
            "%% de UN container, no servicios nuevos. Si le pone un puerto, es un",
            "%% container y va en el diagrama de la Clase 4.",
        ]),
    ],

    # ── Clase 12 · Presupuesto de latencia ──────────────────────────────────
    12: [
        ("El presupuesto de latencia del camino critico", [
            "sequenceDiagram",
            "  autonumber",
            "  participant U as Usuario",
            "  participant W as Web SPA",
            "  participant A as API",
            "  participant D as PostgreSQL",
            "",
            "  U->>W: accion del pico (<su caso>)",
            "  W->>A: POST /recurso          %% red: 40 ms",
            "  A->>A: validar + autorizar    %% 10 ms",
            "  A->>D: SELECT + INSERT        %% 60 ms",
            "  D-->>A: filas",
            "  A-->>W: 201 Created           %% red: 40 ms",
            "  W-->>U: confirmacion          %% render: 50 ms",
            "",
            "  Note over U,D: presupuesto total 200 ms · medido p95, no promedio",
        ]),
        ("Las metricas objetivo, escritas como se verifican", [
            "# Cada metrica necesita las cuatro columnas, o no es verificable:",
            "#   metrica | objetivo | como se mide | que se hace si falla",
            "",
            "# p95 de POST /recurso   | < 200 ms | percentil del log de la API",
            "#                        |          | -> revisar el indice de la consulta",
            "# tasa de error 5xx      | < 1%     | conteo por minuto",
            "#                        |          | -> abrir el log del paso que falla",
            "# uso de CPU de la API   | < 70%    | metrica del proveedor",
            "#                        |          | -> escalar horizontal (Clase 13)",
            "",
            "# PROMEDIO no sirve: con 99 respuestas de 10 ms y una de 5 s el promedio",
            "# da 60 ms y el usuario que espero 5 s existe. Por eso p95.",
        ]),
    ],

    # ── Clase 13 · Escalabilidad automatica ─────────────────────────────────
    13: [
        ("La regla de autoescalado, escrita como configuracion", [
            "# Lo que un autoescalador necesita para no oscilar:",
            "autoescalado:",
            "  servicio: cloudlite-api",
            "  minimo: 2                  # 1 no da tolerancia a fallo",
            "  maximo: 6                  # tope que el presupuesto aguanta",
            "  metrica: cpu_promedio",
            "  objetivo: 65               # por debajo del 70% de la Clase 12",
            "  subir_si:   '> 65% durante 3 min'",
            "  bajar_si:   '< 35% durante 10 min'   # bajar mas lento que subir",
            "  enfriamiento: 5 min        # sin esto entra en bandada de arranques",
            "",
            "# Y el limite honesto: escalar la API no escala la BASE. Si el cuello",
            "# de botella es PostgreSQL, seis instancias lo empeoran.",
        ]),
    ],
}
