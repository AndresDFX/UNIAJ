# -*- coding: utf-8 -*-
"""Enrich Arquitectura guiones with more detailed minute-by-minute PI-first scripts."""
from pathlib import Path
import subprocess, sys

CURSO = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\Arquitectura de Sistemas Computacionales")
CONV = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos\config\slides\guion_md_a_docx.py")

# Detailed addenda per class (appended/replaced into guion body)
ADD = {
1: """
## Bloque especial Clase 1 (Presentacion del curso + Diagnostico + arranque PI)

### 0-25 Presentacion del curso (PPTX del curso, no el de tema)
Abre `Clases/Presentacion del Curso - Arquitectura de Sistemas Computacionales.pptx`.
Di: «Bienvenidos. Soy Julian Andres Castano. Correo julianacastano@profesores.uniajc.edu.co.
Modalidad: presencialidad asistida. Clase 1 presencial; resto virtual; parciales presencial; festivos autonomos.
Hoy: presentacion + diagnostico de conocimientos previos + arranque CloudLite.»
Padlet rompe-hielo (URL institucional). Sin Clear posts en voz a estudiantes.
Recorre RAA, evaluacion 30/30/40, CONTENIDO 1-15, PI CloudLite 20% Corte 3.

### 25-50 Prueba diagnostica
Instrumento: `Kit docente/Clase 1/Prueba Diagnostica - Arquitectura de Sistemas Computacionales.docx`.
Di: «No es nota del corte; diagnostica saberes previos (redes/SO/web/basicos). Silencio 20-25 min.»
Registro institucional en Entregas docente si aplica.

### 50-70 Teoria intro cloud (slides tema Clase 1)
Cambia a `Clases/Clase 1 - Introduccion a arquitecturas cloud/Presentacion.pptx`.
Mapa mental arquitectura cloud. Presenta CloudLite como hilo del semestre.

### 70-110 Taller PI ficha + C4 Context
Equipos. Entregable: ficha dominio + C4 Context. Recorre mesas. Bloquea dominios vagos.

### 110-120 Cierre
Quiz corto opcional / dudas. «Domingo 23:59 ficha+diagrama. Siguiente: IaaS/PaaS/SaaS (autonoma).»
""",
3: """
## Demo Killercoda / Play with Docker (guion casi literal)
1. Abre killercoda.com o labs.play-with-docker.com.
2. Di: «No instalamos Docker Desktop. Lab temporal en navegador.»
3. `docker run --rm -p 8080:80 nginx:alpine` (o equivalente del lab).
4. Muestra respuesta HTTP / puerto.
5. Crea Dockerfile minimo del stub CloudLite (FROM python:slim o nginx con index del dominio).
6. `docker build -t cloudlite-stub .` y `docker run -p 8080:8080 cloudlite-stub`.
7. 📸 Captura `docker ps` → `Kit docente/Clase 3/Capturas/`.
8. Di: «Si el lab muere, guardan Dockerfile + capturas. Eso es evidencia PI.»
""",
4: """
## Demo draw.io C4 (casi literal)
1. app.diagrams.net → Blank → plantilla C4 o formas rectangulares.
2. Caja sistema CloudLite + actores (Usuario, Admin, Email SaaS).
3. Baja a Containers: Web, API, Auth, DB (max 5).
4. Etiqueta flechas HTTPS/REST.
5. Export PNG. Di: «Mismos nombres usaran en Deployment Clase 7.»
""",
8: """
## Demo GitHub Actions (casi literal)
1. Repo free con `app.py` o stub + test trivial.
2. Crea `.github/workflows/ci.yml` con checkout, setup, test, echo deploy simulado.
3. Push → pestaña Actions → run verde (o explica fallo de cuota).
4. Di: «Secrets en Settings, nunca en YAML. CD real con tarjeta no es requisito.»
5. 📸 Captura workflow → Capturas/.
""",
11: """
## Checklist oral de revision (docente)
Por equipo (3-5 min): dominio claro? ADR? C4=Deployment nombres? Dockerfile? Actions? Seguridad? Costos?
Marca ROJO/AMARILLO/VERDE. Backlog escrito 5 items para Clase 12.
""",
12: """
## Ensayo pitch (cronometro)
Orden sugerido: 1 problema, 2 arquitectura, 1 contenedor, 1 CI, 1 seguridad/costos, Q&A.
Di: «Esto NO es el Parcial 3. El Parcial 3 es solo evaluacion en Clase 14. Hoy preparan sustentacion PI.»
""",
}

KIT = CURSO / "Kit docente"
for n, block in ADD.items():
    matches = list((KIT / f"Clase {n}").glob("Guion Docente Clase *.md"))
    if not matches:
        print("missing", n); continue
    md = matches[0]
    text = md.read_text(encoding="utf-8")
    marker = "\n## Anexo de detalle docente\n"
    if marker in text:
        text = text.split(marker)[0]
    text = text.rstrip() + marker + block + "\n"
    md.write_text(text, encoding="utf-8")
    subprocess.run([sys.executable, str(CONV), str(md)], check=False)
    print("enriched", md.name)

# Patch Clase 1 pptx agenda via small rebuild note in taller - add diag mention to taller
taller = CURSO / "Clases" / "Clase 1 - Introduccion a arquitecturas cloud" / "Taller Clase 1 - CloudLite.docx"
print("taller exists", taller.exists())