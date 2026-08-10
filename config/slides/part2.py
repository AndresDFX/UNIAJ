# -*- coding: utf-8 -*-
"""Part 2: PI-first content maps."""

EXTRA = {
1: [
("Que es arquitectura cloud", [
"@@Arquitectura@@ = componentes + relaciones + despliegue + calidad.",
"Cloud: recursos bajo demanda y automatizacion.",
"CloudLite: disenar y simular en labs gratis (sin IaaS de pago).",
"Bloques: cliente → API → logica → datos → observabilidad.",
]),
("CloudLite App — hilo conductor", [
"Web/API de dominio realista (citas, academia, inventario).",
"Entregables: diagramas + contenedor + CI/CD conceptual + informe.",
"Hoy: problema + capacidades + C4 Context.",
"Stack: draw.io, Killercoda, Play with Docker, GitHub Actions.",
]),
("De dominio a arquitectura", [
"Actor/problema → capacidades → contenedores logicos → datos → riesgos.",
"Ejemplo AgendaU: API + auth + agenda + notificaciones.",
"Salida: C4 Context (sistema + actores externos).",
]),
],
2: [
("IaaS · PaaS · SaaS", [
"@@IaaS@@: usted administra SO/runtime; proveedor da computo/red/disco.",
"@@PaaS@@: despliega app; proveedor gestiona runtime.",
"@@SaaS@@: consume servicio listo; poca personalizacion.",
"Simulamos en navegador; no abrimos IaaS con tarjeta.",
]),
("Decision para CloudLite", [
"MVP academico: suele ganar PaaS conceptual + contenedores.",
"SaaS como satelite (auth, email), no como toda la app.",
"ADR: contexto, decision, alternativas, consecuencias.",
]),
],
3: [
("VM vs contenedor", [
"VM: hipervisor + SO completo. Contenedor: kernel compartido.",
"Imagen = capas; contenedor = instancia.",
"CloudLite: al menos un servicio contenerizado.",
]),
("Lab en navegador", [
"Killercoda o Play with Docker: build/run del stub.",
"Si el lab caduca: Dockerfile + capturas con timestamp.",
"Sin secretos en la imagen.",
]),
],
4: [
("Monolito vs microservicios", [
"Monolito modular vale para equipos pequenos.",
"Anti-patron: 12 servicios para 3 estudiantes.",
"Regla CloudLite: 2-5 contenedores logicos justificados.",
]),
("C4-lite en draw.io", [
"Context → Containers. Flechas = protocolos/contratos.",
"Cada caja: nombre + responsabilidad + tech tentativa.",
"Distribuido implica latencia, reintentos, timeouts.",
]),
],
6: [
("Amenazas del PI", [
"Credenciales en repo · APIs abiertas · PII sin TLS.",
"STRIDE-lite: 5 amenazas del dominio, no genericas.",
]),
("Controles practicos", [
"HTTPS en diagrama · tokens · least privilege.",
"Secrets en Actions; nunca en Dockerfile.",
]),
],
7: [
("Red logica", [
"Cliente → edge → app → datos. Zonas Publica/Privada/Datos.",
"Sin subnets AWS inventadas; trust boundaries claros.",
]),
("Storage + Deployment", [
"DB + object segun caso. Nombres alineados al C4.",
"Puertos y almacenes etiquetados en el diagrama.",
]),
],
8: [
("CI/CD sin tarjeta", [
"CI: build+test. CD: deploy simulado (echo/artifact).",
"YAML en .github/workflows/ con runners free.",
]),
("Monitoreo", [
"Golden signals-lite: latencia, trafico, errores, saturacion.",
"Healthcheck del contenedor + logs estructurados.",
]),
],
10: [
("Costos cualitativos", [
"Bajo/Medio/Alto por componente. Drivers: idle, egress, CI.",
"Sostenibilidad: imagenes slim, labs temporales, right-sizing.",
]),
],
11: [
("Checklist v1", [
"Dominio · ADR · C4 · Deployment · Dockerfile · Actions · Seguridad · Costos.",
"Hoy revision en vivo; no es sustentacion ni Parcial 3.",
]),
("Errores frecuentes", [
"Microservicios teatro · nombres distintos · secretos en imagen · CI vacio.",
]),
],
12: [
("Rendimiento", [
"RPS/usuarios · p95 latencia · error rate + bottleneck (DB/auth).",
"Escenario de pico del dominio (narrado/simulado OK).",
]),
("Pitch 5-8 min", [
"Problema · arquitectura · contenedor · CI · seguridad/costos · Q&A.",
"Todos hablan. Demo: diagrama + captura lab/Actions.",
]),
],
13: [
("Escala CloudLite", [
"Horizontal: mas replicas API. Vertical: mas CPU/RAM.",
"Triggers: RPS, p95, cola. Definir min/max y lo que NO escala.",
]),
],
15: [
("Sustentacion", [
"Informe · 3 diagramas · Dockerfile+captura · Actions · pitch.",
"PI 20% no sustituye Parcial 3. Sin cloud de pago.",
]),
],
}

PASOS = {
1: ["Equipo 2-3 (o individual).","Dominio concreto.","Problema 2-3 frases + 3-5 capacidades + actores.",
    "C4 Context en Excalidraw/draw.io.","Entrega Doc+PNG → ExamLab domingo 23:59."],
2: ["Leer slides + enunciado PI.","Matriz IaaS/PaaS/SaaS vs dominio.","ADR-001 con 2 alternativas.",
    "Actualizar informe (Modelo de servicio).","Entrega domingo 23:59."],
3: ["Elegir servicio a contenerizar.","Build/run en Killercoda o PWD.","Dockerfile en repo/ZIP.",
    "Captura o enlace de sesion.","Seccion Contenedores en informe."],
4: ["C4 Containers 2-5 servicios.","3 contratos API.","Export PNG+.drawio.",
    "Seccion Arquitectura logica + riesgos."],
6: ["5 amenazas STRIDE-lite.","Control + evidencia en diagrama.","Politica de secretos.",
    "Seccion Seguridad 1-1.5 paginas."],
7: ["Deployment zonas publica/privada/datos.","Puertos + storage.","Alinear nombres con C4.",
    "Seccion Redes y almacenamiento."],
8: ["Repo free + stub.","ci.yml build/test + deploy simulado.","4-6 metricas.",
    "Captura run o YAML+explicacion.","Secciones CI/CD y Monitoreo."],
10: ["Tabla componente→driver→B/M/A→apalancamiento.","3 acciones sostenibilidad.",
     "Integrar 1 pagina en informe."],
11: ["Checklist si/no + enlaces.","Unificar nombres C4/Deployment.","ZIP/repo evidencias.",
     "Feedback docente + backlog 5 items Clase 12."],
12: ["Escenario carga + 3 metricas + bottleneck.","Ensayo pitch 5-8 min.",
     "Cerrar backlog + paquete casi-final."],
13: ["Que escala y por que.","2 triggers + min/max + lo que no escala.",
     "Impacto costos; nota opcional en Deployment."],
15: ["Subir paquete final.","Pitch 5-8 min segun instruccion.",
     "Q&A escrito (3+3) + reflexion media pagina."],
}

QUIZ = {
1: [("Nube vs servidor local?","Cloud elastico/automatizado; on-prem capacidad fija."),
    ("Dos entregables PI?","Diagramas, lab, Actions, informe o sustentacion."),
    ("Por que no AWS con tarjeta?","Politica gratis+navegador.")],
2: [("Runtime gestionado por proveedor?","PaaS."),("Que es ADR?","Decision + trade-offs."),
    ("SaaS dominante en CloudLite?","Rara vez; si como satelite.")],
3: [("Que comparte el contenedor?","Kernel."),("Lab permitido?","Killercoda o PWD."),
    ("Secretos en Dockerfile?","No; quedan en la imagen.")],
4: [("Cuando monolito?","Equipo pequeno/dominio acotado."),("Etiqueta de flecha C4?","Protocolo."),
    ("Riesgo distribuido?","Latencia/particion/reintentos.")],
6: [("API keys en imagen?","No."),("Control spoofing?","Tokens+HTTPS."),
    ("Least privilege?","Permisos minimos.")],
7: [("Zonas separadas?","Trust boundaries."),("Object storage?","Media/archivos."),
    ("Nombres = C4?","Si.")],
8: [("CI vs CD?","CI valida; CD despliega (aqui simulado)."),("Secrets donde?","Settings Secrets."),
    ("Golden signal?","Latencia/errores/trafico/saturacion.")],
10: [("Driver de costo?","Idle/egress/storage."),("Right-sizing?","Ajustar a uso real."),
     ("Labs temporales?","Evitan siempre-on.")],
11: [("C4 vs Deployment?","Mismos nombres."),("Checkpoint = P3?","No."),
     ("Anti-patron?","Microservicios teatro / secretos / CI vacio.")],
12: [("p95?","95% bajo esa latencia."),("Pitch = P3?","No."),("Bottleneck?","DB/auth/storage.")],
13: [("Horizontal vs vertical?","Mas instancias vs mas recursos."),("Max replicas?","Costo/cascada."),
     ("DB = API?","No necesariamente.")],
15: [("Evidencias minimas?","Diagramas+lab+CI+decisiones."),("PI reemplaza P3?","No."),
     ("AWS obligatorio?","No.")],
}

FUND = {
1: "Arquitectura cloud = componentes+relaciones+despliegue+calidad. CloudLite es el vehiculo practico.",
2: "IaaS/PaaS/SaaS = shared responsibility. ADR documenta trade-offs.",
3: "VM vs contenedor. Labs navegador. Evidencia Dockerfile+captura.",
4: "2-5 contenedores logicos. Contratos etiquetados. Fallos parciales.",
6: "STRIDE-lite del dominio. Secretos fuera de la imagen.",
7: "Zonas Publica/Privada/Datos. Storage segun caso. Nombres=C4.",
8: "CI valida; CD simulado. Golden signals-lite.",
10: "Costo cualitativo B/M/A + sostenibilidad.",
11: "Checkpoint evidencias. No es sustentacion ni P3.",
12: "Metricas + escenario + ensayo pitch. P3 es Clase 14.",
13: "Horizontal/vertical; triggers; lo que no escala.",
15: "Sustentacion con evidencias. PI 20% no sustituye P3.",
}
