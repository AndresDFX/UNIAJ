# -*- coding: utf-8 -*-
"""Genera material Clases 1–15 · Arquitectura (UNIAJC 2026-2) con enfoque PI CloudLite App.

Por clase regular/autónoma:
  - Clases/Clase N - <Tema>/Presentacion.pptx + Taller ….docx
  - Kit docente/Clase N/Guion….md (+ .docx vía guion_md_a_docx) + Quiz….docx + Capturas/
Días de parcial (5, 9, 14): solo guía breve en Kit (enunciados ya en Parciales/).

Enfoque: teoría breve al servicio del PI; talleres = avance de entregables CloudLite.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uniajc_slides_engine import (  # noqa: E402
    before_after_slide,
    box_note_slide,
    closing_slide,
    content_slide,
    new_prs,
    pseudo_code_slide,
    table_content,
)
from uniajc_slides_engine import (  # noqa: E402
    AMARILLO,
    CONTENT_W,
    CIAN,
    GRAY,
    MARGIN,
    MSO_ANCHOR,
    NAVY,
    PP_ALIGN,
    Pt as EPt,
    SW,
    WHITE,
    _rich,
    _run,
    add_logo,
    bg_white,
    blank,
    diagram_boxes_slide,
    footer_num,
    rect,
    textbox,
)

ROOT = Path(__file__).resolve().parents[2]
CURSO = ROOT / "Arquitectura de Sistemas Computacionales"
SLIDES_DIR = Path(__file__).resolve().parent

AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN_D = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
ROJO = RGBColor(0xA0, 0x20, 0x30)
FONT = "Calibri"

# ---------------------------------------------------------------------------
# Catálogo de clases (Plan 2026-2) — PI-first
# ---------------------------------------------------------------------------

CLASSES = [
    {
        "n": 1,
        "tipo": "regular",
        "slug": "Introduccion a arquitecturas cloud",
        "tema": "Introducción a arquitecturas cloud",
        "sub": "Diagnóstico · CloudLite App · primer boceto",
        "pi_hoy": "Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases",
        "entregable": "Ficha PI: dominio, capacidades, actores y boceto C4 Context (Excalidraw/draw.io)",
        "herramienta": "Padlet · Excalidraw / draw.io",
        "objetivos": [
            "Ubicar el curso como diseño de arquitecturas cloud al servicio del **PI CloudLite App**.",
            "Distinguir nube vs on-prem y los bloques de una arquitectura cloud simple.",
            "Dejar el **dominio y alcance** del PI escritos y compartibles.",
        ],
        "slides_extra": [
            ("Qué es arquitectura cloud (mapa mental)", [
                "@@Arquitectura@@ = componentes + relaciones + despliegue + calidad (seguridad, escala, costo).",
                "Cloud: recursos **bajo demanda**, multi-tenant, API/automatización.",
                "Para CloudLite App: no «comprar servidores»; **diseñar** capas y simular en labs gratis.",
                "Bloques tipicos: cliente → API → lógica → datos → observabilidad.",
            ]),
            ("CloudLite App — el hilo conductor", [
                "Aplicación web/API de un dominio realista (citas, academia, inventario liviano…).",
                "Entregables del semestre: diagramas + contenedor (lab) + CI/CD conceptual + informe.",
                "Hoy solo: **problema + capacidades + boceto de contexto**.",
                "Sin AWS/GCP/Oracle: draw.io, Play with Docker, GitHub Actions.",
            ]),
            ("De dominio a arquitectura (mini-método)", [
                "1) Actor y problema. 2) Capacidades. 3) Contenedores lógicos. 4) Datos. 5) Riesgos.",
                "Ejemplo: *AgendaU* — estudiantes reservan tutoría; API + auth + agenda + notificaciones.",
                "Pregunta de diseño: ¿qué es **núcleo** vs satélite?",
                "Salida: diagrama C4 Context (sistema + actores externos).",
            ]),
        ],
        "taller_titulo": "Taller Clase 1 — Ficha y boceto CloudLite App",
        "taller_pasos": [
            "Formen equipo de 2–3 (o individual autorizado).",
            "Elijan dominio concreto (no «red social genérica»).",
            "Escriban: problema (2–3 frases), 3–5 capacidades, 2–3 actores.",
            "En Excalidraw o draw.io: diagrama **C4 Context** (CloudLite + actores + sistemas externos).",
            "Entrega en **ExamLab** (Talleres): Doc/enlace con ficha + PNG del diagrama (domingo 23:59).",
        ],
        "quiz": [
            ("¿Qué diferencia principal hay entre «tener un servidor en un cuarto» y un diseño cloud?",
             "Cloud: recursos elásticos/automatizados bajo demanda; on-prem: capacidad fija y operación local."),
            ("Nombre dos entregables del PI CloudLite App.",
             "Cualquiera de: diagramas C4/despliegue, lab contenedores, workflow Actions, informe, sustentación."),
            ("¿Por qué el curso prohíbe pedir AWS/GCP con tarjeta?",
             "Política gratis+navegador; el estudiante no asume costos ni tarjeta."),
        ],
    },
    {
        "n": 2,
        "tipo": "autonoma",
        "slug": "Modelos de servicio IaaS PaaS SaaS",
        "tema": "Modelos de servicio: IaaS, PaaS, SaaS",
        "sub": "Actividad autónoma · ADR del PI",
        "pi_hoy": "Decidir modelo dominante (IaaS/PaaS/SaaS) para CloudLite + ADR breve",
        "entregable": "ADR-001: decisión de modelo de servicio + matriz de comparación aplicada al dominio",
        "herramienta": "Google Docs · draw.io (opcional)",
        "objetivos": [
            "Comparar IaaS, PaaS y SaaS con criterios de control, operación y velocidad.",
            "Elegir el **modelo dominante** de CloudLite con justificación.",
            "Documentar la decisión como **ADR** reutilizable en el informe PI.",
        ],
        "slides_extra": [
            ("IaaS · PaaS · SaaS (sin cloud de pago)", [
                "@@IaaS@@: usted administra SO/red/runtime; el proveedor da cómputo/red/disco.",
                "@@PaaS@@: usted despliega app; el proveedor gestiona runtime/escala básica.",
                "@@SaaS@@: consume el servicio listo (correo, CRM); poca personalización profunda.",
                "En este curso **simulamos** con labs/navegador; no abrimos cuentas IaaS con tarjeta.",
            ]),
            ("Cómo decidir para CloudLite", [
                "Pregunte: ¿necesito controlar red/SO o solo desplegar API+datos?",
                "Para un MVP académico suele ganar **PaaS conceptual** + contenedores (portable).",
                "Si el dominio exige mucho control de red → justifique IaaS *simulado* en diagrama.",
                "SaaS solo como **satélite** (auth, email, analytics) — no como toda la app.",
            ]),
            ("Plantilla ADR-001", [
                "Contexto · Decisión · Alternativas · Consecuencias · Riesgos.",
                "Máximo 1 página. Lenguaje de arquitectura, no marketing.",
                "Debe citar 2 trade-offs (ej.: control vs velocidad de entrega).",
            ]),
        ],
        "taller_titulo": "Actividad autónoma Clase 2 — ADR modelo de servicio CloudLite",
        "taller_pasos": [
            "Lea las diapositivas y el enunciado del PI (Clases/Proyecto Integrador).",
            "Complete una matriz IaaS/PaaS/SaaS vs su dominio (control, costo cualitativo, operación, time-to-demo).",
            "Redacte ADR-001 (decisión dominante + 2 alternativas descartadas).",
            "Actualice el informe PI (sección «Modelo de servicio»).",
            "Entrega domingo 23:59 en **ExamLab** (Talleres) — mismo doc del PI o anexo.",
        ],
        "quiz": [
            ("Si solo despliega código y el proveedor gestiona el runtime, ¿qué modelo es?", "PaaS."),
            ("¿SaaS puede ser el modelo dominante de CloudLite App? ¿Cuándo sí/no?",
             "Rara vez como dominante (poca personalización); sí como servicios satélite."),
            ("¿Qué es un ADR?", "Architecture Decision Record: documenta una decisión y sus trade-offs."),
        ],
    },
    {
        "n": 3,
        "tipo": "regular",
        "slug": "Virtualizacion y contenedores",
        "tema": "Virtualización y contenedores",
        "sub": "Lab Play with Docker → stub CloudLite",
        "pi_hoy": "Contenerizar un stub del servicio principal de CloudLite",
        "entregable": "Dockerfile (+ compose opcional) + captura/enlace lab navegador",
        "herramienta": "Play with Docker (PWD) · alterna si no carga: Killercoda",
        "objetivos": [
            "Diferenciar VM vs contenedor y el rol de la imagen.",
            "Ejecutar un contenedor en lab de **navegador** (sin Docker Desktop obligatorio).",
            "Dejar evidencia PI: Dockerfile del stub CloudLite + captura.",
        ],
        "slides_extra": [
            ("VM vs contenedor", [
                "VM: hipervisor + SO completo → aislamiento fuerte, más pesado.",
                "Contenedor: comparte kernel del host → portable y rápido para demos.",
                "Imagen = capas inmutables; contenedor = instancia en ejecución.",
                "CloudLite: contenerizamos al menos **un** servicio (API stub o front estático).",
            ]),
            ("Lab en navegador (pasos demo)", [
                "Abrir Play with Docker (labs.play-with-docker.com) → Add new instance.",
                "`docker run` de un nginx/hello y luego **su** imagen stub.",
                "📸 [CAP: pwd-home] Home del lab · 📸 [CAP: docker-ps] `docker ps`.",
                "Sesion de PWD dura 4h y se autodestruye: guardar Dockerfile + capturas con timestamp antes de que expire. Si PWD esta caido: Killercoda (ubuntu/docker) como alterna.",
            ]),
            ("Dockerfile mínimo para el stub", [
                "FROM imagen base ligera → COPY → EXPOSE → CMD.",
                "No secretos en la imagen. Un proceso principal por contenedor (regla práctica).",
                "Compose (opcional): API + fake DB solo si aporta al diagrama.",
            ]),
        ],
        "taller_titulo": "Taller Clase 3 — Contenedor stub CloudLite",
        "taller_pasos": [
            "Definan qué servicio contenerizan hoy (API stub o front estático del dominio).",
            "En Play with Docker: construyan y corran el contenedor (si no carga, Killercoda como alterna).",
            "Documenten Dockerfile (y compose si aplica) en el repo/ZIP del PI.",
            "Capturen evidencia (PNG) o enlace de sesión + nota de caducidad.",
            "Actualicen informe: sección Contenedores + enlace a diagrama de despliegue futuro.",
        ],
        "quiz": [
            ("¿Qué comparte un contenedor con el host que una VM típicamente no comparte?", "El kernel del SO."),
            ("Nombre la herramienta de lab principal del curso para contenedores.", "Play with Docker (alterna: Killercoda)."),
            ("¿Por qué no poner secretos en el Dockerfile?", "Quedan en capas/historial de la imagen."),
        ],
    },
    {
        "n": 4,
        "tipo": "regular",
        "slug": "Microservicios y arquitecturas distribuidas",
        "tema": "Microservicios · Arquitecturas distribuidas",
        "sub": "C4 Componentes CloudLite",
        "pi_hoy": "Diagramar componentes/servicios de CloudLite y sus contratos",
        "entregable": "Diagrama C4 Container/Componentes v0.9 + lista de APIs entre servicios",
        "herramienta": "draw.io / diagrams.net",
        "objetivos": [
            "Contrastar monolito vs microservicios con criterios de equipo y acoplamiento.",
            "Modelar CloudLite en **C4 Container/Componentes** sin exceso de servicios.",
            "Definir 3 contratos/API entre partes del sistema.",
        ],
        "slides_extra": [
            ("Monolito vs microservicios (para el PI)", [
                "Monolito modular ≠ malo: a menudo mejor para equipos pequeños.",
                "Microservicio: frontera de **despliegue** e independencia de datos (ideal).",
                "Anti-patrón: 12 microservicios para 3 estudiantes = diagrama teatro.",
                "Regla CloudLite: 2–5 contenedores lógicos con razón clara.",
            ]),
            ("C4-lite en draw.io", [
                "Context (ya) → Containers → Components (si aporta).",
                "Cada caja: nombre + responsabilidad + tecnología tentativas.",
                "Flechas = protocolos (HTTPS/REST, eventos). Evite «líneas mágicas».",
                "📸 [CAP: drawio-c4] Lienzo C4 de CloudLite.",
            ]),
            ("Distribuido implica fallos", [
                "Latencia, reintentos, idempotencia, timeouts — anótenlos como riesgos PI.",
                "Consistencia eventual vs fuerte: elijan según el dominio (citas ≠ likes).",
                "Hoy no implementan saga completa: solo **reconocen** el trade-off en el informe.",
            ]),
        ],
        "taller_titulo": "Taller Clase 4 — C4 componentes CloudLite",
        "taller_pasos": [
            "Abran draw.io y creen diagrama Containers/Componentes de CloudLite.",
            "Limiten a 2–5 servicios/contenedores lógicos justificados.",
            "Listen 3 contratos (quién llama a quién, verbo HTTP o evento).",
            "Exporten PNG + archivo .drawio al Drive/repo del PI.",
            "En el informe: sección «Arquitectura lógica» + riesgos de distribución.",
        ],
        "quiz": [
            ("¿Cuándo preferiría un monolito modular en CloudLite?",
             "Equipo pequeño, dominio acotado, menos overhead operativo."),
            ("¿Qué debe etiquetar una flecha en C4?", "Protocolo/contrato, no solo «usa»."),
            ("Cite un riesgo de sistemas distribuidos.", "Latencia, particiones, inconsistencia, reintentos…"),
        ],
    },
    {
        "n": 5,
        "tipo": "parcial",
        "slug": "Parcial 1",
        "tema": "Parcial 1",
        "sub": "Solo evaluación",
        "pi_hoy": "Sin avance dirigido de PI (día solo evaluación)",
        "entregable": "—",
        "herramienta": "—",
        "objetivos": ["Evaluar RAA1–intro RAA2 (cloud, modelos, virtualización, distribuidos)."],
        "slides_extra": [],
        "taller_titulo": "",
        "taller_pasos": [],
        "quiz": [],
    },
    {
        "n": 6,
        "tipo": "regular",
        "slug": "Seguridad en la nube",
        "tema": "Seguridad en la nube",
        "sub": "Amenazas y controles → sección PI",
        "pi_hoy": "Modelo de amenazas mínimo + controles para CloudLite",
        "entregable": "Sección Seguridad PI: 5 amenazas STRIDE-lite + controles + secretos/CI",
        "herramienta": "Excalidraw · Google Docs",
        "objetivos": [
            "Aplicar un modelo de amenazas simple al dominio CloudLite.",
            "Mapear controles (authn/z, secretos, superficie de red) sin cloud de pago.",
            "Dejar la sección Seguridad del informe lista en borrador.",
        ],
        "slides_extra": [
            ("Amenazas que sí importan al PI", [
                "Credenciales en repo · APIs abiertas · datos PII sin cifrado en tránsito.",
                "STRIDE-lite: Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation.",
                "Elijan 5 amenazas **del dominio**, no genéricas de Internet.",
            ]),
            ("Controles prácticos (gratis)", [
                "HTTPS en diagrama · tokens/JWT conceptual · least privilege en roles.",
                "Secretos: variables de entorno / GitHub Actions secrets (no en Dockerfile).",
                "Superficie: qué puertos expone el contenedor del lab.",
            ]),
            ("Ejercicio guiado", [
                "Amenaza → activo → control → evidencia en diagrama/informe.",
                "Ej.: Spoofing de API → tokens → caja Auth en C4.",
            ]),
        ],
        "taller_titulo": "Taller Clase 6 — Seguridad CloudLite",
        "taller_pasos": [
            "Listen 5 amenazas STRIDE-lite aplicadas a su dominio.",
            "Para cada una: control + dónde se ve en el diagrama.",
            "Definan política de secretos del repo/Actions.",
            "Redacten sección Seguridad del informe PI (1–1.5 páginas).",
            "Entrega domingo 23:59 (avance PI).",
        ],
        "quiz": [
            ("¿Por qué no hardcodear API keys en el Dockerfile?", "Quedan en la imagen y el historial."),
            ("Nombre un control frente a spoofing de API.", "Autenticación con tokens/credenciales + HTTPS."),
            ("¿Qué es least privilege?", "Dar solo los permisos mínimos necesarios a cada rol/servicio."),
        ],
    },
    {
        "n": 7,
        "tipo": "regular",
        "slug": "Redes y almacenamiento cloud",
        "tema": "Redes y almacenamiento cloud",
        "sub": "Diagrama de despliegue CloudLite",
        "pi_hoy": "Diagrama de despliegue: red, zonas, almacenamiento",
        "entregable": "Diagrama Deployment (draw.io) + elección de storage (objeto/bloque/relacional conceptual)",
        "herramienta": "draw.io",
        "objetivos": [
            "Modelar red lógica (cliente, edge, app, datos) sin VPC de pago.",
            "Elegir tipo de almacenamiento según el caso de uso CloudLite.",
            "Completar el diagrama de **despliegue** del PI.",
        ],
        "slides_extra": [
            ("Red lógica para el diagrama", [
                "Cliente → DNS/edge → balanceador conceptual → app → datos.",
                "Segregación: frontend público vs datos privados (aunque sea «caja» en draw.io).",
                "No inventen subnets AWS: usen zonas **Pública / Privada / Datos**.",
            ]),
            ("Almacenamiento", [
                "Objeto (archivos/media) · Bloque (discos) · Archivo · DB gestionada conceptual.",
                "CloudLite: justifiquen 1 primario + 1 secundario (ej. DB + object para adjuntos).",
                "Backup/retención: una frase de política cualitativa basta.",
            ]),
            ("Checklist del diagrama Deployment", [
                "Nodos, redes/zonas, puertos, almacenes, relación con CI (artefacto).",
                "Debe alinearse con el C4 Containers (mismos nombres).",
            ]),
        ],
        "taller_titulo": "Taller Clase 7 — Despliegue y storage CloudLite",
        "taller_pasos": [
            "Dibujen Deployment en draw.io (zonas pública/privada/datos).",
            "Etiqueten puertos y tipo de storage por componente.",
            "Alineen nombres con el diagrama C4 de Clase 4.",
            "Actualicen informe: sección Redes y almacenamiento.",
            "Entrega domingo 23:59.",
        ],
        "quiz": [
            ("¿Por qué separar zona pública y de datos en el diagrama?",
             "Reducir superficie de ataque y aclarar trust boundaries."),
            ("¿Cuándo usaría almacenamiento de objetos?", "Media/archivos no estructurados / backups."),
            ("¿El diagrama Deployment debe usar los mismos nombres que C4?", "Sí, para trazabilidad."),
        ],
    },
    {
        "n": 8,
        "tipo": "regular",
        "slug": "Monitoreo optimizacion y CI-CD",
        "tema": "Monitoreo y optimización · CI/CD",
        "sub": "GitHub Actions + plan de observabilidad",
        "pi_hoy": "Workflow Actions (build/test/simulate) + métricas de monitoreo del PI",
        "entregable": ".github/workflows/ci.yml + sección Monitoreo/CI del informe",
        "herramienta": "GitHub Actions · Google Docs",
        "objetivos": [
            "Explicar pipeline CI vs CD y qué es realista sin cloud de pago.",
            "Crear un workflow Actions que construya/pruebe un stub.",
            "Definir 4–6 señales de monitoreo para CloudLite.",
        ],
        "slides_extra": [
            ("CI/CD sin tarjeta", [
                "CI: build + test en cada push. CD: deploy — aquí **simulado** (echo/artifact).",
                "GitHub Actions free: runners hosted; YAML en `.github/workflows/`.",
                "📸 [CAP: actions-yml] Workflow del stub CloudLite.",
            ]),
            ("YAML mínimo", [
                "on: push · jobs · steps: checkout → setup → test → upload artifact.",
                "Secrets solo vía Settings; nunca en el YAML en claro.",
                "Deploy stage: `echo Deploy simulado a entorno lab`.",
            ]),
            ("Monitoreo y optimización", [
                "Golden signals-lite: latencia, tráfico, errores, saturación.",
                "Logs estructurados + healthcheck del contenedor.",
                "Optimización: caché conceptual, paginación, límites de rate (anotar en informe).",
            ]),
        ],
        "taller_titulo": "Taller Clase 8 — Actions + monitoreo CloudLite",
        "taller_pasos": [
            "Creen repo free (o usen el del equipo) con stub mínimo.",
            "Agreguen `.github/workflows/ci.yml` (build/test + deploy simulado).",
            "Listen 4–6 métricas/logs a observar en producción hipotética.",
            "Peguen captura del run verde (o YAML + explicación si Actions falla por cuota).",
            "Actualicen informe secciones CI/CD y Monitoreo.",
        ],
        "quiz": [
            ("¿Qué hace el stage CI que no hace necesariamente CD?", "Validar build/tests antes de desplegar."),
            ("¿Dónde van los secretos en Actions?", "En Settings → Secrets, no en el YAML."),
            ("Nombre dos golden signals.", "Latencia, tráfico, errores, saturación."),
        ],
    },
    {
        "n": 9,
        "tipo": "parcial",
        "slug": "Parcial 2",
        "tema": "Parcial 2",
        "sub": "Solo evaluación",
        "pi_hoy": "Sin avance dirigido de PI",
        "entregable": "—",
        "herramienta": "—",
        "objetivos": ["Evaluar seguridad, redes/storage, monitoreo y CI/CD conceptual."],
        "slides_extra": [],
        "taller_titulo": "",
        "taller_pasos": [],
        "quiz": [],
    },
    {
        "n": 10,
        "tipo": "autonoma",
        "slug": "Costos y sostenibilidad cloud",
        "tema": "Costos y sostenibilidad cloud",
        "sub": "Actividad autónoma · sección PI",
        "pi_hoy": "Estimación cualitativa de costos + notas de sostenibilidad",
        "entregable": "Sección Costos/Sostenibilidad del informe (bajo/medio + drivers)",
        "herramienta": "Google Docs",
        "objetivos": [
            "Identificar drivers de costo (cómputo, datos, transferencia, idle).",
            "Proponer 3 apalancamientos de ahorro sin romper el diseño.",
            "Redactar sostenibilidad (apagado de labs, imágenes ligeras, sobredimensionamiento).",
        ],
        "slides_extra": [
            ("Costos sin factura real", [
                "Escala cualitativa: Bajo / Medio / Alto por componente.",
                "Drivers: siempre-on, egress, storage caliente, builds CI frecuentes.",
                "CloudLite: justifiquen por qué su diseño no es «siempre XL».",
            ]),
            ("Sostenibilidad", [
                "Menos capas innecesarias · imágenes slim · apagar labs · right-sizing.",
                "Relación con escalabilidad: escala cuando hay carga, no por vanidad.",
            ]),
        ],
        "taller_titulo": "Actividad autónoma Clase 10 — Costos CloudLite",
        "taller_pasos": [
            "Tabla componente → driver de costo → nivel (B/M/A) → apalancamiento.",
            "3 acciones de sostenibilidad aplicables al diseño.",
            "Integre en el informe PI (1 página).",
            "Entrega domingo 23:59.",
        ],
        "quiz": [
            ("Cite un driver típico de costo cloud.", "Cómputo idle, transferencia de datos, storage caliente…"),
            ("¿Qué es right-sizing?", "Ajustar capacidad al uso real, no sobredimensionar."),
            ("¿Por qué labs temporales ayudan a sostenibilidad académica?", "Evitan recursos siempre-on y costo/energía innecesaria."),
        ],
    },
    {
        "n": 11,
        "tipo": "regular",
        "slug": "Avance del proyecto final",
        "tema": "Avance del proyecto final",
        "sub": "Checkpoint diagramas v1 CloudLite",
        "pi_hoy": "Integrar diagramas v1 + checklist de avance PI",
        "entregable": "Paquete v1: Context + Containers + Deployment + Dockerfile + Actions + informe 60%+",
        "herramienta": "draw.io · GitHub · Google Docs",
        "objetivos": [
            "Consolidar evidencias PI en un paquete revisable.",
            "Detectar huecos (nombres inconsistentes, servicios de más, sin seguridad).",
            "Salir con backlog claro hacia Clase 12/15.",
        ],
        "slides_extra": [
            ("Checklist de avance (obligatorio)", [
                "☐ Dominio + capacidades  ☐ ADR modelo  ☐ C4 Context/Containers",
                "☐ Deployment  ☐ Dockerfile/lab  ☐ Actions YAML  ☐ Seguridad  ☐ Costos",
                "Hoy el docente revisa en vivo; no es sustentación final.",
            ]),
            ("Errores frecuentes a corregir", [
                "Microservicios teatro · nombres distintos entre diagramas · secretos en imagen.",
                "CI sin tests · diagrama sin puertos · dominio infinito.",
            ]),
            ("Rúbrica (recordatorio)", [
                "Diagramas 25 · Contenedores 20 · CI/CD 15 · Dominio/servicio 15 · etc.",
                "Detalle en enunciado PI (no se repite evaluación global aquí).",
            ]),
        ],
        "taller_titulo": "Taller Clase 11 — Checkpoint PI CloudLite v1",
        "taller_pasos": [
            "Completen el checklist en el informe (sí/no + enlace evidencia).",
            "Unifiquen nombres entre C4 y Deployment.",
            "Empaqueten ZIP/repo: diagramas PNG, Dockerfile, YAML, informe.",
            "Feedback docente 1:1 corto (cola).",
            "Backlog escrito: 5 ítems para Clase 12.",
        ],
        "quiz": [
            ("¿Qué debe coincidir entre C4 y Deployment?", "Nombres de componentes/servicios."),
            ("¿El checkpoint de Clase 11 es el Parcial 3?", "No. Parcial 3 es evaluación aparte (Clase 14)."),
            ("Nombre un anti-patrón a corregir hoy.", "Microservicios excesivos / secretos en imagen / CI vacío."),
        ],
    },
    {
        "n": 12,
        "tipo": "regular",
        "slug": "Pruebas de rendimiento y preparacion final",
        "tema": "Pruebas de rendimiento · Preparación de presentación final",
        "sub": "Métricas objetivo + ensayo de pitch PI",
        "pi_hoy": "Escenario de rendimiento + ensayo 5–8 min de sustentación",
        "entregable": "Sección Rendimiento + guion de pitch + paquete casi-final",
        "herramienta": "Google Docs · draw.io · (opcional) lab contenedor",
        "objetivos": [
            "Definir métricas/objetivos de rendimiento realistas para CloudLite.",
            "Diseñar un escenario de prueba (aunque sea cualitativo/simulado).",
            "Ensayar el pitch de sustentación (prep PI; Parcial 3 es otro día).",
        ],
        "slides_extra": [
            ("Rendimiento sin stress-tool de pago", [
                "Definan: RPS/usuarios concurrentes objetivo · p95 latencia · error rate.",
                "Escenario: pico de matrícula / hora pico de citas — narren carga.",
                "Bottlenecks probables: DB, auth, I/O de objetos.",
            ]),
            ("Preparación de presentación (5–8 min)", [
                "1 min problema · 2 min arquitectura · 1 min contenedor · 1 min CI · 1 min seguridad/costos · Q&A.",
                "Demo: diagrama + captura lab/Actions (no improvisar login cloud).",
                "Todos los integrantes hablan.",
            ]),
            ("Paquete de entrega", [
                "Informe + diagramas + Dockerfile + YAML + capturas.",
                "Fecha/canal: Campus Virtual (coordinación del periodo).",
            ]),
        ],
        "taller_titulo": "Taller Clase 12 — Rendimiento y ensayo CloudLite",
        "taller_pasos": [
            "Escriban escenario de carga + 3 métricas objetivo + bottleneck esperado.",
            "Ensayen pitch 5–8 min (cronómetro); feedback entre equipos.",
            "Cierren backlog de Clase 11.",
            "Dejen paquete casi-final en Drive/repo.",
            "Entrega de avance domingo 23:59.",
        ],
        "quiz": [
            ("¿Qué es p95 de latencia?", "El 95% de las solicitudes están por debajo de ese tiempo."),
            ("¿La prep de pitch reemplaza el Parcial 3?", "No; Parcial 3 es evaluación presencial del corte."),
            ("Cite un bottleneck típico.", "Base de datos, autenticación, almacenamiento de objetos…"),
        ],
    },
    {
        "n": 13,
        "tipo": "autonoma",
        "slug": "Escalabilidad automatica",
        "tema": "Escalabilidad automática",
        "sub": "Actividad autónoma · escenario de escala PI",
        "pi_hoy": "Documentar política de autoescalado conceptual de CloudLite",
        "entregable": "Sección Escalabilidad: triggers, límites, qué escala y qué no",
        "herramienta": "Google Docs · draw.io (opcional nota en Deployment)",
        "objetivos": [
            "Distinguir escala vertical vs horizontal y cuándo aplicarlas.",
            "Definir triggers cualitativos (CPU, cola, RPS) sin cloud de pago.",
            "Actualizar el informe PI con la política de escala.",
        ],
        "slides_extra": [
            ("Escala para CloudLite", [
                "Horizontal: más réplicas del API. Vertical: más CPU/RAM a un nodo.",
                "Datos: escala distinta (read replicas conceptuales / partición — solo si aplica).",
                "Triggers: RPS, latencia p95, profundidad de cola, CPU.",
            ]),
            ("Límites y costos", [
                "max replicas · min replicas · cooldown — anótenlos aunque sean hipotéticos.",
                "Escalar mal = costo (enlace con Clase 10).",
            ]),
        ],
        "taller_titulo": "Actividad autónoma Clase 13 — Autoescalado CloudLite",
        "taller_pasos": [
            "Describan qué componente escala y por qué.",
            "Definan 2 triggers + min/max + qué NO se escala.",
            "Anoten impacto en costos/sostenibilidad.",
            "Opcional: marca «ASG/replicas» en diagrama Deployment.",
            "Entrega domingo 23:59 (sección Escalabilidad).",
        ],
        "quiz": [
            ("¿Horizontal vs vertical?", "Más instancias vs más recursos en la misma instancia."),
            ("¿Por qué poner max replicas?", "Controlar costo y fallos de cascada."),
            ("¿La base de datos escala igual que el API?", "No necesariamente; suele ser más delicada."),
        ],
    },
    {
        "n": 14,
        "tipo": "parcial",
        "slug": "Parcial 3",
        "tema": "Parcial 3",
        "sub": "Solo evaluación",
        "pi_hoy": "Sin trabajo dirigido nuevo de PI (evaluación del corte)",
        "entregable": "—",
        "herramienta": "—",
        "objetivos": ["Evaluar rendimiento, escalabilidad y cierre conceptual del diseño."],
        "slides_extra": [],
        "taller_titulo": "",
        "taller_pasos": [],
        "quiz": [],
    },
    {
        "n": 15,
        "tipo": "autonoma",
        "slug": "Presentacion del proyecto y cierre",
        "tema": "Presentación del proyecto + cierre",
        "sub": "Sustentación PI CloudLite (autónoma)",
        "pi_hoy": "Sustentación / entrega final del PI CloudLite App",
        "entregable": "Paquete final + presentación 5–8 min (entrega en ExamLab · módulo Proyectos)",
        "herramienta": "Google Docs/Slides · diagramas · capturas lab",
        "objetivos": [
            "Entregar y sustentar CloudLite App con evidencias completas.",
            "Responder preguntas de arquitectura (ADRs, amenazas, escala).",
            "Cerrar el curso con reflexión de aprendizaje.",
        ],
        "slides_extra": [
            ("Rúbrica de sustentación (recordatorio)", [
                "Claridad del problema · calidad de diagramas · demo lab/CI · respuestas.",
                "Todos hablan. Penalización si solo un integrante presenta.",
            ]),
            ("Checklist final", [
                "Informe completo · 3 diagramas · Dockerfile+captura · Actions · pitch.",
                "Sin cuentas cloud de pago · sin instalar hipervisores como requisito.",
            ]),
            ("Cierre del curso", [
                "RAA1–3 aplicados al PI. Conserven el repo como portafolio.",
                "Gracias — arquitectura es trade-offs documentados, no logos de proveedores.",
            ]),
        ],
        "taller_titulo": "Actividad autónoma Clase 15 — Sustentación CloudLite",
        "taller_pasos": [
            "Suban paquete final a **ExamLab** (módulo Proyectos): informe + evidencias.",
            "Graben o presenten pitch 5–8 min según instrucción del docente.",
            "Incluyan Q&A escrito (3 preguntas que se harían a sí mismos + respuestas).",
            "Reflexión final (½ página): qué trade-off fue el más difícil.",
        ],
        "quiz": [
            ("¿Qué evidencias mínimas debe mostrar la sustentación?",
             "Diagramas + lab contenedor o captura + workflow CI + justificación de decisiones."),
            ("¿El PI reemplaza el Parcial 3?", "No."),
            ("¿Se exige AWS Free Tier?", "No; está prohibido como requisito."),
        ],
    },
]


def _shade(paragraph, fill: str) -> None:
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    pPr.append(shd)


def _run_d(run, *, size=11, bold=False, color=GRIS):
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = color


def para(doc, text, *, size=11, bold=False, color=GRIS, align=WD_ALIGN_PARAGRAPH.LEFT,
         space_after=6, space_before=0, shade=None):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if shade:
        _shade(p, shade)
    r = p.add_run(text)
    _run_d(r, size=size, bold=bold, color=color)
    return p


def banda(doc, text):
    return para(doc, f"  {text}", size=13, bold=True, color=BLANCO, shade="095292",
                space_before=10, space_after=8)


def h2(doc, text):
    return para(doc, text, size=12, bold=True, color=AZUL, space_before=12, space_after=6)


def add_inline_docx(p, text, *, size=11, color=GRIS):
    """Soporta @@negrita@@ dentro de un run de docx (mismo formato usado en las slides)."""
    for part in re.split(r'(@@.*?@@)', text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith('@@') and part.endswith('@@'):
            r.text = part[2:-2]
            _run_d(r, size=size, bold=True, color=color)
        else:
            r.text = part
            _run_d(r, size=size, color=color)


def bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        add_inline_docx(p, it)


def margins(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)


def cover_slide(prs, n: int, tema: str, sub: str, pi_hoy: str):
    s = blank(prs)
    bg_white(s)
    rect(s, 0, 0, SW, 3.0, NAVY)
    rect(s, 0, 3.0, SW, 0.08, CIAN)
    add_logo(s, width=2.0, corner="left-top", mt=0.3, mr=0.5, variant="white")
    tn = textbox(s, SW - 2.2, 0.35, 1.8, 0.4)
    pn = tn.paragraphs[0]
    pn.alignment = PP_ALIGN.RIGHT
    _run(pn.add_run(), f"Clase {n}", 12, CIAN, bold=True)
    tf = textbox(s, MARGIN, 1.0, CONTENT_W, 1.5, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    _run(p.add_run(), tema, 28, WHITE, bold=True)
    ps = tf.add_paragraph()
    ps.alignment = PP_ALIGN.CENTER
    ps.space_before = EPt(8)
    _run(ps.add_run(), sub, 15, CIAN)
    tm = textbox(s, MARGIN, 3.5, CONTENT_W, 2.8)
    for i, ln in enumerate([
        f"**Hoy avanzamos el PI en:** {pi_hoy}",
        "Bloque **120 min** · Teoría breve · Taller PI · cierre.",
        "Herramientas gratis + navegador · sin AWS/GCP/Oracle Cloud.",
    ]):
        p = tm.paragraphs[0] if i == 0 else tm.add_paragraph()
        p.space_after = EPt(8)
        _rich(p, ln, 15, GRAY)
    footer_num(s, 1)
    return s


# Diagramas reales (cajas + flechas dibujadas con formas pptx, no placeholders de
# imagen) para las clases donde el concepto es inherentemente visual.
DIAGRAMAS = {
    1: {
        "titulo": "Ejemplo de diagrama C4 — nivel Context",
        "sub": "Reemplacen actor / sistema / externo por su propio dominio CloudLite",
        "boxes": [
            {"id": "actor", "label": "Estudiante\n(actor)", "x": 0.9, "y": 3.0, "w": 2.3, "h": 1.2, "color": AMARILLO, "text_color": NAVY},
            {"id": "sys", "label": "CloudLite App\n(el sistema = una sola caja)", "x": 5.3, "y": 2.6, "w": 3.1, "h": 1.8, "color": NAVY},
            {"id": "ext", "label": "Sistema externo\n(ej. correo, auth)", "x": 10.1, "y": 3.0, "w": 2.5, "h": 1.2, "color": CIAN},
        ],
        "arrows": [
            {"src": "actor", "dst": "sys", "label": "usa"},
            {"src": "sys", "dst": "ext", "label": "notifica / consume"},
        ],
        "note": "Nivel Context: el sistema es UNA caja (sin abrir por dentro). Actores a la izquierda, sistemas externos a la derecha. El interior se dibuja en Clase 4 (Containers).",
    },
    3: {
        "titulo": "Máquinas virtuales vs. contenedores",
        "sub": "Misma capacidad de cómputo, distinto nivel de aislamiento",
        "boxes": [
            {"id": "h_vm", "label": "Máquinas virtuales", "x": 0.9, "y": 1.55, "w": 4.3, "h": 0.5, "color": NAVY, "size": 12},
            {"id": "hw1", "label": "Hardware físico", "x": 0.9, "y": 2.25, "w": 4.3, "h": 0.65, "color": GRAY},
            {"id": "hyp", "label": "Hipervisor", "x": 0.9, "y": 2.95, "w": 4.3, "h": 0.65, "color": CIAN},
            {"id": "os1", "label": "SO invitado A\n(completo)", "x": 0.9, "y": 3.65, "w": 2.05, "h": 0.7, "color": CIAN, "size": 11},
            {"id": "os2", "label": "SO invitado B\n(completo)", "x": 3.15, "y": 3.65, "w": 2.05, "h": 0.7, "color": CIAN, "size": 11},
            {"id": "appA", "label": "App A", "x": 0.9, "y": 4.4, "w": 2.05, "h": 0.6, "color": AMARILLO, "text_color": NAVY},
            {"id": "appB", "label": "App B", "x": 3.15, "y": 4.4, "w": 2.05, "h": 0.6, "color": AMARILLO, "text_color": NAVY},
            {"id": "h_ct", "label": "Contenedores", "x": 8.0, "y": 1.55, "w": 4.3, "h": 0.5, "color": NAVY, "size": 12},
            {"id": "hw2", "label": "Hardware físico", "x": 8.0, "y": 2.25, "w": 4.3, "h": 0.65, "color": GRAY},
            {"id": "kernel", "label": "SO anfitrión + motor de contenedores (kernel compartido)", "x": 8.0, "y": 2.95, "w": 4.3, "h": 0.65, "color": CIAN, "size": 10.5},
            {"id": "c1", "label": "Contenedor A\n(App A)", "x": 8.0, "y": 3.65, "w": 2.05, "h": 0.7, "color": AMARILLO, "text_color": NAVY, "size": 11},
            {"id": "c2", "label": "Contenedor B\n(App B)", "x": 10.25, "y": 3.65, "w": 2.05, "h": 0.7, "color": AMARILLO, "text_color": NAVY, "size": 11},
        ],
        "note": "VM: cada instancia carga un SO completo (aislamiento fuerte, más pesado). Contenedor: comparte el kernel del anfitrión y solo empaqueta app + dependencias (arranca en segundos, pesa MB no GB).",
    },
    4: {
        "titulo": "Ejemplo de diagrama C4 — nivel Containers",
        "sub": "2–5 cajas justificadas, cada flecha con protocolo + verbo de negocio",
        "boxes": [
            {"id": "cliente", "label": "Cliente/App\n(actor)", "x": 0.9, "y": 4.3, "w": 2.6, "h": 1.0, "color": AMARILLO, "text_color": NAVY},
            {"id": "api", "label": "API CloudLite\n(contenedor)", "x": 0.9, "y": 2.2, "w": 2.6, "h": 1.2, "color": NAVY},
            {"id": "db", "label": "Base de datos\n(contenedor)", "x": 5.2, "y": 2.2, "w": 2.6, "h": 1.2, "color": CIAN},
            {"id": "notif", "label": "Servicio de\nnotificaciones", "x": 9.4, "y": 2.2, "w": 2.6, "h": 1.2, "color": CIAN},
        ],
        "arrows": [
            {"src": "cliente", "dst": "api", "label": "HTTP/JSON"},
            {"src": "api", "dst": "db", "label": "SQL"},
            {"src": "api", "dst": "notif", "label": "evento/cola"},
        ],
        "note": "Los nombres de estas cajas deben reaparecer igual en el diagrama de Deployment (Clase 7) — es el mismo sistema visto desde otro ángulo.",
    },
    7: {
        "titulo": "Ejemplo de diagrama de despliegue (Deployment)",
        "sub": "Zonas de confianza: qué es público, qué es privado, dónde viven los datos",
        "boxes": [
            {"id": "publica", "label": "Zona pública\n(balanceador / edge)", "x": 0.9, "y": 2.4, "w": 3.6, "h": 1.1, "color": AMARILLO, "text_color": NAVY},
            {"id": "privada", "label": "Zona privada\n(app CloudLite)", "x": 5.2, "y": 2.4, "w": 3.6, "h": 1.1, "color": NAVY},
            {"id": "datos", "label": "Zona de datos\n(base de datos)", "x": 9.4, "y": 2.4, "w": 3.6, "h": 1.1, "color": CIAN},
        ],
        "arrows": [
            {"src": "publica", "dst": "privada", "label": "solo puerto 443"},
            {"src": "privada", "dst": "datos", "label": "solo puerto BD"},
        ],
        "note": "La base de datos NUNCA vive en la zona pública. Los nombres deben coincidir con los del C4 Containers (Clase 4) — mismo sistema, otro ángulo.",
    },
}


# Codigo/artefacto PROYECTABLE por clase: lo minimo que el estudiante debe ver
# en pantalla mientras se explica (el archivo completo va al repo del PI).
CODIGO_SLIDE = {
    2: ("ADR-001 — la plantilla completa cabe en una pagina", [
        "# ADR-001: Modelo de servicio de CloudLite",
        "",
        "## Contexto",
        "MVP academico, equipo de 3, sin presupuesto cloud.",
        "",
        "## Decision",
        "PaaS conceptual + contenedores (portable).",
        "",
        "## Alternativas descartadas",
        "- IaaS: control total, pero operamos SO y red -> tiempo que no tenemos.",
        "- SaaS como nucleo: no personalizable; solo satelite (auth/email).",
        "",
        "## Consecuencias",
        "+ Menos operacion.  - Menos control de red.  ~ Portabilidad OK.",
    ], "Si el ADR no nombra un modelo DOMINANTE y 2 descartes con razon, no es un ADR."),
    3: ("Dockerfile minimo del stub CloudLite", [
        "FROM node:20-alpine          # base slim: arranca rapido, pesa poco",
        "WORKDIR /app",
        "COPY package*.json ./",
        "RUN npm ci --omit=dev",
        "COPY . .",
        "EXPOSE 8080                  # el puerto que documentan en el C4",
        'CMD ["node", "server.js"]    # UN proceso principal por contenedor',
    ], "Nunca COPY de un .env con secretos: queda en las capas de la imagen para siempre."),
    6: ("Amenaza -> control -> evidencia (una fila por amenaza)", [
        "STRIDE  | Amenaza concreta del dominio      | Control            | Evidencia",
        "--------|-----------------------------------|--------------------|-------------",
        "Spoof   | Cualquiera llama la API sin auth   | Token/JWT          | C4: flecha 'auth'",
        "Tamper  | Cambian el precio via API          | Rol + validacion   | Contrato del endpoint",
        "Info    | API key dentro de la imagen        | Actions Secrets    | .dockerignore",
        "DoS     | Pico de trafico tumba el API       | Rate limit         | Deployment: edge",
    ], "Una lista generica de buenas practicas no es un modelo de amenazas: falta el dominio."),
    8: (".github/workflows/ci.yml — CI real, no un echo", [
        "name: CI",
        "on: [push, pull_request]",
        "jobs:",
        "  build:",
        "    runs-on: ubuntu-latest",
        "    steps:",
        "      - uses: actions/checkout@v4",
        "      - uses: actions/setup-node@v4",
        "        with: { node-version: '20' }",
        "      - run: npm ci",
        "      - run: npm test              # <- esto es lo que lo hace CI",
        "      - run: docker build -t cloudlite-api .",
    ], "Secretos con ${{ secrets.NOMBRE }}, NUNCA en claro dentro del YAML."),
    13: ("Politica de autoescalado (tabla, no prosa)", [
        "Componente   | Tipo        | Trigger up      | Min | Max | Cooldown",
        "-------------|-------------|-----------------|-----|-----|---------",
        "API          | Horizontal  | CPU > 70% / 5m  |  2  |  6  | 5 min",
        "Worker cola  | Horizontal  | cola > 100 msg  |  1  |  4  | 3 min",
        "BD primaria  | NO escala   | -               |  1  |  1  | -",
    ], "El 'max' es lo que evita que la factura escale sola. La BD primaria casi nunca escala horizontal."),
}

ANTES_DESPUES_ARQ = {
    3: {
        "titulo": "Maquina virtual vs contenedor — que cambia de verdad",
        "b_t": "Maquina virtual",
        "b": ["Cada instancia trae un **SO completo** (kernel propio)",
              "Aislamiento fuerte a nivel de hardware virtual",
              "Arranque en **minutos**, tamaño en **GB**",
              "Util cuando se necesitan SO distintos"],
        "a_t": "Contenedor",
        "a": ["**Comparte el kernel** del anfitrion",
              "Empaqueta solo app + dependencias",
              "Arranque en **segundos**, tamaño en **MB**",
              "Util para desplegar el mismo servicio muchas veces"],
    },
    4: {
        "titulo": "Microservicios de verdad vs microservicios teatro",
        "b_t": "Teatro (lo que NO queremos)",
        "b": ["12 servicios para un equipo de 3",
              "Se separan por capricho tecnico, no por negocio",
              "Flechas sin protocolo ni verbo",
              "Nadie sabe explicar por que ese corte"],
        "a_t": "Frontera justificada",
        "a": ["2-5 contenedores logicos, cada uno con su razon",
              "Frontera = responsabilidad de negocio",
              "Cada flecha: protocolo + verbo (HTTP/JSON, 'reserva')",
              "Cualquiera del equipo lo explica en 60 s"],
    },
    12: {
        "titulo": "«Que sea rapido» no es un requisito",
        "b_t": "Enunciado vago",
        "b": ["«La app tiene que ser rapida»",
              "«Aguanta harta gente»",
              "«Si se pone lenta, le subimos recursos»",
              "No hay con que comparar despues"],
        "a_t": "Enunciado medible",
        "a": ["**p95 < 300 ms** en el endpoint de reserva",
              "Escenario: **150 RPS** en el pico de inicio de semestre",
              "Bottleneck sospechado: **consulta a la BD**",
              "Se puede verificar: pasa o no pasa"],
    },
}


def build_pptx(c: dict) -> Path:
    n = c["n"]
    folder = CURSO / "Clases" / f"Clase {n} - {c['slug']}"
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / "Presentacion.pptx"

    if c["tipo"] == "parcial":
        prs = new_prs()
        cover_slide(prs, n, c["tema"], "Solo evaluación · sin tema de trabajo dirigido", c["pi_hoy"])
        content_slide(prs, "Indicaciones", [
            "Hoy es **solo Parcial** (presencial síncrono).",
            "No hay taller ni avance dirigido del PI en esta clase.",
            "Material de evaluación en carpeta docente de Parciales (no se distribuye antes).",
            "La prep del PI / pitch quedó en la clase regular anterior.",
        ], idx=2)
        closing_slide(prs, f"Parcial · Clase {n}", [
            "Enfocados en la evaluación del corte",
            "PI CloudLite continúa en la siguiente clase regular/autónoma",
        ], accent="Solo evaluación")
        prs.save(str(out))
        print("OK pptx parcial ->", out)
        return out

    prs = new_prs()
    cover_slide(prs, n, c["tema"], c["sub"], c["pi_hoy"])
    idx = 2
    content_slide(prs, "Agenda de hoy (120 min)", [
        "**0–10** Encuadre: hoy avanzamos el PI en… + entregable concreto.",
        "**10–40** Teoría Core breve (solo lo necesario para el taller PI).",
        "**40–100** Taller guiado PI (demo en vivo + trabajo de equipo).",
        "**100–115** Revisión de evidencias del PI.",
        "**115–120** Cierre: criterio de éxito + plazo domingo 23:59.",
    ], idx=idx)
    idx += 1
    content_slide(prs, "Objetivos de la clase", c["objetivos"], idx=idx)
    idx += 1
    content_slide(prs, "PI CloudLite — entregable de hoy", [
        f"@@Entregable:@@ {c['entregable']}",
        f"Herramienta: **{c['herramienta']}**",
        "Todo lo que construyan hoy entra al **informe/repo del PI** (no es lab suelto).",
        "Equipos 2–3 · todos deben poder explicar el artefacto.",
    ], idx=idx)
    idx += 1
    for title, bullets_ in c["slides_extra"]:
        content_slide(prs, title, bullets_, idx=idx)
        idx += 1
    dg = DIAGRAMAS.get(n)
    if dg:
        diagram_boxes_slide(
            prs, dg["titulo"], dg["boxes"], arrows=dg.get("arrows"),
            sub=dg.get("sub"), note=dg.get("note"), idx=idx,
        )
        idx += 1
    ad = ANTES_DESPUES_ARQ.get(n)
    if ad:
        before_after_slide(prs, ad["titulo"], ad["b_t"], ad["b"], ad["a_t"], ad["a"], idx=idx)
        idx += 1
    cs = CODIGO_SLIDE.get(n)
    if cs:
        pseudo_code_slide(prs, cs[0], cs[1], caption=cs[2], idx=idx)
        idx += 1
    content_slide(prs, "Taller PI (paso a paso)", [f"**{i+1}.** {p}" for i, p in enumerate(c["taller_pasos"])], idx=idx)
    idx += 1
    box_note_slide(prs, "Para continuar (PI)", [
        ("info", f"Entregable: {c['entregable']}"),
        ("aclaracion", "Subir evidencias al paquete CloudLite (Drive/repo) y a ExamLab domingo 23:59."),
        ("advertencia", "Sin cloud de pago ni instalaciones obligatorias de hipervisores/Docker Desktop."),
    ], idx=idx)
    idx += 1
    closing_slide(
        prs,
        f"Clase {n} · PI en movimiento",
        [
            c["pi_hoy"],
            f"Evidencia: {c['entregable']}",
            "Siguiente paso = siguiente hito del PI CloudLite",
        ],
        accent="Teoría al servicio del proyecto",
    )
    prs.save(str(out))
    print("OK pptx ->", out)
    return out


# Bloque ampliado por clase (contexto/por-que-importa, escenario, pistas) — fusiona
# el contenido de los dos talleres duplicados que existian antes por clase, quedandose
# con lo mejor de cada uno en un solo documento generado por el pipeline.
TALLER_BLOQUE = {
    1: {
        "contexto": [
            "@@Por qué importa al PI:@@ sin dominio concreto no hay arquitectura que defender.",
            "La ficha + C4 Context son la semilla del informe y de todos los diagramas del semestre.",
            "Si el problema es vago (app de la universidad), el resto del PI se vuelve teatro.",
        ],
        "escenario": [
            "Equipo 2-3 (o individual). Elegir un dominio concreto.",
            "Sugeridos: AgendaU · BiblioLite · InventarioLab · TurnosClinica · EventosCampus.",
            "Plantilla ficha: DOMINIO · PROBLEMA · ACTORES · CAPACIDADES · FUERA DE ALCANCE.",
        ],
        "pistas": [
            "¿Quién sufre el problema y como lo miden?",
            "¿La caja grande es el sistema CloudLite (no un módulo interno)?",
            "¿Las flechas tienen verbo (reservar, notificar, autenticar)?",
            "¿Fuera de alcance está escrito (que NO haran hoy)?",
        ],
    },
    2: {
        "contexto": [
            "@@Por qué importa al PI:@@ el modelo IaaS/PaaS/SaaS define quién opera SO, runtime y costos.",
            "Sin ADR, el PI no puede justificar trade-offs en sustentación ni en parciales.",
        ],
        "escenario": [
            "Partir de la ficha/C4 de Clase 1 (mismo dominio).",
            "MVP académico típico: PaaS conceptual + SaaS satélite (auth/email).",
        ],
        "pistas": [
            "¿La decisión nombra un modelo dominante (no un poco de todo)?",
            "¿Hay al menos dos alternativas descartadas con razón?",
            "¿Consecuencias incluyen operación, costo y aprendizaje?",
        ],
    },
    3: {
        "contexto": [
            "@@Por qué importa al PI:@@ CloudLite debe mostrar al menos un servicio contenerizado con evidencia.",
            "El contenedor es el puente entre el diagrama C4 y el despliegue realista (sin cloud de pago).",
            "Lab en navegador Play with Docker: sin Docker Desktop obligatorio.",
        ],
        "escenario": [
            "Elegir el servicio principal del C4 (API o web).",
            "Abrir Play with Docker (labs.play-with-docker.com); sesión temporal de 4h.",
            "Prohibido: copiar .env / API keys a la imagen.",
        ],
        "pistas": [
            "¿El puerto expuesto coincide con el que documentan?",
            "¿Hay evidencia con timestamp (captura o enlace)?",
            "¿Secretos fuera de la imagen?",
        ],
    },
    4: {
        "contexto": [
            "@@Por qué importa al PI:@@ el C4 Containers es el mapa lógico que luego alinea Deployment y CI.",
            "Anti-patrón: 12 microservicios para 3 estudiantes = teatro, no arquitectura.",
            "Regla CloudLite: 2-5 cajas justificadas + contratos etiquetados.",
        ],
        "escenario": [
            "Partir del C4 Context (mismos nombres de sistema/actores).",
            "draw.io o Excalidraw; vista Containers (no solo Context).",
        ],
        "pistas": [
            "¿Hay 2-5 cajas (no 1 monolito innominado ni 12 microservicios)?",
            "¿Los nombres coincidirán luego con Deployment?",
            "¿Cada contrato tiene error de negocio (ej. 409 conflicto)?",
        ],
    },
    6: {
        "contexto": [
            "@@Por qué importa al PI:@@ seguridad = amenazas del dominio + controles visibles.",
            "Si la API key está en el Dockerfile, ya filtraron el secreto.",
            "STRIDE-lite: 5 amenazas concretas, no lista genérica de internet.",
        ],
        "escenario": [
            "Usar dominio y Containers ya definidos.",
            "Amenazas típicas: secrets en imagen, API sin auth, logs con tokens, PII sin TLS.",
        ],
        "pistas": [
            "¿Cada amenaza tiene control + dónde se ve en el diagrama?",
            "¿Secretos en Settings/Actions, no en Dockerfile?",
            "¿Least privilege aparece aunque sea narrado?",
        ],
    },
    7: {
        "contexto": [
            "@@Por qué importa al PI:@@ sin zonas, el Deployment no demuestra fronteras de confianza.",
            "Si la BD está en zona pública, el diagrama ya falló.",
            "Nombres del Deployment deben = nombres del C4 Containers.",
        ],
        "escenario": [
            "Cliente -> edge -> app -> datos.",
            "Sin inventar subnets AWS; trust boundaries sí.",
        ],
        "pistas": [
            "¿La BD está en zona de datos/privada?",
            "¿Mismos nombres que el C4?",
            "¿Object storage solo si el dominio lo necesita?",
        ],
    },
    8: {
        "contexto": [
            "@@Por qué importa al PI:@@ CI que solo hace echo success no es CI.",
            "GitHub Actions free = evidencia de build/test sin tarjeta.",
            "Observabilidad: 4-6 métricas atadas al dominio (golden signals-lite).",
        ],
        "escenario": [
            "Repo free + stub de Clase 3 (o mínimo).",
            "Secrets en Settings; nunca en el YAML en claro.",
        ],
        "pistas": [
            "¿Hay build o test real (no solo echo vacío)?",
            "¿Secrets fuera del repositorio?",
            "¿Métricas con umbral u objetivo narrado?",
        ],
    },
    10: {
        "contexto": [
            "@@Por qué importa al PI:@@ lo más caro suele ser lo que dejan encendido sin usar.",
            "Costo cualitativo B/M/A es aceptable: no inventar precios USD de cloud de pago.",
        ],
        "escenario": [
            "Componentes: API, DB, object, CI, edge.",
            "Drivers: idle, egress, storage, minutos CI.",
        ],
        "pistas": [
            "¿Cada fila tiene driver (no solo \"caro\")?",
            "¿Las 3 acciones son verificables en el PI?",
            "¿Evitaron inventar facturas de AWS/GCP?",
        ],
    },
    11: {
        "contexto": [
            "@@Por qué importa al PI:@@ checkpoint v1 = integrar evidencias; no es sustentación ni Parcial 3.",
            "Si C4 y Deployment no comparten nombres, el PI está roto.",
        ],
        "escenario": [
            "Revisar: dominio, ADR, C4, Deployment, Dockerfile, Actions, Seguridad, Costos.",
            "Demo corta por equipo si el tiempo alcanza.",
        ],
        "pistas": [
            "¿Cada \"sí\" tiene enlace o ruta de archivo?",
            "¿Hay backlog priorizado (no lista infinita)?",
            "¿Anti-patrones (teatro microservicios / secretos / CI vacío) marcados?",
        ],
    },
    12: {
        "contexto": [
            "@@Por qué importa al PI:@@ sin métrica objetivo, \"rápido\" es opinión — no arquitectura.",
            "Ensayo de pitch 5-8 min reduce riesgo en la sustentación (Clase 15).",
        ],
        "escenario": [
            "Pico del dominio (ej. inicio de semestre / día de citas).",
            "Demo permitida: diagrama + captura lab/Actions — no K8s de pago.",
        ],
        "pistas": [
            "¿p95 / error rate / RPS tienen número u orden de magnitud?",
            "¿Bottleneck nombrado (DB/auth/storage)?",
            "¿Guion de pitch con tiempos por sección?",
        ],
    },
    13: {
        "contexto": [
            "@@Por qué importa al PI:@@ escalar la API no escala sola la base de datos.",
            "Política de autoescalado conceptual = evidencia de diseño (sin cloud de pago).",
        ],
        "escenario": [
            "Plantilla: componente, tipo, trigger up/down, min/max, cooldown.",
            "Impacto en costo cualitativo (enlace a Clase 10).",
        ],
        "pistas": [
            "¿Triggers medibles (RPS, p95, cola)?",
            "¿Hay techo (max) para no escalar infinito?",
            "¿DB/sesión sticky justificados como no-escalables?",
        ],
    },
    15: {
        "contexto": [
            "@@Por qué importa al PI:@@ sustentación = evidencias + decisiones, no tour de logos.",
            "PI 20% Corte 3 no sustituye el Parcial 3 (ya ocurrió en Clase 14).",
        ],
        "escenario": [
            "Orden del pitch: problema -> arquitectura -> contenedor/CI -> seguridad/costos/escala -> Q&A.",
        ],
        "pistas": [
            "¿Evidencias mínimas presentes (diagramas + lab + CI + decisiones)?",
            "¿Tiempos del pitch ensayados?",
            "¿PI y Parcial 3 no se confunden en el discurso?",
        ],
    },
}


def build_taller_docx(c: dict) -> Path | None:
    if c["tipo"] == "parcial":
        return None
    n = c["n"]
    tb = TALLER_BLOQUE.get(n, {})
    folder = CURSO / "Clases" / f"Clase {n} - {c['slug']}"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{c['taller_titulo']}.docx"
    doc = Document()
    margins(doc)
    banda(doc, c["taller_titulo"])
    para(doc, "Arquitectura de Sistemas Computacionales · CloudLite App (PI)",
         size=11, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER)
    para(doc, "Documento estudiante — avance del Proyecto Integrador",
         size=10, color=CIAN_D, align=WD_ALIGN_PARAGRAPH.CENTER, shade="E8F4FA")
    if tb.get("contexto"):
        h2(doc, "1. Contexto / por qué importa al PI")
        bullets(doc, tb["contexto"])
    h2(doc, "2. Hoy avanzamos el PI en…")
    para(doc, c["pi_hoy"])
    h2(doc, "3. Entregable concreto")
    para(doc, c["entregable"], shade="E8F4FA")
    if tb.get("escenario"):
        h2(doc, "4. Escenario / datos de partida")
        bullets(doc, tb["escenario"])
    h2(doc, "5. Herramientas (gratis + navegador)")
    para(doc, c["herramienta"])
    para(doc, "Prohibido como requisito: AWS/GCP/Oracle/Azure con tarjeta; VirtualBox/VMware/Docker Desktop obligatorio.",
         shade="FBE4E4")
    h2(doc, "6. Pasos guiados")
    bullets(doc, c["taller_pasos"])
    h2(doc, "7. Criterio de éxito")
    bullets(doc, [
        "El artefacto queda en el paquete PI (informe y/o repo) con nombres consistentes.",
        "Cualquier integrante puede explicar la decisión en 60 segundos.",
        "Evidencia adjunta (PNG, enlace lab, YAML, etc.).",
    ])
    if tb.get("pistas"):
        h2(doc, "8. Pistas (checklist vacío — sin solución)")
        bullets(doc, [f"☐ {p}" for p in tb["pistas"]])
    h2(doc, "9. Entrega")
    para(doc, "Entrega en ExamLab (examlab.lovable.app/app · módulo Talleres) · domingo 23:59 (regla del Acuerdo). Un envío por equipo.")
    doc.save(str(path))
    print("OK taller ->", path)
    return path


def build_quiz_docx(c: dict) -> Path | None:
    """Genera DOS archivos: version proyectable (sin respuestas) + clave docente
    (solo respuestas). Antes se generaba un unico docx con la respuesta debajo de
    cada pregunta, lo que lo volvia imposible de proyectar sin regalar la clave."""
    if c["tipo"] == "parcial" or not c.get("quiz"):
        return None
    n = c["n"]
    kit = CURSO / "Kit docente" / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)

    # Version estudiante: solo enunciados, proyectable en clase.
    path = kit / f"Quiz Clase {n} - {c['slug']}.docx"
    doc = Document()
    margins(doc)
    banda(doc, f"Quiz Clase {n} — {c['tema']}")
    para(doc, "Version estudiante — SOLO enunciados. No proyectar la Clave docente.",
         size=10, bold=True, color=AZUL, align=WD_ALIGN_PARAGRAPH.CENTER, shade="E8F4FA")
    para(doc, "5–8 min · individual · al servicio de verificar el avance PI de hoy.")
    for i, (q, _a) in enumerate(c["quiz"], 1):
        h2(doc, f"Pregunta {i}")
        para(doc, q)
    doc.save(str(path))
    print("OK quiz ->", path)

    # Clave docente: enunciado + respuesta, documento privado.
    clave_path = kit / f"Quiz Clase {n} - CLAVE DOCENTE.docx"
    doc_k = Document()
    margins(doc_k)
    banda(doc_k, f"Quiz Clase {n} — CLAVE DOCENTE")
    para(doc_k, "DOCUMENTO DOCENTE — PRIVADO. No proyectar en Presentacion.pptx.",
         size=10, bold=True, color=ROJO, align=WD_ALIGN_PARAGRAPH.CENTER, shade="FBE4E4")
    for i, (q, a) in enumerate(c["quiz"], 1):
        h2(doc_k, f"Pregunta {i}")
        para(doc_k, q)
        para(doc_k, f"Respuesta: {a}", shade="E8F4FA")
    doc_k.save(str(clave_path))
    print("OK clave ->", clave_path)
    return path


# Imagenes de SALIDA ESPERADA por clase (generadas por config/slides/mockups.py).
# El guion las embebe con [[captura: archivo.png]]; si falta el archivo,
# guion_md_a_docx.py deja la caja "inserta aqui la captura" sin romper el build.
CAPTURAS_CLASE = {
    3: [("Build y run del stub en Play with Docker (lo que debe verse en pantalla)",
         "salida-docker-build-run.png"),
        ("Evidencia del entregable: el contenedor corriendo (`docker ps`)",
         "salida-docker-ps.png")],
    6: [("Por que un secreto NUNCA va dentro de la imagen (demo de 1 minuto)",
         "salida-secreto-en-imagen.png")],
    8: [("Run verde del workflow: build + test reales, no un `echo ok`",
         "salida-actions-run.png")],
}


def _capturas_md(n: int) -> str:
    items = CAPTURAS_CLASE.get(n)
    if not items:
        return ""
    return "".join(f"📸 {cap} [[captura: {fn}]]\n" for cap, fn in items)


def guion_md(c: dict) -> str:
    n = c["n"]
    if c["tipo"] == "parcial":
        return f"""# Guion docente — Clase {n}: {c['tema']}

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: **Solo evaluación (Parcial)** — sin tema de trabajo dirigido nuevo
- Proyecto Integrador: CloudLite App (hoy **no** se avanza con taller)

## Objetivo del bloque
Aplicar el instrumento de evaluación del corte. Material en `Parciales/`.

## Plan minuto a minuto (120 min)

### 0–10 · Organización
Di: «Hoy es solo Parcial. Guarden materiales del PI; no hay taller dirigido.»
Verificar asistencia y condiciones del aula/Meet presencial.

### 10–100 · Aplicación del parcial
Distribuir enunciado. Silencio de evaluación. Resolver dudas de enunciado (no de contenido).

### 100–115 · Recolección
Recoger evidencias / cierre de envío según modalidad del instrumento.

### 115–120 · Cierre
Di: «Gracias. El PI CloudLite continúa en la siguiente clase regular o autónoma según el plan.»

## Notas
- No mezclar «Tema · Parcial».
- Prep de pitch/PI fue en la clase regular anterior.
"""

    # Fundamento por tipo de tema (breve pero útil al docente)
    fundamentos = {
        1: """Arquitectura de software = las decisiones estructurales dificiles de cambiar despues: como se dividen los componentes, como se comunican, donde se despliegan, y que atributos de calidad priorizan (rendimiento, seguridad, disponibilidad, costo). No es "el diagrama bonito": es el conjunto de decisiones que ese diagrama documenta.

El modelo C4 (Context, Containers, Components, Code) da niveles de zoom consistentes. Hoy se usa SOLO el nivel Context: un diagrama con el sistema como una caja, las personas que lo usan (actores) y los sistemas externos con los que se conecta (ej. pasarela de pagos, servicio de correo) — sin entrar todavia a que hay DENTRO del sistema (eso es Clase 4, nivel Containers).

El estudiante no necesita una cuenta cloud real de pago: CloudLite App se modela y simula con herramientas gratuitas (draw.io, Excalidraw, Play with Docker). La arquitectura se aprende razonando sobre decisiones y trade-offs, no memorizando la consola de un proveedor especifico.

Error de docente que no domina el tema: confundir "arquitectura" con "el stack tecnologico" (ej. "usamos React y Node, esa es la arquitectura") — el stack es una decision DENTRO de la arquitectura, no la arquitectura completa. Lo que se evalua hoy es si el diagrama Context responde con claridad quien usa el sistema y que toca hacia afuera.""",
        2: """IaaS, PaaS y SaaS son niveles de abstraccion sobre la infraestructura, y cada uno mueve la linea de responsabilidad compartida (shared responsibility model): en IaaS (Infrastructure as a Service) el proveedor da solo maquinas/red/almacenamiento y el cliente administra sistema operativo, runtime y aplicacion; en PaaS (Platform as a Service) el proveedor tambien administra el sistema operativo y el runtime, el cliente solo sube su codigo; en SaaS (Software as a Service) el proveedor entrega la aplicacion completa y el cliente solo la usa (ej. Gmail).

Regla practica: mientras mas alto el nivel de abstraccion (SaaS > PaaS > IaaS), menos control tiene el cliente pero menos trabajo operativo asume. Para un MVP academico como CloudLite, un enfoque PaaS conceptual + contenedores suele ser el punto dulce: control suficiente para aprender arquitectura, sin la carga operativa de administrar servidores completos.

Un ADR (Architecture Decision Record) es un documento corto que registra UNA decision arquitectonica: el contexto/problema, las opciones consideradas, la decision tomada y las consecuencias (trade-offs aceptados). Obliga a hacer explicito el trade-off control-vs-velocidad en vez de elegir "porque si".

Error de docente que no domina el tema: presentar IaaS/PaaS/SaaS como si fueran productos especificos de una marca en vez de un modelo conceptual de responsabilidad — el modelo aplica igual a cualquier proveedor, la pregunta siempre es "quien administra que capa".""",
        3: """Virtualizacion (maquinas virtuales): un hipervisor crea varias maquinas virtuales sobre un mismo hardware fisico, y cada VM tiene su PROPIO sistema operativo completo (kernel incluido), aislado de las demas. Es aislamiento fuerte, pero cada VM carga el peso completo de un SO.

Contenedores: en cambio, todos los contenedores de una maquina COMPARTEN el kernel del sistema operativo anfitrion; cada contenedor solo empaqueta la aplicacion y sus dependencias (librerias, configuracion), no un SO completo. Por eso arrancan en segundos (no minutos) y pesan megabytes (no gigabytes) comparado con una VM.

Distincion clave que se confunde seguido: una IMAGEN es la plantilla inmutable (el "molde": codigo + dependencias + configuracion); un CONTENEDOR es una instancia en ejecucion de esa imagen (el "objeto" corriendo). De una misma imagen se pueden lanzar muchos contenedores identicos.

Para evitar depender de Docker Desktop (que requiere licencia/recursos en equipos institucionales), se usa Play with Docker (labs.play-with-docker.com, sesiones de 4h) como lab principal en el navegador — da una terminal Linux real con Docker instalado, sin instalar nada localmente. Killercoda queda como alterna si PWD no esta disponible.

Error de docente que no domina el tema: decir que un contenedor "es una VM ligera" sin mas — la diferencia arquitectonica real es el aislamiento (kernel propio vs kernel compartido), no solo el tamano.""",
        4: """Un microservicio es una unidad de despliegue independiente: se construye, se despliega y se escala por separado de los demas servicios, con su propia frontera de responsabilidad (ej. servicio de citas, servicio de notificaciones). La frontera correcta se define por responsabilidad de negocio, no por capricho tecnico.

Con equipos de 2-3 estudiantes, 2-5 contenedores logicos es un tamano realista para CloudLite (ej. API, base de datos, un servicio de notificaciones) — mas que eso se vuelve "microservicios teatro": servicios separados solo de nombre, sin razon de negocio real que justifique la separacion.

C4 Containers (nivel 2 del modelo visto en Clase 1) muestra que aplicaciones/servicios/bases de datos componen el sistema y COMO se comunican entre si (protocolo, formato de datos) — un contrato explicito, no flechas sin etiqueta.

Consecuencia inevitable de distribuir: lo que antes era una llamada de funcion local ahora es una llamada de red, que puede fallar, tardar, o llegar fuera de orden. Un sistema distribuido no es "el mismo sistema pero en varias partes" — introduce latencia real y fallos parciales (un servicio cae, los demas deben seguir funcionando o degradarse con gracia) que un monolito no tiene.

Error de docente que no domina el tema: aplaudir un diagrama con 8 microservicios sin preguntar por que cada uno existe — el numero de servicios no es una medida de calidad arquitectonica; la justificacion de cada frontera si lo es.""",
        6: """Seguridad en la nube no es "poner un firewall": es identificar amenazas especificas del sistema y mapear cada una a un control verificable. STRIDE (metodologia de modelado de amenazas) da 6 categorias en una frase cada una: Spoofing (alguien se hace pasar por otro), Tampering (alguien modifica datos sin autorizacion), Repudiation (alguien niega haber hecho una accion sin evidencia que lo contradiga), Information disclosure (datos sensibles expuestos a quien no debe verlos), Denial of service (el sistema deja de responder), Elevation of privilege (alguien obtiene mas permisos de los que deberia tener).

Aplicado a CloudLite: por cada categoria relevante al dominio del equipo, se identifica una amenaza concreta (ej. Tampering: alguien modifica el precio de un producto via la API sin autorizacion) y un control que la mitiga (ej. autenticacion + validacion de rol antes de aceptar el cambio).

Gestion de secretos: una credencial (API key, contraseña de BD) NUNCA se escribe dentro de la imagen del contenedor ni se sube al repositorio en texto plano — eso queda expuesto a quien tenga acceso a la imagen o al historial de Git. Se usan mecanismos de secretos del propio pipeline (ej. GitHub Actions Secrets), inyectados en tiempo de ejecucion, nunca guardados en el codigo.

Error de docente que no domina el tema: tratar "seguridad" como una sola diapositiva generica de buenas practicas — el entregable de hoy exige amenaza especifica -> control especifico -> evidencia en el diagrama o repo, no una lista generica de consejos.""",
        7: """El diagrama de despliegue (deployment) muestra DONDE corre cada pieza del sistema y como se conectan a traves de la red, distinguiendo zonas de confianza: una subred publica (expuesta a internet, ej. balanceador de carga) y una subred privada (solo accesible desde dentro, ej. base de datos) — sin necesidad de una VPC real de pago, el concepto se dibuja igual con draw.io.

Balanceo de carga y DNS en una frase cada uno: el DNS traduce un nombre humano (miapp.com) a una direccion de red; un balanceador de carga reparte las peticiones entrantes entre varias instancias del mismo servicio para que ninguna se sature sola.

Almacenamiento: Object storage (ej. tipo S3) guarda archivos/blobs con acceso via URL, ideal para imagenes o backups; storage de base de datos guarda registros estructurados con consultas complejas. La eleccion depende del tipo de dato: un PDF de factura va a object storage, el registro de la factura en si va a la base de datos.

Coherencia con Clase 4: los nombres de servicios en este diagrama de despliegue deben ser LOS MISMOS que los contenedores definidos en el C4 Containers — es el mismo sistema visto desde otro angulo, no un sistema nuevo.

Error de docente que no domina el tema: dibujar "la nube" como una sola caja difusa sin distinguir zona publica de zona privada — esa distincion es precisamente lo que demuestra que el equipo entiende superficie de exposicion, tema central de la clase de seguridad anterior.""",
        8: """CI (Integracion Continua) automatiza la VALIDACION del codigo cada vez que alguien sube un cambio: correr pruebas, verificar que compila/construye, revisar estilo — sin que un humano lo haga manualmente cada vez. CD (Entrega/Despliegue Continuo) automatiza el PASO SIGUIENTE, llevar ese cambio validado a produccion; en este curso, sin infraestructura real de pago, CD se SIMULA (el pipeline llega hasta "listo para desplegar", no despliega a un servidor real).

Un archivo YAML de GitHub Actions es evidencia real y verificable de CI: define triggers (cuando correr, ej. en cada push), jobs (que tareas ejecutar) y steps (comandos concretos). Aunque sea minimo (ej. solo correr un linter), es un pipeline real, no una simulacion en papel.

Monitoreo con golden signals (los 4 indicadores clasicos de observabilidad): latencia (cuanto tarda en responder), errores (que porcentaje de peticiones falla), saturacion (que tan cerca esta el sistema de su limite de capacidad), trafico (cuantas peticiones recibe). Aplicados a CloudLite de forma conceptual: aunque no haya trafico real, se documenta QUE se mediria y COMO se detectaria un problema con cada señal.

Error de docente que no domina el tema: presentar CI/CD como sinonimos intercambiables — CI valida, CD despliega; un pipeline puede tener CI sin CD (validar sin desplegar automaticamente), y eso es exactamente lo que se construye hoy.""",
        10: """Costo en la nube se analiza aunque no haya facturacion real: cualitativamente en niveles Bajo/Medio/Alto por componente (ej. una base de datos gestionada = costo medio-alto por almacenamiento+computo constante; una funcion serverless que casi no se usa = costo bajo), identificando los DRIVERS de costo (que factor especifico hace subir el gasto: numero de instancias, volumen de datos, trafico de red saliente).

Sostenibilidad tecnica (no ambiental en este contexto) = right-sizing: no sobre-aprovisionar recursos "por si acaso" (una maquina grande corriendo al 5% de uso es desperdicio puro), usar labs/entornos temporales que se apagan cuando no se usan en vez de dejar todo corriendo 24/7, e imagenes de contenedor "slim" (minimas, sin paquetes innecesarios) que consumen menos storage y arrancan mas rapido.

Conexion directa con Clase 13 (escalabilidad): escalar automaticamente HACIA ARRIBA sin un limite o politica de apagado tambien escala el costo sin control — el diseño de autoescalado y el analisis de costo son la misma decision vista desde dos angulos.

Error de docente que no domina el tema: tratar el costo como un tema "de negocio, no tecnico" — las decisiones que mas impactan el costo (tipo de instancia, almacenamiento elegido, arquitectura con o sin colas/cache) son decisiones de arquitectura, tomadas por quien diseña el sistema.""",
        11: """Esta clase no introduce teoria nueva a proposito: es un checkpoint donde el equipo demuestra que las piezas ya vistas (C4 Context/Containers, seguridad, despliegue, CI) forman un sistema coherente, no fragmentos sueltos de distintas clases.

El rol del docente hoy es de auditor critico, no de instructor: bloquear dominios que crecieron sin limite desde la Clase 1 original (scope creep), y senalar "microservicios teatro" — servicios separados en el diagrama que en la practica no tienen frontera de responsabilidad real ni justificacion de por que estan separados.

Diferencia importante que evita confusion: esto NO es la sustentacion final (Clase 15) ni el Parcial 3 (Clase 14evaluacion escrita) — es un punto de control intermedio para corregir rumbo a tiempo, con retroalimentacion entre pares ademas de la del docente.

Error de docente que no domina el tema: dejar pasar un checkpoint sin retroalimentacion especifica por equipo ("todo bien, sigan asi") — el valor de un checkpoint es identificar el gap concreto que cada equipo debe cerrar antes de la sustentacion.""",
        12: """Rendimiento en arquitectura se analiza con tres piezas: objetivo medible (ej. "p95 de tiempo de respuesta menor a 300ms" — el percentil 95 indica que el 95% de las peticiones responden en ese tiempo o menos, una medida mas honesta que el promedio porque no la distorsionan casos extremos), escenario de carga (cuantas peticiones por segundo, RPS, se simulan) y bottleneck (el componente especifico que limita el rendimiento del sistema completo — nunca "todo es lento", siempre hay una pieza que limita primero).

Diferencia entre stress test (aumentar la carga progresivamente hasta encontrar el punto de quiebre del sistema) y spike test (una subida SUBITA y grande de trafico, simulando un pico real como una promocion o una noticia viral) — evaluan cosas distintas: capacidad maxima vs capacidad de reaccion ante lo inesperado.

El pitch de 5-8 minutos se ensaya HOY como preparacion, distinto del Parcial 3 (Clase 14) que es la evaluacion escrita formal — no deben confundirse ni mezclar contenido de uno con el otro en esta clase.

Error de docente que no domina el tema: pedir "que la app sea rapida" sin definir p95, RPS objetivo ni el bottleneck sospechado — sin esas tres piezas, "rendimiento" es una palabra vacia, no un analisis.""",
        13: """Escalar verticalmente = darle mas recursos a la MISMA maquina (mas CPU, mas RAM) — simple pero tiene un techo fisico y usualmente requiere reiniciar el servicio. Escalar horizontalmente = agregar MAS instancias iguales corriendo en paralelo, repartiendo la carga entre ellas (requiere que el sistema soporte multiples instancias sin pisarse, ej. no guardar estado de sesion solo en memoria local).

Autoescalado (mencion conceptual): un trigger (ej. uso de CPU sobre 70% durante 5 minutos) dispara automaticamente el arranque de una instancia adicional; y un limite maximo evita que el sistema escale sin control (y sin control de costo, conexion directa con Clase 10).

Punto que suele generar "magia" en las sustentaciones: los datos NO escalan igual que la capa de API. Agregar mas instancias de la aplicacion es relativamente simple; escalar una base de datos relacional (que necesita mantener consistencia) es fundamentalmente mas dificil — por eso el entregable de hoy exige documentar explicitamente QUE NO se escala en el diseño actual de CloudLite, no solo lo que si.

Error de docente que no domina el tema: presentar el autoescalado como si resolviera cualquier problema de rendimiento automaticamente — sin identificar primero el bottleneck (Clase 12), escalar la pieza equivocada no mejora nada y aumenta el costo sin razon.""",
        15: """Esta clase de cierre tampoco introduce teoria nueva: consolida evidencia completa de las 14 clases anteriores (C4 Context/Containers, seguridad, despliegue, CI/monitoreo, costos, rendimiento, escalabilidad) en una sustentacion coherente, no una lista de diapositivas sueltas por tema.

Criterio de calidad de la sustentacion: CUALQUIER integrante del equipo debe poder explicar cualquier parte del sistema en 60 segundos — si solo una persona entiende el diagrama completo, el trabajo en equipo fallo aunque el diagrama este bien hecho.

Recordatorio explicito que evita confusion de pesos: el Proyecto Integrador (20% del Corte 3) es una evaluacion DISTINTA e independiente del Parcial 3 (Clase 14, evaluacion escrita) — uno no sustituye ni compensa al otro en el calculo de la nota.

Error de docente que no domina el tema: permitir que un solo integrante presente todo mientras los demas observan — el Q&A de cierre debe distribuirse entre todo el equipo precisamente para verificar el criterio de los 60 segundos.""",
    }
    fund = fundamentos.get(n, "Teoría al servicio del entregable PI de hoy. Ver diapositivas de la clase.")

    plan_blocks = f"""### 0–10 · Encuadre PI
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **{c['pi_hoy']}**.
Entregable concreto: {c['entregable']}.
Teoría breve y luego taller; no es un lab suelto.»
Pasa diapositiva de agenda y objetivos. Abre el enunciado PI si alguien aún no lo tiene.

### 10–40 · Teoría Core (al servicio del taller)
Recorre las slides de conceptos. Cada 7–8 min amarra al artefacto del PI:
«Esto lo van a dejar hoy en el informe/diagrama/repo.»
Usa ejemplos del dominio de los equipos (pide 1 voluntario).
Capturas sugeridas: ver marcadores [CAP:] en las slides.

### 40–55 · Demo en vivo
Demuestra la herramienta del día (**{c['herramienta']}**) con un mini-ejemplo CloudLite.
Narra clics. Si falla la red, usa capturas en `Kit docente/Clase {n}/Capturas/`.
Di: «Copien la estructura, no el dominio de mi demo.»
{_capturas_md(n)}

### 55–100 · Taller guiado PI (equipos)
Proyecta la lista de pasos del taller estudiante.
Recorre mesas/Meet: bloquea dominios vagos; exige nombres consistentes.
A los 80 min: «Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Quiz / evidencias
Aplica quiz corto (Kit). Mientras, revisa que el entregable esté en Drive/repo.
Retroalimenta 2–3 equipos en voz alta (errores frecuentes).

### 115–120 · Cierre
Di: «Criterio de éxito: cualquier integrante explica el artefacto en 60 s.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»
"""

    if c["tipo"] == "autonoma":
        plan_blocks = f"""### Modalidad autónoma (festivo)
No hay encuentro síncrono obligatorio. El estudiante trabaja con Presentacion.pptx + Taller.docx.

### Guion del docente (asíncrono)
1. Publica en ExamLab (y Campus Virtual si aplica): diapositivas + taller + recordatorio del PI.
2. Mensaje sugerido: «Clase {n} autónoma. Hoy avanzamos el PI en: {c['pi_hoy']}.
   Entregable: {c['entregable']}. Duda por foro/correo institucional.»
3. Revisa entregas domingo 23:59; deja feedback breve orientado a la rúbrica PI.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos de diagrama/ADR; no adelantes Parcial.
"""

    pasos = "\n".join(f"{i+1}. {p}" for i, p in enumerate(c["taller_pasos"]))
    return f"""# Guion docente — Clase {n}: {c['tema']}

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: {"Actividad autónoma" if c["tipo"] == "autonoma" else "Clase regular (teoría + taller PI)"}
- Enfoque: **Proyecto Integrador CloudLite App** (parte práctica)
- Sin fechas de periodo · sin bio · sin mapa completo del curso

## Objetivos de la clase
{chr(10).join("- " + o.replace("**", "") for o in c["objetivos"])}

## Hoy avanzamos el PI en…
**{c["pi_hoy"]}**

**Entregable concreto:** {c["entregable"]}

**Herramienta:** {c["herramienta"]}

## Fundamento teórico para el docente
{fund}

Referencia de slides: `Clases/Clase {n} - {c['slug']}/Presentacion.pptx` (solo tema de esta clase).

## Plan de clase minuto a minuto (120 min)

{plan_blocks}

## Actividad / taller (detalle)
{pasos}

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- Explicación oral de 60 s por integrante (muestreo).

## Quiz
Ver `Kit docente/Clase {n}/Quiz Clase {n} - {c['slug']}.docx` (con respuestas).

## Capturas sugeridas
- 📸 Pantallazo: herramienta del día en uso con artefacto CloudLite [[captura: demo-clase{n:02d}.png]]
- 📸 Pantallazo: evidencia de entregable (diagrama/YAML/lab)

## Notas operativas
- Plataforma de entrega: ExamLab (examlab.lovable.app/app). Campus Virtual sigue siendo el canal institucional.
- Prohibido pedir cloud con tarjeta.
- Día de parcial = solo evaluación (no aplica a esta clase).
"""


def build_guion(c: dict) -> Path:
    n = c["n"]
    kit = CURSO / "Kit docente" / f"Clase {n}"
    cap = kit / "Capturas"
    kit.mkdir(parents=True, exist_ok=True)
    cap.mkdir(parents=True, exist_ok=True)
    # placeholder readme capturas
    readme = cap / "README.txt"
    if not readme.exists():
        readme.write_text(
            f"Capturas Clase {n}. Preferir PNG reales (Playwright/manual). "
            "El guion referencia [CAP:] / [[captura: …]].\n",
            encoding="utf-8",
        )
    path = kit / f"Guion Docente Clase {n} - {c['slug']}.md"
    path.write_text(guion_md(c), encoding="utf-8")
    print("OK guion md ->", path)
    return path


def build_parcial_kit_note(c: dict) -> Path:
    n = c["n"]
    kit = CURSO / "Kit docente" / f"Clase {n}"
    kit.mkdir(parents=True, exist_ok=True)
    path = kit / f"NOTA Docente - Clase {n} Parcial.md"
    mapping = {
        5: "Parcial 1 - Cloud virtualizacion y distribuidos.docx",
        9: "Parcial 2 - Seguridad redes monitoreo y CI-CD.docx",
        14: "Parcial 3 - Rendimiento escalabilidad y cierre de proyecto.docx",
    }
    path.write_text(
        f"""# Clase {n} — Solo Parcial

- Bloque 120 min · presencial síncrono · **sin taller PI**.
- Enunciado/solución: `Parciales/{mapping.get(n, "")}` (+ SOLUCION).
- Recordar: prep de pitch/PI fue en clase regular anterior (p. ej. Clase 12 para P3).
- No publicar solución en `Clases/`.
""",
        encoding="utf-8",
    )
    print("OK nota parcial ->", path)
    return path


def convert_guiones(paths: list[Path]) -> None:
    conv = SLIDES_DIR / "guion_md_a_docx.py"
    for md in paths:
        if not md.exists():
            continue
        os.system(f'python "{conv}" "{md}"')


def build_all():
    guiones = []
    for c in CLASSES:
        n = c["n"]
        print(f"\n=== Clase {n} ({c['tipo']}) ===")
        if c["tipo"] == "parcial":
            build_parcial_kit_note(c)
            # pptx mínimo de indicaciones (opcional en Clases para no confundir; se genera carpeta clara)
            build_pptx(c)
            g = build_guion(c)
            guiones.append(g)
            continue
        build_pptx(c)
        build_taller_docx(c)
        build_quiz_docx(c)
        g = build_guion(c)
        guiones.append(g)
    convert_guiones(guiones)
    print("\nDONE batch Arquitectura PI-first")


if __name__ == "__main__":
    build_all()
