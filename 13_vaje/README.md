# Laboratorijski delovni list 13
## Fermi–Pasta–Ulam–Tsingou (FPU-$\alpha$) eksperiment in rekurenca

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_13.pdf](navodila/delavni_list_13.pdf)

---

## 1. Teoretične osnove in motivacija

Leta 1955 so Fermi, Pasta, Ulam in Mary Tsingou z numeričnim računanjem na računalniku MANIAC preverjali hipotezo o ergodičnosti v nelinearnih kristalnih mrežah. Pričakovali so, da bo poljubno majhna nelinearna sklopitev med delci povzročila hitro in nepovratno ekviparticijo energije med vse nihajne mode sistema (termično ravnovesje).

Obravnavamo verigo $N$ enakih mas, povezanih z nelinearnimi vzmetmi s kvadratnim nelinearnim popravkom (FPU-$\alpha$ model):

$$
\ddot{u}_n = (u_{n+1} - 2u_n + u_{n-1}) + \alpha \left[ (u_{n+1} - u_n)^2 - (u_n - u_{n-1})^2 \right]
$$

za $n = 1, \dots, N$ s fiksnimi robnimi pogoji $u_0 = u_{N+1} = 0$. Za preučevanje porazdelitve energije sistem projiciramo na ortogonalne prostorske Fourierjeve lastne načine (mode) linearne verige:

$$
Q_k(t) = \sqrt{\frac{2}{N+1}} \sum_{n=1}^N u_n(t) \sin\left( \frac{n k \pi}{N+1} \right), \quad \omega_k = 2 \sin\left( \frac{k \pi}{2(N+1)} \right).
$$

Energija posameznega načina nihanja znaša $E_k(t) = \frac{1}{2}(\dot{Q}_k^2 + \omega_k^2 Q_k^2)$. Namesto enakomerne porazdelitve energije so avtorji odkrili presenetljiv pojav: energija se po prehodu skozi nekaj nižjih modov skoraj v celoti vrne v prvotno vzbujeni mod (**FPU rekurenca**).

---

## 2. Pripravljalna naloga (analitični del)

1.  Pojasnite pomen simplektičnega integratorja (Verletov algoritem): zakaj navadna Eulerjeva ali celo standardna RK4 integracija pri dolgotrajnih simulacijah hamiltonskih mrež povzroči umeten numerični drift energije?

2.  Narišite prostorsko obliko prvega lastnega načina nihanja $u_n(0) \propto \sin(\frac{n \pi}{N+1})$ za verigo $N=15$ delcev.

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `13_vaje/vaje_13.ipynb`.

### Naloga 1: Implementacija Verletovega integracijskega algoritma (35 min)

Implementirajte algoritem hitrostnega Verleta (*Velocity Verlet*) za verigo $N=15$ mas z nelinearnostjo $\alpha = 0{,}5$ in časovnim korakom $\Delta t = 0{,}02$. Preverite ohranjanje skupne energije sistema $E_{\text{tot}}(t)$ do časa $t_{\text{max}} = 8000$.

### Naloga 2: Spremljanje modalnih energij $E_k(t)$ in prikaz rekurence (40 min)

1.  Sistem vzbudite izključno v prvem modu ($k=1$) z začetno amplitudo $A = 0{,}12$.

2.  V vsakem časovnem koraku izračunajte deleže energij $E_k(t)/E_{\text{tot}}$ za prvih pet modov ($k \in \{1, 2, 3, 4, 5\}$).

3.  Narišite časovni potek energijskih deležev in določite periodični rekurenčni čas $T_{\text{rec}}$, ko se v mod 1 povrne več kot $95\,\%$ celotne energije.

### Naloga 3: Prehod v ergodičnost pri velikih energijah (15 min)

Povečajte začetno amplitudo na $A = 3{,}0$ in podaljšajte simulacijo na $t_{\text{max}} = 40\,000$. Opazujte razpad FPU rekurence in prehod v kaotično termalizacijo (ekviparticijo energije med vse načine).

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Povezava med FPU eksperimentom in solitoni v KdV enačbi**
>
> Zabosky in Kruskal sta leta 1965 pokazala, da zvezni limitni model FPU verige vodi neposredno do KdV enačbe. Kako solitoni v KdV enačbi pojasnjujejo ohranjanje reda in obstoj rekurenčnega časa?

> **Razmislek 2: KAM izrek**
>
> Kako Kolmogorv–Arnold–Moserjev (KAM) izrek razloži obstoj quasiperiodičnega gibanja v šibko motenih hamiltonskih sistemih in zakaj nelinearnost ne zagotavlja takojšnje ergodičnosti?
