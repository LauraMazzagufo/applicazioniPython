# Negli esercizi seguenti useremo il modulo test con la funzione testEqual. In particolare dopo avere importato con
# from test import testEqual, la chiamata testEqual(x, y) stampa “Pass” se x è uguale a y, altrimenti comunica che x
# è diverso da y generando un errore di esecuzione.

def testEqual(x, y):
    if x == y:
        print("Pass")
    else:
        print("Not Passing")
        # qui stiamo stampando invece di generare un'eccezione e interrompere l'esecuzione


# Scrivere una funzione sumTo(n) che ritorna la somma di tutti i numeri interi fino a n (incluso). Per cui sumTo(10)
# corrisponde a 1+2+3...+10 ovvero 55. Usare l’equazione (n * (n + 1)) / 2. Per vedere l’output della funzione
# ricordiamoci che la funzione va invocata.

def sumTo(n):
    # somma = (n * (n+1)) / 2
    somma = 0
    for i in range(n + 1):
        somma += i
    return somma


print(sumTo(10))
# Prove con TestEqual
testEqual(sumTo(0), 0)
testEqual(sumTo(10), 55)
testEqual(sumTo(5), 15)

# Scrivere una funzione areaOfCircle(r) che ritorna l’area del cerchio di r, usando il modulo math.
import math


def areaOfCircle(r):
    area = math.pi * r * r
    return round(area, 2)


print(areaOfCircle(5))
t = areaOfCircle(0)
testEqual(t, 0)
t = areaOfCircle(1)
testEqual(t, math.pi)
t = areaOfCircle(100)
testEqual(t, 31415.926535897932)


# Riscrivere la funzione sumTo(n) che ritorna la somma dei numeri fino a n incluso usando l’iterazione (accumulazione).
# fatto, vedi primo esercizio


# Scrivere una funzione chiamata mySqrt che approssima la radice quadrata di un numero n usando l’algoritmo di
# Newton. L’algoritmo di Newton raffina l’approssimazione iterativamente: l’approssimazione iniziale è n/2 e
# l’approssimazione successiva (newguess) è ottenuta da quella precedente usando la seguente formula: newguess = (
# 1/2) * (oldguess + (n/oldguess)).
import math


def mySqrt(n, k):
    newguess = n / 2
    for i in range(k):
        newguess = (1/2) * (newguess + (n/newguess))
    return newguess

print(f" La radice quadrata di 43 è {mySqrt(43, 1)} --> {math.sqrt(43)}")


# Scrivere una funzione chiamata myPi che ritorna un’approssimazione di PI (3.14159...), usando l’approssimazione di
# Leibniz <http://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80>.


# Scrivere una funzione che prende in input 10 numeri e calcola il minimo, la somma, il massimo e la media.
def operazioni():
    numero_iniziale = int(input("Inserisci un numero: "))
    minimo = numero_iniziale
    somma = 0
    massimo = numero_iniziale
    media = 0
    for i in range(9):
        n = int(input("Inserisci un numero: "))
        somma += n
        media = somma / 10
        #if n < minimo:
        #    minimo = n
        minimo = min(minimo, n)
        #if n > massimo:
        #    massimo = n
        massimo = max(massimo, n)
    return minimo, somma, massimo, media

print(operazioni())

