# Assegna ad una varibile una stringa (usando tre apici o virgolette) che contiene il testo “Lorem ipsum ecc.”
# Scrivere una funzione che conta il numero di caratteri alfabetici nel testo e tiene traccia di quante lettere ‘e’
# ci sono:

stringa = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
          dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
          ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
          fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
          mollit anim id est laborum"""


def conta_cerca():
    contatore = 0
    for ix in stringa: # in questo modo però conta anche gli spazi e la punteggiatura
        if ix == "e":
            contatore += 1
    print(f"Il tuo testo contiene {len(stringa)} caratteri alfabetici, di cui {contatore} sono 'e'.")


conta_cerca()

# soluzione:
def count(p):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or achar in ups:
            totalChars = totalChars + 1
            if achar == 'e':
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    percent_with_e = round(percent_with_e, 2)
    print("Your text contains", totalChars, "alphabetic characters of which", numberOfe, "(", percent_with_e, "%)", "are 'e'.")


p = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum'''

count(p)



# Scrivere una funzione che ritorna il numero di cifre in un intero.

def n_cifre(n):
    numero = str(n)
    #contatore = 0
    #for i in numero:
        #contatore += 1
    #return contatore
    return len(numero)

print(n_cifre(455))


# Scrivere una funzione che inverte il suo argomento.

from testMy import testEqual

def reverse(astring):
    if astring == "":
        return ""
    return reverse(astring[1:len(astring)]) + astring[0]

# oppure:
def reverse2(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed


testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""), "")


# Scrivere una funzione specchio che ad esempio fa trasforma “Python” in “PythonnohtyP”.

def mirror(astring):
    if astring == "":
        return ""
    return astring + reverse(astring)

print(mirror("Python"))
testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')


#Scrivere una funzione che rimuove tutte le occorrenze di una data lettera da una stringa.

from testMy import testEqual

def remove_letter(theLetter, theString):
    newString = theString.replace(theLetter, "")
    # non serve fare un ciclo, lo fa il metodo della libreria
    #i = 0
    #newString = theString
    #while i < len(theString):
    #    if theString[i] == theLetter:
    #        newString = theString.replace(theLetter, "")
    #    i += 1
    return newString

#oppure con ricorsione:
def remove_letter2(theLetter, theString):
    if theString == "":
        return ""
    if theString[0]==theLetter:
        return remove_letter(theLetter,theString[1:])
    return theString[0] + remove_letter(theLetter,theString[1:])

print(remove_letter("a", "apple"))

testEqual(remove_letter('a', 'apple'), 'pple')
testEqual(remove_letter('a', 'banana'), 'bnn')
testEqual(remove_letter('z', 'banana'), 'banana')


# Scrivere una funzione che riconosce le palindrome. (Suggerimento: possiamo usare reverse!).

from testMy import testEqual

def is_palindrome(myStr):
    #if myStr == reverse(myStr):
    #    return True
    #else:
    #    return False
    # basta scrivere:
    return myStr in reverse(myStr)

testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)


# Scrivere una funzione che conta quante volte una sottostringa data occorre in una stringa. Si noti che le stringhe
# possono essere sovrapposte, motivo per il quale count('ana', 'banana') fa 2.

from testMy import testEqual

def count(substr,theStr):
    """Conta le occorrenze anche sovrapposte -- confrontare il metodo count"""
    if len(substr) > len(theStr):
        return 0
    if substr == theStr[:len(substr)]:
        return 1 + count(substr,theStr[1:])
    return count(substr,theStr[1:])

testEqual(count('is', 'Mississippi'), 2)
testEqual(count('an', 'banana'), 2)
testEqual(count('ana', 'banana'), 2)
testEqual(count('nana', 'banana'), 1)
testEqual(count('nanan', 'banana'), 0)
testEqual(count('aaa', 'aaaaaa'), 4)


# Scrivere una funzione che rimuove la prima occorrenza di una stringa da un’altra stringa.

from testMy import testEqual

def remove(substr,theStr):
    newString = theStr.replace(substr, "", 1) # solo la prima occorrenza
    return newString

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')



# Scrivere una funzione che rimuove tutte le occorrenze di una stringa da un’altra stringa.

from testMy import testEqual


def remove(substr,theStr):
    newString = theStr.replace(substr, "") # solo la prima occorrenza
    return newString

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')


# Scrivere una funzione chiamata removeDups che prende una stringa e restituisce una nuova stringa contenente gli
# stessi caratteri della stringa di partenza una e una sola volta. Ciascun carattere deve comparire nell’ordine in
# cui compare la sua prima occorrenza nella stringa di partenza.


def removeDups(astring):
    newString = ""
    for c in astring:
        if newString.count(c) == 0:
            newString = newString + c
    return newString


print(removeDups("mississippi"))   #should print misp