# Laboratorijski delovni list 15
## Nelinearne valovne enačbe in solitoni (Korteweg–de Vriesova enačba)

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Predmet:** Nelinearni dinamični sistemi

> Izvirnik: [navodila/delavni_list_15.pdf](navodila/delavni_list_15.pdf)

---

## 1. Teoretične osnove in motivacija

V linearnih disperzivnih medijih se valovni paketi med potovanjem raztezajo in izgubljajo obliko, saj se različne spektralne komponente širijo z različnimi faznimi hitrostmi. V izrazito nelinearnih medijih brez disperzije pa odvisnost hitrosti od amplitude povzroči strmenje valovne fronte in nastanek udarnega vala.

Korteweg–de Vriesova (KdV) enačba opisuje plitve vodne valove in predstavlja temeljni model za ravnovesje obeh nasprotujočih si mehanizmov:

$$
\frac{\partial u}{\partial t} + 6u \frac{\partial u}{\partial x} + \frac{\partial^3 u}{\partial x^3} = 0.
$$

Nelinearni advekcijski člen $6u \frac{\partial u}{\partial x}$ pospešuje vrh vala in ga ostri, medtem ko linearni disperzijski člen $\frac{\partial^3 u}{\partial x^3}$ val razteza. Natančno dinamično ravnovesje omogoča nastanek **solitona** – lokaliziranega samotnega vala, ki potuje s stalno obliko in hitrostjo:

$$
u(x, t) = 2 \mathrm{sech}^2(x - 4t).
$$

Hitrost solitona je premo sorazmerna z njegovo amplitudo ($c = 2A$), kar pomeni, da večji solitoni potujejo hitreje od manjših. Solitoni se ob medsebojnih trkih obnašajo kot kvazidelci: po interakciji ohranijo svojo obliko in amplitudo, pri čemer utrpijo le fazni zamik.

---

## 2. Pripravljalna naloga (analitični del)

1.  Za linearno disperzivno enačbo $\frac{\partial u}{\partial t} + \frac{\partial^3 u}{\partial x^3} = 0$ poiščite disperzijsko relacijo $\omega(k)$ z vstavljanjem harmonskega nastavka $u(x,t) = A e^{i(kx - \omega t)}$ ter izračunajte fazno in grupno hitrost.

2.  Pokažite z odvajanjem, da je funkcija $u(x,t) = 2 \mathrm{sech}^2(x - 4t)$ natančna analitična rešitev KdV enačbe.

---

## 3. Laboratorijske naloge na računalniku

> **Programsko okolje in začetna predloga**
>
> Jupyter zvezek za to vajo se nahaja v repozitoriju pod `15_vaje/vaje_15.ipynb`.

### Naloga 1: Dekompozicija učinkov – Disperzija proti nelinearnosti (35 min)

Kot začetni pogoj vzemite profil $u(x, 0) = 2 \mathrm{sech}^2(x)$ na periodičnem območju $x \in [-20, 20]$.

1.  **Samo disperzija ($u_t + u_{xxx} = 0$):** Simulirajte razpad pulza in opazujte oscilatorni disperzijski rep na levi strani.

2.  **Samo nelinearnost ($u_t + 6u u_x = 0$):** Opazujte strmenje desne fronte proti prevoju (nelinearni udarni val).

3.  **Polna KdV enačba:** Potrdite stabilno širjenje solitona brez spremembe oblike s hitrostjo $c = 4$.

### Naloga 2: Trk dveh solitonov različnih amplitud (40 min)

Nastavite začetni pogoj z dvema ločenima solitonoma: večjim (hitrejšim) na levi in manjšim (počasnejšim) na desni:

$$
u(x, 0) = 2 \cdot 4 \mathrm{sech}^2\left(\sqrt{4}(x + 8)\right) + 2 \cdot 1 \mathrm{sech}^2\left(\sqrt{1}(x - 2)\right).
$$

1.  Simulirajte časovni razvoj skozi trk.

2.  Narišite prostorsko-časovni diagram $u(x, t)$ (*waterfall plot* ali barvno karto `imshow`).

3.  Pokažite, da oba vala po trku v celoti ohranita svojo prvotno amplitudo in obliko ter izmerite fazni poskok (položajni zamik).

### Naloga 3: Ohranitveni zakoni KdV enačbe (15 min)

Numerično preverite ohranjanje mase $I_1 = \int u \, dx$ in energije $I_2 = \int u^2 \, dx$ med celotnim potekom simulacije.

---

## 4. Vprašanja za razpravo in zaključni zagovor

> **Razmislek 1: Kvazidelčni značaj solitonov**
>
> Zakaj solitonov ne moremo obravnavati kot običajno valovanje, temveč jih v fiziki pogosto obravnavamo kot »delce«? Kako se ta lastnost kaže pri medsebojnih trkih?

> **Razmislek 2: Solitoni v optičnih vlaknih in komunikacijah**
>
> Kako se koncept solitonov izkorišča v nelinearni optiki (npr. pri širjenju ultrakratkih laserskih svetlobnih impulzov v optičnih vlaknih po nelinearni Schrödingerjevi enačbi NLSE)?
