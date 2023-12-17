# Scrivete una funzione di nome sed che richieda come argomenti una stringa modello,
# una stringa di sostituzione, e due nomi di file. La funzione deve leggere il primo file e scriverne il
# contenuto nel secondo file (creandolo se necessario). Se la stringa modello compare da qualche parte
# nel testo del file, deve sostituirla con la seconda stringa.
# Se si verifica un errore in apertura, lettura, scrittura, chiusura del file, il vostro programma deve gestire
# l’eccezione, stampare un messaggio di errore e terminare.

def sed(modello, sost, file1, file2):
    try:
        f1 = open(file1, "r")
        f2 = open(file2, "w")

        for riga in f1:
            riga = riga.replace(modello, sost)
            f2.write(riga)

        f1.close()
        f2.close()
    except:
        print("Si è verificato un errore")

pattern = 'pattern'
replace = 'replace'
file1 = 'words.txt'
file2 = file1 + '_replaced'
sed(pattern, replace, file1, file2)