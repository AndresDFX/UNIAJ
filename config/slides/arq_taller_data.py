# -*- coding: utf-8 -*-
"""Bloque Taller ampliado + soluciones (PRIVADO) — Arquitectura / CloudLite."""

HERRAMIENTAS_DIA = {
    1: [
        {
            'name': 'Padlet',
            'logo': 'padlet.png',
            'note': 'Rompe-hielo',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'C4 Context',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Boceto rapido',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Ficha PI',
        },
    ],
    2: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'ADR-001',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Matriz modelos',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Boceto',
        },
    ],
    3: [
        {
            'name': 'Killercoda',
            'logo': 'killercoda.png',
            'note': 'Lab contenedores',
        },
        {
            'name': 'LabEx Docker Playground',
            'logo': None,
            'note': 'Sandbox',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Informe PI',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Nota arquitectura',
        },
    ],
    4: [
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'C4 Containers',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Boceto contratos',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Seccion PI',
        },
    ],
    6: [
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Amenazas',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Controles',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Seccion Seguridad',
        },
    ],
    7: [
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Deployment',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Zonas',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Seccion Redes',
        },
    ],
    8: [
        {
            'name': 'GitHub Actions',
            'logo': 'github_actions.png',
            'note': 'CI free',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Monitoreo',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Pipeline conceptual',
        },
    ],
    10: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Costos B/M/A',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Drivers',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Boceto',
        },
    ],
    11: [
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Diagramas v1',
        },
        {
            'name': 'GitHub Actions',
            'logo': 'github_actions.png',
            'note': 'Evidencia CI',
        },
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Informe 60%+',
        },
    ],
    12: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Pitch + metricas',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Arquitectura',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Storyboard',
        },
    ],
    13: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Politica escala',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Nota deploy',
        },
        {
            'name': 'Excalidraw',
            'logo': 'excalidraw.png',
            'note': 'Triggers',
        },
    ],
    15: [
        {
            'name': 'Google Docs',
            'logo': 'google_docs.png',
            'note': 'Paquete final',
        },
        {
            'name': 'draw.io',
            'logo': 'drawio.png',
            'note': 'Diagramas',
        },
        {
            'name': 'GitHub Actions',
            'logo': 'github_actions.png',
            'note': 'Evidencia CI',
        },
    ],
}

TALLER_BLOQUE = {
    1: {
        'contexto': [
            '@@Por qué importa al PI:@@ sin dominio concreto no hay arquitectura que defender.',
            'La ficha + C4 Context son la semilla del informe y de todos los diagramas del semestre.',
            'Si el problema es vago (app de la universidad), el resto del PI se vuelve teatro.',
            'Hoy cierran frontera del sistema + actores externos; Containers internos = Clase 4.',
        ],
        'objetivo': 'Definir dominio CloudLite medible + 3-5 capacidades + boceto C4 Context exportable.',
        'criterios': [
            'Dominio con actor + dolor medible (no genérico).',
            '3-5 capacidades en verbos de negocio.',
            'C4 Context: 1 caja sistema + >=2 actores + >=1 SaaS/sistema externo.',
            'Doc + PNG (o enlace) listos para ExamLab · domingo 23:59.',
        ],
        'escenario': [
            'Actividad individual. Elegir un dominio concreto.',
            'Sugeridos: AgendaU · BiblioLite · InventarioLab · TurnosClinica · EventosCampus.',
            'Plantilla ficha: DOMINIO · PROBLEMA · CAPACIDADES · ACTORES · SISTEMAS EXTERNOS · FUERA DE ALCANCE.',
            'Herramienta: Excalidraw o draw.io (gratis en navegador).',
        ],
        'pistas': [
            '□ Quién sufre el problema y como lo miden?',
            '□ La caja grande es el sistema CloudLite (no un módulo interno)?',
            '□ Las flechas tienen verbo (reservar, notificar, autenticar)?',
            '□ Fuera de alcance está escrito (que NO haran hoy)?',
        ],
    },
    2: {
        'contexto': [
            '@@Por qué importa al PI:@@ el modelo IaaS/PaaS/SaaS define quién opera SO, runtime y costos.',
            'Sin ADR, el PI no puede justificar trade-offs en sustentación ni en parciales.',
            'Restriccion del curso: gratis + navegador; no abrir IaaS con tarjeta.',
        ],
        'objetivo': 'Decidir modelo dominante para CloudLite y documentarlo en ADR-001.',
        'criterios': [
            'Matriz IaaS/PaaS/SaaS vs capacidades del dominio.',
            'ADR con contexto, decisión, >=2 alternativas y consecuencias +/-.',
            'Integrado a la sección Modelo de servicio del informe.',
            'Entrega domingo 23:59 (clase autónoma).',
        ],
        'escenario': [
            'Partir de la ficha/C4 de Clase 1 (mismo dominio).',
            'MVP académico típico: PaaS conceptual + SaaS satélite (auth/email).',
            'Documentar en Google Docs; diagrama opcional de responsabilidad compartida.',
        ],
        'pistas': [
            '□ La decisión nombra un modelo dominante (no un poco de todo)?',
            '□ Hay al menos dos alternativas descartadas con razón?',
            '□ Consecuencias incluyen operación, costo y aprendizaje?',
        ],
    },
    3: {
        'contexto': [
            '@@Por qué importa al PI:@@ CloudLite debe mostrar al menos un servicio contenerizado con evidencia.',
            'El contenedor es el puente entre el diagrama C4 y el despliegue realista (sin cloud de pago).',
            'Labs en navegador (LabEx Docker Playground / Killercoda): sin Docker Desktop obligatorio.',
        ],
        'objetivo': 'Contenerizar un stub HTTP del servicio principal y dejar Dockerfile + captura.',
        'criterios': [
            'Dockerfile legible (imagen slim, EXPOSE, CMD).',
            'Stub responde en / o /health.',
            'Captura o enlace de sesión lab (o plan B si caduca).',
            'Sección Contenedores del informe actualizada.',
        ],
        'escenario': [
            'Elegir el servicio principal del C4 (API o web).',
            'Abrir LabEx Docker Playground (labex.io, login con Google/Microsoft) o Killercoda; sesión temporal.',
            'Prohibido: copiar .env / API keys a la imagen.',
        ],
        'pistas': [
            '□ El puerto expuesto coincide con el que documentan?',
            '□ Hay evidencia con timestamp (captura o enlace)?',
            '□ Secretos fuera de la imagen?',
        ],
    },
    4: {
        'contexto': [
            '@@Por qué importa al PI:@@ el C4 Containers es el mapa lógico que luego alinea Deployment y CI.',
            'Anti-patrón: 12 microservicios para 3 estudiantes = teatro, no arquitectura.',
            'Regla CloudLite: 2-5 cajas justificadas + contratos etiquetados.',
        ],
        'objetivo': 'Diagramar Containers CloudLite (2-5) + 3 contratos API mínimos.',
        'criterios': [
            'Cada caja: nombre + responsabilidad + tech tentativa.',
            'Flechas con protocolo + verbo de negocio.',
            '3 contratos: in/out/errores (ej. 401/409).',
            'Export PNG + .drawio al paquete PI.',
        ],
        'escenario': [
            'Partir del C4 Context (mismos nombres de sistema/actores).',
            'draw.io o Excalidraw; vista Containers (no solo Context).',
            'Contratos en Doc o notas junto al diagrama.',
        ],
        'pistas': [
            '□ Hay 2-5 cajas (no 1 monolito innominado ni 12 microservicios)?',
            '□ Los nombres coincidirán luego con Deployment?',
            '□ Cada contrato tiene error de negocio (ej. 409 conflicto)?',
        ],
    },
    6: {
        'contexto': [
            '@@Por qué importa al PI:@@ seguridad = amenazas del dominio + controles visibles.',
            'Si la API key está en el Dockerfile, ya filtraron el secreto.',
            'STRIDE-lite: 5 amenazas concretas, no lista generica de internet.',
        ],
        'objetivo': 'Modelo de amenazas mínimo + controles + política de secretos para CloudLite.',
        'criterios': [
            '5 amenazas del dominio (STRIDE-lite) con control y evidencia.',
            'Política de secretos (media página).',
            'Sección Seguridad 1-1.5 páginas en el informe.',
            'Controles reflejados en diagrama (HTTPS, trust boundary, etc.).',
        ],
        'escenario': [
            'Usar dominio y Containers ya definidos.',
            'Amenazas tipicas: secrets en imagen, API sin auth, logs con tokens, PII sin TLS.',
            'Herramientas: Excalidraw + Google Docs.',
        ],
        'pistas': [
            '□ Cada amenaza tiene control + donde se ve en el diagrama?',
            '□ Secretos en Settings/Actions, no en Dockerfile?',
            '□ Least privilege aparece aunque sea narrado?',
        ],
    },
    7: {
        'contexto': [
            '@@Por qué importa al PI:@@ sin zonas, el Deployment no demuestra fronteras de confianza.',
            'Si la BD está en zona pública, el diagrama ya falló.',
            'Nombres del Deployment deben = nombres del C4 Containers.',
        ],
        'objetivo': 'Deployment CloudLite: zonas + storage conceptual etiquetado.',
        'criterios': [
            'Zonas Pública / Privada / Datos (o equivalentes claros).',
            'Puertos y almacenes etiquetados.',
            'Eleccion de storage (DB + object si aplica) justificada.',
            'Sección Redes y almacenamiento en el informe.',
        ],
        'escenario': [
            'Cliente -> edge -> app -> datos.',
            'Sin inventar subnets AWS; trust boundaries si.',
            'draw.io como herramienta principal.',
        ],
        'pistas': [
            '□ La BD está en zona de datos/privada?',
            '□ Mismos nombres que el C4?',
            '□ Object storage solo si el dominio lo necesita?',
        ],
    },
    8: {
        'contexto': [
            '@@Por qué importa al PI:@@ CI que solo hace echo success no es CI.',
            'GitHub Actions free = evidencia de build/test sin tarjeta.',
            'Observabilidad: 4-6 métricas atadas al dominio (golden signals-lite).',
        ],
        'objetivo': 'Workflow Actions (build/test + deploy simulado) + plan de monitoreo.',
        'criterios': [
            '.github/workflows/ci.yml con pasos reales (o YAML serio + explicación).',
            'Deploy simulado (artifact/echo) documentado.',
            '4-6 métricas (latencia, errores, tráfico, saturacion).',
            'Secciónes CI/CD y Monitoreo en el informe.',
        ],
        'escenario': [
            'Repo free + stub de Clase 3 (o mínimo).',
            'Secrets en Settings; nunca en el YAML en claro.',
            'Captura de run verde o YAML + explicación si no corre.',
        ],
        'pistas': [
            '□ Hay build o test real (no solo echo vacío)?',
            '□ Secrets fuera del repositorio?',
            '□ Métricas con umbral u objetivo narrado?',
        ],
    },
    10: {
        'contexto': [
            '@@Por qué importa al PI:@@ lo más caro suele ser lo que dejan encendido sin usar.',
            'Costo cualitativo B/M/A es aceptable: no inventar precios USD de cloud de pago.',
            'Sostenibilidad: slim + labs temporales + right-sizing.',
        ],
        'objetivo': 'Sección Costos/Sostenibilidad del PI con tabla por componente.',
        'criterios': [
            'Tabla componente -> driver -> B/M/A -> apalancamiento.',
            '>=3 acciones de sostenibilidad verificables.',
            '1 página integrada al informe.',
            'Entrega domingo 23:59 (autónoma).',
        ],
        'escenario': [
            'Componentes: API, DB, object, CI, edge.',
            'Drivers: idle, egress, storage, minutos CI.',
            'Google Docs como herramienta principal.',
        ],
        'pistas': [
            '□ Cada fila tiene driver (no solo caro)?',
            '□ Las 3 acciones son verificables en el PI?',
            '□ Evitaron inventar facturas de AWS/GCP?',
        ],
    },
    11: {
        'contexto': [
            '@@Por qué importa al PI:@@ checkpoint v1 = integrar evidencias; no es sustentación ni Parcial 3.',
            'Si C4 y Deployment no comparten nombres, el PI esta roto.',
            'Hoy cierran huecos con checklist viva + backlog a Clase 12.',
        ],
        'objetivo': 'Paquete v1 CloudLite: diagramas + Dockerfile + Actions + informe 60%+.',
        'criterios': [
            'Checklist si/no/parcial con enlaces a evidencias.',
            'Nombres unificados C4 <-> Deployment.',
            'ZIP/repo con evidencias + backlog 5 items.',
            'Feedback docente incorporado o anotado.',
        ],
        'escenario': [
            'Revisar: dominio, ADR, C4, Deployment, Dockerfile, Actions, Seguridad, Costos.',
            'Demo corta por estudiante (o por equipo, si el docente los autorizo) si el tiempo alcanza.',
        ],
        'pistas': [
            '□ Cada si tiene enlace o ruta de archivo?',
            '□ Hay backlog priorizado (no lista infinita)?',
            '□ Anti-patrónes (teatro microservicios / secretos / CI vacío) marcados?',
        ],
    },
    12: {
        'contexto': [
            '@@Por qué importa al PI:@@ sin métrica objetivo, rápido es opinion — no arquitectura.',
            'Ensayo de pitch 5-8 min reduce riesgo en la sustentación (Clase 15).',
            'Parcial 3 es Clase 14 (solo evaluación); hoy preparan evidencias.',
        ],
        'objetivo': 'Escenario de rendimiento + ensayo pitch + paquete casi-final.',
        'criterios': [
            'Escenario de carga con 3 métricas + bottleneck.',
            'Pitch cronometrado 5-8 min (en equipo autorizado, hablan todos).',
            'Backlog de Clase 11 cerrado o residual explícito.',
            'Paquete casi-final ordenado.',
        ],
        'escenario': [
            'Pico del dominio (ej. inicio de semestre / dia de citas).',
            'Demo permitida: diagrama + captura lab/Actions — no K8s de pago.',
        ],
        'pistas': [
            '□ p95 / error rate / RPS tienen número u orden de magnitud?',
            '□ Bottleneck nombrado (DB/auth/storage)?',
            '□ Guion de pitch con tiempos por sección?',
        ],
    },
    13: {
        'contexto': [
            '@@Por qué importa al PI:@@ escalar la API no escala sola la base de datos.',
            'Política de autoescalado conceptual = evidencia de diseño (sin cloud de pago).',
            'Definir que NO escala evita promesas imposibles en sustentación.',
        ],
        'objetivo': 'Sección Escalabilidad: triggers, min/max, que escala y que no.',
        'criterios': [
            'Horizontal vs vertical aplicado al dominio.',
            '>=2 triggers + min/max + cooldown narrado.',
            'Lo que NO escala justificado (ej. DB primaria).',
            'Nota opcional en Deployment + entrega domingo 23:59.',
        ],
        'escenario': [
            'Plantilla: componente, tipo, trigger up/down, min/max, cooldown.',
            'Impacto en costo cualitativo (enlace a Clase 10).',
        ],
        'pistas': [
            '□ Triggers medibles (RPS, p95, cola)?',
            '□ Hay techo (max) para no escalar infinito?',
            '□ DB/sesión sticky justificados como no-escalables?',
        ],
    },
    15: {
        'contexto': [
            '@@Por qué importa al PI:@@ sustentación = evidencias + decisiónes, no tour de logos.',
            'PI 20% Corte 3 no sustituye el Parcial 3 (ya ocurrio en Clase 14).',
            'Paquete final ordenado facilita la calificación con rúbrica.',
        ],
        'objetivo': 'Entregar paquete final + pitch 5-8 min + Q&A escrito.',
        'criterios': [
            'ZIP/PDF en ExamLab con diagramas + lab + CI + informe.',
            'Pitch 5-8 min: individual, o con todos los integrantes si el docente autorizo equipo.',
            'Q&A escrito 3+3 + reflexión 1/2 página.',
            'Autoevaluación breve del proceso.',
        ],
        'escenario': [
            'Orden del pitch: problema -> arquitectura -> contenedor/CI -> seguridad/costos/escala -> Q&A.',
            'Sin AWS/GCP obligatorio.',
        ],
        'pistas': [
            '□ Evidencias minimas presentes (diagramas + lab + CI + decisiónes)?',
            '□ Tiempos del pitch ensayados?',
            '□ PI y Parcial 3 no se confunden en el discurso?',
        ],
    },
}

SOLUCION = {
    1: {
        'titulo': 'Solución Taller Clase 1 — Ficha + C4 Context CloudLite',
        'resumen': 'Ejemplo aceptable (AgendaU). Actividad individual. Otros dominios válidos si cumplen criterios.',
        'pasos': [
            'Actividad individual. Dominio: AgendaU (tutorías estudiante-docente).',
            'Problema: estudiantes pierden turnos por doble agenda y recordatorios débiles.',
            'Capacidades: reservar, cancelar, recordar, ver disponibilidad.',
            'Actores: Estudiante, Tutor; sistemas externos: proveedor de identidad, correo/calendario.',
            'C4 Context exportable PNG + .drawio.',
        ],
        'ejemplo': [
            'DOMINIO: AgendaU',
            'PROBLEMA: pérdida de turnos por solapamientos y falta de recordatorio.',
            'CAPACIDADES: reservar, cancelar, listar disponibilidad, notificar.',
            'ACTORES: Estudiante, Tutor.',
            'SISTEMAS EXTERNOS: proveedor de identidad institucional (login), correo/calendario SaaS (recordatorios).',
            'FUERA DE ALCANCE: pagos, videollamada, app nativa.',
            'C4: CloudLite App <-HTTPS-> personas; CloudLite ->SMTP-> correo SaaS; CloudLite ->OIDC-> proveedor de identidad.',
        ],
        'rubrica': [
            'Dominio concreto (2)',
            'Capacidades+actores (2)',
            'Sistemas externos coherentes con el C4 (1)',
            'C4 correcto (3)',
            'Evidencia+entrega (1)',
            'Fuera de alcance (1)',
        ],
        'errores': [
            'Rechazar dominio vago sin actor/métrica.',
            'No pedir Containers internos hoy.',
            'C4 sin flechas.',
            'Ficha con bloque EQUIPO cuando el docente no autorizo equipos: la actividad es individual por defecto y solo admite lenguaje de equipo si hubo autorizacion.',
        ],
    },
    2: {
        'titulo': 'Solución Taller Clase 2 — ADR-001',
        'resumen': 'Decisión tipica: PaaS conceptual + SaaS satélite.',
        'pasos': [
            'Matriz IaaS/PaaS/SaaS vs capacidades.',
            'Decisión: PaaS conceptual API/web; SaaS email/auth.',
            'Alternativas: IaaS puro (tarjeta/ops); SaaS total (poco control).',
            'ADR-001 en Docs + sección informe.',
        ],
        'ejemplo': [
            'Título: Modelo de servicio dominante CloudLite',
            'Decisión: PaaS conceptual + contenedores lab; SaaS email',
            'Estado: Aceptada',
        ],
        'rubrica': [
            'Matriz (2)',
            'Decisión (2)',
            'Alternativas (3)',
            'Consecuencias (2)',
            'Informe (1)',
        ],
        'errores': [
            'Un poco de todo sin dominante.',
            'AWS con tarjeta como requisito.',
        ],
    },
    3: {
        'titulo': 'Solución Taller Clase 3 — Stub contenerizado',
        'resumen': 'Dockerfile mínimo + evidencia lab navegador.',
        'pasos': [
            'Servicio api-reservas.',
            'Dockerfile slim+EXPOSE+CMD.',
            'Stub /health 200.',
            'Captura timestamp + sección Contenedores.',
        ],
        'ejemplo': [
            'FROM python:3.12-slim',
            'WORKDIR /app',
            'COPY app.py .',
            'EXPOSE 8080',
            'CMD ["python","app.py"]',
        ],
        'rubrica': [
            'Dockerfile (3)',
            'HTTP stub (2)',
            'Evidencia (3)',
            'Sin secretos (1)',
            'Informe (1)',
        ],
        'errores': [
            'Keys en imagen.',
            'Sin captura ni archivo.',
        ],
    },
    4: {
        'titulo': 'Solución Taller Clase 4 — C4 Containers + contratos',
        'resumen': 'Ejemplo 3 contenedores: web, api, db.',
        'pasos': [
            'Containers WebApp, ApiReservas, DbAgenda.',
            'Flechas HTTPS/SQL/SMTP etiquetadas.',
            '3 contratos API con errores.',
            'Export PNG+.drawio.',
        ],
        'ejemplo': [
            'POST /api/reservas — 401/409',
            'DELETE /api/reservas/{id} — 404/403',
            'GET /api/disponibilidad — 400',
        ],
        'rubrica': [
            '2-5 cajas (3)',
            'Flechas (2)',
            'Contratos (3)',
            'Export+informe (2)',
        ],
        'errores': [
            '12 microservicios teatro.',
            'Nombres distintos al Context.',
        ],
    },
    6: {
        'titulo': 'Solución Taller Clase 6 — STRIDE-lite',
        'resumen': '5 amenazas del dominio + política secretos.',
        'pasos': [
            '5 amenazas STRIDE-lite.',
            'Control en diagrama.',
            'Política secretos media página.',
            'Sección Seguridad 1-1.5 pag.',
        ],
        'ejemplo': [
            'Spoofing->tokens+HTTPS',
            'Tampering->authz+audit',
            'Disclosure->TLS',
            'DoS-lite->rate-limit',
            'Elevation->least privilege',
        ],
        'rubrica': [
            '5 amenazas (3)',
            'Control+evidencia (3)',
            'Política secretos (2)',
            'Informe (2)',
        ],
        'errores': [
            'Lista generica.',
            'Keys en imagen/README.',
        ],
    },
    7: {
        'titulo': 'Solución Taller Clase 7 — Deployment zonas',
        'resumen': 'Pública/Privada/Datos; DB no pública.',
        'pasos': [
            'Zonas + colocación servicios.',
            'Puertos etiquetados.',
            'Storage justificado.',
            'Nombres=C4.',
        ],
        'ejemplo': [
            'Pública: WebApp',
            'Privada: ApiReservas',
            'Datos: DbAgenda',
            'Object opcional PDF',
        ],
        'rubrica': [
            'Zonas (3)',
            'DB no pública (2)',
            'Nombres=C4 (2)',
            'Storage (2)',
            'Informe (1)',
        ],
        'errores': [
            'DB en zona pública.',
            'Subnets AWS inventadas.',
        ],
    },
    8: {
        'titulo': 'Solución Taller Clase 8 — Actions + monitoreo',
        'resumen': 'ci.yml build/test + deploy simulado + 4 métricas.',
        'pasos': [
            'Repo+stub.',
            'ci.yml checkout->build/test->artifact.',
            '4-6 métricas golden signals-lite.',
            'Captura o YAML+explicación.',
        ],
        'ejemplo': [
            'name: ci',
            'on: [push]',
            'jobs.build.runs-on: ubuntu-latest',
            'steps: checkout + build-and-test + deploy-simulated',
        ],
        'rubrica': [
            'YAML (3)',
            'Build/test serio (2)',
            'Métricas (3)',
            'Evidencia (2)',
        ],
        'errores': [
            'Solo echo vacío.',
            'Secrets en claro.',
        ],
    },
    10: {
        'titulo': 'Solución Taller Clase 10 — Costos B/M/A',
        'resumen': 'Tabla cualitativa + 3 acciones sostenibilidad.',
        'pasos': [
            'Filas API/DB/Object/CI/Edge.',
            'Drivers idle/egress/storage/CI.',
            '3 acciones slim/labs/right-size.',
            '1 página informe.',
        ],
        'ejemplo': [
            'API idle Medio',
            'DB storage Medio',
            'CI minutos Bajo',
            'Acciones: slim + labs off + right-size',
        ],
        'rubrica': [
            'Tabla (4)',
            '3 acciones (3)',
            'Sin USD inventados (2)',
            'Integrado (1)',
        ],
        'errores': [
            'Factura AWS inventada.',
            'Sera barato sin tabla.',
        ],
    },
    11: {
        'titulo': 'Solución Taller Clase 11 — Checkpoint v1',
        'resumen': 'Checklist con enlaces + backlog 5.',
        'pasos': [
            'Marcar si/no/parcial con enlaces.',
            'Unificar nombres.',
            'ZIP/repo + backlog top-5.',
        ],
        'ejemplo': [
            'C4 OK',
            'Deployment Parcial (renombrar)',
            'Actions Parcial (falta test)',
            'Backlog: test CI, secretos en diagrama, p95',
        ],
        'rubrica': [
            'Checklist+evidencia (4)',
            'Nombres (2)',
            'Paquete (2)',
            'Backlog (2)',
        ],
        'errores': [
            'Todo si sin enlaces.',
            'Tratar como sustentación final.',
        ],
    },
    12: {
        'titulo': 'Solución Taller Clase 12 — Rendimiento + pitch',
        'resumen': 'Escenario pico + guion pitch 5-8 min.',
        'pasos': [
            'Escenario con 3 métricas + bottleneck.',
            'Ensayo pitch con tiempos.',
            'Cerrar backlog.',
        ],
        'ejemplo': [
            'RPS pico 50; p95 800ms; error 1%',
            'Bottleneck: disponibilidad DB',
            'Pitch: 1+2+1+1+1-2 min',
        ],
        'rubrica': [
            'Escenario+métricas (3)',
            'Bottleneck (2)',
            'Pitch (3)',
            'Paquete (2)',
        ],
        'errores': [
            'Rapido sin números.',
            'Load test de pago obligatorio.',
        ],
    },
    13: {
        'titulo': 'Solución Taller Clase 13 — Autoescalado',
        'resumen': 'API horizontal; DB no escala igual.',
        'pasos': [
            'Política API min/max/triggers.',
            'NO escala: DB primaria.',
            'Nota costo.',
            'Sección Escalabilidad.',
        ],
        'ejemplo': [
            'ApiReservas H RPS>40 min1 max4',
            'DbAgenda no auto 1/1',
        ],
        'rubrica': [
            'Política (4)',
            'NO escala (3)',
            'Costo (2)',
            'Entrega (1)',
        ],
        'errores': [
            'Escalar DB=API.',
            'Sin techo max.',
        ],
    },
    15: {
        'titulo': 'Solución Taller Clase 15 — Paquete + sustentación',
        'resumen': 'Checklist empaquetado + orden pitch.',
        'pasos': [
            'ZIP completo.',
            'Pitch 5-8 min.',
            'Q&A 3+3 + reflexión.',
        ],
        'ejemplo': [
            '/informe.pdf',
            '/diagramas/*.png',
            '/lab/Dockerfile+captura',
            '/ci/ci.yml+run.png',
            '/anexos/adr+qna',
        ],
        'rubrica': [
            'Paquete (4)',
            'Pitch (3)',
            'Q&A+reflexión (2)',
            'PI!=P3 (1)',
        ],
        'errores': [
            'Tour de logos.',
            'Falta lab o CI.',
        ],
    },
}
