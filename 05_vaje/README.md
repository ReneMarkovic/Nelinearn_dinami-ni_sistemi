# Laboratorijski delovni list 5
## Enorazsežne bifurkacije v dinamičnih sistemih

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_05.pdf](navodila/delavni_list_05.pdf)

---

## 1. Teoretične osnove in motivacija

Bifurkacija predstavlja kvalitativno spremembo v topologiji toka oziroma obnašanju dinamičnega sistema ob zveznem spreminjanju nadzornega (bifurkacijskega) parametra $r$. Pri kritični vrednosti $r_c$ se lahko število stacionarnih stanj spremeni, obstoječa stanja lahko zamenjajo svojo stabilnost ali pa se rodijo povsem nove oblike dinamike.

V enorazsežnih sistemih $\dot{x} = f(x, r)$ lokalno stabilnost stacionarnega stanja $x^{\ast}$ ($f(x^{\ast}, r) = 0$) določa prvi odvod:

$$
\lambda = \left.\frac{\partial f(x, r)}{\partial x}\right|_{x=x^{\ast}}.
$$

Če je $\lambda < 0$, je stanje **stabilno** (motnje eksponentno zamrejo); če je $\lambda > 0$, je stanje **nestabilno**. Pogoj za nastanek bifurkacije je izguba hiperboličnosti: $\lambda = 0$ pri $r = r_c$.

### 1.1 Tipične enorazsežne bifurkacije in njihove normalne forme

1.  **Sedelno-vozelna bifurkacija** (*Saddle-node bifurcation*):  
    Predstavlja mehanizem nastanka ali izginotja parov ravnotežij. Normalna forma je:

    ```math
    \dot{x} = r - x^2.
    ```

    Za $r < 0$ sistem nima realnih stacionarnih stanj. Pri $r_c = 0$ se pojavi polstabilna točka $x^{\ast} = 0$, za $r > 0$ pa nastaneta dve ravnotežji: stabilno $x_1^{\ast} = +\sqrt{r}$ in nestabilno $x_2^{\ast} = -\sqrt{r}$.

2.  **Transkritična bifurkacija** (*Transcritical bifurcation*):  
    Značilna je za sisteme, kjer ravnotežna točka vedno obstaja za vse vrednosti parametra, pri prehodu skozi kritično točko pa pride do **izmenjave stabilnosti**. Normalna forma je:

    ```math
    \dot{x} = rx - x^2 = x(r - x).
    ```

    Stacionarni stanji sta $x_1^{\ast} = 0$ in $x_2^{\ast} = r$. Pri $r < 0$ je $x_1^{\ast} = 0$ stabilno in $x_2^{\ast} = r$ nestabilno; pri $r > 0$ se stabilnost zamenja ($x_1^{\ast} = 0$ postane nestabilno, $x_2^{\ast} = r$ stabilno).

3.  **Vilična bifurkacija** (*Pitchfork bifurcation*):  
    Pojavlja se v fizikalnih sistemih z zrcalno simetrijo ($f(-x) = -f(x)$).

    - **Nadkritična vilična bifurkacija:**

      ```math
      \dot{x} = rx - x^3 = x(r - x^2).
      ```

      Za $r \le 0$ obstaja le stabilno stanje $x^{\ast} = 0$. Za $r > 0$ postane $x^{\ast} = 0$ nestabilno, na obeh straneh simetrično pa nastaneta dve novi stabilni veji $x_{1,2}^{\ast} = \pm\sqrt{r}$.

    - **Podkritična vilična bifurkacija:** $\dot{x} = rx + x^3$, kjer stabilno izhodišče pri $r < 0$ obdajata dve nestabilni veji $x^{\ast} = \pm\sqrt{-r}$.

---

## 2. Pripravljalna naloga (analitični del)

Obravnavamo normalno formo transkritične bifurkacije: $\dot{x} = rx - x^2$.

1.  Izračunajte splošni odvod funkcije: $\frac{\partial f(x, r)}{\partial x} =$ \_\_\_\_\_\_\_\_\_\_

2.  Ovrednotite odvod za obe ravnotežji ($x_1^{\ast} = 0$ in $x_2^{\ast} = r$):

    - Za $x_1^{\ast} = 0$: $\lambda_1(r) = \left.\frac{\partial f}{\partial x}\right|_{x=0} =$ \_\_\_\_\_\_\_\_\_\_

    - Za $x_2^{\ast} = r$: $\lambda_2(r) = \left.\frac{\partial f}{\partial x}\right|_{x=r} =$ \_\_\_\_\_\_\_\_\_\_

3.  Določite predznake $\lambda_{1,2}$ in potrdite izmenjavo stabilnosti:

    - Za $r = -1$: $x_1^{\ast} = 0$ je \_\_\_\_\_, $x_2^{\ast} = -1$ je \_\_\_\_\_.

    - Za $r = +1$: $x_1^{\ast} = 0$ je \_\_\_\_\_, $x_2^{\ast} = +1$ je \_\_\_\_\_.

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Začetna koda se nahaja v repozitoriju predmeta pod:
>
> <div class="center">
>
> `05_vaje/vaje_05.ipynb`
>
> </div>
>
> Zvezek klonirajte na delovno postajo in ga dopolnite v skladu z navodili.

### Naloga 1: Izris faznih premic in časovnih odzivov (30 min)

Za transkritično bifurkacijo $\dot{x} = rx - x^2$:

1.  Narišite graf hitrosti $\dot{x}$ v odvisnosti od $x$ za $r = -1{,}0$, $r = 0{,}0$ in $r = +1{,}0$. Na osi $x$ s puščicami označite smer toka ($\dot{x} > 0 \implies \rightarrow$, $\dot{x} < 0 \implies \leftarrow$) ter označite stabilne točke (polni krožci) in nestabilne (prazni krožci).

2.  Za $r = -1{,}0$ in $r = +1{,}0$ numerično simulirajte časovni razvoj $x(t)$ (uporabite `scipy.integrate.solve_ivp`) za več začetnih pogojev $x_0 \in \{-1{,}5, -0{,}5, 0{,}5, 1{,}5\}$. Prikažite konvergenco proti stabilni veji.

### Naloga 2: Konstrukcija bifurkacijskih diagramov (35 min)

Napišite kodo, ki vzdolž parametra $r \in [-2, 2]$ poišče stacionarna stanja in jih izriše na diagramu $(r, x^{\ast})$:

- \*\*Primer A:\*\* Sedelno-vozelna bifurkacija $\dot{x} = r - x^2$.

- \*\*Primer B:\*\* Nadkritična vilična bifurkacija $\dot{x} = rx - x^3$.

Stabilne veje izrišite s \*\*polno črto\*\*, nestabilne veje pa s \*\*črtkano črto\*\*. Označite bifurkacijsko točko $(r_c, x_c)$.

| **Tip bifurkacije** | **Enačba sistema** | **Stacionarna stanja $x^{\ast}(r)$** | **Stabilnostne veje** |
|:---|:--:|:---|:---|
| **Sedelno-vozelna** | $\dot{x} = r - x^2$ | $x^{\ast} = \pm\sqrt{r}$ ($r \ge 0$) | $+\sqrt{r}$ stabilna, $-\sqrt{r}$ nestabilna. |
| **Transkritična** | $\dot{x} = rx - x^2$ | $x_1^{\ast} = 0$, $x_2^{\ast} = r$ | Zamenjava pri $r_c = 0$. |
| **Nadkritična vilična** | $\dot{x} = rx - x^3$ | $x_0^{\ast} = 0$, $x_{1,2}^{\ast} = \pm\sqrt{r}$ ($r \ge 0$) | $0$ izgubi stabilnost, krakoma stabilna. |

*Pregled normalnih form enorazsežnih bifurkacij.*

### Naloga 3: Dinamični prehod skozi bifurkacijo in histerezni zamik (25 min)

Kadar se bifurkacijski parameter spreminja s časom $r(t) = r_0 + \epsilon t$ z majhno hitrostjo $\epsilon = 0{,}02$, sistem ne preklopi v novo stabilno lego točno pri $r_c = 0$, temveč z opaznim dinamičnim zamikom (*bifurcation delay*).

1.  Simulirajte sistem $\dot{x} = r(t)x - x^3$ od $r = -1$ do $r = +2$ ob začetnem pogoju $x(0) = 0{,}01$.

2.  Vrišite dobljeno trajektorijo $x(r(t))$ čez analitični bifurkacijski diagram in opazujte, kje se začne eksponentni pobeg iz veje $x=0$.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Fizikalni pomen zrcalne simetrije**
>
> Zakaj v sistemih z zrcalno simetrijo ($f(-x) = -f(x)$) ne moremo opaziti sedelno-vozelne ali transkritične bifurkacije, temveč se pojavi vilična bifurkacija? Kako na vilično bifurkacijo vpliva majhna asimetrična motnja $\dot{x} = h + rx - x^3$ ($h \neq 0$)?

> **Razmislek 2: Razlika med nadkritično in podkritično bifurkacijo**
>
> Pri nadkritični vilični bifurkaciji $\dot{x} = rx - x^3$ je prehod v novi stabilni legi zvezen in mehak. Kaj pa se zgodi pri podkritični vilični bifurkaciji $\dot{x} = rx + x^3$, ko $r$ preseže $0$? Zakaj tak prehod imenujemo »katastrofičen«?

> **Razmislek 3: Upočasnitev dinamike v bližini bifurkacije**
>
> Kaj se zgodi s hitrostjo relaksacije proti ravnotežju $\dot{x}$, ko se parameter približuje kritični točki $r \to r_c$ (*critical slowing down*)? Pojasnite to z lastno vrednostjo $\lambda = \partial f / \partial x \to 0$.
