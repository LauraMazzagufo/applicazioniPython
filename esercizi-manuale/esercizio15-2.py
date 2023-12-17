class Punto(object):
    """
        Rappresenta un punto nello spazio
        attributi: coordinate x e y
    """

# istanziazione degli oggetti punto
p1 = Punto()

# attributi dei punti
p1.x = 0
p1.y = 0


p1x = p1.x
p1y = p1.y


# Scrivete una funzione di nome sposta_rettangolo che prenda come parametri
# un Rettangolo e due valori dx e dy. La funzione deve spostare il rettangolo nel piano, aggiungendo
# dx alla coordinata x di angolo, e aggiungendo dy alla coordinata y di angolo.

class Rettangolo(object):
    """
        Descrive un rettangolo
        attributi: angolo, larghezza, altezza
    """

rett1 = Rettangolo()
rett1.h = 2
rett1.l = 3
rett1.a = p1

def sposta_rettangolo(rettangolo, dx, dy):
    rettangolo.a.x += dx
    rettangolo.a.y += dy

sposta_rettangolo(rett1, 6, 8)

def stampa_punto(p):
    print('(%g, %g)' % (p.x, p.y))

# per controllare che effettivamente le coordinate siano cambiate
stampa_punto(p1)