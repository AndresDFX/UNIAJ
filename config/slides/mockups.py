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
    # PL/pgSQL, no PL/SQL: el taller y los 100 puntos se califican en PostgreSQL
    # dentro de ExamLab. La version anterior de esta imagen ilustraba `EXEC` con un
    # parametro OUT `:msg` e ids 101/102 — sintaxis y datos que no existen en la
    # actividad, o sea la ilustracion contradecia lo que se evalua.
    out.append(sql_result(
        BD2 / "Clase 3" / "Capturas" / "salida-proc-ok-y-error.png",
        "Clase 3 · sp_agendar_cita — la bateria de pruebas (P1 OK, P2 rechazado)",
        "-- Un bloque DO por caso: la excepcion se atrapa y el script sigue.\n"
        "DO $$ BEGIN CALL sp_agendar_cita(1, 2, TIMESTAMP '2026-09-20 08:00:00'); ... END $$;\n"
        "DO $$ BEGIN CALL sp_agendar_cita(3, 2, TIMESTAMP '2026-09-21 08:00:00'); ... END $$;\n"
        "SELECT caso, esperado, obtenido, paso FROM resultado_prueba ORDER BY id_prueba;",
        ["caso", "esperado", "obtenido", "paso"],
        [["P1 mascota activa", "OK: cita creada", "OK: cita creada", "t"],
         ["P2 mascota inactiva", "EXCEPCION: mascota inactiva",
          "ERROR: la mascota 3 esta inactiva; ...", "t"]],
        nota="`paso` = «coincidio con lo esperado», asi que las dos filas quedan en t. "
             "La mascota 3 (Rocky) esta INACTIVA y NO inserto fila: cita sigue en 11.",
        width=880,
    ))
    out.append(sql_result(
        BD2 / "Clase 4" / "Capturas" / "cap01_demo.png",
        "Clase 4 · trg_audit_cita — 3 UPDATE dejan 2 filas de auditoria",
        "UPDATE cita SET estado = 'CANCELADA'  WHERE id_cita = 1;\n"
        "UPDATE cita SET estado = 'ATENDIDA'   WHERE id_cita = 3;\n"
        "UPDATE cita SET estado = 'PROGRAMADA' WHERE id_cita = 6;  -- ya estaba PROGRAMADA\n"
        "SELECT id_audit, id_cita, accion, valor_anterior, valor_nuevo FROM audit_cita;",
        ["id_audit", "id_cita", "accion", "valor_anterior", "valor_nuevo"],
        [["1", "1", "CAMBIO_ESTADO", "PROGRAMADA", "CANCELADA"],
         ["2", "3", "CAMBIO_ESTADO", "PROGRAMADA", "ATENDIDA"]],
        nota="2 filas, no 3: el tercer UPDATE no cambio el estado y "
             "WHEN (OLD.estado IS DISTINCT FROM NEW.estado) lo filtro. Si salen 3, falta el WHEN.",
        width=880,
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
    # Esta imagen mostraba un BEGIN/ROLLBACK escrito a mano sobre `id_insumo = 50`, insumo
    # que no existe en el taller (los insumos son 1..6) y con una forma que no es la que se
    # califica: la actividad pide `CALL sp_facturar(...)` y la reversion la hace el motor sin
    # que nadie escriba ROLLBACK --que es justamente la pregunta 4--. El docente comparaba la
    # captura del estudiante contra una salida que su script no puede producir.
    out.append(sql_result(
        BD2 / "Clase 8" / "Capturas" / "salida-rollback-stock.png",
        "Clase 8 · El CALL falla a mitad y la base queda intacta (PostgreSQL · ExamLab)",
        "-- Insumo 3: stock 40 (alcanza)  |  Insumo 2: stock 3 (NO alcanza para 10)\n"
        "DO $$ BEGIN\n"
        "  CALL sp_facturar(4, ARRAY[3,2], ARRAY[2,10]);\n"
        "EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Fallo esperado: %', SQLERRM;\n"
        "END $$;\n"
        "-- NOTICE:  Fallo esperado: ERROR: stock insuficiente del insumo 2 (se pidieron 10)",
        ["momento", "facturas", "lineas de detalle", "stock insumo 3", "stock insumo 2"],
        [["foto INICIAL (antes del CALL)", "1", "3", "40", "3"],
         ["foto FINAL (tras el fallo)", "1", "3", "40", "3"]],
        nota="Atomicidad: el descuento de 2 unidades del insumo 3 SI se aplico y se deshizo solo. "
             "Nadie escribio ROLLBACK. Si el insumo 3 queda en 38, la transaccion no se revirtio.",
        width=880,
    ))
    out.append(sql_result(
        BD2 / "Clase 7" / "Capturas" / "salida-indice-antes-despues.png",
        "Clase 7 · El plan de C1 antes y despues del indice (PostgreSQL · ExamLab)",
        "-- C1 (agenda del dia), la MISMA consulta las dos veces:\n"
        "--   WHERE fecha_hora >= TIMESTAMP '2026-03-10 00:00:00'\n"
        "--     AND fecha_hora <  TIMESTAMP '2026-03-11 00:00:00'\n"
        "--     AND estado = 'PROGRAMADA'\n"
        "-- Entre las dos medidas: CREATE INDEX x3  +  ANALYZE cita;  <-- el paso que se salta medio salon",
        ["momento", "nodo del plan (PostgreSQL)", "filas leidas -> devueltas"],
        [["C1 ANTES (solo las PK)", "Seq Scan on cita", "30.010 -> 91"],
         ["C1 DESPUES", "Index Scan using idx_cita_programada_fecha", "91 -> 91"],
         ["C2 ANTES", "Seq Scan on mascota", "5.008 -> 2"],
         ["C2 DESPUES", "Index Scan using idx_mascota_dueno", "2 -> 2"]],
        nota="Gana el indice PARCIAL, no el completo: recorre 91 entradas que ya cumplen el estado, "
             "y el completo recorreria las 150 del dia. Reporte el que VEA en su plan.",
        width=920,
    ))
    # Esta imagen mostraba «TABLE ACCESS FULL -> INDEX RANGE SCAN (idx_cita_fecha)»
    # con 120.000 filas y fecha 2026-09-01. Tres cosas falsas a la vez: son nombres de
    # nodo de ORACLE y el taller corre en ExamLab (PostgreSQL/PGlite); el indice
    # `idx_cita_fecha` no se crea en esta clase sino en la Clase 7, asi que ninguna de
    # las dos versiones puede dar un Index Scan hoy; y el volumen sembrado son 30.010
    # citas con la fecha 2026-03-10 del taller. El docente comparaba la captura del
    # estudiante contra una salida imposible.
    out.append(sql_result(
        BD2 / "Clase 6" / "Capturas" / "salida-explain-antes-despues.png",
        "Clase 6 · EXPLAIN ANALYZE antes vs despues (PostgreSQL · ExamLab)",
        "-- P1 ANTES : SELECT * ... FROM cita c, mascota m, veterinario v, dueno d\n"
        "--            WHERE to_char(c.fecha_hora,'YYYY-MM-DD') = '2026-03-10'\n"
        "-- P1 DESPUES: 6 columnas + c.fecha_hora >= TIMESTAMP '2026-03-10'\n"
        "--            AND c.fecha_hora < TIMESTAMP '2026-03-11'   (sargable)\n"
        "-- P3 ANTES : subconsulta correlacionada por dueno | DESPUES: LEFT JOIN + GROUP BY",
        ["version", "nodo del plan (PostgreSQL)", "filas / pasadas"],
        [["P1 ANTES", "Seq Scan on cita + Hash Join x3", "30.010 -> 91"],
         ["P1 DESPUES", "Seq Scan on cita + Hash Join x3", "30.010 -> 91"],
         ["P3 ANTES", "SubPlan correlacionado, loops=2006", "2.006 pasadas"],
         ["P3 DESPUES", "Hash Right Join + HashAggregate", "1 pasada"],
         ["equivalencia", "COUNT(*) antes = COUNT(*) despues", "91 = 91"]],
        nota="El nodo de P1 no cambia hoy: sin indice sigue siendo Seq Scan, y eso es la Clase 7. "
             "Hoy se miden pasadas y filas, no milisegundos.",
        width=880,
    ))
    return out


# ------------------------------------------------- Arquitectura (CloudLite)
ARQ = ROOT / "Arquitectura de Sistemas Computacionales" / "Kit docente"


def c4_context(path: Path, titulo: str, sistema: str, personas: list,
               externos: list, nota: str, width: int = 900):
    """Diagrama C4 Context: el sistema como UNA caja, actores a la izquierda y
    sistemas externos a la derecha, con las flechas rotuladas.

    Por que existe: el bloque «Demo en vivo» del guion le pide al docente dibujar
    este diagrama delante del grupo, pero no le daba ninguna referencia de como
    debe quedar. Sin ella la demo sale distinta cada semestre y el estudiante no
    tiene contra que comparar su entrega. `personas` y `externos` son listas de
    (rotulo, etiqueta_de_flecha).
    """
    w = width * SCALE
    top = (34 + 3) * SCALE
    fila = 108 * SCALE
    filas = max(len(personas), len(externos))
    alto_area = max(2, filas) * fila
    h = top + alto_area + 74 * SCALE
    img = Image.new("RGB", (w, h), BLANCO)
    d = ImageDraw.Draw(img)
    _header(d, w, titulo)

    caja_w, caja_h = 210 * SCALE, 96 * SCALE
    lat_w, lat_h = 172 * SCALE, 66 * SCALE
    cx0 = (w - caja_w) // 2
    cy0 = top + (alto_area - caja_h) // 2
    izq_x = 26 * SCALE
    der_x = w - lat_w - 26 * SCALE

    def _caja(x0, y0, x1, y1, fill, borde, texto, color_txt, size=11, bold=True):
        d.rounded_rectangle([x0, y0, x1, y1], radius=9 * SCALE, fill=fill,
                            outline=borde, width=2 * SCALE)
        f = _sans(size, bold)
        lineas = texto.split("\n")
        alto = len(lineas) * (size + 4) * SCALE
        yy = y0 + ((y1 - y0) - alto) / 2
        for ln in lineas:
            tw = d.textlength(ln, font=f)
            d.text((x0 + ((x1 - x0) - tw) / 2, yy), ln, font=f, fill=color_txt)
            yy += (size + 4) * SCALE

    def _flecha(x1, y1, x2, y2, etiqueta):
        d.line([(x1, y1), (x2, y2)], fill=CIAN, width=3 * SCALE)
        ang = 1 if x2 > x1 else -1
        d.polygon([(x2, y2), (x2 - 11 * SCALE * ang, y2 - 6 * SCALE),
                   (x2 - 11 * SCALE * ang, y2 + 6 * SCALE)], fill=CIAN)
        f = _sans(8.5)
        tw = d.textlength(etiqueta, font=f)
        mx, my = (x1 + x2) / 2 - tw / 2, (y1 + y2) / 2 - 15 * SCALE
        d.rectangle([mx - 4 * SCALE, my - 1 * SCALE, mx + tw + 4 * SCALE,
                     my + 13 * SCALE], fill=BLANCO)
        d.text((mx, my), etiqueta, font=f, fill=NAVY)

    _caja(cx0, cy0, cx0 + caja_w, cy0 + caja_h, NAVY, NAVY,
          sistema + "\n[Sistema]", BLANCO, size=13)

    y = top + (alto_area - len(personas) * fila) // 2 + (fila - lat_h) // 2
    for rotulo, etiqueta in personas:
        _caja(izq_x, y, izq_x + lat_w, y + lat_h, AMARILLO, AMARILLO,
              rotulo + "\n[Persona]", GRIS, size=10)
        _flecha(izq_x + lat_w, y + lat_h / 2, cx0, y + lat_h / 2, etiqueta)
        y += fila

    y = top + (alto_area - len(externos) * fila) // 2 + (fila - lat_h) // 2
    for rotulo, etiqueta in externos:
        _caja(der_x, y, der_x + lat_w, y + lat_h, (150, 150, 150), (110, 110, 110),
              rotulo + "\n[Sistema externo]", BLANCO, size=10)
        _flecha(cx0 + caja_w, y + lat_h / 2, der_x, y + lat_h / 2, etiqueta)
        y += fila

    d.line([(0, h - 52 * SCALE), (w, h - 52 * SCALE)], fill=BORDE, width=SCALE)
    d.text((14 * SCALE, h - 42 * SCALE), nota, font=_sans(9.5), fill=SOFT)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def c4_container(path: Path, titulo: str, sistema: str, personas: list,
                 contenedores: list, rels: list, externos: list, nota: str,
                 width: int = 980):
    """Diagrama C4 Container: la caja del Context ABIERTA, con los contenedores
    dentro de un System_Boundary, los actores a la izquierda y los externos a la
    derecha.

    Por que existe: el bloque «Demo en vivo» de la Clase 4 le pide al docente abrir
    el Context de la Clase 1 y dejarlo en Containers, pero la carpeta Capturas/ de
    esa clase estaba vacia — el guion imprimia la receta en vez de la imagen. Esta
    ilustracion es el mismo modelo que `DEMO_MERMAID[4]`, para que lo proyectado, lo
    entregado en ExamLab y lo que el docente compara sean el mismo diagrama.

    personas / externos = [(rotulo, etiqueta_de_flecha, indice_de_contenedor)]
    contenedores        = [(rotulo, tecnologia, "container" | "db")]
    rels                = [(desde_idx, hasta_idx, etiqueta)]  # flechas internas
    """
    CONT = (26, 104, 162)
    CONTDB = (14, 74, 116)
    BOUND_BG = (247, 250, 252)

    caja_w, caja_h, gap = 250, 66, 40
    lat_w, lat_h = 176, 62
    label_h = 28
    pad_b = 16

    n_cont = max(1, len(contenedores))
    bound_h = label_h + pad_b + n_cont * caja_h + (n_cont - 1) * gap + pad_b
    top_u = 37
    alto_lat = max(len(personas), len(externos)) * (lat_h + 46)
    area = max(bound_h, alto_lat)
    h_u = top_u + 20 + area + 20 + 52

    w = width * SCALE
    h = h_u * SCALE
    img = Image.new("RGB", (w, h), BLANCO)
    d = ImageDraw.Draw(img)
    _header(d, w, titulo)

    bx0 = (width - caja_w) // 2 - 22
    bx1 = bx0 + caja_w + 44
    by0 = top_u + 20 + (area - bound_h) // 2

    def _caja(x0, y0, x1, y1, fill, borde, lineas, color_txt, size=11):
        d.rounded_rectangle([x0 * SCALE, y0 * SCALE, x1 * SCALE, y1 * SCALE],
                            radius=9 * SCALE, fill=fill, outline=borde, width=2 * SCALE)
        alto = sum((size + 4) if i == 0 else (size + 1) for i, _ in enumerate(lineas))
        yy = (y0 + ((y1 - y0) - alto) / 2) * SCALE
        for i, ln in enumerate(lineas):
            f = _sans(size, True) if i == 0 else _sans(size - 2)
            tw = d.textlength(ln, font=f)
            d.text((x0 * SCALE + ((x1 - x0) * SCALE - tw) / 2, yy), ln, font=f, fill=color_txt)
            yy += ((size + 4) if i == 0 else (size + 1)) * SCALE

    def _etiqueta(mx, my, texto):
        # Sin texto no hay recuadro: una flecha con rotulo vacio (el tramo final de un
        # codo) dejaba un parche blanco que borraba el borde punteado del boundary.
        if not texto:
            return
        f = _sans(8.5)
        tw = d.textlength(texto, font=f)
        d.rectangle([mx * SCALE - 4 * SCALE, my * SCALE - 1 * SCALE,
                     mx * SCALE + tw + 4 * SCALE, my * SCALE + 13 * SCALE], fill=BLANCO)
        d.text((mx * SCALE, my * SCALE), texto, font=f, fill=NAVY)

    def _flecha_h(x1, x2, y, texto):
        d.line([(x1 * SCALE, y * SCALE), (x2 * SCALE, y * SCALE)], fill=CIAN, width=3 * SCALE)
        s = 1 if x2 > x1 else -1
        d.polygon([(x2 * SCALE, y * SCALE),
                   ((x2 - 11 * s) * SCALE, (y - 6) * SCALE),
                   ((x2 - 11 * s) * SCALE, (y + 6) * SCALE)], fill=CIAN)
        f = _sans(8.5)
        tw = d.textlength(texto, font=f)
        _etiqueta((x1 + x2) / 2 - tw / (2 * SCALE), y - 15, texto)

    def _flecha_v(x, y1, y2, texto):
        d.line([(x * SCALE, y1 * SCALE), (x * SCALE, y2 * SCALE)], fill=CIAN, width=3 * SCALE)
        d.polygon([(x * SCALE, y2 * SCALE),
                   ((x - 6) * SCALE, (y2 - 11) * SCALE),
                   ((x + 6) * SCALE, (y2 - 11) * SCALE)], fill=CIAN)
        _etiqueta(x + 10, (y1 + y2) / 2 - 6, texto)

    # System_Boundary: borde punteado, como lo dibuja C4
    d.rectangle([bx0 * SCALE, by0 * SCALE, bx1 * SCALE, (by0 + bound_h) * SCALE],
                fill=BOUND_BG)
    paso = 12
    for xx in range(bx0, bx1, paso * 2):
        for yy in (by0, by0 + bound_h):
            d.line([(xx * SCALE, yy * SCALE), (min(xx + paso, bx1) * SCALE, yy * SCALE)],
                   fill=(120, 140, 160), width=2 * SCALE)
    for yy in range(by0, by0 + bound_h, paso * 2):
        for xx in (bx0, bx1):
            d.line([(xx * SCALE, yy * SCALE), (xx * SCALE, min(yy + paso, by0 + bound_h) * SCALE)],
                   fill=(120, 140, 160), width=2 * SCALE)
    d.text(((bx0 + 12) * SCALE, (by0 + 8) * SCALE), f"{sistema}  ·  System_Boundary",
           font=_sans(10, True), fill=(90, 108, 126))

    # contenedores apilados
    cy, centros = by0 + label_h + pad_b, []
    for rotulo, tec, tipo in contenedores:
        es_db = tipo == "db"
        _caja(bx0 + 22, cy, bx0 + 22 + caja_w, cy + caja_h,
              CONTDB if es_db else CONT, CONTDB if es_db else CONT,
              [rotulo, f"[{'ContainerDb' if es_db else 'Container'} · {tec}]"], BLANCO)
        centros.append((cy + caja_h / 2, cy, cy + caja_h))
        cy += caja_h + gap

    for desde, hasta, texto in rels:
        _flecha_v(bx0 + 22 + caja_w / 2, centros[desde][2], centros[hasta][1], texto)

    izq_x, der_x = 26, width - lat_w - 26
    # La pila de actores se centra en el promedio de los contenedores a los que apunta,
    # no en el area del lienzo: asi los codos salen simetricos en vez de quedar uno recto
    # y otro con un salto minimo que parece un defecto de dibujo.
    stack_h = len(personas) * (lat_h + 46) - 46
    y = sum(centros[idx][0] for _, _, idx in personas) / len(personas) - stack_h / 2
    for i, (rotulo, etiqueta, idx) in enumerate(personas):
        _caja(izq_x, y, izq_x + lat_w, y + lat_h, AMARILLO, AMARILLO,
              [rotulo, "[Person]"], GRIS, size=10)
        y_act, y_dest = y + lat_h / 2, centros[idx][0]
        if abs(y_act - y_dest) < 4:
            _flecha_h(izq_x + lat_w, bx0 + 22, y_dest, etiqueta)
        else:
            # Codo ortogonal: la flecha tiene que llegar al contenedor que dice el
            # modelo, no al que le quede enfrente. El tramo largo va a la altura del
            # actor para que cada rotulo tenga su propia linea y no se pisen; el canal
            # vertical se separa por actor para que dos flechas no se solapen.
            gx = bx0 - 26 - i * 18
            d.line([((izq_x + lat_w) * SCALE, y_act * SCALE), (gx * SCALE, y_act * SCALE)],
                   fill=CIAN, width=3 * SCALE)
            d.line([(gx * SCALE, y_act * SCALE), (gx * SCALE, y_dest * SCALE)],
                   fill=CIAN, width=3 * SCALE)
            _flecha_h(gx, bx0 + 22, y_dest, "")
            f = _sans(8.5)
            tw = d.textlength(etiqueta, font=f) / SCALE
            _etiqueta((izq_x + lat_w + gx) / 2 - tw / 2, y_act - 16, etiqueta)
        y += lat_h + 46

    y = top_u + 20 + (area - len(externos) * (lat_h + 46)) // 2
    for rotulo, etiqueta, idx in externos:
        _caja(der_x, y, der_x + lat_w, y + lat_h, (150, 150, 150), (110, 110, 110),
              [rotulo, "[System_Ext]"], BLANCO, size=10)
        _flecha_h(bx0 + 22 + caja_w, der_x, centros[idx][0], etiqueta)
        y += lat_h + 46

    d.line([(0, h - 52 * SCALE), (w, h - 52 * SCALE)], fill=BORDE, width=SCALE)
    d.text((14 * SCALE, h - 42 * SCALE), nota, font=_sans(9.5), fill=SOFT)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def deployment_zones(path: Path, titulo: str, cliente, zonas: list, externos: list,
                     rels: list, nota: str):
    """Diagrama de despliegue: tres zonas de confianza en fila, con los componentes
    dentro, el cliente fuera a la izquierda y los sistemas externos fuera abajo.

    Por que existe: la Clase 7 pide dibujar este diagrama en la demo y su carpeta
    `Capturas/` estaba vacia — el guion imprimia la receta en vez de la imagen,
    igual que le pasaba a la Clase 4 antes de `demo-clase04.png`. Es el mismo
    modelo que `DEMO_MERMAID[7]`, para que lo proyectado, lo que el estudiante pega
    en ExamLab y lo que el docente califica sean el mismo diagrama.

    cliente  = (id, nombre, detalle) | None      -> fuera de las zonas, a la izquierda
    zonas    = [(rotulo, ancho, color, [(id, nombre, detalle, "svc"|"db"), ...]), ...]
    externos = [(id, nombre, detalle)]           -> fuera de las zonas, abajo
    rels     = [(id_desde, id_hasta, etiqueta, es_frontera)]
    """
    CONT, CONTDB = (26, 104, 162), (14, 74, 116)
    ZONA_FILL = {"publica": (255, 250, 232), "privada": (240, 246, 251),
                 "datos": (235, 247, 252)}

    label_h, pad, box_h, gap_v = 26, 14, 62, 18
    cli_w, cli_h, gap_cli, gap_z = 140, 58, 142, 80
    ext_w, ext_h = 208, 58

    x = 18 + (cli_w + gap_cli if cliente else 0)
    zonas_x = []
    for _, ancho, _, _ in zonas:
        zonas_x.append(x)
        x += ancho + gap_z
    width = x - gap_z + 20

    altos = [label_h + pad + len(cajas) * box_h + (len(cajas) - 1) * gap_v + pad
             for _, _, _, cajas in zonas]
    zonas_top = 67
    area = max(altos)
    y_ext = zonas_top + area + 44
    h_u = y_ext + (ext_h if externos else 0) + 24 + 52

    w, h = width * SCALE, h_u * SCALE
    img = Image.new("RGB", (w, h), BLANCO)
    d = ImageDraw.Draw(img)
    _header(d, w, titulo)

    def _caja(x0, y0, x1, y1, fill, borde, nombre, detalle, color_txt, size=11):
        d.rounded_rectangle([x0 * SCALE, y0 * SCALE, x1 * SCALE, y1 * SCALE],
                            radius=9 * SCALE, fill=fill, outline=borde, width=2 * SCALE)
        lineas = [(nombre, _sans(size, True), size + 4)]
        if detalle:
            lineas.append((detalle, _sans(size - 2), size + 1))
        alto = sum(paso for _, _, paso in lineas)
        yy = (y0 + ((y1 - y0) - alto) / 2) * SCALE
        for texto, f, paso in lineas:
            tw = d.textlength(texto, font=f)
            d.text((x0 * SCALE + ((x1 - x0) * SCALE - tw) / 2, yy), texto, font=f, fill=color_txt)
            yy += paso * SCALE

    def _punteado(x0, y0, x1, y1, color, paso=11):
        for xx in range(int(x0), int(x1), paso * 2):
            for yy in (y0, y1):
                d.line([(xx * SCALE, yy * SCALE), (min(xx + paso, x1) * SCALE, yy * SCALE)],
                       fill=color, width=2 * SCALE)
        for yy in range(int(y0), int(y1), paso * 2):
            for xx in (x0, x1):
                d.line([(xx * SCALE, yy * SCALE), (xx * SCALE, min(yy + paso, y1) * SCALE)],
                       fill=color, width=2 * SCALE)

    def _etiqueta(mx, my, texto, color=NAVY):
        f = _sans(8.5)
        tw = d.textlength(texto, font=f)
        d.rectangle([mx * SCALE - 4 * SCALE, my * SCALE - 1 * SCALE,
                     mx * SCALE + tw + 4 * SCALE, my * SCALE + 13 * SCALE], fill=BLANCO)
        d.text((mx * SCALE, my * SCALE), texto, font=f, fill=color)

    rects = {}

    # zonas y componentes
    for (rotulo, ancho, clave, cajas), zx, alto in zip(zonas, zonas_x, altos):
        zy = zonas_top + (area - alto) // 2
        d.rectangle([zx * SCALE, zy * SCALE, (zx + ancho) * SCALE, (zy + alto) * SCALE],
                    fill=ZONA_FILL.get(clave, GRID_ALT))
        _punteado(zx, zy, zx + ancho, zy + alto, (120, 140, 160))
        d.text(((zx + 12) * SCALE, (zy + 7) * SCALE), rotulo, font=_sans(10, True),
               fill=(90, 108, 126))
        cy = zy + label_h + pad
        for cid, nombre, detalle, tipo in cajas:
            es_db = tipo == "db"
            _caja(zx + pad, cy, zx + ancho - pad, cy + box_h,
                  CONTDB if es_db else CONT, CONTDB if es_db else CONT,
                  nombre, detalle, BLANCO)
            rects[cid] = (zx + pad, cy, zx + ancho - pad, cy + box_h)
            cy += box_h + gap_v

    # cliente: fuera de las tres zonas, porque es el actor y no algo que se despliega
    if cliente:
        cid, nombre, detalle = cliente
        cy = zonas_top + (area - cli_h) // 2
        _caja(18, cy, 18 + cli_w, cy + cli_h, AMARILLO, AMARILLO, nombre, detalle,
              GRIS, size=10)
        rects[cid] = (18, cy, 18 + cli_w, cy + cli_h)

    # externos: fuera de las zonas, abajo
    ex = zonas_x[min(1, len(zonas_x) - 1)]
    for cid, nombre, detalle in externos:
        _caja(ex, y_ext, ex + ext_w, y_ext + ext_h, (150, 150, 150), (110, 110, 110),
              nombre, detalle, BLANCO, size=10)
        rects[cid] = (ex, y_ext, ex + ext_w, y_ext + ext_h)
        ex += ext_w + 40

    for desde, hasta, etiqueta, frontera in rels:
        ax0, ay0, ax1, ay1 = rects[desde]
        bx0, by0, bx1, by1 = rects[hasta]
        if (bx0 + bx1) / 2 > (ax0 + ax1) / 2 + 20:
            p1 = (ax1, (ay0 + ay1) / 2)
            p2 = (bx0, (by0 + by1) / 2)
        else:
            p1 = ((ax0 + ax1) / 2, ay1)
            p2 = ((bx0 + bx1) / 2, by0)
        color = ROJO if frontera else CIAN
        d.line([(p1[0] * SCALE, p1[1] * SCALE), (p2[0] * SCALE, p2[1] * SCALE)],
               fill=color, width=3 * SCALE)
        if abs(p2[0] - p1[0]) > abs(p2[1] - p1[1]):
            s = 1 if p2[0] > p1[0] else -1
            d.polygon([(p2[0] * SCALE, p2[1] * SCALE),
                       ((p2[0] - 11 * s) * SCALE, (p2[1] - 6) * SCALE),
                       ((p2[0] - 11 * s) * SCALE, (p2[1] + 6) * SCALE)], fill=color)
        else:
            d.polygon([(p2[0] * SCALE, p2[1] * SCALE),
                       ((p2[0] - 6) * SCALE, (p2[1] - 11) * SCALE),
                       ((p2[0] + 6) * SCALE, (p2[1] - 11) * SCALE)], fill=color)
        f = _sans(8.5)
        tw = d.textlength(etiqueta, font=f) / SCALE
        _etiqueta((p1[0] + p2[0]) / 2 - tw / 2, (p1[1] + p2[1]) / 2 - 16, etiqueta,
                  ROJO if frontera else NAVY)

    d.line([(0, h - 52 * SCALE), (w, h - 52 * SCALE)], fill=BORDE, width=SCALE)
    d.text((14 * SCALE, h - 42 * SCALE), nota, font=_sans(9.5), fill=SOFT)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def build_arq():
    out = []
    out.append(c4_context(
        ARQ / "Clase 1" / "Capturas" / "demo-clase01.png",
        "Clase 1 · C4 Context de la demo en vivo (draw.io)",
        "CloudLite App",
        [("Usuario final", "consulta"), ("Administrador", "administra")],
        [("Pasarela de pagos", "cobra")],
        "Nivel Context: el sistema es UNA caja. Nada de base de datos, API ni cache: "
        "eso es Clase 4 (Containers).",
    ))
    # Mismos actores, mismo externo y mismos nombres que demo-clase01.png: la demo de
    # la Clase 4 es ese Context con la caja abierta, y los 2 pts de trazabilidad de la
    # pregunta 13 se cobran exactamente por eso.
    out.append(c4_container(
        ARQ / "Clase 4" / "Capturas" / "demo-clase04.png",
        "Clase 4 · C4 Container de la demo (el Context de la Clase 1, ya abierto)",
        "CloudLite App",
        [("Usuario final", "consulta · HTTPS", 0), ("Administrador", "administra · HTTPS", 0)],
        [("App web", "React", "container"),
         ("API CloudLite", "Node.js", "container"),
         ("Base de datos", "PostgreSQL", "db")],
        [(0, 1, "pide y envia datos · HTTPS/JSON"), (1, 2, "lee y escribe · TCP/SQL")],
        [("Pasarela de pagos", "cobra · API REST sobre HTTPS", 1)],
        "Lo que guarda datos va como ContainerDb. Cada flecha lleva protocolo Y formato. "
        "Los externos, FUERA del System_Boundary.",
    ))
    # Mismos nombres que demo-clase04.png —`App web`, `API CloudLite`, `Base de datos`,
    # `Pasarela de pagos`— porque la pregunta 6 cobra 5.5 pts por que el Despliegue y el
    # C4 Containers usen las mismas palabras. Los puertos son los del `EXPOSE 8080` de la
    # Clase 3, y la base de datos esta en la zona de datos: ponerla en la publica cuesta
    # 4 pts completos, asi que la ilustracion no puede insinuar lo contrario.
    out.append(deployment_zones(
        ARQ / "Clase 7" / "Capturas" / "demo-clase07.png",
        "Clase 7 · Despliegue en tres zonas de la demo (el C4 Container de la Clase 4, ya ubicado)",
        ("cliente", "Cliente / navegador", "Usuario final o Administrador"),
        [
            ("Zona publica · internet", 210, "publica",
             [("edge", "Edge / balanceador", "443 HTTPS", "svc"),
              ("web", "App web", "React estatico · 443", "svc")]),
            ("Zona privada · solo desde el edge", 190, "privada",
             [("api", "API CloudLite", "Node.js · 8080 HTTP", "svc")]),
            ("Zona de datos · sin salida a internet", 230, "datos",
             [("db", "Base de datos", "PostgreSQL · 5432 TCP", "db")]),
        ],
        [("pagos", "Pasarela de pagos", "externo · no lo despliego yo")],
        [
            ("cliente", "edge", "HTTPS 443 · frontera", True),
            ("cliente", "web", "descarga el bundle", False),
            ("edge", "api", "HTTP 8080", False),
            ("api", "db", "TCP 5432", False),
            ("api", "pagos", "HTTPS 443 · frontera", True),
        ],
        "Tres zonas rotuladas (4 pts) · la base de datos en la de datos, nunca en la publica "
        "(4 pts) · un puerto por caja (2 pts) · en rojo las fronteras de confianza (2 pts).",
    ))
    # La ilustracion anterior mostraba exactamente los tres errores que la rubrica
    # descuenta: `build` sin etiqueta (pierde 1.5 pts de la pregunta 10), `-p 8080:8080`
    # con los dos lados iguales (imposible distinguir anfitrion de contenedor, que es lo
    # que esa misma pregunta pide explicado) y un `COPY . /app` antes del `npm ci`, que
    # invierte el orden de cache que la pregunta 8 califica. El docente proyectaba la
    # salida del error mientras enseniaba a no cometerlo.
    out.append(terminal(
        ARQ / "Clase 3" / "Capturas" / "salida-docker-build-run.png",
        "Clase 3 · Killercoda — build, run y verificacion del stub CloudLite",
        [
            ("cmd", "docker build -t cloudlite-api:0.1.0 ."),
            ("dim", "[+] Building 12.4s (10/10) FINISHED"),
            ("dim", " => [1/5] FROM docker.io/library/node:20-alpine        3.1s"),
            ("dim", " => [2/5] WORKDIR /app                                 0.1s"),
            ("dim", " => [3/5] COPY package*.json ./     <- dependencias    0.2s"),
            ("dim", " => [4/5] RUN npm ci --omit=dev       PRIMERO          8.6s"),
            ("dim", " => [5/5] COPY . .                  <- codigo despues  0.2s"),
            ("ok", " => => naming to docker.io/library/cloudlite-api:0.1.0"),
            ("blank", ""),
            ("cmd", "docker run -d -p 8081:8080 --name api cloudlite-api:0.1.0"),
            ("out", "9f3c1e7a2b48c05d1f6a7e93b2d5c8a10e4f7b62c9d3a1f8"),
            ("blank", ""),
            ("cmd", "curl -i http://localhost:8081/health"),
            ("ok", "HTTP/1.1 200 OK"),
            ("out", "Content-Type: application/json"),
            ("ok", '{"status":"ok","service":"cloudlite-api","db":"up"}'),
            ("blank", ""),
            ("dim", "# 8081 = anfitrion (por donde entro yo) · 8080 = contenedor (el del EXPOSE)."),
            ("dim", "# Contrato de salud = ruta + codigo + cuerpo con formato. Los tres se califican."),
        ],
        width=840,
    ))
    out.append(terminal(
        ARQ / "Clase 3" / "Capturas" / "salida-docker-ps.png",
        "Clase 3 · Evidencia para el PI: contenedor corriendo",
        [
            ("cmd", "date"),
            ("out", "Tue Sep  8 14:32:07 UTC 2026"),
            ("blank", ""),
            ("cmd", "docker ps"),
            ("dim", "CONTAINER ID   IMAGE                 STATUS         PORTS"),
            ("out", "9f3c1e7a2b48   cloudlite-api:0.1.0   Up 2 minutes   0.0.0.0:8081->8080/tcp"),
            ("blank", ""),
            ("dim", "# Esta salida + el Dockerfile son la evidencia del entregable de hoy."),
            ("dim", "# El `date` de arriba es la hora del sistema que pide la captura (0.5 pts)."),
            ("dim", "# La sesion del lab es temporal: capturar ANTES de cerrarla."),
        ],
        width=840,
    ))
    out.append(terminal(
        ARQ / "Clase 8" / "Capturas" / "salida-actions-run.png",
        "Clase 8 · GitHub Actions — run del workflow de CI",
        # Los nombres de los pasos son los MISMOS de la diapositiva del ci.yml, y la imagen
        # lleva la etiqueta `0.1.0` de la Clase 3: la pregunta 7 da 1 pt por esa coherencia.
        [
            ("dim", "Run  build (ubuntu-latest)"),
            ("ok", "  ✓ Set up job                                    2s"),
            ("ok", "  ✓ actions/checkout@v4                           1s"),
            ("ok", "  ✓ actions/setup-node@v4  (node 20)              4s"),
            ("ok", "  ✓ Construir   npm ci && docker build -t cloudlite-api:0.1.0 .   25s"),
            ("ok", "  ✓ Probar      npm test                          6s"),
            ("out", "  ✓ Despliegue SIMULADO (no despliega a ningun servidor)          2s"),
            ("out", '      Artefacto cloudlite-api:0.1.0 listo para desplegar'),
            ("blank", ""),
            ("ok", "Job succeeded in 40s"),
            ("dim", "# Los tres pasos calificados, en orden: construir -> probar -> desplegar (simulado)."),
            ("dim", "# CI real = construccion + prueba. Un workflow con solo 'echo ok' NO es evidencia:"),
            ("dim", "# si nada puede poner este check en rojo, la condicion de fallo vale 0 (pregunta 8)."),
        ],
    ))
    out.append(terminal(
        ARQ / "Clase 6" / "Capturas" / "salida-secreto-en-imagen.png",
        "Clase 6 · Por que un secreto NUNCA va en la imagen",
        [
            ("dim", "# El estudiante cree que el .env quedo 'adentro y protegido':"),
            # Con etiqueta, y la misma llave de ejemplo que la diapositiva del codigo:
            # el docente proyecta las dos en la misma sesion, y la Clase 3 califica el
            # `docker build` justamente por traer nombre Y etiqueta.
            ("cmd", "docker history --no-trunc cloudlite-api:0.1.0 | head -3"),
            ("out", "COPY . /app        # <-- aqui entro el .env"),
            ("blank", ""),
            ("cmd", "docker run --rm cloudlite-api:0.1.0 cat /app/.env"),
            ("err", "API_KEY=sk_live_9f3a...c21   <-- CUALQUIERA con la imagen lo lee"),
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
