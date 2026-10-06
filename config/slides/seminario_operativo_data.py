# -*- coding: utf-8 -*-
"""Material operativo proyectado de Seminario: Mermaid y plantillas de artefacto.

Por que existe
--------------
Seminario proyectaba 12 laminas de codigo sobre 276: el 4%. Y sus entregables son casi todos
**diagramas Mermaid** —mapa de dominio, ciclo de vida, modelo en V, plan de sprints, tablero
de flujo, MoSCoW, mapa de backlog, clases, casos de uso, secuencia, actividad, navegacion— y
**plantillas de texto con estructura calificada**: ficha de requisito, historia con criterios
Dado-Cuando-Entonces, especificacion de caso de uso.

La sintaxis de Mermaid es el 100% de si el entregable se puede calificar: un diagrama que no
renderiza en ExamLab no se califica. Y sin embargo no estaba proyectada.

La regla que gobierna lo que se escribe aqui
--------------------------------------------
CLAUDE.md §0: se ensena el MECANISMO que la actividad evalua, no su respuesta. Todas las
actividades piden el artefacto **completo** de VetCare; aqui se proyecta la SINTAXIS sobre un
fragmento minimo de dos o tres entidades, con el resto marcado `<...>`. El estudiante ve como
se escribe y sigue teniendo que construir el modelo entero.

Limite declarado (CLAUDE.md): **estos diagramas no se renderizaron.** No hay Mermaid en el
entorno de generacion. Estan verificados por lectura contra la sintaxis de Mermaid; la
comprobacion real es pegarlos en ExamLab, que los renderiza al instante — y el material ya
pide al estudiante hacer exactamente eso antes de enviar.
"""

#: `{clase: [(titulo, [lineas]) | (titulo, [lineas], leyenda), ...]}`. Cada entrada es una lamina
#: de codigo; la leyenda (opcional) dice la regla que el codigo ya no lleva como comentario.
OPERATIVO = {

    # ── Clase 1 · Mapa de dominio ───────────────────────────────────────────
    1: [
        ("El mapa de dominio en Mermaid", [
            "flowchart LR",
            "  subgraph clinica[Clinica Huellitas]",
            "    rec([Recepcionista])",
            "    vet([Veterinario])",
            "  end",
            "",
            "  subgraph vetcare[VetCare - el sistema]",
            "    agenda[Agendar cita]",
            "    exped[Consultar expediente]",
            "  end",
            "",
            "  lab[Laboratorio externo]",
            "",
            "  rec -->|agenda| agenda",
            "  vet -->|consulta| exped",
            "  exped -->|pide examen| lab",
        ], "Son dos actores y dos capacidades de muestra: el mapa real lleva todos los del dominio."),
        ("La ficha de requisito bien escrito, campo por campo", [
            "RF-01  Registrar mascota",
            "",
            "Actor:        Recepcionista",
            "Precondicion: el dueno ya esta registrado",
            "Descripcion:  El sistema DEBE permitir registrar una mascota con nombre,",
            "              especie, fecha de nacimiento y dueno asociado.",
            "Postcondicion: la mascota queda con expediente abierto y activa = 'S'",
            "Prioridad:    Must",
            "Origen:       entrevista Dr. Ramirez, 12/08/2026",
            "",
            "-- Lo que convierte una frase cruda en requisito: sujeto (el sistema),",
            "-- verbo normativo (DEBE), objeto verificable, y de donde salio.",
            "-- «El sistema debe ser facil de usar» no es un requisito: no se verifica.",
        ]),
    ],

    # ── Clase 2 · Ciclo de vida ─────────────────────────────────────────────
    2: [
        ("El recorrido lineal del ciclo de vida", [
            "flowchart LR",
            "  R[Requisitos] --> D[Diseno] --> C[Construccion]",
            "  C --> P[Pruebas] --> M[Mantenimiento]",
        ], "Lineal significa que no se vuelve: cada fase cierra con un artefacto aprobado y la siguiente empieza sobre el."),
        ("El mismo ciclo en tres vueltas", [
            "flowchart TB",
            "  subgraph v1[Vuelta 1 - ficha del paciente]",
            "    direction LR",
            "    r1[Requisitos] --> d1[Diseno]",
            "    d1 --> c1[Construccion] --> p1[Pruebas]",
            "  end",
            "  subgraph v2[Vuelta 2 - historia clinica y busqueda]",
            "    direction LR",
            "    r2[Requisitos] --> d2[Diseno]",
            "    d2 --> c2[Construccion] --> p2[Pruebas]",
            "  end",
            "  subgraph v3[Vuelta 3 - reportes y metricas]",
            "    direction LR",
            "    r3[Requisitos] --> d3[Diseno]",
            "    d3 --> c3[Construccion] --> p3[Pruebas]",
            "  end",
            "  v1 --> v2 --> v3",
        ], "Iterativo no es «hacerlo mal y repetir»: cada vuelta entrega algo que funciona, sobre una parte del alcance."),
    ],

    # ── Clase 3 · Modelo en V ───────────────────────────────────────────────
    3: [
        ("El modelo en V con trazabilidad", [
            "flowchart TB",
            "  R[Requisitos] --> AF[Analisis funcional]",
            "  AF --> DA[Diseno de arquitectura]",
            "  DA --> DD[Diseno detallado]",
            "  DD --> COD[Codificacion]",
            "  COD --> PU[Pruebas unitarias]",
            "  PU --> PI[Pruebas de integracion]",
            "  PI --> PS[Pruebas de sistema]",
            "  PS --> PA[Pruebas de aceptacion]",
            "",
            "  R  -.verifica.-> PA",
            "  AF -.verifica.-> PS",
            "  DA -.verifica.-> PI",
            "  DD -.verifica.-> PU",
        ], "Las lineas punteadas SON el modelo en V: cada nivel de diseno tiene su nivel de prueba. Sin ellas es una U."),
        ("La solicitud de cambio sobre linea base", [
            "SC-001  Solicitud de cambio",
            "",
            "Documento afectado: ERS VetCare v1.0 (linea base aprobada 20/08/2026)",
            "Solicita:           Dr. Ramirez",
            "Cambio pedido:      agregar recordatorio por WhatsApp al agendar",
            "Requisitos tocados: RF-03 (agendar cita), RNF-02 (disponibilidad)",
            "Impacto en alcance: +1 RF nuevo, +1 integracion externa",
            "Impacto en plan:    +1 sprint de diseno",
            "Decision:           <aprobada | rechazada | diferida>  por <quien>",
            "Nueva version:      ERS VetCare v1.1",
            "",
            "-- Tener linea base no significa que no se pueda cambiar: significa que",
            "-- el cambio deja RASTRO y sube la version. Editar el v1.0 en silencio",
            "-- es lo que rompe la trazabilidad.",
        ]),
    ],

    # ── Clase 4 · Agil ──────────────────────────────────────────────────────
    4: [
        ("El plan de sprints en Mermaid (gantt)", [
            "gantt",
            "  title Tres sprints de diseno de VetCare",
            "  dateFormat YYYY-MM-DD",
            "  axisFormat %d/%m",
            "",
            "  section Sprint 1",
            "  Modelo de dominio      :s1a, 2026-09-01, 7d",
            "  Casos de uso nucleo    :s1b, after s1a, 7d",
            "",
            "  section Sprint 2",
            "  Secuencia de agendar   :s2a, after s1b, 7d",
            "  Wireframes principales :s2b, after s2a, 7d",
            "",
            "  section Sprint 3",
            "  Consolidacion paquete  :s3a, after s2b, 7d",
        ], "Cada tarea empieza «after» la anterior: si una se atrasa, el plan entero se corre."),
        ("El tablero de flujo con limite de trabajo en curso", [
            "flowchart LR",
            "  subgraph backlog[Backlog]",
            "    b1[HU-04]",
            "    b2[HU-05]",
            "  end",
            "  subgraph curso[En curso - LIMITE 2]",
            "    c1[HU-02]",
            "    c2[HU-03]",
            "  end",
            "  subgraph rev[En revision - LIMITE 1]",
            "    r1[HU-01]",
            "  end",
            "  subgraph listo[Terminado]",
            "    l1[HU-00]",
            "  end",
            "",
            "  backlog --> curso --> rev --> listo",
        ], "El limite es lo que hace servir el tablero: sin el todo esta «en curso» y nada termina."),
    ],

    # ── Clase 6 · Requerimientos ────────────────────────────────────────────
    6: [
        ("La priorizacion MoSCoW en Mermaid", [
            "flowchart TB",
            "  subgraph must[Must - sin esto no hay producto]",
            "    m1[RF-01 Registrar mascota]",
            "    m2[RF-03 Agendar cita]",
            "  end",
            "  subgraph should[Should - importante, hay alternativa manual]",
            "    s1[RF-07 Reporte mensual]",
            "  end",
            "  subgraph could[Could - si sobra tiempo]",
            "    c1[RF-11 Exportar a Excel]",
            "  end",
            "  subgraph wont[Wont - fuera de este alcance]",
            "    w1[RF-15 App movil]",
            "  end",
        ], "Wont no es «nunca»: es «no en esta version», y va escrito para que nadie lo de por incluido."),
        ("El RNF cuantificado: la diferencia esta en el numero", [
            "RNF-02  Disponibilidad del agendamiento",
            "",
            "MAL:  «el sistema debe estar disponible»",
            "BIEN: «el modulo de agendamiento DEBE estar disponible el 99% del",
            "       horario de atencion (lunes a sabado, 07:00-19:00), medido",
            "       mensualmente sobre el registro de caidas»",
            "",
            "-- Los cuatro pedazos que lo hacen verificable:",
            "--   1. la magnitud       99%",
            "--   2. la ventana        lun-sab 07:00-19:00",
            "--   3. el periodo        mensual",
            "--   4. la fuente del dato  el registro de caidas",
            "-- Si falta uno, nadie puede decir si se cumplio.",
        ]),
    ],

    # ── Clase 7 · Historias de usuario ──────────────────────────────────────
    7: [
        ("La historia y sus criterios en Dado-Cuando-Entonces", [
            "HU-03  Agendar una cita",
            "",
            "Como recepcionista",
            "quiero agendar una cita para una mascota registrada",
            "para que el veterinario tenga su agenda del dia ordenada.",
            "",
            "Criterios de aceptacion",
            "",
            "CA-1  Dado que la mascota esta activa",
            "      Cuando selecciono fecha y hora libres",
            "      Entonces la cita queda en estado PROGRAMADA",
            "",
            "CA-2  Dado que la mascota esta inactiva",
            "      Cuando intento agendar",
            "      Entonces el sistema lo rechaza y explica por que",
            "",
            "-- Un criterio sin «Dado» no se puede probar: falta el estado inicial.",
        ]),
        ("El mapa del backlog: epicas, historias y orden", [
            "flowchart TB",
            "  E1[EPICA 1 - Agenda]",
            "  E2[EPICA 2 - Expediente]",
            "",
            "  E1 --> H1[HU-01 Registrar dueno<br/>3 pts]",
            "  E1 --> H2[HU-02 Registrar mascota<br/>5 pts]",
            "  E1 --> H3[HU-03 Agendar cita<br/>8 pts]",
            "  E2 --> H4[HU-04 Abrir expediente<br/>5 pts]",
        ], "Los puntos son relativos, no horas; el orden del backlog sale del valor, no de los puntos."),
    ],

    # ── Clase 8 · UML: clases ───────────────────────────────────────────────
    8: [
        ("El diagrama de clases en Mermaid", [
            "classDiagram",
            "  class Dueno {",
            "    -int idDueno",
            "    -String nombre",
            "    -String telefono",
            "    +registrar()",
            "  }",
            "  class Mascota {",
            "    -int idMascota",
            "    -String nombre",
            "    -String especie",
            "    -char activa",
            "    +abrirExpediente()",
            "  }",
            "",
            "  Dueno \"1\" --> \"0..*\" Mascota : posee",
        ], "Visibilidad (- privado, + publico), tipo de cada atributo y multiplicidad en los dos extremos."),
        ("Lo que NO es una clase del dominio", [
            "classDiagram",
            "  class Dueno",
            "  class Mascota",
            "  class Cita",
            "  Dueno \"1\" --> \"0..*\" Mascota : posee",
            "  Mascota \"1\" --> \"0..*\" Cita : tiene",
            "  note for Mascota \"La nombra el cliente\\ny tiene reglas\"",
        ], "No son del dominio: FormularioRegistroMascota (pantalla), ConexionBaseDatos (infraestructura), GestorDeMascotas, BotonGuardar."),
    ],

    # ── Clase 9 · Casos de uso ──────────────────────────────────────────────
    9: [
        ("El diagrama de casos de uso en Mermaid", [
            "flowchart LR",
            "  rec([Recepcionista])",
            "  vet([Veterinario])",
            "",
            "  subgraph sistema[VetCare]",
            "    cu1((CU-01<br/>Registrar mascota))",
            "    cu2((CU-02<br/>Buscar expediente))",
            "    cu3((CU-04<br/>Agendar cita))",
            "    cu4((Validar<br/>disponibilidad))",
            "  end",
            "",
            "  rec --> cu1",
            "  rec --> cu3",
            "  vet --> cu2",
            "  cu3 -.include.-> cu4",
        ], "include: el caso base siempre lo ejecuta (agendar siempre valida). extend: solo si se cumple una condicion."),
        ("La especificacion textual del caso de uso", [
            "CU-01  Registrar mascota",
            "",
            "Actor principal:  Recepcionista",
            "Trazabilidad:     RF-01, RF-02",
            "Precondicion:     el dueno existe y esta activo",
            "Postcondicion:    la mascota queda activa con expediente abierto",
            "",
            "Flujo principal",
            "  1. La recepcionista solicita registrar una mascota.",
            "  2. El sistema pide nombre, especie, fecha de nacimiento y dueno.",
            "  3. La recepcionista ingresa los datos.",
            "  4. El sistema valida que el dueno exista y este activo.",
            "  5. El sistema guarda la mascota y confirma.",
            "",
            "Flujos alternos",
            "  4a. El dueno no existe -> el sistema ofrece registrarlo primero.",
            "  4b. Falta un dato obligatorio -> el sistema lo senala y no guarda.",
            "",
            "-- Sin flujos alternos la especificacion esta a medias: el 4a y el 4b",
            "-- son las dos terceras partes del trabajo real del programador.",
        ]),
    ],

    # ── Clase 11 · Avance del PI ────────────────────────────────────────────
    11: [
        ("El glosario de nombres canonicos: el hueco mas comun", [
            "| Concepto      | Nombre canonico | Como aparece mal en el paquete     |",
            "|---------------|-----------------|------------------------------------|",
            "| el animal     | Mascota         | Paciente, Animal, mascotas         |",
            "| quien lo trae | Propietario     | Dueno, Cliente, Responsable        |",
            "| el encuentro  | Cita            | Turno, Agendamiento, Reserva       |",
            "| el registro   | Consulta        | Atencion, HistoriaClinica          |",
            "",
            "-- El diagrama de clases dice Mascota, el caso de uso dice Paciente y el",
            "-- wireframe dice Animal: son tres entregables que hablan de cosas",
            "-- distintas para quien los lee. Un solo nombre por concepto, y el mismo",
            "-- en TODOS los artefactos. Esto es la P2 del hito y vale puntos.",
        ]),
    ],

    # ── Clase 12 · UML avanzado ─────────────────────────────────────────────
    12: [
        ("El diagrama de secuencia en Mermaid", [
            "sequenceDiagram",
            "  autonumber",
            "  actor R as Recepcionista",
            "  participant UI as Pantalla Agendar",
            "  participant S as ServicioCita",
            "  participant M as RepositorioMascota",
            "  participant C as RepositorioCita",
            "",
            "  R->>UI: solicita agendar",
            "  UI->>S: agendar(idMascota, fechaHora)",
            "  S->>M: estaActiva(idMascota)",
            "  M-->>S: true",
            "  S->>C: existeEnFranja(idVet, fechaHora)",
            "  C-->>S: false",
            "  S->>C: guardar(cita)",
            "  C-->>S: idCita",
            "  S-->>UI: PROGRAMADA (idCita)",
            "  UI-->>R: confirmacion",
        ]),
        ("El diagrama de actividad con decisiones en Mermaid", [
            "flowchart TB",
            "  ini([Inicio]) --> llega[La mascota llega a consulta]",
            "  llega --> tiene{Tiene cita<br/>programada?}",
            "  tiene -->|Si| atiende[Registrar consulta]",
            "  tiene -->|No| urg{Es urgencia?}",
            "  urg -->|Si| crear[Crear cita de urgencia] --> atiende",
            "  urg -->|No| agendar[Agendar para otro dia] --> fin([Fin])",
            "  atiende --> receta[Emitir receta e insumos]",
            "  receta --> fin",
        ], "Cada rombo lleva todas sus salidas rotuladas: un rombo con una sola salida no es una decision, es un paso."),
        ("La tabla de mapeo mensaje a operacion", [
            "| Mensaje            | Clase receptora    | Operacion            |",
            "|--------------------|--------------------|----------------------|",
            "| agendar(m, f)      | ServicioCita       | +agendar(int, Date)  |",
            "| estaActiva(m)      | RepositorioMascota | +estaActiva(int)     |",
            "| existeEnFranja(v,f)| RepositorioCita    | +existeEnFranja(...) |",
            "| guardar(cita)      | RepositorioCita    | +guardar(Cita)       |",
            "",
            "-- Cada mensaje TIENE que existir como operacion en el diagrama de clases:",
            "-- si no esta, o falta la operacion o sobra el mensaje.",
        ]),
    ],

    # ── Clase 13 · Interfaces ───────────────────────────────────────────────
    13: [
        ("El mapa de navegacion del prototipo", [
            "flowchart LR",
            "  login[Ingreso] --> menu[Menu principal]",
            "  menu --> regm[Registrar mascota]",
            "  menu --> busc[Buscar expediente]",
            "  menu --> agen[Agendar cita]",
            "",
            "  regm -->|guardar| menu",
            "  regm -->|cancelar| menu",
            "  busc -->|1 resultado| det[Detalle del expediente]",
            "  busc -->|varios| lista[Lista de resultados] --> det",
            "  busc -->|ninguno| vacio[Estado vacio<br/>con accion sugerida]",
        ], "Los tres caminos de una busqueda —uno, varios, ninguno— separan un wireframe de un dibujo."),
        ("La tabla de anotaciones del wireframe", [
            "| Campo de la pantalla | RF que lo exige | Atributo de la clase  | Validacion        |",
            "|----------------------|-----------------|-----------------------|-------------------|",
            "| Nombre               | RF-01           | Mascota.nombre        | obligatorio       |",
            "| Especie              | RF-01           | Mascota.especie       | lista cerrada     |",
            "| Fecha de nacimiento  | RF-02           | Mascota.fechaNac      | no futura         |",
            "| Dueno                | RF-01           | Mascota.idDueno (FK)  | debe existir      |",
            "",
            "-- Un campo sin RF que lo exija es un campo que nadie pidio: se quita o",
            "-- se agrega el requisito. Un atributo de la clase sin campo en ninguna",
            "-- pantalla es un dato que nadie puede ingresar.",
        ]),
    ],

    # ── Clase 14 · Sustentacion ─────────────────────────────────────────────
    14: [
        ("El guion cronometrado de la sustentacion", [
            "gantt",
            "  title Sustentacion VetCare - 12 minutos",
            "  dateFormat mm:ss",
            "  axisFormat %M:%S",
            "",
            "  section Guion",
            "  Problema               :g1, 00:00, 90s",
            "  Alcance                :g2, after g1, 90s",
            "  Requisitos             :g3, after g2, 2m",
            "  Modelo UML             :g4, after g3, 2m",
            "  Prototipo en vivo      :g5, after g4, 2m",
            "  Decisiones defendidas  :g6, after g5, 2m",
            "  Riesgos y cierre       :g7, after g6, 1m",
        ], "Sin cronometro, el bloque de decisiones —el que mas pesa ante el jurado— se queda sin tiempo."),
    ],
}
