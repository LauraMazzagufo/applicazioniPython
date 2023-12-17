fin = open('words.txt')

def crea_dizionario(file):
    dizionario = dict()
    for riga in file:
        parola = riga.strip()
        dizionario[parola] = None
    return dizionario

dizionario = crea_dizionario(fin)

#verifica se una stringa è contenuta in un dizionario
p = input("Inserisci la stringa da cercare: > ")
if p in dizionario:
    print(f"{p} è nel dizionario!")
else:
    print(f"{p} non è nel dizionario.")
