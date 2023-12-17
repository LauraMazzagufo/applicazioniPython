#Modificate la funzione trova in modo che richieda un terzo parametro, che
# rappresenta la posizione da cui si deve cominciare la ricerca all’interno della stringa parola.
# def trova(parola, lettera):
#     indice = 0
#     while indice < len(parola):
#         if parola[indice] == lettera:
#             return indice
#         indice += 1
#     avviso = "NON TROVATO!"
#     return avviso


def trova(parola, lettera, posizione):
    while posizione < len(parola):
        if parola[posizione-1] == lettera:
            return posizione
        posizione += 1
    avviso = "NON TROVATO!"
    return avviso

print(trova("abcdefghi", "g", 4))
