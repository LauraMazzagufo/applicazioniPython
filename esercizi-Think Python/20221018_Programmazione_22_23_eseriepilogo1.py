# Generare i primi 20 numeri di una sequenza pseudocasuale nell’intervallo [1, 100)
# e stamparli sullo schermo. Verificare su internet il funzionamento della random.seed()
# e usarla per generare due volte la stessa identica sequenza di 20 numeri.

import random


def genera(seed,n):
    random.seed(seed)
    for i in range(n):
        print(random.randrange(1,200))

seme = int(input("inserisci il seme:"))
for i in range(2):
    print("Sequenza" + str(i+1))
    genera(seme,20)


# costruire un generatore
# parametri (Gordon):
M = 2**31
a = 5**13
b = 0

def genera_numero(n):
    nuovo_n = (a * n + b) % M
    return nuovo_n


seme = int(input("Inserisci il seme:"))
x = seme
for i in range(100):
    x = genera_numero(x)
    print(x)


# Utilizzare il modulo Turtle e Random per effettuare uno spostamento casuale.
# La tartaruga si muove di 5 pixel, ruota casualmente verso sinistra o verso destra
# di un angolo compreso fra (-30,30) e ripete l’operazione per un numero di volte
# fornito in input dall’utente.
# Guardate su internet la documentazione di turtle.color e usatela per
# scegliere il colore della penna della tartaruga.

#import turtle
from turtle import *
from random import *
import math

passi = int(input("Quanti passi?"))
t = Turtle()

color('green', 'light blue')

for i in range(passi):
    x = randint(-30, 30)
    forward(5)
    left(x)


# test
def testEqual(x,y):
    """Testa l’uguaglianza fra due valori (int, str)"""
    if x == y:
        print("Pass")
    else:
        print("Not Passing")

#test float
def testEqualF(x, y, e):
    """Testa l’uguaglianza fra due valori (float)"""
    if abs(x - y) < e:
        print("Pass Float")
    else:
        print("Expected" + str(x) + "got" + str(y))

testEqual(2,2) #Pass
testEqual(2,3) #Expected 2 got 3
testEqual("ss","ss") #Pass
testEqual("h","g") #Expected h got g
testEqual(2.0,2) #Pass
testEqualF(math.hypot(1, 1.73205),1.999999,0.001) #pass
