# -*- coding: utf-8 -*-
"""Genera diagramas PNG para presentaciones de Arquitectura (UNIAJC)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "assets" / "arq"
NAVY = (9, 82, 146)
CIAN = (38, 156, 203)
YELLOW = (255, 208, 0)
GRAY = (43, 43, 43)
SOFT = (143, 152, 157)
WHITE = (255, 255, 255)
ALT = (242, 242, 242)
RED = (160, 32, 48)
INFO = (232, 244, 250)


def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for c in candidates:
        p = Path(c)
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def new_img(w=1400, h=900, bg=WHITE):
    im = Image.new("RGB", (w, h), bg)
    return im, ImageDraw.Draw(im)


def rounded_box(draw, xy, fill, radius=18, outline=None, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def center_text(draw, box, text, fnt, fill=GRAY):
    x0, y0, x1, y1 = box
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((x0 + (x1 - x0 - tw) / 2, y0 + (y1 - y0 - th) / 2), text, font=fnt, fill=fill)


def arrow(draw, a, b, fill=CIAN, width=4):
    draw.line([a, b], fill=fill, width=width)
    # punta simple
    bx, by = b
    draw.polygon([(bx, by), (bx - 12, by - 8), (bx - 12, by + 8)], fill=fill)


def save(im, name):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    im.save(path, "PNG")
    print("OK", path)
    return path


def diagram_cloud_layers():
    im, d = new_img()
    title = font(36, True)
    body = font(22, True)
    small = font(18)
    d.text((60, 40), "Arquitectura cloud — bloques lógicos", font=title, fill=NAVY)
    layers = [
        ("Cliente / UI", "Browser · móvil · Padlet demo", CIAN),
        ("Edge / API", "Gateway · autenticación · contratos", NAVY),
        ("Lógica de dominio", "Servicios CloudLite (capacidades)", CIAN),
        ("Datos", "DB · object storage conceptual", NAVY),
        ("Observabilidad", "Logs · métricas · healthchecks", YELLOW),
    ]
    y = 120
    for name, desc, color in layers:
        fill = color if color != YELLOW else ALT
        text_c = WHITE if color != YELLOW else GRAY
        rounded_box(d, (180, y, 1220, y + 110), fill=fill, outline=color if color == YELLOW else None)
        center_text(d, (180, y, 1220, y + 55), name, body, text_c if color != YELLOW else NAVY)
        center_text(d, (180, y + 50, 1220, y + 100), desc, small, text_c if color != YELLOW else SOFT)
        if y < 120 + 110 * 4:
            arrow(d, (700, y + 110), (700, y + 135), CIAN, 5)
        y += 135
    save(im, "cloud_layers.png")


def diagram_c4_context():
    im, d = new_img(1500, 1000)
    title = font(34, True)
    body = font(20, True)
    small = font(16)
    d.text((50, 30), "C4 Context — ejemplo AgendaU (CloudLite)", font=title, fill=NAVY)
    # actores
    actors = [
        (80, 220, "Estudiante"),
        (80, 520, "Docente"),
        (1200, 220, "Email SaaS"),
        (1200, 520, "Auth SaaS"),
    ]
    for x, y, label in actors:
        rounded_box(d, (x, y, x + 220, y + 120), INFO, outline=CIAN)
        center_text(d, (x, y, x + 220, y + 120), label, body, NAVY)
    # sistema
    rounded_box(d, (480, 300, 1020, 620), NAVY)
    center_text(d, (480, 360, 1020, 460), "CloudLite App", font(28, True), WHITE)
    center_text(d, (500, 470, 1000, 580), "Sistema de agenda académica\n(API + lógica + datos)", small, CIAN)
    # flechas
    arrow(d, (300, 280), (480, 400), CIAN)
    arrow(d, (300, 580), (480, 520), CIAN)
    arrow(d, (1020, 400), (1200, 280), CIAN)
    arrow(d, (1020, 520), (1200, 580), CIAN)
    d.text((420, 900), "Personas/sistemas externos ↔ frontera del sistema CloudLite", font=small, fill=SOFT)
    save(im, "c4_context_cloudlite.png")


def diagram_iaas_paas_saas():
    im, d = new_img(1400, 950)
    title = font(34, True)
    body = font(18, True)
    small = font(15)
    d.text((50, 30), "IaaS · PaaS · SaaS — responsabilidad compartida", font=title, fill=NAVY)
    cols = [
        ("On-prem", ["Apps", "Datos", "Runtime", "SO", "Virtualización", "Servidores", "Red/Storage"], RED),
        ("IaaS", ["Apps", "Datos", "Runtime", "SO", "Virtualización*", "Servidores*", "Red*"], NAVY),
        ("PaaS", ["Apps", "Datos", "Runtime*", "SO*", "Virtualización*", "Servidores*", "Red*"], CIAN),
        ("SaaS", ["Apps*", "Datos*", "Runtime*", "SO*", "Virtualización*", "Servidores*", "Red*"], YELLOW),
    ]
    x = 60
    for name, rows, accent in cols:
        rounded_box(d, (x, 100, x + 300, 880), ALT, outline=accent, width=4)
        rounded_box(d, (x, 100, x + 300, 160), accent)
        center_text(d, (x, 100, x + 300, 160), name, body, WHITE if accent != YELLOW else GRAY)
        yy = 190
        for r in rows:
            provider = r.endswith("*")
            label = r.rstrip("*")
            fill = (210, 230, 210) if provider else INFO
            rounded_box(d, (x + 20, yy, x + 280, yy + 70), fill, outline=SOFT, width=1)
            center_text(
                d, (x + 20, yy, x + 280, yy + 70),
                label + (" · proveedor" if provider else " · usted"), small, GRAY,
            )
            yy += 85
        x += 330
    save(im, "iaas_paas_saas.png")


def diagram_vm_vs_container():
    im, d = new_img(1400, 850)
    title = font(34, True)
    body = font(20, True)
    small = font(16)
    d.text((50, 30), "VM vs Contenedor", font=title, fill=NAVY)
    # VM
    rounded_box(d, (80, 120, 640, 780), ALT, outline=NAVY, width=3)
    center_text(d, (80, 140, 640, 190), "Máquina virtual", body, NAVY)
    layers_vm = ["App", "Libs", "Guest OS", "Hypervisor", "Host OS / Hardware"]
    y = 220
    for i, lab in enumerate(layers_vm):
        color = NAVY if i >= 3 else CIAN
        rounded_box(d, (140, y, 580, y + 80), color)
        center_text(d, (140, y, 580, y + 80), lab, small, WHITE)
        y += 100
    # Container
    rounded_box(d, (760, 120, 1320, 780), ALT, outline=CIAN, width=3)
    center_text(d, (760, 140, 1320, 190), "Contenedor", body, CIAN)
    layers_c = ["App", "Libs", "Container runtime", "Host OS (kernel compartido)", "Hardware"]
    y = 220
    for i, lab in enumerate(layers_c):
        color = CIAN if i < 3 else NAVY
        rounded_box(d, (820, y, 1260, y + 80), color)
        center_text(d, (820, y, 1260, y + 80), lab, small, WHITE)
        y += 100
    save(im, "vm_vs_container.png")


def diagram_mono_micro():
    im, d = new_img(1400, 850)
    title = font(34, True)
    body = font(20, True)
    small = font(16)
    d.text((50, 30), "Monolito modular vs microservicios (CloudLite)", font=title, fill=NAVY)
    rounded_box(d, (80, 140, 620, 760), INFO, outline=NAVY, width=3)
    center_text(d, (80, 160, 620, 220), "Monolito modular", body, NAVY)
    for i, lab in enumerate(["API + Agenda", "Auth módulo", "Notificaciones", "Datos compartidos"]):
        y = 260 + i * 100
        rounded_box(d, (140, y, 560, y + 70), NAVY)
        center_text(d, (140, y, 560, y + 70), lab, small, WHITE)
    rounded_box(d, (780, 140, 1320, 760), ALT, outline=CIAN, width=3)
    center_text(d, (780, 160, 1320, 220), "2–5 contenedores lógicos", body, CIAN)
    boxes = [("API Gateway", 280), ("Agenda Svc", 400), ("Notify Svc", 520), ("DB / Object", 640)]
    for lab, y in boxes:
        rounded_box(d, (860, y, 1240, y + 80), CIAN)
        center_text(d, (860, y, 1240, y + 80), lab, small, WHITE)
    d.text((80, 780), "Regla: justifique cada caja. Evite 'microservicios teatro'.", font=small, fill=SOFT)
    save(im, "mono_vs_micro.png")


def diagram_network_zones():
    im, d = new_img(1400, 850)
    title = font(34, True)
    body = font(22, True)
    small = font(16)
    d.text((50, 30), "Zonas de confianza — despliegue CloudLite", font=title, fill=NAVY)
    zones = [
        ("Pública / Edge", "Cliente · CDN · API Gateway", CIAN, 140),
        ("Privada / App", "Servicios de dominio", NAVY, 360),
        ("Datos", "DB · object storage · backups", YELLOW, 580),
    ]
    for name, desc, color, y in zones:
        fill = ALT if color == YELLOW else color
        tc = GRAY if color == YELLOW else WHITE
        rounded_box(d, (120, y, 1280, y + 170), fill, outline=color, width=4)
        center_text(d, (120, y + 30, 1280, y + 90), name, body, NAVY if color == YELLOW else WHITE)
        center_text(d, (120, y + 90, 1280, y + 150), desc, small, SOFT if color == YELLOW else CIAN)
        if y < 580:
            arrow(d, (700, y + 170), (700, y + 200), CIAN, 5)
    save(im, "network_zones.png")


def diagram_cicd():
    im, d = new_img(1500, 700)
    title = font(34, True)
    body = font(18, True)
    small = font(15)
    d.text((50, 30), "CI/CD conceptual — GitHub Actions (free)", font=title, fill=NAVY)
    steps = ["Push", "Checkout", "Build", "Test", "Artifact", "Deploy\nsimulado"]
    x = 60
    for i, st in enumerate(steps):
        rounded_box(d, (x, 220, x + 200, 420), NAVY if i % 2 == 0 else CIAN)
        center_text(d, (x, 220, x + 200, 420), st, body, WHITE)
        if i < len(steps) - 1:
            arrow(d, (x + 200, 320), (x + 240, 320), YELLOW, 6)
        x += 240
    d.text((60, 520), "Secrets en Settings · nunca en Dockerfile · CD = echo/artifact (sin tarjeta)", font=small, fill=SOFT)
    save(im, "cicd_pipeline.png")


def diagram_stride():
    im, d = new_img(1400, 850)
    title = font(34, True)
    body = font(18, True)
    small = font(15)
    d.text((50, 30), "STRIDE-lite para CloudLite", font=title, fill=NAVY)
    items = [
        ("S", "Spoofing", "Tokens + HTTPS"),
        ("T", "Tampering", "Validación de entrada"),
        ("R", "Repudiation", "Logs de auditoría"),
        ("I", "Info disclosure", "Least privilege + TLS"),
        ("D", "DoS", "Rate limit / health"),
        ("E", "Elevation", "Roles mínimos"),
    ]
    positions = [(80, 140), (500, 140), (920, 140), (80, 480), (500, 480), (920, 480)]
    for (letter, name, ctrl), (x, y) in zip(items, positions):
        rounded_box(d, (x, y, x + 380, y + 260), ALT, outline=NAVY, width=3)
        rounded_box(d, (x + 20, y + 20, x + 100, y + 100), NAVY)
        center_text(d, (x + 20, y + 20, x + 100, y + 100), letter, font(28, True), WHITE)
        d.text((x + 120, y + 40), name, font=body, fill=NAVY)
        d.text((x + 40, y + 140), "Control:", font=small, fill=SOFT)
        d.text((x + 40, y + 175), ctrl, font=body, fill=CIAN)
    save(im, "stride_lite.png")


def diagram_autoscaling():
    im, d = new_img(1400, 800)
    title = font(34, True)
    body = font(18, True)
    small = font(15)
    d.text((50, 30), "Autoescalado conceptual CloudLite", font=title, fill=NAVY)
    rounded_box(d, (100, 150, 500, 350), INFO, outline=CIAN, width=3)
    center_text(d, (100, 150, 500, 350), "Métricas\nRPS · p95 · cola", body, NAVY)
    arrow(d, (500, 250), (620, 250), YELLOW, 6)
    rounded_box(d, (620, 150, 980, 350), NAVY)
    center_text(d, (620, 150, 980, 350), "Política\nmin / max / cooldown", body, WHITE)
    arrow(d, (980, 250), (1100, 250), YELLOW, 6)
    rounded_box(d, (1100, 120, 1320, 220), CIAN)
    center_text(d, (1100, 120, 1320, 220), "API x2", body, WHITE)
    rounded_box(d, (1100, 250, 1320, 350), CIAN)
    center_text(d, (1100, 250, 1320, 350), "API x3", body, WHITE)
    rounded_box(d, (100, 450, 1320, 700), ALT, outline=RED, width=3)
    center_text(d, (100, 480, 1320, 560), "Lo que NO escala igual", body, RED)
    center_text(d, (100, 560, 1320, 680), "Base de datos · estado en sesión · jobs largos sin cola", small, GRAY)
    save(im, "autoscaling.png")


def diagram_cost_drivers():
    im, d = new_img(1400, 800)
    title = font(34, True)
    body = font(20, True)
    small = font(16)
    d.text((50, 30), "Drivers de costo (cualitativo B / M / A)", font=title, fill=NAVY)
    drivers = [
        ("Compute idle", "Instancias siempre-on", "B→A según horas"),
        ("Egress", "Salida de datos", "A en media/CDN mal"),
        ("Storage", "DB + objetos", "M crece con historial"),
        ("CI minutos", "Actions free tier", "B si pipeline corto"),
    ]
    x = 70
    for name, desc, note in drivers:
        rounded_box(d, (x, 160, x + 300, 680), ALT, outline=CIAN, width=3)
        rounded_box(d, (x, 160, x + 300, 250), NAVY)
        center_text(d, (x, 160, x + 300, 250), name, body, WHITE)
        center_text(d, (x + 20, 300, x + 280, 450), desc, small, GRAY)
        center_text(d, (x + 20, 500, x + 280, 620), note, body, CIAN)
        x += 330
    save(im, "cost_drivers.png")


def diagram_cloudlite_stack():
    im, d = new_img(1400, 900)
    title = font(34, True)
    body = font(18, True)
    small = font(15)
    d.text((50, 30), "Stack CloudLite — gratis + navegador", font=title, fill=NAVY)
    tools = [
        ("draw.io", "C4 / Deployment"),
        ("Excalidraw", "Bocetos rápidos"),
        ("Killercoda", "Labs contenedor"),
        ("LabEx Docker Playground", "Build/run stub"),
        ("GitHub Actions", "CI/CD simulado"),
        ("Google Docs", "Informe PI"),
    ]
    positions = [(80, 140), (520, 140), (960, 140), (80, 480), (520, 480), (960, 480)]
    for (name, use), (x, y) in zip(tools, positions):
        rounded_box(d, (x, y, x + 360, y + 260), INFO, outline=NAVY, width=3)
        center_text(d, (x, y + 40, x + 360, y + 120), name, body, NAVY)
        center_text(d, (x, y + 140, x + 360, y + 220), use, small, CIAN)
    save(im, "cloudlite_stack.png")


def main():
    diagram_cloud_layers()
    diagram_c4_context()
    diagram_iaas_paas_saas()
    diagram_vm_vs_container()
    diagram_mono_micro()
    diagram_network_zones()
    diagram_cicd()
    diagram_stride()
    diagram_autoscaling()
    diagram_cost_drivers()
    diagram_cloudlite_stack()
    print("DONE assets →", OUT)


if __name__ == "__main__":
    main()
