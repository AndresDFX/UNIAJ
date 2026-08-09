# -*- coding: utf-8 -*-
"""Generador de imagenes de SALIDA ESPERADA para los guiones docente.

Por que existe
--------------
El guion decia "📸 Pantallazo: [CAP: demo ...]" y dejaba una caja vacia que el
docente debia llenar a mano ANTES de dictar. En la practica esas cajas quedaban
vacias. Estas imagenes no reemplazan una captura real del navegador: son una
ILUSTRACION fiel de la salida que el comando/consulta debe producir, para que el
docente sepa que esperar y pueda detectar en 2 segundos si algo salio distinto.

Por eso TODAS llevan el rotulo "SALIDA ESPERADA (ilustracion)" en la cabecera:
es honesto con quien la ve y evita que se confunda con evidencia real de ejecucion.

Uso: `python mockups.py` regenera todo en las carpetas Capturas/ de cada clase.
"""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONTS = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"

NAVY = (9, 82, 146)
CIAN = (38, 156, 203)
AMARILLO = (255, 208, 0)
GRIS = (43, 43, 43)
SOFT = (110, 110, 110)
BLANCO = (255, 255, 255)
ROJO = (176, 32, 48)
VERDE = (27, 122, 78)
TERM_BG = (24, 26, 32)
TERM_FG = (222, 226, 232)
TERM_DIM = (140, 148, 160)
GRID_ALT = (243, 246, 249)
BORDE = (206, 214, 222)

SCALE = 2  # render 2x para que no se vea pixelado dentro del .docx


def _font(name: str, size: int):
    try:
        return ImageFont.truetype(str(FONTS / name), size * SCALE)
    except Exception:
        return ImageFont.load_default()


def _mono(size: int, bold: bool = False):
    return _font("consolab.ttf" if bold else "consola.ttf", size)


def _sans(size: int, bold: bool = False):
    return _font("calibrib.ttf" if bold else "calibri.ttf", size)


def _header(d: ImageDraw.ImageDraw, w: int, titulo: str, h: int = 34):
    """Banda superior con el rotulo honesto de 'ilustracion'."""
    d.rectangle([0, 0, w, h * SCALE], fill=NAVY)
    d.rectangle([0, h * SCALE, w, (h + 3) * SCALE], fill=AMARILLO)
    d.text((14 * SCALE, 9 * SCALE), titulo, font=_sans(12, True), fill=BLANCO)
    rot = "SALIDA ESPERADA (ilustracion)"
    tw = d.textlength(rot, font=_sans(9))
    d.text((w - tw - 14 * SCALE, 11 * SCALE), rot, font=_sans(9), fill=(184, 216, 238))
    return (h + 3) * SCALE


def terminal(path: Path, titulo: str, lineas: list[tuple[str, str]], width: int = 760):
    """Consola. lineas = [(tipo, texto)] con tipo in {cmd, out, dim, ok, err, blank}."""
    w = width * SCALE
    lh = 19 * SCALE
    top = (34 + 3) * SCALE
    pad = 14 * SCALE
    h = top + pad + lh * len(lineas) + pad
    img = Image.new("RGB", (w, h), TERM_BG)
    d = ImageDraw.Draw(img)
    _header(d, w, titulo)
    y = top + pad
    f = _mono(10)
    fb = _mono(10, True)
    for kind, text in lineas:
        if kind == "blank":
            y += lh
            continue
        if kind == "cmd":
            d.text((pad, y), "$ ", font=fb, fill=CIAN)
            d.text((pad + d.textlength("$ ", font=fb), y), text, font=fb, fill=TERM_FG)
        elif kind == "ok":
            d.text((pad, y), text, font=fb, fill=(120, 210, 150))
        elif kind == "err":
            d.text((pad, y), text, font=fb, fill=(240, 130, 130))
        elif kind == "dim":
            d.text((pad, y), text, font=f, fill=TERM_DIM)
        else:
            d.text((pad, y), text, font=f, fill=TERM_FG)
        y += lh
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def sql_result(path: Path, titulo: str, sql: str, headers: list[str],
               rows: list[list[str]], nota: str | None = None,
               error: str | None = None, width: int = 760):
    """Panel tipo playground SQL: sentencia arriba + grilla de resultado abajo."""
    w = width * SCALE
    pad = 14 * SCALE
    sql_lines = sql.strip().split("\n")
    lh_sql = 18 * SCALE
    row_h = 26 * SCALE
    top = (34 + 3) * SCALE
    sql_h = pad + lh_sql * len(sql_lines) + pad
    grid_h = 0 if error else row_h * (1 + len(rows))
    err_h = 46 * SCALE if error else 0
    nota_h = 30 * SCALE if nota else 0
    h = top + sql_h + grid_h + err_h + nota_h + pad
    img = Image.new("RGB", (w, h), BLANCO)
    d = ImageDraw.Draw(img)
    _header(d, w, titulo)

    # bloque SQL
    y = top
    d.rectangle([0, y, w, y + sql_h], fill=(246, 248, 250))
    d.line([(0, y + sql_h), (w, y + sql_h)], fill=BORDE, width=SCALE)
    yy = y + pad
    for ln in sql_lines:
        d.text((pad, yy), ln, font=_mono(10), fill=(17, 17, 17))
        yy += lh_sql
    y += sql_h

    if error:
        d.rectangle([0, y, w, y + err_h], fill=(253, 235, 235))
        d.text((pad, y + 14 * SCALE), error, font=_mono(10, True), fill=ROJO)
        y += err_h
    else:
        n = max(1, len(headers))
        cw = (w - 2 * pad) / n
        # encabezado
        d.rectangle([pad, y, w - pad, y + row_h], fill=NAVY)
        for i, hd in enumerate(headers):
            d.text((pad + i * cw + 8 * SCALE, y + 6 * SCALE), str(hd), font=_sans(10, True), fill=BLANCO)
        y += row_h
        for r_i, row in enumerate(rows):
            bg = GRID_ALT if r_i % 2 else BLANCO
            d.rectangle([pad, y, w - pad, y + row_h], fill=bg)
            d.line([(pad, y + row_h), (w - pad, y + row_h)], fill=BORDE, width=1)
            for i in range(n):
                val = str(row[i]) if i < len(row) else ""
                d.text((pad + i * cw + 8 * SCALE, y + 6 * SCALE), val, font=_mono(9.5), fill=GRIS)
            y += row_h

    if nota:
        d.text((pad, y + 8 * SCALE), nota, font=_sans(9.5), fill=SOFT)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


# ---------------------------------------------------------------- BD II
BD2 = ROOT / "Bases de Datos II" / "Kit docente"


def build_bd2():
    out = []
    out.append(sql_result(
        BD2 / "Clase 1" / "Capturas" / "salida-join-vetcare.png",
        "Clase 1 · VetCare — consulta de verificacion del ER",
        "SELECT m.nombre, d.nombre AS dueno, c.fecha_hora\n"
        "FROM cita c JOIN mascota m ON m.id_mascota = c.id_mascota\n"
        "JOIN dueno d ON d.id_dueno = m.id_dueno;",
        ["nombre", "dueno", "fecha_hora"],
        [["Luna", "Ana Perez", "2026-09-01 09:00:00"]],
        nota="1 fila. Si sale vacia: falta el INSERT o la FK no coincide — revisar id_mascota / id_dueno.",
    ))
    out.append(sql_result(
        BD2 / "Clase 3" / "Capturas" / "salida-proc-ok-y-error.png",
        "Clase 3 · sp_agendar_cita — caso OK y caso rechazado",
        "-- Caso 1: mascota ACTIVA  |  Caso 2: mascota INACTIVA\n"
        "EXEC sp_agendar_cita(101, 10, TIMESTAMP '2026-09-02 10:00', :msg);\n"
        "EXEC sp_agendar_cita(102, 11, TIMESTAMP '2026-09-02 11:00', :msg);",
        ["caso", "id_mascota", "activa", "p_msg devuelto"],
        [["1", "10", "S", "OK: cita agendada"],
         ["2", "11", "N", "ERROR: mascota inactiva; no se agenda"]],
        nota="La validacion vive en el proc: el caso 2 NO inserta fila en cita. Ese es el punto de la clase.",
    ))
    out.append(sql_result(
        BD2 / "Clase 10" / "Capturas" / "salida-doble-reserva.png",
        "Clase 10 · Evidencia del problema (sin restriccion)",
        "SELECT id_veterinario, fecha_hora, COUNT(*) AS citas_en_la_misma_franja\n"
        "FROM cita_demo GROUP BY id_veterinario, fecha_hora HAVING COUNT(*) > 1;",
        ["id_veterinario", "fecha_hora", "citas_en_la_misma_franja"],
        [["5", "2026-10-12 09:00:00", "2"]],
        nota="2 citas para el MISMO veterinario en la MISMA franja: la doble reserva ya ocurrio.",
    ))
    out.append(sql_result(
        BD2 / "Clase 10" / "Capturas" / "salida-unique-rechaza.png",
        "Clase 10 · La misma insercion, ya con la restriccion UNIQUE",
        "ALTER TABLE cita_demo ADD CONSTRAINT uq_cita_demo_vet_fecha\n"
        "  UNIQUE (id_veterinario, fecha_hora);\n"
        "INSERT INTO cita_demo VALUES (3, 35, 5, TIMESTAMP '2026-10-12 09:00:00', 'PROGRAMADA');",
        [], [],
        error="ORA-00001: unique constraint (UQ_CITA_DEMO_VET_FECHA) violated",
        nota="Ahora la BD rechaza la doble reserva sola. Comparar con la imagen anterior: mismo INSERT, distinto resultado.",
    ))
    out.append(sql_result(
        BD2 / "Clase 8" / "Capturas" / "salida-rollback-stock.png",
        "Clase 8 · Transaccion: stock insuficiente dispara ROLLBACK",
        "BEGIN;\n"
        "  INSERT INTO factura ...;  INSERT INTO detalle_factura ...;\n"
        "  UPDATE insumo SET stock = stock - 5 WHERE id_insumo = 50 AND stock >= 5;\n"
        "  -- 0 filas afectadas (solo hay 3) -> ROLLBACK;",
        ["momento", "facturas", "detalles", "stock insumo 50"],
        [["antes de la transaccion", "0", "0", "3"],
         ["durante (antes del commit)", "1", "1", "3"],
         ["despues del ROLLBACK", "0", "0", "3"]],
        nota="Atomicidad: la factura NO queda a medias. Si la fila final no vuelve a 0/0/3, el ROLLBACK no se aplico.",
    ))
    out.append(sql_result(
        BD2 / "Clase 6" / "Capturas" / "salida-explain-antes-despues.png",
        "Clase 6 · Plan de ejecucion antes vs despues",
        "-- ANTES: SELECT * FROM cita c JOIN mascota m ... (sin filtro)\n"
        "-- DESPUES: SELECT c.fecha_hora, m.nombre ... WHERE c.fecha_hora >= DATE '2026-09-01'",
        ["version", "operacion del plan", "filas estimadas"],
        [["ANTES", "TABLE ACCESS FULL (cita)", "120.000"],
         ["ANTES", "HASH JOIN", "120.000"],
         ["DESPUES", "INDEX RANGE SCAN (idx_cita_fecha)", "340"],
         ["DESPUES", "NESTED LOOPS", "340"]],
        nota="Lo que cambia no es 'se ve mas corto': cambia FULL SCAN por INDEX RANGE SCAN y el estimado de filas.",
    ))
    return out


# ------------------------------------------------- Arquitectura (CloudLite)
ARQ = ROOT / "Arquitectura de Sistemas Computacionales" / "Kit docente"


def build_arq():
    out = []
    out.append(terminal(
        ARQ / "Clase 3" / "Capturas" / "salida-docker-build-run.png",
        "Clase 3 · Play with Docker — build y run del stub CloudLite",
        [
            ("cmd", "docker build -t cloudlite-api ."),
            ("dim", "[+] Building 12.4s (8/8) FINISHED"),
            ("dim", " => [1/3] FROM docker.io/library/node:20-alpine        3.1s"),
            ("dim", " => [2/3] COPY . /app                                  0.2s"),
            ("dim", " => [3/3] RUN npm ci --omit=dev                        8.6s"),
            ("ok", " => => naming to docker.io/library/cloudlite-api"),
            ("blank", ""),
            ("cmd", "docker run -d -p 8080:8080 --name api cloudlite-api"),
            ("out", "9f3c1e7a2b48c05d1f6a7e93b2d5c8a10e4f7b62c9d3a1f8"),
            ("blank", ""),
            ("cmd", "curl -s localhost:8080/health"),
            ("ok", '{"status":"ok","service":"cloudlite-api"}'),
        ],
    ))
    out.append(terminal(
        ARQ / "Clase 3" / "Capturas" / "salida-docker-ps.png",
        "Clase 3 · Evidencia para el PI: contenedor corriendo",
        [
            ("cmd", "docker ps"),
            ("dim", "CONTAINER ID   IMAGE           STATUS         PORTS"),
            ("out", "9f3c1e7a2b48   cloudlite-api   Up 2 minutes   0.0.0.0:8080->8080/tcp"),
            ("blank", ""),
            ("dim", "# Esta salida + el Dockerfile son la evidencia del entregable de hoy."),
            ("dim", "# La sesion de PWD caduca a las 4h: capturar ANTES de que expire."),
        ],
    ))
    out.append(terminal(
        ARQ / "Clase 8" / "Capturas" / "salida-actions-run.png",
        "Clase 8 · GitHub Actions — run del workflow de CI",
        [
            ("dim", "Run  build (ubuntu-latest)"),
            ("ok", "  ✓ Set up job                                    2s"),
            ("ok", "  ✓ Checkout repository                           1s"),
            ("ok", "  ✓ Set up Node 20                                4s"),
            ("ok", "  ✓ npm ci                                       11s"),
            ("ok", "  ✓ npm test                                      6s"),
            ("ok", "  ✓ docker build -t cloudlite-api .              14s"),
            ("out", "  ✓ Deploy (simulado): artifact subido            2s"),
            ("blank", ""),
            ("ok", "Job succeeded in 40s"),
            ("dim", "# CI real = build + test. Un workflow con solo 'echo ok' NO cuenta como evidencia."),
        ],
    ))
    out.append(terminal(
        ARQ / "Clase 6" / "Capturas" / "salida-secreto-en-imagen.png",
        "Clase 6 · Por que un secreto NUNCA va en la imagen",
        [
            ("dim", "# El estudiante cree que el .env quedo 'adentro y protegido':"),
            ("cmd", "docker history --no-trunc cloudlite-api | head -3"),
            ("out", "COPY . /app        # <-- aqui entro el .env"),
            ("blank", ""),
            ("cmd", "docker run --rm cloudlite-api cat /app/.env"),
            ("err", "API_KEY=sk_live_9f2a...   <-- CUALQUIERA con la imagen lo lee"),
            ("blank", ""),
            ("dim", "# Correcto: .dockerignore + secreto inyectado en runtime"),
            ("dim", "# (GitHub Actions Secrets / variable de entorno del despliegue)."),
        ],
    ))
    return out


if __name__ == "__main__":
    hechos = build_bd2() + build_arq()
    for p in hechos:
        print("OK", p.relative_to(ROOT))
    print(f"\n{len(hechos)} imagenes generadas.")
