# Scrivete una funzione di nome mediani che prenda una lista e restituisca una nuova
# lista che contenga tutti gli elementi esclusi il primo e l’ultimo. Quindi mediani([1,2,3,4])
# deve restituire [2,3].

t = [1, 2, 3, 4]
def mediani(lista):
    del(lista[0])
    del(lista[-1])
    return lista

print(mediani(t))