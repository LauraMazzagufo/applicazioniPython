def conta(parola, l):
    conta = 0
    for lettera in parola:
        if lettera == l:
            conta = conta + 1
    return conta

print(conta("gatto", "t"))