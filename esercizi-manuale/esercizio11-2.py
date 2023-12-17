# Usate get per scrivere istogramma in modo più compatto. Dovreste riuscire a fare a meno
# dell’istruzione if.
#def istogramma(s):
#    d = dict()
#    for c in s:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#    return d

#h = istogramma("brontosauro")
#print(h)

def istogramma(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = istogramma("brontosauro")
print(h)
