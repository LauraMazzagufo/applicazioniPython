# Scrivete una funzione chiamata somma_nidificata che richieda come parametro
# una lista nidificata di numeri interi e sommi gli elementi di tutte le liste nidificate.

t = [[1, 2], [4, 5, 6, 7]]

def somma_nidificata(lista):
    parziale = 0
    for sottolista in lista:
        parziale += sum(sottolista)
    return(parziale)

print(somma_nidificata(t))
