# Laboratorijski delovni list 3
## Linearizacija in analiza stabilnosti ravnotežij v 2D sistemih

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko

> [!IMPORTANT]
> **Programsko okolje: Python**
>
> Vse računalniške naloge te vaje se izvajajo **izključno v programskem jeziku Python** (priporočena različica 3.10 ali novejša). Uporabljamo knjižnice `numpy` (`linalg.eig`), `scipy` (`solve_ivp`), `sympy` (simbolno računanje) in `matplotlib` (`streamplot`, `quiver`). Uporaba drugih programskih jezikov ali okolij (npr. MATLAB, Octave, Mathematica) ni predvidena. Rešitev oddajte kot Jupyter zvezek (`.ipynb`).

---

## 1. Teoretične osnove in motivacija

Pri proučevanju večdimenzionalnih dinamičnih sistemov nas primarno zanima obnašanje v okolici ravnotežnih (stacionarnih) točk $\mathbf{x}^{\ast}$, kjer velja $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}^{\ast}) = \mathbf{0}$. Z razvojem v Taylorjevo vrsto do prvega reda dinamiko v bližini ravnotežja opišemo z lineariziranim sistemom

$$
\dot{\mathbf{u}} = \mathbf{J}(\mathbf{x}^{\ast})\,\mathbf{u}, \quad \text{kjer je } \mathbf{u} = \mathbf{x} - \mathbf{x}^{\ast}
$$

in $\mathbf{J}$ Jacobijeva matrika delnih odvodov. Za splošni avtonomni 2D sistem z matriko $\mathbf{A}$

$$
\begin{bmatrix} \dot{x} \\ \dot{y} \end{bmatrix} = \mathbf{A} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
$$

lastne vrednosti $\lambda$ določimo iz karakterističnega polinoma:

$$
\det(\mathbf{A} - \lambda \mathbf{I}) = \lambda^2 - \tau \lambda + \Delta = 0 \implies \lambda_{1,2} = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2},
$$

pri čemer sta $\tau = \mathrm{Tr}(\mathbf{A}) = a + d$ (sled matrike) in $\Delta = \det(\mathbf{A}) = ad - bc$ (determinanta matrike).

### 1.1 Klasifikacija stacionarnih stanj v ravnini $(\tau, \Delta)$

Vrsto ravnotežja in topologijo faznega portreta enolično določata predznaka $\tau$ in $\Delta$ ter diskriminanta $D = \tau^2 - 4\Delta$:

- **Sedlo (vedno nestabilno):** $\Delta < 0$. Lastni vrednosti sta realni in nasprotnih predznakov ($\lambda_1 > 0 > \lambda_2$). Trajektorije se vzdolž smeri stabilnega lastnega vektorja približujejo, vzdolž nestabilnega pa oddaljujejo.
- **Vozel:** $\Delta > 0$ in $\tau^2 - 4\Delta > 0$. Lastni vrednosti sta realni in enakega predznaka. Če je $\tau < 0$, je vozel **stabilen** ($\lambda_{1,2} < 0$); če je $\tau > 0$, je **nestabilen** ($\lambda_{1,2} > 0$).
- **Gorišče (spirala):** $\Delta > 0$ in $\tau^2 - 4\Delta < 0$. Lastni vrednosti sta konjugirano kompleksni: $\lambda_{1,2} = \frac{\tau}{2} \pm i\omega$. Če je $\tau < 0$, imamo **stabilno gorišče** (spiralno krčenje); če je $\tau > 0$, je gorišče **nestabilno** (spiralno širjenje).
- **Center (nevtralno stabilno):** $\Delta > 0$ in $\tau = 0$. Lastni vrednosti sta čisto imaginarni ($\lambda_{1,2} = \pm i\sqrt{\Delta}$). Fazne trajektorije tvorijo zaprte eliptične orbite.

Sled matrike določa tudi divergenco faznega toka: $\mathrm{div}(\dot{\mathbf{x}}) = \frac{\partial \dot{x}}{\partial x} + \frac{\partial \dot{y}}{\partial y} = a + d = \tau$. Kadar je $\tau < 0$, se fazni volumen disipativno krči.

---

## 2. Pripravljalna naloga (analitični del)

Obravnavamo linearni 2D sistem iz učbenika:

$$
\dot{x} = x + y, \qquad \dot{y} = 4x - 2y.
$$

1. Zapišite matriko sistema $\mathbf{A}$ ter izračunajte sled $\tau$ in determinanto $\Delta$:

   $\mathbf{A} =$ __________  $\tau = \mathrm{Tr}(\mathbf{A}) =$ __________  $\Delta = \det(\mathbf{A}) =$ __________

2. Poiščite lastni vrednosti $\lambda_1, \lambda_2$ in pripadajoča lastna vektorja $\mathbf{v}_1, \mathbf{v}_2$:

   $\lambda_1 =$ ______, $\mathbf{v}_1 =$ ______ | $\lambda_2 =$ ______, $\mathbf{v}_2 =$ ______

3. Določite tip ravnotežja v izhodišču $(0,0)$: ____________________
4. Zapišite analitično rešitev $(x(t), y(t))$ za začetni pogoj $(x(0), y(0)) = (2, -3)$:

   $x(t) =$ ____________________  $y(t) =$ ____________________

---

## 3. Laboratorijske naloge na računalniku (Python)

Vse naloge v tem razdelku rešite v programskem jeziku **Python**.

> **Programsko okolje in začetna predloga**
>
> Začetni Jupyter zvezek se nahaja v repozitoriju predmeta pod: `03_vaje/vaje_03.ipynb`
>
> Zvezek odprite v svojem razvojnem okolju in dopolnite manjkajoče funkcije.

### Naloga 1: Numerični izračun lastnih vrednosti in lastnih smeri (25 min)

S knjižnico NumPy (uporabite funkcijo `numpy.linalg.eig`) izračunajte lastne vrednosti in normalizirane lastne vektorje za matriko $\mathbf{A}$. Preverite ujemanje z analitičnimi rezultati iz pripravljalnega dela.

### Naloga 2: Izris vektorskega polja in invariantnih premic sedla (35 min)

1. Na območju $(x, y) \in [-3, 3] \times [-3, 3]$ s funkcijo `matplotlib.pyplot.streamplot` ali `quiver` izrišite vektorsko polje $(\dot{x}, \dot{y})$.
2. Vrišite obe **invariantni smeri** (premici vzdolž lastnih vektorjev $\mathbf{v}_1$ in $\mathbf{v}_2$), ki predstavljata separatrisi stabilne in nestabilne smeri sedla.
3. Z integratorjem (npr. `scipy.integrate.solve_ivp`) izračunajte in vrišite trajektorije za vsaj 6 različnih začetnih točk. Posebej označite trajektorijo z začetnim pogojem $(x_0, y_0) = (2, -3)$.

### Naloga 3: Eksploracija topologij fazne ravnine (30 min)

Spremenite parametre matrike $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$ tako, da realizirate še preostale osnovne topologije stacionarnih točk. Za vsak primer izračunajte $\tau, \Delta$ ter izrišite fazni portret.

| Tip ravnotežja | Izbira matrike $\mathbf{A}$ | $\tau$ | $\Delta$ | Komentar dinamike |
|---|:-:|:-:|:-:|---|
| **Sedlo** | $\begin{bmatrix} 1 & 1 \\ 4 & -2 \end{bmatrix}$ | $-1$ | $-6$ | Nestabilno, eksponentni pobeg vzdolž $\mathbf{v}_1$. |
| **Stabilni vozel** | | | | Dve realni negativni lastni vrednosti. |
| **Stabilno gorišče** | | | | Kompleksni lastni vrednosti z $\mathrm{Re}(\lambda) < 0$. |
| **Center** | | | | Čisto imaginarni lastni vrednosti ($\tau = 0, \Delta > 0$). |

*Preglednica 1: Pregled osnovnih konfiguracij faznih ravnin.*

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Geometrijski pomen lastnih vektorjev**
>
> Kakšen je fizikalni pomen lastnih smeri pri sedelni točki? Kaj se zgodi s trajektorijo, katere začetni pogoj leži točno na smeri lastnega vektorja $\mathbf{v}_2$ z negativno lastno vrednostjo? Ali v praksi numerična integracija na tej premici zdrži poljubno dolgo?

> **Razmislek 2: Disipacija in krčenje volumna**
>
> Povežite sled matrike $\tau = a+d$ z divergenco faznega prostora $\mathrm{div}(\dot{\mathbf{x}})$. Zakaj je za ohranitvene (hamiltonske) mehanske sisteme vedno $\tau = 0$? Kaj to pomeni za vrsto stacionarne točke pri nedušenem linearnem oscilatorju?

> **Razmislek 3: Robustnost centra v nelinearnih sistemih**
>
> Center nastopi pri pogoju $\tau = 0$ in $\Delta > 0$. Če linearnemu sistemu s centrom dodamo poljubno majhne nelinearne člene višjega reda (npr. $\dot{x} = y + \epsilon x^3$, $\dot{y} = -x$), ali center nujno preživi ali pa preide v stabilno/nestabilno gorišče? Utemeljite.

---

**Podpis študenta/ke:** ____________________  **Ocena / Podpis asistenta:** ____________________
