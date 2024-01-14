#ese1-inclasse: chiedere all'utente n calcolare il fattoriale di n (n!)

f = int(input("Inserisci il numero di cui vuoi calcolare il fattoriale: > "))

def fattoriale(n):
    risultato = 1
    for i in range(1, n+1):
        risultato = i * risultato
    return risultato

print(fattoriale(f))


#ese2-inclasse: chiedere all'utente K e per ogni numero n fra 0 e K calcolare
# il fattoriale di n (n!)

K = int(input("Inserisci il numero di massimo di cui vuoi calcolare il fattoriale: > "))
def lista_fattoriale(n):
    risultato = 1
    for i in range(1, K+1):
        risultato = i * risultato
        print(f"Il fattoriale di {i} e' {risultato}.")
        # CAMBIA L'INDENTAZIONE: IL RISULTATO VIENE RESTITUITO A OGNI RIPETIZIONE DEL CICLO!!

lista_fattoriale(K)


#ese3-in classe: chiedere all'utente n ed k (n>0 e 0<= k < n) e calcolare
# il coefficiente binomiale  C(n k) = n! /(k! * (n-k)!)

n = int(input("Inserisci n: > "))
k = int(input("Inserisci K: > "))

def coefficiente_binomiale(n, k):
    s = n-k
    risultato = (fattoriale(n)) / (((fattoriale(k)) * (fattoriale(s))))
    return risultato

print(coefficiente_binomiale(n,k))

# SOLUZIONE SUGGERITA IN CLASSE: #############
n = int(input("Dammi n :"))
k = int(input("Dammi 0<= k <=n :"))
nfatt = 1
kfatt = 1
nmenoK = n- k
nkfatt = 1
for i in range(2,n+1):
    nfatt = nfatt * i
for i in range(2,k+1):
    kfatt = kfatt * i
for i in range(2,nmenoK+1):
    nkfatt = nkfatt * i

print("c(n,k) = ", nfatt/(kfatt *nkfatt))

#Esempio -- la funzione fattoriale 04.10.2022
def fattoriale(a):
    fatt = 1
    for i in range(2,a+1):
        fatt = fatt * i
    return fatt

n = int(input("Dammi n :"))
k = int(input("Dammi 0<= k <=n :"))
nfatt = 1
kfatt = 1
nkfatt = 1
nfatt = fattoriale(n)
kfatt = fattoriale(k)
nkfatt= fattoriale(n-k)

print("c(n,k) = ", nfatt/(kfatt *nkfatt))