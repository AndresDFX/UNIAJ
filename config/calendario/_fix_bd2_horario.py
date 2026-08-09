from pathlib import Path
import csv, io
root = Path(r"G:\Mi unidad\Trabajos\Empleo\UNIAJ\Cursos")
files = [
    root / "Bases de Datos II/Plan curso/2026-2/calendario_eventos_2026-2.csv",
    root / ".config/calendario/eventos_bases_datos_ii_2026-2.csv",
]
def fix_rows(path):
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
    fieldnames = reader.fieldnames
    rows = list(reader)
    for r in rows:
        r["hora_inicio"] = "18:00"
        r["hora_fin"] = "20:00"
        if (r.get("es_parcial") or "").lower() == "si":
            r["tipo_clase"] = "presencial"
            r["notas"] = (r.get("notas") or "").replace("parcial virtual sincrono", "parcial presencial sincrono")
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    out = buf.getvalue()
    path.write_bytes((("\ufeff" + out) if has_bom else out).encode("utf-8"))
    print("OK", path.name, len(rows))
for p in files:
    fix_rows(p)
combo = root / ".config/calendario/eventos_todos_cursos_2026-2.csv"
raw = combo.read_bytes(); has_bom = raw.startswith(b"\xef\xbb\xbf")
reader = csv.DictReader(io.StringIO(raw.decode("utf-8-sig")))
fieldnames = reader.fieldnames; rows = list(reader); n = 0
for r in rows:
    if r.get("curso") == "Bases de Datos II":
        r["hora_inicio"] = "18:00"; r["hora_fin"] = "20:00"; n += 1
        if (r.get("es_parcial") or "").lower() == "si":
            r["tipo_clase"] = "presencial"
            r["notas"] = (r.get("notas") or "").replace("parcial virtual sincrono", "parcial presencial sincrono")
buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=fieldnames, lineterminator="\n"); w.writeheader(); w.writerows(rows)
out = buf.getvalue(); combo.write_bytes((("\ufeff" + out) if has_bom else out).encode("utf-8")); print("OK todos", n)
