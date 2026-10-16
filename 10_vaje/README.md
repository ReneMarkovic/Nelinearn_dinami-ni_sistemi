# Laboratorijski delovni list 10
## Sinhronizacija dveh sklopljenih Van der Polovih oscilatorjev

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_10.pdf](navodila/delavni_list_10.pdf)

---

## 1. Teoretične osnove in motivacija

Sinhronizacija predstavlja pojav uskladitve ritmov samovzbujenih oscilatorjev zaradi šibke medsebojne sklopitve. Za razliko od linearnih oscilatorjev, kjer sklopitev povzroči le linearno interferenco (utripanje), nelinearnost omogoča obstoj robustnih **limitnih ciklov** ter prilagajanje faz in frekvenc (**fazni zaklep**).

Model dveh linearno sklopljenih Van der Polovih oscilatorjev z različnima lastnima frekvencama ($\omega_1 \neq \omega_2$) zapišemo z enačbama:

$$
\begin{aligned}
    \ddot{x}_1 - \mu(1 - x_1^2)\dot{x}_1 + \omega_1^2 x_1 &= K(x_2 - x_1), \\
    \ddot{x}_2 - \mu(1 - x_2^2)\dot{x}_2 + \omega_2^2 x_2 &= K(x_1 - x_2),
\end{aligned}
$$

kjer $\mu > 0$ določa moč nelinearnega samovzbujanja (negativno dušenje pri majhnih amplitudah in pozitivno disipativno dušenje pri velikih odklonih) ter $K$ moč sklopitve med oscilatorjema. Pri preseganju kritične jakosti sklopitve $K_c$ nastopi prehod iz kvaziperiodičnega stanja v popolno sinhronizacijo.

---

## 2. Pripravljalna naloga (analitični del)

1.  Kako se obnaša izoliran Van der Polov oscilator ($K = 0$): zakaj je amplituda njegovega limitnega cikla pri majhnem $\mu$ približno enaka $A \approx 2$?

2.  Pojasnite razliko med linearnim utripanjem dveh sklopljenih vzmeti ($\mu = 0$) in faznim zaklepom dveh nelinearnih oscilatorjev ($\mu > 0$).

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `10_vaje/vaje_10.ipynb`.

### Naloga 1: Simulacija šibke sklopitve – Kvaziperiodično gibanje (35 min)

Izberite parametre $\mu = 1{,}0$, $\omega_1 = 1{,}0$, $\omega_2 = 1{,}2$ ter šibko sklopitev $K = 0{,}1$.

1.  Simulirajte sistem za $t \in [0, 400]$ z začetnimi pogoji $(x_1, v_1, x_2, v_2) = (0{,}8, 0, -0{,}2, 0)$.

2.  Narišite ravnino stanj $(x_1, x_2)$ in opazujte nesklenjeno klobčičasto trajektorijo (torus v faznem prostoru).

### Naloga 2: Prehod v sinhronizacijo pri močni sklopitvi (35 min)

Povečajte parameter sklopitve na $K = 0{,}8$ (nad pragom sklopitve $K_c \approx 0{,}56$).

1.  Narišite časovni potek $x_1(t)$ in $x_2(t)$ ter ravnino $(x_1, x_2)$.

2.  Potrdite, da se trajektorija v ravnini $(x_1, x_2)$ skrči v sklenjen, stabilen limitni cikel popolne sinhronizacije.

### Naloga 3: Analiza razvoja fazne razlike $\Delta \phi(t)$ (20 min)

Določite fazi obeh oscilatorjev prek Hilbertove transformacije ali detekcije vrhov ter izrišite časovni razvoj fazne razlike $\Delta\phi(t) = \phi_1(t) - \phi_2(t)$ za obe vrednosti $K$.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Vpliv frekvenčnega razkoraka $|\omega_1 - \omega_2|$**
>
> Kako je kritična jakost sklopitve $K_c$ odvisna od razlike lastnih frekvenc $|\omega_1 - \omega_2|$? Kaj to pomeni za t.i. Arnoldov jezik (*Arnold tongue*) sinhronizacije?

> **Razmislek 2: Sinhronizacija v naravnih sistemih**
>
> Navedite vsaj dva primera sinhronizacije iz biologije ali tehnike (npr. proženje srčnih celic spodbujevalnikov, sinhrono utripanje kresnic, sinhronizacija elektroenergetskih generatorjev).
