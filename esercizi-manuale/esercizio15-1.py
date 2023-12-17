import math
class Punto(object):
    """ Rappresenta un punto """

nuovo_punto = Punto()
print(nuovo_punto)

nuovo_punto.x = 3.0
nuovo_punto.y = 4.0

x = nuovo_punto.x
y = nuovo_punto.y

print(x)
print(y)

# Scrivete una funzione di nome distanza_tra_punti che riceva due Punti come
# argomenti e ne restituisca la distanza.
class Punto(object):
    """
        Rappresenta un punto nello spazio
        attributi: coordinate x e y
    """

# istanziazione degli oggetti punto
p1 = Punto()
p2 = Punto()

# attributi dei punti
p1.x = 0
p1.y = 0
p2.x = 5
p2.y = 5

p1x = p1.x
p1y = p1.y
p2x = p2.x
p2y = p2.y


def distanza_tra_punti(punto1, punto2):
    distanza = math.sqrt((p2x - p1x) ** 2 + (p2y - p1y) ** 2)
    print(distanza)


distanza_tra_punti(p1, p2)

# soluzione del manuale:
def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

print(distance_between_points(p1, p2))

