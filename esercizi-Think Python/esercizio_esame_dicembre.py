# Funzione che stampa solo elementi di indice pari di una lista.

lista = [3, 5, 4, 7, 6, 1, 0, -3, -2, 0]
def stampa_indice_pari(list):
    for i in range(0, len(list), 2):
        print(list[i])

stampa_indice_pari(lista)




# data una lista di valori interi, scrivere una funzione che sommi tutti i valori,
# una funzione che sommi tutti i valori in posizione pari
# una funzione che sommi tutti i valori in posizione dispari
# una funzione che sommi tutti i valori pari
# una funzione che sommi tutti i valori dispari


def somma_valori(list):
    somma = 0
    for i in list:
        somma += i
    return somma


def somma_valori_posizione_pari(list):
    somma = 0
    for item in range(0, len(list), 2):
        somma += list[item]
    return somma


def somma_valori_posizione_dispari(list):
    somma = 0
    for i in range(1, len(list), 2):
        somma += list[i]
    return somma


def somma_valori_pari(list):
    somma = 0
    for i in list:
        if i % 2 == 0:
            somma += i
    return somma


def somma_valori_dispari(list):
    somma = 0
    for i in list:
        if i % 2 != 0:
            somma += i
    return somma

lista = [1, 2, 3, 4, 5, 20, 100]
print()
print(lista)
print(somma_valori(lista))
print(somma_valori_posizione_pari(lista))
print(somma_valori_posizione_dispari(lista))
print(somma_valori_pari(lista))
print(somma_valori_dispari(lista))



def somma_valori(l):
    totale = 0
    for i in l:
        totale += i
    return totale


print("La somma dei valori della lista è: ", somma_valori(lista))


def somma_valori_posizione_pari(l):
    totale = 0
    for i in range(1, len(l), 2):
        totale += l[i]
    return totale


print("La somma dei valori della lista in posizione pari è: ", somma_valori_posizione_pari(lista))


def somma_valori_posizione_dispari(l):
    totale = 0
    for i in range(0, len(l), 2):
        totale += l[i]
    return totale


print("La somma dei valori della lista in posizione dispari è: ", somma_valori_posizione_dispari(lista))


def somma_valori_pari(l):
    totale = 0
    for i in l:
        if i % 2 == 0:
            totale += i
    return totale

print("La somma dei valori pari della lista è: ", somma_valori_pari(lista))


def somma_valori_dispari(l):
    totale = 0
    for i in l:
        if i % 2 != 0:
            totale += i
    return totale


print("La somma dei valori dispari della lista è: ", somma_valori_dispari(lista))