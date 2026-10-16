# Nelinearni dinamični sistemi – laboratorijske vaje

**Univerza v Mariboru** · Fakulteta za naravoslovje in matematiko · Oddelek za fiziko  
**Letnik/Smer:** 1. letnik MAG / Fizika

Repozitorij vsebuje gradiva za laboratorijske vaje pri predmetu *Nelinearni dinamični sistemi*. Vsaka vaja ima svojo mapo z:

- `README.md` – navodila (delovni list) v obliki Markdown,
- `navodila/` – izvirni delovni list v PDF obliki,
- `vaje_XX.ipynb` – Jupyter zvezek z začetno predlogo za reševanje.

Vse računalniške naloge se rešujejo v programskem jeziku **Python** (3.10 ali novejši) s knjižnicami `numpy`, `scipy`, `sympy` in `matplotlib`. Vsaka vaja traja 2 šolski uri (90 min) in je samostojno zaključena celota.

## Priprava okolja

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS
python -m pip install -U pip
pip install -r req.txt
```

Podrobnejši opis postavitve virtualnega okolja je v [00_vaje](00_vaje/readme.md).

## Pregled vaj

| Vaja | Tema | Vsebina |
|:--:|---|---|
| [00](00_vaje/readme.md) | Priprava okolja | Virtualno okolje, namestitev knjižnic, preizkus delovanja. |
| [01](01_vaje/README.md) | Nelinearne algebrajske enačbe | Bisekcija, Newton–Raphsonova in sekantna metoda; primerjava hitrosti konvergence. |
| [02](02_vaje/README.md) | Odvisnost frekvence od amplitude | Matematično nihalo pri velikih odklonih (eliptični integral), neprisiljeni Duffingov oscilator. |
| [03](03_vaje/README.md) | Linearizacija in stabilnost 2D sistemov | Lastne vrednosti, klasifikacija ravnotežij v ravnini $(\tau, \Delta)$, fazni portreti. |
| [04](04_vaje/README.md) | Dvojna potencialna jama | Bistabilnost, nivojnice energije, separatrisa, bazeni privlačnosti dušenega sistema. |
| [05](05_vaje/README.md) | Enorazsežne bifurkacije | Sedelno-vozelna, transkritična in vilična bifurkacija; bifurkacijski diagrami, dinamični zamik. |
| [06](06_vaje/README.md) | Vsiljeni Duffingov oscilator | Nelinearna resonanca, frekvenčni prelet, histereza in skoki amplitude. |
| [07](07_vaje/README.md) | Bouc–Wenov model histereze | Histerezne zanke, prosto nihanje s histerezo, disipirana energija. |
| [08](08_vaje/README.md) | Lorenzov sistem | Čudni atraktor, občutljivost na začetne pogoje, dinamika v odvisnosti od $r$. |
| [09](09_vaje/README.md) | Kvantifikacija kaosa | Največji Ljapunovov eksponent, stroboskopski Poincaréjev presek. |
| [10](10_vaje/README.md) | Sinhronizacija oscilatorjev | Sklopljena Van der Polova oscilatorja, kvaziperiodičnost, fazni zaklep. |
| [11](11_vaje/README.md) | Prenosne funkcije | Bodejev diagram za člena 1. in 2. reda, stopničasti odziv. |
| [12](12_vaje/README.md) | Zaprtozančni sistemi | Redukcija blokovnih shem, P- in PI-regulacija, meje stabilnosti. |
| [13](13_vaje/README.md) | FPU eksperiment | Verletova integracija verige FPU-$\alpha$, modalne energije in rekurenca, prehod v ergodičnost. |
| [14](14_vaje/README.md) | Nelinearna toplotna difuzija | Končne diference za prevajanje toplote s $k(T)$, von Neumannova stabilnost. |
| [15](15_vaje/README.md) | KdV solitoni | Disperzija proti nelinearnosti, trk solitonov, ohranitveni zakoni. |
