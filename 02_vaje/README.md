# Laboratorijski delovni list 2
## Nelinearna vezava med amplitudo in frekvenco oscilacij

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko

| | |
|---|---|
| **Predmet:** Nelinearni dinamični sistemi | **Študent/ka:** ____________________ |
| **Letnik/Smer:** 1. letnik MAG / Fizika | **Vpisna številka:** ____________________ |
| **Izvedba:** 2 šolski uri (90 min) | **Datum izvedbe:** ____________________ |

> [!IMPORTANT]
> **Programsko okolje: Python**
>
> Vse računalniške naloge te vaje se izvajajo **izključno v programskem jeziku Python** (priporočena različica 3.10 ali novejša). Uporabljamo knjižnice `numpy`, `scipy` (`solve_ivp`, `ellipk`), `sympy` (simbolno računanje) in `matplotlib` (grafični prikaz). Uporaba drugih programskih jezikov ali okolij (npr. MATLAB, Octave, Mathematica) ni predvidena. Rešitev oddajte kot Jupyter zvezek (`.ipynb`).

---

## 1. Teoretične osnove in motivacija

Pri linearnem harmonskem oscilatorju je povratna sila premo sorazmerna z odmikom ($F = -kx$), zato je lastna krožna frekvenca $\omega_0 = \sqrt{k/m}$ univerzalna konstanta sistema, neodvisna od začetnega odmika. V nelinearnih sistemih pa deformacija oblike potenciala povzroči, da se efektivna togost spreminja z amplitudo nihanja $A$, kar vodi do **nelinearnega frekvenčnega premika** $\omega = \omega(A)$.

### 1.1 Nitno nihalo pri poljubnih odklonih

Enačba prostega nihanja matematičnega nihala z dolžino $L$ v gravitacijskem polju $g$ je:

$$
\ddot{\theta} + \frac{g}{L}\sin\theta = 0.
$$

Iz ohranitve celotne mehanske energije pri začetnem kotnem odmiku $\theta_0$ (ob $\dot{\theta}(0) = 0$) izpeljemo natančni nihajni čas:

$$
T(\theta_0) = 4\sqrt{\frac{L}{g}} \int_{0}^{\pi/2} \frac{d\phi}{\sqrt{1 - k^2\sin^2\phi}} = 4\sqrt{\frac{L}{g}}\, K(k), \quad \text{kjer je } k = \sin\left(\frac{\theta_0}{2}\right).
$$

Integralska funkcija $K(k)$ je **popolni eliptični integral prve vrste**. Z razvojem v vrsto za majhne do zmerne odklone dobimo popravek glede na harmonsko periodo $T_0 = 2\pi\sqrt{L/g}$:

$$
T(\theta_0) \approx T_0 \left( 1 + \frac{1}{4}\sin^2\frac{\theta_0}{2} + \frac{9}{64}\sin^4\frac{\theta_0}{2} + \dots \right) \approx T_0 \left( 1 + \frac{1}{16}\theta_0^2 \right).
$$

Ker sila $\sin\theta < \theta$ narašča počasneje kot pri linearnem približku, se efektivna togost zmanjšuje (*mehčanje*), kar povzroči podaljševanje nihajnega časa ($T$ raste, $\omega$ pada).

### 1.2 Duffingov oscilator

Pri Duffingovem oscilatorju linearni elastični sili dodamo kubični nelinearni člen:

$$
\ddot{x} + \omega_0^2 x + \alpha x^3 = 0.
$$

Z metodo perturbacij (motenjska metoda prvega reda) izpeljemo odvisnost frekvence od amplitude $A$:

$$
\omega(A) \approx \omega_0 \left( 1 + \frac{3}{8}\frac{\alpha}{\omega_0^2} A^2 \right).
$$

Kadar je $\alpha > 0$, govorimo o **utrjeni vzmeti** (*hardening spring*, frekvenca $\omega$ raste z $A$), pri $\alpha < 0$ pa o **mehčani vzmeti** (*softening spring*, frekvenca $\omega$ pada z $A$).

---

## 2. Pripravljalna naloga (analitični del)

Za matematično nihalo z dolžino $L = 1{,}0\ \text{m}$ in težnim pospeškom $g = 9{,}81\ \text{m/s}^2$ je linearna perioda $T_0 = 2\pi\sqrt{L/g} \approx 2{,}006\ \text{s}$.

1. Izračunajte parameter eliptičnega integrala $k = \sin(\theta_0/2)$ in analitični približek $T(\theta_0) \approx T_0(1 + \frac{1}{16}\theta_0^2)$ za odklon $\theta_0 = 60^\circ$ ($\theta_0 = \pi/3\ \text{rad}$):

   $k =$ __________  $T(60^\circ) \approx$ __________ s

2. Kolikšen je pričakovani relativni odstop $\frac{T - T_0}{T_0}$ v odstotkih pri $\theta_0 = 60^\circ$? __________ %

---

## 3. Laboratorijske naloge na računalniku (Python)

Vse naloge v tem razdelku rešite v programskem jeziku **Python**.

> **Programsko okolje in začetne predloge**
>
> Začetni Jupyter zvezek za to vajo se nahaja v repozitoriju predmeta: `02_vaje/vaje_02.ipynb`
>
> Repozitorij klonirajte ali zvezek prenesite na delovno postajo ter vanj dopolnite manjkajoče funkcije v skladu s spodnjimi navodili.

### Naloga 1: Numerična integracija sistema dveh NDE 1. reda (35 min)

Diferencialno enačbo drugega reda pretvorite v sistem dveh diferencialnih enačb prvega reda:

$$
\frac{d\theta}{dt} = \omega_v, \qquad \frac{d\omega_v}{dt} = -\frac{g}{L}\sin\theta.
$$

Uporabite numerični integrator (npr. metodo RK4 ali vgrajeno metodo `scipy.integrate.solve_ivp` z metodo RK45). Ker periodo določamo na več decimalk natančno, nastavite majhno relativno toleranco integratorja (npr. `rtol=1e-10`). Simulirajte prosto nihanje za začetne kote $\theta_0 \in \{10^\circ, 30^\circ, 60^\circ, 90^\circ, 120^\circ, 150^\circ\}$ ob začetni hitrosti $\omega_v(0) = 0$.

### Naloga 2: Določitev periode in primerjava z eliptičnim integralom (30 min)

Iz dobljenih numeričnih časovnih potekov $\theta(t)$ določite dejanski nihajni čas $T_{\text{num}}$ prek detekcije pozitivnih prehodov skozi ničelno lego ali z merjenjem časovnega razmika med sosednjima vrhovoma.

Vrednost primerjajte z natančnim eliptičnim integralom $T_{\text{elip}} = 4\sqrt{L/g}\,K(\sin(\theta_0/2))$ (uporabite `scipy.special.ellipk`).

> [!WARNING]
> Funkcija `ellipk(m)` kot argument sprejme parameter $m = k^2$ in ne modula $k$, zato pravilno kličemo `ellipk(np.sin(theta0/2)**2)`.

Izpolnite spodnjo preglednico.

| $\theta_0$ [°] | $\theta_0$ [rad] | $T_{\text{num}}$ [s] | $T_{\text{elip}}$ [s] | Relativna razlika [%] |
|:-:|:-:|---|---|:-:|
| $10^\circ$  | $0{,}1745$ | | | |
| $30^\circ$  | $0{,}5236$ | | | |
| $60^\circ$  | $1{,}0472$ | | | |
| $90^\circ$  | $1{,}5708$ | | | |
| $120^\circ$ | $2{,}0944$ | | | |
| $150^\circ$ | $2{,}6180$ | | | |

*Preglednica 1: Primerjava numerične periode nihala s točnim eliptičnim integralom.*

### Naloga 3: Simulacija neprisiljenega Duffingovega oscilatorja (25 min)

Simulirajte neprisiljen Duffingov oscilator $\ddot{x} + \omega_0^2 x + \alpha x^3 = 0$ za $\omega_0 = 1{,}0\ \text{s}^{-1}$ pri več začetnih amplitudah $A \in [0{,}2,\ 1{,}8]$:

1. Primer 1: utrjena vzmet ($\alpha = +0{,}5$).
2. Primer 2: mehčana vzmet ($\alpha = -0{,}1$).

Narišite graf odvisnosti frekvence $\omega$ od amplitude $A$ in primerjajte numerične točke z analitičnim približkom perturbacijske metode $\omega(A) \approx \omega_0 \left(1 + \frac{3}{8}\frac{\alpha}{\omega_0^2}A^2\right)$.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Fizikalno ozadje mehčanja nihala**
>
> Zakaj se pri matematičnem nihalu z naraščanjem začetnega kota nihajni čas povečuje ($T \to \infty$, ko $\theta_0 \to \pi$)? Pojasnite to z vidika oblike nelinearnega potenciala $V(\theta) = mgL(1 - \cos\theta)$ v primerjavi s paraboličnim harmonskim potencialom.

> **Razmislek 2: Omejitve perturbacijske metode**
>
> Do katere vrednosti amplitude $A$ je motenjski približek $\omega(A) \approx \omega_0\left(1 + \frac{3}{8}\frac{\alpha}{\omega_0^2}A^2\right)$ še zanesljiv? Kaj se v primeru mehčane vzmeti ($\alpha < 0$) zgodi pri zelo velikih začetnih odmikih $A > \sqrt{\omega_0^2 / |\alpha|}$?

> **Razmislek 3: Razpad načela linearne superpozicije**
>
> Če nihalu seštejemo dve posamezni rešitvi $\theta_1(t) + \theta_2(t)$, zakaj dobljena funkcija ni rešitev nelinearne diferencialne enačbe? Kako se nelinearnost odraža v frekvenčnem spektru gibanja (pojav višjih harmonikov)?

---

**Podpis študenta/ke:** ____________________  **Ocena / Podpis asistenta:** ____________________
