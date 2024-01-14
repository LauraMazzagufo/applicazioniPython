# Scrivere una funzione ricorsiva che calcola la somma dei primi n numeri
def somma(n):
    if n == 1:
        return n
    return n + somma(n-1)

print(somma(5))
print()

# Scrivere una funzione ricorsiva che calcola la potenza di un numero
def potenza(n,m):
    if m == 1:
        return n
    return n * potenza(n, m-1)

print(potenza(2,3))
print()


# Il Triangolo di Pascal è un insieme di numeri organizzati in un triangolo di numeri tali che anr=n! / (r!(n−r)!)
# Questa equazione è l’equazione del coefficiente binomiale. Possiamo costruire il triangolo di Pascal sommando i due
# numeri che sono sopra (diagonalmente) a ciascun numero. Scrivere un programma che stampa il triangolo di Pascal. Il
# programma deve accettare un parametro che dice il numero di righe da stampare.

# iterativo:
def binomial(n,k):
    if k==0 or k==n :
        return 1
    return binomial(n-1,k-1)+binomial(n-1,k)

def pascal(n):
    for i in range(n+1):
        s = ""
        for k in range(i+1):
            s = s + str(binomial(i,k)) + " "
        print(s)


pascal(2)
pascal(10)
print()

# ricorsivo:
def binomial(n,k):
    if k==0 or k==n :
        return 1
    return binomial(n-1,k-1)+binomial(n-1,k)

def riga(n):
    s = ""
    for k in range(n + 1):
        s = s + str(binomial(n, k)) + " "
    return s

def pascal(n):
    if n == 1:
        print ("1")
        return
    pascal(n-1)
    print(riga(n))
    return


pascal(2)
pascal(10)
print()

# I numeri di Catalan sono una sequenza di interi particolare. Realizzare una funzione ricorsiva, che dato un numero
# n calcola (e restituisce) l’n-esimo numero delle sequenza in base alla definizione induttiva fornita in questo pdf.


# Verifica (ricorsiva) di proprietà. Scrivere una funzione ricorsiva che legge da input una sequenza di valori interi
# positivi terminata dal valore 0 (che non fa parte della sequenza) e che verifica la seguente proprietà: ogni valore
# letto è doppio del valore precedente. Ad esempio la sequenza 2 4 8 16 32 0 verifica la proprietà. La funzione deve
# restituire 1 se la proprietà è verificata e 0 altrimenti e non può utilizzare gli array.



# Inversione di una stringa ricorsiva. Scrivere un programma che legge una sequenza di interi terminata da 0 (chiede
# un intero alla volta) e stampa la sequenze invertita sullo schermo. Ad esempio, leggendo la sequenza 1 8 3 4 6 0,
# deve stampare 6 4 3 8 1. Il programma deve fare uso di una funzione ricorsiva e non può usare liste o array.

