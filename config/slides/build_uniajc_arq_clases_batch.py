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
import calendario_2026_2 as cal  # noqa: E402
from arq_fundamentos import FUNDAMENTOS  # noqa: E402
from arq_examlab_data import EXAMLAB as TALLERES_EXAMLAB  # noqa: E402
import examlab_talleres  # noqa: E402
from uniajc_slides_engine import (  # noqa: E402
    before_after_slide,
    box_note_slide,
    closing_slide,
    content_slide,
    new_prs,
    herramientas_slide,
    pseudo_code_slide,
    steps_visual_slide,
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
    SH,
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

# Marcador interno "[CAP: token] descripcion" en las bullets de slides_extra: le
# recuerda al docente que tome esa captura antes de clase (ver Kit docente/Capturas/
# README.txt). NUNCA debe llegar literal a la diapositiva del estudiante. Donde ya
# existe la captura real (o su ilustracion "salida esperada"), se inserta la imagen
# y se limpia el texto; donde todavia no existe, solo se limpia el texto.
_CAP_RE = re.compile(r"📸?\s*\[CAP:\s*([\w-]+)\]\s*")
CAPTURAS_REALES = {
    "docker-ps": CURSO / "Kit docente" / "Clase 3" / "Capturas" / "salida-docker-ps.png",
    "actions-yml": CURSO / "Kit docente" / "Clase 8" / "Capturas" / "salida-actions-run.png",
}


def _limpiar_y_capturar(bullets_):
    """Quita el marcador [CAP:] de las bullets y devuelve la ruta de imagen real
    a insertar en la diapositiva, si existe alguna para los tokens presentes."""
    limpias, imagen = [], None
    for b in bullets_:
        tokens = _CAP_RE.findall(b)
        b2 = _CAP_RE.sub("", b).strip()
        b2 = re.sub(r"\s*·\s*$", "", b2).strip()
        limpias.append(b2)
        for t in tokens:
            ruta = CAPTURAS_REALES.get(t)
            if ruta and ruta.exists():
                imagen = ruta
    return limpias, imagen


def _add_captura(slide, ruta_png):
    """Inserta la captura real en la esquina inferior derecha de una content_slide,
    sin tapar las vinetas (ancho fijo moderado, alto proporcional real)."""
    from PIL import Image as _PILImage
    iw, ih = _PILImage.open(str(ruta_png)).size
    w = 3.4
    h = w * ih / iw
    x = SW - MARGIN - w
    y = SH - MARGIN - h
    slide.shapes.add_picture(str(ruta_png), Inches(x), Inches(y), width=Inches(w), height=Inches(h))

AZUL = RGBColor(0x09, 0x52, 0x92)
CIAN_D = RGBColor(0x26, 0x9C, 0xCB)
GRIS = RGBColor(0x2B, 0x2B, 0x2B)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
ROJO = RGBColor(0xA0, 0x20, 0x30)
FONT = "Calibri"

# ---------------------------------------------------------------------------
# Modalidad de trabajo — decision docente 2026-2
# ---------------------------------------------------------------------------
# El curso paso de «equipos de 2-3, individual si el docente lo autoriza» a lo
# contrario: INDIVIDUAL POR DEFECTO, y el docente puede autorizar equipos de 2 o 3.
# Cuando hay equipo autorizado el artefacto puede ser compartido, pero la entrega en
# ExamLab SIEMPRE es individual (cada estudiante responde con sus propias palabras) y
# cualquier integrante debe poder explicar cualquier parte en 60 segundos.
#
# Estos son los textos por DEFECTO de las 15 clases. Una clase puede sobreescribir
# cualquiera de estas claves en su dict de CLASSES (p. ej. la Clase 1, donde el trabajo
# es estrictamente individual porque cada estudiante define su propio dominio).
MODALIDAD_DEFAULTS = {
    # Slides
    "agenda_taller_nota": "avance individual",
    "equipo_note": "Individual por defecto · el docente puede autorizar equipos de 2–3; "
                   "la entrega en ExamLab siempre es individual.",
    # Taller del estudiante
    "explica_60s_note": "Puedes explicar tu decisión en 60 segundos "
                        "(si trabajas en equipo autorizado, cualquier integrante debe poder hacerlo).",
    "entrega_unidad_note": "Modalidad de trabajo: individual por defecto; el docente puede autorizar "
                           "equipos de 2 o 3 y en ese caso el artefacto puede ser compartido, pero el "
                           "envío en ExamLab es siempre individual (responde con tus propias palabras).",
    # Guion docente
    "arranque_cita": "¿En qué quedó tu CloudLite la clase pasada?",
    "arranque_nota": "pregunta de arranque (1 min) para detectar estudiantes rezagados antes de avanzar:",
    "voluntario_word": "estudiante",
    "taller_modalidad_word": "individual · equipos de 2–3 solo si tú los autorizaste",
    "retro_word": "estudiantes",
    "criterio_60s_note": "el estudiante explica su artefacto en 60 s",
    "criterio_oral_note": "Explicación oral de 60 s por estudiante (muestreo; si autorizaste equipos, "
                          "pregunta a cualquier integrante).",
    "entregan_word": "los estudiantes",
}


def mod(c: dict, key: str) -> str:
    """Texto de modalidad de trabajo: override de la clase o default individual."""
    return c.get(key, MODALIDAD_DEFAULTS[key])


# ---------------------------------------------------------------------------
# Tipo de bloque: SE DERIVA DEL CALENDARIO, no se escribe a mano por clase
# ---------------------------------------------------------------------------
# Historia del defecto que esto previene: el material se genero con el calendario
# viejo, donde el festivo del 17/08 caia en la Clase 2 y el del 16/11 cerraba el
# curso. Al acortarse el semestre (24/08-22/11, 13 sesiones para 15 temas) el
# 17/08 quedo FUERA del rango y la Sesion 13 (16/11) se destino a las
# sustentaciones del PI en vivo. Como el tipo estaba escrito a mano en cada dict,
# el material siguio anunciando «actividad autonoma» para dos clases que si
# tienen encuentro sincrono. Leyendolo del calendario en cada build, un cambio de
# fechas no puede volver a desincronizar el material.
CAL_KEY = "arquitectura"


def tipo_de_clase(n_clase: int) -> str:
    """'parcial' | 'autonoma' | 'sustentacion' | 'regular' para una Clase de material.

    'presencial' y 'virtual' colapsan a 'regular': la diferencia entre ellas es de
    modalidad (aula vs Meet) y no cambia la estructura del bloque, porque las dos
    son sincronas. Lo que si cambia la estructura es que no haya encuentro
    (autonoma), que el bloque sea solo evaluacion (parcial) o que se dedique a
    sustentar el PI (sustentacion).
    """
    s = cal.sesion_de_clase(CAL_KEY, n_clase)
    if s is None:
        raise SystemExit(
            "Clase %d no aparece en 'clases_material' de ninguna sesion de '%s' en %s. "
            "Corrija el calendario, no este build." % (n_clase, CAL_KEY, cal.JSON_PATH)
        )
    if s.get("parcial"):
        return "parcial"
    t = (s.get("tipo") or "").lower()
    return t if t in ("autonoma", "sustentacion") else "regular"


TIPO_LABEL = {
    "regular": "Clase regular (teoría + taller PI) · encuentro síncrono",
    "autonoma": "Actividad autónoma (festivo, sin encuentro síncrono)",
    "sustentacion": "Sustentación del Proyecto Integrador · **en vivo** (síncrona)",
    "parcial": "Solo evaluación (Parcial)",
}


# ---------------------------------------------------------------------------
# Catálogo de clases (Plan 2026-2) — PI-first
# ---------------------------------------------------------------------------
# Sin clave "tipo": se inyecta desde el calendario justo despues de esta lista.

CLASSES = [
    {
        "n": 1,
        "slug": "Introduccion a arquitecturas cloud",
        "tema": "Introducción a arquitecturas cloud",
        "sub": "Diagnóstico · CloudLite App · primer boceto",
        "pi_hoy": "Definir dominio CloudLite App + 3–5 capacidades + problema en 2–3 frases",
        "entregable": "Ficha PI de 6 bloques + C4 Context en Mermaid renderizado en ExamLab (boceto previo en Excalidraw/draw.io)",
        "herramienta": "Padlet · Excalidraw / draw.io",
        # Modalidad individual por defecto: desde 2026-2 los textos por defecto del
        # curso ya estan escritos en modo individual (ver MODALIDAD_DEFAULTS abajo),
        # asi que esta clase solo necesita el matiz propio de la Clase 1: aqui el
        # trabajo es estrictamente individual porque cada estudiante define SU dominio.
        "agenda_taller_nota": "avance individual",
        "equipo_note": "Actividad individual: cada estudiante define su propio dominio CloudLite.",
        "ficha_bloques_note": "Ficha de 6 bloques: DOMINIO · PROBLEMA · CAPACIDADES · ACTORES · SISTEMAS EXTERNOS · FUERA DE ALCANCE.",
        "explica_60s_note": "El estudiante puede explicar su decisión en 60 segundos.",
        "entrega_unidad_note": "Un envío por estudiante.",
        "entrega_oficial_nota": "La entrega oficial se hace respondiendo las preguntas abiertas del taller dentro de ExamLab (https://uniaj.examlab.workers.dev/). El documento/ficha en Word o Google Docs es opcional, solo para que el estudiante conserve sus respuestas; lo que califica es lo que quede escrito en las preguntas de ExamLab.",
        "separar_notas_docente": True,
        "arranque_cita": "¿En qué quedó tu CloudLite la clase pasada?",
        "arranque_nota": "pregunta de arranque (1 min) para detectar estudiantes rezagados antes de avanzar:",
        "voluntario_word": "estudiante",
        "taller_modalidad_word": "individual",
        "retro_word": "estudiantes",
        "criterio_60s_note": "el estudiante explica su artefacto en 60 s",
        "criterio_oral_note": "Explicación oral de 60 s por el estudiante (muestreo).",
        "entregan_word": "los estudiantes",
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
            ("Nube vs on-premise para CloudLite", [], {
                "headers": ["Criterio", "On-premise en la UNIAJC", "Nube"],
                "rows": [
                    ["**Inversión inicial**",
                     "Comprar servidor, UPS y licencias antes de escribir una línea. Gasto de capital.",
                     "Casi cero para arrancar. Gasto operativo por lo que se consume."],
                    ["**Tiempo hasta la primera demo del PI**",
                     "Semanas: cotizar, comprar, instalar y pedir permisos a TI.",
                     "Minutos: la capacidad se aprovisiona sin pedir permiso."],
                    ["**Quién opera SO, parches y respaldos**",
                     "Usted o la oficina de TI de la universidad, todo el semestre.",
                     "Se reparte con el proveedor; cuánto, lo decide el modelo de servicio (Clase 2)."],
                    ["**El día del pico** (inicio de semestre)",
                     "La capacidad es fija: si se queda corta, AgendaU se cae y no hay nada que hacer ese día.",
                     "Elasticidad: sube mientras dura el pico y luego se devuelve."],
                ],
                "note": "Resuelta sobre el dominio de referencia AgendaU. Usted conserva los 4 criterios "
                        "y rehace las celdas con SU dominio: es la pregunta 4 del taller. Hoy se decide "
                        "nube u on-premise; el modelo de servicio (IaaS/PaaS/SaaS) es la Clase 2.",
                "col_w": [2.6, 5.1, 5.1],
            }),
            ("CloudLite App — el hilo conductor", [
                "Aplicación web/API de un dominio realista (citas, academia, inventario liviano…).",
                "Entregables del semestre: diagramas + contenedor (lab) + CI/CD conceptual + informe.",
                "Hoy solo: **problema + capacidades + boceto de contexto**.",
                "Sin AWS/GCP/Oracle: draw.io, LabEx Docker Playground, GitHub Actions.",
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
            "Elija dominio concreto (no «red social genérica») y escriba: problema (2–3 frases), 4 capacidades.",
            "Escriba actores, sistemas externos (2–3) y fuera de alcance.",
            "Boceto del **C4 Context** en Excalidraw o draw.io (CloudLite + actores + sistemas externos), y después convertirlo a **Mermaid** con ayuda de una IA para pegarlo renderizado en ExamLab.",
            "Tabla nube vs on-prem + veredicto. Entregue en **ExamLab** (Talleres) las preguntas resueltas (domingo 23:59).",
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
        "slug": "Modelos de servicio IaaS PaaS SaaS",
        "tema": "Modelos de servicio: IaaS, PaaS, SaaS",
        "sub": "ADR del PI · elección del modelo de servicio",
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
        "taller_titulo": "Taller Clase 2 — ADR modelo de servicio CloudLite",
        "taller_pasos": [
            "Retome su ficha y su C4 Context de la Clase 1: dominio, capacidades y actores (no cambie de dominio).",
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
        "slug": "Virtualizacion y contenedores",
        "tema": "Virtualización y contenedores",
        "sub": "Lab LabEx Docker Playground → stub CloudLite",
        "pi_hoy": "Contenerizar un stub del servicio principal de CloudLite",
        "entregable": "Dockerfile (+ compose opcional) + captura/enlace lab navegador",
        "herramienta": "LabEx Docker Playground · alterna si no carga: Killercoda",
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
                "Abrir LabEx Docker Playground (labex.io, inicie sesión con su cuenta de Google o Microsoft).",
                "`docker run` de un nginx/hello y luego **su** imagen stub.",
                "📸 [CAP: labex-home] Home del lab · 📸 [CAP: docker-ps] `docker ps`.",
                "La sesión de LabEx es temporal: guardar Dockerfile + capturas con timestamp antes de cerrarla. Si LabEx está caído: Killercoda (ubuntu/docker) como alterna.",
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
            "En LabEx Docker Playground: construyan y corran el contenedor (si no carga, Killercoda como alterna).",
            "Documenten Dockerfile (y compose si aplica) en el repo/ZIP del PI.",
            "Capturen evidencia (PNG) o enlace de sesión + nota de caducidad.",
            "Actualicen informe: sección Contenedores + enlace a diagrama de despliegue futuro.",
        ],
        "quiz": [
            ("¿Qué comparte un contenedor con el host que una VM típicamente no comparte?", "El kernel del SO."),
            ("Nombre la herramienta de lab principal del curso para contenedores.", "LabEx Docker Playground (alterna: Killercoda)."),
            ("¿Por qué no poner secretos en el Dockerfile?", "Quedan en capas/historial de la imagen."),
        ],
    },
    {
        "n": 4,
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
            "Crea un repo free (o usa el que ya tengas del PI) con stub mínimo.",
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
                "Sustentas tú los 5 bloques; si hay equipo autorizado, hablan todos.",
            ]),
            ("Paquete de entrega", [
                "Informe + diagramas + Dockerfile + YAML + capturas.",
                "Fecha/canal: coordinación del periodo.",
            ]),
        ],
        "taller_titulo": "Taller Clase 12 — Rendimiento y ensayo CloudLite",
        "taller_pasos": [
            "Escriban escenario de carga + 3 métricas objetivo + bottleneck esperado.",
            "Ensaya el pitch 5–8 min (cronómetro) y da feedback cruzado a otro estudiante (o a otro equipo, si el docente los autorizó).",
            "Cierren backlog de Clase 11.",
            "Dejen paquete casi-final en Drive/repo.",
            "Entrega de avance domingo 23:59.",
        ],
        "quiz": [
            ("¿Qué es p95 de latencia?", "El 95% de las solicitudes están por debajo de ese tiempo."),
            ("¿La prep de pitch reemplaza el Parcial 3?", "No; Parcial 3 es evaluación síncrona por Meet del corte."),
            ("Cite un bottleneck típico.", "Base de datos, autenticación, almacenamiento de objetos…"),
        ],
    },
    {
        "n": 13,
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
        "slug": "Presentacion del proyecto y cierre",
        "tema": "Presentación del proyecto + cierre",
        "sub": "Sustentación en vivo del PI CloudLite · cierre del curso",
        "pi_hoy": "Sustentar en vivo el PI CloudLite App y entregar el paquete final",
        "entregable": "Paquete final en ExamLab (módulo Proyectos) + pitch de 5–8 min sustentado hoy en clase + Q&A",
        "herramienta": "Google Docs/Slides · diagramas · capturas lab",
        "objetivos": [
            "Sustentar **en vivo** CloudLite App con evidencias completas.",
            "Responder **en vivo** preguntas de arquitectura (ADRs, amenazas, escala).",
            "Cerrar el curso con reflexión de aprendizaje.",
        ],
        "slides_extra": [
            ("Cómo se ordena la sesión de hoy", [
                "Sustentación **en vivo**, en este bloque: no se reemplaza por video grabado.",
                "Turnos de **6 min de pitch + 2–4 min de Q&A**; el orden se sortea al empezar.",
                "Ten el paquete ya subido a ExamLab **antes** de tu turno (no se sube presentando).",
                "Mientras otros presentan, escuchas: el cierre del curso se hace con todo el grupo.",
            ]),
            ("Rúbrica de sustentación (recordatorio)", [
                "Claridad del problema · calidad de diagramas · demo lab/CI · respuestas.",
                "Cubres los 5 bloques del guion; en equipo autorizado hablan todos (penalización si solo uno presenta).",
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
        "taller_titulo": "Guía de sustentación Clase 15 — PI CloudLite",
        "taller_pasos": [
            "Sube el paquete final a **ExamLab** (módulo Proyectos) **antes** de tu turno: informe + evidencias.",
            "Sustenta **en vivo** el pitch de 5–8 min con la lámina de arquitectura en pantalla.",
            "Responde el **Q&A en vivo** (3–4 preguntas del docente, dirigidas al azar).",
            "Entrega el Q&A escrito (3 preguntas duras que te harías + respuestas) como preparación del anterior.",
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

# Fuente de verdad del tipo de bloque: el calendario del periodo (ver tipo_de_clase).
for _c in CLASSES:
    _c["tipo"] = tipo_de_clase(_c["n"])


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


def cover_slide(prs, n: int, tema: str, sub: str, pi_hoy: str, *, tipo: str = "regular"):
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
    if tipo == "sustentacion":
        # El bloque no se reparte en teoría + taller: son turnos de sustentación.
        lineas_cover = [
            f"**Hoy cerramos el PI:** {pi_hoy}",
            "Bloque **120 min** · sesión **síncrona** de sustentaciones · turnos consecutivos.",
            "Paquete subido a ExamLab **antes** de tu turno · defensa **en vivo**, no video grabado.",
        ]
    else:
        lineas_cover = [
            f"**Hoy avanzamos el PI en:** {pi_hoy}",
            "Bloque **120 min** · Teoría breve · Taller PI · cierre.",
            "Herramientas gratis + navegador · sin AWS/GCP/Oracle Cloud.",
        ]
    for i, ln in enumerate(lineas_cover):
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
        "MVP academico, un desarrollador (2 o 3 si el docente autorizo equipo), sin presupuesto cloud.",
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
              "Se explica en 60 s sin leer notas"],
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


def _pasos(c):
    """Pasos del taller de esta clase.

    Los pasos originales eran one-liners vagos ("creen diagrama Containers") sin
    cantidad ni criterio de verificacion, asi que el estudiante no sabia cuando
    habia terminado. La version reescrita vive en
    `arq_examlab_data.EXAMLAB[n]["pasos"]`; si falta, se cae a los originales
    para no romper el build.
    """
    t = TALLERES_EXAMLAB.get(c["n"]) or {}
    return t.get("pasos") or c["taller_pasos"]


# Herramientas por clase. El orden importa: primero la herramienta con la que se
# trabaja, y al final siempre Mermaid (cuando el taller pide un diagrama) y ExamLab,
# que es donde se entrega todo. Los nombres deben coincidir con el campo
# `herramienta` del dict de la clase; los logos viven en assets/herramientas/ y se
# normalizan con `python config/slides/normalizar_iconos.py`.
HERRAMIENTAS_DIA = {
    1: [{"name": "Padlet", "logo": "padlet.png", "note": "Rompehielos"},
        {"name": "Excalidraw", "logo": "excalidraw.png", "note": "Boceto rapido"},
        {"name": "draw.io", "logo": "drawio.png", "note": "C4 Context"}],
    2: [{"name": "Google Docs", "logo": "google_docs.png", "note": "ADR-001"},
        {"name": "draw.io", "logo": "drawio.png", "note": "Matriz de modelos"}],
    3: [{"name": "LabEx Docker Playground", "logo": "labex.png", "note": "Lab del dia"},
        {"name": "Killercoda", "logo": "killercoda.png", "note": "Alterna si no carga"},
        {"name": "Google Docs", "logo": "google_docs.png", "note": "Informe PI"}],
    4: [{"name": "draw.io", "logo": "drawio.png", "note": "C4 Containers"},
        {"name": "Excalidraw", "logo": "excalidraw.png", "note": "Boceto rapido"}],
    6: [{"name": "Excalidraw", "logo": "excalidraw.png", "note": "Tabla STRIDE"},
        {"name": "Google Docs", "logo": "google_docs.png", "note": "Informe PI"}],
    7: [{"name": "draw.io", "logo": "drawio.png", "note": "Deployment"},
        {"name": "Google Docs", "logo": "google_docs.png", "note": "Informe PI"}],
    8: [{"name": "GitHub Actions", "logo": "github_actions.png", "note": "CI del PI"},
        {"name": "Google Docs", "logo": "google_docs.png", "note": "Informe PI"}],
    10: [{"name": "Google Docs", "logo": "google_docs.png", "note": "Tabla de costos"}],
    11: [{"name": "draw.io", "logo": "drawio.png", "note": "Auditoria del paquete"},
         {"name": "GitHub Actions", "logo": "github_actions.png", "note": "Evidencia CI"},
         {"name": "Google Docs", "logo": "google_docs.png", "note": "Informe PI"}],
    12: [{"name": "Google Docs", "logo": "google_docs.png", "note": "Objetivo de rendimiento"},
         {"name": "draw.io", "logo": "drawio.png", "note": "Bottleneck"}],
    13: [{"name": "Google Docs", "logo": "google_docs.png", "note": "Politica de escalado"},
         {"name": "draw.io", "logo": "drawio.png", "note": "Nota en Deployment"}],
    15: [{"name": "Google Docs", "logo": "google_docs.png", "note": "Pitch y portafolio"},
         {"name": "draw.io", "logo": "drawio.png", "note": "Diagramas del paquete"}],
}


def _herramientas_de(c: dict) -> list:
    """Herramientas de la clase + Mermaid (si hay diagrama) + ExamLab.

    Mermaid y ExamLab no se escriben clase por clase porque son transversales: si
    el taller tiene pregunta de diagrama, el estudiante entrega codigo Mermaid, y
    la entrega siempre ocurre en ExamLab. Anadirlos aqui evita que una clase se
    quede sin nombrarlos.
    """
    base = list(HERRAMIENTAS_DIA.get(c["n"], []))
    if not base:
        return []
    if _tiene_diagrama(c["n"]):
        base.append({"name": "Mermaid", "logo": "mermaid.png", "note": "Codigo del diagrama"})
    base.append({"name": "ExamLab", "logo": "examlab.png", "note": "Donde se entrega"})
    return base


# Titulo de la diapositiva del flujo de diagramacion (Excalidraw -> IA -> Mermaid
# -> ExamLab). El CONTENIDO de los 4 pasos es compartido (examlab_talleres), este
# es solo el rotulo con el que aparece en el deck del curso.
FLUJO_SLIDE_TITULO = "Del boceto a ExamLab (diagrama)"


def _tiene_diagrama(n: int) -> bool:
    """True si el taller de ExamLab de esta clase tiene pregunta tipo `diagrama`.

    Decide si la clase necesita la diapositiva del flujo: 12 de las 15 clases de
    Arquitectura piden un diagrama, y hasta ahora ninguna explicaba que la respuesta
    es codigo Mermaid y no una imagen exportada.
    """
    taller = TALLERES_EXAMLAB.get(n) or {}
    return any(p.get("tipo") == "diagrama" for p in taller.get("preguntas", []))


def _slide_map(c: dict) -> list:
    """Titulos de las diapositivas de esta clase, EN ORDEN.

    Refleja los mismos condicionales que `build_pptx`. El guion docente numera sus
    referencias con esta lista para que se pueda leer con la presentacion
    proyectada, y `build_pptx` verifica al final que las dos coincidan: si alguien
    agrega una diapositiva y olvida el mapa, el build falla en vez de publicar un
    guion que apunta a la diapositiva equivocada.
    """
    n = c["n"]
    if c["tipo"] == "parcial":
        return [f"Portada · Clase {n} · {c['tema']}",
                "Indicaciones (dia de parcial)",
                f"Parcial · Clase {n}"]
    m = [f"Portada · Clase {n} · {c['tema']}",
         "Agenda de hoy (120 min)",
         "Objetivos de la clase",
         "PI CloudLite — entregable de hoy"]
    m += [x[0] for x in c.get("slides_extra", [])]
    dg = DIAGRAMAS.get(n)
    if dg:
        m.append(dg["titulo"])
    ad = ANTES_DESPUES_ARQ.get(n)
    if ad:
        m.append(ad["titulo"])
    cs = CODIGO_SLIDE.get(n)
    if cs:
        m.append(cs[0])
    if _herramientas_de(c):
        m.append("Herramientas de hoy")
    if _tiene_diagrama(n):
        m.append(FLUJO_SLIDE_TITULO)
    m.append("Sustentación (paso a paso)" if c["tipo"] == "sustentacion"
             else "Taller PI (paso a paso)")
    m.append("Para continuar (PI)")
    m.append(f"Clase {n} · cierre del PI CloudLite" if c["tipo"] == "sustentacion"
             else f"Clase {n} · PI en movimiento")
    return m


def _slide_no(mapa, *fragmentos):
    """Numero (1-based) de la primera diapositiva cuyo titulo contiene el fragmento."""
    for frag in fragmentos:
        f = frag.lower()
        for i, t in enumerate(mapa, 1):
            if f in t.lower():
                return i
    return None


def _slide_tag(mapa, *fragmentos) -> str:
    """`[Slide 8]` listo para pegar en el guion, o cadena vacia si no aplica."""
    i = _slide_no(mapa, *fragmentos)
    return f"[Slide {i}] " if i else ""


# --- Referencias a diapositivas dentro del fundamento teorico ---------------
# En la prosa se escribe «{{slide:Teoria Core}}» y aqui se convierte en
# «diapositiva 4» usando el mapa real del deck. Asi el numero no se escribe a mano
# en ningun sitio y no puede quedar corrido.
_SLIDE_TOKEN = re.compile(r"\{\{\s*slide:\s*([^}]+?)\s*\}\}")


def _resolver_slides(texto, mapa, n_clase):
    def _rep(m):
        frag = m.group(1)
        i = _slide_no(mapa, frag)
        if i is None:
            raise SystemExit(
                f"Clase {n_clase}: el fundamento referencia la diapositiva "
                f"«{frag}», que ya no existe en el deck. Corrige el texto o "
                "_slide_map()."
            )
        return f"diapositiva {i}"
    return _SLIDE_TOKEN.sub(_rep, texto)


def _verificar_mapa(c: dict, prs) -> None:
    """Aborta si `_slide_map` y el deck real dejaron de coincidir."""
    esperado, real = len(_slide_map(c)), len(prs.slides)
    if esperado != real:
        raise SystemExit(
            f"Clase {c['n']}: el deck tiene {real} diapositivas y _slide_map() "
            f"declara {esperado}. Actualiza _slide_map() en "
            "build_uniajc_arq_clases_batch.py para que el guion siga apuntando a "
            "las diapositivas correctas."
        )


def build_pptx(c: dict) -> Path:
    n = c["n"]
    folder = CURSO / "Clases" / f"Clase {n} - {c['slug']}"
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / "Presentacion.pptx"

    if c["tipo"] == "parcial":
        prs = new_prs()
        cover_slide(prs, n, c["tema"], "Solo evaluación · sin tema de trabajo dirigido", c["pi_hoy"])
        content_slide(prs, "Indicaciones", [
            "Hoy es **solo Parcial** (virtual síncrono por Meet).",
            "No hay taller ni avance dirigido del PI en esta clase.",
            "Material de evaluación en carpeta docente de Parciales (no se distribuye antes).",
            "La prep del PI / pitch quedó en la clase regular anterior.",
        ], idx=2)
        closing_slide(prs, f"Parcial · Clase {n}", [
            "Enfocados en la evaluación del corte",
            "PI CloudLite continúa en la siguiente clase regular/autónoma",
        ], accent="Solo evaluación")
        _verificar_mapa(c, prs)
        prs.save(str(out))
        print("OK pptx parcial ->", out)
        return out

    prs = new_prs()
    cover_slide(prs, n, c["tema"], c["sub"], c["pi_hoy"], tipo=c["tipo"])
    idx = 2
    if c["tipo"] == "sustentacion":
        # El bloque no se reparte en teoría + taller: son turnos de sustentación
        # en vivo. Proyectar la agenda genérica aquí haría creer que todavía queda
        # tiempo de trabajo en clase, y el estudiante llegaría a subir archivos.
        agenda = [
            "**0–10** Encuadre + sorteo del orden de turnos.",
            "**10–110** Sustentaciones: **6 min de pitch + 2–4 min de Q&A** por turno.",
            "**110–120** Cierre del curso.",
            "El paquete debe estar **subido a ExamLab antes** de tu turno.",
            "Sesión **síncrona**: la defensa no se reemplaza por video grabado.",
        ]
    else:
        agenda = [
            "**0–10** Encuadre: hoy avanzamos el PI en… + entregable concreto.",
            "**10–40** Teoría Core breve (solo lo necesario para el taller PI).",
            f"**40–100** Taller guiado PI (demo en vivo + {mod(c, 'agenda_taller_nota')}).",
            "**100–115** Revisión de evidencias del PI.",
            "**115–120** Cierre: criterio de éxito + plazo domingo 23:59.",
        ]
    content_slide(prs, "Agenda de hoy (120 min)", agenda, idx=idx)
    idx += 1
    content_slide(prs, "Objetivos de la clase", c["objetivos"], idx=idx)
    idx += 1
    entregable_bullets = [
        f"@@Entregable:@@ {c['entregable']}",
        f"Herramienta: **{c['herramienta']}**",
        ("Hoy no se construye: se **defiende** lo que ya está en el paquete del PI."
         if c["tipo"] == "sustentacion"
         else "Todo lo que construyan hoy entra al **informe/repo del PI** (no es lab suelto)."),
        mod(c, "equipo_note"),
    ]
    if c.get("ficha_bloques_note"):
        entregable_bullets[-1:-1] = [c["ficha_bloques_note"]]
    content_slide(prs, "PI CloudLite — entregable de hoy", entregable_bullets, idx=idx)
    idx += 1
    for extra in c["slides_extra"]:
        # Una entrada es (titulo, vinetas) o (titulo, vinetas, tabla). La tercera
        # forma existe porque hay conceptos que son una comparacion y salen mejor
        # como tabla; renderizarla aqui, y no en un diccionario aparte, la mantiene
        # en el ORDEN de la teoria y dentro de `conceptos` (que es de donde el
        # guion saca la lista de temas y el reparto de minutos).
        title, bullets_ = extra[0], extra[1]
        tabla = extra[2] if len(extra) > 2 else None
        if tabla:
            table_content(prs, title, tabla["headers"], tabla["rows"],
                          note=tabla.get("note"), col_w=tabla.get("col_w"),
                          fs_body=tabla.get("fs_body", 11), idx=idx)
        else:
            bullets_limpias, imagen = _limpiar_y_capturar(bullets_)
            slide = content_slide(prs, title, bullets_limpias, idx=idx)
            if imagen:
                _add_captura(slide, imagen)
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
    tools = _herramientas_de(c)
    if tools:
        herramientas_slide(prs, tools, title="Herramientas de hoy",
                           sub="Gratis · navegador o free tier · sin cuenta de pago",
                           idx=idx)
        idx += 1
    # Del boceto al codigo: solo donde el taller pide un diagrama. El estudiante
    # disena en Excalidraw/draw.io y entrega Mermaid; sin esta diapositiva llegaba
    # con un PNG a una caja de texto.
    if _tiene_diagrama(n):
        dialectos = examlab_talleres._dialectos_del_taller(TALLERES_EXAMLAB[n])
        steps_visual_slide(
            prs, FLUJO_SLIDE_TITULO,
            examlab_talleres.flujo_diagrama_pasos(
                dialectos[0] if len(dialectos) == 1 else "el tipo que pide el enunciado"),
            sub="El diagrama se entrega como código Mermaid dentro de ExamLab, no como imagen",
            idx=idx)
        idx += 1
    pasos_titulo = ("Sustentación (paso a paso)" if c["tipo"] == "sustentacion"
                    else "Taller PI (paso a paso)")
    content_slide(prs, pasos_titulo, [f"**{i+1}.** {p}" for i, p in enumerate(_pasos(c))], idx=idx)
    idx += 1
    if c["tipo"] == "sustentacion":
        box_note_slide(prs, "Para continuar (PI)", [
            ("info", f"Entregable: {c['entregable']}"),
            ("aclaracion", "El paquete se sube a ExamLab (https://uniaj.examlab.workers.dev/ · módulo Proyectos) **antes** del bloque de sustentaciones."),
            ("advertencia", "La sustentación es **en vivo** y con Q&A: no se acepta video grabado en su lugar."),
        ], idx=idx)
    else:
        box_note_slide(prs, "Para continuar (PI)", [
            ("info", f"Entregable: {c['entregable']}"),
            ("aclaracion", "Subir evidencias al paquete CloudLite (Drive/repo) y a ExamLab (https://uniaj.examlab.workers.dev/) domingo 23:59."),
            ("advertencia", "Sin cloud de pago ni instalaciones obligatorias de hipervisores/Docker Desktop."),
        ], idx=idx)
    idx += 1
    if c["tipo"] == "sustentacion":
        closing_slide(
            prs,
            f"Clase {n} · cierre del PI CloudLite",
            [
                c["pi_hoy"],
                f"Evidencia: {c['entregable']}",
                "Conserva el repo (informe, diagramas, Dockerfile, ci.yml) como portafolio",
            ],
            accent="Arquitectura = decisiones documentadas con sus consecuencias",
        )
    else:
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
    _verificar_mapa(c, prs)
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
            "Actividad individual. Elegir un dominio concreto.",
            "Sugeridos: AgendaU · BiblioLite · InventarioLab · TurnosClinica · EventosCampus.",
            "Plantilla ficha: DOMINIO · PROBLEMA · CAPACIDADES · ACTORES · SISTEMAS EXTERNOS · FUERA DE ALCANCE.",
            "Diagrama: boceto visual en @@Excalidraw o draw.io@@ → conversión a @@Mermaid (C4Context)@@ con ayuda de una IA → pegar y @@renderizar en ExamLab@@.",
        ],
        "pistas": [
            "¿Quién sufre el problema y como lo miden?",
            "¿La caja grande es el sistema CloudLite (no un módulo interno)?",
            "¿Las flechas tienen verbo (reservar, notificar, autenticar)?",
            "¿Los 2-3 sistemas externos coinciden con los System_Ext del diagrama C4?",
            "¿El diagrama quedó pegado como Mermaid y renderizado en ExamLab (no solo como imagen)?",
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
            "Lab en navegador LabEx Docker Playground: sin Docker Desktop obligatorio.",
        ],
        "escenario": [
            "Elegir el servicio principal del C4 (API o web).",
            "Abrir LabEx Docker Playground (labex.io, login con Google/Microsoft); sesión temporal.",
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
            "Demo corta por estudiante (o por equipo, si el docente los autorizó) si el tiempo alcanza.",
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
    bullets(doc, _pasos(c))
    h2(doc, "7. Criterio de éxito")
    bullets(doc, [
        "El artefacto queda en el paquete PI (informe y/o repo) con nombres consistentes.",
        mod(c, "explica_60s_note"),
        "Evidencia adjunta (PNG, enlace lab, YAML, etc.).",
    ])
    if tb.get("pistas"):
        h2(doc, "8. Pistas (checklist vacío — sin solución)")
        bullets(doc, [f"☐ {p}" for p in tb["pistas"]])
    h2(doc, "9. Entrega")
    if c["tipo"] == "sustentacion":
        # No es un taller con plazo del domingo: la sesión es la sustentación en vivo,
        # así que el paquete tiene que estar arriba ANTES del bloque.
        para(doc, "El paquete final se sube a ExamLab (https://uniaj.examlab.workers.dev/ · módulo Proyectos) "
                  "ANTES del bloque de sustentaciones: quien llega a subir archivos consume su propio "
                  "turno. La sustentación es en vivo (5–8 min de pitch + Q&A) en la sesión de clase; no "
                  "se reemplaza por un video grabado. " + mod(c, "entrega_unidad_note"))
    else:
        para(doc, "Entrega en ExamLab (https://uniaj.examlab.workers.dev/ · módulo Talleres) · domingo 23:59 (regla del Acuerdo). "
                  + mod(c, "entrega_unidad_note"))
    if c.get("entrega_oficial_nota"):
        para(doc, c["entrega_oficial_nota"], shade="E8F4FA")
    # 10. Que encuentra en la plataforma. Antes el taller decia «suba el PNG a ExamLab»
    # sin explicar en que forma se responde; ademas pedia exportar de draw.io cuando la
    # plataforma dibuja Mermaid nativo (incluido C4). Esto lo hace explicito.
    _taller_el = TALLERES_EXAMLAB.get(c["n"])
    if _taller_el:
        examlab_talleres.render_estudiante(
            doc, _taller_el, para=para, bullets=bullets,
            add_inline=add_inline_docx, color_titulo=AZUL,
            titulo="10. Que vas a resolver en ExamLab",
        )
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
    1: [("C4 Context de la demo en vivo: asi debe quedar el tablero al terminar",
         "demo-clase01.png")],
    3: [("Build y run del stub en LabEx Docker Playground (lo que debe verse en pantalla)",
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


# ---------------------------------------------------------------------------
# Guion docente: material que el docente necesita ADEMAS del fundamento teorico.
# Antes el plan minuto a minuto era una plantilla generica ("recorre las slides
# de conceptos") que no le decia al docente que hacer ni que decir. Estos tres
# diccionarios son lo que convierte el guion en algo dictable sin preparacion:
#   DEMO_ARQ      -> la demo concreta, paso a paso, que el docente debe repetir
#   ERRORES_ARQ   -> lo que el estudiante hace mal y como corregirlo en el momento
#   PREGUNTAS_ARQ -> preguntas de comprobacion oral (no del quiz) para el cierre
# ---------------------------------------------------------------------------

DEMO_ARQ = {
    1: ("Dibujar en vivo el C4 Context de un CloudLite de ejemplo", [
        "Abra draw.io en blanco y dibuje UNA caja al centro rotulada «CloudLite App».",
        "Agregue 2 monigotes a la izquierda (Usuario final, Administrador) con flechas rotuladas «consulta», «administra».",
        "Agregue 1 caja gris a la derecha rotulada «Pasarela de pagos (externo)» y una flecha «cobra».",
        "Diga en voz alta: «no dibuje que hay ADENTRO de la caja; eso es Clase 4».",
    ]),
    2: ("Llenar un ADR-001 delante del grupo, en 6 lineas", [
        "Abra un Google Doc y escriba los 4 encabezados del ADR: Contexto, Opciones, Decision, Consecuencias.",
        "Contexto: «CloudLite necesita correr una API y una base de datos; lo desarrolla una persona en un semestre y con cero presupuesto».",
        "Opciones: IaaS (control total, mas trabajo operativo) · PaaS (menos control, menos operacion) · SaaS (no aplica, no compramos software hecho).",
        "Decision: PaaS conceptual + contenedores. Consecuencias: se acepta menos control del sistema operativo a cambio de no administrar servidores.",
        "Diga: «un ADR de media pagina que se entiende vale mas que 5 paginas que nadie lee».",
    ]),
    3: ("Construir y correr el stub en LabEx Docker Playground", [
        "Abra labex.io e inicie sesion con su cuenta de Google o Microsoft (advierta en voz alta: la sesion es temporal, guarden capturas antes de cerrarla).",
        "Escriba un Dockerfile minimo en vivo: FROM nginx:alpine y COPY de un index.html de una linea.",
        "Ejecute docker build -t cloudlite-stub . y luego docker run -d -p 80:80 cloudlite-stub.",
        "Ejecute docker ps y senale las columnas IMAGE, STATUS y PORTS: «esta es la evidencia que entregan».",
        "Si la red falla, proyecte las capturas de `Kit docente/Clase 3/Capturas/`.",
    ]),
    4: ("Convertir el Context de la Clase 1 en Containers", [
        "Abra el diagrama C4 Context de la demo de Clase 1 y haga zoom a la caja «CloudLite App».",
        "Reemplace esa caja por 3 cajas internas: «API (REST)», «Base de datos» y «Worker de notificaciones».",
        "Rotule CADA flecha con protocolo y formato: «HTTPS/JSON», «TCP/SQL». Sin flechas sin etiqueta.",
        "Pregunte al grupo por que el worker esta separado; si nadie da una razon de negocio, borrelo en vivo: «eso es microservicios teatro».",
    ]),
    6: ("De amenaza STRIDE a control verificable, en vivo", [
        "Escriba en el tablero: «Tampering: alguien cambia el precio de un item via la API sin permiso».",
        "Pregunte al grupo cual seria el control; guie hasta «autenticacion + validacion de rol antes de aceptar el cambio».",
        "Agregue la columna Evidencia: «en que archivo o diagrama se ve ese control» — sin evidencia, el control no cuenta.",
        "Demo de 1 minuto del anti-patron: muestre un Dockerfile con una API key escrita en texto plano y explique que queda en el historial de la imagen para siempre.",
    ]),
    7: ("Dibujar zonas de confianza sobre el diagrama de despliegue", [
        "En draw.io dibuje dos rectangulos grandes rotulados «Subred publica» y «Subred privada».",
        "Ponga el balanceador en la publica y la base de datos en la privada; dibuje la flecha API -> BD cruzando de una a otra.",
        "Pregunte: «si un atacante llega desde internet, con que se topa primero?» — eso es superficie de exposicion.",
        "Verifique en voz alta que los nombres de los servicios son LOS MISMOS del C4 Containers de la Clase 4.",
    ]),
    8: ("Un workflow de GitHub Actions que corra de verdad", [
        "Cree `.github/workflows/ci.yml` con on: push, un job y 3 steps: checkout, setup, y un comando de prueba real.",
        "Haga commit y push, y abra la pestana Actions del repositorio para ver el run.",
        "Espere el check verde y senale el log del step: «esto es evidencia, no una diapositiva que dice que tenemos CI».",
        "Aclare la frontera: el pipeline llega hasta «listo para desplegar»; no despliega a ningun servidor real en este curso.",
    ]),
    10: ("Tabla de costo cualitativo en 5 minutos", [
        "Dibuje 3 columnas: Componente | Costo (Bajo/Medio/Alto) | Driver del costo.",
        "Llene 3 filas de CloudLite: base de datos gestionada (Alto, computo+almacenamiento constante 24/7), API en contenedor (Medio, numero de instancias), object storage de imagenes (Bajo, volumen de datos).",
        "Pregunte cual bajaria primero si el presupuesto se corta a la mitad, y exija que justifiquen con el driver, no con intuicion.",
    ]),
    11: ("Auditar en vivo el paquete de un voluntario", [
        "Pida a un estudiante voluntario (o a un equipo, si autorizo equipos) que proyecte su C4 Containers y su diagrama de despliegue lado a lado.",
        "Compare nombre por nombre: todo servicio del Containers debe existir en el despliegue y viceversa.",
        "Senale en voz alta el primer gap concreto que encuentre y escribalo como accion con responsable y fecha.",
        "Modele el tono: el hallazgo es sobre el artefacto, nunca sobre la persona.",
    ]),
    12: ("Definir un objetivo de rendimiento que si se puede verificar", [
        "Escriba la frase mala: «la app debe ser rapida». Pregunte al grupo como la comprobarian; deje que fallen.",
        "Reescribala en vivo: «el p95 del endpoint de consulta responde en menos de 300 ms con 50 peticiones por segundo».",
        "Explique el p95 con 20 numeros en el tablero: ordene y marque el que deja 95% por debajo.",
        "Cierre pidiendo el bottleneck sospechado: «cual pieza creen que revienta primero, y por que esa».",
    ]),
    13: ("Vertical vs horizontal, y lo que NO escala", [
        "Dibuje una caja «API» y agrandela: eso es vertical (mas CPU/RAM a la misma maquina, con techo fisico).",
        "Borre y dibuje 3 cajas «API» iguales con un balanceador arriba: eso es horizontal.",
        "Agregue la base de datos abajo, conectada a las 3, y encierrela en rojo: «esta no se multiplica igual; aqui esta el limite real».",
        "Escriba el trigger y el limite: «CPU > 70% por 5 min -> +1 instancia, maximo 4» y amarre con el costo de la Clase 10.",
    ]),
    15: ("Modelar una sustentacion de 6 minutos y un Q&A", [
        "Presente usted mismo un CloudLite de ejemplo en 6 minutos cronometrados, con la estructura: problema, decision clave, evidencia, limite conocido.",
        "Hagase una pregunta dificil en voz alta y respondala: «por que no uso microservicios? Porque el proyecto lo sostiene una sola persona y la frontera no se justificaba».",
        "Muestre la rubrica proyectada y senale donde habria perdido puntos su propia demo.",
        "Recuerde la regla de los 60 segundos: quien sustenta debe poder explicar cualquier parte del paquete, y si hubo equipo autorizado, cualquier integrante.",
    ]),
}

ERRORES_ARQ = {
    1: ["Dominio vago tipo «una red social» o «un e-commerce»: sin problema concreto no hay decisiones que tomar. Exija sector, usuario y dolor observable.",
        "Dibujar lo que hay DENTRO del sistema en el nivel Context (base de datos, API). Se corrige recordando que eso es el nivel Containers de la Clase 4.",
        "Confundir capacidad con pantalla: «tener un login» no es capacidad; «autenticar usuarios» si."],
    2: ["Elegir el modelo de servicio por moda y no por trade-off. Pida la frase «aceptamos perder X para ganar Y» escrita en el ADR.",
        "ADR sin alternativas descartadas: un ADR con una sola opcion no documenta una decision, documenta un hecho.",
        "Nombrar productos de marca en vez del modelo conceptual; el modelo aplica a cualquier proveedor."],
    3: ["Decir que el contenedor «es una VM ligera». Insista en la diferencia real: kernel propio vs kernel compartido.",
        "Confundir imagen con contenedor al hablar. Corrija en el momento: la imagen es el molde, el contenedor la instancia corriendo.",
        "Perder el trabajo porque la sesion de LabEx Docker Playground se cerro. Recuerdeles guardar el Dockerfile y las capturas ANTES."],
    4: ["Inventar 6 u 8 servicios para verse sofisticados. Pregunte por cada uno: que responsabilidad de negocio propia tiene y quien lo despliega por separado.",
        "Flechas sin etiqueta entre servicios. Toda flecha lleva protocolo y formato de datos.",
        "Olvidar que distribuir agrega fallos parciales: exija al menos 2 riesgos de red en la tabla."],
    6: ["Entregar una lista generica de buenas practicas en vez de amenaza -> control -> evidencia. Devuelva la tabla si no tiene las 3 columnas.",
        "Escribir credenciales en el Dockerfile o en el repositorio. Es el error mas costoso y hay que cortarlo el mismo dia.",
        "Cubrir las 6 categorias STRIDE de forma superficial en vez de 3 bien argumentadas para su dominio."],
    7: ["Dibujar «la nube» como una caja difusa. Exija las dos zonas, publica y privada, explicitas.",
        "Poner la base de datos en la subred publica «para que sea mas facil probar». Es exactamente lo que la Clase 6 acaba de prohibir.",
        "Renombrar servicios respecto al C4 Containers, con lo que los dos diagramas dejan de ser el mismo sistema."],
    8: ["Un workflow que solo hace `echo ok`: es un pipeline decorativo. Exija que corra algo que pueda fallar de verdad.",
        "Decir que ya tienen CD porque el YAML dice deploy. En este curso el despliegue se simula; que lo digan asi.",
        "Golden signals sin umbral: «medimos latencia» no sirve; falta a partir de que valor se considera un problema."],
    10: ["Pedir precios exactos de un proveedor. No es el objetivo: el analisis es cualitativo y por driver.",
         "Marcar todo como costo «Medio» para no pensar. Fuerce al menos un Alto y un Bajo con justificacion.",
         "Olvidar el trafico de red saliente, que es el driver que mas sorprende en facturas reales."],
    11: ["Traer el paquete de la Clase 1 sin actualizar y presentarlo como avance. Compare contra la version anterior.",
         "Conocer solo la parte que se copio de una plantilla y no el paquete completo. Pregunte al azar por cualquier seccion; si hubo equipo autorizado, pregunte a un integrante distinto del que presenta y si solo uno responde, ese es el hallazgo principal.",
         "Confundir este checkpoint con la sustentacion final o con el Parcial 3. Aclarelo al abrir la sesion."],
    12: ["Objetivo de rendimiento sin numero, sin escenario de carga o sin bottleneck. Falta cualquiera de los tres y no es un analisis.",
         "Usar el promedio en vez del p95 y concluir que todo esta bien. Muestre por que el promedio esconde los casos malos.",
         "Ensayar el pitch leyendo las diapositivas. Cronometre y corte a los 8 minutos."],
    13: ["Prometer autoescalado infinito sin limite maximo ni control de costo (Clase 10).",
         "Escalar horizontalmente un servicio que guarda la sesion en memoria local: al repartir la carga, el usuario pierde su sesion.",
         "No documentar QUE NO escala. La base de datos relacional es casi siempre la respuesta y hay que decirlo."],
    15: ["Describir el diagrama en vez de justificar la decision. Reoriente con «por que asi y no de la otra forma».",
         "En equipos autorizados, que un integrante presente y el resto observe. Distribuya el Q&A a proposito entre todos.",
         "Presentar sin mencionar ningun limite del diseno. Quien no reconoce limites no entendio el trade-off."],
}

PREGUNTAS_ARQ = {
    1: ["Cual es la diferencia entre arquitectura y stack tecnologico?",
        "Que va DENTRO y que va FUERA de la caja en un diagrama C4 Context?",
        "Digan una capacidad de su CloudLite que NO sea una pantalla."],
    2: ["Quien administra el sistema operativo en IaaS, en PaaS y en SaaS?",
        "Que perdieron y que ganaron con el modelo que eligieron?",
        "Por que un ADR necesita las alternativas que descartaron?"],
    3: ["Que comparten los contenedores de una misma maquina que las VM no comparten?",
        "Cual es la diferencia entre imagen y contenedor?",
        "Que pasa con su trabajo cuando se cierra la sesion de LabEx Docker Playground?"],
    4: ["Que justifica que dos funciones vivan en servicios separados?",
        "Que cambia cuando una llamada de funcion se vuelve una llamada de red?",
        "Como se llama en su C4 Containers el servicio que expone la API?"],
    6: ["Que significa la T de STRIDE y una amenaza concreta de su CloudLite?",
        "Donde guardan una API key y por que NO dentro de la imagen?",
        "Que evidencia demuestra que su control existe de verdad?"],
    7: ["Que va en la subred publica y que en la privada, y por que?",
        "Que hace un balanceador de carga en una frase?",
        "Cuando conviene object storage y cuando la base de datos?"],
    8: ["Que valida CI y que hace CD, y cual de los dos construyeron hoy?",
        "Digan las 4 golden signals y el umbral de una de ellas.",
        "Que pasaria en su pipeline si alguien sube codigo que no compila?"],
    10: ["Cual es el componente mas caro de su CloudLite y cual es su driver?",
         "Que es right-sizing en una frase?",
         "Como se conecta el autoescalado con el costo?"],
    11: ["Que gap concreto identificaron hoy y quien lo cierra?",
         "Su diagrama de despliegue usa los mismos nombres que su C4 Containers?",
         "Que evidencia de la rubrica les falta todavia?"],
    12: ["Que es el p95 y por que no usamos el promedio?",
         "Cual es su bottleneck sospechado y en que se basan?",
         "Diferencia entre stress test y spike test?"],
    13: ["Vertical u horizontal: cual eligieron y por que?",
         "Cual es su trigger y cual su limite maximo?",
         "Que pieza de su sistema NO escala, y que harian al respecto?"],
    15: ["Justifiquen su decision de arquitectura mas importante en 60 segundos.",
         "Cual es el limite conocido de su diseno actual?",
         "Si tuvieran un mes mas, que cambiarian primero y por que?"],
}


def _lista_md(items, bullet="- "):
    return "\n".join(f"{bullet}{x}" for x in items) if items else ""


# Codigo de referencia del diagrama que el docente dibuja en vivo. Existe porque el
# bloque «Demo en vivo» pedia dibujar un diagrama sin dar ninguna referencia de como
# debe quedar: si el proyector o la red fallan, o si el docente prefiere no dibujar a
# mano, pega este codigo en la pregunta de diagrama de ExamLab y lo proyecta
# renderizado en un minuto. Es el mismo contenido que la imagen de Capturas/.
DEMO_MERMAID = {
    1: ("C4 Context de la demo (el mismo de `Capturas/demo-clase01.png`)", """C4Context
    title CloudLite App - nivel Context (demo de clase)
    Person(usuario, "Usuario final", "Consulta y usa el servicio")
    Person(admin, "Administrador", "Configura y opera")
    System(cloudlite, "CloudLite App", "El sistema completo, como caja negra")
    System_Ext(pagos, "Pasarela de pagos", "Servicio de terceros")
    Rel(usuario, cloudlite, "consulta", "HTTPS")
    Rel(admin, cloudlite, "administra", "HTTPS")
    Rel(cloudlite, pagos, "cobra", "API REST sobre HTTPS")"""),
}


def _demo_md(n: int) -> str:
    d = DEMO_ARQ.get(n)
    if not d:
        return "Muestre en vivo la herramienta del dia con un mini-ejemplo de CloudLite.\n"
    titulo, pasos = d
    cuerpo = "\n".join(f"{i + 1}. {p}" for i, p in enumerate(pasos))
    md = f"**Demo que usted debe poder repetir:** {titulo}\n\n{cuerpo}\n"
    ref = DEMO_MERMAID.get(n)
    if ref:
        rotulo, codigo = ref
        md += (
            f"\n**Referencia del resultado:** {rotulo}. Si la red falla o prefiere no "
            "dibujar a mano, pegue este codigo en la pregunta de diagrama de ExamLab y "
            "proyectelo renderizado; tambien sirve para volver a generar la imagen en "
            "cualquier editor que soporte Mermaid.\n\n"
            "```mermaid\n" + codigo + "\n```\n"
        )
    return md


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
Verificar asistencia y que todos entren al Meet.

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

    # El desarrollo completo del tema vive en arq_fundamentos.py (modulo de datos,
    # misma convencion que prog2_clases_data / seminario_clases_data). Antes estaba
    # inline y en 4-5 parrafos, insuficiente para la regla de oro del workspace:
    # el guion debe permitir dictar la clase sin consultar otra fuente.
    fund = FUNDAMENTOS.get(
        n, "Teoria al servicio del entregable PI de hoy. Ver diapositivas de la clase."
    )
    fund = _resolver_slides(fund, _slide_map(c), n)

    # Conceptos reales de esta clase (titulos de las slides de teoria), para que el
    # plan diga QUE cubrir en cada tramo en vez de "recorre las slides".
    conceptos = [x[0] for x in c.get("slides_extra", [])]
    conceptos_md = _lista_md(conceptos) or "- Ver diapositivas de la clase."
    minutos_por_concepto = max(5, 30 // max(1, len(conceptos)))

    # Modalidad de trabajo (individual por defecto, equipos si el docente los autoriza).
    # Las dos ramas de abajo usan las MISMAS variables para no volver a divergir.
    arranque_cita = mod(c, "arranque_cita")
    arranque_nota = mod(c, "arranque_nota")
    voluntario_word = mod(c, "voluntario_word")
    taller_modalidad_word = mod(c, "taller_modalidad_word")
    retro_word = mod(c, "retro_word")
    criterio_60s_note = mod(c, "criterio_60s_note")

    # Mapeo real del deck: el guion se lee CON la presentacion proyectada, asi que
    # cada tramo del plan dice a que diapositiva corresponde. Sale de _slide_map(),
    # la misma lista que arma build_pptx, no de numeros escritos a mano.
    mapa = _slide_map(c)
    sl_agenda = _slide_tag(mapa, "Agenda de hoy").strip()
    sl_obj = _slide_tag(mapa, "Objetivos de la clase").strip()
    sl_entreg = _slide_tag(mapa, "entregable de hoy").strip()
    sl_teoria = _slide_tag(mapa, *(conceptos or ["Objetivos"])).strip()
    sl_flujo = _slide_tag(mapa, FLUJO_SLIDE_TITULO).strip()
    sl_taller = _slide_tag(mapa, "paso a paso").strip()
    sl_cierre = f"[Slide {len(mapa)}]"
    mapa_md = "\n".join(f"{i}. {t}" for i, t in enumerate(mapa, 1))
    # Bloque del flujo de diagramacion: solo si el taller de hoy pide un diagrama.
    if _tiene_diagrama(n):
        _dial = examlab_talleres._dialectos_del_taller(TALLERES_EXAMLAB[n])
        flujo_guion = (
            "\n**Cierra la demo dentro de ExamLab** " + sl_flujo + " — es el paso que el "
            "estudiante no adivina: pasa el boceto a codigo Mermaid con ayuda de una IA, "
            "pegalo en la pregunta de diagrama y muestralo renderizado.\n\n"
            + examlab_talleres.flujo_diagrama_md(
                _dial[0] if len(_dial) == 1 else "el tipo que pide el enunciado")
            + "\n"
        )
    else:
        flujo_guion = ""

    if not c.get("separar_notas_docente"):
        # Plantilla compartida por las clases que no separan «lo que el docente dice»
        # de «las notas para el docente». Cualquier cambio aqui se propaga a esas
        # clases en su proximo build; las frases de modalidad de trabajo estan
        # parametrizadas arriba, no las vuelvas a escribir a mano.
        plan_blocks = f"""### 0–10 · Encuadre PI · {sl_agenda}{sl_obj}{sl_entreg}
Di casi literal: «Hoy avanzamos el PI CloudLite App en: **{c['pi_hoy']}**.
Entregable concreto: {c['entregable']}.
Teoría breve y luego taller; no es un lab suelto.»
Pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.
Pregunta de arranque (1 min): «{arranque_cita}» — sirve para detectar estudiantes rezagados antes de avanzar.

### 10–40 · Teoría Core (al servicio del taller) · desde {sl_teoria}
Cubre estos conceptos, en este orden, ~{minutos_por_concepto} min cada uno (son los títulos de las diapositivas de teoría):
{conceptos_md}

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente»:
esa sección está escrita para que puedas dictarla sin consultar otra fuente.
Cada 8–10 min amarra al artefacto: «esto es lo que van a dejar hoy en su informe/diagrama/repo».
Pide un {voluntario_word} voluntario y usa SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · {sl_flujo}
Herramienta del día: **{c['herramienta']}**.
{_demo_md(n)}
Narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase {n}/Capturas/`.
Cierra la demo con: «copien la estructura, no el dominio de mi ejemplo.»
{flujo_guion}{_capturas_md(n)}

### 55–100 · Taller guiado PI ({taller_modalidad_word}) · {sl_taller}
Proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller» de este guion).
Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas a ver hoy.
A los 80 min anuncia: «faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador.»

### 100–115 · Comprobación y evidencias
Haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase {n}/Quiz Clase {n} - {c['slug']}.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 {retro_word} en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · {sl_cierre}
Di: «Queda avanzado: {c['pi_hoy']}.
Criterio de éxito: {criterio_60s_note}.
Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan.»
"""
    else:
        # Rama exclusiva para clases con actividad individual (hoy: Clase 1), donde se
        # separa explicitamente lo que el docente DICE (bloques "> ...") de las
        # instrucciones PARA el docente (bloques "**[Nota docente]:**").
        plan_blocks = f"""### 0–10 · Encuadre PI · {sl_agenda}{sl_obj}{sl_entreg}
Di casi literal:
> "Hoy avanzamos el PI CloudLite App en: {c['pi_hoy']}. Entregable concreto: {c['entregable']}. Teoría breve y luego taller; no es un lab suelto."

**[Nota docente]:** pasa la diapositiva de agenda y la de objetivos. Abre el enunciado PI si alguien aún no lo tiene.

**[Nota docente]:** {arranque_nota}
> "{arranque_cita}"

### 10–40 · Teoría Core (al servicio del taller) · desde {sl_teoria}
Cubre estos conceptos, en este orden, ~{minutos_por_concepto} min cada uno (son los títulos de las diapositivas de teoría):
{conceptos_md}

El desarrollo completo de cada uno está arriba, en «Fundamento teórico para el docente», ya dividido
por diapositiva: esa sección está escrita para que puedas dictarla sin consultar otra fuente.

**[Nota docente]:** cada 8–10 min amarra al artefacto («esto es lo que van a dejar hoy en su informe/diagrama/repo»)
y pide un {voluntario_word} voluntario para usar SU dominio como ejemplo en vivo (no el de la demo).

### 40–55 · Demo en vivo · {sl_flujo}
Herramienta del día: **{c['herramienta']}**.
{_demo_md(n)}

**[Nota docente]:** narra los clics en voz alta. Si falla la red, proyecta las capturas de `Kit docente/Clase {n}/Capturas/`.
Cierra la demo diciendo:
> "Copien la estructura, no el dominio de mi ejemplo."
{flujo_guion}{_capturas_md(n)}

### 55–100 · Taller guiado PI ({taller_modalidad_word}) · {sl_taller}
**[Nota docente]:** proyecta la lista de pasos del taller del estudiante (está en la sección «Actividad / taller»
de este guion). Circula por mesas/Meet con la lista de errores frecuentes de abajo en la mano: son los que vas
a ver hoy. A los 80 min anuncia:
> "Faltan 20 min. Falta evidencia: PNG/YAML/enlace. Empiecen a subir borrador."

### 100–115 · Comprobación y evidencias
**[Nota docente]:** haz 3–4 de las preguntas de comprobación oral de abajo, a personas distintas y al azar
(no al que levanta la mano). Es el mecanismo para verificar la regla de los 60 segundos.
Aplica el quiz corto de `Kit docente/Clase {n}/Quiz Clase {n} - {c['slug']}.docx`
(la clave va en archivo aparte y **no se proyecta**).
Mientras responden, verifica que el entregable esté realmente subido.
Retroalimenta 2–3 {retro_word} en voz alta, nombrando el error y la corrección concreta.

### 115–120 · Cierre · {sl_cierre}
Di:
> "Queda avanzado: {c['pi_hoy']}. Criterio de éxito: {criterio_60s_note}. Entrega domingo 23:59 en ExamLab. Siguiente hito del PI según el plan."
"""

    if c["tipo"] == "autonoma":
        plan_blocks = f"""### Modalidad autónoma (festivo)
Esta clase cae en festivo: no hay encuentro síncrono obligatorio. El estudiante trabaja solo,
con `Presentacion.pptx` + el taller de la carpeta `Clases/`. Por eso el material publicado
tiene que ser **autosuficiente**: lo que no quede escrito, nadie lo va a explicar en vivo.

### Qué publicar (antes del día de la clase)
1. En ExamLab: las diapositivas, el taller y el recordatorio del hito del PI.
2. La sección «Fundamento teórico para el docente» de este guion, adaptada como **lectura guía**
   del estudiante — es el reemplazo de la explicación en vivo, no un anexo opcional.
3. La **salida esperada** del ejercicio (ver la demo de abajo), para que el estudiante autónomo
   pueda comparar y saber si le quedó bien sin preguntarte.
4. Mensaje sugerido: «Clase {n} autónoma (festivo). Hoy avanzamos el PI en: {c['pi_hoy']}.
   Entregable: {c['entregable']}. Fecha límite: domingo 23:59. Dudas por foro/correo institucional.»

### Cómo debería repartir su tiempo el estudiante (120 min equivalentes)
- **0–15** Leer el encuadre y el objetivo del día; ubicar en qué quedó su CloudLite.
- **15–45** Leer la teoría (lectura guía) y tomar notas directamente en el informe del PI.
- **45–60** Revisar la salida esperada del ejercicio resuelto.
- **60–105** Desarrollar el taller sobre su propio CloudLite.
- **105–120** Empaquetar la evidencia y subirla a ExamLab.

### La demo, en versión asíncrona
{_demo_md(n)}
Publica esto como pasos escritos o como un video corto (3–5 min) grabado con estos mismos pasos.
Sin uno de los dos, el estudiante autónomo no tiene con qué comparar su resultado.
{_capturas_md(n)}

### Seguimiento (lo que sí es tu trabajo esa semana)
1. Revisa las entregas del domingo 23:59 con la lista de errores frecuentes de abajo:
   en modalidad autónoma esos errores aparecen más, porque nadie los corrigió en el momento.
2. Deja feedback breve orientado a la rúbrica del PI, nombrando el error y la corrección.
3. En la siguiente clase regular, dedica los primeros 10 min a los 2 errores más repetidos.
   Es el sustituto de la retroalimentación en vivo que esta clase no tuvo.

### Si ofreces office hours voluntario (opcional, 20–30 min)
Resuelve bloqueos concretos de diagrama/ADR/lab. Usa las preguntas de comprobación de abajo
para detectar quién entendió y quién solo copió la plantilla. No adelantes contenido de Parcial.
"""

    if c["tipo"] == "sustentacion":
        plan_blocks = f"""### Modalidad de la sesión: sustentaciones EN VIVO
Este bloque de 120 min se dedica íntegramente a las sustentaciones del Proyecto Integrador,
con encuentro síncrono. **No es clase autónoma y no es parcial.** No autorices reemplazar la
defensa por un video grabado: la sustentación es el único instrumento con el que verificas
autoría de los otros puntos del PI, y el Q&A en vivo no se puede sustituir por un documento.
El día cae en festivo de calendario, pero la sesión está destinada por decisión docente a
sustentar: anúncialo por escrito una semana antes para que nadie asuma que no hay clase.

### Antes de la sesión (semana previa)
1. Publica el orden y la duración exacta del turno: **6 min de pitch + 2–4 min de Q&A**.
   Con 12 sustentaciones eso es ~110 min; si el grupo es más grande, baja a 5 + 2 y avísalo
   antes, nunca el mismo día.
2. Exige el paquete subido a ExamLab (módulo Proyectos) **antes** del bloque: quien llega a
   subir archivos consume el tiempo de otro. Verifica tú mismo que los enlaces abren.
3. Ten a mano la rúbrica impresa por estudiante y la lista de preguntas de comprobación de
   abajo, para no improvisar el Q&A ni preguntar lo mismo a todos.
4. Si en la clase anterior no alcanzaron a ensayar, modela tú el formato antes de abrir turnos
   (no dentro de este bloque: no hay tiempo para eso y una sustentación menos):

{_demo_md(n)}

### 0–10 · Encuadre y orden de turnos
Di casi literal:
> "Hoy sustentamos. 6 minutos de pitch y hasta 4 de preguntas. Yo corto a los 6 minutos: si no
> llegaron a seguridad, costos y escala, esa parte no se califica. El orden lo sorteo ahora."

**[Nota docente]:** sortea el orden delante del grupo (evita el reclamo de «me tocó primero»),
proyecta el cronómetro y pide que el resto escuche: cerramos el curso entre todos.

### 10–110 · Sustentaciones (turnos consecutivos)
Por cada turno, en este orden:
1. **6 min de pitch.** No interrumpas ni siquiera para corregir un error: se anota y se pregunta
   después. Corta seco a los 6 min.
2. **2–4 min de Q&A.** Haz siempre una pregunta de verificación («muéstrame el .yml del
   workflow»), una de profundización («¿por qué la base de datos no está en el mismo contenedor
   que la API?») y, si queda tiempo, una hipotética («si el tráfico se multiplica por diez el
   lunes, ¿qué pieza se rompe primero?»). En equipo autorizado, dirige cada pregunta a un
   integrante distinto y **no** dejes que responda siempre el mismo.
3. **Cierra el turno con la nota puesta**, no al final del día: la rúbrica se llena en caliente
   mientras recuerdas la respuesta exacta.

**[Nota docente]:** frase de rescate cuando el estudiante se bloquea, para no perder el turno:
> "Déjame la respuesta pendiente y sigue con el siguiente bloque; vuelvo a preguntar al final."

### 110–120 · Cierre del curso
Di casi literal:
> "Lo que entregaron —diagramas, Dockerfile, workflow, informe— es un portafolio real: no lo
> borren al terminar el semestre. Arquitectura no es una lista de logos de proveedores, es un
> conjunto de decisiones documentadas con sus consecuencias."

Recuerda los pesos sin abrir discusión de notas: el PI vale **20% del Corte 3** y el Parcial 3
ya se aplicó en su propia sesión; el proyecto no reemplaza ni compensa el parcial.

### Si un estudiante no se presenta o falla la conexión
Deja constancia escrita en el momento (hora, motivo) y reprograma dentro de la misma semana con
Meet, sustentando igualmente en vivo. Aceptar un video grabado «por esta vez» convierte la
excepción en la regla del semestre siguiente y elimina el Q&A, que es la mitad de lo que evalúas.
"""

    pasos = "\n".join(f"{i+1}. {p}" for i, p in enumerate(_pasos(c)))
    return f"""# Guion docente — Clase {n}: {c['tema']}

## Información de la clase
- Asignatura: Arquitectura de Sistemas Computacionales (FI303380)
- Duración del bloque: **120 min**
- Tipo: {TIPO_LABEL[c["tipo"]]}
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

## Referencias a diapositivas
Numeración real del deck `Clases/Clase {n} - {c['slug']}/Presentacion.pptx` (solo tema
de esta clase). Las etiquetas [Slide N] del plan y del fundamento apuntan aquí.

{mapa_md}

## Plan de clase minuto a minuto (120 min)

{plan_blocks}

## Actividad / taller (detalle)
{pasos}

### Criterio de éxito
- Artefacto integrado al paquete PI (no archivo huérfano).
- Evidencia adjunta.
- {mod(c, "criterio_oral_note")}

## Errores frecuentes del estudiante (y cómo corregirlos en el momento)
{_lista_md(ERRORES_ARQ.get(n, [])) or "- Sin errores catalogados para esta clase."}

## Preguntas de comprobación oral (no son del quiz)
{"Úsalas como Q&A al cerrar cada turno de sustentación, variándolas entre estudiantes." if c["tipo"] == "sustentacion" else "Úsalas en el tramo 100–115, a personas distintas y al azar."}
{_lista_md(PREGUNTAS_ARQ.get(n, []), bullet="1. ") or "- Sin preguntas catalogadas para esta clase."}

## Solución del taller (privada)
`Kit docente/Clase {n}/Solucion Taller Clase {n} - CloudLite.docx` — es la referencia con la que
comparas lo que entregan {mod(c, "entregan_word")}. **No proyectarla completa** antes de que trabajen.

## Quiz
`Kit docente/Clase {n}/Quiz Clase {n} - {c['slug']}.docx` (versión estudiante, sin respuestas)
y `Kit docente/Clase {n}/Quiz Clase {n} - CLAVE DOCENTE.docx` (clave, privada).

## Capturas sugeridas
- 📸 La herramienta del día en uso con el artefacto CloudLite [[captura: demo-clase{n:02d}.png | receta: 1) Abre {c['herramienta']} y repite la demo de este guion.  2) Captura solo la ventana útil, no el escritorio completo.  3) Recorta a ~1200 px de ancho.  4) Guárdala como Kit docente/Clase {n}/Capturas/demo-clase{n:02d}.png.  5) Vuelve a generar el guion y la imagen queda embebida aquí sola. Detalle en Capturas/README.txt.]]
- 📸 Evidencia del entregable de un estudiante (diagrama / YAML / lab) [[captura: evidencia-clase{n:02d}.png | receta: 1) Con permiso del estudiante, captura su artefacto de hoy.  2) Recorta nombre y correo antes de guardar.  3) Guárdala como Kit docente/Clase {n}/Capturas/evidencia-clase{n:02d}.png.  4) Es para tu registro del corte; no se proyecta en clase.]]

## Notas operativas
- Plataforma de entrega: ExamLab (https://uniaj.examlab.workers.dev/). No es la plataforma oficial de la UNIAJC; la universidad no tiene campus virtual propio.{chr(10) + "- " + c["entrega_oficial_nota"] if c.get("entrega_oficial_nota") else ""}
- Prohibido pedir cloud con tarjeta: todo el curso corre con free tier o en el navegador.
- Día de parcial = solo evaluación (no aplica a esta clase).
"""


def _escribir_readme_capturas(c: dict, cap: Path) -> None:
    """README de la carpeta Capturas/ con el paso a paso de cada imagen.

    Antes era una linea generica («preferir PNG reales») que no decia que abrir ni
    con que nombre guardar, asi que las carpetas quedaban vacias y el .docx salia
    con la caja de captura en blanco el dia de la clase. Se reescribe en cada build
    para que refleje la herramienta y la demo actuales de la clase.
    """
    n = c["n"]
    demo = DEMO_ARQ.get(n)
    L = [f"Capturas de la Clase {n} — Arquitectura de Sistemas Computacionales",
         "=" * 62, "",
         "El guion embebe automaticamente cualquier PNG que exista aqui con el nombre",
         "esperado. Mientras no exista, el .docx imprime la receta en su lugar.", ""]
    ya = CAPTURAS_CLASE.get(n) or []
    if ya:
        L.append("Ya generadas por `python config/slides/mockups.py` (no hay que tomarlas):")
        for rotulo, fn in ya:
            L.append(f"  - {fn} — {rotulo}")
        L.append("")
    L += [f"Pendiente: demo-clase{n:02d}.png — la herramienta del dia en uso",
          f"  1. Abrir {c['herramienta']}."]
    if demo:
        L.append(f"  2. Repetir la demo: {demo[0]}.")
        for i, paso in enumerate(demo[1], 1):
            L.append(f"     {i}. {paso}")
    else:
        L.append("  2. Reproducir el ejercicio del bloque sobre el dominio CloudLite de ejemplo.")
    L += ["  3. Capturar solo la ventana util, no el escritorio completo.",
          "  4. Recortar a ~1200 px de ancho.",
          f"  5. Guardar aqui como demo-clase{n:02d}.png.",
          "",
          "Pendiente: evidencia del entregable (diagrama / YAML / lab)",
          "  - Con permiso del estudiante, capturar su artefacto de hoy.",
          "  - Recortar nombre y correo antes de guardar. No se proyecta en clase.",
          "",
          "Despues de agregar una imagen, regenerar el guion:",
          f"  SOLO_CLASES={n} python config/slides/build_uniajc_arq_clases_batch.py",
          ""]
    cap.mkdir(parents=True, exist_ok=True)
    (cap / "README.txt").write_text("\n".join(L), encoding="utf-8")


def build_guion(c: dict) -> Path:
    n = c["n"]
    kit = CURSO / "Kit docente" / f"Clase {n}"
    cap = kit / "Capturas"
    kit.mkdir(parents=True, exist_ok=True)
    cap.mkdir(parents=True, exist_ok=True)
    # placeholder readme capturas
    _escribir_readme_capturas(c, cap)
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

- Bloque 120 min · virtual síncrono por Meet · **sin taller PI**.
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


def build_examlab_guia(c):
    """Guia para armar el taller de esta clase dentro de ExamLab.

    Va en el Kit docente porque la plataforma no importa preguntas desde archivo:
    el docente las crea en la UI y necesita el texto exacto de cada campo.
    """
    taller = TALLERES_EXAMLAB.get(c["n"])
    if not taller:
        return None
    d = CURSO / "Kit docente" / f"Clase {c['n']}"
    d.mkdir(parents=True, exist_ok=True)
    md = examlab_talleres.guia_docente_md(
        c["n"], taller, "Arquitectura de Sistemas Computacionales (FI303380)",
        hito=c.get("pi_hoy"), entregable=c.get("entregable"),
    )
    out = d / f"Taller en ExamLab - Clase {c['n']} (configuracion).md"
    out.write_text(md, encoding="utf-8")
    print("OK examlab ->", out)
    return out


def build_all(solo_clases=None):
    """Regenera el batch completo, o solo un subconjunto de clases si se pasa
    ``solo_clases`` (iterable de numeros de clase) o se define la variable de
    entorno SOLO_CLASES="1,3,7" (coma-separada). Las clases no incluidas no se
    tocan, para poder aislar un cambio (p.ej. reemplazo de una herramienta de
    lab) a las clases afectadas sin regenerar el resto del curso.
    """
    if solo_clases is None:
        env_val = os.environ.get("SOLO_CLASES")
        if env_val:
            solo_clases = {int(x.strip()) for x in env_val.split(",") if x.strip()}
    else:
        solo_clases = set(solo_clases)
    guiones = []
    for c in CLASSES:
        n = c["n"]
        if solo_clases is not None and n not in solo_clases:
            continue
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
        build_examlab_guia(c)
        g = build_guion(c)
        guiones.append(g)
    convert_guiones(guiones)
    print("\nDONE batch Arquitectura PI-first")


if __name__ == "__main__":
    build_all()
