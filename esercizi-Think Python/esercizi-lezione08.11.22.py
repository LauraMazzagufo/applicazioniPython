# Creare una lista contenente 100 numeri interi random tra 0 e 1000. Scrivere una funzione chiamata average che
# prende una lista come parametro e ritorna la media dei valori contenuti nella lista.
import random

lista = []
for i in range(100):
    numero = random.randint(0, 1000)
    lista.append(numero)
print(lista)


def average(list):
    somma = 0
    for i in list:
        somma += i
    return somma / 100


print(average(lista))


# funzione generica:
def crea_random(n):
    lst = []
    for i in range(n):
        x = lst.append(random.randint(0, 1000))
    return lst


def media(lst):
    somma = 0
    for i in lst:
        somma = somma + i
    return somma / len(lst)


x = crea_random(10)
y = media(x)
print(x)
print(y)

# Scrivere una funzione che prende una lista di 100 interi random tra 0 e 100 e ritorna il valore massimo contenuto
# nella lista. (Nota: non usare la funzione max.)
import random


def crea_random(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, 100))
    return list


def massimo(lista):
    n_massimo = 0
    for n in lista:
        if n > n_massimo:
            n_massimo = n
    return n_massimo


list = crea_random(100)
print(list)
print(massimo(list))


# Scrivere una funzione sum_of_squares(xs) che calcola la somma dei quadrati dei numeri nella lista xs. Per esempio,
# sum_of_squares([2, 3, 4]) dovrebbe ritornare 4+9+16 ovvero 29:

def sum_of_squares(xs):
    somma = 0
    for i in xs:
        quadrato = i * i
        somma += quadrato
    return somma


# con ricorsione:
# def sum_of_squares(lst):
#     if lst == []:
#         return 0
#     return sum_of_squares(lst[1:]) + lst[0]*lst[0]

lista = [2, 3, 4]
print(sum_of_squares(lista))


# Scrivere una funzione per contare quanti numeri dispari ci sono in una lista.

def conta_dispari(lista):
    contatore = 0
    for i in lista:
        if i % 2 != 0:
            contatore += 1
    return contatore


# ricorsiva:
# def countOddrec(lst):
#     if lst == []:
#         return 0
#     if lst[0] % 2 != 0:
#         return 1 + countOddrec(lst[1:])
#     return countOddrec(lst[1:])


list = [2, 4, 6, 5, 2, 9, 7, 5, 6, 0, 11, 13, 2, 3, 5, 6, 9]
print(conta_dispari(list))


# Sommare tutti i numeri pari in una lista.


def somma_pari(lista):
    contatore = 0
    for i in lista:
        if i % 2 == 0:
            contatore += i
    return contatore


def somma_pari_rec(lista):
    if lista == []:
        return 0
    if lista[0] % 2 == 0:
        return lista[0] + somma_pari_rec(lista[1:])
    return somma_pari_rec(lista[1:])


list = [2, 4, 6, 5, 2, 9, 7, 5, 6, 0, 11, 13, 2, 3, 5, 6, 9]
print(somma_pari(list))
print(somma_pari_rec(list))


# Contare quante parole in una lista hanno lunghezza 5.


def conta_parole(list):
    contatore = 0
    for parola in list:
        if len(parola) == 5:
            contatore += 1
    return contatore


lista = ["casa", "gatto", "luce", "bicchiere", "manto", "conta"]
print(conta_parole(lista))


# funzione generica
def conta_parole(list, n):
    contatore = 0
    for parola in list:
        if len(parola) == n:
            contatore += 1
    return contatore


lista = ["casa", "gatto", "luce", "bicchiere", "manto", "conta"]
print(conta_parole(lista, 5))


# Sommare tutti gli elementi in una lista fino al primo numero pari contenuto nella lista escluso.

def conta_parole(lst,k):
    """Conta le parole lunghe k (k> 0) nella lista lst"""
    s = 0
    for i in lst:
        if len(i) == k:
            s = s+1
    return s

g = ["gatto","pianta","gigi"]
print(conta_parole(g,5))


# Sommare tutti gli elementi in una lista fino al primo numero pari contenuto nella lista escluso.

def conta_fino_pari(list):
    somma = 0
    index = 0
    while list[index] % 2 != 0:
        somma += list[index]
        index += 1
    return somma


lista = [5, 9, 7, 5, 6, 0, 11, 13, 2, 3, 5, 6, 9]
print(conta_fino_pari(lista))


# Contare quante parole occorrono in una lista fino alla prima occorrenza della parola “sam”.

def conta_fino_sam(list):
    contatore = 0
    index = 0
    while list[index] != "sam":
        contatore += 1
        index += 1
    return contatore

# soluzione con for
def conta_fino_sam2(list):
    contatore = 0
    for parola in list:
        if parola == "sam":
            return contatore
        contatore += 1


lista = ["casa", "gatto", "luce", "sam", "bicchiere", "manto", "conta"]
print(conta_fino_sam(lista))
print(conta_fino_sam2(lista))


# Con riferimento alle liste, implementare funzioni Python che funzionano come le seguenti (senza usare le funzioni
# corrispondenti fornite dalla libreria):
# count (parametro: item, risultato: Ritorna il numero di occorrenze)
# in (in e not in sono operatori booleani che controllano l’appartenenza)
# reverse (parametro: none, risultato: Inverte l’ordine degli elementi)
# index (parametro: item, risultato: Ritorna la posizione della prima occorrenza)
# insert (parametro: position, item; risultato: Inserisce un nuovo elemento alla posizione data)


def count(list, item):
    contatore = 0
    for i in list:
        if i == item:
            contatore += 1
    return contatore


def inside(list, item):
    flag = False
    for i in list:
        if i == item:
            flag = True
    return flag


def reverse(list):
    list2 = []
    for i in range(len(list)-1, -1, -1): # len(list)-1 --> perché l'indice parte da 0, deve arrivare a 0 (indice -1), e ciclo scorre al contrario
        list2.append(list[i])
    return list2


def index(list, item):
    index = 0
    while list[index] != item:
        index += 1
    return index


def insert(list, position, item):
    list2 = list[:position]
    list3 = list[position:]
    list2.append(item)
    for i in list3:
        list2.append(i)
    return list2

# def insert(list, index, item):
#     newlst = []
#     for i in range(len(list)):
#         if i == index:
#             newlst.append(item)
#         newlst.append(list[i])
#     return newlst


lista = [5, 9, 7, 5, 6, 0, 11, 13, 2, 3, 5, 6, 9]
print(count(lista, 6))
print(lista.count(6))

print(inside(lista, 11))
print(11 in lista)

print(reverse(lista))
lista.reverse() # non si può riassegnare, altrimenti si perde contenuto lista (come con sort)
print(lista)

print(index(lista, 0)) # dà 7 come risultato perché gli elementi sono stati invertiti con reverse()
print(lista.index(0))

print(insert(lista, 2, "gatto"))
lista.insert(2, "gatto")
print(lista)
