# Quanto valgono le seguenti espressioni?
#
# 3 == 3        --> True
# 3 != 3        --> False
# 3 >= 4        --> False
# not (3 < 4)   --> False


# Qual’è il contrario di queste condizioni? Non è possibile usare il not.
#
# a > b                     --> a <= b
# a >= b                    --> a < b
# a >= 18  and  day == 3    --> a < 18 OR day != 3
# a >= 18  or  day != 3     --> a < 18 AND day == 3


# Scrivere una funzione che dato un punteggio, ritorna una stringa — il voto del punteggio — seguendo questo schema:
# Punteggio	Voto
# >= 90	    A
# [80-90)	B
# [70-80)	C
# [60-70)	D
# < 60	    F
# La parentesi quadrata vuol dire estremo incluso, la tonda estremo escluso. Provare la
# funzione stampando il voto per diversi punteggi.

def voto(n):
    if n >= 90:
        return "A"
    elif 80 <= n < 90:
        return "B"
    elif 70 <= n < 80:
        return "C"
    elif 60 <= n < 70:
        return "D"
    else:
        return "F"

print(f"Il voto 88 corrisponde a una {voto(88)}.")
print(f"Il voto 97 corrisponde a una {voto(97)}.")
print(f"Il voto 59 corrisponde a una {voto(59)}.")
print(f"Il voto 72 corrisponde a una {voto(72)}.")


# Scrivere una funzione findHypot che, data la lunghezza dei due cateti ritorna la lunghezza dell’ipotenusa. (
# Suggerimento: usare x ** 0.5 per ritornare la radice quadrata, oppure sqrt del modulo math)
import math

def provaUguali(x, y):
    if x == y:
        print("Pass")
    else:
        print("Not Passing")

def findHypot(a,b):
    return math.sqrt((a*a)+(b*b))

provaUguali(findHypot(12.0, 5.0), 13.0)
provaUguali(findHypot(14.0, 48.0), 50.0)
provaUguali(findHypot(21.0, 72.0), 75.0)
provaUguali(findHypot(1, 1.73205), 1.999999)


# Scrivere una funzione chiamata is_even(n) che prende un intero come argomento e ritorna True se l’argomento è un
# numero pari and False se è dispari odd.

def is_even(n):
    return n % 2 == 0


provaUguali(is_even(10), True)
provaUguali(is_even(5), False)
provaUguali(is_even(1), False)
provaUguali(is_even(0), True)


# Scrivere la funzione is_odd(n) che ritorna True quando n is è dispari e False altrimenti.

def is_odd(n):
    return n % 2 != 0


provaUguali(is_odd(10), False)
provaUguali(is_odd(5), True)
provaUguali(is_odd(1), True)
provaUguali(is_odd(0), False)


# Modificare is_odd in modo che usi la chiamata a is_even.

def is_odd(n):
    return not is_even(n)

print()
provaUguali(is_odd(10), False)
provaUguali(is_odd(5), True)
provaUguali(is_odd(1), True)
provaUguali(is_odd(0), False)


# es. 8 --> Scrivere la funzione is_rightangled che, data la lunghezza di tre lati di un triangolo, determina se il
# triangolo è rettangolo. Assumiamo che il terzo argomento è sempre il lato più lungo. La funzione deve ritornare
# True se il triangolo è rettangolo e False altrimenti.
# Suggerimento: l’aritmetica dei numeri in floating point non è sempre accurata per cui non è sicuro controllare
# l’uguaglianza tra due numeri con ==. Piuttosto, è meglio controllare se x è abbastanza vicino a y, come segue:
# if  abs(x - y) < 0.001:      # if x is approximately equal to y

def is_rightangled(a, b, c):
    y = a*a + b*b
    x = c*c
    if abs(x - y) < 0.001:
        return True
    else:
        return False


provaUguali(is_rightangled(1.5, 2.0, 2.5), True)
provaUguali(is_rightangled(4.0, 8.0, 16.0), False)
provaUguali(is_rightangled(4.1, 8.2, 9.1678787077), True)
provaUguali(is_rightangled(4.1, 8.2, 9.16787), True)
provaUguali(is_rightangled(4.1, 8.2, 9.168), False)
provaUguali(is_rightangled(0.5, 0.4, 0.64031), True)


# Estendere il programma sopra in modo che i lati possano essere dati in qualsiasi ordine.

def is_rightangled(a, b, c):
    massimo = max(a, b, c)
    x = massimo * massimo
    y = a*a + b*b + c*c - x
    if abs(x - y) < 0.001:
        return True
    else:
        return False

# def is_rightangled2(a, b, c):
#     is_rightangled = False
#
#     if a > b and a > c:
#         is_rightangled = abs(b**2 + c**2 - a**2) < 0.001
#     elif b > a and b > c:
#         is_rightangled = abs(a**2 + c**2 - b**2) < 0.001
#     else:
#         is_rightangled = abs(a**2 + b**2 - c**2) < 0.001
#     return is_rightangled

provaUguali(is_rightangled(1.5, 2.0, 2.5), True)
provaUguali(is_rightangled(16.0, 4.0, 8.0), False)
provaUguali(is_rightangled(4.1, 9.1678787077, 8.2), True)
provaUguali(is_rightangled(9.16787, 4.1, 8.2), True)
provaUguali(is_rightangled(4.1, 8.2, 9.168), False)
provaUguali(is_rightangled(0.5, 0.64031, 0.4), True)


# Scrivere la funzione is_prime(n) che ritorna True quando n è primo e False altrimenti.
def isPrime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

print(isPrime(15))

# Un anno è detto bisestile se è divisibile per 4 a meno che non sia un secolo che non è divisibile per 400.
# Scrivere una funzione che prende un anno come parametro e ritorna True se l’anno è bisestile, False altrimenti.

def isLeap(year):
    isBisestile = False
    if year % 100 == 0:
        if year % 400 == 0:
            isBisestile = True
    elif year % 4 == 0:
        isBisestile = True
    return isBisestile

provaUguali(isLeap(1944), True)
provaUguali(isLeap(2011), False)
provaUguali(isLeap(1986), False)
provaUguali(isLeap(1800), False)
provaUguali(isLeap(1900), False)
provaUguali(isLeap(2000), True)
provaUguali(isLeap(2056), True)

# Implementare il calcolo della Pasqua.
# L’algoritmo seguente calcola la data della Pasqua dal 1900 e il 2099.
# Chiedere all’utente di inserire un anno. Calcolare quanto segue:
#
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateofeaster = 22 + d + e
# Nota: L’algoritmo può ritornare una data in Aprile. Inoltre, nel caso in cui l’anno è uno degli anni speciali
# (1954, 1981, 2049, or 2076), bisogna sottrarre 7 dalla data.
# Your program should print an error message if the user provides a date that is out of range.

def data_Pasqua():
    year = int(input("Inserisci un anno compreso tra il 1900 e il 2099: > "))
    if year < 1900 or year > 2099:
        print("Errore. Anno non valido")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateofeaster = 22 + d + e
        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            dateofeaster -= 7
        if dateofeaster > 31:
            dateofeaster -= 31
            print(f"Nell'anno {year} la Pasqua sarà il giorno {dateofeaster} Aprile.")
        else:
            print(f"Nell'anno {year} la Pasqua sarà il giorno {dateofeaster} Marzo.")

data_Pasqua()

# Generare un numero casuale intero nell’intervallo [25,30] o [35,55)
# in modo che ogni numero tra quelli estraibili abbia la stessa probabilità di uscita.


# Generare un numero casuale reale nell’intervallo [25,30] o [35,55)
# in modo che ogni numero tra quelli estraibili abbia la stessa probabilità di uscita.
