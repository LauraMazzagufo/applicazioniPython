# Scrivete una funzione di nome stampa_tempo che accetti un oggetto Tempo come
# argomento e ne stampi il risultato nel formato ore:minuti:secondi. Suggerimento: la sequenza
# di formato '%.2d' stampa un intero usando almeno due cifre, compreso uno zero iniziale dove
# necessario.

class Tempo(object):
    """
    Rappresenta un momento del tempo
    attributi: ore, minuti, secondi
    """

t1 = Tempo()

t1.ore = 11
t1.minuti = 59
t1.secondi = 0

def stampa_tempo(orario):
    x = orario.ore
    y = orario.minuti
    z = orario.secondi
    print('%.2d:%.2d:%.2d' % (x, y, z))


stampa_tempo(t1)
