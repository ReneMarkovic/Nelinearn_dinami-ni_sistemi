# Laboratorijski delovni list 14
## Nelinearne parcialne diferencialne enačbe: Prevajanje toplote s temperaturno odvisno prevodnostjo

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_14.pdf](navodila/delavni_list_14.pdf)

---

## 1. Teoretične osnove in motivacija

Pri obravnavi prenosa toplote v realnih materialih ob večjih temperaturnih razlikah toplotna prevodnost ni več konstantna, temveč postane funkcija temperature $k = k(T)$. Enodimenzionalno toplotno prevajanje vzdolž homogene palice opisuje nelinearna difuzijska enačba:

$$
\rho c \frac{\partial T}{\partial t} = \frac{\partial}{\partial x} \left( k(T) \frac{\partial T}{\partial x} \right) = k(T) \frac{\partial^2 T}{\partial x^2} + \frac{dk}{dT} \left( \frac{\partial T}{\partial x} \right)^2.
$$

Zaradi člena z kvadratom gradienta temperature $(\partial T / \partial x)^2$ enačba ni več linearna, kar poruši veljavnost načela superpozicije.

Predpostavimo linearno temperaturno odvisnost toplotne prevodnosti:

$$
k(T) = k_0 \left[ 1 + \beta (T - T_0) \right].
$$

Za stacionarno stanje ($\partial T / \partial t = 0$) z robnima pogojema $T(0) = T_1$ in $T(L) = T_2$ (kjer je $\Delta T = T_1 - T_2$ in referenčna temperatura $T_0 = T_2$) obstaja analitična rešitev:

$$
T(x) = T_0 + \frac{\sqrt{1 + \left(2\beta \Delta T + \beta^2 \Delta T^2\right) \left(1 - \frac{x}{L}\right)} - 1}{\beta}.
$$

---

## 2. Pripravljalna naloga (analitični del)

1.  Pokažite, da v limiti $\beta \to 0$ (konstantna prevodnost $k_0$) analitični temperaturni profil preide v klasično linearno porazdelitev $T(x) = T_1 - \frac{x}{L}\Delta T$.

2.  Kakšna je ukrivljenost stacionarnega temperaturnega profila ($\partial^2 T / \partial x^2$), če toplotna prevodnost s temperaturo narašča ($\beta > 0$)?

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `14_vaje/vaje_14.ipynb`.

### Naloga 1: Diskretizacija s končnimi diferencami (35 min)

Palico dolžine $L = 0{,}2\ \text{m}$ razdelite na $N = 200$ prostorskih intervalov s korakom $\Delta x = L/N$.

1.  Prostorski odvod diskretizirajte z metodo vmesnih točk:

    ```math
    \frac{dT_i}{dt} = \frac{k_{i+1/2}(T_{i+1} - T_i) - k_{i-1/2}(T_i - T_{i-1})}{\rho c \, \Delta x^2}, \quad k_{i+1/2} = k\left(\frac{T_i + T_{i+1}}{2}\right).
    ```

2.  Uporabite parametre bakrene palice z $\alpha_0 = k_0/(\rho c) = 8{,}23 \times 10^{-5}\ \text{m}^2/\text{s}$, $\beta = 0{,}005\ \text{K}^{-1}$ ter robnima pogojema $T(0, t) = 200^\circ\text{C}$ in $T(L, t) = 20^\circ\text{C}$.

### Naloga 2: Časovni razvoj in primerjava z analitično rešitvijo (35 min)

1.  Začnite s homogenim začetnim profilom $T(x, 0) = 20^\circ\text{C}$.

2.  Integrirajte časovni razvoj do vzpostavitve stacionarnega stanja ($t_{\text{end}} \approx 600\ \text{s}$; pri $120\ \text{s}$ profil od stacionarnega odstopa še za nekaj kelvinov).

3.  Na istem grafu primerjajte numerični profil $T_{\text{num}}(x)$, analitični nelinearni profil ter linearni profil ($\beta = 0$).

### Naloga 3: Numerična stabilnost in von Neumannov kriterij (20 min)

Preizkusite časovni korak $\Delta t$. Poiščite kritični korak $\Delta t_c \approx \frac{\Delta x^2}{2 \alpha_{\text{max}}}$, nad katerim eksplicitna diferenčna shema postane numerično nestabilna.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Fizikalni pomen člena $(\partial T / \partial x)^2$**
>
> Kakšno fizikalno vlogo igra nelinearni gradientni člen $\frac{1}{\rho c}\frac{dk}{dT}(\nabla T)^2$ pri akumulaciji ali odtekanju toplotne energije v palici?

> **Razmislek 2: Razpad Fourierjeve metode ločitve spremenljivk**
>
> Zakaj nelinearne parcialne diferencialne enačbe ne moremo rešiti s standardno Fourierjevo metodo ločitve spremenljivk $T(x,t) = X(x)\mathcal{T}(t)$ in razvojem po lastnih sinusnih načinih?
