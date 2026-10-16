# Laboratorijski delovni list 4
## Bistabilnost in dinamika delca v dvojni potencialni jami

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko · *Nelinearni dinamični sistemi*

> [!IMPORTANT]
> **Programsko okolje: Python**
>
> Vse računalniške naloge te vaje se izvajajo **izključno v programskem jeziku Python** (priporočena različica 3.10 ali novejša). Uporabljamo knjižnice `numpy`, `scipy` (`solve_ivp`), `sympy` (simbolno računanje) in `matplotlib` (`contour`, `streamplot`). Uporaba drugih programskih jezikov ali okolij (npr. MATLAB, Octave, Mathematica) ni predvidena. Rešitev oddajte kot Jupyter zvezek (`.ipynb`).

---

## 1. Teoretične osnove in motivacija

Ena ključnih lastnosti, ki ločuje nelinearne sisteme od linearnih, je zmožnost obstoja **več izoliranih stabilnih ravnotežnih stanj** (bistabilnost ali multistabilnost). Linearni avtonomni sistemi lahko posedujejo kvečjemu eno izolirano stacionarno točko ali pa kontinuum ravnotežij, nikoli pa več ločenih stabilnih privlačnih leg.

Klasični primer nelinearnega bistabilnega pojava je gibanje točkastega delca v potencialu z dvojno jamo ob prisotnosti dušenja:

$$
\ddot{x} + d\dot{x} = F(x), \quad \text{kjer je } F(x) = ax - bx^3, \quad a > 0,\ b > 0.
$$

Tukaj je $d \ge 0$ koeficient viskoznega dušenja, nelinearna povratna sila pa izhaja iz potencialne funkcije $F(x) = -\frac{dV}{dx}$:

$$
V(x) = -\frac{a}{2}x^2 + \frac{b}{4}x^4.
$$

### 1.1 Ravnotežne točke in lokalna stabilnost

Stacionarne točke sistema v faznem prostoru $(x, v)$, kjer je $v = \dot{x}$, določata pogoja $\dot{x} = v = 0$ in $\dot{v} = ax - bx^3 = 0$:

1. $x_0^{\ast} = 0$: lokalni maksimum potenciala ($V(0) = 0$), ki ustreza **sedelni točki** v ravnini faznih stanj (nestabilno ravnotežje).
2. $x_{1,2}^{\ast} = \pm\sqrt{a/b}$: dva simetrična lokalna minimuma potenciala z energijo $V_{\min} = -\frac{a^2}{4b}$, ki ustrezata **stabilnima stanjema**.

Pri $d > 0$ sta točki $(\pm\sqrt{a/b}, 0)$ privlačni gorišči ali vozlišči, točka $(0,0)$ pa ostane sedlo.

### 1.2 Energetska bilanca, separatrisa in privlačna območja

Skupna mehanska energija delca z enotsko maso je $E(x, v) = \frac{1}{2}v^2 + V(x)$. Časovni odvod energije vzdolž trajektorije poda disipacijo:

$$
\frac{dE}{dt} = v\dot{v} + \frac{dV}{dx}\dot{x} = v(ax - bx^3 - dv) - (ax - bx^3)v = -d v^2 \le 0.
$$

Kadar ni dušenja ($d = 0$), se energija ohranja ($E = \text{konst.}$), trajektorija, ki poteka skozi sedelno točko z energijo $E = 0$, pa tvori **separatriso**. Separatrisa v obliki osmice razmejuje oscilacije znotraj posamezne jame od tistih, ki prehajajo prek obeh jamic.

Pri prisotnem dušenju ($d > 0$) vsaka trajektorija sčasoma konvergira v eno od dveh stabilnih leg. Fazni prostor se razdeli na dva **bazena privlačnosti** (*basins of attraction*), mejo med njima pa tvori stabilna mnogoterost sedelne točke v izhodišču.

---

## 2. Pripravljalna naloga (analitični del)

Za sistem izberemo normirane parametre iz učbenika: $a = 1{,}0$, $b = 1{,}0$ ter dušenje $d = 0{,}3$.

1. Zapišite sistem dveh diferencialnih enačb prvega reda za $x$ in $v = \dot{x}$:

   $\dot{x} =$ ____________________  $\dot{v} =$ ______________________________

2. Določite numerične koordinate vseh treh stacionarnih točk $(x^{\ast}, v^{\ast})$ v fazni ravnini:

   $T_0^{\ast} = (0, 0)$, $T_1^{\ast} = ($ ______ $, 0)$, $T_2^{\ast} = ($ ______ $, 0)$.

3. Zapišite splošno Jacobijevo matriko sistema $\mathbf{J}(x, v)$ ter jo ovrednotite v točkah $T_0^{\ast}$ in $T_1^{\ast}$:

   $\mathbf{J}(0, 0) =$ __________  $\mathbf{J}(1, 0) =$ __________

4. Za točko $T_1^{\ast} = (1, 0)$ izračunajte sled $\tau$, determinanto $\Delta$ in lastni vrednosti $\lambda_{1,2}$. Določite tip ravnotežja:

   $\tau =$ ______, $\Delta =$ ______ $\implies$ Tip: ____________________

---

## 3. Laboratorijske naloge na računalniku (Python)

Vse naloge v tem razdelku rešite v programskem jeziku **Python**.

> **Programsko okolje in začetna predloga**
>
> Začetni Jupyter zvezek za vajo se nahaja v repozitoriju predmeta pod: `04_vaje/vaje_04.ipynb`
>
> Zvezek odprite in vanj dopolnite funkcije za izris potenciala, vektorskega polja in kartiranje privlačnih bazenov.

### Naloga 1: Profil potenciala in nivojnice energije (25 min)

1. Izrišite profil potencialne energije $V(x) = -\frac{a}{2}x^2 + \frac{b}{4}x^4$ na območju $x \in [-2, 2]$. Označite oba minimuma in vrh pregrade pri $x=0$.
2. Za primer brez dušenja ($d = 0$) narišite nivojnice skupne mehanske energije $E(x, v) = \frac{1}{2}v^2 + V(x) = \text{konst.}$ v fazni ravnini s funkcijo `matplotlib.pyplot.contour`. Posebej poudarite separatriso z energijo $E = 0$.

### Naloga 2: Fazni portret dušenega sistema in konvergence (35 min)

1. Vključite dušenje $d = 0{,}3$. Na območju $(x, v) \in [-2, 2] \times [-2, 2]$ izrišite vektorsko polje toka s funkcijo `matplotlib.pyplot.streamplot`.
2. Z numeričnim integratorjem (npr. `scipy.integrate.solve_ivp`) simulirajte časovni odziv za začetna pogoja iz učbenika:
   - Trajektorija A: $(x_0, v_0) = (-1{,}5,\ 0{,}5)$
   - Trajektorija B: $(x_0, v_0) = (1{,}5,\ -0{,}5)$

   Obe trajektoriji vrišite v fazno ravnino in potrdite, da konvergirata vsaka v svoj stabilni jašek.
3. Izrišite časovni potek mehanske energije $E(t)$ in preverite, da se energija monotono zmanjšuje proti $V_{\min} = -0{,}25$.

### Naloga 3: Kartiranje bazenov privlačnosti (30 min)

Za mrežo začetnih pogojev $(x_0, v_0) \in [-2, 2] \times [-2, 2]$ z ločljivostjo vsaj $100 \times 100$ točk določite končno stanje po dovolj dolgem času integracije ($t_{\text{end}} \approx 30$).

- Če se trajektorija ustali v levem minimumu ($x^{\ast} \approx -1$), točko obarvajte modro.
- Če se trajektorija ustali v desnem minimumu ($x^{\ast} \approx +1$), točko obarvajte rdeče.
- Izrišite dobljeno karto in opazujte mejo med bazenoma, ki poteka skozi sedelno točko $(0,0)$.

| Začetni pogoj $(x_0, v_0)$ | Končna lega $x(\infty)$ | Končna energija $E(\infty)$ | Bazen privlačnosti |
|:-:|:-:|:-:|:-:|
| $(-1{,}5,\ 0{,}5)$ | | | Levi / Desni |
| $(1{,}5,\ -0{,}5)$ | | | Levi / Desni |
| $(0{,}1,\ 0{,}0)$ | | | Levi / Desni |
| $(-0{,}1,\ 0{,}0)$ | | | Levi / Desni |
| $(0{,}0,\ 1{,}2)$ | | | Levi / Desni |

*Preglednica 1: Konvergentna analiza izbranih začetnih točk.*

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Vpliv začetne energije na preskok pregrade**
>
> Kolikšna mora biti minimalna začetna kinetična energija delca, ki miruje na dnu levega jaška ($x_0 = -1, v_0 = 0$), da lahko preskoči potencialno pregrado in preide v desni jašek? Kako se ta pogoj spremeni, če je dušenje $d > 0$?

> **Razmislek 2: Geometrija meje med bazeni**
>
> Meja med obema bazenoma privlačnosti predstavlja stabilno mnogoterost sedelne točke v izhodišču. Ali se trajektorija, ki se začne točno na tej meji, sploh kdaj ustali v enem od obeh jaškov? Kaj se zgodi ob prisotnosti majhnega numeričnega šuma?

> **Razmislek 3: Primerjava z linearnim oscilatorjem**
>
> Zakaj linearni harmonski oscilator $\ddot{x} + d\dot{x} + \omega_0^2 x = 0$ nikoli ne more imeti dveh različnih bazenov privlačnosti, ne glede na vrednosti parametrov in začetnih pogojev? Pojasnite z vidika načela superpozicije in oblike potenciala.
