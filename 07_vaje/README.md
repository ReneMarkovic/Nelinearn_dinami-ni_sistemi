# Laboratorijski delovni list 7
## Fenomenološko modeliranje histereze (Bouc–Wenov model)

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_07.pdf](navodila/delavni_list_07.pdf)

---

## 1. Teoretične osnove in motivacija

V materialih z nelinearno elastičnostjo in plastičnimi deformacijami povrnjena sila ni odvisna zgolj od trenutnega pomika $x(t)$, temveč tudi od celotne zgodovine obremenjevanja (sistemi s spominom). Bouc–Wenov model predstavlja fenomenološki pristop, ki zgodovino deformacije opiše z dodatno notranjo histerezno spremenljivko $z(t)$:

$$
m\ddot{x} + c\dot{x} + F_s(x, z) = 0,
$$

pri čemer je skupna povrnjena sila sestavljena iz linearnega elastičnega prispevka in histerezne komponente:

$$
F_s(x, z) = k_0 x + \alpha z.
$$

Časovni razvoj histerezne spremenljivke $z$ določa nelinearna diferencialna enačba:

$$
\dot{z} = A v - \beta |v| |z|^{n-1} z - \gamma v |z|^n, \quad \text{kjer je } v = \dot{x}.
$$

Parametri $A$, $\beta$, $\gamma$ in $n$ določajo nagib, debelino in zaobljenost histerezne zanke v ravnini sila–pomik. Ploščina zanke ponazarja energijo, ki se med enim periodičnim ciklom nepovratno disipira v obliki toplote:

$$
W_{\text{dis}} = \oint F_s \, dx = \int_0^T F_s(t) \, v(t) \, dt.
$$

---

## 2. Pripravljalna naloga (analitični del)

1.  Pojasnite pomen parametra $n$ v Bouc–Wenovi enačbi: kakšna je razlika med mehkim prehodom v plastičnost ($n=1$) in ostrim popuščanjem materiala ($n \gg 1$)?

2.  Zakaj zgolj z enačbo oblike $F = F(x, \dot{x})$ (brez notranje spremenljivke $z$) ne moremo opisati histereze pri kvazistatičnem obremenjevanju ($\dot{x} \to 0$)?

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `07_vaje/vaje_07.ipynb`.

### Naloga 1: Histerezna zanka pri vsiljenem kinematičnem gibanju (35 min)

Predpišite harmonsko nihanje lege $x(t) = X_0 \sin(\omega t)$ z amplitudo $X_0 = 1{,}5$ in frekvenco $\omega = 1{,}0$.

1.  Integrirajte enačbo za $z(t)$ pri parametrih $A=1$, $\beta=10$, $\gamma=1$, $n=2$, $k_0=0{,}4$ in $\alpha=0{,}2$.

2.  Izrišite histerezno zanko $F_s(x)$ v ravnini pomik–sila.

3.  Spreminjajte parameter $\beta \in \{1, 5, 20\}$ in opazujte spreminjanje debeline zanke.

### Naloga 2: Prosto nihanje sistema z Bouc–Wenovo histerezo (35 min)

Sistem mase $m=1$ z Bouc–Wenovo histerezno vzmetjo spustite iz začetnega odmika $x_0 = 1{,}5$ ob ničelni začetni hitrosti ($v_0 = 0$) in $z_0 = 0$.

1.  Simulirajte časovni odziv $x(t)$ in $v(t)$ za primer brez viskoznega dušenja ($c = 0$).

2.  Izračunajte skupno mehansko energijo $E(t) = \frac{1}{2}m v^2 + \frac{1}{2}k_0 x^2$ ter preverite, da energija kljub $c=0$ sčasoma upada zaradi histerezne disipacije.

### Naloga 3: Numerični izračun disipirane energije (20 min)

Za ustaljeno histerezno zanko iz Naloge 1 numerično izračunajte ploščino zanke $W_{\text{dis}} = \oint F_s \, dx$ z uporabo trapezne integracije (`numpy.trapz`).

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Kratkotrajno naraščanje elastične energije**
>
> Ali lahko skupna energija $E(t) = \frac{1}{2}mv^2 + \frac{1}{2}k_0 x^2$ v določenem delu cikla začasno naraste? Pojasnite prenos energije med histerezno notranjo spremenljivko $z$ in mehanskim nihanjem.

> **Razmislek 2: Fizikalna uporaba Bouc–Wenovega modela**
>
> Navedite vsaj dva praktična fizikalna ali inženirska sistema, kjer se Bouc–Wenov model uporablja za zaščito konstrukcij (npr. potresni blažilniki, magnetoreološki dušilci).
