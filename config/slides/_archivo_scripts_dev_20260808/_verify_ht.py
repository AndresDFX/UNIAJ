from pathlib import Path
for name in ["build_uniajc_prog2_curso.py","build_uniajc_seminario_curso.py","build_uniajc_bd2_curso.py","build_uniajc_arq_curso.py"]:
    t=(Path(".config/slides")/name).read_text(encoding="utf-8")
    j=t.find("herramientas_slide(\n        prs")
    print("====", name)
    print(t[j:j+650]); print()
eng=Path(".config/slides/uniajc_slides_engine.py").read_text(encoding="utf-8")
print("logo_cap", "logo_cap" in eng)
CONTENT_W=13.333-1.4
for cols in (3,4):
    gap_x=0.38 if cols<=3 else 0.30
    card_w=(CONTENT_W-gap_x*(cols-1))/cols
    logo_cap={3:2.40,4:2.05}[cols]
    logo_side=min(card_w-0.45, 4.35-0.95-0.35, logo_cap)
    print(f"cols={cols} card_w={card_w:.2f} logo~{logo_side:.2f}")
