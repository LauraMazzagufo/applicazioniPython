def crea_triangolo():
    lato1= int(input("Inserisci il lato 1: \n"))
    lato2= int(input("Inserisci il lato 2: \n"))
    lato3= int(input("Inserisci il lato 3: \n"))
    triangolo(lato1, lato2, lato3)

def triangolo(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("Sì")
    else:
        print("no")

crea_triangolo()