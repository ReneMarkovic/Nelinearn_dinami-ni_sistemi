# Laboratorijski delovni list 12
## Zaprtozančni sistemi s povratno vezavo in redukcija blokovnih shem

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_12.pdf](navodila/delavni_list_12.pdf)

---

## 1. Teoretične osnove in motivacija

Povratna vezava predstavlja temeljni mehanizem avtomatskega vodenja in stabilizacije fizikalnih procesov. Z vračanjem dela izhodnega signala $Y(s)$ prek povratne veje $F_2(s)$ na vhodni seštevalnik tvorimo signal regulacijske napake $E(s) = X(s) - F_2(s)Y(s)$. Prenosna funkcija zaprte zanke z negativno povratno vezavo je:

$$
H(s) = \frac{Y(s)}{X(s)} = \frac{F_1(s)}{1 + F_1(s) F_2(s)},
$$

kjer je $F_0(s) = F_1(s) F_2(s)$ prenosna funkcija odprte zanke.

Negativna povratna vezava zmanjšuje občutljivost sistema na motnje, pospešuje odziv in omogoča stabilizacijo inherentno nestabilnih procesov. Vendar pa lahko preveliko ojačanje v zaprti zanki povzroči fazni zamik in sistem privede v samovzbudno nihanje ali nestabilnost. V praksi kompleksne strukture z več zankami poenostavimo s postopno algebrajsko redukcijo blokovnih shem.

---

## 2. Pripravljalna naloga (analitični del)

Obravnavamo regulacijo procesa prvega reda $F_p(s) = \frac{1}{s + 2}$ s proporcionalnim regulatorjem $F_r(s) = K_p$ in enotsko negativno povratno vezavo ($F_2(s) = 1$).

1.  Izpeljite prenosno funkcijo zaprte zanke $H(s)$ v odvisnosti od $K_p$:  
    $H(s) =$ \_\_\_\_\_\_\_\_\_\_

2.  Izračunajte stacionarno regulacijsko napako $e_{\text{stat}} = \lim_{t \to \infty} (1 - y(t))$ za enotski stopničasti vhod ($X(s) = 1/s$) prek izreka o končni vrednosti.

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `12_vaje/vaje_12.ipynb`.

### Naloga 1: Algebrajska redukcija večzančne blokovne sheme (35 min)

Za sistem iz učbenika s prenosnimi funkcijami $F_1, F_2, F_3, F_4, F_5, F_6, F_7$:

$$
H_0(s) = \frac{F_1 F_2 F_3 F_4}{1 + F_2 F_3 F_4 F_5 + F_1 F_2 F_3 F_6 F_7}
$$

v programskem jeziku Python s knjižnico `scipy.signal` ali orodjem `control` definirajte posamezne bloke ter sestavite skupno nadomestno prenosno funkcijo $H_0(s)$.

### Naloga 2: Primerjava P- in PI-regulacije na odpravo stacionarne napake (35 min)

Za proces $F_p(s) = \frac{2}{s^2 + 3s + 2}$ simulirajte stopničasti odziv zaprte zanke:

1.  S čisto proporcionalnim vodenjem ($F_r(s) = K_p$) pri $K_p \in \{2, 5, 10\}$; zabeležite prenihaj in stacionarni odstop.

2.  Z dodanim integracijskim členom ($F_r(s) = K_p + \frac{K_i}{s}$) ter pokažite, da integrator $1/s$ popolnoma odpravi stacionarno napako ($y(\infty) = 1$).

### Naloga 3: Analiza korenov in meja stabilnosti (20 min)

Izračunajte lege polov zaprte zanke pri naraščanju ojačanja $K_p$ ter izrišite trajektorijo korenov (*root locus*).

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Odprava napake z integralnim členom**
>
> Zakaj integralni člen $1/s$ v regulacijski zanki matematično zagotavlja ničelno napako v stacionarnem stanju za stopničast vhod? Pojasnite to z vidika pola v izhodišču $s=0$.

> **Razmislek 2: Vpliv pozitivne povratne vezave**
>
> Kaj se zgodi z imenovalcem zaprte zanke, če namesto negativne uporabimo pozitivno povratno vezavo ($1 - F_1(s)F_2(s)$)? Kje v fiziki pozitivno povratno vezavo namerno izkoriščamo (npr. laserji, oscilatorji)?
