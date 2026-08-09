# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(__file__).resolve().parents[2] / ".claude/agents/uniajc-dudas-material.md"
raw = p.read_bytes()
if raw[:2] in (b"\xff\xfe", b"\xfe\xff") or (len(raw) > 3 and raw[1] == 0):
    t = raw.decode("utf-16")
else:
    t = raw.decode("utf-8")

t = t.replace(
    "| Arquitectura de Sist. Comp. | lun 10:00–13:00 (180 min) | Skeleton + Acuerdo/Calendario 2026-2 (grupo/código pendientes) |",
    "| Arquitectura de Sist. Comp. | lun 10:00–13:00 (180 min) · Presencialidad asistida | Skeleton + Acuerdo/Calendario 2026-2 (grupo pendiente) |",
)

old = (
    "**Evaluación teórica 2026-2:** 30/30/40 · Parcial 1/2/3 al cierre de cada corte (Clases 5, 10, 15) · "
    "talleres/quiz + asistencia · Proyecto Integrador en Corte 3 · festivos = clase autónoma.\n"
    "\n"
    "## Separación material (recordatorio)\n"
    "\n"
    "- **Presentación del curso:** docente, grupo/periodo en negrita, evaluación, cronograma, Campus Virtual.\n"
    "- **PPTX / guion de clase:** solo tema de esa clase + nº discreto («Clase N»). "
    "Sin fechas de periodo, sin mapa completo del curso, sin bio, sin políticas globales de evaluación.\n"
    "- Plataforma: **Campus Virtual UNIAJC** (URL pendiente). Nunca “LMS” como nombre · nunca CDigital/CUN.\n"
)
new = (
    "**Evaluación teórica 2026-2:** 30/30/40 · Parciales en última regular del corte "
    "(mié/jue 5/10/15; lun 5/9/14) · siempre **presenciales** · talleres/quiz + asistencia · "
    "Proyecto Integrador en Corte 3 · festivos = clase autónoma.\n"
    "\n"
    "**Modalidad por sesión:** Clase 1 presencial · resto virtual · parciales presencial · "
    "festivos autónoma (encuadre: Presencialidad asistida).\n"
    "\n"
    "## Separación material (recordatorio)\n"
    "\n"
    "- **Presentación del curso:** docente, grupo/periodo en negrita, evaluación, cronograma, Padlet. "
    "**Sin** placeholder de Campus Virtual ni de listado de estudiantes.\n"
    "- **PPTX / guion de clase:** solo tema de esa clase + nº discreto («Clase N»). "
    "Sin fechas de periodo, sin mapa completo del curso, sin bio, sin políticas globales de evaluación.\n"
    "- Plataforma de entregas: **Campus Virtual UNIAJC** (no poner URL pendiente en slides del curso). "
    "Nunca “LMS” como nombre · nunca CDigital/CUN.\n"
)
if old in t:
    t = t.replace(old, new)
    print("dudas block replaced")
else:
    print("dudas block NOT found; writing markers")
    print("eval in file", "Evaluación teórica 2026-2" in t)
    print("Campus Virtual in sep", "cronograma, Campus Virtual" in t)

p.write_text(t, encoding="utf-8")
print("done", "Clase 1 presencial" in t, "**Sin** placeholder" in t)

# Patch arq build modality info line
bp = Path(__file__).resolve().parents[2] / ".config/slides/build_uniajc_arq_curso.py"
raw = bp.read_bytes()
if raw[:2] in (b"\xff\xfe", b"\xfe\xff") or (len(raw) > 3 and raw[1] == 0):
    bt = raw.decode("utf-16")
else:
    bt = raw.decode("utf-8")
oldb = "Lunes 10:00-13:00 (180 min). Modalidad: Presencialidad asistida. Grupo: [PENDIENTE]."
newb = (
    "Lunes 10:00-13:00 (180 min). Modalidad: Presencialidad asistida "
    "(Clase 1 presencial / resto virtual / parciales presencial). Grupo: [PENDIENTE]."
)
if oldb in bt:
    bt = bt.replace(oldb, newb)
    bp.write_text(bt, encoding="utf-8")
    print("arq build patched")
else:
    print("arq build line missing", oldb[:40] in bt)
