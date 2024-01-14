# Esericizi: http://www.andreamarino.it/python/thinkcspy/PythonTurtle/Exercises.html

# Scrivere un programma che stampa We like Python's turtles! 1000 volte.
for i in range(1000):
    print("We like Python's turtles!")


# Scrivere un programma che usa un ciclo for per stampare
# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March
# etc ...
year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
        "December"]

for month in year:
    print("One of the months of the year is ", month)


# Assumiamo che abbiamo una lista di numeri 12, 10, 32, 3, 66, 17, 42, 99, 20
# Scrivere un ciclo che stampa ogni numero su una nuova riga.
# Scrivere un ciclo for che stampa ogni numero e il suo quadrato su una nuova linea.

lista = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in lista:
    print(i)
print()
for i in lista:
    print(i, "\t", i*i)


# Scrivere un programma che stampa tutte le possibili coppie di numeri tra 5 e 10.
for i in range(5, 11):
    for j in range(5, 11):
        print(i, " - ", j)
print()
print()

# OPPURE in questo modo non si ripetono le coppie già elencate nell'ordine inverso:
for i in range(5, 11):
    for j in range(i, 11):
        print(i, " - ", j)


# Scrivere un programma che stampa tutte le possibili triple di numeri x,y,z dove x varia tre 5 e 10, y varia tra 6 e
# 12, z varia tra 7 e 13.
for x in range(5, 11):
    for y in range(6, 13):
        for z in range(7, 14):
            print(x, "\t", y, "\t", z)


# Scrivere un programma che stampa tutte le possibili coppie di numeri x,y con x,y tra 0 e 10, dove x è pari e y è
# dispari.
for x in range(0, 11, 2):
    for y in range(1, 10, 2):
        print(x, "\t", y)
