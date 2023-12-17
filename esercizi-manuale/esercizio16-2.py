# Scrivete una funzione booleana viene_dopo che riceva come argomenti due oggetti
# Tempo, t1 e t2, e restituisca True se t1 è temporalmente successivo a t2 e False in caso contrario.


class Tempo(object):
    """
    Rappresenta un momento del tempo
    attributi: ore, minuti, secondi
    """

t1 = Tempo()
t2 = Tempo()

t1.ore = 12
t1.minuti = 59
t1.secondi = 0


t2.ore = 12
t2.minuti = 49
t2.secondi = 10

def viene_dopo(orario1, orario2):
    if orario1.ore > orario2.ore:
        return True
    elif orario1.ore == orario2.ore:
        if orario1.minuti > orario2.minuti:
            return True
        elif orario1.minuti == orario2.minuti:
            if orario1.secondi > orario2.secondi:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(viene_dopo(t1, t2))