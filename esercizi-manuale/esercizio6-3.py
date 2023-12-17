# Scrivete una funzione compreso_tra(x, y, z) che restituisca True se x<=y<=z o False altrimenti

def compreso_tra(x, y, z):
    if (x <= y) and (y <= z):
        return True
    else:
        return False


print(compreso_tra(6, 4, 5))
