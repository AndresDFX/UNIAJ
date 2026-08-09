from build_uniajc_bd2_all import CLASES, build_pptx
ok = []
for c in CLASES:
    if c["tipo"] == "parcial":
        print("SKIP parcial", c["n"])
        continue
    out = build_pptx(c)
    if out:
        ok.append(c["n"])
print("BD2 PPTX:", ok)
