# Laboratorijski delovni list 6
## Vsiljeni Duffingov oscilator: Resonanca, histereza in skoki amplitude

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_06.pdf](navodila/delavni_list_06.pdf)

---

## 1. Teoretične osnove in motivacija

Vsiljeno nihanje dušenega nelinearnega oscilatorja z nelinearno prožnostjo opisuje Duffingova enačba:

$$
\ddot{x} + \delta \dot{x} + \omega_0^2 x + \beta x^3 = F_0 \cos(\omega t),
$$

kjer je $\delta$ koeficient viskoznega dušenja, $\omega_0$ linearna lastna frekvenca, $\beta$ koeficient kubične nelinearnosti ter $F_0$ in $\omega$ amplituda ter kotna frekvenca periodičnega vzbujanja.

Zaradi odvisnosti lastne frekvence od amplitude nihanja pride pri nelinearnih oscilatorjih do deformacije resonančne krivulje. Vrh resonance se pri utrjeni vzmeti ($\beta > 0$) nagne v smeri višjih frekvenc (»desno«), pri mehčani vzmeti ($\beta < 0$) pa v smeri nižjih frekvenc. Pri dovolj močnem vzbujanju $F_0$ postane krivulja večvrednostna: pri določenih frekvencah obstajata dve stabilni periodični rešitvi (bistabilnost). Ob počasnem zveznem spreminjanju vsiljene frekvence $\omega$ opazimo pojav **resonančnega preskoka** (*jump phenomenon*) in **histerezo amplitude**.

---

## 2. Pripravljalna naloga (analitični del)

Privzemimo harmonsko rešitev prvega reda $x(t) \approx A \cos(\omega t - \phi)$.

1.  Uporabite identiteto $\cos^3(\alpha) = \frac{3}{4}\cos(\alpha) + \frac{1}{4}\cos(3\alpha)$ in pojasnite, zakaj kubični člen pripelje do efektivne lastne frekvence $\omega_{\text{eff}}^2(A) = \omega_0^2 + \frac{3}{4}\beta A^2$.

2.  Za sistem brez dušenja ($\delta = 0$) zapišite nelinearno algebrajsko enačbo, ki povezuje amplitudo $A$, frekvenco $\omega$ ter amplitudo vzbujanja $F_0$:

    ```math
    \left( \omega_0^2 - \omega^2 + \frac{3}{4}\beta A^2 \right) A = \_\_\_\_\_
    ```

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `06_vaje/vaje_06.ipynb`.

### Naloga 1: Časovni odziv in prehod v ustaljeno stanje (30 min)

Simulirajte Duffingov sistem za parametre $\omega_0 = 1{,}0$, $\beta = 0{,}2$, $\delta = 0{,}1$ in $F_0 = 0{,}3$.

1.  Za frekvenco vzbujanja $\omega = 1{,}2$ integrirajte sistem dovolj dolgo ($t \in [0, 200]$), da zamre prehodni pojav.

2.  Narišite časovni odziv $x(t)$ in fazni portret $(x, \dot{x})$ za zadnjih 10 period vzbujanja.

### Naloga 2: Frekvenčni prelet in demonstracija histereze (40 min)

Izvedite simulacijo frekvenčnega preleta v dveh smereh skozi območje $\omega \in [0{,}6, \, 1{,}8]$:

1.  **Prelet navzgor ($\omega \uparrow$):** Frekvenco postopoma večajte; končno stanje pri frekvenci $\omega_k$ uporabite kot začetni pogoj za naslednjo frekvenco $\omega_{k+1}$.

2.  **Prelet navzdol ($\omega \downarrow$):** Frekvenco postopoma manjšajte od $1{,}8$ nazaj proti $0{,}6$.

3.  Izrišite ustaljeno amplitudo $A(\omega)$ za obe smeri ter označite točki preskoka amplitude in histerezno zanko.

### Naloga 3: Primerjava z linearnim oscilatorjem (20 min)

Ponovite simulacijo za linearni oscilator ($\beta = 0$) z enakim dušenjem in vzbujanjem ter primerjajte simetrijo resonančne krivulje.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Fizikalni izvor preskoka amplitude**
>
> Zakaj sistem med frekvenčnim preletom ne ostane na srednji veji resonančne krivulje? Pojasnite stabilnost srednje veje prek linearizacije okoli periodične orbite.

> **Razmislek 2: Vpliv dušenja $\delta$**
>
> Kaj se zgodi z večvrednostnim območjem in histerezo, če koeficient dušenja $\delta$ močno povečamo? Ali histereza obstaja pri poljubno velikem dušenju?
