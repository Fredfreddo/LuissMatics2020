**Difficoltà: _3_**

## Descrizione del problema

Data Science è alla base dei Social Media moderni. Non solo le piattaforme possono raccogliere ed analizzare i dati degli utenti, ma anche gli stessi utenti possono scoprire qualcosa di nuovo processando i dati pubblicamente accessibili.

"LuissZone" è una nuova piattaforma social. Questa piattaforma consente agli utenti di postare articoli su "LuissZone", e ogni utente, se vuole, può mettere like a ciascun post presente su "LuissZone". Tutti i post e tutti i 'like' sono pubblici e visibili a tutti gli utenti iscritti a "LuissZone".

![Grafica della luiss](luiss.jpg)

Fred ama analizzare i dati provenienti da "LuissZone". Fred è particolarmente interessato nel determinare l'utente più popolare di una data piattaforma. Dopo anni di ricerca ha determinato 3 importanti parametri per decidere la popolarità di un utente:

1. Il numero medio di parole nei post di un dato utente, denotato da $L=\frac{\sum{L_i}}{N}$, dove $N$ è il numero di post che l'utente ha postato e $L_i$ è il numero di parole di ciascun post.
2. Il numero totale di 'like' che l'utente ha ricevuto da altri utenti (escludendo i like messi dall'utente ai suoi post), denotato da $R$.
3. Il numero totale di like che l'utente ha aggiunto a post su "LuissZone" (includendo i like messi ai propri post), denotato da $G$.

Con questi tre parametri Fred ha inventato il 'Fred Coefficient':
: $F=\frac{LR}{G+1}$

Il testo di ciascun post è composto da lettere e spazi. Una sequenza di lettere separata da spazi (o separata da uno spazio se a inizio/fine riga) è considerata una parola.

L'utente con il maggiore 'Fred Coefficient' è definito come l'utente più popolare. Nel caso di più utenti con lo stesso 'Fred Coefficient', l'utente più popolare è l'utente che viene prima in ordine alfabetico.

Il tuo compito ora è trovare l'utente più popolare in un dato dataset "LuissZone", determinato calcolando il 'Fred Coefficient'.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di testcase.

Le righe seguenti contengono i $T$ testcase in ordine. Per ogni testcase: 

La prima riga è composta da: $N$, un intero, che rappresenta il numero di utenti in "LuissZone". 

La seconda riga è composta da: $M$ i nomi degli utenti separati da spazi.

La terza riga è composta da: $N_1,N_2....N_M$, interi separati da spazio, il numero di post postati da ogni utente, nello stesso ordine degli utenti indicati nella seconda riga.

Le seguenti $2\sum{N_i}$ righe: il numero di post e 'like' di ciascun utente indicati in base all'ordine fornito nella seconda riga. Per ogni post, la prima riga è una stringa con il testo del post, la seconda riga contiene i vari username separati da spazio, che indicano gli utenti che hanno messo like al post. (è possibile che un post non abbia ricevuto 'like' e abbia quindi $0$ 'like')

## Dati di output

Il file di output deve essere composto da $T$ righe, ciascuna delle quali contenente la dicitura ```Case #x: y``` dove `x` è il numero del testcase (a partire da $1$) e `y` è una stringa che rappresenta l'utente più popolare del testcase.

## Assunzioni

- $1 \leq T \leq 5$.
- $0 \le M \leq 100$.
- $1 \leq N_i \leq 10$, per $1 \leq i \leq M$.
- Il numero di parole di ciascun post è al più 50. (Per ogni post, $0 \le L \leq 100$).

## Esempi di input/output

***

**Input:**
```
2
2
Fred Michele
1 1
Ciao
Michele
A presto
Fred
3
Fred Francesco Michele
2 1 1
Hello world
Michele
Luiss is great
Fred Michele Francesco
Go Taddy Bear!
Fred
Minecraft
Fred Francesco Michele
```

***

**Output:**
```
Case #1: Michele
Case #2: Fred
```

***

## Spiegazione

_Case #1_:

Il 'Fred Coefficient' dei due utenti è:

Fred: ha un post con numero medio di parole 1, ha ricevuto 1 like da utenti diversi da se, e ha messo 1 like in totale. 
$1*1/(1+1)=0.5$


Michele: ha un post con numero medio di parole 2, ha ricevuto 1 like da utenti diversi da se, e ha messo 1 like in totale. 
$1*1/(1+1)=1$

_Case #2_:

Il 'Fred Coefficient' dei tre utenti è:

Fred: ha due post con numero medio di parole 2.5, ha ricevuto 3 like da utenti diversi da se, e ha messo 3 like in totale. 
$2.5*3/(3+1)=15/8$

Francesco: ha un post con numero medio di parole 3, ha ricevuto 1 like da utenti diversi da se, e ha messo 2 like in totale. 
$3*1/(2+1)=1$

Michele: ha un post con numero medio di parole 1, ha ricevuto 2 like da utenti diversi da se, e ha messo 3 like in totale. 
$1*2/(3+1)=0.5$
