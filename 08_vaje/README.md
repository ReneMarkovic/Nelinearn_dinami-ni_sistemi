# Laboratorijski delovni list 8
## Prehod v deterministični kaos v Lorenzovem sistemu

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_08.pdf](navodila/delavni_list_08.pdf)

---

## 1. Teoretične osnove in motivacija

Deterministični kaos predstavlja pojav, kjer natančno določene deterministične enačbe gibanja brez prisotnosti naključnega šuma generirajo aperiodičen in dolgoročno nepredvidljiv odziv. V skladu s Poincaré–Bendixsonovim izrekom se v zveznih avtonomnih sistemih kaos lahko pojavi le v sistemih z vsaj tremi dinamičnimi spremenljivkami ($N \ge 3$).

Najbolj znan paradigmatski primer je Lorenzov sistem treh sklopljenih nelinearnih diferencialnih enačb prvega reda:

$$
\begin{aligned}
    \dot{x} &= \sigma(y - x), \\
    \dot{y} &= r x - y - x z, \\
    \dot{z} &= x y - b z,
\end{aligned}
$$

kjer $\sigma$ predstavlja Prandtlovo število, $r$ Rayleighjevo število ter $b$ geometrijski parameter konvektivne celice. Sistem je disipativen, saj je divergenca faznega toka konstantna in negativna:

$$
\mathrm{div} \mathbf{f} = \frac{\partial \dot{x}}{\partial x} + \frac{\partial \dot{y}}{\partial y} + \frac{\partial \dot{z}}{\partial z} = -(\sigma + 1 + b) < 0.
$$

Vsak začetni fazni volumen $V(0)$ se v času eksponentno krči ($V(t) = V(0) e^{-(\sigma+1+b)t}$), kar trajektorije prisili k akumulaciji na geometrijsko zapleteni fraktalni strukturi – **čudnem atraktorju**.

---

## 2. Pripravljalna naloga (analitični del)

1.  Poiščite vse tri stacionarne točke Lorenzovega sistema:

    - Izhodišče: $C_0^{\ast} = (0, 0, 0)$.

    - Dve simetrični konvektivni stanji (za $r > 1$): $C_{1,2}^{\ast} = (\pm\sqrt{b(r-1)}, \, \pm\sqrt{b(r-1)}, \, r-1)$.

2.  Za standardne parametre $\sigma = 10$ in $b = 8/3$ izračunajte hitrost krčenja volumna $\mathrm{div} \mathbf{f}$:  
    $\mathrm{div} \mathbf{f} =$ \_\_\_\_\_\_\_\_\_\_

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `08_vaje/vaje_08.ipynb`.

### Naloga 1: Integracija in 3D vizualizacija atraktorja (35 min)

Simulirajte Lorenzov sistem za klasične parametre kaosa: $\sigma = 10$, $b = 8/3$ in $r = 28$ z metodo RK45.

1.  Izrišite 3D fazni portret $(x(t), y(t), z(t))$ ter 2D projekciji v ravninah $(x, z)$ in $(x, y)$.

2.  Opazujte preklapljanje trajektorije med obema kriloma atraktorja (metuljasti atraktor).

### Naloga 2: Demonstracija občutljivosti na začetne pogoje (35 min)

Izberite dva izhodiščna pogoja z izjemno majhno razliko:

- Trajektorija 1: $\mathbf{x}_1(0) = (1{,}0, \, 1{,}0, \, 1{,}0)$

- Trajektorija 2: $\mathbf{x}_2(0) = (1{,}0 + 10^{-8}, \, 1{,}0, \, 1{,}0)$

1.  Na istem grafu izrišite časovni potek $x_1(t)$ in $x_2(t)$ za čas $t \in [0, 40]$.

2.  Določite časovni horizont predvidljivosti $t_{\text{pred}}$, pri katerem se rešitvi povsem razideta.

### Naloga 3: Eksploracija dinamike pri različnih vrednostih $r$ (20 min)

Spremenite parameter $r$: simulirajte stabilno stanje pri $r=15$, subkritično nihanje pri $r=22$ ter popolnoma razvit kaos pri $r=28$.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Krčenje volumna in raztezanje trajektorij**
>
> Kako je mogoče, da se fazni volumen disipativno krči ($\mathrm{div}\mathbf{f} < 0$), hkrati pa se sosednje trajektorije eksponentno oddaljujejo? Pojasnite geometrijski mehanizem raztezanja in prepogibanja (*stretching and folding*).

> **Razmislek 2: Determinizem proti napovedljivosti**
>
> Ali Lorenzov sistem vsebuje kakršnekoli stohastične ali naključne člene? Kakšna je razlika med determinističnim kaosom in čistim statističnim šumom?
