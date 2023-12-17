def prima(parola):
    return parola[0]

def ultima(parola):
    return parola[-1]

def mezzo(parola):
    return parola[1:-1]

print(prima("cavolo"))
print(mezzo("ok"))
print(ultima("cavolo"))
print(mezzo(""))
print(mezzo("cavolo"))

def palindromo(stringa):
    if len(stringa) <= 1:
        return True
    if prima(stringa) != ultima(stringa):
        return False
    else:
        stringa = palindromo(mezzo(stringa))
        return stringa

print(palindromo("ciao"))
print(palindromo("i"))
print(palindromo("bob"))
print(palindromo("radar"))





