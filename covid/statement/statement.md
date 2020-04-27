**Difficoltà: _2_**

## Descrizione del problema

Giuseppe e Irene sono molto preoccupati per la pandemia da COVID-19, e vogliono mettere a frutto le loro competenze accademiche di data scientist per costruire un'app che possa essere utile a diminuire il contagio. L'app che hanno in mente permette di monitorare
il numero di casi positivi rilevati in vari luoghi fornendo una serie di informazioni utili, tra cui una stima della probabilità di contagio di una persona a seconda che viva più o meno vicino ad un alto numero di persone già infette. 

Scaricando dati dalla rete, Giuseppe e Irene si procurano innanzitutto una mappa dei contagi, oltre ad altre informazioni sulla residenza delle persone da monitorare. Hanno quindi a disposizione i seguenti dati: 

- $N$ = numero di persone da monitorare
- $N$ coppie $(X_i,Y_i)$, con $1\leq i \leq N$, che rappresentano il luogo in cui risiede ciascuna delle $N$ persone 
- $Z$ = numero di punti geografici per cui si dispone di una stima del numero di casi positivi rilevati in quel luogo 
- La mappa dei contagi, ovvero $Z$ triple $(X_j,Y_j,P_j)$, con $1\leq j \leq Z$, che rappresentano una coordinata geografica $(X_j,Y_j)$ e il numero $P_j$ di casi positivi rilevati in quel luogo 
- Una distanza $D \gt 0$ 

![Grafica della mappa dei contagi in Italia](mappa.jpg "Grafica della mappa dei contagi in Italia")

In modo molto semplificato, assumono che la probabilità di infettarsi di una persona che vive nel luogo con coordinate $(X,Y)$ sia tanto maggiore quanto maggiore è il numero totale di casi positivi rilevati a una distanza $\leq D$ da $(X,Y)$. 
 
Ricorda che la distanza (Euclidea) tra due punti $(X,Y)$ e $(A,B)$ può essere stimata come 
$\sqrt{(X-A)^2 + (Y-B)^2 }$ . 
 
Il tuo compito è di aiutare Giuseppe e Irene a sviluppare l'app, identificando, tra le N persone, _**chi ha la maggiore probabilità di sviluppare il contagio**_.  


## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di testcase. Le successive righe mostrano i $T$ testcase in ordine. Per ogni testcase:

- La prima riga contiene l'intero $N$
- Le successive $N$ righe contengono le coppie $X_i, Y_i$, ciascuna su una riga diversa, rappresentate come due interi separati da uno spazio, senza parentesi
- La riga successiva contiene l'intero $Z$ 
- Le successive $Z$ righe contengono le triple $X_j,Y_j,P_j$, ciascuna su una riga diversa, rappresentate come tre interi separati da uno spazio, senza parentesi
- La riga successiva contiene l'intero $D$ 

## Dati di output

Il file di output deve essere composto da $T$ righe, ciascuna delle quali contenente la dicitura ```Case #x: y``` dove `x` è il numero del testcase (a partire da $1$) e `y` è un numero tra $1$ ed $N$ che rappresenta la persona con la massima probabilità di contagio (si può assumere che tale persona sia unica).

## Assunzioni

- $1\le T\le 10$
- $1 \le N \le 100$
- $1 \le X\le 100$, $1 \le Y\le 100$
- $1 \le D \le 10$
- $1 \le P \le 10$
- $1 \le Z \le 100$ 


## Esempi di input/output

---

**Input:**

```
1
3 
1 1 
3 3 
5 5  
4 
0 1 5 
2 3 10 
8 6 2 
4 4 15 
2 
```

---

**Output:**

```
Case #1: 2
```

## Spiegazione

- La persona $1$, che vive in $(1,1)$, si trova a distanza $1$ da $(0,1)$, a distanza $\sqrt{5}= 2.23$ da $(2,3)$ e a distanza ancora maggiore dai punti $(4,4)$ e $(8,6)$. Quindi il numero di casi positivi a distanza al più $2$ dalla persona $1$ è pari a $5$, ovvero il numero di casi positivi rilevati in $(0,1)$. 

- La persona $2$, che vive in $(3,3)$, si trova a distanza $1$ da $(2,3)$, a distanza $\sqrt{2}= 1.41$ da $(4,4)$ e a distanza maggiore di $2$ dai punti $(0,1)$ e $(8,6)$. Quindi il numero di casi positivi a distanza al più $2$ dalla persona $2$ è pari a $10+15 = 25$. 

- La persona $3$, che vive in $(5,5)$, si trova a distanza $\sqrt{2}= 1.41$ da $(4,4)$ e a distanza maggiore di $2$ da tutti gli altri punti. Quindi il numero di casi positivi a distanza al più $2$ dalla persona $3$ è pari a $15$. 

La persona con il maggior numero di casi positivi nel suo vicinato è quindi la persona $2$.
