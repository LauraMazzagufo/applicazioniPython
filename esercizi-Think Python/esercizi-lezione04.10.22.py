# Usare il ciclo for per stampare 10 numeri casuali.
import random
for i in range(10):
    n = random.randint(0, 1000)
    print(n)


# Ripetere l’esercizio sopra, ma questa volta stampare 10 numeri interi nell’intervallo [25,35).
# import random
for i in range(10):
    n = random.randint(25, 35)
    print(n)


# Generare un numero casuale reale nell’intervallo [25,35).
# import random
n_float = random.random()
n = 25 + (n_float * (35-25))
print(n)


# Il Teorema di Pitagora dice che la lunghezza dell’ipotenusa di un triangolo rettangolo è legata alla lunghezza dei
# cateti. Usando il modulo math, trovare una funzione che calcola l’ipotenusa a partire dai due cateti.

import math

l1 = int(input("Inserisci la lunghezza del primo catete: "))
l2 = int(input("Inserisci la lunghezza del secondo catete: "))


def pitagora(c1, c2):
    ipotenusa = math.sqrt((c1*c1) + (c2*c2))
    # oppure ipotenusa = math.sqrt((c1**2) + (c2**2))
    # oppure ypotenuse = math.hypot(side1,side2)
    ipotenusa = round(ipotenusa, 2)
    return ipotenusa

print(pitagora(l1, l2))


# Cercare un modo su internet per calcolare pi. Ce ne sono molti che usano semplici operazioni aritmetiche. Scrivere
# un programma per calcolare l’approssimazione e confrontare l’approssimazione con il valore di math.pi del modulo math.

# serie di Gregory-Leibniz
howmany= 30000
pigreco= 0
for i in range(1,howmany,4):
    pigreco = pigreco + 4/(i)
for i in range(3,howmany,4):
    pigreco = pigreco - 4/(i)

print(pigreco)
print(math.pi)

# un esempio di calcolo che amplifica l'errore -- attenzione ad alternare + e -
howmany1=30000
pigreco1 = 0
for i in range(1,howmany,4):
    pigreco1 = pigreco1 + 4/(i) - 4/(i+2)

print(pigreco1)
print(math.pi)