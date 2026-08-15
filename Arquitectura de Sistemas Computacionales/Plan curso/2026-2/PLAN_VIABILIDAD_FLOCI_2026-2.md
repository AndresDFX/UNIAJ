# Plan de viabilidad — Floci (Arquitectura de Sistemas Computacionales · 2026-2)

| Campo | Valor |
|---|---|
| Curso | Arquitectura de Sistemas Computacionales (FI303380) |
| Grupo | **6303C** |
| Docente | Julian Andres Castaño Espinosa · `julianacastano@profesores.uniajc.edu.co` |
| PI | **CloudLite** |
| Fecha | 2026-08-07 |
| Estado | **Borrador para aprobación docente** |

---

## 1. Resumen ejecutivo

**Veredicto: viable condicionado.**

Floci **no es** un free tier de AWS/GCP/Azure/OCI con tarjeta. Es una familia de **emuladores locales** (MIT, $0) que reproducen APIs cloud en el PC o en un lab con Docker, **sin cuenta cloud y sin tarjeta**.

Eso **alinea mejor** con la política UNIAJC “sin costos / sin tarjeta” que Oracle/GCP/AWS Free Tier (retirados del plan por pedir tarjeta). El trade-off es otro: **rompe el criterio “solo navegador / sin instalación”**, porque hace falta **Docker** (local o en Killercoda / LabEx Docker Playground).

| Criterio | Resultado |
|---|---|
| Gratis / sin tarjeta | **Sí** (MIT, sin auth token, sin billing) |
| Sin cuenta cloud real | **Sí** (credenciales dummy / throwaway) |
| Solo navegador | **No** (Docker obligatorio para el camino local) |
| Clase 120 min usable | **Sí, si** la imagen se pre-descarga o se usa lab en navegador |
| Apto para CloudLite | **Sí** (storage, colas, funciones, IAM local) |

**Recomendación:** piloto en **Clase 7 (Redes y almacenamiento cloud)** con `floci` (AWS/S3) vía script; mantener Killercoda / LabEx Docker Playground / draw.io como camino principal hasta aprobar el piloto. No reescribir el semestre todavía.

---

## 2. Qué es cada variante

Sitio: [https://floci.io/](https://floci.io/) · Org GitHub: [https://github.com/floci-io](https://github.com/floci-io)

Nombre: de *cirrocumulus floccus* (“nubes tipo palomitas”). Familia de emuladores locales multi-cloud.

| Variante | Cloud emulado | Puerto | Imagen Docker | Repo | Cobertura (resumen) |
|---|---|---:|---|---|---|
| **floci** | AWS | 4566 | `floci/floci:latest` | [floci-io/floci](https://github.com/floci-io/floci) (~18k★) | ~69 servicios (S3, SQS, Lambda, DynamoDB, IAM, ECS/EKS, etc.). Drop-in vs LocalStack |
| **floci-az** | Azure | 4577 | `floci/floci-az:latest` | [floci-io/floci-az](https://github.com/floci-io/floci-az) | Blob, Queue, Table, Functions, Key Vault, Event Hubs, Service Bus, etc. |
| **floci-gcp** *(también “floc-gcp”)* | GCP | 4588 | `floci/floci-gcp:latest` | [floci-io/floci-gcp](https://github.com/floci-io/floci-gcp) | GCS, Pub/Sub, Firestore, Cloud Run, IAM, etc. (~24 servicios) |
| **floci-oci** | Oracle Cloud (OCI) | 4599 | `floci/floci-oci:latest` | [floci-io/floci-oci](https://github.com/floci-io/floci-oci) | Object Storage, Identity, Queue, Streaming, KMS, Vault, Functions |
| **floci-cli** | Todas | — | — | [floci-io/floci-cli](https://github.com/floci-io/floci-cli) | CLI unificada: `floci start`, `floci az start`, `floci gcp start`, `floci oci …` |
| **floci-ui** | Todas | — | — | [floci-io/floci-ui](https://github.com/floci-io/floci-ui) | Dashboard visual (opcional, no necesario en MVP) |

> Nota de nomenclatura docente: “floc-gcp” = **floci-gcp**. “floci + oci” = **floci-oci**.

### Propósito pedagógico
Practicar **APIs y CLIs cloud reales** (aws / az / gcloud / oci) apuntando a `localhost`, sin riesgo de factura ni provisioning de cuentas institucionales.

### Licencia y costos
- **Licencia:** MIT (“forever free”).
- **Costo estudiante:** $0.
- **Auth token:** no (contraste con LocalStack Community, que desde 2026 exige token).
- **Límites de uso:** no hay cuota de proveedor; el límite es CPU/RAM/disco del equipo o del lab.

### Requisitos técnicos (familia)
| Requisito | Detalle |
|---|---|
| Cuenta AWS/Azure/GCP/OCI | **No** |
| Tarjeta | **No** |
| Free tier cloud | **No aplica** (no es nube real) |
| Docker Engine / Desktop | **Sí** (recomendado; Lambda/Functions/RDS usan socket Docker) |
| OS | Linux, macOS, **Windows** (`install.ps1`) |
| CLI cloud (opcional pero útil) | AWS CLI / Azure CLI / gcloud / OCI CLI según variante |
| Red | Primera vez: pull de imagen (~90 MB floci nativo; más si hay sidecars) |
| Alternativa sin PC local | LabEx Docker Playground / Killercoda con `docker run …` |

---

## 3. Contraste con la política vigente del curso

### Política actual (post-limpieza docente)
- **Gratis + navegador / free tier sin tarjeta.**
- Regla previa: **quitar AWS / GCP / Oracle Cloud** de herramientas “de tarjeta”.
- Stack vigente propuesto: **draw.io**, **Excalidraw**, **Killercoda / LabEx Docker Playground**, **GitHub Actions** (opcional), Docs/Padlet.
- **No** exigir VirtualBox/VMware/Docker Desktop como requisito del curso.

### Trade-off honesto con Floci

| Pregunta | Respuesta |
|---|---|
| ¿Sigue sin tarjeta? | **Sí.** Floci no cobra ni pide tarjeta. |
| ¿Es OCI Always Free / Azure for Students / AWS Free Tier? | **No.** No usa esos programas. Emula APIs en local. |
| ¿Rompe “solo navegador”? | **Sí, en el camino local** (Docker Desktop/Engine). |
| ¿Se puede usar sin instalar en el PC? | **Parcialmente:** lab en **LabEx Docker Playground** o escenario **Killercoda** con el mismo `docker run`. |
| ¿Cambia la regla “sin AWS/GCP/Oracle”? | **Sí, con matices:** se puede enseñar *forma* de esas nubes **sin cuentas reales**. No reintroduce riesgo de facturación. Hay que **decir en clase** “esto es emulador, no producción”. |
| ¿Mejor que free tier con tarjeta? | **Para UNIAJC, sí** en seguridad de costos. Peor en “cero instalación”. |

**Conclusión de política:** Floci es una **excepción justificada** a “solo navegador”, no una vuelta a free tiers con tarjeta. Debe quedar marcada como **piloto / camino B**, no como requisito único.

---

## 4. Requisitos por estudiante (piloto)

### Camino A — Local (script del curso)
1. Windows 10/11, Linux o macOS con **Docker Desktop** (o Engine) corriendo.
2. 4 GB RAM libres recomendados (8 GB ideal si se usan Functions/Lambda).
3. Ejecutar script MVP (`scripts/lab-floci.ps1` o `.sh`) → pull + arranque + variables de entorno.
4. Opcional: AWS CLI v2 para el lab S3 (o usar `curl` al health endpoint).

### Camino B — Solo navegador (alineado a política)
1. Cuenta gratuita Killercoda o sesión LabEx Docker Playground.
2. Pegar el one-liner del README de scripts.
3. Entregar capturas / enlace según taller.

### Camino C — Demo docente
Docente proyecta Floci; estudiantes hacen diagrama en draw.io + cuestionario. Cero instalación estudiante.

---

## 5. Pros / contras vs herramientas actuales

| Criterio | Floci | Killercoda | LabEx Docker Playground | draw.io |
|---|---|---|---|---|
| Costo / tarjeta | Excelente ($0) | Excelente | Excelente | Excelente |
| Solo navegador | Débil (local) / Medio (si va embebido en lab) | Excelente | Excelente | Excelente |
| Fidelity APIs cloud | Excelente | Medio (depende del scenario) | Bajo–medio | N/A (diseño) |
| Contenedores reales | Alto (usa Docker) | Alto | Alto | N/A |
| CI/CD local reproducible | Alto | Bajo | Bajo | N/A |
| Soporte Windows aula | Medio (Docker Desktop) | Alto | Alto | Alto |
| Madurez / riesgo proyecto | Medio (org joven, 2026; AWS más maduro que az/gcp/oci) | Alto | Alto | Alto |
| Encaje CloudLite | Alto (object storage + colas + funciones) | Medio | Medio | Alto (C4/diagramas) |

**Lectura:** Floci **complementa** Killercoda/LabEx y draw.io; **no los reemplaza** en 2026-2 hasta que el piloto salga bien.

---

## 6. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Docker Desktop no instalado / permisos admin | Alto en aula | Camino B (Killercoda/LabEx) + demo docente |
| Pull lento en WiFi del salón | Alto (come 20–40 min) | Pre-cargar imagen en PCs / USB / mirror; o usar lab remoto |
| Confusión “esto es AWS de verdad” | Medio | Slide explícita: emulador local · $0 · sin cuenta |
| Cobertura incompleta az/gcp/oci | Medio | Piloto solo con **floci (AWS/S3)**; otras variantes demo docente |
| Windows + docker.sock / WSL2 | Medio | Probar script en un PC del aula antes; fallback JVM tag `latest-jvm` |
| Aula virtual / sin Docker en casa | Medio | Entrega alternativa draw.io + Killercoda |
| Proyecto Floci cambia rápido | Bajo–medio | Fijar tag de imagen (`1.x.y`) en el script del curso |
| CLI cloud (aws/az/gcloud) no instalada | Bajo | Lab mínimo con `curl` health + Docker logs; o instalar CLI en el script opcional |

---

## 7. Propuesta pedagógica (encaje en el plan)

| Clase | Tema | Uso Floci sugerido | Prioridad |
|---:|---|---|---|
| 2 | Modelos IaaS / PaaS / SaaS | Demo: “misma CLI, endpoint local” | Baja (demo 10 min) |
| 3 | Virtualización y contenedores | Arrancar Floci con Docker; ver health | Media |
| 4 | Microservicios / distribuidos | Cola (SQS) + función (Lambda) opcional | Media (post-piloto) |
| 6 | Seguridad en la nube | IAM / KMS locales (demo) | Baja |
| **7** | **Redes y almacenamiento cloud** | **Lab S3/Blob/GCS Object Storage local** | **Alta — piloto** |
| 8 | Monitoreo / CI-CD | Job GitHub Actions que levanta Floci y corre test | Media |
| 10 | Costos y sostenibilidad | Contraste factura real vs emulador ($0) | Baja (concepto) |
| 11–12 | Avance / pruebas PI CloudLite | Storage del PI contra endpoint local | Condicionado a piloto OK |

**No usar** Floci en días de parcial (5 / 9 / 14) ni como dependencia de la presentación final (15) en el primer ciclo.

### Diseño del laboratorio piloto (Clase 7 · ~40–50 min)
1. Arranque one-command (`lab-floci.ps1 -Cloud aws` o one-liner LabEx).
2. Crear bucket / subir objeto / listar / descargar.
3. Captura + nota: “endpoint local · sin cuenta · sin tarjeta”.
4. Diagrama draw.io del flujo CloudLite (cliente → API → object storage).

---

## 8. MVP script estudiante

Ubicación:

```text
Plan curso/2026-2/scripts/
  README.md          ← uso previsto (local + Killercoda/LabEx)
  lab-floci.ps1      ← Windows (aula típica)
  lab-floci.sh       ← Linux/macOS / Git Bash
```

### Diseño (pasos 1-2-3)
1. **Prerrequisito:** Docker corriendo (`docker info`).
2. **Comando único:** `.\lab-floci.ps1 -Cloud aws` (o `az` / `gcp` / `oci`).
3. **Resultado:** contenedor healthy + variables de entorno impresas + smoke test.

Si no hay Docker → mensaje claro con enlace al camino B (LabEx Docker Playground).

Esqueleto listo en `scripts/` (no depende de un “repo lab UNIAJC” externo; clona/arranca imagen oficial Floci).

---

## 9. Decisión recomendada y siguientes pasos

### Decisión
1. **Aprobar piloto Floci** como camino B/C complementario (no sustituye draw.io ni Killercoda).
2. Variante por defecto del piloto: **`floci` (AWS, puerto 4566, lab S3)**.
3. `floci-az` / `floci-gcp` / `floci-oci`: solo demo docente o optativo post-piloto.
4. **No** pedir cuentas AWS/GCP/OCI/Azure ni Azure for Students para este piloto.
5. Congelar tag de imagen tras la prueba en un PC del aula.

### Siguientes pasos (checklist)
- [ ] Docente aprueba este plan (veredicto + piloto Clase 7).
- [ ] Probar `lab-floci.ps1 -Cloud aws` en un PC Windows del salón (medir tiempo de pull).
- [ ] Decidir camino oficial del piloto: Local Docker **o** LabEx Docker Playground.
- [ ] Redactar taller CloudLite Clase 7 (estudiante) apuntando al script.
- [ ] Si el piloto OK → mencionar Floci en Presentación del Curso / Recursos (sin regenerar todas las PPTX ahora).
- [ ] Si falla por Docker en aula → archivar como “demo docente” y seguir con Killercoda.

---

## 10. Fuentes

| Recurso | URL |
|---|---|
| Sitio Floci | https://floci.io/ |
| floci (AWS) | https://github.com/floci-io/floci · https://floci.io/floci/ |
| floci-az | https://github.com/floci-io/floci-az |
| floci-gcp | https://github.com/floci-io/floci-gcp |
| floci-oci | https://github.com/floci-io/floci-oci · https://floci.io/floci-oci/ |
| floci-cli | https://github.com/floci-io/floci-cli |
| Org | https://github.com/floci-io |
| Artículo intro | https://hectorvent.dev/posts/introducing-floci/ |
| Docker Hub (AWS) | https://hub.docker.com/r/floci/floci |

---

*Documento interno Plan de curso · no distribuir a estudiantes hasta aprobación del piloto.*
