# Usate tutte_maiuscole per scrivere una funzione di nome maiuscole_nidif
# che prenda una lista nidificata di stringhe e restituisca una nuova lista nidificata di stringhe, in
# lettere maiuscole.

t = [["a", "b"], ["c", "d", "e", "f"]]


def tutte_maiuscole(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def maiuscole_nidif(lista):
    nuova_lista = []
    for sottolista in lista:
        nuova_lista.append(tutte_maiuscole(sottolista))
    return nuova_lista


print(maiuscole_nidif(t))
