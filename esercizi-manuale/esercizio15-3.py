import copy
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


# Scrivete una versione di sposta_rettangolo che crei e restituisca un nuovo
# Rettangolo anziché modificare quello di origine.

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

def sposta_nuovo_rettangolo(rettangolo, dx, dy):
    rett2 = copy.deepcopy(rettangolo)
    sposta_rettangolo(rett2, dx, dy)
    return rett2
