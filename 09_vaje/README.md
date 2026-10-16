# Laboratorijski delovni list 9
## Kvantifikacija kaosa: Največji Ljapunovov eksponent in Poincaréjevi preseki

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_09.pdf](navodila/delavni_list_09.pdf)

---

## 1. Teoretične osnove in motivacija

Za zanesljivo razlikovanje kaotičnega gibanja od navadnega kvaziperiodičnega nihanja ali šuma moramo kaos kvantitativno ovrednotiti. Temeljno merilo občutljivosti na začetne pogoje predstavlja **največji Ljapunovov eksponent** $\lambda_{\text{max}}$, ki meri povprečno asimptotično stopnjo eksponentne divergence sosednjih tirnic:

$$
\|\delta(t)\| \approx \|\delta_0\| e^{\lambda_{\text{max}} t} \implies \lambda_{\text{max}} = \lim_{t \to \infty} \lim_{\|\delta_0\| \to 0} \frac{1}{t} \ln \left( \frac{\|\delta(t)\|}{\|\delta_0\|} \right).
$$

Pozitiven največji Ljapunovov eksponent ($\lambda_{\text{max}} > 0$) je neizpodbiten dokaz prisotnosti kaosa.

Druga pomembna metoda redukcije večdimenzionalnega toka je **Poincaréjev presek**. Z zveznim vzorčenjem stanja ob vsakem periodičnem preletu vzbujanja $t_k = k \frac{2\pi}{\omega}$ zvezni sistem pretvorimo v diskretno preslikavo. Na preseku se periodično gibanje izrazi kot končno število izoliranih točk, kvaziperiodično kot sklenjena gladka krivulja, kaotični atraktor pa tvori fraktalno strukturo točk.

---

## 2. Pripravljalna naloga (analitični del)

1.  Pojasnite pomen spektra treh Ljapunovovih eksponentov $(\lambda_1, \lambda_2, \lambda_3)$ za avtonomni 3D disipativni sistem:

    - Stabilna fiksna točka: $(-, -, -)$

    - Stabilen limitni cikel: $(0, -, -)$

    - Čudni kaotični atraktor: $(+, 0, -)$, pri čemer velja $\lambda_1 + \lambda_2 + \lambda_3 < 0$.

2.  Zakaj mora za vsak zvezni limitni cikel ali kaotični atraktor vsaj en Ljapunovov eksponent znašati natanko $0$?

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `09_vaje/vaje_09.ipynb`.

### Naloga 1: Numerična ocena $\lambda_{\text{max}}$ za Lorenzov sistem (40 min)

Uporabite dve sosednji trajektoriji Lorenzovega sistema z začetnim odmikom $d_0 = 10^{-8}$.

1.  Spremljajte evklidsko razdaljo $d(t) = \|\mathbf{x}_1(t) - \mathbf{x}_2(t)\|$ v času.

2.  Narišite graf $\ln(d(t))$ v odvisnosti od časa za območje pred nasičenjem atraktorja ($t \in [0, 15]$).

3.  Z linearno regresijo ocenite naklon premice in primerjajte rezultat s teoretično vrednostjo za Lorenzov sistem ($\lambda_{\text{max}} \approx 0{,}905$).

### Naloga 2: Stroboskopski Poincaréjev presek Duffingovega oscilatorja (40 min)

Za kaotični Duffingov oscilator (Uedov oscilator) $\ddot{x} + 0{,}05 \dot{x} + x^3 = 7{,}5 \cos(t)$:

1.  Integrirajte sistem skozi $N_{\text{ciklov}} = 2000$ period vzbujanja $T = 2\pi$.

2.  Izpustite prvih 200 prehodnih ciklov, nato pa zabeležite točke $(x(t_k), \dot{x}(t_k))$ ob časih $t_k = 2\pi k$.

3.  Narišite točkovni diagram Poincaréjevega preseka in opazujte fraktalno plastenje kaotičnega atraktorja.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Nasičenje razdalje med trajektorijama**
>
> Zakaj funkcija $\ln(d(t))$ po določenem času preneha linearno naraščati in se ustali pri konstantni vrednosti? Kaj to pove o omejenosti čudnega atraktorja v faznem prostoru?

> **Razmislek 2: Razlika med kaosom in kvaziperiodičnostjo na Poincaréjevem preseku**
>
> Kako na Poincaréjevem preseku zanesljivo ločimo kvaziperiodično gibanje (npr. vsoto dveh sinusnih signalov z iracionalnim razmerjem frekvenc) od determinističnega kaosa?
