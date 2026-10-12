import os
import subprocess

# koren repozitorija = mapa te skripte
base = os.path.dirname(os.path.abspath(__file__))

#Preveri če obstaja mapa z navodili za vsako vajo če ne ustvari ustrezen tex dokument, ki ga bom napolnil kasneje
for vaja in range(1, 16, 1):
    folder = os.path.join(base, f"{vaja:02d}_vaje", "navodila")
    if not os.path.exists(folder):
        os.makedirs(folder)
        tex_file = os.path.join(folder, f"delavni_list_{vaja:02d}.tex")
        with open(tex_file, "w", encoding="utf-8") as f:
            f.write("\\documentclass[a4paper,12pt]{article}\n")
            f.write("\\usepackage[utf8]{inputenc}\n")
            f.write("\\usepackage[T1]{fontenc}\n")
            f.write("\\usepackage{lmodern}\n")
            f.write("\\usepackage{geometry}\n")
            f.write("\\geometry{a4paper, margin=2.5cm}\n")
            f.write("\\usepackage{amsmath, amssymb}\n")
            f.write("\\usepackage{graphicx}\n")
            f.write("\\usepackage{hyperref}\n")
            f.write("\\begin{document}\n")
            f.write(f"\\section*{{Delavni list {vaja:02d}}}\n")
            f.write("\\end{document}\n")
        
    

for vaja in range(1, 16, 1):
    folder = os.path.join(base, f"{vaja:02d}_vaje", "navodila")
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".tex"):
                print(os.path.join(root, file))
                # dva prehoda zaradi kazala/hyperref
                for _ in range(2):
                    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", file],cwd=root, capture_output=True, text=True, errors="replace")
                if res.returncode != 0:
                    print(f"  NAPAKA: glej {os.path.splitext(file)[0]}.log")


