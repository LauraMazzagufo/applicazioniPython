def fai():
    print("Faccio qualcosa")

def fai_n(funzione, n):
    if n<=0:
        print()
    else:
        funzione()
        n -= 1

fai_n(fai, 3)