**Difficoltà: _1_**

## Descrizione del problema

Michele è stato il primo vincitore della borsa di studio **LuissMatics** per frequentare il **Bachelor in Management and Computer Science** alla Luiss. Durante il suo terzo anno di studi, è stato ammesso allo scambio con l'Università di Paris Dauphine. Michele adora **Parigi**, sin da quando ha gareggiato per SWERC 2019! Ogni volta che si trova a Parigi, Michele cerca di visitare più monumenti possibili e ogni giorno annota nel suo diario quali monumenti ha visitato in quel giorno. Dopo vari viaggi e vari giorni passati a Parigi, Michele si chiede quanti monumenti diversi ha visitato in totale durante la sua permanenza a Parigi. 

![Michele e il suo team SWERC a Parigi](swerc_luiss.jpg "Michele e il suo team SWERC a Parigi")

Aiuta Michele scrivendo un programma che, dato il suo diario, calcoli il **numero di monumenti diversi** che ha visitato durante tutti i suoi viaggi a Parigi.

## Dati di input

La prima riga del file di input contiene un intero $T$, il numero di testcase.
Le successive righe mostrano i $T$ testcase in ordine. Ogni testcase è composto da $N+1$ righe. La prima riga contiene l’intero $N$, il numero di monumenti che Michele ha visitato durante tutti i suoi viaggi a Parigi. Le successive $N$ righe contengono prima una data (nel formato YYYY-MM-DD), poi uno spazio, e infine il nome di un monumento. I nomi dei monumenti sono stringhe di caratteri di lunghezza arbitraria e possono contenere qualsiasi carattere stampabile, ad eccezione del carattere newline. 

## Dati di output

Il file di output deve essere composto da $T$ righe, ciascuna delle quali contenente la dicitura ```Case #x: y``` dove `x` è il numero del testcase (a partire da $1$) e `y` è un intero positivo (o nullo): il numero di monumenti diversi visitati da Michele.

## Assunzioni
- $1 \le T \le 10$.
- $1 \le N \le 100$.

## Esempi di input/output

---

**Input:**

```
2
9
2019-12-30 Tour Eiffel
2019-12-31 Tour Saint-Jacques
2019-12-31 Centre Georges Pompidou
2020-01-23 Tour Eiffel
2020-01-23 Invalides
2020-01-23 Arc de Triomphe
2020-01-26 Tour Saint-Jacques
2020-01-26 Panthéon
2020-01-27 Sacré Cœur
5
2019-12-29 Tour Eiffel
2019-01-05 Tour Saint-Jacques
2020-01-05 Tour Eiffel
2020-01-05 Arc de Triomphe
2020-01-06 Tour Saint-Jacques
```

---

**Output:**

```
Case #1: 7
Case #2: 3
```
