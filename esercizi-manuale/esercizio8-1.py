# Scrivete una funzione che riceva una stringa come argomento e ne stampi i singoli
# caratteri, uno per riga, partendo dall’ultimo a ritroso.

def stampa_al_contrario(stringa):
    i = len(stringa)
    while i > 0:
        lettera = stringa[i-1]
        print(lettera)
        i -= 1

parola = input("Inserisci una parola:\n")
stampa_al_contrario(parola)

# parola = "camion"
# lunghezza = len(parola)
# ultima_lettera = parola[lunghezza - 1]
#
# print(ultima_lettera)
# print(parola[-1])
# print()
#
# indice = 0
# while indice < len(parola):
#     lettera = parola[indice]
#     print(lettera)
#     indice += 1
