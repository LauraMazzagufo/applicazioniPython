# Scrivere una funzione print_triangular_numbers(n) che stampa i primi n numeri triangolari (Cercare sul web cosa è
# un numero triangolare). Una chiamata a print_triangular_numbers(5) produrrebbe il seguente risultato:
# 1       1
# 2       3
# 3       6
# 4       10
# 5       15

# formula: t di n = (n(n + 1) / 2)
def print_triangular_numbers(n):
    for i in range(1, n + 1):
        t = (i * (i + 1) / 2)
        print(i, "\t", int(t))


print_triangular_numbers(5)


# Leggere tre reali e stampare il massimo il minimo e la somma dei tre.

def operazioni(a, b, c):
    somma = a + b + c
    massimo = max(a, b, c)
    minimo = min(a, b, c)
    print(massimo, minimo, somma)


operazioni(2, -4, 0.5)


# Leggere venti reali in input, calcolare il massimo, il minimo e la somma di tutti i valori e stamparli.

def operazioni2():
    n = int(input("Inserisci un numero: "))
    massimo = n
    minimo = n
    somma = 0
    for i in range(19):
        n_nuovo = int(input("Inserisci un altro numero: "))
        if n_nuovo >= massimo:
            massimo = n_nuovo
        if n_nuovo <= minimo:
            minimo = n_nuovo
        somma += n_nuovo
    print(f"Massimo: {massimo}\nMinimo: {minimo}\nSomma: {somma}")


operazioni2()


# Leggere una serie di reali terminata dal valore 0.0. Calcolare il massimo, minimo e somma totale dei reali nella
# serie e stamparli.
def operazioni3():
    n = float(input("Inserisci un numero: "))
    massimo = n
    minimo = n
    somma = 0
    while n != 0.0:
        n_nuovo = float(input("Inserisci un altro numero: "))
        if n_nuovo >= massimo:
            massimo = n_nuovo
        if n_nuovo <= minimo:
            minimo = n_nuovo
        somma += n_nuovo
        n = n_nuovo
    print(f"Massimo: {massimo}\nMinimo: {minimo}\nSomma: {somma}")


operazioni3()


# Si scriva una funzione con un parametro intero n che calcola la somma dei numeri dispari nell’intervallo (0, n).
def somma_dispari(n):
    somma = 0
    # for i in range(0, n+1):
    # if i % 2 != 0:
    for i in range(1, n + 1, 2):
        somma += i
    print(somma)


somma_dispari(5)


def somma_dispari_2(n):
    somma = 0
    counter = 1
    while counter <= n:
        # if counter % 2 != 0:
        #   somma += counter
        # counter += 1
        somma += counter
        counter += 2
    print(somma)


somma_dispari_2(7)


def somma_dispari_3(n):
    somma = 0
    counter = 1
    while True:
        somma += counter
        counter += 2
        if counter == n + 2:
            break
    print(somma)


somma_dispari_3(7)


# Scrivere un programma che legga da tastiera un numero intero x e stampi il valore di x!. Per x! si intende x
# fattoriale

def fattoriale(n):
    risultato = 1
    for i in range(1, n + 1):
        risultato = i * risultato
    print(risultato)


fattoriale(4)


def fattoriale_2(n):
    risultato = 1
    counter = 1
    while counter <= n:
        risultato = counter * risultato
        counter += 1
    print(risultato)


fattoriale_2(18)


# Si scriva una funzione che, dati 2 parametri n ed m interi positivi, calcola e stampa il loro prodotto senza usare
# l’operatore * ma usando solo le operazioni di somma, sottrazione e gli operatori di confronto.

def stampa_prodotto(n, m):
    risultato = 0
    for i in range(1, m + 1):
        risultato += n
    print(risultato)


stampa_prodotto(3, 4)


def stampa_prodotto_2(n, m):
    risultato = 0
    i = 1
    while i <= m:
        risultato += n
        i += 1
    print(risultato)


stampa_prodotto_2(3, 5)


# Si scriva una funzione che, dati 2 parametri n ed m naturali (n maggiore o uguale a 0 e m maggiore di 0),
# calcola la loro divisione intera senza usare gli operatori di divisione ma usando solo le operazioni di somma,
# sottrazione e gli operatori di confronto.
# Si scriva una funzione che, dati 2 parametri n ed m, naturali (n maggiore o uguale a 0 e m maggiore di 0),
# calcola il resto della divisione intera di n ed m senza usare gli operatori di divisione e il modulo ma usando solo
# le operazioni di somma, sottrazione e gli operatori di confronto.
def stampa_differenza(n, m):
    dividendo = max(n, m)
    divisore = min(n, m)
    # in realtà no! questo è errore concettuale, la divisione non è commutativa!
    quoziente = 1
    if not (dividendo >= 0 and divisore > 0):
        print("Divisione non consentita")
    resto = dividendo - divisore
    while resto >= divisore:
        resto -= divisore
        quoziente += 1
    print(f"{dividendo} diviso {divisore} = {quoziente} con il resto di {resto}")


stampa_differenza(17, 4)


def stampa_differenza_2(n, m):
    dividendo = max(n, m)
    divisore = min(n, m)
    resto = dividendo - divisore
    counter = 1
    while True:
        resto -= divisore
        counter += 1
        if resto == 0:
            break
        if resto < 0:
            resto += divisore
            counter -= 1
            break
    print(f"{dividendo} diviso {divisore} = {counter} con il resto di {resto}")


stampa_differenza_2(25, 4)


# Si scriva una funzione che, dati 2 parametri n ed m interi positivi, calcola n**m. Non usare funzioni di libreria e
# **, ma solo le operazioni aritmetiche.

def stampa_potenza(n, m):
    potenza = n
    for i in range(1, m):
        potenza = potenza * n
    return potenza


print(stampa_potenza(5, 3))
print(5 ** 3)


# Si scriva un programma che legge in input un valore k e poi legge k valori uno alla volta. Il programma deve
# stampare il messaggio “Zero contenuto nella sequenza” oppure “Zero non contenuto nella sequenza” a seconda che il
# valore 0 sia o meno contenuto tra i k valori letti.
def trovazero():
    k = int(input("Per quante volte vuoi eseguire la verifica? > "))
    zero = False
    for i in range(k):
        n = int(input("Inserisci un numero: > "))
        if n == 0:
            zero = True
    if zero:
        print("Zero contenuto nella sequenza")
    else:
        print("Zero non contenuto nella sequenza")


trovazero()


def trovazero_2():
    k = int(input("Per quante volte vuoi eseguire la verifica? > "))
    zero = False
    i = 0
    while i < k:
        n = int(input("Inserisci un numero: > "))
        if n == 0:
            zero = True
        i += 1
    if zero:
        print("Zero contenuto nella sequenza")
    else:
        print("Zero non contenuto nella sequenza")


trovazero_2()


# Leggere una serie di reali terminata dal valore 0.0. Stampare in output la parola “Ordinata” se la sequenza e’
# ordinata in modo crescente e “Non ordinata” altrimenti.

def ordine():
    n = int(input("Inserisci un numero: > "))
    ordinata = True
    while True:
        nuovo = int(input("Inserisci un numero: > "))
        if nuovo == 0:
            break
        elif nuovo > n:
            n = nuovo
            continue
        elif nuovo < n:
            ordinata = False
    if ordinata:
        print("Ordinata")
    else:
        print("Non ordinata")


ordine()


# Estendere il programma in modo da riconoscere se la sequenza è ordinata in modo crescente o descrescente e stampare
# “Ordinata crescente” o “Ordinata decrescente”.


def ordine():
    n = int(input("Inserisci un numero: > "))
    ordinata_crescente = True
    ordinata_decrescente = True
    while True:
        nuovo = int(input("Inserisci un numero: > "))
        if nuovo == 0:
            break
        elif nuovo > n:
            ordinata_decrescente = False
            n = nuovo
            continue
        elif nuovo < n:
            ordinata_crescente = False
            n = nuovo
            continue
    if ordinata_crescente:
        print("Ordinata in ordine crescente")
    elif ordinata_decrescente:
        print("Ordinata in ordine decrescente")
    else:
        print("Non ordinata")


ordine()

# Scrivere un programma che legge da tastiera un intero x e stabilisce se il numero è primo. Il programma stampa in
# output 1 se x è primo, 0 altrimenti.

def numero_primo():
    n = int(input("Inserisci un numero: > "))
    divisibile = False
    for i in range(2, n):
        if n % i == 0:
            divisibile = True
    if not divisibile:
        print("1")
    else:
        print("0")


numero_primo()

def numero_primo2(n):
    i = 2
    while (i<=n/2):
        if n%i == 0:
            return False
        i=i+1
    return True

numero_primo2(17)

# Scrivere un programma che prende in ingresso tre reali a, b e c e stampa le due soluzioni dell’equazione a*x**2 +
# b*x + c = 0 usando la formula standard. Controllare che il delta sia maggiore o uguale a 0.

def equazione(a, b, c):
    """Risolve a*x**2 + b*x + c = 0 fornendo le due soluzioni solo nel caso che a >0 e delta >=0"""
    if a <= 0:
        print("Errore nel calcolo dell'equazione")
        return None
    else:
        delta = b * b - 4 * a * c

        # se delta negativo la radice quadrata esiste solo nel capo dei numeri complessi
        if delta < 0:
            print("Errore nel calcolo dell'equazione")
            return None
        # se delta == 0 ho due radici reali coincidenti
        if delta == 0:
            ris = (-b) / (2 * a)
            return (ris, ris)
        # altrimenti ho due radici reali distinte ottenibili dalla formula standard
        deltasqrt = math.sqrt(delta)
        return ((-b - deltasqrt) / (2 * a), (-b + deltasqrt) / (2 * a))