# Laboratorijski delovni list 11
## Analiza sistemov s prenosnimi funkcijami in frekvenčni odziv

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_11.pdf](navodila/delavni_list_11.pdf)

---

## 1. Teoretične osnove in motivacija

Z uporabo Laplaceove transformacije pri ničelnih začetnih pogojih linearno diferencialno enačbo pretvorimo v algebrsko razmerje v kompleksni frekvenčni domeni $s = \sigma + j\omega$. Prenosna funkcija $F(s) = \frac{Y(s)}{X(s)}$ povezuje Laplaceovo transformacijo izhodnega in vhodnega signala ter v celoti določa lastnosti sistema.

Za analizo ustaljenega harmonskega odziva nadomestimo kompleksno spremenljivko $s \to j\omega$. Frekvenčni odziv podata dve ključni količini:

- **Amplitudno ojačenje v decibelih:** $A_{\text{dB}}(\omega) = 20 \log_{10} |F(j\omega)|$.

- **Fazni zamik v stopinjah:** $\phi(\omega) = \arg(F(j\omega))$.

Za sistem drugega reda z lastno frekvenco $\omega_0 = 1/T$ in relativnim dušenjem $\zeta$ je normirana prenosna funkcija:

$$
F(s) = \frac{K}{T^2 s^2 + 2\zeta T s + 1}.
$$

Kadar je $\zeta < 1/\sqrt{2} \approx 0{,}707$, se v amplitudnem spektru pojavi izrazit **resonančni vrh** pri frekvenci $\omega_r = \omega_0 \sqrt{1 - 2\zeta^2}$.

---

## 2. Pripravljalna naloga (analitični del)

1.  Izračunajte teoretično višino resonančnega vrha $|F(j\omega_r)|$ v decibelih za sistem z ojačenjem $K = 1$ in dušenjem $\zeta = 0{,}2$.

2.  Kakšen je fazni zamik $\phi(\omega)$ sistema drugega reda točno pri frekvenci $\omega = \omega_0$?

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `11_vaje/vaje_11.ipynb`.

### Naloga 1: Izris Bodejevega diagrama za člen 1. reda (30 min)

Za nizkoprepustni RC filter s prenosno funkcijo $F(s) = \frac{1}{1 + sT}$ ($T = 0{,}01\ \text{s}$):

1.  Izračunajte frekvenčni odziv na logaritemski mreži frekvenc $\omega \in [10^0, 10^4]\ \text{rad/s}$.

2.  Narišite Bodejev diagram (amplituda v dB in faza v stopinjah) ter preverite prelomno frekvenco $\omega_c = 1/T$, kjer amplituda upade za $-3\ \text{dB}$ in faza znaša $-45^\circ$.

### Naloga 2: Parametrična analiza člena 2. reda (35 min)

Za sistem drugega reda z $\omega_0 = 10\ \text{rad/s}$ in $K=1$ preučite vpliv dušenja:

1.  Na skupnem Bodejevem diagramu izrišite krivulje za $\zeta \in \{0{,}1, \, 0{,}3, \, 0{,}707, \, 1{,}0, \, 1{,}5\}$.

2.  Izmerite položaj in višino resonančnih vrhov ter potrdite, da pri $\zeta \ge 0{,}707$ resonančni vrh popolnoma izgine.

### Naloga 3: Odziv na stopničasti vhod v časovni domeni (25 min)

S knjižnico `scipy.signal.step` simulirajte časovni odziv $y(t)$ na enotsko stopnico ter primerjajte prenihaj v času z višino resonančnega vrha v frekvenčnem prostoru.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Povezava med poli v s-ravnini in frekvenčnim odzivom**
>
> Kje v kompleksni ravnini $s$ ležijo poli sistema drugega reda pri $\zeta < 1$? Kako njihova oddaljenost od imaginarne osi $j\omega$ določa višino resonančnega vrha?

> **Razmislek 2: Asimptotski nakloni Bodejevega diagrama**
>
> Zakaj je asimptotski padec amplitude pri visokih frekvencah za sistem prvega reda enak $-20\ \text{dB/dekado}$, za sistem drugega reda pa $-40\ \text{dB/dekado}$?
